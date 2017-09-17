代码易维护--代码复用--功能封装
模块(Module)
    在Python中，'一个.py文件'就称之为一个 模块(Module)。
    在计算机程序的开发过程中，随着程序代码越写越多，在一个文件里代码就会越来越长，越来越不容易维护。
    为了'编写可维护的代码'，我们把很多'函数分组'，分别放到不同的文件里，这样，每个文件包含的代码就相对较少，
    很多编程语言都采用这种组织代码的方式。
使用模块好处()
    代码易维护()

        最大的好处是大大'提高了代码的可维护性'。
    代码复用()

        其次，'编写代码不必从零开始'。当一个模块编写完毕，就可以被其他地方引用。
    避免函数名和变量名冲突()
        相同名字的函数和变量完全可以分别存在不同的模块中
        因此，我们自己在编写模块时，不必考虑名字会与其他模块冲突。
        但是也要注意，'尽量不要与内置函数名字冲突。'
    存在大量内置模块与第三方模块()
        我们在编写程序的时候，也经常引用其他模块，
        包括Python内置的模块和来自第三方的模块
包(package) 
    定义   
        按'目录来组织模块'的方法，称为 包(Package)，每一个包目录下必须有一个__init__.py的文件。 
        类似的，可以有'多级目录'，'组成多级层次的包结构'。  
    例
        一个abc.py的文件就是一个名字叫 'abc 的模块'，一个xyz.py的文件就是一个名字叫 'xyz 的模块'。现在，假设我们的 abc 和 xyz 
        这两个模块名字与其他模块冲突了，于是我们可以'通过包来组织模块，避免冲突。方法是选择一个顶层包名',比如mycompany
        引入了包以后，只要顶层的包名不与别人冲突，那所有模块都不会与别人冲突。        

        现在，abc.py模块的名字就变成了mycompany.abc，类似的，xyz.py的模块名变成了mycompany.xyz。
        请注意，每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的，否则，Python就把这个目录当成普通目录，
        而不是一个包。__init__.py可以是空文件，也可以有Python代码，因为__init__.py本身就是一个模块，而它的模块名就是mycompany。
        向代码中导入某个包，该包下面的__init__模块就会自动运行
__init__.py 的使用 
        每一个包目录下必须有一个 __init__.py的文件，有了这个文件，我们才能导入这个目录下的module，否则，Python就把这个目录当成普通目录
        避免多个模块中的模块名冲突，只要顶层的包名不与别人冲突，所有模块都不会与别人冲突
        
        __init__.py 可以是空文件，也可以有Python代码
        该包只要一经导入,  该包下面的 __init__.py 模块即自动运行
                故，我们可以在 __init__.py文件中再导入其他的包，或者模块。
                这样，当我们导入这个包的时候，__init__.py文件自动运行。就帮我们导入了其他的包和模块，我们就不需要将所有的import语句写在一个文件里了，可以减少写代码时的代码量。
               
                __init__.py 中还有一个重要的变量，叫做 __all__。我们有时会使出一招“全部导入”，也就是这样：from PackageName import *
                这时 import 就会把注册在包 __init__.py 文件中 __all__ 列表中的子模块和子包导入到当前作用域中来，注意，如果在__all__中没有加入某个需要调用的子包或子模块，则调用无效
                比如：
                            #文件 __init__.py
                            __all__ = ["Module1", "Module2", "subPackage1", "subPackage2"]
                            or
                            __all__=(Module1+Module2+subPack1+subPack2)

        原理
                python中的Module是比较重要的概念。常见的情况是，事先写好一个.py文 件，在另一个文件中需要import时，将事先写好的.py文件拷贝 到当前目录，或者是在
                sys.path中增加事先写好的.py文件所在的目录，然后import。这样的做法，对于少数文件是可行的，但如果程序数目很 多，层级很复杂，就很吃力了。
                有没有办法，像Java的Package一样，将多个.py文件组织起来，以便在外部统一调用，和在内部互相调用呢？答案是有的。
                主要是用到python的包的概念，python __init__.py在包里起一个比较重要的作用
                要弄明白这个问题，首先要知道，python在执行import语句时，到底进行了什么操作，按照python的文档，它执行了如下操作：
                第1步，创建一个新的，空的module对象（它可能包含多个module）；
                第2步，把这个module对象插入sys.module中
                第3步，装载module的代码（如果需要，首先必须编译）
                第4步，执行新的module中对应的代码。

                在执行第3步时，首先要找到module程序所在的位置，其原理为：
                如 果需要导入的module的名字是m1，则解释器必须找到m1.py，它首先在当前目录查找，然后是在环境变量PYTHONPATH中查找。 PYTHONPATH可以视为
                系统的PATH变量一类的东西，其中包含若干个目录。如果PYTHONPATH没有设定，或者找不到m1.py，则继续搜索 与python的安装设置相关的默认路径，在Unix下，
                通常是/usr/local/lib/python。
                事实上，搜索的顺序是：当前路径 （以及从当前目录指定的sys.path），然后是PYTHONPATH，然后是python的安装设置相关的默认路径。正因为存在这样的顺序，
                如果当前 路径或PYTHONPATH中存在与标准module同样的module，则会覆盖标准module。也就是说，如果当前目录下存在xml.py，那么执 行import xml时，导入
                的是当前目录下的module，而不是系统标准的xml。

                了解了这些，我们就可以先构建一个package，以普通module的方式导入，就可以直接访问此package中的各个module了。

                Python中的package定义很简单，其层次结构与程序所在目录的层次结构相同，这一点与Java类似，唯一不同的地方在于，python中的package必须包含一个__init__.py的文件。
                例如，我们可以这样组织一个package:

                package1/
                    __init__.py
                    subPack1/
                        __init__.py
                        module_11.py
                        module_12.py
                        module_13.py
                    subPack2/
                        __init__.py
                        module_21.py
                        module_22.py
                    ……

                __init__.py可以为空，只要它存在，就表明此目录应被作为一个package处理。当然，__init__.py中也可以设置相应的内容，下文详细介绍。

                好了，现在我们在module_11.py中定义一个函数：

                def funA():
                    print "funcA in module_11"
                    return

                在顶层目录（也就是package1所在的目录，当然也参考上面的介绍，将package1放在解释器能够搜索到的地方）运行python:

                >>>from package1.subPack1.module_11 import funcA
                >>>funcA()
                funcA in module_11

                这样，我们就按照package的层次关系，正确调用了module_11中的函数。

                细心的用户会发现，有时在import语句中会出现通配符*，导入某个module中的所有元素，这是怎么实现的呢？
                答案就在__init__.py中。我们在subPack1的__init__.py文件中写

                __all__ = ['module_13', 'module_12']

                然后进入python

                >>>from package1.subPack1 import *
                >>>module_11.funcA()
                Traceback (most recent call last):
                  File "<stdin>", line 1, in <module>
                ImportError: No module named module_11

                也就是说，以*导入时，package内的module是受__init__.py限制的。
                好了，最后来看看，如何在package内部互相调用。
                如果希望调用同一个package中的module，则直接import即可。也就是说，在module_12.py中，可以直接使用
                import module_11
                如果不在同一个package中，例如我们希望在module_21.py中调用module_11.py中的FuncA，则应该这样：
                from module_11包名.module_11 import funcA        
模块使用方法()
    标准使用
        #!/usr/bin/env python3
        # -*- coding: utf-8 -*-        

        ' a test module '        

        __author__ = 'Michael Liao'        

        import sys        

        def test():
            args = sys.argv
            if len(args)==1:
                print('Hello, world!')
            elif len(args)==2:
                print('Hello, %s!' % args[1])
            else:
                print('Too many arguments!')        

        if __name__=='__main__':
            test()
    解释
        标准文件模板
            标准注释  
                第1行和第2行是标准注释，第1行注释可以让这个hello.py文件直接在Unix/Linux/Mac上运行，第2行注释表示.py文件本身
                使用标准 UTF-8 编码；
            文档注释
                第4行是一个字符串，表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释；
            作者
                第6行使用__author__变量把作者写进去，这样当你公开源代码后别人就可以瞻仰你的大名；
        
        以上就是Python模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。
        
        后面开始就是真正的代码部分
            使用模块的第一步，就是导入该模块：
                import sys

                '导入 sys 模块后，我们就有了变量 sys 指向该模块，利用sys这个变量，就可以访问 sys 模块的所有功能。'
                sys 模块有一个 argv 变量，用 list 存储了命令行的所有参数。argv 至少有一个元素，因为第一个参数永远是该 .py 文件的名称，例如：
                运行 python3 hello.py 获得的 sys.argv 就是['hello.py']；
                运行 python3 hello.py Michael 获得的 sys.argv 就是['hello.py', 'Michael']。
            最后，注意到这两行代码：
                if __name__=='__main__':
                    test()

                'if 测试' 当我们在'命令行'运行 hello 模块文件时，Python解释器'把一个特殊变量 __name__ 置为 __main__ '
                而如果在'其他地方'导入该 hello 模块时，'if 判断将失败'
                
                因此，这种 'if 测试'可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是'运行测试'。
                我们可以用命令行运行 hello.py 看看效果：
                $ python3 hello.py
                Hello, world!
                $ python hello.py Michael
                Hello, Michael!
                $ python hello.py Michael point
                Too many arguments!
函数与变量的作用域() -- 实现代码封装和抽象的一种方法
    定义
        在一个模块中，我们可能会定义很多函数和变量，但有的函数和变量我们希望给别人使用，有的函数和变量我们希望仅仅在模块内部使用。
        在Python中，是通过_前缀来实现的。
    正常的函数和变量()

        正常的函数和变量名是公开的（public），可以被直接引用，比如：abc，x123，PI等；
    特殊的函数和变量()
        类似__xxx__这样的变量是特殊变量，'可以被直接引用，但是有特殊用途'，比如上面的__author__，__name__就是特殊变量，hello模块定义
        的文档注释也可以用特殊变量__doc__访问，我们自己的变量一般不要用这种变量名；
    私有的函数和变量()

        类似_xxx和__xxx这样的函数或变量就是非公开的（private），'不应该被直接引用'，比如_abc，__abc等；

    之所以我们说，'private函数和变量“不应该”被直接引用，而不是“不能”被直接引用'，是因为Python并没有一种方法可以完全限制访问
    private函数或变量，但是，从编程习惯上不应该引用private函数或变量。
    
    例
        private函数或变量不应该被别人引用，那它们有什么用呢？请看例子：
        def _private_1(name):
            return 'Hello, %s' % name        

        def _private_2(name):
            return 'Hi, %s' % name        

        def greeting(name):
            if len(name) > 3:
                return _private_1(name)
            else:
                return _private_2(name)
        我们在模块里公开 greeting()函数，而把内部逻辑用private函数隐藏起来了，这样，调用 greeting()函数不用关心内部的private函数细节，
    意义
        这也是一种非常有用的代码封装和抽象的方法，即：
        外部不需要引用的函数全部定义成private，只有外部需要引用的函数才定义为public。

内置模块(build-in modules) -- 无需额外安装和配置，即可直接使用
    datetime 模块 -- 是Python处理日期和时间的标准库
                获取当前日期和时间  
                    from datetime import datetime
                    datetime.now() # 返回当前日期和时间，其类型是datetime
                    例
                        >>> from datetime import datetime
                        >>> now = datetime.now() # 获取当前datetime
                        >>> print(now)
                        2015-05-18 16:28:07.198690
                        >>> print(type(now))
                        <class 'datetime.datetime'>
                        注意到datetime是模块，datetime模块还包含一个datetime类，通过 from datetime import datetime 导入的才是datetime这个类
                        如果仅导入import datetime，则必须引用全名 datetime.datetime 。
                        datetime.now()返回当前日期和时间，其类型是datetime。
                获取指定日期和时间       

                    要指定某个日期和时间，我们直接用参数构造一个datetime：
                        >>> from datetime import datetime
                        >>> dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
                        >>> print(dt)
                        2015-04-19 12:20:00
                datetime转换为timestamp
                    timestamp
                        在计算机中，时间实际上是用数字表示的。我们把1970年1月1日 00:00:00 UTC+00:00时区的时刻称为 epoch time，记为0（1970年以前的时间timestamp为负数），
                        当前时间就是相对于epoch time的秒数，称为 timestamp。
                        你可以认为：
                        timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00
                        对应的北京时间是：
                        timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00
                        可见timestamp的值与时区毫无关系，因为timestamp一旦确定，其UTC时间就确定了，转换到任意时区的时间也是完全确定的，这就是为什么计算机存储的当前
                        时间是以timestamp表示的，因为全球各地的计算机在任意时刻的timestamp都是完全相同的（假定时间已校准）。
                    把一个datetime类型转换为timestamp只需要简单调用 timestamp()方法：
                        >>> from datetime import datetime
                        >>> dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
                        >>> dt.timestamp() # 把datetime转换为timestamp
                        1429417200.0
                        注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。
                        某些编程语言（如Java和JavaScript）的timestamp使用整数表示毫秒数，这种情况下只需要把timestamp除以1000就得到Python的浮点表示方法
                timestamp转换为datetime
                    要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法：
                        >>> from datetime import datetime
                        >>> t = 1429417200.0
                        >>> print(datetime.fromtimestamp(t))
                        2015-04-19 12:20:00
                        注意到'timestamp是一个浮点数，它没有时区的概念，而datetime是有时区的'。上述转换是在timestamp和本地时间做转换。
                    本地时间
                        本地时间是指当前操作系统设定的时区。例如北京时区是东8区，则本地时间：
                        2015-04-19 12:20:00
                        实际上就是UTC+8:00时区的时间：
                        2015-04-19 12:20:00 UTC+8:00
                        而此刻的格林威治标准时间与北京时间差了8小时，也就是UTC+0:00时区的时间应该是：
                        2015-04-19 04:20:00 UTC+0:00
                    timestamp也可以直接被转换到UTC标准时区的时间：
                        >>> from datetime import datetime
                        >>> t = 1429417200.0
                        >>> print(datetime.fromtimestamp(t)) # 本地时间
                        2015-04-19 12:20:00
                        >>> print(datetime.utcfromtimestamp(t)) # UTC时间
                        2015-04-19 04:20:00
                str 转换为datetime
                    datetime.strptime()实现
                        很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把 str 转换为datetime。转换方法是通过datetime.strptime()实现，
                        需要一个日期和时间的格式化字符串：
                        >>> from datetime import datetime
                        >>> cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
                        >>> print(cday)
                        2015-06-01 18:19:59
                    字符串'%Y-%m-%d %H:%M:%S'规定了日期和时间部分的格式。详细的说明请参考Python文档。
                        注意转换后的datetime是没有时区信息的。
                datetime转换为str
                    通过 strftime()实现
                        如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，转换方法是通过 strftime()实现的，同样需要一个日期和时间的格式
                        化字符串：
                        >>> from datetime import datetime
                        >>> now = datetime.now()
                        >>> print(now.strftime('%a, %b %d %H:%M'))
                        Mon, May 05 16:28
                datetime加减
                        对日期和时间进行加减实际上就是把datetime往后或往前计算，得到新的datetime。加减可以直接用+和-运算符，不过需要导入timedelta这个类：
                        >>> from datetime import datetime, timedelta
                        >>> now = datetime.now()
                        >>> now
                        datetime.datetime(2015, 5, 18, 16, 57, 3, 540997)
                        >>> now + timedelta(hours=10)
                        datetime.datetime(2015, 5, 19, 2, 57, 3, 540997)
                        >>> now - timedelta(days=1)
                        datetime.datetime(2015, 5, 17, 16, 57, 3, 540997)
                        >>> now + timedelta(days=2, hours=12)
                        datetime.datetime(2015, 5, 21, 4, 57, 3, 540997)
                        可见，使用timedelta你可以很容易地算出前几天和后几天的时刻。
                本地时间转换为UTC时间
                        本地时间是指系统设定时区的时间，例如北京时间是UTC+8:00时区的时间，而UTC时间指UTC+0:00时区的时间。
                        一个datetime类型有一个时区属性tzinfo，但是默认为None，所以无法区分这个datetime到底是哪个时区，除非强行给datetime设置一个时区：
                        >>> from datetime import datetime, timedelta, timezone
                        >>> tz_utc_8 = timezone(timedelta(hours=8)) # 创建时区UTC+8:00
                        >>> now = datetime.now()
                        >>> now
                        datetime.datetime(2015, 5, 18, 17, 2, 10, 871012)
                        >>> dt = now.replace(tzinfo=tz_utc_8) # 强制设置为UTC+8:00
                        >>> dt
                        datetime.datetime(2015, 5, 18, 17, 2, 10, 871012, tzinfo=datetime.timezone(datetime.timedelta(0, 28800)))
                        如果系统时区恰好是UTC+8:00，那么上述代码就是正确的，否则，不能强制设置为UTC+8:00时区。
                时区转换
                        我们可以先通过utcnow()拿到当前的UTC时间，再转换为任意时区的时间：
                        # 拿到UTC时间，并强制设置时区为UTC+0:00:
                        >>> utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
                        >>> print(utc_dt)
                        2015-05-18 09:05:12.377316+00:00
                        # astimezone()将转换时区为北京时间:
                        >>> bj_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
                        >>> print(bj_dt)
                        2015-05-18 17:05:12.377316+08:00
                        # astimezone()将转换时区为东京时间:
                        >>> tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours=9)))
                        >>> print(tokyo_dt)
                        2015-05-18 18:05:12.377316+09:00
                        # astimezone()将bj_dt转换时区为东京时间:
                        >>> tokyo_dt2 = bj_dt.astimezone(timezone(timedelta(hours=9)))
                        >>> print(tokyo_dt2)
                        2015-05-18 18:05:12.377316+09:00
                        时区转换的关键在于，拿到一个datetime时，要获知其正确的时区，然后强制设置时区，作为基准时间。
                        利用带时区的datetime，通过 astimezone()方法，可以转换到任意时区。
                        注：不是必须从UTC+0:00时区转换到其他时区，任何带时区的datetime都可以正确转换，例如上述bj_dt到tokyo_dt的转换。
    time 模块
    logging 模块 – 不会抛出错误，记录指定信息，输出到文件
		logging模块介绍
			Python的logging模块提供了通用的日志系统，熟练使用logging模块可以方便开发者开发第三方模块或者是自己的Python
			应用。同样这个模块提供不同的日志级别，并可以采用不同的方式记录日志，比如文件，HTTP、GET/POST，SMTP，Socket等，
			甚至可以自己实现具体的日志记录方式。下文我将主要介绍如何使用文件方式记录log。
		logging的好处
			logging不会抛出错误
			允许你指定记录信息的级别
				有debug，info，warning，error等几个级别，当我们指定level=INFO时，logging.debug就不起作用了。同理，
				指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，也不用删除，
				最后统一控制输出哪个级别的信息。
			输出到文件	
				通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。	

			简介
				Python的 logging 模块提供了灵活的日志处理相关功能, 可以用来追踪程序运行的情况。
				logging 模块提供了一系列标准的日志等级: DEBUG, INFO, WARNING, ERROR, CRITICAL, 顾名思义可以大致看出
				它们各自的使用情况。 logging 模块设置的默认等级时 WARNING, 这意味着默认情况下，日志级别为 WARNING, 
				ERROR, CRITICAL 的日志会被记录，而 DEBUG, INFO 的日志会被忽略。
				不同等级的value值如下，只有当value大于 logger 的值才会记录日志。
				Level    Value
				CRITICAL 50
				ERROR    40
				WARNING  30
				INFO     20
				DEBUG    10
				UNSET    0
		简单输出日志
			下面看一个简单的官方文档上的例子:
			import logging
			logging.warning('Watch out!')  # will print a message to the console
			logging.info('I told you so')  # will not print anything
			输出如下：
			WARNING:root:Watch out!
			可以看到info记录的信息没有输出，这是因为默认输出级别不低于WARNING级别的。

			>>> import logging; logging.basicConfig(level=logging.INFO)
			>>> logging.info('info will be shown!')
			INFO:root:info will be shown!
			>>> logging.debug('debug will not be shown!')
			>>> logging.warning('warning will be shown!')
			WARNING:root:warning will be shown!		
		输入日志到文件
			logging 支持输出日志到文件，参考下面示例:
			import logging
			logging.basicConfig(filename='example.log',level=logging.DEBUG)
			logging.debug('This message should go to the log file')
			logging.info('So should this')
			logging.warning('And this, too')
			其中level是指的记录等级， 输出如下：
			DEBUG:root:This message should go to the log file
			INFO:root:So should this
			WARNING:root:And this, too
		几个基本概念
			loggers
				logger是logging模块提供的日志类 Logger 的实例，它提供日志接口可以直接供程序调用。
				logger最常用的操作有两类：配置和发送日志消息。
				可以通过logging.getLogger(name)获取logger对象，如果不指定name则返回root对象，多次使用相同
				的name调用getLogger方法返回同一个logger对象。
			handler
					handler：将日志记录（log record）发送到合适的目的地（destination），比如文件，socket等。一个logger对象可以
					通过addHandler方法添加0到多个handler，每个handler又可以定义不同日志级别，以实现日志分级过滤显示。
					handlers 和轮转日志每个实例都有一个名字，并且实例间有类之间那种继承关系，根据logger的名字来区分，比如叫
					"scan"的logger是叫"scan.text"和"scan.html"的父类(没错，他们是以点号做分隔符)。
					所有logger共同的父类是 root , 就是上面示例中的中间那个默认的root。 basicConfig 默认的输出格式为:
					 severity:logger name:message 。
					Logger是通过 logging.getLogger(name) 来创建，有种在包里命名的惯用做法是：
					logger = logging.getLogger(__name__)
					这样的好处是可以从logger的名字清楚的看到记录的来源。		

					handlers 承担 logging 模块里负责处理合适的信息到不同的地方的角色，下面通过设置一个RotatingFileHandler来
					展示handler的特性。
					有时候需要创建多个轮转日志，每个日志保存一定长度的内容，最多保留一定数量的日志，其余的丢弃，这种情况下，
					可以定义 RotatingFileHandler 来实现:
					logging_rotatingfile_example.py
					import glob
					import logging
					import logging.handlers		

					LOG_FILENAME = 'logging_rotatingfile_example.out'		

					# Set up a specific logger with our desired output level
					my_logger = logging.getLogger('MyLogger')
					my_logger.setLevel(logging.DEBUG)		

					# Add the log message handler to the logger
					handler = logging.handlers.RotatingFileHandler(
					    LOG_FILENAME,
					    maxBytes=20,
					    backupCount=5,
					)
					my_logger.addHandler(handler)		

					# Log some messages
					for i in range(20):
					    my_logger.debug('i = %d' % i)		

					# See what files are created
					logfiles = glob.glob('%s*' % LOG_FILENAME)
					for filename in logfiles:
					    print(filename)
					运行输出如下:
					logging_rotatingfile_example.out
					logging_rotatingfile_example.out.1
					logging_rotatingfile_example.out.2
					logging_rotatingfile_example.out.3
					logging_rotatingfile_example.out.4
					logging_rotatingfile_example.out.5
					当日志内容达到定义的 maxBytes 时，会自动重命名文件后加上后缀".1",如果已经存在后续的".1",".2"等则自动
					重命名他们向后加1，最后最多只保留 backupCount 定义数量的日志文件。
					其它有用的handler参见这里。
			filter

				filter：提供一种优雅的方式决定一个日志记录是否发送到handler。
			Formatters 和 个性化输出
				formatter：指定日志记录输出的具体格式。formatter的构造方法需要两个参数：消息的格式字符串和日期字符串，这两个
				参数都是可选的。
				Formatters 可以用来控制日志输出的格式，参考下面的示例:
					import logging

					# create logger
					logger = logging.getLogger('simple_example')
					logger.setLevel(logging.DEBUG)

					# create console handler and set level to debug
					ch = logging.StreamHandler()
					ch.setLevel(logging.DEBUG)

					# create formatter
					formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

					# add formatter to ch
					ch.setFormatter(formatter)

					# add ch to logger
					logger.addHandler(ch)

					# 'application' code
					logger.debug('debug message')
					logger.info('info message')
					logger.warn('warn message')
					logger.error('error message')
					logger.critical('critical message')
					输出如下:
					2016-11-27 23:18:51,128 - simple_example - DEBUG - debug message
					2016-11-27 23:18:51,128 - simple_example - INFO - info message
					2016-11-27 23:18:51,128 - simple_example - WARNING - warn message
					2016-11-27 23:18:51,128 - simple_example - ERROR - error message
					2016-11-27 23:18:51,128 - simple_example - CRITICAL - critical message
					可以看到 %(asctime)s - %(name)s - %(levelname)s - %(message)s 这里对格式化输出的影响。
					其中默认的日期时间显示的格式是ISO8601格式， 也可以自定义时间格式，如下面的例子:
					import logging
					logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
					logging.warning('is when this event was logged.')
					输出:
					python test12.py
					11/27/2016 11:22:41 PM is when this event was logged.
					好有个比较有用的格式化参数时 %(lineno)d, 显示logger调用的时候所处的行数。具体的格式和作用可以参见这里。
					其它
					logger.exception
					以 ERROR 的等级记录日志，但和 DEBUG 等级一样会输出详细的错误信息，通常用在exception处理中
					Filter Object
					Filters 是可以被handlers和loggers用来过滤日志的输出的，因为用的不多，具体可参见文档。
					线程安全
					logging模块是通过线程锁保证线程安全的。
					Logging Flow
					官方文档上看到的logging流程图，可以帮助理解日志记录流程，参见这里。
					从配置文件获取logging的配置
					参见这里。
					参考资料
					https://docs.python.org/2.7/howto/logging.html
					https://pymotw.com/3/logging/index.html#module-logging
		Python中使用logging模块打印log日志详解
			学一门新技术或者新语言，我们都要首先学会如何去适应这们新技术，其中在适应过程中，我们必须得学习如何调试
			程序并打出相应的log信息来，正所谓“只要log打的好，没有bug解不了”，在我们熟知的一些信息技术中，log4xxx系列
			以及开发Android app时的android.util.Log包等等都是为了开发者更好的得到log信息服务的。在Python这门语言中，
			我们同样可以根据自己的程序需要打出log。
			log信息不同于使用打桩法打印一定的标记信息，log可以根据程序需要而分出不同的log级别，比如info、debug、warn等
			等级别的信息，只要实时控制log级别开关就可以为开发人员提供更好的log信息，与log4xx类似，logger，handler和日志
			消息的调用可以有具体的日志级别（Level），只有在日志消息的级别大于logger和handler的设定的级别，才会显示。
			下面我就来谈谈我在Python中使用的logging模块一些方法。
		基本使用方法
			一些小型的程序我们不需要构造太复杂的log系统，可以直接使用logging模块的basicConfig函数即可，代码如下：
			复制代码 代码如下:			

			'''
			Created on 2012-8-12
			 
			@author: walfred
			@module: loggingmodule.BasicLogger
			'''
			import logging
			 
			log_file = "./basic_logger.log"
			 
			logging.basicConfig(filename = log_file, level = logging.DEBUG)
			 
			logging.debug("this is a debugmsg!")
			logging.info("this is a infomsg!")
			logging.warn("this is a warn msg!")
			logging.error("this is a error msg!")
			logging.critical("this is a critical msg!")
			运行程序时我们就会在该文件的当前目录下发现basic_logger.log文件，查看basic_logger.log内容如下：
			复制代码 代码如下:			

			INFO:root:this is a info msg!
			DEBUG:root:this is a debug msg!
			WARNING:root:this is a warn msg!
			ERROR:root:this is a error msg!
			CRITICAL:root:this is a critical msg!
			需要说明的是我将level设定为DEBUG级别，所以log日志中只显示了包含该级别及该级别以上的log信息。信息级别依次
			是：notset、debug、info、warn、error、critical。如果在多个模块中使用这个配置的话，只需在主模块中配置即可，
			其他模块会有相同的使用效果。
		较高级版本
				上述的基础使用比较简单，没有显示出logging模块的厉害，适合小程序用，现在我介绍一个较高级版本的代码，
				我们需要依次设置logger、handler、formatter等配置。
				复制代码 代码如下:				

				'''
				Created on 2012-8-12
				 
				@author: walfred
				@module: loggingmodule.NomalLogger
				'''
				import logging
				 
				log_file = "./nomal_logger.log"
				log_level = logging.DEBUG
				 
				logger = logging.getLogger("loggingmodule.NomalLogger")
				handler = logging.FileHandler(log_file)
				formatter = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")
				 
				handler.setFormatter(formatter)
				logger.addHandler(handler)
				logger.setLevel(log_level)
				 
				#test
				logger.debug("this is a debug msg!")
				logger.info("this is a info msg!")
				logger.warn("this is a warn msg!")
				logger.error("this is a error msg!")
				logger.critical("this is a critical msg!")
				这时我们查看当前目录的nomal_logger.log日志文件，如下：
				复制代码 代码如下:				

				[DEBUG][][2012-08-12 17:43:59,295]this is a debug msg!
				[INFO][][2012-08-12 17:43:59,295]this is a info msg!
				[WARNING][][2012-08-12 17:43:59,295]this is a warn msg!
				[ERROR][][2012-08-12 17:43:59,295]this is a error msg!
				[CRITICAL][][2012-08-12 17:43:59,295]this is a critical msg!
				这个对照前面介绍的logging模块，不难理解，下面的最终版本将会更加完整。				
		完善版本
				这个最终版本我用singleton设计模式来写一个Logger类，代码如下：
				复制代码 代码如下:				

				'''
				Created on 2012-8-12
				 
				@author: walfred
				@module: loggingmodule.FinalLogger
				'''
				 
				import logging.handlers
				 
				class FinalLogger:
				 
				 logger = None
				 
				 levels = {"n" : logging.NOTSET,
				  "d" : logging.DEBUG,
				  "i" : logging.INFO,
				  "w" : logging.WARN,
				  "e" : logging.ERROR,
				  "c" : logging.CRITICAL}
				 
				 log_level = "d"
				 log_file = "final_logger.log"
				 log_max_byte = 10 * 1024 * 1024;
				 log_backup_count = 5
				 
				 @staticmethod
				 def getLogger():
				  if FinalLogger.logger is not None:
				   return FinalLogger.logger
				 
				  FinalLogger.logger = logging.Logger("oggingmodule.FinalLogger")
				  log_handler = logging.handlers.RotatingFileHandler(filename = FinalLogger.log_file,\
				  maxBytes = FinalLogger.log_max_byte,\
				  backupCount = FinalLogger.log_backup_count)
				  log_fmt = logging.Formatter("[%(levelname)s][%(funcName)s][%(asctime)s]%(message)s")
				  log_handler.setFormatter(log_fmt)
				  FinalLogger.logger.addHandler(log_handler)
				  FinalLogger.logger.setLevel(FinalLogger.levels.get(FinalLogger.log_level))
				  return FinalLogger.logger
				 
				if __name__ == "__main__":
				 logger = FinalLogger.getLogger()
				 logger.debug("this is a debug msg!")
				 logger.info("this is a info msg!")
				 logger.warn("this is a warn msg!")
				 logger.error("this is a error msg!")
				 logger.critical("this is a critical msg!")
				当前目录下的 final_logger.log内容如下：
				复制代码 代码如下:				

				[DEBUG][][2012-08-12 18:12:23,029]this is a debug msg!
				[INFO][][2012-08-12 18:12:23,029]this is a info msg!
				[WARNING][][2012-08-12 18:12:23,029]this is a warn msg!
				[ERROR][][2012-08-12 18:12:23,029]this is a error msg!
				[CRITICAL][][2012-08-12 18:12:23,029]this is a critical msg!				

				这个final版本，也是我一直用的，读者朋友也可以再加上其他的一些Handler，比如StreamHandler等等来获取
				更多的log信息，当然也可以将你的log信息通过配置文件来完成。
    collections--collections是Python内建的一个集合模块，提供了许多有用的集合类
                        namedtuple--一个函数，用来创建自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素往头部添加或删除元素。                       
                        defaultdict--使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defultdict                     
                        OrderedDict--使用dict时，Ke是无序的, 如果要保持Key的顺序，可以用OderedDictalue
                        Counter-一个简单计数器          
                        小结  
                      参考源码tions.py
    base64--一种用64个字符来表示任意二进制数据的方法 
                        乱码
                                    用记事本打开exe、jpg、pdf这些文件时，我们都会看到一大堆乱码，因为二进制文件包含很多无法显示和打印的字符，所以，如果
                                    要让记事本这样的文本处理软件能处理二进制数据，就需要一个二进制到字符串的转换方法。Base64是一种最常见的二进制编码方法。                                    

                        Base64的原理很简单，首先，准备一个包含64个字符的数组 

                                    ['A', 'B', 'C', ... 'a', 'b', 'c', ... '0', '1', ... '+', '/']
                                    然后，对二进制数据进行处理，每3个字节一组，一共是3x8=24bit，划为4组，每组正好6个bit：                                  

                                    base64-encode                                   

                                    这样我们得到4个数字作为索引，然后查表，获得相应的4个字符，就是编码后的字符串。                                    

                                    所以，Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示。                                   

                                    如果要编码的二进制数据不是3的倍数，最后会剩下1个或2个字节怎么办？Base64用'\x00'字节在末尾补足后，再在编码的末尾加上1个或2个=号，
                                    表示补了多少字节，解码的时候，会自动去掉。                                    

                        Python内置的base64可以直接进行base64的编解码：                                    

                                    >>> import base64
                                    >>> base64.b64encode(b'binary\x00string')
                                    b'YmluYXJ5AHN0cmluZw=='
                                    >>> base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
                                    b'binary\x00string'
                        由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_：                                 

                                    >>> base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
                                    b'abcd++//'
                                    >>> base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
                                    b'abcd--__'
                                    >>> base64.urlsafe_b64decode('abcd--__')
                                    b'i\xb7\x1d\xfb\xef\xff'
                        还可以自己定义64个字符的排列顺序，这样就可以自定义Base64编码，不过，通常情况下完全没有必要。                                  

                                    Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行。                                   

                                    Base64适用于小段内容的编码，比如数字证书签名、Cookie的内容等。                                   

                                    由于=字符也可能出现在Base64编码中，但=用在URL、Cookie里面会造成歧义，所以，很多Base64编码后会把=去掉：                                 

                                    # 标准Base64:
                                    'abcd' -> 'YWJjZA=='
                                    # 自动去掉=:
                                    'abcd' -> 'YWJjZA'
                                    去掉=后怎么解码呢？因为Base64是把3个字节变为4个字节，所以，Base64编码的长度永远是4的倍数，因此，需要加上=把Base64字符串
                                    的长度变为4的倍数，就可以正常解码了。                                  

                        小结                                  

                                    Base64是一种任意二进制到文本字符串的编码方法，常用于在URL、Cookie、网页中传输少量二进制数据。                                  

                        练习                                  

                                    请写一个能处理去掉=的base64解码函数：                                  

                                    # -*- coding: utf-8 -*-                                 

                                    import base64                                   

                                    def safe_base64_decode(s):                                  

                                        pass                                    

                                    # 测试:
                                    assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
                                    assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
                                    print('Pass')
                                     Run
                        参考源码                                    

                                    do_base64.py
    hashlib--摘要算法--MD5，SHA1
                        Python的hashlib提供了常见的摘要算法，如MD5，SHA1等等。                       
                        什么是摘要算法呢？
                       摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）。                      

                        举个例子，你写了一篇文章，内容是一个字符串'how to use python hashlib - by Michael'，并附上这篇文章的摘要是
                        '2d73d4f15c0db7f5ecb321b6a65e5d6d'。如果有人篡改了你的文章，并发表为'how to use python hashlib - by Bob'，你可以一下子
                        指出Bob篡改了你的文章，因为根据'how to use python hashlib - by Bob'计算出的摘要不同于原始文章的摘要。                       

                        可见，摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest，目的是为了发现原始数据是否被人篡改过。                      

                        摘要算法之所以能指出数据是否被篡改过，就是因为摘要函数是一个单向函数，计算f(data)很容易，但通过digest反推data却非常困难。
                        而且，对原始数据做一个bit的修改，都会导致计算出的摘要完全不同。                      

                        我们以常见的摘要算法MD5为例，计算出一个字符串的MD5值：                      

                        import hashlib                      

                        md5 = hashlib.md5()
                        md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
                        print(md5.hexdigest())
                        计算结果如下：                     

                        d26a53750bc40b38b65a520292f69306
                        如果数据量很大，可以分块多次调用update()，最后计算的结果是一样的：                       

                        import hashlib                      

                        md5 = hashlib.md5()
                        md5.update('how to use md5 in '.encode('utf-8'))
                        md5.update('python hashlib?'.encode('utf-8'))
                        print(md5.hexdigest())
                        试试改动一个字母，看看计算的结果是否完全不同。                     

                        MD5是最常见的摘要算法，速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示。                     

                        另一种常见的摘要算法是SHA1，调用SHA1和调用MD5完全类似：                       

                        import hashlib                      

                        sha1 = hashlib.sha1()
                        sha1.update('how to use sha1 in '.encode('utf-8'))
                        sha1.update('python hashlib?'.encode('utf-8'))
                        print(sha1.hexdigest())
                        SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示。                       

                        比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长。                        

                        有没有可能两个不同的数据通过某个摘要算法得到了相同的摘要？完全有可能，因为任何摘要算法都是把无限多的数据集合映射到一个有限的集合中。
                        这种情况称为碰撞，比如Bob试图根据你的摘要反推出一篇文章'how to learn hashlib in python - by Bob'，并且这篇文章的摘要恰好和你的文章完全
                        一致，这种情况也并非不可能出现，但是非常非常困难。                        

                        摘要算法应用                      

                        摘要算法能应用到什么地方？举个常用例子：                        

                        任何允许用户登录的网站都会存储用户登录的用户名和口令。如何存储用户名和口令呢？方法是存到数据库表中：                      

                        name    | password
                        --------+----------
                        michael | 123456
                        bob     | abc999
                        alice   | alice2008
                        如果以明文保存用户口令，如果数据库泄露，所有用户的口令就落入黑客的手里。此外，网站运维人员是可以访问数据库的，也就是能获取到所有用户的口令。                      

                        正确的保存口令的方式是不存储用户的明文口令，而是存储用户口令的摘要，比如MD5：                        

                        username | password
                        ---------+---------------------------------
                        michael  | e10adc3949ba59abbe56e057f20f883e
                        bob      | 878ef96e86145580c38c87f0410ad153
                        alice    | 99b1c2188db85afee403b1536010c2c9
                        当用户登录时，首先计算用户输入的明文口令的MD5，然后和数据库存储的MD5对比，如果一致，说明口令输入正确，如果不一致，口令肯定错误。                     

                        练习                      

                        根据用户输入的口令，计算出存储在数据库中的MD5口令：                     

                        def calc_md5(password):
                            pass
                        存储MD5的好处是即使运维人员能访问数据库，也无法获知用户的明文口令。                     

                        设计一个验证用户登录的函数，根据用户输入的口令是否正确，返回True或False：                       

                        db = {
                            'michael': 'e10adc3949ba59abbe56e057f20f883e',
                            'bob': '878ef96e86145580c38c87f0410ad153',
                            'alice': '99b1c2188db85afee403b1536010c2c9'
                        }                       

                        def login(user, password):
                            pass
                        采用MD5存储口令是否就一定安全呢？也不一定。假设你是一个黑客，已经拿到了存储MD5口令的数据库，如何通过MD5反推用户的明文口令呢？暴力破解费事费力，真正的黑客不会这么干。                     

                        考虑这么个情况，很多用户喜欢用123456，888888，password这些简单的口令，于是，黑客可以事先计算出这些常用口令的MD5值，得到一个反推表：                       

                        'e10adc3949ba59abbe56e057f20f883e': '123456'
                        '21218cca77804d2ba1922c33e0151105': '888888'
                        '5f4dcc3b5aa765d61d8327deb882cf99': 'password'
                        这样，无需破解，只需要对比数据库的MD5，黑客就获得了使用常用口令的用户账号。                     

                        对于用户来讲，当然不要使用过于简单的口令。但是，我们能否在程序设计上对简单口令加强保护呢？                       

                        由于常用口令的MD5值很容易被计算出来，所以，要确保存储的用户口令不是那些已经被计算出来的常用口令的MD5，这一方法通过对原始口令加一个复杂字符串来实现，俗称“加盐”：                        

                        def calc_md5(password):
                            return get_md5(password + 'the-Salt')
                        经过Salt处理的MD5口令，只要Salt不被黑客知道，即使用户输入简单口令，也很难通过MD5反推明文口令。                      

                        但是如果有两个用户都使用了相同的简单口令比如123456，在数据库中，将存储两条相同的MD5值，这说明这两个用户的口令是一样的。有没有办法让使用相同口令的用户存储不同的MD5呢？                       

                        如果假定用户无法修改登录名，就可以通过把登录名作为Salt的一部分来计算MD5，从而实现相同口令的用户也存储不同的MD5。                       

                        练习                      

                        根据用户输入的登录名和口令模拟用户注册，计算更安全的MD5：                      

                        db = {}                     

                        def register(username, password):
                            db[username] = get_md5(password + username + 'the-Salt')
                        然后，根据修改后的MD5算法实现用户登录的验证：                        

                        def login(username, password):
                            pass
                        小结                      

                        摘要算法在很多地方都有广泛的应用。要注意摘要算法不是加密算法，不能用于加密（因为无法通过摘要反推明文），只能用于防篡改，但是它的单向计算特性决定了可以在不存储明文口令的情况下验证用户口令。                      

                        参考源码                        

                        use_hashlib.py
    contextlib--任何对象，只要正确实现了上下文管理，就可以用于with语句 
                        在Python中，读写文件这样的资源要特别注意，必须在使用完毕后正确关闭它们。正确关闭文件资源的一个方法是使用 try...finally

                                    try:
                                        f = open('/path/to/file', 'r')
                                        f.read()
                                    finally:
                                        if f:
                                            f.close()
                        写try...finally非常繁琐。Python的with语句允许我们非常方便地使用资源，而不必担心资源没有关闭，所以上面的代码可以简化为：

                                    with open('/path/to/file', 'r') as f:
                                        f.read()
                        并不是只有open()函数返回的fp对象才能使用with语句。实际上，任何对象，只要正确实现了上下文管理，就可以用于with语句。                                   

                                    实现上下文管理是通过__enter__和__exit__这两个方法实现的。例如，下面的class实现了这两个方法：                                   

                                    class Query(object):

                                        def __init__(self, name):
                                            self.name = name                                    

                                        def __enter__(self):
                                            print('Begin')
                                            return self                                 

                                        def __exit__(self, exc_type, exc_value, traceback):
                                            if exc_type:
                                                print('Error')
                                            else:
                                                print('End')                                    

                                        def query(self):
                                            print('Query info about %s...' % self.name)
                                    这样我们就可以把自己写的资源对象用于with语句：                                   

                                    with Query('Bob') as q:
                                        q.query()
                                    @contextmanager                                 

                                    编写__enter__和__exit__仍然很繁琐，因此Python的标准库contextlib提供了更简单的写法，上面的代码可以改写如下：                                  

                                    from contextlib import contextmanager                                   

                                    class Query(object):                                    

                                        def __init__(self, name):
                                            self.name = name                                    

                                        def query(self):
                                            print('Query info about %s...' % self.name)                                 

                                    @contextmanager
                                    def create_query(name):
                                        print('Begin')
                                        q = Query(name)
                                        yield q
                                        print('End')
                                    @contextmanager这个decorator接受一个generator，用yield语句把 with ... as var把变量输出出去，然后，with语句就可以正常地工作了：                                 

                                    with create_query('Bob') as q:
                                        q.query()
                                    很多时候，我们希望在某段代码执行前后自动执行特定代码，也可以用@contextmanager实现。例如：                                    

                                    @contextmanager
                                    def tag(name):
                                        print("<%s>" % name)
                                        yield
                                        print("</%s>" % name)                                   

                                    with tag("h1"):
                                        print("hello")
                                        print("world")
                                    上述代码执行结果为：                                  

                                    <h1>
                                    hello
                                    world
                                    </h1>
                                    代码的执行顺序是：                                   

                                    with语句首先执行yield之前的语句，因此打印出<h1>；
                                    yield调用会执行with语句内部的所有语句，因此打印出hello和world；
                                    最后执行yield之后的语句，打印出</h1>。
                                    因此，@contextmanager让我们通过编写generator来简化上下文管理。                                 

                                    @closing                                    

                                    如果一个对象没有实现上下文，我们就不能把它用于with语句。这个时候，可以用closing()来把该对象变为上下文对象。例如，
                                    用with语句使用urlopen()：                                  

                                    from contextlib import closing
                                    from urllib.request import urlopen                                  

                                    with closing(urlopen('https://www.python.org')) as page:
                                        for line in page:
                                            print(line)
                                    closing也是一个经过@contextmanager装饰的generator，这个generator编写起来其实非常简单：                                 

                                    @contextmanager
                                    def closing(thing):
                                        try:
                                            yield thing
                                        finally:
                                            thing.close()
                                    它的作用就是把任意对象变为上下文对象，并支持with语句。                                   

                                    @contextlib还有一些其他decorator，便于我们编写更简洁的代码。
    XML
                        XML虽然比JSON复杂，在Web中应用也不如以前多了，不过仍有很多地方在用，所以，有必要了解如何操作XML。                                 

                        DOM vs SAX                                  

                                    操作XML有两种方法：DOM和SAX。DOM会把整个XML读入内存，解析为树，因此占用内存大，解析慢，优点是可以任意遍历树的节点。
                                    SAX是流模式，边读边解析，占用内存小，解析快，缺点是我们需要自己处理事件。                                 

                                    正常情况下，优先考虑SAX，因为DOM实在太占内存。                                  

                                    在Python中使用SAX解析XML非常简洁，通常我们关心的事件是start_element，end_element和char_data，准备好这3个函数，然后就可以
                                    解析xml了。                                  

                                    举个例子，当SAX解析器读到一个节点时：                                    

                                    <a href="/">python</a>
                                    会产生3个事件：                                    

                                    start_element事件，在读取<a href="/">时；                                   

                                    char_data事件，在读取python时；                                 

                                    end_element事件，在读取</a>时。                                 

                                    用代码实验一下：                                    

                                    from xml.parsers.expat import ParserCreate                                  

                                    class DefaultSaxHandler(object):
                                        def start_element(self, name, attrs):
                                            print('sax:start_element: %s, attrs: %s' % (name, str(attrs)))                                  

                                        def end_element(self, name):
                                            print('sax:end_element: %s' % name)                                 

                                        def char_data(self, text):
                                            print('sax:char_data: %s' % text)                                   

                                    xml = r'''<?xml version="1.0"?>
                                    <ol>
                                        <li><a href="/python">Python</a></li>
                                        <li><a href="/ruby">Ruby</a></li>
                                    </ol>
                                    '''                                 

                                    handler = DefaultSaxHandler()
                                    parser = ParserCreate()
                                    parser.StartElementHandler = handler.start_element
                                    parser.EndElementHandler = handler.end_element
                                    parser.CharacterDataHandler = handler.char_data
                                    parser.Parse(xml)
                                    需要注意的是读取一大段字符串时，CharacterDataHandler可能被多次调用，所以需要自己保存起来，在EndElementHandler里面再合并。                                 

                        除了解析XML外，如何生成XML呢？99%的情况下需要生成的XML结构都是非常简单的，因此，最简单也是最有效的生成XML的方法是拼接字符串：                                  

                                    L = []
                                    L.append(r'<?xml version="1.0"?>')
                                    L.append(r'<root>')
                                    L.append(encode('some & data'))
                                    L.append(r'</root>')
                                    return ''.join(L)
                                    如果要生成复杂的XML呢？建议你不要用XML，改成JSON。                                  

                        小结                                  

                                    解析XML时，注意找出自己感兴趣的节点，响应事件时，把节点数据保存起来。解析完毕后，就可以处理数据。                                  

                        练习                                  

                                    请利用SAX编写程序解析Yahoo的XML格式的天气预报，获取当天和第二天的天气：                                   

                                    http://weather.yahooapis.com/forecastrss?u=c&w=2151330                                  

                                    参数w是城市代码，要查询某个城市代码，可以在weather.yahoo.com搜索城市，浏览器地址栏的URL就包含城市代码。                                  

                                    # -*- coding:utf-8 -*-                                  

                                    from xml.parsers.expat import ParserCreate                                  

                                    class WeatherSaxHandler(object):
                                        pass                                    

                                    def parse_weather(xml):
                                        return {
                                            'city': 'Beijing',
                                            'country': 'China',
                                            'today': {
                                                'text': 'Partly Cloudy',
                                                'low': 20,
                                                'high': 33
                                            },
                                            'tomorrow': {
                                                'text': 'Sunny',
                                                'low': 21,
                                                'high': 34
                                            }
                                        }                                   

                                    # 测试:
                                    data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
                                    <rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
                                        <channel>
                                            <title>Yahoo! Weather - Beijing, CN</title>
                                            <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
                                            <yweather:location city="Beijing" region="" country="China"/>
                                            <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
                                            <yweather:wind chill="28" direction="180" speed="14.48" />
                                            <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
                                            <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
                                            <item>
                                                <geo:lat>39.91</geo:lat>
                                                <geo:long>116.39</geo:long>
                                                <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
                                                <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
                                                <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
                                                <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
                                                <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
                                                <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
                                                <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
                                            </item>
                                        </channel>
                                    </rss>
                                    '''
                                    weather = parse_weather(data)
                                    assert weather['city'] == 'Beijing', weather['city']
                                    assert weather['country'] == 'China', weather['country']
                                    assert weather['today']['text'] == 'Partly Cloudy', weather['today']['text']
                                    assert weather['today']['low'] == 20, weather['today']['low']
                                    assert weather['today']['high'] == 33, weather['today']['high']
                                    assert weather['tomorrow']['text'] == 'Sunny', weather['tomorrow']['text']
                                    assert weather['tomorrow']['low'] == 21, weather['tomorrow']['low']
                                    assert weather['tomorrow']['high'] == 34, weather['tomorrow']['high']
                                    print('Weather:', str(weather))
                                     Run
                        参考源码                                    

                                    use_sax.py
    HTMLParser--   利用HTMLParser，可以把网页中的文本、图像等解析出来
                        如果我们要编写一个搜索引擎，第一步是用爬虫把目标网站的页面抓下来，第二步就是解析该HTML页面，看看里面的内容到底是新闻、图片还是视频。                                    

                        假设第一步已经完成了，第二步应该如何解析HTML呢？                                  

                        HTML本质上是XML的子集，但是HTML的语法没有XML那么严格，所以不能用标准的DOM或SAX来解析HTML。                                   

                        好在Python提供了HTMLParser来非常方便地解析HTML，只需简单几行代码：

                                    from html.parser import HTMLParser
                                    from html.entities import name2codepoint                                    

                                    class MyHTMLParser(HTMLParser):                                 

                                        def handle_starttag(self, tag, attrs):
                                            print('<%s>' % tag)                                 

                                        def handle_endtag(self, tag):
                                            print('</%s>' % tag)                                    

                                        def handle_startendtag(self, tag, attrs):
                                            print('<%s/>' % tag)                                    

                                        def handle_data(self, data):
                                            print(data)                                 

                                        def handle_comment(self, data):
                                            print('<!--', data, '-->')                                  

                                        def handle_entityref(self, name):
                                            print('&%s;' % name)                                    

                                        def handle_charref(self, name):
                                            print('&#%s;' % name)                                   

                                    parser = MyHTMLParser()
                                    parser.feed('''<html>
                                    <head></head>
                                    <body>
                                    <!-- test html parser -->
                                        <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...<br>END</p>
                                    </body></html>''')
                                    feed()方法可以多次调用，也就是不一定一次把整个HTML字符串都塞进去，可以一部分一部分塞进去。                                  

                                    特殊字符有两种，一种是英文表示的&nbsp;，一种是数字表示的&#1234;，这两种字符都可以通过Parser解析出来。                                    
                        小结

                                    利用HTMLParser，可以把网页中的文本、图像等解析出来。                                 
                        练习

                                    找一个网页，例如https://www.python.org/events/python-events/，用浏览器查看源码并复制，然后尝试解析一下HTML，输出Python官网
                                    发布的会议时间、名称和地点。                                  
                        参考源码

                                    use_htmlparser.py
    urllib--操作URL--利用程序去执行各种HTTP请求--抓取URL内容
                        Get

                                    urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：                                  

                                    例如，对豆瓣的一个URLhttps://api.douban.com/v2/book/2129650进行抓取，并返回响应：                                   

                                    from urllib import request                                  

                                    with request.urlopen('https://api.douban.com/v2/book/2129650') as f:
                                        data = f.read()
                                        print('Status:', f.status, f.reason)
                                        for k, v in f.getheaders():
                                            print('%s: %s' % (k, v))
                                        print('Data:', data.decode('utf-8'))
                                    可以看到HTTP响应的头和JSON数据：                                    

                                    Status: 200 OK
                                    Server: nginx
                                    Date: Tue, 26 May 2015 10:02:27 GMT
                                    Content-Type: application/json; charset=utf-8
                                    Content-Length: 2049
                                    Connection: close
                                    Expires: Sun, 1 Jan 2006 01:00:00 GMT
                                    Pragma: no-cache
                                    Cache-Control: must-revalidate, no-cache, private
                                    X-DAE-Node: pidl1
                                    Data: {"rating":{"max":10,"numRaters":16,"average":"7.4","min":0},"subtitle":"","author":["廖雪峰编著"],"pubdate":"2007-6","tags":[{"count":20,"name":"spring","title":"spring"}...}
                                    如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。例如，
                                    模拟iPhone 6去请求豆瓣首页：                                  

                                    from urllib import request                                  

                                    req = request.Request('http://www.douban.com/')
                                    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
                                    with request.urlopen(req) as f:
                                        print('Status:', f.status, f.reason)
                                        for k, v in f.getheaders():
                                            print('%s: %s' % (k, v))
                                        print('Data:', f.read().decode('utf-8'))
                                    这样豆瓣会返回适合iPhone的移动版网页：                                  

                                    ...
                                        <meta name="viewport" content="width=device-width, user-scalable=no, initial-scale=1.0, minimum-scale=1.0, maximum-scale=1.0">
                                        <meta name="format-detection" content="telephone=no">
                                        <link rel="apple-touch-icon" sizes="57x57" href="http://img4.douban.com/pics/cardkit/launcher/57.png" />
                                    ...
                        Post

                                    如果要以POST发送一个请求，只需要把参数data以bytes形式传入。                                    

                                    我们模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入：                                  

                                    from urllib import request, parse                                   

                                    print('Login to weibo.cn...')
                                    email = input('Email: ')
                                    passwd = input('Password: ')
                                    login_data = parse.urlencode([
                                        ('username', email),
                                        ('password', passwd),
                                        ('entry', 'mweibo'),
                                        ('client_id', ''),
                                        ('savestate', '1'),
                                        ('ec', ''),
                                        ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
                                    ])                                  

                                    req = request.Request('https://passport.weibo.cn/sso/login')
                                    req.add_header('Origin', 'https://passport.weibo.cn')
                                    req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
                                    req.add_header('Referer', 'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')                                   

                                    with request.urlopen(req, data=login_data.encode('utf-8')) as f:
                                        print('Status:', f.status, f.reason)
                                        for k, v in f.getheaders():
                                            print('%s: %s' % (k, v))
                                        print('Data:', f.read().decode('utf-8'))
                                    如果登录成功，我们获得的响应如下：                                   

                                    Status: 200 OK
                                    Server: nginx/1.2.0
                                    ...
                                    Set-Cookie: SSOLoginState=1432620126; path=/; domain=weibo.cn
                                    ...
                                    Data: {"retcode":20000000,"msg":"","data":{...,"uid":"1658384301"}}
                                    如果登录失败，我们获得的响应如下：                                   

                                    ...
                                    Data: {"retcode":50011015,"msg":"\u7528\u6237\u540d\u6216\u5bc6\u7801\u9519\u8bef","data":{"username":"example@python.org","errline":536}}
                                    Handler                                 

                                    如果还需要更复杂的控制，比如通过一个Proxy去访问网站，我们需要利用ProxyHandler来处理，示例代码如下：                                  

                                    proxy_handler = urllib.request.ProxyHandler({'http': 'http://www.example.com:3128/'})
                                    proxy_auth_handler = urllib.request.ProxyBasicAuthHandler()
                                    proxy_auth_handler.add_password('realm', 'host', 'username', 'password')
                                    opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler)
                                    with opener.open('http://www.example.com/login.html') as f:
                                        pass
                        小结

                                    urllib提供的功能就是利用程序去执行各种HTTP请求。如果要模拟浏览器完成特定功能，需要把请求伪装成浏览器。伪装的方法是先监控浏览器
                                    发出的请求，再根据浏览器的请求头来伪装，User-Agent头就是用来标识浏览器的。                                  

                        练习                                  

                                    利用urllib读取XML，将XML一节的数据由硬编码改为由urllib获取：                                 

                                    from urllib import request, parse                                   

                                    def fetch_xml(url):                                 

                                        pass                                    

                                    # 测试
                                    print(fetch_xml('http://weather.yahooapis.com/forecastrss?u=c&w=2151330'))
                                     Run
                        参考源码                                    

                                    use_urllib.py
    uuid模块
                    概述：

                        UUID是128位的全局唯一标识符，通常由32字节的字符串表示。
                        它可以保证时间和空间的唯一性，也称为GUID，全称为：
                                UUID —— Universally Unique IDentifier      Python 中叫 UUID
                                GUID —— Globally Unique IDentifier          C#  中叫 GUID

                        它通过MAC地址、时间戳、命名空间、随机数、伪随机数来保证生成ID的唯一性。
                        UUID主要有五个算法，也就是五种方法来实现：

                           1、uuid1()——基于时间戳

                                   由MAC地址、当前时间戳、随机数生成。可以保证全球范围内的唯一性，
                                   但MAC的使用同时带来安全性问题，局域网中可以使用IP来代替MAC。

                           2、uuid2()——基于分布式计算环境DCE（Python中没有这个函数）

                                    算法与uuid1相同，不同的是把时间戳的前4位置换为POSIX的UID。
                                    实际中很少用到该方法。

                          3、uuid3()——基于名字的MD5散列值

                                    通过计算名字和命名空间的MD5散列值得到，保证了同一命名空间中不同名字的唯一性，
                                    和不同命名空间的唯一性，但同一命名空间的同一名字生成相同的uuid。    

                           4、uuid4()——基于随机数

                                    由伪随机数得到，有一定的重复概率，该概率可以计算出来。

                           5、uuid5()——基于名字的SHA-1散列值

                                    算法与uuid3相同，不同的是使用 Secure Hash Algorithm 1 算法

                    使用方面：

                        首先，Python中没有基于DCE的，所以uuid2可以忽略；
                        其次，uuid4存在概率性重复，由无映射性，最好不用；
                        再次，若在Global的分布式计算环境下，最好用uuid1；
                        最后，若有名字的唯一性要求，最好用uuid3或uuid5。

                    编码方法：

                        # -*- coding: utf-8 -*-

                        import uuid

                        name = "test_name"
                        namespace = "test_namespace"

                        print uuid.uuid1()  # 带参的方法参见Python Doc
                        print uuid.uuid3(namespace, name)
                        print uuid.uuid4()
                        print uuid.uuid5(namespace, name)

                        
                        uuid模块在Python 2.5以后引入，接口包括：不可变对象UUID（UUID类）和函数uuid1()、uuid3()、uuid4()和uuid5()，后面的四个函数用于生成 
                        RFC 4122 规范中指定的第1、3、4、5版UUID。使用uuid1()或uuid4()可以获得一个唯一的ID，uuid1()包含了主机的网络名称，uuid4()不涉及网络主机名，
                        仅生成一个随机UUID，因此从隐私保护角度uuid4()更加安全。

                         

                         class uuid.UUID([hex[, bytes[, bytes_le[, fields[, int[, version]]]]]]) 

                        　　该类用于从参数给定的内容中实例化UUID对象（hex, bytes, bytes_le, fields, int 必须且只能指定一个）：

                        　　hex：指定32个字符以创建UUID对象，当指定一个32个字符构成的字符串来创建一个UUID对象时，花括号、连字符和URN前缀等都是可选的；

                        　　bytes：指定一个大端字节序的总长16字节的字节串来创建UUID对象；

                        　　bytes_le：指定一个小端字节序的总长16字节的字节串来创建UUID对象；

                        　　fields：指定6个整数域，共计128位来创建UUID（其中，32位作为time_low段，16位作为time_mid段，16位作为time_hi_version段，8位作为clock_seq_hi_variant段，8位作为clock_seq_low段，48位作为node段）；

                        　　int：直接指定一个长度为128个二进制位的整数用于创建UUID对象；

                        　　version：（可选）指定UUID的版本，从1到5，一旦指定了该参数，生成的UUID将具有自己的变体（variant）和版本数，具体请参考RFC 4122，

                         

                         例.

                        下面的各种方法创建相同的UUID对象，
                        u = UUID('{12345678-1234-5678-1234-567812345678}')
                        u = UUID(hex = '12345678123456781234567812345678')
                        u = UUID('urn:uuid:12345678-1234-5678-1234-567812345678')
                        u = UUID(bytes='\x12\x34\x56\x78'*4)
                        u = UUID(bytes_le='\x78\x56\x34\x12\x34\x12\x78\x56' +
                                      '\x12\x34\x56\x78\x12\x34\x56\x78')
                        u = UUID(fields=(0x12345678, 0x1234, 0x5678, 0x12, 0x34, 0x567812345678))
                        u = UUID(int=0x12345678123456781234567812345678)
                         

                        UUID对象含有以下只读属性

                         UUID.bytes 

                        　　以16个字节构成的字节串形式表示UUID，包含6个大端字节序的整数域；

                        >>> u.bytes
                        '\x124Vx\x124Vx\x124Vx\x124Vx'
                         　　

                         UUID.bytes_le 

                        　　以16个字节构成的字节串形式表示UUID，包含6个小端字节序的整数域；

                        >>> u.bytes_le
                        'xV4\x124\x12xV\x124Vx\x124Vx'
                        　　

                         UUID.fields 
                        　　以元组形式存放的UUID的6个整数域，该元组中的6个元素分别可以通过6个属性查看，还额外导出了两个属性（下面的每个域的名称也是UUID对象的一个属性）：
                        域   含义
                        time_low    UUID的初始32位
                        time_mid    接前一域的16位
                        time_hi_version 接前一域的16位
                        clock_seq_hi_variant    接前一域的8位
                        clock_seq_low   接前一域的8位
                        node    UUID的最后48位
                        time    UUID的总长60位的时间戳
                        clock_seq   14位的序列号
                        1
                        2
                        >>> u.fields
                        (305419896L, 4660L, 22136L, 18L, 52L, 95073701484152L)
                         
                         UUID.hex 
                        　　以32个字符表示的UUID
                        1
                        2
                        >>> u.hex
                        '12345678123456781234567812345678'
                        　　
                         UUID.int 
                        　　以一个长度为128个二进制位的整数表示的UUID；
                        1
                        2
                        >>> u.int
                        24197857161011715162171839636988778104L
                        　　
                         UUID.urn 
                        　　以 RFC 4122 中指定的URN形式表示的UUID；
                        1
                        2
                        >>> u.urn
                        'urn:uuid:12345678-1234-5678-1234-567812345678'
                        　　
                         UUID.variant 
                        　　UUID变体（variant），决定UUID内部的布局，已有的值为 RESERVED_NCS、RFC_4122、RESERVED_MICROSOFT 或 RESERVED_FUTURE；
                        1
                        2
                        >>> u.variant
                        'reserved for NCS compatibility'
                        　　
                         UUID.version 
                        　　UUID版本，只有当变体为 RFC_4122 时才有效。
                        1
                        2
                        >>> u.version
                        >>>
                        　　这里由于u.variant == 'reserved for NCS compatibility'，所以此处u.version为空。

                        　　
                        uuid模块还定义了如下函数
                         
                         uuid.getnode() 
                        　　获取硬件的地址并以48位二进制长度的正整数形式返回，这里所说的硬件地址是指网络接口的MAC地址，如果一个机器有多个网络接口，可能返回其中的任一个。如果获取失败，将按照RFC 4122的规定将随机返回的48位二进制整数的第8位设置成1。
                        1
                        2
                        >>> uuid.getnode()
                        152667293855L
                        　　
                         uuid.uuid1([node[, clock_seq]]) 
                        　　利用主机ID、序列号和当前时间生成一个UUID，如果参数 node 没有给定，会调用 getnode() 来获取硬件地址。如果参数中指定了 clock_seq ，使用参数中给定的时钟序列作为序列号，否则使用一个随机的14位长的序列号。
                        1
                        2
                        >>> uuid.uuid1()
                        UUID('a89e9d00-a710-11e4-a84a-00238bae089f')
                        　　
                         uuid.uuid3(namespace, name) 
                        　　基于命名空间标识符（实质上是一个UUID）和一个名称（实质上是一个字符串）的MD5哈希值生成UUID。
                        　　
                         uuid.uuid4() 
                        　　生成一个随机的UUID
                        1
                        2
                        >>> uuid4()
                        UUID('b9f9fb88-49f3-4cea-9885-19e57c3572c6')
                        　　
                         uuid.uuid5(namespace, name) 
                        　　基于命名空间标识符（实质上是一个UUID）和一个名称（实质上是一个字符串）的SHA-1哈希值生成UUID
                        　　
                        关于uuid3()和uuid5()中提到的命名空间标识符，uuid模块定义了如下的备选项
                         uuid.NAMESPACE_DNS 
                        　　当指定该命名空间时，参数 name 是一个完全限定的（fully-qualified）域名
                        　　
                         uuid.NAMESPACE_URL 
                        　　当指定该命名空间时，参数 name 是一个URL
                        　　
                         uuid.NAMESPACE_OID 
                        　　当指定该命名空间时，参数 name 是一个ISO OID
                        　　
                         uuid.NAMESPACE_X500 
                        　　当指定该命名空间时，参数 name 是一个DER格式或文本格式的X.500 DN。
                        　　
                        关于属性variant，uuid模块定义了如下的常量
                        　　
                         uuid.RESERVED_NCS 
                        　　该常量为兼容NCS而保留；
                        　　
                         uuid.RFC_4122 
                        　　按照 RFC 4122 的规定来确定UUID的布局；
                        　　
                         uuid.RESERVED_MICROSOFT 
                        　　该常量位兼容微软而保留
                         　　
                         uuid.RESERVED_FUTURE 
                        　　该常量为未来可能的定义保留
                        可以在Python中查看这些常量：
                        1
                        2
                        3
                        4
                        5
                        6
                        7
                        8
                        >>> uuid.RESERVED_NCS
                        'reserved for NCS compatibility'
                        >>> uuid.RFC_4122
                        'specified in RFC 4122'
                        >>> uuid.RESERVED_MICROSOFT
                        'reserved for Microsoft compatibility'
                        >>> uuid.RESERVED_FUTURE
                        'reserved for future definition'
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
                    JSON类型  Python类型
                    {}  dict
                    []  list
                    "string"    str
                    1234.56 int或float
                    true/false  True/False
                    null    None
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
    inspect 模块 --  用于检查运行模块的一些基本信息
                    
                Python使用inspect查看代码参数
                            使用import inspect查看python 类的参数和模块、函数代码

                                         文件就是最小的模块，文件夹是比较大的模块。

                                        文件里面可以包含类，函数。

                                        函数可以执行一个操作，多个函数组合在一起可以写为一个模块，根据不同事物写成一个类，这个类包含几个行为写成几个类内的函数，也可以
                                        将这些作为一个文件。

                                        主要步骤是将文件路径设置到系统，再将文件作为模块引入，再开始查看文件里面的内容。

                                         

                                        首先，写了一个函数

                                        复制代码
                                        def h():
                                            print "hello"

                                        def hm(m,k):
                                            print m, k


                                        class w(object):
                                            def __init__(a, self):
                                                name =a
                                            def g(self):
                                                print name,"hello world!"
                                        复制代码
                                        保存在路径C:\下，起个名字叫hello.py

                                        打开python shell 窗口，将这个路径加入到系统路径里。命令如下

                                        import sys

                                        sys.path.append('C:/')

                                        将文件当做一个模块引入。

                                        import hello

                                        import inspect

                                         

                            查看整个模块hello的源代码: inspect.getsource(hello)  整个样子不好看，需要print inspect.getsource(hello)

                            查看模块hello里面wo这个类的全部代码  print inspect.getsource(hello.w)

                            查看模块内某个函数的代码： print inspect.getsource(hello.h)

                            查看模块内某个类中函数的代码 print inspect.getsource(hello.w.g)

                                         

                            查看模块中某个函数的参数的代码：inspect.getargspec(hello.hm)

                            查看模块中类的参数代码 inspect.getargspec(hello.w.__init__)   #这里还是查看类的初始定义函数。

                            查看类中函数参数代码 inspect.getargspec(hello.w.g)

                            查看模块路径 inspect.getabsfile(hello)  

                            查看文件夹模块中某个类的路径 inspect.getabsfile（。。。）#结果是显示类的初始定义函数__init__.py的位置。

                                         

                                         

                                         >>> inspect.getabsfile(django.db)

                                        'c:\\python27\\lib\\site-packages\\django-1.7.1-py2.7.egg\\django\\db\\__init__.py'

                            综上，最重要的是要记住，

                                        查看全部代码 inspect.getsource(模块.函数）或者（模块.类.函数）

                                        查看函数参数 inspect.getargspec(...)   查看类的参数，则括号里为（模块.类.__init__）

                                        查看函数的位置 inspect.getabsfile(...) 
                                        这些应该够学习用了。以后有什么再补充

                关于python中inspect模块的一些探究

                            前言

                                        我在学习到实战Day5 - python教程 - 廖雪峰的官方网站时，遇到了inspect模块，之前对这个inspect模块一无所知啊，所以本着打破砂锅问到底的精神，
                                        决定对inspect模块做一些探究。

                                        根据度娘搜到的，inspect模块主要提供了四种用处：

                                        (1). 对是否是模块，框架，函数等进行类型检查。

                                        (2). 获取源码

                                        (3). 获取类或函数的参数的信息

                                        (4). 解析堆栈

                                        我在这次课程中，只用到了第三种用处，即获取类或函数的参数的信息，下面我来探究一下。
                            探究

                                        结合我正在学习的课程，我自己也对inspect做了一些探究。根据在课程中用到的一些函数及方法，我做了一个python脚本。

                                        # test
                                        import inspect
                                        def a(a, b=0, *c, d, e=1, **f):
                                            pass
                                        aa = inspect.signature(a)
                                        print("inspect.signature（fn)是:%s" % aa)
                                        print("inspect.signature（fn)的类型：%s" % (type(aa)))
                                        print("\n")

                                        bb = aa.parameters
                                        print("signature.paramerters属性是:%s" % bb)
                                        print("ignature.paramerters属性的类型是%s" % type(bb))
                                        print("\n")

                                        for cc, dd in bb.items():
                                            print("mappingproxy.items()返回的两个值分别是：%s和%s" % (cc, dd))
                                            print("mappingproxy.items()返回的两个值的类型分别是：%s和%s" % (type(cc), type(dd)))
                                            print("\n")
                                            ee = dd.kind
                                            print("Parameter.kind属性是:%s" % ee)
                                            print("Parameter.kind属性的类型是:%s" % type(ee))
                                            print("\n")
                                            gg = dd.default
                                            print("Parameter.default的值是: %s" % gg)
                                            print("Parameter.default的属性是: %s" % type(gg))
                                            print("\n")


                                        ff = inspect.Parameter.KEYWORD_ONLY
                                        print("inspect.Parameter.KEYWORD_ONLY的值是:%s" % ff)
                                        print("inspect.Parameter.KEYWORD_ONLY的类型是:%s" % type(ff))
                                        执行以上脚本，将得到如下输出：

                                        inspect.signature（fn)是:(a, b=0, *c, d, e=1, **f)
                                        inspect.signature（fn)的类型：<class 'inspect.Signature'>


                                        signature.paramerters属性是:OrderedDict([('a', <Parameter "a">), ('b', <Parameter "b=0">), ('c', <Parameter "*c">), ('d', <Parameter "d">), ('e', <Parameter "e=1">), ('f', <Parameter "**f">)])
                                        ignature.paramerters属性的类型是<class 'mappingproxy'>


                                        mappingproxy.items()返回的两个值分别是：a和a
                                        mappingproxy.items()返回的两个值的类型分别是：<class 'str'>和<class 'inspect.Parameter'>


                                        Parameter.kind属性是:POSITIONAL_OR_KEYWORD
                                        Parameter.kind属性的类型是:<enum '_ParameterKind'>


                                        Parameter.default的值是: <class 'inspect._empty'>
                                        Parameter.default的属性是: <class 'type'>


                                        mappingproxy.items()返回的两个值分别是：b和b=0
                                        mappingproxy.items()返回的两个值的类型分别是：<class 'str'>和<class 'inspect.Parameter'>


                                        Parameter.kind属性是:POSITIONAL_OR_KEYWORD
                                        Parameter.kind属性的类型是:<enum '_ParameterKind'>


                                        Parameter.default的值是: 0
                                        Parameter.default的属性是: <class 'int'>


                                        mappingproxy.items()返回的两个值分别是：c和*c
                                        mappingproxy.items()返回的两个值的类型分别是：<class 'str'>和<class 'inspect.Parameter'>


                                        Parameter.kind属性是:VAR_POSITIONAL
                                        Parameter.kind属性的类型是:<enum '_ParameterKind'>


                                        Parameter.default的值是: <class 'inspect._empty'>
                                        Parameter.default的属性是: <class 'type'>


                                        mappingproxy.items()返回的两个值分别是：d和d
                                        mappingproxy.items()返回的两个值的类型分别是：<class 'str'>和<class 'inspect.Parameter'>


                                        Parameter.kind属性是:KEYWORD_ONLY
                                        Parameter.kind属性的类型是:<enum '_ParameterKind'>


                                        Parameter.default的值是: <class 'inspect._empty'>
                                        Parameter.default的属性是: <class 'type'>


                                        mappingproxy.items()返回的两个值分别是：e和e=1
                                        mappingproxy.items()返回的两个值的类型分别是：<class 'str'>和<class 'inspect.Parameter'>


                                        Parameter.kind属性是:KEYWORD_ONLY
                                        Parameter.kind属性的类型是:<enum '_ParameterKind'>


                                        Parameter.default的值是: 1
                                        Parameter.default的属性是: <class 'int'>


                                        mappingproxy.items()返回的两个值分别是：f和**f
                                        mappingproxy.items()返回的两个值的类型分别是：<class 'str'>和<class 'inspect.Parameter'>


                                        Parameter.kind属性是:VAR_KEYWORD
                                        Parameter.kind属性的类型是:<enum '_ParameterKind'>


                                        Parameter.default的值是: <class 'inspect._empty'>
                                        Parameter.default的属性是: <class 'type'>


                                        inspect.Parameter.KEYWORD_ONLY的值是:KEYWORD_ONLY
                                        inspect.Parameter.KEYWORD_ONLY的类型是:<enum '_ParameterKind'>
                            总结

                                        inspect.signature（fn)将返回一个inspect.Signature类型的对象，值为fn这个函数的所有参数

                                        inspect.Signature对象的paramerters属性是一个mappingproxy（映射）类型的对象，值为一个有序字典（Orderdict)。

                                        这个字典里的key是即为参数名，str类型

                                        这个字典里的value是一个inspect.Parameter类型的对象，根据我的理解，这个对象里包含的一个参数的各种信息

                                        inspect.Parameter对象的kind属性是一个_ParameterKind枚举类型的对象，值为这个参数的类型（可变参数，关键词参数，etc）

                                        inspect.Parameter对象的default属性：如果这个参数有默认值，即返回这个默认值，如果没有，返回一个inspect._empty类。                                    
    functools 模块 -- 为高阶函数提供支持
                        该模块为高阶函数提供支持——作用于或返回函数的函数被称为高阶函数。在该模块看来，一切可调用的对象均可视为本模块中所说的“函数”。
                        目录

                                    　　一、模块方法

                                    　　　　1. functools.cmp_to_key(func)

                                    　　　　2. functools.total_ordering(cls)

                                    　　　　3. functools.reduce(function, iterable[, initializer])

                                    　　　　*4. functools.partial(func[,*args][, **keywords])

                                    　　　　5. functools.update_wrapper(wrapper, wrapped[, assigned][, updated])

                                    　　　　*6. functools.wraps(wrapped[, assigned][, updated])

                                    　　二、partial对象

                                    　　　　1. partial.func

                                    　　　　2. partial.args

                                    　　　　3. partial.keywords       

                        一、模块方法

                                    　　该模块中定义了如下方法：

                                    functools.cmp_to_key(func) 

                                                　　将老式的比较函数（comparison function）转化为关键字函数（key function）。与接受key function的工具一同使用
                                                （如 sorted(), min(), max(), heapq.nlargest(), itertools.groupby())。该函数主要用来将程序转成 Python 3 格式的，因为 Python 3 中不支持比较函数。

                                                　　比较函数是可调用的，接受两个参数，比较这两个参数并根据他们的大小关系返回负值、零或正值中的某一个。关键字函数也是可调用的，接受
                                                一个参数，同时返回一个可以用作排序关键字的值。

                                                　　例如：

                                                sorted(iterable, key=cmp_to_key(locale.strcoll))
                                    functools.total_ordering(cls) 

                                                    　　这是一个类装饰器，给定一个类，这个类定义了一个或多个比较排序方法，这个类装饰器将会补充其余的比较方法，减少了自己定义所有比较方法
                                                    时的工作量。

                                                    　　被修饰的类必须至少定义 __lt__(), __le__(), __gt__() 或 __ge__() 中的一个，同时，被修饰的类还应该提供 __eq__() 方法。

                                                    　　例如：

                                                    复制代码
                                                    @total_ordering
                                                    class Student:
                                                        def __eq__(self, other):
                                                            return ((self.lastname.lower(), self.firstname.lower()) ==
                                                                    (other.lastname.lower(), other.firstname.lower()))
                                                        def __lt__(self, other):
                                                            return ((self.lastname.lower(), self.firstname.lower()) <
                                                                    (other.lastname.lower(), other.firstname.lower()))
                                                    复制代码
                                    functools.reduce(function, iterable[, initializer]) 

                                                和 reduce() 方法的作用相同，这里提供了向 Python 3 过渡的前向支持。
                                    functools.partial(func[,*args][, **keywords]) 

                                                　　函数装饰器，返回一个新的 partial 对象，关于 partial 对象的介绍见下文。调用 partial 对象就和调用被修饰的函数 func 相同，只不过调用 partial 
                                                对象时传入的参数个数通常少于调用 func 时传入的参数个数。 当一个函数 func 可以接收很多参数，而某一次使用只需要更改其中的一部分参数，其他
                                                的某些参数都保持不变时， partial 对象就可以将这些不变的对象冻结起来，这样调用 partial 对象时传入未冻结的参数， partial 对象调用 func 时连同
                                                已经被冻结的参数一同传给 func 函数，从而简化了调用过程。

                                                　　如果调用 partial 对象时提供了更多的参数，那么他们会被添加到 args 的后面，如果提供了更多的关键字参数，那么它们将扩展或覆写已经冻结的
                                                关键字参数

                                                　　 partial 对象的作用大抵如下：

                                                复制代码
                                                def partial(func, *args, **keywords):
                                                    def newfunc(*fargs, **fkeywords):
                                                        newkeywords = keywords.copy()
                                                        newkeywords.update(fkeywords)
                                                        return func(*(args + fargs), **newkeywords)
                                                    newfunc.func = func
                                                    newfunc.args = args
                                                    newfunc.keywords = keywords
                                                    return newfunc
                                                复制代码
                                                　　使用 partial 对象创建一个 base 参数始终为 2 的 int()

                                                复制代码
                                                from functools import partial

                                                basetwo = partial(int, base=2)
                                                basetwo.__doc__ = 'Convert base 2 string to an int.'
                                                basetwo('10010')
                                                复制代码
                                                　　这个新的 partial 对象 basetwo 能够将二进制的参数转化为十进制的整型结果，在调用这个 partial 对象时只需要传入二进制的目标参数即可。
                                    functools.update_wrapper(wrapper, wrapped[, assigned][, updated]) 

                                                　　更新一个包裹（wrapper）函数，使其看起来更像被包裹(wrapped)的函数。

                                                　　可选的参数指定了被包裹函数的哪些属性直接赋值给包裹函数的对应属性，同时包裹函数的哪些属性要更新而不是直接接受被包裹函数的对应属性。
                                                参数 assigned 的默认值对应于模块级常量 WRAPPER_ASSIGNMENTS (默认地将被包裹函数的 __name__, __module__ 和 __doc__ 属性赋给包裹函数)，
                                                 参数 updatedd  的默认值对应于模块级常量 WRAPPER_UPDATES (默认更新 wrapper 函数的 __dict__ 属性)。

                                                　　这个函数的主要用途是在一个装饰器中，原函数会被装饰（包裹），装饰器函数会返回一个 wrapper 函数，如果装饰器返回的这个 wrapper 函数没
                                                有被更新，那么它的一些元数据更多的是反映 wrapper 函数定义时的特征，无法反映 wrapped 函数的特性。
                                    functools.wraps(wrapped[, assigned][, updated]) 

                                                　　这个函数可以用作一个装饰器，简化调用上一个函数 update_wrapper 的过程。调用这个函数等价于调用  
                                                partial(update_wrapper, wrapped=wrapped, assigned=assigned, updated=updated)  。

                                                　　例如：

                                                复制代码
                                                >>> from functools import wraps
                                                >>> def my_decorator(f):
                                                ...     @wraps(f)
                                                ...     def wrapper(*args, **kwds):
                                                ...         print 'Calling decorated function'
                                                ...         return f(*args, **kwds)
                                                ...     return wrapper
                                                ...
                                                >>> @my_decorator
                                                ... def example():
                                                ...     """Docstring"""
                                                ...     print 'Called example function'
                                                ...
                                                >>> example()
                                                Calling decorated function
                                                Called example function
                                                >>> example.__name__
                                                'example'
                                                >>> example.__doc__
                                                'Docstring'
                                                复制代码
                                                　　可以看到最终调用的 example() 函数是经过 @my_decorator 装饰的，装饰器的作用是接受一个被包裹函数作为参数，对其进行加工，返回
                                                一个包裹函数。代码使用 @functools.wraps 装饰将要返回的包裹函数 wrapper，使得他的 __name__, __doc__ 和 __module__ 属性与被装饰
                                                函数 examle()完全相同， 这样虽然最终调用的是经过装饰的 example() 函数，但是某些属性还是得到了维护。

                                                　　如果在 @my_decorator 的定义中不使用 @functools.wraps 装饰包裹函数，那么最终 example.__name__ 将会变为 ‘wrapper’， 而 
                                                example.__doc__ 也会丢失。
                        二、partial对象

                                    　　partial对象是调用partial()时创建的可调用对象，他们有三个只读的属性：

                                     

                                    1.  partial.func 

                                    　　可调用或函数，调用partial对象时，会结合新的参数和关键字最终调用func。

                                     

                                    2.  partial.args 

                                    　　默认为最左的位置参数，这些参数会被自动添加到所有调用partial对象时传入的参数前。也就是说在调用partial对象时不用传入这些参数即可，
                                    他们视为恒定的，从而自动添加到func的调用中。

                                     

                                    3.  partial.keywords 

                                    　　当调用partial对象时提供的关键字参数。

                                     

                                    　　partial对象在一些方面类似于函数对象：可调用，弱引用，可以拥有属性。但是也有一些关键的区别：

                                    　　1.partial对象的 __name__ 和 __doc__ 属性不会自动创建；

                                    　　2. 在类里定义的partial对象使用时更像静态方法，在实例的属性查询过程中不会转变成绑定方法（bound methods, 通过类的实例对象进行属性引用）。
第三方模块() --基本上，所有的第三方模块都会在PyPI - the Python Package Index上注册，只要找到对应的模块名字，即可用pip安装
    PIL--Python Imaging Library--提供了操作图像的强大功能，可以通过简单的代码完成复杂的图像处理
                        PIL：Python Imaging Library，已经是Python平台事实上的图像处理标准库了。PIL功能非常强大，但API却非常简单易用

                                    由于PIL仅支持到Python 2.7，加上年久失修，于是一群志愿者在PIL的基础上创建了兼容的版本，名字叫Pillow，支持最新
                                    Python 3.x，又加入了许多新特性，因此，我们可以直接安装使用Pillow。                                  
                        安装Pillow
                                    在命令行下直接通过pip安装：                                 

                                    $ pip install pillow
                                    如果遇到Permission denied安装失败，请加上sudo重试。                                    
                        操作图像
                                    来看看最常见的图像缩放操作，只需三四行代码：                                  

                                    from PIL import Image                                   

                                    # 打开一个jpg图像文件，注意是当前路径:
                                    im = Image.open('test.jpg')
                                    # 获得图像尺寸:
                                    w, h = im.size
                                    print('Original image size: %sx%s' % (w, h))
                                    # 缩放到50%:
                                    im.thumbnail((w//2, h//2))
                                    print('Resize image to: %sx%s' % (w//2, h//2))
                                    # 把缩放后的图像用jpeg格式保存:
                                    im.save('thumbnail.jpg', 'jpeg')
                                    其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。                                    

                                    比如，模糊效果也只需几行代码：                                 

                                    from PIL import Image, ImageFilter                                  

                                    # 打开一个jpg图像文件，注意是当前路径:
                                    im = Image.open('test.jpg')
                                    # 应用模糊滤镜:
                                    im2 = im.filter(ImageFilter.BLUR)
                                    im2.save('blur.jpg', 'jpeg')
                        效果如下

                                    PIL-blur                                    
                        PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片

                                    from PIL import Image, ImageDraw, ImageFont, ImageFilter                                    

                                    import random                                   

                                    # 随机字母:
                                    def rndChar():
                                        return chr(random.randint(65, 90))                                  

                                    # 随机颜色1:
                                    def rndColor():
                                        return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))                                  

                                    # 随机颜色2:
                                    def rndColor2():
                                        return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))                                  

                                    # 240 x 60:
                                    width = 60 * 4
                                    height = 60
                                    image = Image.new('RGB', (width, height), (255, 255, 255))
                                    # 创建Font对象:
                                    font = ImageFont.truetype('C://windows//Fonts//Arial.ttf', 36)
                                    # 创建Draw对象:
                                    draw = ImageDraw.Draw(image)
                                    # 填充每个像素:
                                    for x in range(width):
                                        for y in range(height):
                                            draw.point((x, y), fill=rndColor())
                                    # 输出文字:
                                    for t in range(4):
                                        draw.text((60 * t + 10, 10), rndChar(), font=font, fill=rndColor2())
                                    # 模糊:
                                    image = image.filter(ImageFilter.BLUR)
                                    image.save('code.jpg', 'jpeg')
                                    我们用随机颜色填充背景，再画上文字，最后对图像进行模糊，得到验证码图片如下：                                  
                        验证码 

                                    如果运行的时候报错：                                  

                                    IOError: cannot open resource
                                    这是因为PIL无法定位到字体文件的位置，可以根据操作系统提供绝对路径，比如：                                  

                                    '/Library/Fonts/Arial.ttf'
                                    要详细了解PIL的强大功能，请请参考Pillow官方文档：                                   

                                    https://pillow.readthedocs.org/                                 
                        小结

                                    PIL提供了操作图像的强大功能，可以通过简单的代码完成复杂的图像处理。                                 
                        参考源码

                                    https://github.com/michaelliao/learn-python3/blob/master/samples/packages/pil/use_pil_resize.py                                 

                                    https://github.com/michaelliao/learn-python3/blob/master/samples/packages/pil/use_pil_blur.py                                   

                                    https://github.com/michaelliao/learn-python3/blob/master/samples/packages/pil/use_pil_draw.py 