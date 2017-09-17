
class 进制:
    二进制
    八进制
    十进制
    十六进制
class 字符编码:
	码(code)--编码(encode)—解码(decode)--比特(位,bit)--字节(byte)--字符(character):
        码(code)： 

         是用另一个字、词、数字或标志来'置换'一个字、词或短语，达到隐藏原来的词或短语的目的()，它主要起到置换的作用
        编码(encode)：

         编码是信息从一种'形式或格式转换'为另一种形式的过程。用预先规定的方法将文字、数字或其他对象编成数码，或将信息、数据转换成规定的电脉冲信号
            ASCII编码()--GB2312编码()--Unicode编码(通常两个字节)--UTF8编码(可变长编码,UTF-8)
                字母A用ASCII编码是十进制的65，二进制的01000001；
                字符0用ASCII编码是十进制的48，二进制的00110000。
                把ASCII编码的A用Unicode编码，只需要在前面补8个0就可以

                以Unicode表示的str通过encode()方法可以编码为指定的bytes
                 >>> 'ABC'.encode('ascii')
                 b'ABC'
                 >>> '中文'.encode('utf-8')
                 b'\xe4\xb8\xad\xe6\x96\x87'
                 >>> '中文'.encode('ascii')
                 Traceback (most recent call last):
                   File "<stdin>", line 1, in <module>
                 UnicodeEncodeError: 'ascii' codec cannot encode characters in position 0-1: ordinal not in range(128)
                 纯英文的str可以用ASCII编码为bytes，内容是一样的，含有中文的str可以用UTF-8编码为bytes。
                 '含有中文的str无法用ASCII编码'，因为中文编码的范围超过了ASCII编码的范围，Python会报错

                '在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，就转换为UTF-8编码。'
        解码(decode)：

         解码，是'编码的逆过程'。用特定方法把数码还原成它所代表的内容或将电脉冲信号、光信号、无线电波等转换成它所代表的信息、数据等的过程。
            ASCII解码()--GB2312解码()--Unicode解码(通常两个字节)--UTF8解码(可变长编码,UTF-8)
             如果我们从网络或磁盘上读取了字节流，那么读到的数据就是bytes。要把bytes变为str，就需要用decode()方法：
             >>> b'ABC'.decode('ascii')
             'ABC'
             >>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
             '中文'
             要计算str包含多少个字符，可以用len()函数：
             >>> len('ABC')
             3
             >>> len('中文')
             2
             len()函数计算的是str的字符数，如果换成bytes，len()函数就计算字节数：
             >>> len(b'ABC')
             3
             >>> len(b'\xe4\xb8\xad\xe6\x96\x87')
             6
             >>> len('中文'.encode('utf-8'))
             6
             可见，1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节。
             在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。
        比特(位,bit)：
         
         bit是Binary digit（二进制数）位的缩写，二进制数系统中，每个0或1就是一个位(bit)，'位是数据存储的最小单位，信息量的度量单位，信息量的最小单位'。
        字节(byte)：

         8个比特（bit）为一个字节（byte）
            Python对bytes类型的数据用带b前缀的单引号或双引号表示：
            x = b'ABC'
            要注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节。
        字符(character)：

         一个字符对应若干个字节
        字符和码的相互转化()：对于单个字符的编码，Python提供了 ord()函数获取字符的十进制整数表示，chr()函数把十进制整数编码转换为对应的字符
            >>> ord('A')
            65
            >>> ord('中')
            20013
            >>> chr(66)
            'B'
            >>> chr(25991)
            '文'
    注意 
    乱码问题()
     在操作字符串时，我们经常遇到str和bytes的互相转换。为了避免乱码问题，应当始终坚持使用UTF-8编码对str和bytes进行转换。
     由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。
     当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：
     #!/usr/bin/env python3
     # -*- coding: utf-8 -*-
     第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
     第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
     申明了UTF-8编码并不意味着你的.py文件就是UTF-8编码的，必须并且要确保文本编辑器正在使用UTF-8 without BOM编码
    格式化的字符串输出(用%实现):
     常见的占位符有:
       %d 整数
       %f	浮点数
       %s	字符串
       %x	十六进制整数
     例：
      >>> 'Hello, %s' % 'world'
      'Hello, world'
      >>> 'Hi, %s, you have $%d.' % ('Michael', 1000000)
      'Hi, Michael, you have $1000000.'
      你可能猜到了，%运算符就是用来格式化字符串的。在字符串内部，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，
      后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
     格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
       >>> '%2d-%02d' % (3, 1)
       ' 3-01'
       >>> '%.2f' % 3.1415926
       '3.14'
     如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
       >>> 'Age: %s. Gender: %s' % (25, True)
       'Age: 25. Gender: True'
     %转义，用%%来表示一个%：
       >>> 'growth rate: %d %%' % 7
       'growth rate: 7 %'
class 输入与输出(input(‘hint’/‘file path’,‘how do’),print(data)):
	输出
     用print()在括号中加上字符串，就可以向屏幕上输出指定的文字。比如输出'hello, world':
           >>> print('hello, world')
           hello, world
     print()函数也可以接受多个字符串，用逗号“,”隔开，遇到逗号“,”会输出一个空格,就可以连成一串输出：
           >>> print('The quick brown fox', 'jumps over', 'the lazy dog')
           The quick brown fox jumps over the lazy dog
     print()也可以打印整数，或者计算结果：
           >>> print(300)
           300
           >>> print(100 + 200)
           300
           因此，我们可以把计算100 + 200的结果打印得更漂亮一点：
           >>> print('100 + 200 =', 100 + 200)
           100 + 200 = 300
           注意，对于100 + 200，Python解释器自动计算出结果300，但是，'100 + 200 ='是字符串而非数学公式，Python把它视为字符串，
           请自行解释上述打印结果。
    输入
     >>> name = input()
     Michael
     >>>
     当你输入name = input()并按下回车后，Python交互式命令行就在等待你的输入了。这时，你可以输入任意字符，然后按回车后完成输入。
     输入完成后，不会有任何提示，Python交互式命令行又回到>>>状态了。那我们刚才输入的内容到哪去了？答案是存放到name变量里了。可以
     直接输入name查看变量内容：
     >>> name
     'Michael'
     但是程序运行的时候，没有任何提示信息告诉用户：“嘿，赶紧输入你的名字”，这样显得很不友好。幸好，input()可以让你显示一个字符串来提示
     用户，于是我们把代码改成：
     name = input('please enter your name: ')
     print('hello,', name)
     再次运行这个程序，你会发现，程序一运行，会首先打印出please enter your name:，这样，用户就可以根据提示，输入名字后，得到hello, xxx
     的输出
class 变量:
	变量表示
	 在计算机程序中，变量可以是'任意数据类型'
	 变量在程序中就是用一个变量名表示，变量名必须是大小写英文、数字和_的组合，且不能用数字开头
	 同一个变量可以反复赋值，而且可以是不同类型的变量
	变量赋值
	 用等号"="赋值
	 把等号右边的'data'赋值给等号左边的变量，data可以是任何数据（包括变量）
	变量在python中的理解
     当我们写：
     a = 'ABC'
     时，Python解释器干了两件事情：
     1.	在内存中创建了一个'ABC'的字符串；
     2.	在内存中创建了一个名为a的变量，并把它指向'ABC'

     把一个变量a赋值给另一个变量b，这个操作实际上是把变量b指向变量a所指向的数据，例如下面的代码：
      a = 'ABC'
      b = a
      a = 'XYZ'
      print(b)
      最后一行打印出变量b的内容到底是'ABC'呢还是'XYZ'？如果从数学意义上理解，就会错误地得出b和a相同，也应该是'XYZ'，但实际上b的值是'ABC'，让我们一行一行地执行代码，就可以看到到底发生了什么事：
      执行a = 'ABC'，解释器创建了字符串'ABC'和变量a，并把a指向'ABC'：      
      执行b = a，解释器创建了变量b，并把b指向a指向的字符串'ABC'：      
      执行a = 'XYZ'，解释器创建了字符串'XYZ'，并把a的指向改为'XYZ'，但b并没有更改：      
      所以，最后打印变量b的结果自然是'ABC'了。

    动态语言
	 变量本身类型不固定的语言称之为动态语言，和静态语言相比，动态语言更灵活，与之对应的是静态语言。
	 静态语言在定义变量时必须指定变量类型，如果赋值的时候类型不匹配，就会报错。
class 常量：
    常量就是不能变的变量，比如常用的数学常数π就是一个常量。在Python中，通常用全部大写的变量名表示常量：
    PI = 3.14159265359
    但事实上PI仍然是一个变量，Python根本没有任何机制保证PI不会被改变，所以，'用全部大写的变量名表示常量只是一个习惯上的用法'
    如果你一定要改变变量PI的值，也没人能拦住你。
class 条件判断:
	If…(elif…elif)…(else)… 语句
        if语句，'从上往下判断'，如果在某个判断上是True，把该判断对应的缩进语句执行后，就忽略掉剩下的elif和else；
        如果所有的if和elif条件都不成立，则最后执行else语句
            if <条件判断1>:
                <执行1>
            elif <条件判断2>:
                <执行2>
            elif <条件判断3>:
                <执行3>
            else:
                <执行4>

        if判断条件还可以简写，比如写：
            if x:
                print('True')
            '只要x是非零数值、非空字符串、非空list等'，就判断为True，否则为False
    Try…(except…except)...(else)…(finally) 语句 
        Try用来运行try内部的代码，如果执行出错，则try内部后续代码不会继续执行，而是直接跳转至错误处理代码，即except语句块，执行完
        except后，如果有finally语句块，则执行finally语句块，至此，执行完毕。
        如果没有错误发生，可以在except语句块后面加一个else，当没有错误发生时，会自动执行else语句
        使用try...except捕获错误还有一个巨大的好处，就是可以跨越多层调用
        try:
            print('try...')
            r = 10 / int('2')
            print('result:', r)
        except ValueError as e:
            print('ValueError:', e)
        except ZeroDivisionError as e:
            print('ZeroDivisionError:', e)
        else:
            print('no error!')
        finally:
            print('finally...')
        print('END')
class 循环:
	for...in 循环
        for x in ...循环就是把list或tuple的中每个元素代入变量x，然后执行缩进块的语句
            看例子：
                names = ['Michael', 'Bob', 'Tracy']
                for name in names:
                    print(name)
                执行这段代码，会依次打印names的每一个元素：
                Michael
                Bob
                Tracy
    while 循环
        只要条件满足，就不断循环，条件不满足时退出循环（条件语句参看'条件判断'部分）
            例：
                sum = 0
                n = 99                
                while n > 0:
                    sum = sum + n
                    n = n - 2
                print(sum)
    死循环(条件永远为 True 时，出现死循环)

    break 语句(执行缩进语句块时，遇到 break 则提前结束并退出循环)
        例：
            n = 1
            while n <= 100:
                if n > 10: # 当n = 11时，条件满足，执行break语句
                    break # break语句会结束当前循环
                print(n)
    continue 语句(执行缩进语句块时，遇到 continue 则结束本轮循环，直接开始下一轮循环)
        例：
            n = 0
            while n < 10:
                n = n + 1
                print(n)
            上面的程序可以打印出1～10。但是，如果我们想只打印奇数，可以用continue语句跳过某些循环：
            n = 0
            while n < 10:
                n = n + 1
                if n % 2 == 0: # 如果n是偶数，执行continue语句
                    continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
                print(n)
            执行上面的代码可以看到，打印的不再是1～10，而是1，3，5，7，9
class 上下文管理(with ... [as ...])：
    基本概念
     上下文管理协议(Context Management Protocol)
         包含方法 __enter__() 和 __exit__()，
         支持该协议的对象要实现这两个方法。
     上下文管理器(Context Manager)
         支持上下文管理协议的对象，这种对象实现了__enter__() 和 __exit__() 方法。上下文管理器定义执行 with 语句时要建立的'运行时上下文'，
         负责执行 with 语句块上下文中的进入与退出操作。通常使用 with 语句调用上下文管理器，也可以通过直接调用其方法来使用。
     运行时上下文(runtime context)
         由上下文管理器创建，通过上下文管理器的 __enter__() 和__exit__() 方法实现，__enter__() 方法在语句体执行之前进入运行时上下文，
         __exit__() 在语句体执行完后从运行时上下文退出。with 语句支持运行时上下文这一概念。
     上下文表达式(Context Expression) 

         with 语句中跟在关键字 with 之后的表达式，该表达式要返回一个'上下文管理器对象'。
     语句体(with-body)
         with 语句包裹起来的代码块，在执行语句体之前会调用上下文管理器的 __enter__() 方法，
         执行完语句体之后会执行 __exit__() 方法。    
    基本语法
        语法格式
        with context_expression [as target(s)]:
            with-body
        这里 context_expression 要返回一个上下文管理器对象，该对象并不赋值给 as 子句中的 target(s) ，如果指定了 as 子句的话，
        会将上下文管理器的 __enter__() 方法的返回值赋值给 target(s)。target(s) 可以是单个变量，或者由“()”括起来的元组（不能
        是仅仅由“,”分隔的变量列表，必须加“()”）。
    
    应用
        with 语句适用于对资源进行访问的场合，确保不管使用过程中是否发生异常都会执行必要的“清理”操作，释放资源，比如文件使用后自动
        关闭、线程中锁的自动获取和释放等。
    例：
        使用 with 语句操作文件对象，不管在处理文件过程中是否发生异常，都保证 with 语句执行完毕后已经关闭了打开的文件句柄
            with open(r'somefileName') as somefile:
                for line in somefile:
                    print line
                    # ...more code        
        如果使用传统的 try/finally 范式操作文件对象，则要使用类似如下代码：
            somefile = open(r'somefileName')
            try:
                for line in somefile:
                    print line
                    # ...more code
            finally:
                somefile.close()
        比较起来，使用 with 语句可以减少编码量。已经加入对上下文管理协议支持的还有模块 threading、decimal 等。
    工作原理
        PEP 0343 对 with 语句的实现进行了描述。with 语句的执行过程类似如下代码块：
        清单 4. with 语句执行过程
            context_manager = context_expression
            exit = type(context_manager).__exit__  
            value = type(context_manager).__enter__(context_manager)
            exc = True   # True 表示正常执行，即便有异常也忽略；False 表示重新抛出异常，需要对异常进行处理
            try:
                try:
                    target = value  # 如果使用了 as 子句
                    with-body     # 执行 with-body
                except:
                    # 执行过程中有异常发生
                    exc = False
                    # 如果 __exit__ 返回 True，则异常被忽略；如果返回 False，则重新抛出异常
                    # 由外层代码对异常进行处理
                    if not exit(context_manager, *sys.exc_info()):
                        raise
            finally:
                # 正常退出，或者通过 statement-body 中的 break/continue/return 语句退出
                # 或者忽略异常退出
                if exc:
                    exit(context_manager, None, None, None) 
                # 缺省返回 None，None 在布尔上下文中看做是 False
        执行 context_expression，生成上下文管理器 context_manager
        调用上下文管理器的 __enter__() 方法；如果使用了 as 子句，则将 __enter__() 方法的返回值赋值给 as 子句中的 target(s)
        执行语句体 with-body
        不管是否执行过程中是否发生了异常，执行上下文管理器的 __exit__() 方法，__exit__() 方法负责执行“清理”工作，如释放资源等。如果执行过程中没有出现异常，或者语句体中执行了语句 break/continue/return，则以 None 作为参数调用 __exit__(None, None, None) ；如果执行过程中出现异常，则使用 sys.exc_info 得到的异常信息为参数调用 __exit__(exc_type, exc_value, exc_traceback)
        出现异常时，如果 __exit__(type, value, traceback) 返回 False，则会重新抛出异常，让with 之外的语句逻辑来处理异常，这也是通用做法；如果返回 True，则忽略异常，不再对异常进行处理
class 命名空间：
            Python 的命名空间--命名空间 标识符 python 全局变量

                        栗子
                                    a 文件中有变量 va 以及类 A，b 文件导入 a 中class A ，并打印出 A：

                                                #a.py
                                                va = ['dobi', 'a', 'dog']

                                                print('a1', id(va))

                                                class A():
                                                    def __init__(self):
                                                        pass

                                                    def rtn(self):
                                                        global va
                                                        va.insert(1,'is')
                                                        print('a3', id(va))
                                                        return va

                                                print('a2', va)


                                                #b.py
                                                from a import A

                                                print('b', A)
                                    执行 b 文件的结果为：

                                                Reloaded modules: a
                                                a1 2407907960200
                                                a2 ['dobi', 'a', 'dog']
                                                b <class 'a.A'>
                                    可以发现，虽然 b 只是导入了 a 中的 class A,但导入这个过程却执行了整个 a 文件，那么我们是否能够在 b 中访问 a 中的全局变量 va 呢：

                                                print(va)
                                                # NameError: name 'va' is not defined
                                                print(a.va)
                                                # NameError: name 'a' is not defined
                                                print(b.va)
                                                # NameError: name 'b' is not defined
                                                尝试了各类调用方法，发现都无法正常访问 a 的全局变量 va，既然 b 的导入执行了整个 a 文件，甚至还打印出了 va 的 id 和值，又为什么无法在 
                                                b 中调用 va 呢？

                                    这个问题所涉及到的内容就是：命名空间。

                        但在开始正题之前，我们需要阐明若干概念：

                        一些基本概念的澄清
                                    对象
                                                Python 一切皆对象，每个对象都具有 一个ID、一个类型、一个值；对象一旦建立，ID 便不会改变，可以直观的认为 ID 就是对象在内存中的地址：

                                                a = [1, 2]
                                                b = a
                                                id(a)
                                                # 2407907978632
                                                id(b)
                                                # 2407907978632
                                                b[1] = 3
                                                a
                                                # [1, 3]
                                                上例 a, b 共享了同一个 ID、同一个值、同一个类型。因此 a, b 表达的是同一个对象，但 a, b 又明显是不同的，比如一个叫 'a' 一个叫 'b'...既然是同一个对象，为什么又有不同的名字呢？难道名字不是对象的属性？

                                    标识符
                                                事实确实如此，这是 Python 比较特殊一点：如同'a' 'b' 这样的名称其实有一个共同的名字：identifier（注意不要与 ID 混淆了），中文名为
                                                “标识符”，来解释一下：

                                                标识符：各类对象的名称，比如函数名、方法名、类名，变量名、常量名等。

                                                在 Python 中赋值并不会直接复制数据，而只是将名称绑定到对象，对象本身是不知道也不需要关心（该关心这个的是程序猿）自己叫什么
                                                名字的。一个对象甚至可以指向不同的标识符，上例中的'a' 'b'便是如此。真正管理这些名子的事物就是本文的主角“命名空间”。

                                    命名空间
                                                命名空间（Namespace）：名字（标识符）到对象的映射。

                                                简而言之，命名空间可以理解为：记录对象和对象名字对应关系的空间；现今 Python 的大部分命名空间是通过字典来实现的，也即一个
                                                命名空间就是名字到对象的映射，标识符是键，对象则是值。

                                    作用域
                                                与命名空间相对的一个概念就是“作用域”，那么什么又是作用域呢？

                                                作用域（Scope）：本质是一块文本区域，Python 通过该文本区域可以直接访问相应的命名空间。

                                                这里需要搞清楚什么是直接访问：

                                                #x.py
                                                a = 1
                                                class A():
                                                    def func():pass
                                                python x.py
                                                a   #直接访问
                                                # 1
                                                A.func  #属性访问
                                                Python 中不加 . 的访问为直接访问，反之为属性访问。

                                                因此可以简单的将作用域理解为“直接访问命名空间的一种实现”，具体而言：

                                                作用域内相应的命名空间可以被直接访问；
                                                只有作用域内的命名空间才可以被直接访问（因此并不是所有的命名空间都可以被直接访问）。
                                                看不懂？ 没关系，后面会解释，现在先回到命名空间这个话题上，我们经常接触的命名空间有四类：

                                    LEGB命名空间
                                
                                                这四类命名空间可以简记为 LEGB:

                                                            局部命名空间（local）：指的是一个函数或者一个类所定义的名称空间；包括函数的参数、局部变量、类的属性等。
                                                            闭包命名空间（enclosing function）：闭包函数 的名称空间（Python 3 引入）。
                                                            全局命名空间（global）：读入一个模块（也即一个.py文档）后产生的名称空间。
                                                            内建命名空间（builtin）：Python 解释器启动时自动载入__built__模块后所形成的名称空间；诸如 str/list/dict...等内置对象的名称就处于这里。
                                                为了说清楚这几类命名空间，举个栗子：

                                                            #c.py
                                                            v1 = 'a global var'

                                                            def func(v):
                                                                v2 = 'a local var'
                                                                def inn_func():
                                                                    v3 = v2 + v
                                                                    return v3
                                                                return inn_func
                                                内建命名空间比较好理解，我们重点讲解下其他三个：

                                                            'v1' 为全局变量 v1 的名子，其所处的命名空间为全局命名空间；需要注意的是全局命名空间包括 'func' 但不包括 func 的参数和内部变量。
                                                            func 囊括 'v'、'v2' 和 'inn_func' 名称的空间为局部命名空间；
                                                            执行 func 后，func 的作用域释放（或许遗忘更合适），并返回了绑定了 v 和 v2 变量的闭包函数 inn_func，此时闭包所具有命名空间即为
                                                            闭包命名空间，因此局部命名空间和闭包命名空间是相对而言的，对于父函数 func 而言，两者具有产生时间上的差异。
                                    LEGB 访问规则
                                                通过上面描述，我们发现 LEGB 四类命名空间本身具有明显的内外层级概念，而这种层级概念正是构建作用域的前提：作用域依据这种
                                                层级概念将不同类型的命名空间组织起来并划归到不同层级的作用域，然后定义好不同层级作用域之间的访问规则，从而实现命名空间的直接访问：
                                                LEGB 访问规则： 同样的标识符在各层命名空间中可以被重复使用而不会发生冲突，但 Python 寻找一个标识符的过程总是从当前层开始
                                                逐层往上找，直到首次找到这个标识符为止：

                                                #d.py
                                                v1 = 1
                                                v2 = 3
                                                def f():
                                                    v1 = 2
                                                    print(1, v1)
                                                    print(2, v2)

                                                f()
                                                print(3, v1)
                                                1 2
                                                2 3
                                                3 1
                                                上例中，全局变量和函数 f 都定义了 变量 v1,结果 Python 会优先选择 f 的局部变量 v1 ，对于 f 内并未定义的变量 v2 ，Python 会向上搜寻
                                                全局命名空间，读取全局变量 v2 后打印输出。

                                    global 和 nonlocal 语句
                                                global 和 nonlocal 的作用
                                                            如前所述，对于上层变量，python 允许直接读取，但是却不可以在内层作用域直接改写上层变量，来看一个典型的闭包结构:

                                                            #e.py
                                                            gv = ['a', 'global', 'var']

                                                            def func(v):
                                                                gv = ['gv'] + gv #UnboundLocalError:local variable 'gv' referenced before assignment
                                                                lv = []
                                                                def inn_func():
                                                                    lv = lv + [v]  #UnboundLocalError:local variable 'lv' referenced before assignment
                                                                    gv.insert(1, lv[0])
                                                                    return gv
                                                                return inn_func
                                                            实际调用 func()函数后，上面两处对 gv 和 lv 进行赋值操作的地方都会发生 UnboundLocalError：因为 Python 在执行函数前，会首先生成各层命名空间和作用域，因此 Python 在执行赋值前会将func 内的 'gv' 'lv' 写入局部命名空间和闭包命名空间，当 Python 执行赋值时会在局部作用域、闭包作用域内发现局部命名空间和闭包命名空间内已经具有'gv' 和 'lv' 标识符，但这两个非全局标识符在该赋值语句执行之前并没有被赋值，也即没有对象与标识符关联，因此无法参与四则运算，从而引发错误；但这段程序本意可能只是想让具有对象的全局变量gv 和局部变量 lv 参与运算，为了避免类似的情况发生，Python 便引入了 global、nonlocal 语句就来说明所修饰的 gv、lv 分别来自全局命名空间和局部命名空间，声明之后，就可以在 func 和 inn_func 内直接改写上层命名空间内 gv 和 lv 的值：

                                                            #f.py
                                                            gv = ['a', 'global', 'var']

                                                            def func(v):
                                                                global gv
                                                                gv = ['gv'] + gv
                                                                lv = []
                                                                print(id(lv))
                                                                def inn_func():
                                                                    nonlocal lv
                                                                    lv = lv + [v]
                                                                    print(id(lv))
                                                                    gv.insert(1, lv[0])
                                                                    return gv
                                                                return inn_func
                                                            a = func('is')
                                                            # 2608229974344

                                                            a()
                                                            # 2608229974344
                                                            # ['gv', 'is', 'a', 'global', 'var']

                                                            print(gv)
                                                            # ['gv', 'is', 'a', 'global', 'var']
                                                            如上，全局变量 gv 值被函数改写了， inn_func 修改的也确实是父函数 lv的值 （依据 ID 判断）。

                                    借壳
                                            那么是不是不使用 global 和 nonlocal 就不能达到上面的目的呢？来看看这段程序：

                                            #g.py
                                            gv = ['a', 'global', 'var']

                                            def func(v):
                                                gv.insert(0, 'gv')
                                                lv = []
                                                print(id(lv))
                                                def inn_func():
                                                    lv.append(v)
                                                    print(id(lv))
                                                    gv.insert(1, lv[0])
                                                    return gv
                                                return inn_func
                                            执行的结果：

                                            a = func('is')
                                            # 2608110869168

                                            a()
                                            # 2608110869168
                                            # ['gv', 'is', 'a', 'global', 'var']

                                            print(gv)
                                            # ['gv', 'is', 'a', 'global', 'var']
                                            可以发现，执行结果同上面完全一致，问题自然来了：“为什么不用 global nonlocal 也可以改写全局变量gv和父函数变量lv的值？

                                            为了看清楚这个过程，我们将上面的gv.insert(0, 'gv') lv.append(v) 改写为 gv[0:0] = ['gv'] lv[:] = [v]:

                                            #h.py
                                            gv = ['a', 'global', 'var']

                                            def func(v):
                                                gv[0:0] = ['gv']
                                                lv = []
                                                print(id(lv))
                                                def inn_func():
                                                    lv[:] = [v]
                                                    print(id(lv))
                                                    gv.insert(1, lv[0])
                                                    return gv
                                                return inn_func
                                            执行结果：

                                            a = func('is')
                                            # 2608229959496

                                            a()
                                            # 2608229959496
                                            # ['gv', 'is', 'a', 'global', 'var']
                                            同 g.py 文件的执行结果完全一致，事实上两者之间的内在也是完全一样的。
                                            So 我们其实改写的不是 gv 和 lv ,而是 gv 和 lv 的元素 gv[0:0] 和 lv[:] 。因此，不需要 global 和 nonlocal 修饰就可以直接改写，这就是“借壳”，在 nonlocal 尚未引入 Python 中，比如 Python 2.x 若要在子函数中改写父函数变量的值就得通过这种方法。
                                            当然借壳蕴藏着一个相对复杂的标识符创建的问题：比如子函数通过借壳修改父函数变量lv的值，那么子函数的标识符lv是怎么绑定到父函数变量lv的值 ID 的上的？

                                                            关于这个问题，这里有个问答就是讨论这个的：python的嵌套函数中局部作用域问题?

                                                            global 和 nonlocal 语句对标识符创建的不同影响
                                                            另外，需要注意的是：global 语句只是声明该标识符引用的变量来自于全局变量，但并不能直接在当前层创建该标识符；nonlocal 语句则会在子函数命名空间中创建与父函数变量同名的标识符：

                                                            #j.py
                                                            gv = 'a global var'

                                                            def func():
                                                                global gv
                                                                lv = 'a local var'
                                                                print(locals())
                                                                def inn_func():
                                                                    nonlocal lv
                                                                    global gv
                                                                    print(locals())
                                                                return inn_func
                                                            执行结果：

                                                            c = func()
                                                            {'lv': 'a local var'}   #运行 `func` 函数后，`global` 语句并未将 `gv` 变量引入局部命名空间

                                                            c()
                                                            {'lv': 'a local var'}   #运行闭包函数后，`nonlocal` 语句将父函数变量 `lv` 引入闭包命名空间
                                                            之所以 nonlocal 语句与 global 语句的处置不同，在于全局变量的作用域生存期很长，在模块内随时都可以访问，而父函数的局部作用域在父函数执行完毕后便会直接释放，因此 nonlocal 语句必须将父函数变量的标识符和引用写入闭包命名空间。

                                    命名空间的生命周期
                                                创建规则
                                                            实际上，到这里其实还有一个重要的重要问题没有解决：“标识符并不是天生就在命名空间内的，命名空间也不是平白无故就产生的，
                                                            那么命名空间是在什么时候被创建？又是在什么时候被删除的呢？”规则有四：

                                                            内建命名空间在 Python 解释器启动时创建，之后会一直存在；
                                                            模块的全局命名空间在模块定义被读入时创建，通常模块命名空间也会保持到解释器退出。
                                                            函数调用时产生新的局部命名空间；函数返回结果、抛出异常时释放命名空间，每一次递归都生成一个命名空间。
                                                            标识符产生地点决定标识符所处的命名空间。
                                                            这四点就是拿来秒懂的！不过，仍然有一点常常被忽视：类的命名空间：

                                                            类的局部命名空间
                                                            首先，函数和类执行时都会产生局部命名空间，但类的执行机制不同于函数：

                                                            #i.py
                                                            def a():
                                                                print('function')

                                                            class A():
                                                                print(1)
                                                                class B():
                                                                    print(2)
                                                                    class C():
                                                                        print(3)
                                                            执行文件，结果为：

                                                            1
                                                            2
                                                            3
                                                            如上，类就是一个可执行的代码块，只要该类被加载，就会被执行，这一点不同于函数。类之所以这么设计的原因在于：类是创建其
                                                            他实例（生成其他的类或者具体的对象）的对象，因此必须在实例之前被创建，而类又可能涉及到与其他类的继承、重载等一系列问
                                                            题，故在代码加载时就被创建利于提高效率和降低逻辑复杂度。

                                                            其次，与函数不同的是，类的局部命名空间并非作用域

                                                            class A():
                                                                a = 1
                                                                b = [a + i for i in range(3)]  #NameError: name 'a' is not defined
                                                            执行上段代码，我们可以发现在类 A 内列表推导式无法调取 a 的值，但函数却可以：

                                                            def func():
                                                                a = 1
                                                                b = [a + i for i in range(3)]
                                                                print(b)

                                                            func()  #[1, 2, 3]
                                                            因此，A 中的 a 不同于函数 func 中的 a 在局部命名空间中可以被任意读取，之所以说是“不可以被任意”读取而不是“不可被读取”
                                                            ，原因在于在类A 的局部空间内，a 其实一定程度上是可以直接被读取的：

                                                            class A():
                                                                a = 1
                                                                c = a + 2
                                                            执行上段代码后：

                                                            A.c 
                                                            #3
                                                            而上例中 b 的赋值操作不能执行，原因在于列表推导式会创建自己的局部命名空间，因此难以访问到 a。

                                    编译与局部命名空间
                                                Python 是动态语言，很多行为是动态发生的，但 Python 自身也在不断进步，比如为了提高效率，有些行为会在编译时候完成，局部变量的
                                                创建就是如此：

                                                def func():
                                                    a = 1
                                                    def inn_func():
                                                        print(a)  # error
                                                        a = 2     # error
                                                    inn_func()
                                                上段程序还未执行，就提示存在有语法错误，原因在于python 解释器发现 inn_func 内存在自身的 a 变量，但却在声明之前就被 print 了。

                        总结
                                啰嗦了这么多，终于该结尾了！
                                我们再来回过头来看下文章开头的栗子：
                                1、为什么 b.py 只是导入 a.py 中的 class A,却执行了整个 a.py 文件?
                                答：因为 Python 并不知道 class A 在 a.py 文档的何处，为了能够找到 class A，Python 需要执行整个文档。
                                2、为什么 b.py 的导入执行了整个 a.py 文档，却在 b 中难以调用 a 的全局变量 va？
                                答：Python 的全局变量指的是模块全局，因此不可以跨文档，因此 global 语句也是不可以跨文档的。另外， b 只是导入了 a 的 class A，因此并不会导入 a 中所有的标识符，所以 类似a.va 这样的调用也是不起作用的。

                                关于命名空间：
                                1、赋值、定义类和函数都会产生新的标识符；
                                2、全局变量的标识符不能跨文档；
                                3、各级命名空间相互独立互不影响；
                                4、Python 总是从当前层逐渐向上寻找标识符；
                                5、内层作用域若想直接修改上层变量，需要通过 global nonlocal 语句先声明；
                                6、单纯的 global 语句并不能为所在层级创建相应标识符，但 nonlocal 语句可以在闭包空间中创建相应标识符；
                                7、类的局部命名空间不是作用域。 