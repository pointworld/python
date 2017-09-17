IO(Input/Output)-- Stream(流)--同步IO(CPU等着)--异步IO(CPU不等待)--IO操作(打开文件--读写文件数据--关闭文件)

IO(Input/Output)--涉及到数据交换--磁盘、网络等，就需要IO接口
Stream(流)-数据流--单向流动

同步IO(CPU等着)--CPU等待IO执行的结果，再执行其他任务
	CPU和内存的运行速度快于外设，所以，在IO编程中，存在速度不匹配问题。举个例子来说，比如要把100M的数据
	写入磁盘，CPU输出100M的数据只需要0.01秒，可是磁盘要接收这100M数据可能需要10秒，怎么办呢？有两种办法：

	第一种是CPU等着，也就是程序暂停执行后续代码，等100M的数据在10秒后写入磁盘，再接着往下执行，这种模式称为同步IO；
异步IO(CPU不等待)--CPU不等待IO执行的结果，执行其他任务
	另一种方法是CPU不等待，只是告诉磁盘，“您老慢慢写，不着急，我接着干别的事去了”，于是，后续代码可以立刻接着执行，这种模式
	称为异步IO。

	同步和异步的区别就在于是否等待IO执行的结果。好比你去麦当劳点餐，你说“来个汉堡”，服务员告诉你，对不起，汉堡要现做，需要
	等5分钟，于是你站在收银台前面等了5分钟，拿到汉堡再去逛商场，这是同步IO。
	你说“来个汉堡”，服务员告诉你，汉堡需要等5分钟，你可以先去逛商场，等做好了，我们再通知你，这样你可以立刻去干别的事情
	（逛商场），这是异步IO。

IO操作(打开文件--读写文件数据--关闭文件)--'操作系统封装'了在磁盘上读写文件的功能，不允许普通的程序直接操作磁盘
	读写磁盘文件--就是请求操作系统打开一个 文件对象(通常称为'文件描述符')，然后，通过操作系统提供的接口对该文件对象中数据进行读写
		打开一个文件对象--open()函数--open('文件路径', '标识符', encode/decode'编码/解码方式', errors='处理编码错误方式')
			'文件路径'--目标数据所在位置
			'标识符'--文件读写方式
				'r'--以'只读'方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
				'rb' 以'二进制格式'打开一个文件用于'只读'。文件指针将会放在文件的开头。这是默认模式。
				'r+' 打开一个文件用于'读写'。文件指针将会放在文件的开头。
				'rb+' 以'二进制格式'打开一个文件用于'读写'。文件指针将会放在文件的开头。
				'w' 打开一个文件'只用于写入'。如果'该文件已存在则将其覆盖。如果该文件不存在，创建新文件'。
				'wb' 以'二进制格式打开一个文件只用于写入'。'如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件'。
				'w+' 打开一个文件用于'读写'。'如果该文件已存在则将其覆盖。如果该文件不存在，创建新文件'。
				'wb+' 以二进制格式打开一个文件用于读写。文件已存在则覆盖，不存在，则创建新文件。
				'a' 打开文件用于追加。文件已存在，文件指针将会放在文件的结尾，新内容将会被写入到已有内容之后。文件不存在，创建新文件进行写入。
				'ab' 二进制格式打开文件用于追加。文件已存在，文件指针放在结尾，新的内容被写入到已有内容之后。文件不存在，创建新文件进行写入。
				'a+' 打开文件用于读写。文件已存在，文件指针将会放在结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
				'ab+' 二进制格式打开文件用于追加。文件已存在，文件指针将会放在文件的结尾。不存在，创建新文件用于读写。
				
				如
					>>> f = open('/Users/michael/test.txt', 'r')
					标示符'r'表示读，这样，我们就成功地打开了一个文件。
					如果文件不存在，open()函数就会抛出一个IOError的错误，并且给出错误码和详细的信息告诉你文件不存在：
					>>> f=open('/Users/michael/notfound.txt', 'r')
					Traceback (most recent call last):
					  File "<stdin>", line 1, in <module>
					FileNotFoundError: [Errno 2] No such file or directory: '/Users/michael/notfound.txt'
			'编码/解码方式'--指定字符编码
			errors='处理编码错误方式'--遇到编码错误后如何处理--最简单的方式是直接忽略：errors='ignore'
		读写文件数据
			read()方法--一次性读取文件的全部内容, Python把内容读到内存，用一个str对象表示
			read(size)方法--每次最多读取size个字节的内容
			readline()方法--每次读取一行内容
			readlines()方法--一次读取所有内容并按行返回list
			write()方法--写入文件
		关闭文件
			close()方法--文件使用完后必须关闭，文件对象会占用OS资源，且OS同一时间能打开的文件数量是有限的，还可防止写入数据丢失	
				当我们写文件时，操作系统往往不会立刻把数据写入磁盘，而是放到内存缓存起来，空闲的时候再慢慢写入。只有调用close()方法时，
				操作系统才保证把没有写入的数据全部写入磁盘。忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。
			with语句-- with open('文件路径', '标示符', ’编码/解码方式’) as 变量名: -- 自动关闭文件
				with open('/Users/michael/test.txt', 'w') as f:
					f.write('Hello, world!')
				和 try ... finally 是一样的，但是代码更佳简洁，并且不必调用f.close()方法。	
			try ... finally语句--正确关闭文件
				由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。所以，为了保证无论是否出错都能正确地关闭文件，
				我们可以使用try ... finally来实现：
				try:
				    f = open('/path/to/file', 'r')
				    print(f.read())
				finally:
				    if f:
				        f.close()
		file-like Object
			像open()函数返回的这种有个 read()方法的对象，在Python中统称为file-like Object。除了file外，还可以是内存的
			字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
			StringIO就是在内存中创建的file-like Object，常用作临时缓冲。
		小结
			
			在Python中，文件读写是通过 open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯。				
	读写内存数据--StringIO和BytesIO -- file-like Object
		StringIO模块--实现在内存中读写str
			把str写入StringIO，先创建一个StringIO，然后，像文件一样写入即可：
				>>> from io import StringIO
				>>> f = StringIO()
				>>> f.write('hello')
				5
				>>> f.write(' ')
				1
				>>> f.write('world!')
				6
				>>> print(f.getvalue())
				hello world!
				getvalue()方法用于获得写入后的str。
			读取StringIO中的str，像读文件一样读取即可：
				>>> from io import StringIO
				>>> f = StringIO('Hello!\nHi!\nGoodbye!')
				>>> while True:
				...     s = f.readline()
				...     if s == '':
				...         break
				...     print(s.strip())
				...
				Hello!
				Hi!
				Goodbye!
		BytesIO模块--实现在内存中读写 二进制数据(Bytes)
			内存中读写bytes，先创建一个BytesIO，然后写入一些bytes：
				>>> from io import BytesIO
				>>> f = BytesIO()
				>>> f.write('中文'.encode('utf-8'))
				6
				>>> print(f.getvalue())
				b'\xe4\xb8\xad\xe6\x96\x87'
				请注意，写入的不是str，而是经过UTF-8编码的bytes。
			和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
				>>> from io import BytesIO
				>>> f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
				>>> f.read()
				b'\xe4\xb8\xad\xe6\x96\x87'
		小结--StringIO和BytesIO是在内存中操作str和bytes的方法，使得和读写文件具有一致的接口。
		参考源码
				do_stringio.py
				do_bytesio.py
	操作文件和目录
		在命令行输入操作系统提供的各种命令来完成--调用了操作系统提供的接口函数
			比如dir、cp等命令。
				Dir：abbr. 目录（directory）
		Python内置的os模块也可以直接调用操作系统提供的接口函数--os模块的某些函数是跟操作系统有关
			如何使用os模块的基本功能
				>>> import os
				>>> os.name # 操作系统类型
				'posix'
				如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
				要获取详细的系统信息，可以调用uname()函数：
				>>> os.uname()
				posix.uname_result(sysname='Darwin', nodename='MichaelMacPro.local', release='14.3.0', version=
				'Darwin Kernel Version 14.3.0: Mon Mar 23 11:59:05 PDT 2015; root:xnu-2782.20.48~5/RELEASE_X86_64', machine='x86_64')
				注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。
			环境变量--在操作系统中定义的环境变量，全部保存在os.environ这个变量中			
				>>> os.environ
				environ({'VERSIONER_PYTHON_PREFER_32_BIT': 'no', 'TERM_PROGRAM_VERSION': '326', 'LOGNAME': 'michael', 'USER': 
				'michael', 'PATH': '/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/mysql/bin', ...})
				要获取某个环境变量的值，可以调用os.environ.get('key')：
				>>> os.environ.get('PATH')
				'/usr/bin:/bin:/usr/sbin:/sbin:/usr/local/bin:/opt/X11/bin:/usr/local/mysql/bin'
				>>> os.environ.get('x', 'default')
				'default'
			操作文件和目录--操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中
				查看、创建和删除目录可以这么调用：
				# 查看当前目录的绝对路径:
				>>> os.path.abspath('.')
				'/Users/michael'
				# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
				>>> os.path.join('/Users/michael', 'testdir')
				'/Users/michael/testdir'
				# 然后创建一个目录:
				>>> os.mkdir('/Users/michael/testdir')
				# 删掉一个目录:
				>>> os.rmdir('/Users/michael/testdir')
				把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符。
				在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
				part-1/part-2
				而Windows下会返回这样的字符串：
				part-1\part-2
				同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，
				后一部分总是最后级别的目录或文件名：
				>>> os.path.split('/Users/michael/testdir/file.txt')
				('/Users/michael/testdir', 'file.txt')
				os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
				>>> os.path.splitext('/path/to/file.txt')
				('/path/to/file', '.txt')
				这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。
				文件操作使用下面的函数。假定当前目录下有一个test.txt文件：
				# 对文件重命名:
				>>> os.rename('test.txt', 'test.py')
				# 删掉文件:
				>>> os.remove('test.py')
				但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的
				读写文件可以完成文件复制，只不过要多写很多代码。
			shutil模块--提供了copyfile()的函数等，它们可以看做是os模块的补充。
				最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：
				>>> [x for x in os.listdir('.') if os.path.isdir(x)]
				['.lein', '.local', '.m2', '.npm', '.ssh', '.Trash', '.vim', 'Applications', 'Desktop', ...]
				要列出所有的.py文件，也只需一行代码：
				>>> [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
				['apis.py', 'config.py', 'models.py', 'pymonitor.py', 'test_db.py', 'urls.py', 'wsgiapp.py']
				是不是非常简洁？
		小结
				Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。
		练习
				1.	利用os模块编写一个能实现dir -l输出的程序。
				2.	编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
		参考源码
				do_dir
	序列化-pickling--把变量从内存中变成可存储或可传输的过程--序列化后的内容可以写入磁盘，或者通过网络传输到别的机器上
		定义
			在程序运行的过程中，所有的变量都是在内存中，
			比如，定义一个dict：
				d = dict(name='Bob', age=20, score=88)
			可以随时修改变量，比如把name改成'Bill'，但是一旦程序结束，变量所占用的内存就被操作系统全部回收。如果
			没有把修改后的'Bill'存储到磁盘上，下次重新运行程序，变量又被初始化为'Bob'。
		'pickle模块'--实现序列化，反序列化--bytes--只能用于Python
			序列化
			pickle.dumps(对象)--把任意对象序列化为一个bytes, 然后把这个bytes写入文件
			pickle.dump(对象,  open('dump.txt', 'wb'))-- 直接把对象序列化后写入一个file-like Object-
				
				首先，我们尝试把一个对象序列化并写入文件：
				>>> import pickle
				>>> d = dict(name='Bob', age=20, score=88)
				>>> pickle.dumps(d)
				b'\x80\x03}q\x00(X\x03\x00\x00\x00ageq\x01K\x14X\x05\x00\x00\x00scoreq\x02KXX\x04\x00\x00\x00nameq\x03X\x03\x00\x00\x00Bobq\x04u.'
				pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法
				pickle.dump()直接把对象序列化后写入一个file-like Object：
				>>> f = open('dump.txt', 'wb')
				>>> pickle.dump(d, f)
				>>> f.close()
				看看写入的dump.txt文件，一堆乱七八糟的内容，这些都是Python保存的对象内部信息。
			反序列化
			pickle.loads(bytes)--把对象从磁盘读到内存时，先把内容读到一个bytes，然后用pickle.loads(bytes)方法反序列化出对象
			pickle.load(open('dump.txt', 'rb'))-- 直接用pickle.load()方法从一个file-like Object中直接反序列化出对象
				我们打开另一个Python命令行来反序列化刚才保存的对象：
				>>> f = open('dump.txt', 'rb')
				>>> d = pickle.load(f)
				>>> f.close()
				>>> d
				{'age': 20, 'score': 88, 'name': 'Bob'}
				变量的内容又回来了！
				当然，这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。
				Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python
				彼此都不兼容，因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。
		'JSON模块'--实现序列化，反序列化--str--更通用
			序列化为JSON标准格式
				json.dumps(对象)--把对象序列化为JSON标准格式--返回一个str，内容就是标准的JSON，然后写入文件
				json.dump(对象)方法可以直接把JSON写入一个file-like Object				

				如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式，比如XML，但更好的方法是序列化为
				JSON，因为JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
				JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
				JSON表示的对象就是标准的JavaScript语言的对象，JSON和Python内置的数据类型对应如下：
				JSON类型	Python类型
				{}	dict
				[]	list
				"string"	str
				1234.56	int或float
				true/false	True/False
				null	None
				Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：
				>>> import json
				>>> d = dict(name='Bob', age=20, score=88)
				>>> json.dumps(d)
				'{"age": 20, "score": 88, "name": "Bob"}'
				dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
			把JSON反序列化为Python对象
				要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从
				file-like Object中读取字符串并反序列化：
				>>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
				>>> json.loads(json_str)
				{'age': 20, 'score': 88, 'name': 'Bob'}
				由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换。
			JSON进阶--定义类，然后序列化
				Python的dict对象可以直接序列化为JSON的{}，不过，很多时候，我们更喜欢用class表示对象
				比如定义Student类，然后序列化：
				import json				

				class Student(object):
				    def __init__(self, name, age, score):
				        self.name = name
				        self.age = age
				        self.score = score				

				s = Student('Bob', 20, 88)
				print(json.dumps(s))
				运行代码，毫不留情地得到一个TypeError：
				Traceback (most recent call last):
				  ...
				TypeError: <__main__.Student object at 0x10603cc50> is not JSON serializable
				错误的原因是Student对象不是一个可序列化为JSON的对象。
				如果连class的实例对象都无法序列化为JSON，这肯定不合理！
				别急，我们仔细看看dumps()方法的参数列表，可以发现，除了第一个必须的obj参数外，dumps()方法还提供了
				一大堆的可选参数：
				https://docs.python.org/3/library/json.html#json.dumps
				这些可选参数就是让我们来定制JSON序列化。前面的代码之所以无法把Student类实例序列化为JSON，是因为默认
				情况下，dumps()方法不知道如何将Student实例变为一个JSON的{}对象。
				可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，
				再把函数传进去即可：
				def student2dict(std):
				    return {
				        'name': std.name,
				        'age': std.age,
				        'score': std.score
				    }
				这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON：
				>>> print(json.dumps(s, default=student2dict))
				{"age": 20, "name": "Bob", "score": 88}
				不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
				print(json.dumps(s, default=lambda obj: obj.__dict__))
				因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义
				了__slots__的class。
				同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们
				传入的object_hook函数负责把dict转换为Student实例：
				def dict2student(d):
				    return Student(d['name'], d['age'], d['score'])
				运行结果如下：
				>>> json_str = '{"age": 20, "score": 88, "name": "Bob"}'
				>>> print(json.loads(json_str, object_hook=dict2student))
				<__main__.Student object at 0x10cd3c190>
				打印出的是反序列化的Student实例对象。
			小结
				Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。
				json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。但是，
				当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，既做
				到了接口简单易用，又做到了充分的扩展性和灵活性。
			参考源码
				use_pickle.py
				use_json.py
	