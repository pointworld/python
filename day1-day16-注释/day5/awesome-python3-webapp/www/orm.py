#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
	选择MySQL(作为网站的'后台数据库')
	 
	执行'SQL语句进行操作'，并将常用的SELECT、INSERT等语句进行函数封装
	 
	在异步框架的基础上，采用aiomysql(作为数据库的异步IO驱动)
	 
	将数据库中表的操作，'映射'成一个类的操作，也就是数据库表的一行映射成一个对象(ORM)
	 
	整个ORM也是异步操作
	 
	预备知识：Python协程和异步IO(yield from的使用)、SQL数据库操作、元类、面向对象知识、Python语法
	 
	# -*- -----  思路  ----- -*-
	    如何定义一个user类，这个类和数据库中的表User构成映射关系，二者应该关联起来，user可以操作表User	

	    通过Field类将user类的属性映射到User表的列中，其中每一列的字段又有自己的一些属性，包括数据类型，列名，主键和默认值
'''

__author__ = 'Point'
	
import logging;logging.basicConfig(level=logging.INFO)
import aiomysql, asyncio

#
	# 引入 asyncio, logging，aiomysql 库
	# asyncio-异步IO, logging-日志，aiomysql-异步IO+MySQL
	# 在异步框架的基础上，采用aiomysql作为数据库的异步IO驱动

def log(sql, args=()): # 定义 log 函数，sql为 必选参数，args为默认参数，参数类型是元组
    logging.info('SQL: %s' % sql) 
	#
  		# 记录信息，logging 模块设置的默认等级时 WARNING, 这里不会记录信息
		# 打印SQL查询语句 日志
async def create_pool(loop, **kw): # 该函数用于创建连接池
	#
		# 定义 create_pool函数，loop为 必选参数，**kw为关键字参数
		# 创建一个全局的连接池，每个HTTP请求都从池中获得数据库连接
		# async 关键字 等价于 @asyncio.coroutine
		# **kw参数可以包含所有连接需要用到的关键字参数
    logging.info('create database connection pool...') # 记录信息，logging 模块设置的默认等级时 WARNING, 这里不会记录信息
    global __pool 
    # 私有变量__pool用于存储整个连接池，模块外部不能访问私有变量      
    # 这里用global声明，表示在该模块中可以通用
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'), 
        #
        	# dict的get方法，如果key不存在，可以返回None，或者自己指定的value，这里指定'localhost'，默认本机IP
    		# host　主机  MySQL server IP address or name
        port=kw.get('port', 3306),
        #
        	# dict的get方法，如果key不存在，可以返回None，或者自己指定的value，这里指定3306，默认mysql的端口号为3306
        	# port 端口号  MySQL server TCP/IP port        
        user=kw['user'],# 通过关键字参数传递user
        #
        	# 获得键'user'的值，赋值给user变量
        	# user  User used while connecting to MySQL
        password=kw['password'],# 通过关键字参数传递password
        #
        	
        	# 获得键'password'的值，赋值给password变量      
        db=kw['db'],# 通过关键字参数传递数据库名称
        #
        	# 数据库名字
        	# 获得键'db'的值，赋值给db变量  
        	# db  Current database name.       
        charesultsetet=kw.get('charesultsetet', 'utf8'),
        #
        	# dict的get方法，如果key不存在，可以返回None，或者自己指定的value，这里指定默认数据库字符集utf8
        	# charesultsetet  Returns the character set for current connection.
        	# 在MySQL数据库中只能使用“utf8”, 不能写成utf8的其他形式       
        autocommit=kw.get('autocommit', True),
        #
        	# dict的get方法，如果key不存在，可以返回None，或者自己指定的value，这里指定True，默认autocommit=True
			# # 默认自动提交事务
			# autocommit(self, value)  Enable/disable autocommit mode for current MySQL session.       
        maxsize=kw.get('maxsize', 10), # 默认连接池最多同时处理10个请求            
        minsize=kw.get('minsize', 1), # 默认连接池最少1个请求        
        loop=loop # 接收一个event_loop实例，需要关联函数内的 loop = asyncio.get_event_loop()，用于异步执行
    )
async def select(sql, args, size=None): # 用于SQL的SELECT语句。对应select方法,传入sql语句和参数
	#
		# 定义select函数，封装SQL SELECT语句
		# 注意，这里的args不是可变参数，可变参数的表示是：*args  
    log(sql, args) # 调用log函数，记录信息，这里不记录
    global __pool # 调用全局变量 __pool，__pool作为字典存储了整个连接池  
    async with __pool.get() as conn: 
    #
    		# 异步等待连接池对象返回可以连接线程
    		# with 语句实现上下文管理，替代try-finally语句
    		# with 语句封装了清理（关闭conn）和处理异常的工作
    		# 调用字典的get方法，赋值给变量conn
        async with conn.curesultsetor(aiomysql.DictCuresultsetor) as cur: # DictCuresultsetor is a curesultsetor which returns results as a dictionary
            # 异步等待连接对象返回DictCuresultsetor可以通过dict的方式获取数据库对象，需要通过游标对象执行SQL
            await cur.execute(sql.replace('?', '%s'), args or ())
            #
        		# 执行SQL语句
            	# 将sql中的'?'替换为'%s'，因为mysql语句中的占位符为%s

           		# execute(self, query, args=None)
            	# Executes the given operation
            	# Executes the given operation substituting any markeresultset with the given parameteresultset.
            if size:# 如果指定size				
                resultset = await cur.fetchmany(size)
            	#
            		# 根据指定返回的size，返回查询的结果
            		# 返回size条查询结果
                	# fetchmany(self, size=None)
               		# Returns the next set of rows of a query result, returning a list of tuples. When no more 
                	# rows are available, it returns an empty list.
            else:			
                resultset = await cur.fetchall()
            	#
	                # 返回所有的结果集
	                # 返回所有查询结果
	                # fetchmany(self, size=None)
	                # Returns the next set of rows of a query result, returning a list of tuples. When no more 
	                # rows are available, it returns an empty list.  
        logging.info('rows returned: %s' % len(resultset))
        conn.close()
        return resultset # 返回结果集
async def execute(sql, args, autocommit=True):# 用于SQL的INSERT INTO，UPDATE，DELETE语句，execute方法只返回结果数，不返回结果集
    #
		# 定义一个execute函数，参数为sql, args, autocommit=True
		# 封装INSERT, UPDATE, DELETE
		# 语句操作参数一样，所以定义一个通用的执行函数
		# 返回操作影响的行数
    log(sql) # 调用log函数，记录信息，这里不记录
    async with __pool.get() as conn:
    #
    		# with 语句实现上下文管理，替代try-finally语句
    		# 调用字典的get方法，赋值给变量conn
        if not autocommit:
        	#
        		# 若设置不是自动提交，则调用协程启动连接
        		# begin(self)  one of methods in class Connection(builtins.object)
            	# Begin transaction.
            await conn.begin()
        try:
            async with conn.curesultsetor(aiomysql.DictCuresultsetor) as cur:
                # 打开一个DictCursor，它与普通游标的不同在于，以dict形式返回结果
                await cur.execute(sql.replace('?', '%s'), args)
                affected = cur.rowcount # 返回受影响的行数
            if not autocommit: # 同上, 如果设置不是自动提交的话，手动提交事务
                await conn.commit()
        except BaseException as e:
            if not autocommit:                  
                await conn.rollback()# 出错, 回滚事务到增删改之前
                #
                	# rollback(self)  one of methods in class Connection(builtins.object)
                	# Roll back the current transaction.   
            raise e
        return affected
def create_args_string(num):
	# 根据输入的参数生成占位符列表
    L = []
    for n in range(num):
        L.append('?')   
    return ', '.join(L) # 以','为分隔符，将列表合成字符串

# 定义Field类，它负责保存数据库表的字段名和字段类型
class Field(object):
    def __init__(self, name, column_type, primary_key, default):
        self.name = name 
        self.column_type = column_type
        self.primary_key = primary_key
	        # 主键，即主关键字(primary key)是表中的一个或多个字段，它的值用于唯一地标识表中的某一条记录。在两个表的关系中，
	        # 主关键字用来在一个表中引用来自于另一个表中的特定记录。主关键字是一种唯一关键字，表定义的一部分。一个
	        # 表的主键可以由多个关键字共同组成，并且主关键字的列不能包含空值。主关键字是可选的，并且可在 CREATE TABLE 
	        # 或 ALTER TABLE 语句中定义
        self.default = default

    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type, self.name)
        	# return '<{0.__class__.__name__}, {0.column_type}: {0.name}>'.format(self)
        	# <实例类名, 实例属性column_type值:实例属性name值>
# 定义不同字段类型(column_type)的衍生Field
	
	# 数据库表的不同纵列数据类型不一样
class StringField(Field):#字符串域
    def __init__(self, name=None, primary_key=False, default=None, ddl='varchar(100)'):
        # String一般不作为主键，所以默认False, DDL是数据定义语言，为了配合mysql，所以默认设定为100的长度
        super().__init__(name, ddl, primary_key, default)
class BooleanField(Field):#布尔域
    def __init__(self, name=None, default=False):
    	# 这个是不能作为主键的对象，所以这里直接就设定成False
        super().__init__(name, 'boolean', False, default)
class IntegerField(Field):#整数域
    def __init__(self, name=None, primary_key=False, default=0):
        super().__init__(name, 'bigint', primary_key, default)
class FloatField(Field):#浮点数域
    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, 'real', primary_key, default)
class TextField(Field):#文本域
    def __init__(self, name=None, default=None):
        # 这个是不能作为主键的对象，所以这里直接就设定成False
        super().__init__(name, 'text', False, default)

# 定义Model的元类
	# 所有的元类都继承自type
	# 先定义metaclass，就可以创建类，最后创建实例   metaclass允许你创建类或者修改类
	# ModelMetaclass元类定义了所有Model基类(继承ModelMetaclass)的子类实现的操作	
	# 任何继承自Model的类，都会自动通过ModelMetaclass扫描映射关系，并存储到自身的类属性
	
	# -*-ModelMetaclass的工作主要是为一个数据库表映射成一个封装的类做准备：
	# ***读取具体子类(user)的映射信息
	# 创造类的时候，排除对Model类的修改
	# 在当前类中查找所有的类属性(attresultset)，如果找到Field属性，就将其保存到__mappings__的dict中，同时从类属性中
	# 删除Field(防止实例属性遮住类的同名属性)
	# 将数据库表名保存到__table__中	

	# 完成这些工作就可以在Model中定义各种数据库的操作方法
class ModelMetaclass(type):
	# __new__控制__init__的执行，所以在其执行之前，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。
	    # cls: 当前准备创建的类的对象。代表要__init__的类，此参数在实例化时由Python解释器自动提供(例如下文的User和Model)
	    # name：当前准备创建的类的名称
	    # bases：代表继承父类的集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
	    # attresultset：类的方法集合
	    # 实例化类
    def __new__(cls, name, bases, attresultset):
	    #	
	    	# cls: 当前准备创建的类对象,相当于self
	        # name: 类名,比如User继承自Model,当使用该元类创建User类时,name=User
	        # bases: 父类的元组
	        # attrs: 属性(方法)的字典,比如User有__table__,id,等,就作为attrs的keys
	        # 排除Model类本身,因为Model类主要就是用来被继承的,其不存在与数据库表的映射
	    	# 如果是Model类直接返回,排除掉对Model类的修改
        if name=='Model':
            return type.__new__(cls, name, bases, attresultset)
        # 找到表名，若没有定义__table__属性,将类名作为表名
        tableName = attresultset.get('__table__', None) or name
        logging.info('found model: %s (table: %s)' % (name, tableName))
        # 建立映射关系表和找到主键
        mappings = dict()      # 用于保存映射关系
        fields = []            # 用于保存所有字段名
        primaryKey = None      # 保存主键
        # 遍历类的属性,找出定义的域(如StringField,字符串域)内的值,建立映射关系
        # key是属性名,val其实是定义域!请看name=StringField(ddl="varchar50")
        for k, v in attresultset.items():
        	# 判断val是否属于Field属性类
            if isinstance(v, Field):
                logging.info('  found mapping: %s ==> %s' % (k, v))
                # 把Field属性类保存在映射关系表
                mappings[k] = v
                # 找到了主键
                # 查找并检验主键是否唯一，主键初始值为None，找到一个主键后会被设置为k
                if v.primary_key:
                    # 找到主键:
                    # 如果此时类实例的已存在主键，说明主键重复了
                    if primaryKey:
                        raise StandardError('Duplicate primary key for field: %s' % k)
                    # 否则将此列设为列表的主键
                    primaryKey = k
                else:
                    fields.append(k) # 将非主键的属性名都保存到fields
        # end for

        if not primaryKey: # 没有找到主键也将报错
            raise StandardError('Primary key not found.')
        for k in mappings.keys():
            attresultset.pop(k)
        # 保存除主键外的属性名为``（运算出字符串）列表形式
        escaped_fields = list(map(lambda f: '`%s`' % f, fields))
        # 保存新的属性和列的映射关系
        attresultset['__mappings__'] = mappings # 保存映射关系表
        attresultset['__table__'] = tableName # 保存表名               
        attresultset['__primary_key__'] = primaryKey # 保存主键属性名      
        attresultset['__fields__'] = fields # 保存除主键外的属性名
        
        # 构造默认的SELECT、INSERT、UPDATE、DELETE语句
        # ``反引号功能同repr()
        attresultset['__select__'] = 'select `%s`, %s from `%s`' % (primaryKey, ', '.join(escaped_fields), tableName)
        attresultset['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (tableName, ', '.join(escaped_fields), primaryKey, create_args_string(len(escaped_fields) + 1))
        attresultset['__update__'] = 'update `%s` set %s where `%s`=?' % (tableName, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primaryKey)
        attresultset['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName, primaryKey)
        return type.__new__(cls, name, bases, attresultset)
# 定义Model类
	# 定义ORM所有映射的基类：Model
	# Model类的任意子类可以映射一个数据库表
	# Model类可以看作是对所有数据库表操作的基本定义的映射
	 
	# 基于字典查询形式
	# Model从dict继承，拥有字典的所有功能，同时实现特殊方法__getattr__和__setattr__，能够实现属性操作
	# 实现数据库操作的所有方法，定义为class方法，所有继承自Model都具有数据库操作方法
class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    #
    	# 增加__getattr__方法，使获取属性更加简单，即可通过"a.b"的形式
    	# __getattr__ 当调用不存在的属性时，python解释器会试图调用__getattr__(self, 'attr')来尝试获得属性
    	# 例如b属性不存在，当调用a.b时python会试图调用__getattr__(self, 'b')来获得属性，在这里返回的是a[b]对应的值
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)
     # 增加__setattr__方法，使设置属性更方便，可通过"a.b=c"的形式
    def __setattr__(self, key, value):
        self[key] = value
    # 通过键取值,若值不存在,则取默认值
    def getValue(self, key):
    	# 内建函数getattr会自动处理
        return getattr(self, key, None)

    def getValueOrDefault(self, key):
        value = getattr(self, key, None)
        if value is None:
            field = self.__mappings__[key]
            if field.default is not None:
            	# 如果field.default可被调用，则返回field.default()，否则返回field.default
                value = field.default() if callable(field.default) else field.default
                logging.debug('using default value for %s: %s' % (key, str(value)))
                # 通过default取到值之后再将其作为当前值
                setattr(self, key, value)
        return value

    # classmethod装饰器将方法定义为类方法
    # 一般来说，要使用某个类的方法，需要先实例化一个对象再调用方法。
    # 而使用@staticmethod或@classmethod，就可以不需要实例化，直接类名.方法名()来调用。
    # 这有利于组织代码，把某些应该属于某个类的函数给放到那个类里去，同时有利于命名空间的整洁。
    @classmethod
    # 类方法由类变量cls传入，从而可以用cls做一些相关的处理。并且有子类继承时，调用该类方法时，传入的类变量cls是子类，而非父类。
    async def findAll(cls, where=None, args=None, **kw):
        # find objects by where clause. 
        # 初始化SQL语句和参数列表
        sql = [cls.__select__]
        # WHERE 是查找条件的关键字
        if where:
            sql.append('where')
            sql.append(where)
        if args is None:
            args = []
        # ORDER BY是排序的关键字
        orderBy = kw.get('orderBy', None)
        if orderBy:
            sql.append('order by')
            sql.append(orderBy)
        # LIMIT 是筛选结果集的关键字
        limit = kw.get('limit', None)
        if limit is not None:
            sql.append('limit')
            if isinstance(limit, int): # 如果是int类型则增加占位符
                sql.append('?')
                args.append(limit)
            elif isinstance(limit, tuple) and len(limit) == 2: # limit可以取2个参数，表示一个范围
                sql.append('?, ?')
                args.extend(limit)
            else:
                raise ValueError('Invalid limit value: %s' % str(limit))
        resultset = await select(' '.join(sql), args) # 调用前面定义的select函数，没有指定size,因此会fetchall
        return [cls(**r) for r in resultset] # 返回结果，结果是list对象，里面的元素是dict类型的

    # 根据列名和条件查看数据库有多少条信息
    @classmethod
    async def findNumber(cls, selectField, where=None, args=None):
        # find number by select and where. 
        sql = ['select %s _num_ from `%s`' % (selectField, cls.__table__)]
        if where:
            sql.append('where')
            sql.append(where)
        resultset = await select(' '.join(sql), args, 1) # size = 1
        if len(resultset) == 0:
            return None
        return resultset[0]['_num_']

    # 根据主键查找一个实例的信息
    @classmethod
    async def find(cls, pk):
        # find object by primary key. 
        resultset = await select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pk], 1)
        if len(resultset) == 0:
            return None
        return cls(**resultset[0])

    # 把一个实例保存到数据库
    async def save(self):
        args = list(map(self.getValueOrDefault, self.__fields__))
        args.append(self.getValueOrDefault(self.__primary_key__))
        rows = await execute(self.__insert__, args)
        if rows != 1:
            logging.warn('failed to insert record: affected rows: %s' % rows)

    # 把一个实例从数据库中删除
    async def update(self):
        args = list(map(self.getValue, self.__fields__))
        args.append(self.getValue(self.__primary_key__))
        rows = await execute(self.__update__, args)
        if rows != 1:
            logging.warn('failed to update by primary key: affected rows: %s' % rows)

    async def remove(self):
        args = [self.getValue(self.__primary_key__)]
        rows = await execute(self.__delete__, args)
        if rows != 1:
            logging.warn('failed to remove by primary key: affected rows: %s' % rows)

"""
	if __name__ == '__main__':
	    class User(Model):
	        id = IntegerField('id',primary_key=True)
	        name = StringField('username')
	        email = StringField('email')
	        password = StringField('password')
	 
	    u = User(id=12345, name='point', email='point@python.org', password='password')
	    print(u)
	    
	    u.save() # 保存到数据库
	    print(u)	
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
		        charesultsetet=kw.get('charesultsetet', 'utf8'),
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
		        cur = yield from conn.curesultsetor(aiomysql.DictCuresultsetor)
		        yield from cur.execute(sql.replace('?', '%s'), args or ())
			        # SQL语句的占位符是?，而MySQL的占位符是%s，select()函数在内部自动替换。注意要始终坚持使用
			        # 带参数的SQL，而不是自己拼接SQL字符串，这样可以防止SQL注入攻击。			

			        # execute(self, query, args=None)
			        #     Executes the given operation
			        #     
			        #     Executes the given operation substituting any markeresultset with
			        #     the given parameteresultset.
			        #     
			        #     For example, getting all rows where id is 5:
			        #       curesultsetor.execute("SELECT * FROM t1 WHERE id = %s", (5,))
			        #     
			        #     :param query: ``str`` sql statement
			        #     :param args: ``tuple`` or ``list`` of arguments for sql query
			        #     :returns: ``int``, number of rows that has been produced of affected		
		        if size:
		            resultset = yield from cur.fetchmany(size)
		        else:
		            resultset = yield from cur.fetchall()
		        yield from cur.close()
		        logging.info('rows returned: %s' % len(resultset))
		        return resultset
	通用的execute函数--执行INSERT、UPDATE、DELETE语句
		要执行INSERT、UPDATE、DELETE语句，可以定义一个通用的execute()函数，因为这3种SQL的执行都需要相同
		的参数，以及返回一个整数表示影响的行数：		

		@asyncio.coroutine
		def execute(sql, args):
		    log(sql)
		    with (yield from __pool) as conn:
		        try:
		            cur = yield from conn.curesultsetor()
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
				        #     on the curesultsetor or the row count of the last operation if it
				        #     can't be determined by the interface.
		            affected = cur.rowcount
		            yield from cur.close()
		        except BaseException as e:
		            raise
		        return affected		

		execute()函数和select()函数所不同的是，curesultsetor对象不返回结果集，而是通过rowcount返回结果数。		
	ORM
		ORM全称“Object Relational Mapping”，即'对象-关系映射'
		就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，写代码更简单，不用直接操作SQL语句。
		要'编写一个ORM框架，所有的类都只能动态定义'，因为只有使用者才能根据表的结构定义出对应的类来。
		
		有了基本的select()和execute()函数，我们就可以开始编写一个简单的ORM了。
		设计ORM需要'从上层调用者角度'来设计。
		我们先考虑如何定义一个'User对象'，然后把数据库表useresultset和它关联起来。
		编写底层模块的第一步，就是先把调用接口写出来。比如，使用者如果使用这个ORM框架，想定义一个User类来
		操作对应的数据库表User，我们期待他写出这样的代码：		

		from orm import Model, StringField, IntegerField		

		class User(Model):
		    __table__ = 'useresultset'
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
		useresultset = User.findAll()
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

		        def __new__(cls, name, bases, attresultset):
		            # 排除Model类本身:
		            if name=='Model':
		                return type.__new__(cls, name, bases, attresultset)
		            # 获取table名称:
		            tableName = attresultset.get('__table__', None) or name
		            logging.info('found model: %s (table: %s)' % (name, tableName))
		            # 获取所有的Field和主键名:
		            mappings = dict()
		            fields = []
		            primaryKey = None
		            for k, v in attresultset.items():
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
		                attresultset.pop(k)
		            escaped_fields = list(map(lambda f: '`%s`' % f, fields))
		            attresultset['__mappings__'] = mappings # 保存属性和列的映射关系
		            attresultset['__table__'] = tableName
		            attresultset['__primary_key__'] = primaryKey # 主键属性名
		            attresultset['__fields__'] = fields # 除主键外的属性名
		            # 构造默认的SELECT, INSERT, UPDATE和DELETE语句:
		            attresultset['__select__'] = 'select `%s`, %s from `%s`' % (primaryKey, ', '.join(escaped_fields), tableName)
		            attresultset['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s)' % (tableName, ', '.join(escaped_fields), primaryKey, create_args_string(len(escaped_fields) + 1))
		            attresultset['__update__'] = 'update `%s` set %s where `%s`=?' % (tableName, ', '.join(map(lambda f: '`%s`=?' % (mappings.get(f).name or f), fields)), primaryKey)
		            attresultset['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName, primaryKey)
		            return type.__new__(cls, name, bases, attresultset)		
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
									        # TypeError: unbound method get_weight() must be called with C instance as firesultsett argument (got nothing instead)
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
		            resultset = yield from select('%s where `%s`=?' % (cls.__select__, cls.__primary_key__), [pk], 1)
		            if len(resultset) == 0:
		                return None
		            return cls(**resultset[0])		
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