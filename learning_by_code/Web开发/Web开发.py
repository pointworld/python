'Web开发'--HTML()定义了页面的内容，CSS()来控制页面元素的样式，JavaScript()负责页面的交互逻辑
HTTP接口()--WSGI框架()--Web框架()
CSS(Cascading Style Sheets层叠样式表)--用来控制HTML里的所有元素如何展现
JavaScript()--JavaScript负责HTML页面的交互逻辑，为了让HTML具有交互性而作为脚本语言添加的，既可内嵌到HTML中，也可外链HTML中
HTTP(Hypertext Transfer Protocol 超文本传送协议)--是在网络上传输HTML的协议，用于浏览器和服务器的通信--具备极强的扩展性，可以链入其他服务器的资源
	HTTP请求的流程：

		步骤1：浏览器首先向服务器发送HTTP请求，请求包括：

			方法：GET还是POST，表示一个读取请求，将从服务器获得网页数据，GET仅请求资源，POST会附带用户数据；

			路径：/表示URL的路径，URL总是以/开头，/就表示首页；最后的HTTP/1.1指示采用的HTTP协议版本是1.1；

			域名：由Host头指定：Host: www.sina.com.cn

			以及其他相关的Header；

			如果是POST，那么请求还包括一个Body，包含用户数据。
		步骤2：服务器向浏览器返回HTTP响应，响应包括：

			响应代码：200表示成功，3xx表示重定向，4xx表示客户端发送的请求有错误，5xx表示服务器端处理时发生了错误；

			响应类型：由Content-Type指定；text/html表示HTML网页；浏览器依靠Content-Type来判断响应的内容是网页还是图片，是视频还是音乐。浏览器并不靠URL来判断响应的内容

			以及其他相关的Header；

			通常服务器的HTTP响应会携带内容，也就是有一个Body，包含响应的内容，网页的HTML源码就在Body中。
		步骤3：如果浏览器还需要继续向服务器请求其他资源，比如图片，就再次发出HTTP请求，重复步骤1、2。
	HTTP格式

		HTTP协议是一种文本协议，每个HTTP请求和响应都遵循相同的格式，一个HTTP包含Header和Body两部分，其中Body是可选的。

		HTTP GET请求的格式：

			GET /path HTTP/1.1
			Header1: Value1
			Header2: Value2
			Header3: Value3
			每个Header一行一个，换行符是\r\n。
		HTTP POST请求的格式：

			POST /path HTTP/1.1
			Header1: Value1
			Header2: Value2
			Header3: Value3

			body data goes here...
		当遇到连续两个\r\n时，Header部分结束，后面的数据全部是Body
		HTTP响应的格式：

			200 OK
			Header1: Value1
			Header2: Value2
			Header3: Value3

			body data goes here...

			HTTP响应如果包含body，也是通过\r\n\r\n来分隔的。请再次注意，Body的数据类型由Content-Type头来确定，如果是网页，Body就是文本，
			如果是图片，Body就是图片的二进制数据。

			当存在Content-Encoding时，Body数据是被压缩的，最常见的压缩方式是gzip，所以，看到Content-Encoding: gzip时，需要将Body数据先解压缩，
			才能得到真正的数据。压缩的目的在于减少Body的大小，加快网络传输。
HTML(Hypertext Markup Language 超文本链接标示语言)--是一种用来定义网页的文本，服务器把网页传给浏览器，就是把网页的HTML代码发送给浏览器，会HTML，就可以编写网页

CS架构--Client/Server模式
BS架构()--Browser/Server模式

Web应用的本质()
	浏览器发送一个HTTP请求；

	服务器收到请求，生成一个HTML文档；

	服务器把HTML文档作为HTTP响应的Body发送给浏览器；

	浏览器收到HTTP响应，从HTTP Body取出HTML文档并显示。
'最简单的Web应用'--先把HTML用文件保存好，用一个现成的HTTP服务器软件，接收用户请求，从文件中读取HTML，返回。
'Web的HTTP协议'--采用请求-响应模式。
	当我们编写一个页面时，我们只需要在HTTP请求中把HTML发送出去，不需要考虑如何附带图片、视频等，
	浏览器如果需要请求图片和视频，它会发送另一个HTTP请求，因此，一个HTTP请求只处理一个资源。
WSGI框架(Web Server Gateway Interface)--web 组件的接口规范
	接受HTTP请求、解析HTTP请求、发送HTTP响应都是苦力活，这些底层代码可由专门的服务器软件实现，我们用Python专注于生成HTML文档。
	因为我们不希望接触到TCP连接、HTTP原始请求和响应格式，所以，需要一个统一的接口，让我们专心用Python编写Web业务。
	定义
		wsgi 是一个 web 组件的接口规范. wsgi将 web 组件分为三类: web服务器,web中间件,web应用程序. 其目标是提高web组件的可重用性. wsgi 的设计目标
		是适合尽可能广泛的web应用, 较原始.

	实现--WSGI接口定义非常简单，它只要求Web开发者实现一个函数，就可以响应HTTP请求。
		我们来看一个最简单的Web版本的“Hello, web!”：

		def application(environ, start_response):
		    start_response('200 OK', [('Content-Type', 'text/html')])
		    return [b'<h1>Hello, web!</h1>']

		application()函数就是符合WSGI标准的一个HTTP处理函数，它接收两个参数：

			environ：一个包含所有HTTP请求信息的dict对象；
			start_response：一个发送HTTP响应的函数。
		在 application()函数中，调用：

		start_response('200 OK', [('Content-Type', 'text/html')])
		就发送了HTTP响应的Header，注意Header只能发送一次，也就是只能调用一次 start_response()函数。start_response()函数接收两个参数，
		一个是HTTP响应码，一个是一组list表示的HTTP Header，每个Header用一个包含两个str的tuple表示。

		通常情况下，都应该把Content-Type头发送给浏览器。其他很多常用的HTTP Header也应该发送。
		然后，函数的返回值b'<h1>Hello, web!</h1>'将作为HTTP响应的Body发送给浏览器。

	有了WSGI，我们关心的就是如何从environ这个dict对象拿到HTTP请求信息，然后构造HTML，通过 start_response()发送Header，最后返回Body。
	整个 application()函数本身没有涉及到任何解析HTTP的部分，底层代码不需要我们自己编写，我们只负责在更高层次上考虑如何响应请求就可以了。

	application()函数调用--由WSGI服务器来调用--Python内置了一个WSGI服务器--wsgiref模块()
		wsgiref模块--是用纯Python编写的WSGI服务器的参考实现。所谓“参考实现”是指该实现完全符合WSGI标准，但是不考虑任何运行效率，仅供开发和测试使用。

	运行WSGI服务
		先编写hello.py，实现Web应用程序的WSGI处理函数：

			# hello.py
			def application(environ, start_response):
			    start_response('200 OK', [('Content-Type', 'text/html')])
			    return [b'<h1>Hello, web!</h1>']
		然后，再编写一个server.py，负责启动WSGI服务器，加载 application()函数：

			# server.py
			# 从wsgiref模块导入:
			from wsgiref.simple_server import make_server
			# 导入我们自己编写的application函数:
			from hello import application

			# 创建一个服务器，IP地址为空，端口是8000，处理函数是application:
			httpd = make_server('', 8000, application)
			print('Serving HTTP on port 8000...')
			# 开始监听HTTP请求:
			httpd.serve_forever()
		确保以上两个文件在同一个目录下，然后在命令行输入python server.py来启动WSGI服务器：

			wsgiref-start
		注意：如果8000端口已被其他程序占用，启动将失败，请修改成其他端口。
		启动成功后，打开浏览器，输入http://localhost:8000/，就可以看到结果
		按Ctrl+C终止服务器。

	如果你觉得这个Web应用太简单了，可以稍微改造一下，从environ里读取PATH_INFO，这样可以显示更加动态的内容：

		# hello.py

		def application(environ, start_response):
		    start_response('200 OK', [('Content-Type', 'text/html')])
		    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
		    return [body.encode('utf-8')]
		你可以在地址栏输入用户名作为URL的一部分，将返回Hello, xxx!：

		hello-michael

使用Web框架()

	WSGI框架--一个Web App，就是写一个WSGI的处理函数，针对每个HTTP请求进行响应。
	但是如何处理HTTP请求不是问题，问题是如何处理100个不同的URL
		每一个URL可以对应GET和POST请求，当然还有PUT、DELETE等请求，但是我们通常只考虑最常见的GET和POST请求。
		从environ变量里取出HTTP请求的信息，然后逐个判断：
			def application(environ, start_response):
			    method = environ['REQUEST_METHOD']
			    path = environ['PATH_INFO']
			    if method=='GET' and path=='/':
			        return handle_home(environ, start_response)
			    if method=='POST' and path='/signin':
			        return handle_signin(environ, start_response)
			    ...
		只是这么写下去代码是肯定没法维护了
			代码这么写没法维护的原因是因为WSGI提供的接口虽然比HTTP接口高级了不少，但和Web App的处理逻辑比，还是比较低级
	在WSGI接口之上进一步抽象，专注于用一个函数处理一个URL，至于URL到函数的映射，就交给Web框架来做
	flask框架()--一个Web框架--处理 URL 到函数的映射--用Flask编写Web App比WSGI接口简单
		$ pip install flask # 安装flask
		写一个app.py，处理3个URL，分别是：

			GET /：首页，返回Home；

			GET /signin：登录页，显示登录表单；

			POST /signin：处理登录表单，显示登录结果。

			注意噢，同一个URL/signin分别有GET和POST两种请求，映射到两个处理函数中。
		Flask通过Python的装饰器在内部自动地把URL和函数关联起来，所以，我们写出来的代码就像这样：
			from flask import Flask
			from flask import request

			app = Flask(__name__)

			@app.route('/', methods=['GET', 'POST'])
			def home():
			    return '<h1>Home</h1>'

			@app.route('/signin', methods=['GET'])
			def signin_form():
			    return '''<form action="/signin" method="post">
			              <p><input name="username"></p>
			              <p><input name="password" type="password"></p>
			              <p><button type="submit">Sign In</button></p>
			              </form>'''

			@app.route('/signin', methods=['POST'])
			def signin():
			    # 需要从request对象读取表单内容：
			    if request.form['username']=='admin' and request.form['password']=='password':
			        return '<h3>Hello, admin!</h3>'
			    return '<h3>Bad username or password.</h3>'

			if __name__ == '__main__':
			    app.run()
		运行python app.py，Flask自带的Server在端口5000上监听：

			$ python app.py 
			 * Running on http://127.0.0.1:5000/
			打开浏览器，输入首页地址http://localhost:5000/
			首页显示正确！
			再在浏览器地址栏输入http://localhost:5000/signin，会显示登录表单
			输入预设的用户名admin和口令password，登录成功
			输入其他错误的用户名和口令，登录失败

	实际的Web App应该拿到用户名和口令后，去数据库查询再比对，来判断用户是否能登录成功。

	除了Flask，常见的Python Web框架还有：

		Django：全能型Web框架；

		web.py：一个小巧的Web框架；

		Bottle：和Flask类似的Web框架；

		Tornado：Facebook的开源异步Web框架。
	开发Python的Web框架也不是什么难事，后面会讲到开发Web框架的内容。

	小结

		有了Web框架，我们在编写Web应用时，注意力就从WSGI处理函数转移到URL+对应的处理函数，这样，编写Web App就更加简单了。

		在编写URL处理函数时，除了配置URL外，从HTTP请求拿到用户数据也是非常重要的。Web框架都提供了自己的API来实现这些功能。Flask通过request.form['name']来获取表单的内容。

