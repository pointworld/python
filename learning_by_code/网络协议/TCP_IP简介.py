网络编程

'互联网协议簇'--TCP/IP协议('TCP协议'-IP协议('IP地址','网卡',IPv4,IPv6,'IP包'))--'端口'--实现网络互连

	互联网协议簇(Internet Protocol Suite)通用协议标准, 任何私有网络，只要支持这个协议，就可联入互联网	

	'TCP/IP协议'--互联网协议包含上百种协议标准，最重要的两个协议是TCP和IP协议	

	'IP地址'--互联网上每个计算机的唯一标识，实现通信，双方须知道对方标识，类似 123.123.123.123。
	'网卡'--IP地址对应计算机的网络接口，如果一台计算机同时接入多个网络，比如路由器，它就会有多个IP地址
	'IPv4地址'--一个32位整数，以字符串表示的IP地址如 192.168.0.1实际上是把32位整数按8位分组后的数字表示，目的是便于阅读。
	'IPv6地址'--一个128位整数，是IPv4的升级版，以字符串表示类似于2001:0db8:85a3:0042:1000:8a2e:0370:7334。	

	IP协议(Internet Protocol, 网际协议)-负责'把数据从一台计算机通过网络发送到另一台计算机'。数据被分割成多个小块，然后通过IP包发送出去。由于互联网链路复杂，两台计算机之间经常有
	多条线路，因此，路由器就负责决定如何把一个IP包转发出去。
	'IP包'--'除了包含要传输的数据外，还包含源IP地址和目标IP地址，源端口和目标端口'。IP包的特点是按块发送，途径多个路由，但不保证能到达，也不保证顺序到达。	

	TCP协议(Transfer Control Protocol, 传输控制协议)-'建立在IP协议之上'。负责在两台计算机之间'建立可靠连接，保证数据包按顺序到达'。TCP协议通过握手建立连接，然后，对每个IP包编号，
	确保对方按顺序收到，如果包丢掉了，就自动重发。许多常用的更高级的协议都是建立在TCP协议基础上的，如用于浏览器的HTTP协议、发送邮件的SMTP协议等。	

	'端口'-port--在两台计算机通信时，只发IP地址是不够的，因为同一台计算机上跑着多个网络程序。一个IP包来了之后，到底是交给浏览器还是QQ，
	就需要端口号来区分。'每个网络程序都向操作系统申请唯一的端口号'，这样，两个进程在两台计算机之间建立网络连接就需要各自的IP地址和各自的端口号。
	一个进程也可能同时与多个计算机建立链接，因此它会申请很多端口。
'TCP编程'--Socket(套接字)--'客户端-服务器'--'客户端编程-服务器编程'--建立可靠连接，通信双方以流的形式发送数据

	Socket(套接字)--使应用程序能够'读写与收发 通讯协定(protocol) 与资料'的程序。'打开一个网络链接'--需要知道目标计算机的IP地址和端口号，再指定协议类型即可
	
	'客户端--服务器'--创建TCP连接时，主动发起连接的叫 客户端()，被动响应连接的叫 服务器()
	
	'客户端编程'--获取服务器数据
		创建一个基于TCP连接的Socket，可以这样做：
			
			import socket	# 导入socket库:		
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)# 创建一个socket, AF_INET指定使用IPv4协议, SOCK_STREAM指定使用面向流的TCP协议
			s.connect(('www.sina.com.cn', 80)) # 建立连接:
			创建Socket时，AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议，这样，
			一个Socket对象就创建成功，但是还没有建立连接。			
		建立连接--客户端要主动发起TCP连接，必须知道服务器的IP地址和端口号
			新浪网站的IP地址可以用域名www.sina.com.cn自动转换到IP地址
			但是怎么知道新浪服务器的端口号呢？	

			答案是作为服务器，提供什么样的服务，端口号就必须固定下来。由于我们想要访问网页，因此新浪提供网页服务的服务器必须把端口号固定在80端口，
			因为80端口是Web服务的标准端口。其他服务都有对应的标准端口号，例如SMTP服务是 25端口，FTP服务是 21端口，等等。

			'端口号小于 1024的是Internet标准服务的端口，端口号大于 1024的，可以任意使用。'

			因此，我们连接新浪服务器的代码如下：			

			s.connect(('www.sina.com.cn', 80))  # 注意参数是一个tuple，包含地址和端口号			
		建立TCP连接后，向服务器发送请求，要求返回首页的内容：
			# 发送数据:
			s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
			TCP连接创建的是双向通道，双方都可以同时给对方发数据。但是谁先发谁后发，怎么协调，要'根据具体的协议来决定'。例如，HTTP协议规定客户端
			必须先发请求给服务器，服务器收到后才发数据给客户端。
		发送的文本格式必须符合HTTP标准，如果格式没问题，接下来就可以接收新浪服务器返回的数据了
			# 接收数据:
			buffer = []
			while True:
			    d = s.recv(1024) # 每次最多接收1k字节:
			    if d:
			        buffer.append(d)
			    else:
			        break
			data = b''.join(buffer) # join函数俩连接字符串， 将buffer中的二进制数据元素以无空格形式重新拼接
			接收数据时，调用recv(max)方法，一次最多接收指定的字节数，因此，在一个while循环中反复接收，直到recv()返回空数据，表示接收完毕，退出循环。			
		当我们接收完数据后，调用close()方法关闭Socket，这样，一次完整的网络通信就结束了：
			# 关闭连接:
			s.close()
		接收到的数据包括HTTP头和网页本身，我们只需要把HTTP头和网页分离一下，把HTTP头打印出来，网页内容保存到文件：
			header, html = data.split(b'\r\n\r\n', 1) # split函数拆分字符串，将data中的数据以两个空行和 1 进行数据拆分
			print(header.decode('utf-8'))
			# 把接收的数据写入文件:
			with open('path/sina.html', 'wb') as f:
			    f.write(html)
			现在，只需要在浏览器中打开这个sina.html文件，就可以看到新浪的首页了。			
	'服务器编程'--给客户端发送数据
		服务器进程首先要绑定一个端口并监听来自其他客户端的连接。如果某个客户端连接过来了，服务器就与该客户端建立Socket连接，实现通信
			所以，服务器会打开固定端口（比如 80）监听，每来一个客户端连接，就创建该Socket连接。由于服务器会有大量来自客户端的连接，所以，服务器
			要能够区分一个Socket连接是和哪个客户端绑定的。'一个Socket依赖4项：服务器地址、服务器端口、客户端地址、客户端端口来唯一确定一个Socket。'
		服务器需要同时响应多个客户端的请求，所以，每个连接都需要一个新的进程或者新的线程来处理，否则，服务器一次就只能服务一个客户。
		我们来编写一个简单的服务器程序，它接收客户端连接，把客户端发过来的字符串加上Hello再发回去
		首先，创建一个基于IPv4和TCP协议的Socket

			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		然后，绑定监听的地址和端口
			服务器可能有多块网卡，可以绑定到某一块网卡的IP地址上，也可以用 0.0.0.0绑定到所有的网络地址，还可以用 127.0.0.1绑定到本机地址。
			127.0.0.1是一个特殊的IP地址，表示本机地址，如果绑定到这个地址，客户端必须同时在本机运行才能连接，也就是说，外部的计算机无法连接进来。			

			端口号需要预先指定。因为我们写的这个服务不是标准服务，所以用 9999这个端口号。请注意，小于 1024的端口号必须要有管理员权限才能绑定
			# 监听端口:
			s.bind(('127.0.0.1', 9999))
		调用 listen()方法开始监听端口，传入的参数指定等待连接的最大数量：
			s.listen(5)
			print('Waiting for connection...')
		接下来，服务器程序通过一个永久循环来接受来自客户端的连接，accept()会等待并返回一个客户端的连接
			while True:
			    # 接受一个新连接:
			    sock, addr = s.accept() # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)， addr接收的是(客户端IP, 端口)
			    # <socket.socket fd=384, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 9999), 
			    # raddr=('127.0.0.1', 57278)>
			    # ('127.0.0.1', 57278)

			    # 创建新线程来处理TCP连接:
			    t = threading.Thread(target=tcplink, args=(sock, addr))
			    t.start()
		每个连接都必须创建新线程（或进程）来处理，否则，单线程在处理连接的过程中，无法接受其他客户端的连接
			def tcplink(sock, addr):
			    print('Accept new connection from %s:%s...' % addr) # addr 是一个元组 (客户端IP, 端口)
			    sock.send(b'Welcome!')
			    while True:
			        data = sock.recv(1024)
			        time.sleep(1)
			        if not data or data.decode('utf-8') == 'exit':
			            break
			        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
			    sock.close()
			    print('Connection from %s:%s closed.' % addr)
		连接建立后，服务器首先发一条欢迎消息，然后等待客户端数据，并加上Hello再发送给客户端。如果客户端发送了exit字符串，就直接关闭连接。
		要测试这个服务器程序，我们还需要编写一个客户端程序：

			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			# 建立连接:
			s.connect(('127.0.0.1', 9999))
			# 接收欢迎消息:
			print(s.recv(1024).decode('utf-8'))
			for data in [b'Michael', b'Tracy', b'Sarah']:
			    # 发送数据:
			    s.send(data)
			    print(s.recv(1024).decode('utf-8'))
			s.send(b'exit')
			s.close()
		我们需要打开两个命令行窗口，一个运行服务器程序，另一个运行客户端程序，就可以看到效果了：
		需要注意的是，客户端程序运行完毕就退出了，而服务器程序会永远运行下去，必须按Ctrl+C退出程序。			
	小结

		用TCP协议进行Socket编程在Python中十分简单，对于客户端，要主动连接服务器的IP和指定端口，对于服务器，要首先监听指定端口，然后，对
		每一个新的连接，创建一个线程或进程来处理。通常，服务器程序会无限运行下去。			

		同一个端口，被一个Socket绑定了以后，就不能被别的Socket绑定了。			
	参考源码
		do_tcp.py 
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			# 建立连接:
			s.connect(('www.sina.com.cn', 80))
			# 发送数据:
			s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')
			# 接收数据:
			buffer = []
			while True:
			    # 每次最多接收1k字节:
			    d = s.recv(1024)
			    if d:
			        buffer.append(d)
			    else:
			        break
			data = b''.join(buffer)
			# 关闭连接:
			s.close()
			header, html = data.split(b'\r\n\r\n', 1)
			print(header.decode('utf-8'))
			# 把接收的数据写入文件:
			with open('E:\\Unzip files\\Python\\point\\sina.html', 'wb') as f:
			    f.write(html)
		echo_server.py
			import socket, threading, time
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.bind(('127.0.0.1', 9999))
			s.listen(5)
			print('Waiting for connection...')
			def tcplink(sock, addr):
			    print('Accept new connection from %s:%s...' % addr)
			    sock.send(b'Welcome!')
			    while True:
			        data = sock.recv(1024)
			        time.sleep(1)
			        if not data or data.decode('utf-8') == 'exit':
			            break
			        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
			    sock.close()
			    print('Connection from %s:%s closed.' % addr)
			while True:
			    sock, addr = s.accept()
			    t = threading.Thread(target = tcplink, args = (sock, addr))
			    t.start() 
		echo_client.py
			import socket
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect(('127.0.0.1', 9999))
			print(s.recv(1024).decode('utf-8'))
			for data in [b'Michael', b'Tracy', b'Sarah']:
			    s.send(data)
			    print(s.recv(1024).decode('utf-8'))
			s.send(b'exit')
			s.close() 
'UDP编程'--不需要建立连接, 数据不要求可靠到达

	使用UDP协议时，不需要建立连接，只需要知道对方的IP地址和端口号，就可以直接发数据包。但是，能不能到达就不知道了。
			虽然用UDP传输数据不可靠，但它的优点是和TCP比，速度快，对于不要求可靠到达的数据，就可以使用UDP协议。			

			我们来看看如何通过UDP协议传输数据。和TCP类似，使用UDP的通信双方也分为客户端和服务器。服务器首先需要绑定端口：			

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			# 绑定端口:
			s.bind(('127.0.0.1', 9999))
			创建Socket时，SOCK_DGRAM指定了这个Socket的类型是UDP。绑定端口和TCP一样，但是不需要调用listen()方法，而是
			直接接收来自任何客户端的数据：
			print('Bind UDP on 9999...')
			while True:
			    # 接收数据:
			    data, addr = s.recvfrom(1024)
			    print('Received from %s:%s.' % addr)		    
			    s.sendto(b'Hello, %s!' % data, addr)
			    	第一个，你打印addr看看打出来是什么
				（应该是个元组，包含IP和PORT两个内容）
				addr=('127.0.0.1',8000)
				print('%s-%s'%addr)就是 分别把addr[0],addr[1]传给%s %s				

				第二个，只是把两个参数传给函数发给客户端而已。
				函数原型sendto(string[,flags],address)，课程中的string就是'Hello, %s!' %data	
			recvfrom()方法返回数据和客户端的地址与端口，这样，服务器收到数据后，直接调用sendto()就可以把数据用UDP发给客户端。			

			注意这里省掉了多线程，因为这个例子很简单。			

			客户端使用UDP时，首先仍然创建基于UDP的Socket，然后，不需要调用connect()，直接通过sendto()给服务器发数据：			

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			for data in [b'Michael', b'Tracy', b'Sarah']:
			    # 发送数据:
			    s.sendto(data, ('127.0.0.1', 9999))
			    # 接收数据:
			    print(s.recv(1024).decode('utf-8'))
			s.close()
			从服务器接收数据仍然调用recv()方法。			

			仍然用两个命令行分别启动服务器和客户端测试，结果如下：			

			client-server			

	小结			

			UDP的使用与TCP类似，但是不需要建立连接。此外，服务器绑定UDP端口和TCP端口互不冲突，也就是说，UDP的 9999端口
			与TCP的 9999端口可以各自绑定。			

	参考源码			

		udp_server.py
			#!/usr/bin/env python3
			# -*- coding: utf-8 -*-			

			import socket			

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)			

			# 绑定端口:
			s.bind(('127.0.0.1', 9999))			

			print('Bind UDP on 9999...')			

			while True:
			    # 接收数据:
			    data, addr = s.recvfrom(1024)
			    print('Received from %s:%s.' % addr)
			    reply = 'Hello, %s!' % data.decode('utf-8')
			    s.sendto(reply.encode('utf-8'), addr)
		udp_client.py
			#!/usr/bin/env python3
			# -*- coding: utf-8 -*-			

			import socket			

			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)			

			for data in [b'Michael', b'Tracy', b'Sarah']:
			    # 发送数据:
			    s.sendto(data, ('127.0.0.1', 9999))
			    # 接收数据:
			    print(s.recv(1024).decode('utf-8'))			

			s.close() 