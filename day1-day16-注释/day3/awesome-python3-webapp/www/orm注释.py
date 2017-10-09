#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
    选择MySQL(作为网站的'后台数据库')，能快速查询和保存数据
    执行'SQL语句进行操作'，并将常用的SELECT、INSERT等语句进行函数封装
    在异步框架的基础上，采用aiomysql(作为数据库的异步IO驱动)
    将数据库中表的操作，'映射'成一个类的操作，也就是数据库表的一行映射成一个对象(ORM)
    整个ORM也是异步操作
    预备知识：Python协程和异步IO(async 和 await的使用)、SQL数据库操作、元类、面向对象知识、Python语法
    # -*- -----  思路  ----- -*-
    如定义一个user类，这个类和数据库中的表User构成映射关系，二者应该关联起来，user类可以操作表User表
    通过Field类将user类的属性映射到User表的列中，其中每一列的字段又有自己的一些属性，包括数据类型，列名，主键和默认值等'''

__author__ = 'Point'
	
import asyncio
import logging
import aiomysql 
#
    # 引入 asyncio, logging，aiomysql 库
    # asyncio-异步IO, logging-日志，aiomysql-异步IO+MySQL
    # 在异步框架的基础上，采用aiomysql作为数据库的异步IO驱动
    # aiomysql是Mysql的python异步驱动程序，操作数据库要用到

# 这个函数的作用是输出信息，让你知道这个时间点程序在做什么
def log(sql, args=()):
    # 定义 log 函数，sql为 必选参数，args为默认参数 （参数类型是元组）
    # 参数 sql 表示要传入的 sql 语句
    # 参数 args 表示 sql 语句中 对应的 values 值，用元组表示；使用带参数的SQL，而不是自己拼接SQL字符串，这样可以防止SQL注入攻击
    # 该函数用于记录或输出执行的SQL语句信息
    logging.info('SQL: %s' % sql) 

# 创建全局连接池，每个HTTP请求都可以从连接池中直接获取数据库连接，不必频繁地打开和关闭数据库连接，而是尽量复用
async def create_pool(loop, **kw): 
    #
                    # 定义 create_pool函数，loop为 必选参数，**kw为关键字参数
                    # 参数 loop 表示一个异步消息循环，后面在 app.py 中会通过 loop = loop 方式 赋值， loop = asyncio.get_event_loop()
                    # **kw参数包含所有连接需要用到的关键字参数，下面代码中 user，password，db需要使用关键词参数传入值，同上，会在app.py 中调用时赋值
                    
                    # 这个函数将来会在后面 app.py中的 init函数中引用
    logging.info('create database connection pool...') 
    global __pool 
                    # 全局私有变量__pool用于存储整个连接池      
                    # 用global关键字声明变量__pool为一个全局变量，如果不加声明，变量__pool 就不能被该模块中的其他函数引用
                    # __xx 表示私有变量，只能在该模块中使用，外部模块不应该访问该变量
    __pool = await aiomysql.create_pool(
                        # aiomysql.create_pool(...) 在 aiomysql.pool.py 模块中被定义，格式为：
                        # create_pool(minsize=1, maxsize=10, echo=False, loop=None, **kwargs)
                        # 函数内部对 loop赋默认值为 loop = asyncio.get_event_loop()

                        # pool类实例 利用with语句调用和处理其属性 _cond，类实例pool的_cond 属性值为 asyncio.Condition(loop=loop)
                        # asyncio.Condition(loop=loop) 首先被with语句执行打开该对象的操作，该对象是一个类实例，存在于asyncio.locks.py模块中
                        # 接着with语句内部调用 pool类实例的 _fill_free_pool(override_min) 方法 
                        # 该方法异步调用 aiomysql.connection.py 中的connect函数，该函数接着调用 _connect函数
                        # _connect 函数 内部创建 Connection类实例赋值给 conn变量，该实例有_connect(), cursor(), 等方法实现对MySQL数据库进行操作
                        # conn实例调用实例方法 conn._connect()，实现数据库连接
                        # 最后_connect函数返回 conn，conn为 Connection类的实例
                        # 最后 connect函数 将 Connection类的实例conn 赋值给 coro，返回一个Connection类的实例，同时是一个上下文管理对象
                        # pool类实例的 _fill_free_pool(override_min) 方法 将上述返回值赋值给 conn
                        # _create_pool函数 --->create_pool函数  --> __pool   

                        # __pool.get() 的结果是Connection类的实例，同时是一个上下文管理对象，该实例有_connect(), cursor(), 等方法实现对MySQL数据库进行操作

                        # 调用一个协程来创建全局连接池
                        # 创建数据库连接需要用到的一些参数，从**kw（关键字参数）中取出
                        # kw.get的作用是，当没有传入参数时，参数默认值就是get函数的第二项
                        # kw[key] 即从kw中取出 键key 对应的值，该值没有默认值，所以kw必须传入该参数和对应的值
        host=kw.get('host', 'localhost'), 
                        # dict的get方法，如果key不存在，可以返回None，或者自己指定的value，这里指定'localhost'，默认本机IP
                        # host　主机  MySQL server IP address or name
                        # 数据库服务器位置，默认设在本地
        port=kw.get('port', 3306),
                        # dict的get方法，如果key不存在，可以返回None，或者自己指定的value，这里指定3306，默认端口号3306
                        # port 端口号  MySQL server TCP/IP port       
                        # mysql的端口，默认设为3306 
        user=kw['user'],
                        # 获得键'user'的值，赋值给user变量
                        # user  User used while connecting to MySQL
                        # 登陆用户名，通过关键词参数传进来
        password=kw['password'],
                        # 获得键'password'的值，赋值给password变量      
                        # 登陆密码，通过关键词参数传进来
        db=kw['db'],
                        # 获得键'db'的值，赋值给db变量  
                        # db  Current database name.       
                        # 当前数据库名，通过关键词参数传进来
        charset=kw.get('charset', 'utf8'),
                        # dict的get方法，如果key不存在，可以返回None，或者自己指定的value，这里指定utf8，默认字符集charset=utf8
                        # charset  Returns the character set for current connection.
                        # 在MySQL数据库中只能使用“utf8”, 不能写成utf8的其他形式       
        autocommit=kw.get('autocommit', True),
                        # dict的get方法，如果key不存在，可以返回None，或者自己指定的value，这里指定True，默认autocommit=True
                        # autocommit(self, value)  Enable/disable autocommit mode for current MySQL session.    
                        # 自动提交模式，设置默认开启   
        maxsize=kw.get('maxsize', 10), # 默认最大连接数为10，即允许用户同时连接该数据库的最大连接数量为10 ，超过会报错，MySQL服务器瘫痪    
        minsize=kw.get('minsize', 1), # 最小连接数，默认设为1，这样可以保证任何时候都会有一个数据库连接      
        loop=loop 
                    # 接收一个event_loop实例 loop = asyncio.get_event_loop()
                    # 传递消息循环对象，用于异步执行
    )

# =================================SQL处理函数区====================================
# select和execute方法是实现其他Model类中SQL语句 经常要用到的方法         

# 定义select函数，封装SQL SELECT 操作
async def select(sql, args, size=None): 
    #
                    # 数据库的select语句对应该select方法 
                    # 定义select函数，封装SQL SELECT语句，调用时传入对应参数
                    # sql参数即为sql语句，后面调用时会传入一个字符串
                    # 如 sql='select `id` `names` `password` `email` from `User` where where条件 order by orderBy条件 limit '?' '?''
                    # args表示要搜索的参数值，后面调用时会会传入一个列表
                    # 如 args = [3, 2]
                    # size用于指定最大的查询数量，不指定将返回所有查询结果   
    log(sql, args) # 调用log函数，记录执行的SQL语句信息 
    global __pool 
    #
                        # 调用全局变量 __pool，__pool作为字典存储了整个连接池  
                        # 声明全局变量，这样才能引用create_pool函数创建的__pool变量
                         # __pool 是aiomysql.connection.py模块 Connection类的实例，同时是一个上下文管理对象，该实例有_connect(), cursor(), 等方法实现对MySQL数据库进行操作
    async with __pool.get() as conn: 
    #
                # __pool.get() 的结果是Connection类的实例，同时是一个上下文管理对象，该实例有_connect(), cursor(), 等方法实现对MySQL数据库进行操作
                # 从连接池中获得一个数据库连接，相当于在MySQL数据库中打开一个数据库操作
                # 如
                # 用with语句可以封装清理（关闭conn）和处理异常工作
                # with 语句实现上下文管理，替代try-finally语句
                # 调用字典的get方法，赋值给变量conn
        async with conn.cursor(aiomysql.DictCursor) as cur: 
        #
                # aiomysql.connection.py模块 Connection类的实例conn具有 cursor 方法
                # 调用该方法获得 pymysql.cusors.py 中Cursor类的实例 赋值给 cur
                # This is the object you use to interact with the database.

                # cursor 是用来在数据库中执行命令的方法    
                # DictCursor is a cursor which returns results as a dictionary
                # 等待连接对象返回DictCursor，可以通过dict的方式获取数据库对象，需要通过游标对象执行SQL
            await cur.execute(sql.replace('?', '%s'), args or ())
            #
                # cur 是 aiomysql.curcurs.py 中 Cursor类的实例
                # 具有 execute(self, query, args=None) 方法 

                # 若 args = [3, 2]
                # 若 sql='select `id` `names` `password` `email` from `User` where where条件 order by orderBy条件 limit '?' '?''
                # 则 经replace处理后为 # sql2='select `id` `names` `password` `email` from `User` where where条件 order by orderBy条件 limit '%s' '%s'' 
                # 则在MySQL数据库中的执行语句为：
                # # select `id` `names` `password` `email` from `User` where where条件 order by orderBy条件 limit '%s' '%s'  [3, 2]

                # 异步执行MySQL数据库的execute方法，执行单条sql语句，传入两个参数，一个为sql语句，另一个为args 或 ()
                # sql参数和args参数在调用select函数时会传入
                # MySQL的execute方法封装在 模块 aiomysql 中，调用该方法相当于在MySQL数据库中执行一条sql语句
                # 所有args都通过repalce方法把sql语句的占位符？替换成 %s，因为MySQL数据库的占位符是 %s
                # 执行SQL语句，并在MySQL数据库中返回一个查询结果

                # execute(self, query, args) 执行单条语句
                # executemany(self, query,args) 执行多条语句
                # Executes the given operation 
                # Executes the given operation substituting any markers with the given parameters.
            if size: # 如果制定了查询数量，则查询制定数量的结果，如果不指定则查询所有结果
                rs = await cur.fetchmany(size)
                #
                            # fetchmany(self, size=None) 函数 根据指定的size，从数据库返回size条查询结果
                            # fetchmany(self, size=None)
                            # Returns the next set of rows of a query result, returning a list of tuples. When no more 
                            # rows are available, it returns an empty list.
            else:    # 如果不指定则查询所有结果
                rs = await cur.fetchall()
                #
	                # 返回所有查询结果 
	                # fetchmany(self, size=None)
	                # Returns the next set of rows of a query result, returning a list of tuples. When no more 
	                # rows are available, it returns an empty list.  
        logging.info('rows returned: %s' % len(rs))
        # await conn.close() # 异步关闭连接池
        return rs
        # 返回结果集
# 定义execute函数，封装SQL INSERT, UPDATE, DELETE 操作
async def execute(sql, args, autocommit=True):
    #
                    # 定义一个execute函数，参数为sql, args, autocommit=True
                    # 封装 INSERT, UPDATE, DELETE 操作
                    # 语句操作参数一样，所以定义一个通用的执行函数
                    # 返回操作影响的行号，不返回结果集 
    log(sql) 
    async with __pool.get() as conn:
    #
    		# with 语句实现上下文管理，替代try-finally语句
    		 # __pool.get() 的结果是Connection类的实例，同时是一个上下文管理对象，该实例有_connect(), cursor(), 等方法实现对MySQL数据库进行操作
        if not autocommit:
        #
        		# 若 autocommit 为False，则手动开启事务
                        # begin(self)  one of methods in class Connection(builtins.object)
            	# Begin transaction.
            await conn.begin()
        try:
            async with conn.cursor(aiomysql.DictCursor) as cur:
                            # aiomysql.connection.py模块 Connection类的实例conn具有 cursor 方法
                            # 调用该方法获得 pymysql.cusors.py 中Cursor类的实例 赋值给 cur
                            # This is the object you use to interact with the database.
                await cur.execute(sql.replace('?', '%s'), args) 
                # 效果相当于在MySQL数据库中执行一条语句
                # 如 create table test(id int, info varchar(20))
                affected = cur.rowcount
                # 返回受影响的行数
            if not autocommit:
                await conn.commit() 
                            # 请注意如果autocommit 值不是True， 则一定要有conn.commit()这句来提交事务，要不然不能真正的执行该操作
                            # Commit changes to stable storage.
        except BaseException as e:
            if not autocommit:                  
                await conn.rollback() # 发生错误则回滚到未产生操作前的状态
                #
                        	# rollback(self)  one of methods in class Connection(builtins.object)
                        	# Roll back the current transaction.   
            raise # raise不带参数，则把此处的错误往上抛;为了方便理解还是建议加e吧，即 raise e
        return affected

# 这个函数在元类中被引用，作用是创建一定数量的占位符       
def create_args_string(num):
	# 根据输入的参数生成占位符列表
    L = []
    for n in range(num):
        L.append('?')   
        #比如说num=3，那L就是['?','?','?']，通过下面这句代码返回一个字符串'?,?,?'
    return ', '.join(L) # 以','为分隔符，将列表合成字符串

# =================================Field定义域区=====================================
# 父定义域，可以被其他定义域继承
class Field(object): # 定义 Field类
    def __init__(self, name, column_type, primary_key, default):
    #
                    # 定义域的初始化，包括属性（列）名，属性（列）的类型，主键，默认值
                    # 实例化属性，通过 __init__ 方法给实例绑定属性; 在创建实例的时候，不能传入
                    # 空的参数了，必须传入与__init__方法匹配的参数, 但self不需要传
                    # Python解释器自己会把实例变量传进去   
        self.name = name # name属性绑定
        self.column_type = column_type
        self.primary_key = primary_key
        self.default = default # 如果存在默认值，在getOrDefault()中会被用到

    # 定制输出信息为 <实例类名, 实例属性column_type（列）值 : 实例属性（列）name值>
    def __str__(self):
    #
                    # __str__方法用于将值转化为适于人阅读的形式，而且方便看出实例内部重要的数据
                    # 当打印实例时，会调用__str__方法，显示 return语句返回的信息
                    # 返回结果   <实例类名, 实例属性column_type（列）值 : 实例属性（列）name值>
                    # 如 <IntegerField, 'bigint':'id'>
        return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type, self.name)

# 定义不同类型的衍生Field
	# 表的不同列的字段的类型不一样
	# 继承Field 定义数据库字符串类型
class StringField(Field): 
    # 定义 StringField类，父类为Field, 继承父类所有功能
    def __init__(self, name=None, primary_key=False, default=None, ddl='(varchar100)'):
    #
                        # 实例化属性，通过 __init__ 方法给实例绑定属性; 在创建实例的时候，不能传入
                        # 空的参数了，必须传入与__init__方法匹配的参数, 但self不需要传
                        # Python解释器自己会把实例变量传进去 
                        # name 默认为 None 
                        # String一般不作为主键，所以默认False
                        # default 默认为 None
                        # DDL是数据定义语言(data definition languages)，varchar100)意思是可变字符串，长度为100    
                        # 和char相对应，char是固定长度，字符串长度不够会自动补齐，varchar则是多长就是多长，但最长不能超过规定长度
        super().__init__(name, ddl, primary_key, default)
        #
                    # 执行父类实例化函数，column_type属性绑定值为'varchar(100)' 
                    # name=None
                    # column_type=ddl='(varchar100)'
                    # primary_key=False
                    # default=None
class BooleanField(Field):
    def __init__(self, name=None, default=False):
        super().__init__(name, 'boolean', False, default)
        #
                    # name=None
                    # column_type= 'boolean'
                    # primary_key=False
                    # default=False
class IntegerField(Field):
    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'bigint', primary_key, default)
        #
                    # name=None
                    # column_type= 'bigint'
                    # primary_key=False
                    # default=0       
class FloatField(Field):
    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, 'real', primary_key, default)
        #
                    # name=None
                    # column_type= 'real'
                    # primary_key=False
                    # default=0.0   
class TextField(Field):
    def __init__(self, name=None, default=None):
        super().__init__(name, 'text', False, default)
        #
                    # name=None
                    # column_type= 'text'
                    # primary_key=False
                    # default=None

# =====================================Model元类区==========================================
# -*-定义Model的元类
    # 该元类主要使得Model基类具备以下功能:
    # 1.任何继承自Model的类（比如User），会自动通过ModelMetaclass扫描映射关系
    # 并存储到自身的类属性如__table__、__mappings__中
    # 2.创建了一些默认的SQL语句

	# 所有的元类都继承自type
	# 先定义metaclass，就可以创建类，最后创建实例   metaclass允许你创建类或者修改类
	# ModelMetaclass元类定义了所有Model基类(继承ModelMetaclass)的子类实现的操作	

	# -*-ModelMetaclass的工作主要是为一个数据库表映射成一个封装的类做准备：
	# ***读取具体子类(user)的映射信息
	# 创造类的时候，排除对Model类的修改
	# 在当前类中查找所有的类属性(attrs)，如果找到Field属性，就将其保存到__mappings__的dict中，同时从类属性中
	# 删除Field(防止实例属性遮住类的同名属性)
	# 将数据库表名保存到__table__中	

	# 完成这些工作就可以在Model中定义各种数据库的操作方法
class ModelMetaclass(type):
    #
                # __new__控制__init__的执行，所以在其执行之前，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
                # cls: 当前准备创建的类的对象。此参数在实例化时由Python解释器自动提供(例如下文的User和Model)，相当于给类实例 self，只是这里是元类实例 类 cls
                # name：当前准备创建的类的名称
                # bases：当前准备继承的父类的集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
                # attrs：当前准备创建类的方法集合
                # 实例化类
    def __new__(cls, name, bases, attrs):
        if name=='Model': # 如果待创建类的名字为 'Model'，返回并退出该创建类的过程，不对类名为Model的类进行修改
            return type.__new__(cls, name, bases, attrs)

        tableName = attrs.get('__table__', None) or name
                
                # 如果类属性中定义了__table__属性并有相应值，则使用该值，否则直接使用类名赋值给 tableName
        logging.info('found model: %s (table: %s)' % (name, tableName))
                # 记录信息 'Found model: 类名 (表名)'
                # 排除Model后，这里只剩 Model的子类 如User 
                # 即打印信息 Found model:User (table: User)
        mappings = dict() # 创建一个字典，并赋值给变量 mappings，目的是将扫描后的类属性项存储到 mappings字典中
        fields = [] # 创建一个空列表 fields，目的是保存扫描后的Model子类（如 User）的非主键属性
        primaryKey = None # primaryKey默认为 None ，目的是保存扫描后的Model子类（如 User）的主键属性
        for k, v in attrs.items(): 
                # Model子类的属性除拥有自己的类属性外，还继承了 父类字典的所有属性和父类model赋予的类属性
                # 用变量 k, v 遍历类（User）的属性项
                # 这里只剩 Model的子类 如User了，故遍历的是User类的属性项
            if isinstance(v, Field): 
                    # 判断类属性项的值 v 的类型是否是Field类 的子类或实例
                    # User类有4个类属性的值继承自 Field类，分别是
                    # IntegerField('id')，StringField('username')，StringField('email')，StringField('password')
                logging.info('  found mapping: %s ==> %s' % (k, v))
                            # 若条件成立，则输出 Found mapping: 类属性项的键==>类属性项的值
                            # 这里的类属性项的值是Field类的4种子类的实例，打印实例时，调用父类Field的__str__方法，返回结果 <实例类名, 实例属性column_type（列类型）值 : 实例属性（列）name值>
                            # 因为字典是无序的，因此打印输出的时候也是无序的
                            # 结果可能为：
                            # INFO:root:  found mapping: email ==> <StringField, varchar(50):None>
                            # INFO:root:  found mapping: passwd ==> <StringField, varchar(50):None>
                            # INFO:root:  found mapping: id ==> <StringField, varchar(50):None>
                            # INFO:root:  found mapping: name ==> <StringField, varchar(50):None>
                mappings[k] = v
                             # 将类属性项的键和值存储到 mappings字典中,此时的mappings如下
                             # mappings={'id':IntegerField('id'),'name':StringField('username'),'email':StringField('email'),'password':StringField('password')}  
                if v.primary_key: 
                            # 先判断找到的映射 (列) 是不是主键
                            # v是类属性项的值，是Field类的4种子类的实例： IntegerField('id')，StringField('username')，StringField('email')，StringField('password')
                            # v.primary_key，是指Field类的4种子类实例的primary_key属性值
                            # primary_key属性值只有两个 True 或 False
                            # if v.primary_key 是指如果primary_key值为True，则执行缩进语句块，为False 则跳过
                    if primaryKey:
                            # 若主键已存在,又找到一个主键,将报错,每张表有且仅有一个主键
                            # 主键是唯一的，
                            # primaryKey默认为 None，若前面的循环中给primaryKey赋值了，那该循环的条件继续为真，则主键重复了，抛出错误
                        raise StandardError('Duplicate primary key for field: %s' % k)
                    primaryKey = k
                            # k 是类属性项的键，对应mappings字典中的id，name 等
                            # mappings={'id':IntegerField('id'),'name':StringField('username'),'email':StringField('email'),'password':StringField('password')}
                            # 将此列设为列表的主键
                else: # 若v.primary_key条件不成立，则该列不是主键，添加到fields列表中
                    fields.append(k)         
        # end for

        # 如果遍历完还没找到主键，那抛出错误
        if not primaryKey: #  primaryKey默认值为None，为若上述循环遍历过程中没有给primaryKey 赋值--即主键没有找到，抛出错误
            raise StandardError('Primary key not found.')
        for k in mappings.keys(): 
                    # 用变量 k 遍历 mappings字典的所有类属性项的键   
                    # mappings={'id':IntegerField('id'),'name':StringField('username'),'email':StringField('email'),'password':StringField('password')}
            attrs.pop(k)
                        # 删除并弹出类（User）属性中和mappings字典同名的键--即删除该同名类属性
                        # 避免后续将mappings字典保存在类（User）属性中时出现重复
        escaped_fields = list(map(lambda f: '`%s`' % f, fields))
                # 将非主键的属性变形,放入escaped_fields中,方便sql语句的书写
                # 保存除主键外的属性名为``（运算出字符串）列表形式
                # fields 可能为 ['name', 'password', 'email'] 
                # 结果可能为 escaped_fields = ['`name`', '`password`', '`email`']

                # lambda函数
                # lambda 参数 ：表达式
                # 关键字 lambda 表示匿名函数，冒号前表示函数参数, 冒号后面为表达式

                # map函数
                # 表示 -- map(函数, Iterable)     
                # 参数
                        # map()函数接收两个参数，一个是函数，一个是Iterable--可迭代对象
                        # 可迭代对象--可以通过 for ... in 循环来遍历的对象
                # 作用 -- map将传入的函数依次作用到可迭代对象的每个元素，并把结果作为新的Iterator返回。

                # list()函数--将对象列表化

        # 保存类属性和列的映射关系
        attrs['__mappings__'] = mappings 
                # 即将一个键值对 '__mappings__' : mappings 存到类属性字典 attrs 中，mappings 本身也是一个字典
                # mappings={'id':IntegerField('id'),'name':StringField('username'),'email':StringField('email'),'password':StringField('password')} 
                # '__mappings__' : {'id':IntegerField('id'),'name':StringField('username'),'email':StringField('email'),'password':StringField('password')} 
        attrs['__table__'] = tableName 
                # 添加 表名 项到类属性字典中 
                # tableName = attrs.get('__table__', None) or name
                # 如tableName = 'User'
                # '__table__' = 'User'
        attrs['__primary_key__'] = primaryKey
                # 添加 主键 项到类属性字典中
                # primaryKey = 'id'
                # '__primary_key__' : 'id'
        attrs['__fields__'] = fields
                # 添加 非主键 项到类属性字典中，保存除主键外的属性名
                # fields = ['name', 'password', 'email'] 
                # '__fields__' ：['name', 'password', 'email'] 

        # 构造默认的SELECT、INSERT、UPDATE、DELETE语句
                # 以下都是sql语句
                # ``反引号功能同repr()
                # 函数str() 用于将值转化为适于人阅读的形式
                # 函数repr() 用于将值转化为供解释器读取的形式
        attrs['__select__'] = 'select `%s`, %s from `%s`' % (primaryKey, ', '.join(escaped_fields), tableName)
                # 添加 默认select语句 项到类属性字典中
                # primaryKey = 'id'
                # escaped_fields = ['`name`', '`password`', '`email`']
                # join连接字符串--string.join(sep)
                # 以string作为分割符，将sep中所有的元素(元素是字符串表示)合并成一个新的字符串
                # tableName = 'User'
                # 结果可能为
                # attrs['__select__'] = 'select `id`, `name`, `password`, `email` from `User`'
        attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (tableName, ', '.join(escaped_fields), primaryKey, create_args_string(len(escaped_fields) + 1))
                    # tableName = 'User'
                    # escaped_fields = ['`name`', '`password`', '`email`']
                    # ', '.join(escaped_fields) = '`name`, `password`, `email`'
                    # primaryKey = 'id'
                    # len(escaped_fields) = 3
                    # create_args_string(len(escaped_fields) + 1) = create_args_string(4)
                    # 调用 create_args_string 函数
                    # create_args_string(4) = '?, ?, ?, ?'
                    # attrs['__insert__'] = 'insert into `User` (`name`, `password`, `email`, `id`) values (?, ?, ?, ?)'  
        attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (tableName, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primaryKey)
                # tableName = 'User'
                # fields=['name', 'password', 'email'] 
                # mappings={'id':IntegerField('id'),'name':StringField('username'),'email':StringField('email'),'password':StringField('password')}
                # primaryKey = 'id'
                # attrs['__update__'] = 'update `User` set `name`=?, `password`=?, `email`=? where `id`=?' 
        attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName, primaryKey)
                # tableName = 'User'
                # primaryKey = 'id'
                # attrs['__delete__'] = 'delete from `User` where `id`=?'
        return type.__new__(cls, name, bases, attrs) # 类创建或修改完毕，返回修改后的类

# =====================================Model类区==========================================
# 定义Model类
	# 定义ORM所有映射的基类：Model
	# Model类的任意子类可以映射一个数据库表
	# Model类可以看作是对所有数据库表操作的基本定义的映射
	 
	# 基于字典查询形式
	# Model从dict继承，拥有字典的所有功能，同时实现特殊方法__getattr__和__setattr__，能够通过字典方式访问属性 ，也能通过类的方式获得属性
	# 实现数据库操作的所有方法，定义为class方法，所有继承自Model都具有数据库操作方法
class Model(dict, metaclass=ModelMetaclass): 
    # 创建 Model类，该类继承 dict类的所有功能并要通过 ModelMetaclass.__new__()来创建    
    # Model类只继承 dict类的所有功能，因为元类__new__()方法中排除了对Model类的修改    
    def __init__(self, **kw):
                # 实例化属性，通过 __init__ 方法给实例绑定属性; 在创建实例的时候，不能传入
                # 空的参数，必须传入与__init__方法匹配的参数, 但self不需要传
                # Python解释器自己会把实例变量传进去
                # 这里直接调用了Model的父类dict的初始化方法，把传入的关键字参数存入自身的dict中
                # 元类ModelMetaclass不对Model 类进行修改，因为元类__new__()方法中排除了对Model类的修改 
                # ？调用父类(dict)的实例化函数，这个类首先继承了dict类，所以会先调用dict的构造函数，把dict里的attr都写到自己的属性里   
                # 参照field子类和field类之间的关系理解
        super(Model, self).__init__(**kw)
    # 获取dict的key
    def __getattr__(self, key):
                # __getattr__()方法，动态返回一个属性或方法，只有在对象树（从下往上查询）没有找到（实例/类）属性或方法的情况下，才调用__getattr__，
                # 已有的属性或方法，不会在__getattr__中查找。
                # 查找对象树为：当前类实例属性-->类属性-->父类属性（可有多个父类）-->元类属性
        try:
            return self[key]
        except KeyError: # __getattr__默认返回None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError
            raise AttributeError(r"'Model' object has no attribute '%s'" % key) # 创建的Model类实例（应用Model实例化函数创建）中没有此属性
    
    # 实现字典方式调用，同时具有一般属性的调用方式         
    def __setattr__(self, key, value):
                # __setattr__()方法，动态创建属性或方法，只有在在对象树（从下往上查询）和__getattr__函数中没有找到（实例/类）属性或方法的情况下才创建新属性
                # 或方法，已有的属性或方法，不会通过__setattr__创建，创建时需赋值
        self[key] = value
                    # 给key赋值value
                    # Model从dict继承，所以具备所有dict的功能，同时又实现了特殊方法__getattr__()和__setattr__()，因此又可以
                    # 像引用普通字段那样写
                    # >>> user['id']
                    # 12345
                    # >>> user.id
                    # 12345

    # 获取某个具体的值即Value,如果不存在则返回None   
    def getValue(self, key):
                # 获取某个具体的值，肯定存在的情况下使用该函数,否则会使用__getattr()__
                # getattr(object, name[, default])     根据 name(属性名) 返回属性值，默认为None，若返回None，该函数不做处理
        return getattr(self, key, None)

    # 与上一个函数类似，但是如果这个属性与之对应的值为None时，就需要返回自定义的默认值，即上面函数返回值为None是的处理方式
    # 获取某个具体的值，肯定存在的情况下使用该函数
    def getValueOrDefault(self, key):
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]
                    # self.__mapping__在metaclass中，用于保存不同实例属性在Model基类中的映射关系
                    # mappings={'id':IntegerField('id'),'name':StringField('username'),'email':StringField('email'),'password':StringField('password')}
                    # field是一个定义域!
                    # 如 field = IntegerField('id')
            if field.default is not None:
                        # 如果field存在default属性，那可以直接使用这个默认值
                        # 如 后面Models.py User类的类属性id = StringField(primary_key=True, default=next_id, ddl='varchar(50)') 中
                        # 默认值为 default=next_id，next_id 是一个函数，返回一个唯一的随机 id 
                        # 如果field的default属性是callable(可被调用的)，就给value赋值它被调用后的值，如上，如果不可被调用直接返回这个值
                        # 这里的 next_id 是可以调用的，所以value = field.default() = field.next_id()
                value = field.default() if callable(field.default) else field.default
                logging.debug('using default value for %s: %s' % (key, str(value)))
                # 把默认值设为这个属性的值
                setattr(self, key, value) # 该函数重设 key 对应的 value 值，如 key = 'id'，则 默认值 value = 0
        return value

    # ==============往Model类添加类方法，就可以让所有子类调用类方法=================
    # classmethod装饰器将方法定义为类方法，即可以不创建实例直接调用类方法
                # classmethod装饰器将方法定义为类方法，即可以不创建实例直接调用类方法
                # 对于查询相关的操作,我们都定义为类方法,就可以方便查询,而不必先创建实例再查询
                # 一般来说，要使用某个类
                # 而使用@staticmethod或@classmethod，就可以不需要实例化，直接类名.方法名()来调用。
                # 这有利于组织代码，把某些应该属于某个类的函数给放到那个类里去，同时有利于命名空间的整洁。的方法，需要先实例化一个对象再调用方法。
    # 查找所有合乎条件的信息
    @classmethod
    # 类方法名由类变量cls传入，从而可以用cls做一些相关的处理。并且有子类继承时，调用该类方法时，传入的类变量cls是子类，而非父类。
    async def findAll(cls, where=None, args=None, **kw):
                # cls 参数 指元类的实例，对比 类的实例 self 参数
                # 这里的 cls 相当于 User类（model元类的一个实例，model也是元类的实例，但元类排除了对model类的修改，其子类不受影响）
                # find objects by where clause. 
                # 初始化SQL语句和参数列表
        sql = [cls.__select__]
                # attrs['__select__'] = 'select `%s`, %s from `%s`' % (primaryKey, ', '.join(escaped_fields), tableName)
                # 这里相当于 sql = [User.__select__] = ['select `id`, `name`, `password`, `email` from `Users`']
                # 即 sql = [select `id`, `name`, `password`, `email` from `User`]
        
        # WHERE 是查找条件的关键字，在关键字参数中定义
        if where:
                
                # 如果where不为None，则执行缩进语句块
            sql.append('where') 
                    # 将 where 关键字 添加到 sql语句 中
                    # 如 sql = [select `id`, `name`, `password`, `email` from `User`, where]
            sql.append(where) 
                    # 将 where 的值 添加到 where 关键字 后
                    # 如 sql = [select `id`, `name`, `password`, `email` from `User`, 'where' where条件]
        if args is None: # 这个参数是在执行sql语句前嵌入到sql语句中的，如果为None则定义一个空的list
            args = []
        # ORDER BY是排序的关键字，在关键字参数中定义
        orderBy = kw.get('orderBy', None)
        if orderBy: # 如果有OrderBy参数就在sql语句中添加OrderBy关键字和OrderBy 的值
            sql.append('order by')

                    # 如 sql = [select `id`, `name`, `password`, `email` from `User`, 'where' where条件 'order by']
            sql.append(orderBy)

                    # 如 sql = [select `id`, `name`, `password`, `email` from `User`, 'where' where条件 'order by' orderBy条件]
        # LIMIT 是筛选结果集的关键字，在关键字参数中定义
        limit = kw.get('limit', None) # 从字典中获取limit值，若无则返回None
        if limit is not None: # 如果有limit参数就在sql语句中添加limit关键字
            sql.append('limit')

                    # 如 sql = [select `id`, `name`, `password`, `email` from `User`, 'where' where条件 'order by' orderBy条件  'limit']
            if isinstance(limit, int): # 若limit的数据类型为整数 int
                sql.append('?') 
                            # 向 sql 语句中添加 一个占位符 ？
                            # 如 sql = [select `id`, `name`, `password`, `email` from `User`, 'where' where条件 'order by' orderBy条件  'limit' '?']
                args.append(limit) 
                            # 将limit的值添加到 args 列表中
                            # 若 limit = 3
                            # 则 args = [limit] = [3]
            elif isinstance(limit, tuple) and len(limit) == 2: # 若limit的数据类型是元组tuple 且 长度为2,
                sql.append('?, ?') 
                            # 则向sql语句中加入两个占位符 ？？
                            # 如 sql = [select `id`, `name`, `password`, `email` from `User`, 'where' where条件 'order by' orderBy条件  'limit' '?' '?']
                args.extend(limit) 
                            # 将元组limit中的值拆开后全部加到 args 列表中，得到一个新列表
                            # 若 limit =(3, 2)
                            # 则 args =[limit] = [3, 2]
                            # extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
                            # 若使用 args.append(limit)，只是将元组作为一个元素加到args后
                            # 而 args.extend(limit) 则将元组limit内的所有元素拆开作为args的每一个元素并添加到末尾
            else: # 若上述的 if 和 elif 不成立，则抛出错误，limit值无效
                raise ValueError('Invalid limit value: %s' % str(limit))
        rs = await select(' '.join(sql), args) 
                # 若符合 上面的 if 条件 则 select(' '.join(sql), args) = select(sql1, args1)
                # sql1='select `id` `names` `password` `email` from `User` where where条件 order by orderBy条件 limit '?''
                # args1 = [3]

                # 若符合 上面的 elif 条件 则 select(' '.join(sql), args) = select(sql2, args2)
                # sql2='select `id` `names` `password` `email` from `User` where where条件 order by orderBy条件 limit '?' '?''
                # args1 = [3, 2]

                # 用空格将sql语句内的元素重新连接为新的字符串
                # 异步调用select函数，并传入两个参数，一个是sql语句字符串，另一个是args 列表
                # select函数在前面已经定义，即函数 select(sql, args, size=None)
                # 将调用函数的结果赋值为 变量rs，select函数返回的是一个结果集
                # 由于调用的select函数没有传入 size参数，所以这里会返回查询的所有结果
        return [cls(**r) for r in rs]
                # 这是一个列表生成式
                # 表示 -- [表达式 for 表达式中的变量 in 可迭代对象 '... for 表达式中的变量 in 可迭代对象' 'if 条件'] # for 循环可以只有一个，if 条件可以省略
                # 作用 -- 用表达式中的变量 通过 for in 循环遍历 可迭代对象中的元素，将表达式作用于可迭代对象中的元素，返回一个新的列表
                # 这里具体为 [表达式 for 表达式中的变量 in 可迭代对象 ] 
                # 如 [User(**r) for r in re]
                # 即用 关键字参数 r 循环遍历 re (执行select语句后返回的结果集) 中的每一个元素，以一个新的列表返回结果
                # 若返回结果类似 {id=12345, name='point'}
                # 则 经上述列表生成式处理后得到结果为 [<'User', 'bigint':12345>, <'User','varchar(100)':'point'>]


    # findNumber() - 根据WHERE条件查找，但返回的是整数--行数，适用于select count(*)类型的SQL
    # count(*) 可以是 任意数字，或任意用引号包围的字符串，或 count(数字) 或 count("字符串")
    @classmethod
    async def findNumber(cls, selectField, where=None, args=None):
                # cls 参数 指元类的实例，对比 类的实例 self 参数
                # 这里的 cls 相当于 User类（model元类的一个实例，model也是元类的实例，但元类排除了对model类的修改，其子类不受影响）
                # find number by select and where. 
                # 初始化SQL语句和参数列表        
        sql = ['select %s _num_ from `%s`' % (selectField, cls.__table__)]
                    # _num_ 是一个标记或注释内容，可以是 任意数字，或任意用引号包围的字符串，或 count(数字) 或 count("字符串")
                    # 若 selectField 为 *   '*' 表示全选，此时不能使用 _num_
                    # 如 sql = ['select * from User']
                    # 如 sql = ['select id 'idid' from User']
                                # mysql> select id 'idid' from users;
                                # +----------------------------------------------------+
                                # | idid                                               |
                                # +----------------------------------------------------+
                                # | 0014891280111283e475b2dc6aa463a99548ba67df8d80d000 |
                                # | 00148912801119482f11e5c2a1540dd96a172bd3716bd0a000 |
                                # | 0014891280112258e2577742d4f4f46abfeb742178ba237000 |
                                # | 001489137170948e22ae3bcaf7b44bea2e993b58cad79de000 |
                                # | 001489137635530aecfeab5dada40179166b705c82966ff000 |
                                # | 0014891456251694f0b639a877040db865052c77c45f34e000 |
                                # | 0014891477016275261feb7c5534d3293edc4d9ce6aacb2000 |
                                # +----------------------------------------------------+                    
                    # 如 sql =[select count('users表中有多少行数据') from users]
                                # mysql> select count('users表中有多少行数据') from users;
                                # +----------------------------------------+
                                # | count('users表中有多少行数据')          
                                # +----------------------------------------+
                                # |                                      7  
                                # +----------------------------------------+
        if where: # 如果存在 where 条件
            sql.append('where') 
                        # 将 where 关键字添加到sql 语句末尾
                        # 如 sql = ['select count(*) _num_ from User' 'where']
            sql.append(where) 
            # 将 where 条件添加到 sql 语句中的 where 关键字 后面
            # 如 sql = ['select count(*) _num_ from User' 'where' where条件]
        rs = await select(' '.join(sql), args, 1)
        if len(rs) == 0:
            return None
        return rs[0]['_num_']

    # 根据主键查找一个实例的信息
    @classmethod
    async def find(cls, pk):
                # cls 参数 指元类的实例，对比 类的实例 self 参数
                # 这里的 cls 相当于 User类（model元类的一个实例，model也是元类的实例，但元类排除了对model类的修改，其子类不受影响）
                # pk 
                # find object by primary key.
                # select函数之前定义过，这里传入了三个参数分别是之前定义的 sql、args、size 
        rs = await select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pk], 1)
                # 若 cls 为 User 则
                # User.__select__ = 'select `id`, `name`, `password`, `email` from `User`'
                # User.__primary_key__ = 'id'
                # 'select `id`, `name`, `password`, `email` from `User`', where 'id' =[pk]
                # select函数中的size = 1，故该函数只返回一条结果
        if len(rs) == 0:
            return None
        return cls(**rs[0]) # 返回 User(**rs[0])

    # ===============往Model类添加实例方法，就可以让所有子类调用实例方法===================
    
    # save、update、remove这三个方法需要管理员权限才能操作，所以不定义为类方法，需要创建实例之后才能调用
    # 把一个实例的信息保存到数据库
    async def save(self):
        # args是保存所有Model实例属性和主键的list,使用getValueOrDefault方法的好处是没有具体value值则保存默认值 
        # 将除主键外的属性名添加到args这个列表中
        args = list(map(self.getValueOrDefault, self.__fields__))
                # map函数
                # 表示 -- map(函数, Iterable)     
                # 参数
                        # map()函数接收两个参数，一个是函数，一个是Iterable--可迭代对象
                        # 可迭代对象--可以通过 for ... in 循环来遍历的对象
                # 作用 -- map将传入的函数依次作用到可迭代对象的每个元素，并把结果作为新的Iterator返回。

                # list()函数--将对象列表化
                
                # fields 可能为 ['name', 'password', 'email'] 
                # attrs['__fields__'] = fields =  ['name', 'password', 'email']        
                # 即   '__fields__' ：['name', 'password', 'email']               
                # 添加 非主键 项到类属性字典中，保存除主键外的属性名

                # getValueOrDefault 函数获取某个具体的值，肯定存在的情况下使用该函数，否则会使用__getattr()__
                # getValueOrDefault 函数相比于 getValue函数 其好处是当 getattr(self, key, None)返回的value值为None时
                # 返回 默认值，如StringField(Field)的default属性默认值为 None，BooleanField(Field))的default属性默认值为False
                # IntegerField(Field)的default属性默认值为 0，FloatField(Field)的default属性默认值 ,0.0
                
                # 若 实例为 u = User(id=12345, name='point', email='point@python.org', password='password')
                # 所以这里的 args 可能为 args= ['point', 'password', 'point@python.org']
        args.append(self.getValueOrDefault(self.__primary_key__)) 
                # 再把主键添加到这个列表的最后
                # 结果可能为 args = ['point', 'password', 'point@python.org', 12345]
        rows = await execute(self.__insert__, args)
                # 异步执行execute函数，并传入两个参数，一个为sql语句，另一个为args值列表，前面已经定义
                # attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (tableName, ', '.join(escaped_fields), primaryKey, create_args_string(len(escaped_fields) + 1))
                # attrs['__insert__'] = 'insert into `User` (`name`, `password`, `email`, `id`) values (?, ?, ?, ?)'  
                # self.__insert__ = u.__insert__ = 'insert into `User` (`name`, `password`, `email`, `id`) values (?, ?, ?, ?)'  
                # args = ['point', 'password', 'point@python.org', 12345]
                # 这里的args可能为args = ['point', 'password', 'point@python.org']
                # 最终的执行sql语句可能为 execute('insert into `User` (`name`, `password`, `email`, `id`) values (?, ?, ?, ?)',  ['point', 'password', 'point@python.org', 12345])
                # execute函数返回的是受影响的结果数，正常情况下返回为1，因为select函数只执行一条sql语句
        if rows != 1: # 插入纪录受影响的行数应该为1，如果不是1 那就错了，因为select函数只执行一条sql语句
            logging.warn('failed to insert record: affected rows: %s' % rows)

    # 更新一个实例在数据库的信息
    async def update(self):
        args = list(map(self.getValue, self.__fields__))
                    # getValue函数获取某个具体的值，肯定存在的情况下使用该函数,否则会使用__getattr()__
                    # getValue函数对值为None的属性不做处理        
        args.append(self.getValue(self.__primary_key__))
        rows = await execute(self.__update__, args)
        if rows != 1:
            logging.warn('failed to update by primary key: affected rows: %s' % rows)

    # 把一个实例从数据库中删除
    async def remove(self):
        args = [self.getValue(self.__primary_key__)]
                    # getValue函数获取某个具体的值，肯定存在的情况下使用该函数,否则会使用__getattr()__
                    # getValue函数对值为None的属性不做处理
                    # 这里获得主键的value值，然后执行删除语句
        rows = await execute(self.__delete__, args)
        if rows != 1:
            logging.warn('failed to remove by primary key: affected rows: %s' % rows)

if __name__ == '__main__':
    class User(Model): # 定义 User类 ，父类为Model
        # 定义类的属性到列的映射：
        id = IntegerField('id',primary_key=True) 
        name = StringField('username')
        email = StringField('email')
        password = StringField('password') # 创建 StringField类 的实例，实例有一个参数'password'，赋值给变量 password，作为User类的类属性
    # 创建 User类 的实例，赋值给 变量 u
    u = User(id=12345, name='point', email='point@python.org', password='password')
    print(u)
    # 保存到数据库
    u.save() 
    print(u)

"""
	数据(储存与访问)--数据库--数据库操作(封装)--异步(协程)
		'''
		在一个Web App中，所有数据，包括用户信息、发布的日志、评论等，都存储在数据库中我们选择MySQL
		作为数据库。		

		Web App里面有很多地方都要访问数据库。访问数据库需要创建数据库连接、游标对象，然后执行SQL语句，
		最后处理异常，清理资源。		

		这些访问数据库的代码如果分散到各个函数中，势必无法维护，也不利于代码复用。		

		所以，我们要首先把常用的SELECT、INSERT、UPDATE和DELETE操作用函数封装起来。
		由于Web框架使用了基于asyncio的aiohttp，这是基于协程的异步模型。在协程中，不能调用普通的同步IO
		操作，因为所有用户都是由一个线程服务的。协程的执行速度必须非常快，才能处理大量用户的请求。而耗
		时的IO操作不能在协程中以同步的方式调用，否则，等待一个IO操作时，系统无法响应任何其他用户		

		这就是异步编程的一个原则：一旦决定使用异步，则系统每一层都必须是异步，“开弓没有回头箭”。		

		'幸运的是aiomysql为MySQL数据库提供了异步IO的驱动'
		'''	

	创建连接池
		我们需要创建一个'全局'的连接池，'每个HTTP请求都可以从连接池中直接获取数据库连接'。使用连接池的好
		处是'不必频繁地打开和关闭数据库连接'，而是'能复用就尽量复用'。		

		连接池由'全局变量__pool'存储，缺省情况下将编码设置为utf8，自动提交事务：		

		@asyncio.coroutine
		def create_pool(loop, **kw):
		    logging.info('create database connection pool...')
		    global __pool
		    __pool = yield from aiomysql.create_pool(
		        host=kw.get('host', 'localhost'), # 通过字典的get方法给键key 'host' 指定 value值 'localhost' 并赋值给host
		        port=kw.get('port', 3306),
		        user=kw['user'], # 将字典中键key为'user'的值value 赋值给 user 变量
		        password=kw['password'],
		        db=kw['db'],
		        charset=kw.get('charset', 'utf8'),
					""
						“UTF-8”是标准写法，在Windows下边英文不区分大小写，所以也可以写成“utf-8”。“UTF-8”也可以把中间的“-”省略，写成
						“UTF8”。一般程序都能识别，但也有例外（如下文），为了严格一点，最好用标准的大写“UTF-8”。
						在MySQL数据库中只能使用“utf8”
						在MySQL的命令模式中只能使用“utf8”，不能使用“utf-8”，也就是说在PHP程序中只能使用“set names utf8(不加小横杠)”，
						如果你加了“-”此行命令将不会生效，但是在PHP中header时却要加上“-”，因为IE不认识没杠的“utf8”，原因 见下文。
						在IE浏览器中只能使用“utf-8”
						IE中如果使用了“utf8”，页面可能会 空白 或 显示为乱码。
						但是在其它浏览器却是正常的，原因是因为：其它浏览器默认使用的是UTF-8的编码，如果无法识别页面的编码就会用默认
						的UTF-8来解码，但 是IE的默认编码是GB2312，所以默认的话就。。。。。（其它浏览器指“FireFox”、“Chrome”、“Opera”）
						总结　　
						【只有在MySQL中可以使用“utf-8”的别名“utf8”，但是在其他地方一律使用大写“UTF-8”。】
						具体为：
						在命令“mysql_query(set names utf8)”外一律用大写“UTF-8”。
					""
		        autocommit=kw.get('autocommit', True),
		        maxsize=kw.get('maxsize', 10),
		        minsize=kw.get('minsize', 1),
		        loop=loop
		    )		
	select函数--执行SELECT语句
		要执行SELECT语句，我们用select函数执行，需要传入SQL语句和SQL参数：		

		@asyncio.coroutine
		def select(sql, args, size=None):
		    log(sql, args)
		    global __pool
		    with (yield from __pool) as conn:
						# with 语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”
						# 操作，释放资源，比如文件使用后自动关闭、线程中锁的自动获取和释放等。实现上下文管理
						# with 语句的语法格式
						# with context_expression [as target(s)]:
						# with-body
						# 这里 context_expression 要返回一个上下文管理器对象，该对象并不赋值给 as 子句中的 target(s) ，
						# 如果指定了 as 子句的话，会将上下文管理器的 __enter__() 方法的返回值赋值给 target(s)。target(s) 
						# 可以是单个变量，或者由“()”括起来的元组（不能是仅仅由“,”分隔的变量列表，必须加“()”）。							

						# yield from 调用一个子协程（也就是在一个协程中调用另一个协程）并直接获得子协程的返回结果
		        cur = yield from conn.cursor(aiomysql.DictCursor)
		        yield from cur.execute(sql.replace('?', '%s'), args or ())
			        # SQL语句的占位符是?，而MySQL的占位符是%s，select()函数在内部自动替换。注意要始终坚持使用
			        # 带参数的SQL，而不是自己拼接SQL字符串，这样可以防止SQL注入攻击。			

			        # execute(self, query, args=None)
			        #     Executes the given operation
			        #     
			        #     Executes the given operation substituting any markers with
			        #     the given parameters.
			        #     
			        #     For example, getting all rows where id is 5:
			        #       cursor.execute("SELECT * FROM t1 WHERE id = %s", (5,))
			        #     
			        #     :param query: ``str`` sql statement
			        #     :param args: ``tuple`` or ``list`` of arguments for sql query
			        #     :returns: ``int``, number of rows that has been produced of affected		
		        if size:
		            rs = yield from cur.fetchmany(size)
		        else:
		            rs = yield from cur.fetchall()
		        yield from cur.close()
		        logging.info('rows returned: %s' % len(rs))
		        return rs
	通用的execute函数--执行INSERT、UPDATE、DELETE语句
		要执行INSERT、UPDATE、DELETE语句，可以定义一个通用的execute()函数，因为这3种SQL的执行都需要相同
		的参数，以及返回一个整数表示影响的行数：		

		@asyncio.coroutine
		def execute(sql, args):
		    log(sql)
		    with (yield from __pool) as conn:
		        try:
		            cur = yield from conn.cursor()
		            yield from cur.execute(sql.replace('?', '%s'), args)
				        # rowcount
				        #     Returns the number of rows that has been produced of affected.
				        #     
				        #     This read-only attribute specifies the number of rows that the
				        #     last :meth:`execute` produced (for Data Query Language
				        #     statements like SELECT) or affected (for Data Manipulation
				        #     Language statements like UPDATE or INSERT).
				        #     
				        #     The attribute is -1 in case no .execute() has been performed
				        #     on the cursor or the row count of the last operation if it
				        #     can't be determined by the interface.
		            affected = cur.rowcount
		            yield from cur.close()
		        except BaseException as e:
		            raise
		        return affected		

		execute()函数和select()函数所不同的是，cursor对象不返回结果集，而是通过rowcount返回结果数。		
	ORM
		ORM全称“Object Relational Mapping”，即'对象-关系映射'
		就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。
		要'编写一个ORM框架，所有的类都只能动态定义'，因为只有使用者才能根据表的结构定义出对应的类来。
		
		有了基本的select()和execute()函数，我们就可以开始编写一个简单的ORM了。
		设计ORM需要'从上层调用者角度'来设计。
		我们先考虑如何定义一个'User对象'，然后把数据库表users和它关联起来。
		编写底层模块的第一步，就是先把调用接口写出来。比如，使用者如果使用这个ORM框架，想定义一个User类来
		操作对应的数据库表User，我们期待他写出这样的代码：		

		from orm import Model, StringField, IntegerField		

		class User(Model):
		    __table__ = 'users'
		    # # 定义类的属性到列的映射：
		    id = IntegerField(primary_key=True)
		    name = StringField()		

		注意到定义在User类中的__table__、id和name是'类'的属性，不是实例的属性。所以，在类级别上定义的属性
		用来'描述User对象和表的映射关系'，而实例属性必须通过__init__()方法去初始化，所以两者互不干扰：		

		# 创建实例:
		user = User(id=123, name='Michael')
		# 存入数据库:
		user.insert()
		# 查询所有User对象:
		users = User.findAll()
		        # class User(Model):
		        #     # 定义类的属性到列的映射：
		        #     id = IntegerField('id')
		        #     name = StringField('username')
		        #     email = StringField('email')
		        #     password = StringField('password')        		

		        # # 创建一个实例：
		        # u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
		        # # 保存到数据库：
		        # u.save()
		        # 其中，父类Model和属性类型StringField、IntegerField是由ORM框架提供的，剩下的魔术方法比如
		        # save()全部由metaclass自动完成。虽然metaclass的编写会比较复杂，但ORM的使用者用起来却异常简单。		
	定义Model
			首先要定义的是所有ORM映射的基类Model：

		    class Model(dict, metaclass=ModelMetaclass):
		    # Model从dict继承，所以具备所有dict的功能
		        def __init__(self, **kw):
		            super(Model, self).__init__(**kw)    		

		        def __getattr__(self, key):
		            try:
		                return self[key]
		            except KeyError:
		                raise AttributeError(r"'Model' object has no attribute '%s'" % key)    		

		        def __setattr__(self, key, value):
		            self[key] = value    		

		        def getValue(self, key):
		            return getattr(self, key, None)    		

		        def getValueOrDefault(self, key):
		            value = getattr(self, key, None)
		            if value is None:
		                field = self.__mappings__[key]
		                if field.default is not None:
		                    value = field.default() if callable(field.default) else field.default
		                    logging.debug('using default value for %s: %s' % (key, str(value)))
		                    setattr(self, key, value)
		            return value    		

		    同时又实现了特殊方法__getattr__()和__setattr__()，因此又可以像引用普通字段那样写:    		

		    >>> user['id']
		    123
		    >>> user.id
		    123		
	以及Field和各种Field子类

		    class Field(object):

		        def __init__(self, name, column_type, primary_key, default): 
		            self.name = name
		            self.column_type = column_type
		            self.primary_key = primary_key
		            self.default = default    		

		        def __str__(self):
		            return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type, self.name)		

			    # >>> class Field(object):     
			    #     def __init__(self, name, column_type, primary_key, default):
			    #         self.name = name
			    #         self.column_type = column_type
			    #         self.primary_key = primary_key
			    #         self.default = default    
			    #     def __str__(self):
			    #         return '<%s, %s:%s>'  %  (self.__class__.__name__, self.column_type, self.name)   
			    # >>> print(Field('','','',''))
			    # <Field, :>
			    # >>> print(Field('1','2','3','4'))
			    # <Field, 2:1>
			    # >>> 		
		    class StringField(Field):

		        def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
		            super().__init__(name, ddl, primary_key, default)
		        # >>> print(StringField('1','2','3','4'))
		        # <StringField, 4:1>		
		    class BooleanField(Field):

		        def __init__(self, name=None, default=False):
		            super().__init__(name, 'boolean', False, default)    
		        # >>> print(BooleanField( ))
		        # <BooleanField, boolean:None>
		        # >>> print(BooleanField( '1',' '))
		        # <BooleanField, boolean:1>
		        # >>> print(BooleanField( '1',' 2'))
		        # <BooleanField, boolean:1>
		        # >>> print(BooleanField( '1',' 2',''))    		
		    class IntegerField(Field):

		        def __init__(self, name=None, primary_key=False, default=0):
		            super().__init__(name, 'bigint', primary_key, default)    
		        # >>> print(IntegerField())
		        # <IntegerField, bigint:None>
		        # >>> print(IntegerField('1'))
		        # <IntegerField, bigint:1>
		        # >>> print(IntegerField('1','2'))
		        # <IntegerField, bigint:1>
		        # >>> print(IntegerField('1','2','3'))
		        # <IntegerField, bigint:1>
		    class FloatField(Field):

		        def __init__(self, name=None, primary_key=False, default=0.0):
		            super().__init__(name, 'real', primary_key, default)    		
		    class TextField(Field):

		        def __init__(self, name=None, default=None):
		            super().__init__(name, 'text', False, default)		
	定义Model的元类
		    注意到Model只是一个基类/父类，'如何将具体的子类如User的映射信息读取出来呢？'答案就是通过metaclass：ModelMetaclass：
		    class ModelMetaclass(type):    		

		        def __new__(cls, name, bases, attrs):
		            # 排除Model类本身:
		            if name=='Model':
		                return type.__new__(cls, name, bases, attrs)
		            # 获取table名称:
		            tableName = attrs.get('__table__', None) or name
		            logging.info('found model: %s (table: %s)' % (name, tableName))
		            # 获取所有的Field和主键名:
		            mappings = dict()
		            fields = []
		            primaryKey = None
		            for k, v in attrs.items():
		                if isinstance(v, Field):
		                    logging.info('  found mapping: %s ==> %s' % (k, v))
		                    mappings[k] = v
		                    if v.primary_key:
		                        # 找到主键:
		                        if primaryKey:
		                            raise RuntimeError('Duplicate primary key for field: %s' % k)
		                        primaryKey = k
		                    else:
		                        fields.append(k)
		            if not primaryKey:
		                raise RuntimeError('Primary key not found.')
		            for k in mappings.keys():
		                attrs.pop(k)
		            escaped_fields = list(map(lambda f: '`%s`' % f, fields))
		            attrs['__mappings__'] = mappings # 保存属性和列的映射关系
		            attrs['__table__'] = tableName
		            attrs['__primary_key__'] = primaryKey # 主键属性名
		            attrs['__fields__'] = fields # 除主键外的属性名
		            # 构造默认的SELECT, INSERT, UPDATE和DELETE语句:
		            attrs['__select__'] = 'select `%s`, %s from `%s`' % (primaryKey, ', '.join(escaped_fields), tableName)
		            attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (tableName, ', '.join(escaped_fields), primaryKey, create_args_string(len(escaped_fields) + 1))
		            attrs['__update__'] = 'update `%s` set %s where `%s`=?' % (tableName, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primaryKey)
		            attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName, primaryKey)
		            return type.__new__(cls, name, bases, attrs)		
			这样，任何继承自Model的类（比如User），会自动通过ModelMetaclass扫描映射关系，并存储到自身的类属性如__table__、__mappings__中。
	然后，我们往Model类添加class方法，就可以让所有子类调用class方法：
		在Model类中，就可以定义各种操作数据库的方法，比如save()，delete()，find()，update等等。
		    class Model(dict):    		
			    # @staticmethod或@classmethod
			        #  一般来说，要使用某个类的方法，需要先实例化一个对象再调用方法。
			        # 而使用@staticmethod或@classmethod，就可以不需要实例化，直接类名.方法名()来调用。
			        # 这有利于组织代码，把某些应该属于某个类的函数给放到那个类里去，同时有利于命名空间的整洁。	
						    既然@staticmethod和@classmethod都可以直接类名.方法名()来调用，那他们有什么区别呢
						        从它们的使用上来看,
						         •@staticmethod不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样。
						         •@classmethod也不需要self参数，但第一个参数需要是表示自身类的cls参数。        		

						        如果在@staticmethod中要调用到这个类的一些属性方法，只能直接类名/实例名.属性名或类名/实例名.方法名。       		

						        而@classmethod因为持有cls参数，可以来调用类的属性，类的方法，实例化对象等，避免硬编码。    
						    下面上代码

						        # [python] view plain copy 
						        # 01.class A(object):  
						        # 02.    bar = 1  
						        # 03.    def foo(self):  
						        # 04.        print 'foo'  
						        # 05. 
						        # 06.    @staticmethod  
						        # 07.    def static_foo():  
						        # 08.        print 'static_foo'  
						        # 09.        print A.bar  
						        # 10. 
						        # 11.    @classmethod  
						        # 12.    def class_foo(cls):  
						        # 13.        print 'class_foo'  
						        # 14.        print cls.bar  
						        # 15.        cls().foo()  
						        # 16.  
						        # 17.A.static_foo()  
						        # 18.A.class_foo()          	

						        # 输出
						        # static_foo
						        #  1
						        #  class_foo
						        #  1
						        #  foo		
						    python @classmethod 和 @staticmethod区别，以及类中方法参数cls和self的区别        
						        staticmethod

							        首先来看@staticmethod，这个装饰器很好理解，就是让类中的方法变成一个普通的函数（因为是普通函数，并没有绑定在任何一个
							        特定的类或者实例上。所以与不需要对象实例化就可以直接调用）。可以使用类或者类的实例调用，并且没有任何隐含参数的传入，
							        所以不需要self(参数名是随便定的)。        			

							        # >>> class C(object):
							        # ...     @staticmethod
							        # ...     def add(a,b):
							        # ...             return a+b
							        # ...     def get_weight(self):
							        # ...             return self.add(1,2)
							        # ... 
							        # >>> C.add
							        # <function add at 0x1d32668>
							        # >>> C().add
							        # <function add at 0x1d32668>
							        # >>> C.get_weight
							        # <unbound method C.get_weight>      		
						        总结

						            1、当一个函数逻辑上属于一个类又不依赖于类的属性的时候，可以使用 @staticmethod。      		
						            2、使用 @staticmethod 可以避免每次使用的时都会创建一个对象的开销。       	
						            3、@staticmethod 可以使用类和类的实例调用。但是不依赖于类和类的实例的状态。    	  		
						        classmethod
						        	再看@classmethod，我们对比下加与不加装饰前后函数 
									    不加装饰前
									      
									        # >>> class C(object):
									        # ...     weight = 12
									        # ...     def get_weight(self):
									        # ...             print self
									        # ... 
									        # >>> C.get_weight
									        # <unbound method C.get_weight>
									        # >>> C().get_weight
									        # <bound method C.get_weight of <__main__.C object at 0x25d7b10>>
									        # >>> C().get_weight()
									        # <__main__.C object at 0x25d7a50>
									        # >>> myc = C()
									        # >>> myc.get_weight
									        # <bound method C.get_weight of <__main__.C object at 0x25d7a50>>
									        # >>> myc.get_weight()
									        # <__main__.C object at 0x25d7a50>    	

									        # 通过例子知道，C().get_weight和myc.get_weight都是绑定在对象C的一个实例上的。
									        # （e.g. <bound method C.get_weight of <__main__.C object at 0x25d7b10>>）        		

									        # 顺便通过下面的代码，看下get_weight的self到底接收的是什么：    
									        
									        # #继续上面的代码
									        # >>> C.get_weight()        #异常报错
									        # Traceback (most recent call last):
									        #   File "<stdin>", line 1, in <module>
									        # TypeError: unbound method get_weight() must be called with C instance as first argument (got nothing instead)
									        # >>> C.get_weight(C())    #将C的一个实例显示传递给self
									        # <__main__.C object at 0x25d7b50>
									        # >>> myc.get_weight()    # myc.get_weight()隐藏了第一个参数myc
									        # <__main__.C object at 0x25d7a50>
									        # >>>        			

									        # 调用的实例隐藏的作为一个参数self传递过去了，self 只是一个普通的参数名称（参数名是随便定的），不是关键字。      	
									    加@classmethod装饰后
									        
									        # >>> class C(object):
									        # ...     weight = 12
									        # ...     @classmethod
									        # ...     def get_weight(cls):
									        # ...             print cls
									        # ... 
									        # >>> C.get_weight
									        # <bound method type.get_weight of <class '__main__.C'>>
									        # >>> C().get_weight
									        # <bound method type.get_weight of <class '__main__.C'>>
									        # >>> myc = C()
									        # >>> myc.get_weight
									        # <bound method type.get_weight of <class '__main__.C'>>
									        # >>> myc.get_weight()
									        # <class '__main__.C'>
									        # >>> C.get_weight()
									        # <class '__main__.C'>      	
									       
									        # 可以看出，C类和C类的实例都能调用 get_weight 而且调用结果完全一样。 我们看到 weight 是属于 C类的属性，
									        # 当然也是C的实例的属性(元对象__get__机制)。        	

									        # 再看一下get_weight的参数cls到底接收的是什么，可以看到C.get_weight()和myc.get_weight()接收的都是C类
									        # (e.g. <class '__main__.C'> )而不是C类的实例，cls只是一个普通的函数参数，调用时隐含的传递过去。         		
						    	总结
						        	1、classmethod 是类对象与函数的结合。        	
						        	2、可以使用类和类的实例调用，但是都是将类作为隐含参数传递过去。        		
						        	3、使用类来调用 classmethod 可以避免将类实例化的开销。   					
						        补充
						        	@staticmethod 装饰器会让 foo 的 __get__ 返回一个函数，而不是一个方法。看下面的例子
							        
							        # >>> class C(object):
							        # ...     def foo(self):
							        # ...         pass
							        # ...
							        # >>> C.foo
							        # <unbound method C.foo>
							        # >>> C().foo
							        # <bound method C.foo of <__main__.C object at 0xb76ddcac>>
							        # >>>        		
						        	所谓 bound method ，就是方法对象的第一个函数参数绑定为了这个类的实例(所谓 bind )。这也是那个 self 的由来

							        # 那，我们加入@staticmethod之后：        
							     
							        # >>> class C(object):
							        # ...     @staticmethod
							        # ...     def foo():
							        # ...         pass
							        # ...
							        # >>> C.foo
							        # <function foo at 0xb76d056c>
							        # >>> C.__dict__['foo'].__get__(None, C)
							        # <function foo at 0xb76d056c>        		
						        	装饰器会让 foo 的 __get__ 返回一个函数，而不是一个方法。	
		        @classmethod
		        @asyncio.coroutine
		        def find(cls, pk):
		            # ' find object by primary key. '
		            rs = yield from select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pk], 1)
		            if len(rs) == 0:
		                return None
		            return cls(**rs[0])		
		    # User类现在就可以通过类方法实现主键查找：
		    user = yield from User.find('123')		
		往Model类添加实例方法，就可以让所有子类调用实例方法：
		    class Model(dict):    		

		        ...    		

		        @asyncio.coroutine
		        def save(self):
		            args = list(map(self.getValueOrDefault, self.__fields__))
		            args.append(self.getValueOrDefault(self.__primary_key__))
		            rows = yield from execute(self.__insert__, args)
		            if rows != 1:
		                logging.warn('failed to insert record: affected rows: %s' % rows)    		

		    这样，就可以把一个User实例存入数据库：
		    user = User(id=123, name='Michael')
		    yield from user.save()		
	最后一步是完善ORM，对于查找，我们可以实现以下方法：
			•	findAll() - 根据WHERE条件查找；
			•	findNumber() - 根据WHERE条件查找，但返回的是整数，适用于select count(*)类型的SQL。
			以及update()和remove()方法。
			所有这些方法都必须用@asyncio.coroutine装饰，变成一个协程。
			调用时需要特别注意：
			user.save()
			没有任何效果，因为调用save()仅仅是创建了一个协程，并没有执行它。一定要用：
			yield from user.save()
			才真正执行了INSERT操作。
			最后看看我们实现的ORM模块一共多少行代码？累计不到300多行。用Python写一个ORM是不是很容易呢？
"""