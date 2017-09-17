几个概念()
    '面向过程的程序设计'    
        函数是Python内建支持的一种封装，我们通过把大段代码拆成函数，通过一层一层的函数调用，就可以把复杂任务分解成简单的任务，
        这种分解可以称之为'面向过程的程序设计'。

        '函数'就是面向过程的程序设计的'基本单元'。
    函数式编程(Functional Programming)
        ——请注意多了一个“式”字，虽然也可以归结到面向过程的程序设计，但其思想更接近数学计算。
        函数式编程就是一种'抽象程度很高'的编程范式
        '纯粹的函数式编程语言'编写的函数'没有变量'，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之
        为'没有副作用'。
        而'允许使用变量'的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是'有副作用'的。
        函数式编程的一个'特点'就是，'允许把函数本身作为参数传入另一个函数，还允许返回一个函数'！
    计算机(Computer)和计算(Compute)    
        在计算机的层次上，CPU执行的是加减乘除的指令代码，以及各种条件判断和跳转指令，所以，汇编语言是最贴近计算机的语言。

        而计算则指数学意义上的计算，越是抽象的计算，离计算机硬件越远。
    对应到编程语言()
        就是越低级的语言，越贴近计算机，抽象程度低，执行效率高，比如C语言；
        
        越高级的语言，越贴近计算，抽象程度高，执行效率低，比如Lisp语言。
高阶函数(Higher-order function)
    定义
        一个函数就可以接收另一个函数作为参数，这种函数就称之为'高阶函数'。
        '变量可以指向函数'--即函数本身也可以赋值给变量
        '函数名也是变量'
        '函数的参数能接收变量'--变量可以指向函数。
        把函数作为结果值返回--返回函数
    类型
返回函数()
    函数作为返回值
    高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
    例    
        我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：
            def calc_sum(*args):  # 该函数返回值为 ax, ax是一个计算结果
                ax = 0	
                for n in args:
                    ax = ax + n
                return ax
        但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数：
            def lazy_sum(*args): # 该函数返回值为 sum，sum是一个函数
                def sum(): 
                    ax = 0
                    for n in args:
                        ax = ax + n
                    return ax
                return sum
            当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
            >>> f = lazy_sum(1, 3, 5, 7, 9)
            >>> f
            <function lazy_sum.<locals>.sum at 0x101c6ed90>
        调用函数f时，才真正计算求和的结果：
            >>> f()
            25
        闭包(closure)    
            在这个例子中，我们在函数lazy_sum中又定义了函数 sum，并且，内部函数 sum 可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum
            返回函数 sum 时，相关参数和变量都保存在返回的函数中，这种称为"闭包（Closure）"的程序结构拥有极大的威力。   
            注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，
            闭包用起来简单，实现起来可不容易         
    闭包例子：
            def count():
                fs = []
                for i in range(1, 4):
                    def f():
                         return i*i
                    fs.append(f)
                return fs            

            f1, f2, f3 = count()
            在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。
            你可能认为调用 f1()，f2()和 f3()结果应该是 1，4，9，但实际结果是：
            >>> f1()
            9
            >>> f2()
            9
            >>> f3()
            9
            全部都是9！原因就在于'返回的函数引用了变量i，但它并非立刻执行'。等到3个函数都返回时，它们所引用的变量i已经变成了3，
            因此最终结果为9。
            '返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。'
            如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，
            已绑定到函数参数的值不变：
            def count():
                def f(j):
                    def g():
                        return j*j
                    return g
                fs = []
                for i in range(1, 4):
                    fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
                return fs
            再看看结果：
            >>> f1, f2, f3 = count()
            >>> f1()
            1
            >>> f2()
            4
            >>> f3()
            9
            缺点是代码较长，可利用lambda函数缩短代码。
    小结
        一个函数可以返回一个计算结果，也可以返回一个函数。
        返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。

        请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：
            >>> f1 = lazy_sum(1, 3, 5, 7, 9)
            >>> f2 = lazy_sum(1, 3, 5, 7, 9)
            >>> f1==f2
            False
            f1()和f2()的调用结果互不影响。
匿名函数(lambda)
    定义   

       当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。            
    例  
        还是以map()函数为例，计算f(x)=x2时，除了定义一个 f(x)的函数外，还可以直接传入匿名函数：
        >>> list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
        [1, 4, 9, 16, 25, 36, 49, 64, 81]
        通过对比可以看出，匿名函数 lambda x: x * x实际上就是：
        def f(x):
            return x * x
    表示 
        lambda 参数 ：表达式
        关键字 lambda 表示匿名函数，冒号前表示函数参数, 冒号后面为表达式。# 需要给参数赋值
    用法      
函数装饰器(decorator)
    定义
        其实就是一个以函数为参数的函数。只不过用了一种比较优雅的方式 @
        函数装饰器是一个函数，接受被装饰的函数作为参数，返回一个新的函数，其中的逻辑你可以随便加进去
        调用函数，先执行装饰器的函数（装饰器内部可以调用被装饰的函数），再执行被装饰的函数
        这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
        本质上，decorator就是一个返回函数的高阶函数
        @a_d
        def f:
        pass 

        等价于
        def f:
        pass 
        f = a_d(f) 
    例    
        由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。
        >>> def now():
        ...     print('2015-3-25')
        ...
        >>> f = now
        >>> f()
        2015-3-25
        函数对象有一个__name__属性，可以拿到函数的名字：
        >>> now.__name__
        'now'
        >>> f.__name__
        'now'
        
        假设我们要增强 now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改 now()函数的定义，可以定义如下：
        def log(func):
            def wrapper(*args, **kw):
                print('call %s():' % func.__name__)
                return func(*args, **kw) # 调用原始函数（被装饰的函数）
            return wrapper
        观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：
        @log  # @log 等价于 now = log(now)
        def now():
            print('2015-3-25')
        调用 now()函数，先执行装饰器的函数（装饰器内部可以调用函数），再执行被装饰的函数：
        >>> now() # 先执行@log函数，再执行now函数
        call now():
        2015-3-25
        把@log放到 now()函数的定义处，相当于执行了语句：
        now = log(now)

        由于 log()是一个decorator，返回一个函数，所以，原来的 now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用 now()将执行新函数，
        即在 log()函数中返回 wrapper()函数。
        wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，'再紧接着调用原始函数'。
    装饰器本身传入参数    
        如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：
        def log(text):
            def decorator(func):
                def wrapper(*args, **kw):
                    print('%s %s():' % (text, func.__name__))
                    return func(*args, **kw)
                return wrapper
            return decorator
        这个3层嵌套的decorator用法如下：
        @log('execute')
        def now():
            print('2015-3-25')
        执行结果如下：
        >>> now()
        execute now():
        2015-3-25
        和两层嵌套的decorator相比，3层嵌套的效果是这样的：
        >>> now = log('execute')(now)
        我们来剖析上面的语句，首先执行 log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
        以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，
        它们的__name__已经从原来的'now'变成了'wrapper'：
        >>> now.__name__
        'wrapper'
    @functools.wraps(func) 完整的装饰器写法   
        因为返回的那个 wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到 wrapper()函数中，否则，有些依赖函数签名的代码
        执行就会出错。
        不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的 functools.wraps 就是干这个事的，所以，一个完整的decorator的写法如下：
        import functools        

        def log(func):
            @functools.wraps(func) # 把原始函数的__name__等属性复制到 wrapper()函数中
            def wrapper(*args, **kw): 
                print('call %s():' % func.__name__)
                return func(*args, **kw)
            return wrapper

        或者针对带参数的decorator：
        import functools        

        def log(text):
            def decorator(func):
                @functools.wraps(func) # 把原始函数的__name__等属性复制到 wrapper()函数中
                def wrapper(*args, **kw):
                    print('%s %s():' % (text, func.__name__))
                    return func(*args, **kw)
                return wrapper
            return decorator
        import functools是导入functools模块。模块的概念稍候讲解。现在，只需记住在定义 wrapper()的前面加上@functools.wraps(func)即可。
map()和 reduce()函数
    map()函数
            表示 -- map(函数, Iterable)     
            参数
                map()函数接收两个参数，一个是函数，一个是Iterable--可迭代对象
                可迭代对象--可以通过 for ... in 循环来遍历的对象
            作用 -- map将传入的函数依次作用到可迭代对象的每个元素，并把结果作为新的Iterator返回。
        
            举例说明，比如我们有一个函数f(x)=x2，要把这个函数作用在一个list [1, 2, 3, 4, 5, 6, 7, 8, 9]上，就可以用map()实现如下：

                >>> def f(x):
                ...     return x * x
                ...
                >>> r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
                >>> list(r)
                [1, 4, 9, 16, 25, 36, 49, 64, 81]
                map()传入的第一个参数是f，即函数对象本身。由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。

                你可能会想，不需要map()函数，写一个循环，也可以计算出结果：

                L = []
                for n in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                    L.append(f(n))
                print(L)
                的确可以，但是，从上面的循环代码，能一眼看明白“把f(x)作用在list的每一个元素并把结果生成一个新的list”吗？

                所以，map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：

                >>> list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
                ['1', '2', '3', '4', '5', '6', '7', '8', '9']
                只需要一行代码。

    reduce()函数
        表示 -- reduce(函数, Iterable)
        参数
                reduce()函数接收两个参数，一个是函数，一个是Iterable--可迭代对象
                可迭代对象--可以通过 for ... in 循环来遍历的对象
        作用 -- reduce将传入的函数依次作用到可迭代对象的每个元素，把结果继续和下一个元素做累积计算
        例子
                reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
                比方说对一个序列求和，就可以用reduce实现：

                >>> from functools import reduce
                >>> def add(x, y):
                ...     return x + y
                ...
                >>> reduce(add, [1, 3, 5, 7, 9])
                25
                当然求和运算可以直接用Python内建函数sum()，没必要动用reduce。

                但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：

                >>> from functools import reduce
                >>> def fn(x, y):
                ...     return x * 10 + y
                ...
                >>> reduce(fn, [1, 3, 5, 7, 9])
                13579
                这个例子本身没多大用处，但是，如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：

                >>> from functools import reduce
                >>> def fn(x, y):
                ...     return x * 10 + y
                ...
                >>> def char2num(s):
                ...     return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
                ...
                >>> reduce(fn, map(char2num, '13579'))
                13579
                整理成一个str2int的函数就是：

                from functools import reduce

                def str2int(s):
                    def fn(x, y):
                        return x * 10 + y
                    def char2num(s):
                        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
                    return reduce(fn, map(char2num, s))
                还可以用lambda函数进一步简化成：

                from functools import reduce

                def char2num(s):
                    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

                def str2int(s):
                    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
                也就是说，假设Python没有提供int()函数，你完全可以自己写一个把字符串转化为整数的函数，而且只需要几行代码！

                lambda函数的用法在后面介绍。

        练习

                利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

                # -*- coding: utf-8 -*-

                def normalize(name):
                    pass

                # 测试:
                L1 = ['adam', 'LISA', 'barT']
                L2 = list(map(normalize, L1))
                print(L2)
                 Run
                Python提供的sum()函数可以接受一个list并求和，请编写一个prod()函数，可以接受一个list并利用reduce()求积：

                # -*- coding: utf-8 -*-

                from functools import reduce

                def prod(L):

                    pass

                print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
                 Run
                利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

                # -*- coding: utf-8 -*-

                from functools import reduce

                def str2float(s):

                    pass

                print('str2float(\'123.456\') =', str2float('123.456'))
                 Run
        参考代码

                do_map.py

                do_reduce.py 