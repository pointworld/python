#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'async web application.'

__author__ = 'Point'

import logging; logging.basicConfig(level=logging.INFO,
        format="%(asctime)s %(message)s",  # display date
        datefmt="[%Y-%m-%d %H:%M:%S]")
        # logging模块定义了一些函数和模块，可以帮助我们对一个应用程序或库实现一个灵活的事件日志处理系统
        # logging模块可以纪录错误信息，并在错误信息记录完后继续执行
        # 设置logging的默认level为INFO
        # 日志级别大小关系为：CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET
import asyncio, os, json, time
        # asyncio 内置了对异步IO的支持, 提供事件循环的框架 ，使程序内部的子程序（函数）之间异步化
        # os模块提供了调用操作系统的接口函数
        # json模块提供了Python对象到Json模块的转换, 序列化数据
        # time模块提供各种操作时间的函数
from datetime import datetime
from aiohttp import web
        # aiohttp是基于asyncio实现的http框架
        # aiohttp模块 网络应用框架使用了基于asyncio的aiohttp，这是基于协程（coroutine，微线程）的异步模型，实现网络程序异步化
from jinja2 import Environment, FileSystemLoader
        # Jinja2 是仿照 Django 模板的 Python 前端引擎模板
        # Environment指的是jinjia2模板的配置环境，FileSystemLoader是文件系统加载器，用来加载模板路径
import orm
from coroweb import add_routes, add_static

'''
# 这是一个使用aiohttp的简单例子
        def index(request):
            return web.Response(body=b'<h1>Awesome</h1>')
        @asyncio.coroutine
        def init(loop):
            app = web.Application(loop=loop)
            app.router.add_route('GET', '/', index)
            srv = yield from loop.create_server(app.make_handler(), '127.0.0.1', 9000)
            logger.info('server started at http://127.0.0.1:9000...')
            return srv
        loop = asyncio.get_event_loop()
        loop.run_until_complete(init(loop))
        loop.run_forever()'''

# 异步方式构建网络应用（async web application.）
# 在异步IO（asyncio）基础上用异步IO HTTP框架（aiohttp）写一个基本的应用程序（app.py）

# 初始化jinja2模板，配置jinja2的环境，最后配置好后把信息env 以 app['__templating__'] = env  的形式存储在 app中
def init_jinja2(app, **kw):
    logging.info('init jinja2...')
    # 设置解析模板需要用到的环境参数
    options = dict( # 后面的 init_jinja2(app, filters=dict(datetime=datetime_filter)) 调用的关键字参数中不存在以下值，故全为默认值
        autoescape = kw.get('autoescape', True), # 自动转义xml/html的特殊字符，默认 autoescape = True
        # 下面两句的意思是{%和%}中间的是python代码而不是html
        block_start_string = kw.get('block_start_string', '{%'), # 代码块开始标志，默认 block_start_string = '{%'
        block_end_string = kw.get('block_end_string', '%}'), # 代码块结束标志，默认 block_end_string = '%}'
        variable_start_string = kw.get('variable_start_string', '{{'), # 变量开始标志，默认 variable_start_string = '{{'
        variable_end_string = kw.get('variable_end_string', '}}'), # 变量结束标志，默认 variable_end_string = '}}'
        auto_reload = kw.get('auto_reload', True)  # 每当对模板发起请求, 加载器首先检查模板是否发生改变.若是,则重载模板，默认 auto_reload = True
    )
    path = kw.get('path', None)  # 后面的 init_jinja2(app, filters=dict(datetime=datetime_filter)) 调用的关键字参数中不存在以下值，故为默认值 None
    #从参数中获取path字段，即模板文件的位置
    if path is None:  
    # 如果没有，则默认为当前文件目录下的 templates 目录      
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
                # os.path.abspath(__file__), 返回当前脚本的绝对路径(包括文件名)
                # os.path.dirname(), 去掉文件名,返回目录路径
                # os.path.join(), 将分离的各部分组合成一个路径名
                # 若路径不存在,则将当前目录下的templates(www/templates/)设为jinja2的目录
    logging.info('set jinja2 template path: %s' % path)
    env = Environment(loader=FileSystemLoader(path), **options)
                # loader 默认值为None，这里赋值为 FileSystemLoader(path)
                # FileSystemLoader是一个类，存在于janja2.loders.py中，
                # Loads templates from the file system.  This loader can find templates in folders on the file system and is the preferred way to load them.
                # 加载器负责从指定位置加载模板, 此处选择FileSystemLoader, 顾名思义就是从文件系统加载模板,前面我们已经设置了path
                
                # Environment是jinjia2中的一个核心类，参见 jinjia2.environment.py，它的实例用来保存配置、全局对象以及模板文件的路径
                # loader=FileSystemLoader(path)指的是到哪个目录下加载模板文件， **options就是前面的options
    # 设置过滤器
                # 先通过filters关键字参数获取过滤字典
                # 再通过建立env.filters的键值对建立过滤器   
    filters = kw.get('filters', None)  
                # 后面的 init_jinja2(app, filters=dict(datetime=datetime_filter)) 调用的关键字参数中存在filters值，故为值为 dict(datetime=datetime_filter)
                # datetime_filter 函数返回的结果只是一段时间字符串（如'一分钟前'）
                # 故类似 datetime= '一分钟前'，dict(datetime=datetime_filter) 即返回 {'datetime' : '一分钟前'}，即 filters = {'datetime' : '一分钟前'}
                # filters: 一个字典描述的filters过滤器集合, 如果非模板文件被加载的时候, 可以安全的添加或较早的移除.
    if filters is not None:
        for name, f in filters.items(): # 循环遍历filters项，将filters项的键和值添加到env的filters属性中
            env.filters[name] = f  
                    # env.filters -- env 是 Environment类的实例，filters 是 该实例的属性，注意区分该filters属性不是env实例里面的参数
                    # env实例属性filters的默认值见 jinjia2.filters 里的FILTERS(是一个字典)
                    # 故这里不是给env赋予属性filters 而是给 env的filters属性增加新的字典项
    app['__templating__'] = env 
                # app是aiohttp.web模块中Application类的实例，Appication 类定义的__init__构造构造方法内加入了一个实例属性值为字典的方法（self._state = {}）
                # 又定义了__getitem__魔法（return self._state[key]）和__setitem__魔法（self._state[key] = value）两个黑暗魔法，故可以给Application 类的实例app增加这样类似字典的操作方法：app['__templating__'] = env  
                # 通过obj[key]的方式来访问，设置和添加类实例属性_state 中的字典项
                # 注意--仅限于init，getitem和setitem方法中共同的对象（如上面的_state，如下面的d），通过这种方式访问和设置都是针对于该对象，值也是存储在该对象中
                # 魔术方法示例如下
                                    # class A(object):
                                    #  def __init__(self):
                                    #   self.d={} 
                                    #  def __getitem__(self, key):
                                    #   return self.d[key]
                                    #  def __setitem__(self,key,value):
                                    #   self.d[key]=value
                                    # a=A()
                                    # a['b']=2
                                    # a['b']
                                    # 2
    # 前面已经把jinjia2的环境配置都赋值给env了，这里再把env存入app的_state属性中（该属性值类型为字典），这样app就知道要去哪找模板，怎么解析模板

# 给webapp设置模板    
#============================请求对象（request）的处理工序--工厂模式===================================
# 请求对象request的处理工序流水线先后依次是：
        # logger_factory->response_factory->RequestHandler().__call__->get或post->handler
        
        # 创建应用时,通过指定命名关键字为一些"middle factory"的列表可创建中间件Middleware
        # 每个middle factory接收2个参数,一个app实例,一个handler, 并返回一个新的handler
        # 以下是一些middleware(中间件), 可以在url处理函数处理前后对url进行处理

# 在处理请求之前,先记录日志，记录完后继续处理请求
# 这个函数的作用就是当http请求的时候，通过logging.info输出请求的信息，其中包括请求的方法和路径
async def logger_factory(app, handler):
    async def logger(request):
        # 记录日志,包括http method, 和path
        logging.info('Request: %s %s' % (request.method, request.path))
        # await asyncio.sleep(0.3)
        # 日志记录完毕之后, 调用传入的handler继续处理请求
        return (await handler(request))
    return logger

# 在处理请求之前,先将cookie解析出来,并将登录用于绑定到request对象上，继续处理请求
        # 这样后续的url处理函数就可以直接拿到登录用户
        # 以后的每个请求,都是在这个middle之后处理的,都已经绑定了用户信息
async def auth_factory(app, handler):
    async def auth(request):
        logging.info("check user: %s %s" % (request.method, request.path))
        request.__user__ = None # 先绑定一个None到请求的__user__属性
        cookie_str = request.cookies.get(COOKIE_NAME) # 通过cookie名取得加密cookie字符串(不明白的看看handlers.py)
        # 获取到cookie字符串, cookies是用分号分割的一组名值对，在python中被看成dict
        if cookie_str:
            user = await cookie2user(cookie_str) # 验证cookie,并得到用户信息
            # 通过反向解析字符串和与数据库对比获取出user
            if user:
                logging.info("set current user: %s" % user.email)
                request.__user__ = user # 将用户信息绑定到请求上
            # 请求的路径是管理页面,但用户非管理员,将会重定向到登录页面?
            # user存在则绑定到request上
        if request.path.startswith('/manage/') and (request.__user__ is None or not request.__user__.admin):
            return web.HTTPFound('/signin')
            # 继续执行下一步
        return (await handler(request))
    return auth
 
# 在处理请求之前，解析数据--只有当请求方法为POST时这个函数才起作用，继续处理请求
async def data_factory(app, handler):
    async def parse_data(request):
        # 解析数据是针对post方法传来的数据,若http method非post,将跳过,直接调用handler处理请求
        if request.method == 'POST':
            # content_type字段表示post的消息主体的类型, 以application/json打头表示消息主体为json
            # request.json方法,读取消息主题,并以utf-8解码
            # 将消息主体存入请求的__data__属性            
            if request.content_type.startswith('application/json'):
                request.__data__ = await request.json()
                logging.info('request json: %s' % str(request.__data__))
            # content type字段以application/x-www-form-urlencodeed打头的,是浏览器表单
            # request.post方法读取post来的消息主体,即表单信息                
            elif request.content_type.startswith('application/x-www-form-urlencoded'):
                request.__data__ = await request.post()
                logging.info('request form: %s' % str(request.__data__))
        # 调用传入的handler继续处理请求                
        return (await handler(request))
    return parse_data

# ***********************************************响应处理（重点，重点，重点，重要的事说三遍）***************************************************
# 总结一下
            # 请求对象request的处理工序流水线先后依次是：
            #       logger_factory->response_factory->RequestHandler().__call__->get或post->handler
            # 对应的响应对象response的处理工序流水线先后依次是:
            #       由handler构造出要返回的具体对象
            #       然后在这个返回的对象上加上'__method__'和'__route__'属性，以标识别这个对象并使接下来的程序容易处理
            #       RequestHandler目的就是从请求对象request的请求content中获取必要的参数，调用URL处理函数,然后把结果返回给response_factory
            #       response_factory在拿到经过处理后的对象，经过一系列类型判断，构造出正确web.Response对象，以正确的方式返回给客户端
            # 在这个过程中，我们只用关心我们的handler的处理就好了，其他的都走统一的通道，如果需要差异化处理，就在通道中选择适合的地方添加处理代码。
            # 注： 在response_factory中应用了jinja2来渲染模板文件
# 上面factory是在url处理函数之前先对请求进行了处理,以下则在url处理函数之后进行处理

# 其将request handler的返回值转换为web.Response对象
async def response_factory(app, handler):
    async def response(request):
        logging.info('Response handler...')
        r = await handler(request)
                    # 调用handler来处理url请求,并返回响应结果
                    # 调用相应的URL处理函数处理请求
        if isinstance(r, web.StreamResponse):
                # 如果相应结果为StreamResponse，直接返回
                # StreamResponse是aiohttp定义response的基类,即所有响应类型都继承自该类，定义在aiohttp.web_reqrep.py中
                # StreamResponse主要为流式数据而设计            
            return r
        if isinstance(r, bytes):
        # 如果相应结果为字节流，则将其作为应答的body部分，并设置响应类型为流型
        # 如果响应结果为字节流，则把字节流塞到response的body里，设置响应类型为流类型，返回 
            resp = web.Response(body=r)
            resp.content_type = 'application/octet-stream'
            return resp
        if isinstance(r, str):
        # 如果响应结果为字符串
            if r.startswith('redirect:'):
                # 先判断是不是需要重定向，是的话直接用重定向的地址重定向
            # 判断响应结果是否为重定向，如果是，返回重定向后的结果                
                return web.HTTPFound(r[9:]) # 即把r字符串之前的"redirect:"去掉
            resp = web.Response(body=r.encode('utf-8'))
            # 然后以utf8对其编码，并设置响应类型为text/html型
            resp.content_type = 'text/html;charset=utf-8'
            return resp
        if isinstance(r, dict):
            # 先查看一下有没有'__template__'为key的值
        # 如果响应结果是字典，则获取他的jinja2模板信息，此处为jinja2.env
            template = r.get('__template__')
            if template is None:
                # 如果没有，说明要返回json字符串，则把字典转换为json返回，对应的response类型设为json类型
            # 若不存在对应模板，则将字典调整为json格式返回，并设置响应类型为json
                resp = web.Response(body=json.dumps(r, ensure_ascii=False, default=lambda o: o.__dict__).encode('utf-8'))
                resp.content_type = 'application/json;charset=utf-8'
                return resp
            else:
                r["__user__"] = request.__user__  
                # 增加__user__,前端页面将依次来决定是否显示评论框
                # 在__base__.html中会根据__user__设置用户相关信息
                # 如果有'__template__'为key的值，则说明要套用jinja2的模板，'__template__'Key对应的为模板文件名
                # 得到模板文件然后用**r去渲染render                
                resp = web.Response(body=app['__templating__'].get_template(template).render(**r).encode('utf-8'))
                resp.content_type = 'text/html;charset=utf-8'
                return resp            
        if isinstance(r, int) and r >= 100 and r < 600:
        # 如果响应结果为整数型，且在100和600之间
        # 则此时r为状态码，即404，500等                
            return web.Response(r)
        if isinstance(r, tuple) and len(r) == 2:
        # 如果响应结果为长度为2的元组
        # 元组第一个值为整数型且在100和600之间
        # 则t为http状态码，m为错误描述，返回状态码和错误描述            
            t, m = r # status_code, description = r
            # 如果tuple的第一个元素是int类型且在100到600之间，这里应该是认定为status_code为http状态码，description为描述
            if isinstance(t, int) and t >= 100 and t < 600:
                return web.Response(t, str(m))
        # default:
        resp = web.Response(body=str(r).encode('utf-8'))
        # 默认以字符串形式返回响应结果，设置类型为普通文本
        resp.content_type = 'text/plain;charset=utf-8'
        return resp
    #上面6个if其实只用到了一个，准确的说只用到了半个。大家可以把用到的代码找出来，把没有用到的注释掉，如果程序能正常运行，那我觉得任务也就完成了
    #没用到的if语句块了解一下就好，等用到了再回过头来看，你就瞬间理解了。        
    return response
# 时间过滤器，作用是返回日志创建的时间，用于显示在日志标题下面
def datetime_filter(t): # 返回一个时间字符串
    # 定义时间差
    delta = int(time.time() - t)
    # time.time()取得当前时间（新纪元开始后的秒数）
    # 针对时间分类
    if delta < 60:
        return u'1分钟前'
                # 以u或U开头的字符串表示unicode字符串
                # Unicode是书写国际文本的标准方法。如果你想要用非英语写文本,那么你需要有一个支持Unicode的编辑器。
                # 类似地,Python允许你处理Unicode文本——你只需要在字符串前加上前缀u或U。
                # 举例：
                # u"This is a Unicode st以u或U开头的字符串表示unicode字符串"     
    if delta < 3600:
        return u'%s分钟前' % (delta // 60)
        # 双斜线表示整除
    if delta < 86400:
        return u'%s小时前' % (delta // 3600)
    if delta < 604800:
        return u'%s天前' % (delta // 86400)
    dt = datetime.fromtimestamp(t)
    return u'%s年%s月%s日' % (dt.year, dt.month, dt.day)
# 调用asyncio实现异步IO, 初始化
    # middlewares(中间件)设置3个中间处理函数(都是装饰器)
    # middlewares中的每个factory接受两个参数，app 和 handler(即middlewares中的下一个handler)
    # 譬如这里logger_factory的handler参数其实就是auth_factory
    # middlewares的最后一个元素的handler会通过routes查找到相应的，其实就是routes注册的对应handler
    # 这其实是装饰模式的典型体现，logger_factory, auth_factory, response_factory都是URL处理函数前（如handler.index）的装饰功能
async def init(loop):
    # 创建全局数据库连接池
    await orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='www-data', password='www-data', db='awesome')
    # 创建app对象，同时传入上文定义的拦截器middlewares
    # 创建web应用
    app = web.Application(loop=loop, middlewares=[
        logger_factory, response_factory
    ])
    # 初始化jinja2模板，并传入时间过滤器
    init_jinja2(app, filters=dict(datetime=datetime_filter))
    # 下面这两个函数在coroweb模块中
    # 注册所有url处理函数
    add_routes(app, 'handlers') # handlers指的是handlers模块也就是handlers.py
    # 将当前目录下的static目录加入app目录    # 添加CSS等静态文件路径
    add_static(app)
    # 调用子协程:创建一个TCP服务器,绑定到"127.0.0.1:9000"socket,并返回一个服务器对象
    # 启动
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv
# 入口，固定写法
# 获取eventloop然后加入运行事件
# get_event_loop()函数详见python官方文档18.5.2.5
# get_event_loop() => 获取当前脚本下的事件循环，返回一个event loop对象(这个对象的类型是'asyncio.windows_events._WindowsSelectorEventLoop')，实现AbstractEventLoop（事件循环的基类）接口
# 如果当前脚本下没有事件循环，将抛出异常，get_event_loop()永远不会抛出None
loop = asyncio.get_event_loop()# loop是一个消息循环对象
# 之后是执行curoutine
loop.run_until_complete(init(loop))#在消息循环中执行协程
# 无限循环运行直到stop()
loop.run_forever()

"""
	运行python app.py
	    '''
	    Web App将在9000端口监听HTTP请求，并且对首页/进行响应：
	    $ python3 app.py
	    INFO:root:server started at http://127.0.0.1:9000...
	    '''
	logging模块 -- 提供了灵活的日志处理相关功能, 可以用来追踪程序运行的情况	
	    '''
		记录错误,后续代码继续执行， logging不会抛出错误，而且可以输出到文件	
		logging的好处，它允许你指定记录信息的级别：
		  你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。
		  logging 模块提供了一系列标准的日志等级: DEBUG, INFO, WARNING, ERROR, CRITICAL, 顾名思义可以
		  大致看出它们各自的使用情况。 logging 模块设置的默认等级时 WARNING, 这意味着默认情况下，日志
		  级别为 WARNING, ERROR, CRITICAL 的日志会被记录，而 DEBUG, INFO 的日志会被忽略。	
		  不同等级的value值如下，只有当value大于或等于 logger 的值才会记录日志。
		     Level    Value
		     CRITICAL 50
		     ERROR    40
		     WARNING  30
		     INFO     20
		     DEBUG    10
		     UNSET     0
		 
		     e.g.:
		        >>> import logging; logging.basicConfig(level = logging.INFO)
		        >>> logging.info('info will be shown!')
		        INFO:root:info will be shown!
		        >>> logging.debug('debug will not be shown!')
		        >>> logging.warning('warning will be shown!')
		        WARNING:root:warning will be shown!		

		logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。	
		     import logging
		     logging.basicConfig(filename='D:\\computer_learning\\awesome-python3-webapp\\www\\example.log',level=logging.DEBUG)
		     logging.debug('This message should go to the log file')
		     logging.info('So should this')
		     logging.warning('And this, too')	
		  其中level是指的'记录等级'，当执行该段程序时，会在上述指定路径下的example.log中记录如下：
		  DEBUG:root:This message should go to the log file
		  INFO:root:So should this
		  WARNING:root:And this, too		

		logger是logging模块提供的日志类 Logger 的实例，它暴露出接口可以直接供程序调用。	
		每个实例都有一个名字，并且实例间有类之间那种继承关系，根据logger的名字来区分，比如叫
		"scan"的logger是叫"scan.text"和"scan.html"的父类(没错，他们是以点号做分隔符)。	
		所有logger共同的父类是 root , 就是上面示例中的中间那个默认的root。 
		'basicConfig 默认的输出格式为: severity:logger name:message 。'
		Logger是通过 logging.getLogger(name) 来创建，有种在包里命名的惯用做法是：
		logger = logging.getLogger(__name__)
		这样的好处是可以从logger的名字清楚的看到记录的来源。
	    '''
	json内置库	
	    '''
	 	'JSON(JavaScript Object Notation)' 是一种轻量级的数据交换格式,'序列化数据'。易于人阅读和编写。
		 同时也易于机器解析和生成。它基于JavaScript Programming Language, JSON采用完全独立于语言的文本格
		 式，但是也使用了类似于C语言家族的习惯（包括C, C++, 'C#', Java, JavaScript, Perl, Python等）。
		 这些特性使JSON成为理想的'数据交换语言'
		  
		   实际上'JSON就是Python字典的字符串表示'，但是字典作为一个复杂对象是无法直接传递，所以需要
		   将其转换成字符串形式，转换的过程也是一种序列化过程。需要注意的是，'Python内置json模块序'
		   '列化时，字符串中的字典类型的键名必须是英文双引号的格式'	

		   json模块中还有load和dump方法，与loads和dumps的区别是前者是从文件中读取需要处理的对象。
		 
		JSON建构于两种结构：
		 名称/值”对的集合(A collection of name/value pairs)
		   不同的语言中，它被理解为对象(object)，纪录(record)，结构(struct)，字典(dictionary)，
		   哈希表(hash table)，有键列表(keyed list)，或者关联数组 (associative array)。
		  
		 值的有序列表(An ordered list of values)
		   在大部分语言中，它被理解为数组(array)
		'''
	asyncio库 -- 基于coroutine的异步IO库	
		'''
		asyncio库一个重要的概念就是'事件循环'，事件循环就是等待一些任务发生，然后执行相应的事件。
		它也会处理例如IO操作或者系统事件。asyncio实际中有好几种循环实现方式。模块默认使用的方式是
		其所运行的操作系统上最有效的方式。如果你愿意，你也可以显式地选择其它事件循环方式。一个事件
		循环就是当事件A发生时，函数B共同起作用。只有启动事件循环以后，才可以让coroutine任务得以继续执
		行，如果event loop停止或者暂停，那么整个异步io也停止或者暂停，类似于操作系统的事件循环机制	

		asyncio的内部是基于selector(也可能是epoll)或者windows iocp来实现的，这也是为什么需要启动一
		个event loop，'event loop可以看成是对各个平台的异步IO"等待"这个操作的封装'	

		cotoutine 函数
		coroutine即为一个支持写成的函数，可以利用iscoroutinefunction来判断是否coroutine函数，这个函
		数需要@asyncio.coroutine来修饰
		利用@asyncio.coroutine修饰以后，这个函数可以支持await(python 3.5) 或者 yield from语法,一旦
		执行yield from 语法以后，asyncio将会挂起当前的coroutine，去执行其他的coroutine	

		在3.5中，新增加了'async以及await的语法，用于代替asynio.coroutine以及yield from'
		在Python 3.4中，你可以按照如下方式创建一个协程，	

		import asyncio	

		@asyncio.coroutine
		def my_foo():
		    yield from func()
		这个装饰器在Python 3.5中依然有效，但是模块的类型有所更新，协程函数可以告诉你正在交互的是不
		是一个原生的协程。从Python 3.5开始，你可以使用async def这种语法来定义一个协程函数，所以上述
		函数可以按照如下方式定义，	

		import asyncio	

		async def my_coro():
		    await func()
		当你以这种方式定义一个协程函数，你不能在函数内部使用yield。取而代之，你必须使用return或者
		await语句，用于将返回值返回给调用者。你需要注意的是，关键字await只能在async def函数中使用。	

		'关键字async和await可以认为是异步编程中的接口。'
		'''
	aiohttp 外部库	
		'''
		aiohttp是基于asyncio实现的HTTP框架, aiohttp 是 asyncio 的 HTTP 客户端/服务端 	

		利用 aiohttp 来构造一个最简单的web服务器是非常轻松的事情，只需要下面几行代码就可以搞定：
		from aiohttp import web
		import asyncio
		 
		def index(request):
		    return web.Response(body=b'<h1>Hello World!</h1>', content_type='text/html', charset='UTF-8')
		 
		async def init(loop):
		    app = web.Application(loop=loop)
		    app.router.add_route('GET', '/index', index) # '/' 表示路径，这里是定位到index函数
		    server = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
		    return server
		 
		def main():
		    loop = asyncio.get_event_loop()
		    loop.run_until_complete(init(loop))
		    loop.run_forever()
		 
		if __name__ == '__main__':
		    main()
		这样就实现了一个最简单的 web 服务器
		运行这个 python 文件，再打开浏览器，在地址栏输入 http://127.0.0.1:8000/index 你就能看见 
		Hello World 了。
		当用户在浏览器输入 http://127.0.0.1:8000/index 的时候，服务器究竟是怎么把请求定位到我们的
		url 处理函数 index(request) 里的呢？是因为有 app.router.add_route('GET', '/index', index)
		服务器才知道，你的 request 请求(method:GET path:/index) 需要让 index(request)函数来处理。	

		那么行代码的内部究竟做了什么？服务器是如何响应一个request请求的呢？	
		'''
	Content-Type	
		'''
		Content-Type指示响应的内容，这里是text/html表示HTML网页
		通常服务器的HTTP响应会携带内容，也就是有一个Body，包含响应的内容，网页的HTML源码就在Body中
		Web采用的HTTP协议采用了非常简单的请求-响应模式, 当我们编写一个页面时，我们只需要在HTTP请求
		中把HTML发送出去
		HTTP协议同时具备极强的扩展性, 从而将请求压力分散到各个服务器上，并且，一个站点可以链接到其
		他站点，无数个站点互相链接起来，就形成了World Wide Web，简称WWW。	

		  Web应用的本质
		   浏览器发送一个HTTP请求；
		   服务器收到请求，生成一个HTML文档；
		   服务器把HTML文档作为HTTP响应的Body发送给浏览器；
		   浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示	

		不指定 content_type 的话，默认返回 application/octet-stream ，也就是返回文件是“.*（ 二进制流，
		不知道下载文件类型）” 没有扩展名，浏览器没法正常解读。
		'''
	"""    