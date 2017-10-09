#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a simple app frame'

__author__ = 'Point'

#
	# 异步方式构建网络应用（async web application.）
	# 在异步IO（asyncio）基础上用异步IO HTTP框架（aiohttp）写一个基本的应用程序（app.py）
    
	# logging模块 配置记录信息的级别，记录日志信息，输出日志信息
	# asyncio模块 异步IO, 基于协程(coroutine) 的异步IO库，提供事件循环的框架 ，使程序内部的子程序（函数）之间异步化，实现单线程并发IO操作
		
		# '协程' – coroutine (co+routine) or 微线程--一个线程执行--执行过程中断--通过generator实现
	# json模块 序列化数据
	# aiohttp外部模块 异步网络IO(async+io+http), 基于asyncio(异步IO) 的异步Web开发框架，基于协程的异步模型，实现网络程序IO异步化--用单线程+coroutine实现多用户的高并发支持
	
		# HTTP--超文本传输协议,WWW服务程序所用的协议
import logging; logging.basicConfig(level=logging.INFO) 
import asyncio
import os 
import json
import time 
from datetime import datetime
from aiohttp import web 

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>', content_type='text/html', charset='UTF-8')
	    # 通过web.py 模块调用 web_reqrep.py 模块内的 Response类，并创建实例web.Response(body=b'<h1>Awesome</h1>', content_type='text/html', charset='UTF-8') 
	    # 作为index函数的返回结果

	    # Response类的实例格式为 Response(self, *, body=None, status=200, reason=None, text=None, headers=None, content_type=None, charset=None)
	    # headers 默认 headers = CIMultiDict()

	    # body是网页要显示的内容 
	    # Content-Type 指定响应文本的内容类型，不指定 ，默认返回 application/octet-stream （ 二进制流，不知道下载文件类型）
	    # charset 决定网页的编码，决定文件接收方将以什么编码读取这个文件

async def init(loop):
    app = web.Application(loop=loop) 
    		# aiohttp.py 外部包-->web.py 子模块--> Application类--Application(self, *, logger=web_logger, loop=None, router=None, middlewares=(), debug=...) 类实例
    		# 参数 loop 为 命名关键字参数，默认值为 asyncio.get_event_loop()，该实例传入的值为 asyncio.get_event_loop()，见下方 loop = asyncio.get_event_loop()
    		# 创建类实例 app
    app.router.add_route('GET', '/', index)
    		# router 为该实例app的方法属性(@property)，该实例方法属性默认值为 router = web_urldispatcher.UrlDispatcher()
    		# web_urldispatcher.UrlDispatcher()  --> aiohttp 外部包 --> web_urldispatcher.py 子模块 --> UrlDispatcher类 --> UrlDispatcher() 类实例 router

    		# add_route 为该类实例 router 的实例方法 add_route(self, method, path, handler, *, name=None, expect_handler=None)
    		# 参数解释 （结合该实例）
		    	# 'GET' 表示请求方法 method， method = request.method，请求方法有head，get，post，put，patch，delete
		    	# '/' 表示url路径 path，这里是首页，url 以 / 开始和结束
		    	# index 表示调用处理函数 handler，上方已定义
		    	# 将浏览器通过GET方式传过来的对根目录的请求 转发给index函数处理
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
    logging.info('server started at http://127.0.0.1:9000...')
    return srv # srv 是 server 的简写

loop = asyncio.get_event_loop()
	# get_event_loop() 函数存在asyncio 包的 events.py 模块中，但asyncio包的下面有一个__init__模块，该包只要导入 asyncio 包 __init__.py 模块即自动运行
	# 该 __init__.py 模块中已提前导入了events.py 模块，所以可以通过 asyncio.get_event_loop() 的方式调用events模块中的get_event_loop() 函数
	
	# get_event_loop() 函数  返回结果是 接着调用 get_event_loop_policy().get_event_loop() 函数

	# 先调用 get_event_loop_policy() 函数 获得 run_until_complete() 方法和 run_forever() 方法
		# get_event_loop_policy() 函数 --> 调用 _init_event_loop_policy() 函数 --> 导入 asyncio.windows_events.py 或  asyncio.unix_events.py中的 DefaultEventLoopPolicy 变量
		# 这里机智的实现了对不同操作系统的选择，实现了对不同系统的兼容，具体实现 暂不细究，这里选择 _WindowsDefaultEventLoopPolicy 
		# DefaultEventLoopPolicy = _WindowsDefaultEventLoopPolicy -- 该变量名对应 _WindowsDefaultEventLoopPolicy 类
		
		# _WindowsDefaultEventLoopPolicy类的父类AbstractEventLoopPolicy 定义了 get_event_loop(self) 方法，该方法调用后 抛出错误
		# 当然，这里一般不会执行到该父类的 get_event_loop(self) 方法，因为 get_event_loop_policy() 函数内的操作相当于一个无限循环，所以一般不会抛出错误
		
		# _WindowsDefaultEventLoopPolicy 类内部 会继续执行代码 _loop_factory = SelectorEventLoop
		# SelectorEventLoop = _WindowsSelectorEventLoop -- 该变量名对应 _WindowsSelectorEventLoop 类 -- Windows version of selector event loop.
		# 该类父类为 asyncio.selector_events.BaseSelectorEventLoop,  BaseSelectorEventLoop 的父类为 asyncio.base_events.BaseEventLoop

		# BaseEventLoop类 定义了 stop(self)， _check_closed(self)，run_forever(self)，run_until_complete(self, future)，close(self)，is_closed(self)，is_running(self)等方法以供
		# 其实例或继承者的实例调用

		# 即 asyncio.get_event_loop() 首先调用get_event_loop_policy() 函数 返回 asyncio.base_events.BaseEventLoop类的 实例
	# 由于后面调用asyncio.base_events.BaseEventLoop类的 实例 方法基本上是无限循环，所以 get_event_loop_policy().get_event_loop() 函数中的后半部分不会被执行到

	# 流程
	# loop <-- asyncio.get_event_loop() -- get_event_loop_policy().get_event_loop() -- get_event_loop_policy() <--  _init_event_loop_policy() <-- DefaultEventLoopPolicy
	# --  类_WindowsDefaultEventLoopPolicy (-- get_event_loop(self) ) -- SelectorEventLoop -- 类_WindowsSelectorEventLoop <-- 父类asyncio.selector_events.BaseSelectorEventLoop
	# <-- 父类asyncio.base_events.BaseEventLoop

	# 故 asyncio.get_event_loop() 是创建 asyncio.base_events.BaseEventLoop类的实例 赋给变量 loop
loop.run_until_complete(init(loop))
	# loop实例调用 BaseEventLoop类 中的 run_until_complete(self, future) 方法

	# run_until_complete(init(loop)) 函数 是 asyncio.base_events.py 模块中 BaseEventLoop类 的实例方法 run_until_complete(self, future)，Run until the Future is done.
	#  If the argument is a coroutine, it is wrapped in a Task. It would be disastrous to call run_until_complete() with the same coroutine twice -- it would wrap it in two
	# different Tasks and that can't be good.
	# 返回结果是 future.result() 或抛出错误（raise its exception） -- Return the Future's result, or raise its exception.
	# 这里返回 init(loop).result() 或者运行被强制关闭后抛出错误 RuntimeError: Event loop is closed
loop.run_forever()
	# loop实例调用 BaseEventLoop类 中的 run_forever(self) 方法
	# loop.run_forever() 函数 是 asyncio.base_event.ase模块中 BaseEventLoop类 的实例方法 run_forever(self)，Run until stop() is called.

# def tip():
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