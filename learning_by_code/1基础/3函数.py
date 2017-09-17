'抽象'是数学中非常常见的概念
借助抽象，我们才能'不关心底层的具体计算过程'，而'直接在更高的层次上思考问题'。
写计算机程序也是一样，'函数就是最基本的一种代码抽象的方式'

class 定义函数:
	定义
    	在Python中，'定义一个函数'要使用'def语句'，
    	依次写出'函数名、括号、括号中的参数和冒号:'，
    	然后，在'缩进块'中'编写函数体'，
    	函数的'返回值'用'return语句'返回。
    函数的返回值(注意)
        函数返回值是一个 tuple, tuple 内的元素可以是一个也可以是多个
            在语法上，返回一个tuple可以省略括号，而返回多个值时，全部放入一个 tuple 中，
            按位置赋给对应的值，所以，Python的函数返回多值其实就是返回一个tuple，但写起来更方便。        

        函数体内部的语句在执行时，一旦执行到 return 时，函数就执行完毕，并将结果返回。
        因此，函数内部通过条件判断和循环可以实现非常复杂的逻辑。
        
        如果没有 return 语句，函数执行完毕后也会返回结果，只是结果为 None。
        return None 可以简写为 return

        函数返回结果并不代表显示结果，显示该函数的返回值需要调用该函数
        调用该函数也不一定会显示出结果，因为函数返回值为 None 时，是不显示的
        故函数语句体内的 return 语句需指明该函数返回什么样的结果，才会在函数调用时显示该 return 语句指明的结果
    例：
        >>> def a():
        	b=1+2                	
        >>> a() # 返回值默认为 None，不显示
        >>> def a():
        	b=1+2
        	return        
        >>> a() # 返回值默认为 None，不显示
        >>> def a():
        	b=1+2
        	return None        
        >>> a() # 返回值为 None，不显示
        >>> def a():
        	b=1+2
        	return 7        
        >>> a() # 指定返回值为 7，显示 7
        7
        >>> def a():
        	b=1+2
        	return b        
        >>> a() # 指定返回值为 b 的计算结果，返回 b 的计算结果
        3
        >>> 

        >>> def a():
        	aa=1+2
        	return        
        >>> def b():
        	bb=2+3
        	return a(),bb        
        >>> b() # 调用 b()函数, 返回两个值，但显示在一个 tuple 中
        (None, 5)     
    空函数
        如果想定义一个什么事也不做的空函数，可以用pass语句：
            def nope():
                pass
        用途
            缺少了pass，代码运行就会有语法错误
            pass语句可以用来作为占位符，比如现在还没想好怎么写函数的代码，就可以先放一个pass，让代码能运行起来。
    函数的参数
        参数类型 
            位置参数(positional agument)
                定义 
                    即按位置传递参数
            必选参数(required agument)
                定义 
                    必选参数，与其对应的是可选参数，是指在调用函数或方法时，必须给这个参数指定一个符合该类型的值
            可选参数()
                默认参数(default / optional argument)
                    作用
                        默认参数可以简化函数的调用，降低调用函数的难度
                    表示方式
                        argument=value # argument 为参数名，等号 = 表示赋值，value 为该参数的默认值
                    注意
                        一 是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
                        二 是如何设置默认参数。当函数有多个参数时，把变化大的参数放前面作为必选参数，变化小的参数放后面。变化小的参数
                           就可以作为默认参数。
                        三 有多个默认参数时，调用的时候，既可以按顺序提供默认参数，也可以不按顺序提供部分默认参数。当不按顺序提供部分
                           默认参数时，需要把参数名写上，如 argument1 = new_value
                        四 默认参数必须指向不变对象！
                            指向可变对象时，如 list
                                def add_end(L=[]):
                                    L.append('END')
                                    return L
                                当你正常调用时，结果似乎不错：
                                >>> add_end([1, 2, 3])
                                [1, 2, 3, 'END']
                                >>> add_end(['x', 'y', 'z'])
                                ['x', 'y', 'z', 'END']
                                当你使用默认参数调用时，一开始结果也是对的：
                                >>> add_end()
                                ['END']
                                但是，再次调用add_end()时，结果就不对了：
                                >>> add_end()
                                ['END', 'END']
                                >>> add_end()
                                ['END', 'END', 'END']
                                原因解释如下：
                                Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，
                                如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
                                所以，定义默认参数要牢记一点：默认参数必须指向不变对象！                                
                            指向不可变对象时，如 None
                                要修改上面的例子，我们可以用None这个不变对象来实现：
                                def add_end(L=None):  
                                    if L is None:                                 
                                        L = []
                                    L.append('END')
                                    return L
                                现在，无论调用多少次，都不会有问题：
                                >>> add_end()
                                ['END']
                                >>> add_end()
                                ['END']
                                >>> add_end([9,0])
                                [9, 0, 'END']
                                为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于
                                修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在
                                编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。


                    使用
                        调用函数是默认参数可以传递值也可以不传递值，传递值时使用该值，不传递值时使用默认值
                位置可变参数(*args，variable positional arguments) # 参数个数可变
                    定义
                        顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个
                        这些可变参数在函数调用时自动组装为一个 tuple
                        例：
                            >>> def person(name, age, *args):
                                print('name:', name, 'age:', age, 'other:', args)
                            >>> person('point',1)
                            name: point age: 1 other: ()      
                    例： 

                        我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。                            
                        不使用可变参数 
                            要定义出这个函数，我们必须确定输入的参数。由于参数个数不确定，我们首先想到可以把a，b，c……作为一个list或tuple传
                            进来，这样，函数可以定义如下：   
                            def calc(numbers):
                                sum = 0
                                for n in numbers:
                                    sum = sum + n * n
                                return sum
                            但是调用的时候，需要先组装出一个list或tuple：
                            >>> calc([1, 2, 3])
                            14
                            >>> calc((1, 3, 5, 7))
                            84
                        使用可变参数
                            如果利用可变参数，调用函数的方式可以简化成这样：
                            >>> calc(1, 2, 3)
                            14
                            >>> calc(1, 3, 5, 7)
                            84
                            所以，我们把函数的参数改为可变参数：
                            def calc(*numbers):
                                sum = 0
                                for n in numbers:
                                    sum = sum + n * n
                                return sum
                        区别
                            定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，
                            因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数：
                            >>> calc(1, 2)
                            5
                            >>> calc()
                            0
                            如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
                            >>> nums = [1, 2, 3]
                            >>> calc(nums[0], nums[1], nums[2])
                            14
                            这种写法当然是可行的，问题是太繁琐，所以Python允许你在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传
                            进去：
                            >>> nums = [1, 2, 3]
                            >>> calc(*nums)
                            14
                            *nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。               
                关键字可变参数(**kwargs, variable keyword arguments)
                        定义                        
                            关键字可变参数允许你传入 0个或任意个含参数名的参数，
                            这些关键字参数在函数内部自动组装为一个 dict。
                        例：
                            函数person除了必选参数name和age外，还接受关键字参数kw。
                              在调用该函数时，可以只传入必选参数：  
                                def person(name, age, **kw):
                                    print('name:', name, 'age:', age, 'other:', kw)                                
                                >>> person('Michael', 30)
                                name: Michael age: 30 other: {}
                              也可以传入任意个数的关键字参数：
                                >>> person('Bob', 35, city='Beijing')
                                name: Bob age: 35 other: {'city': 'Beijing'}
                                >>> person('Adam', 45, gender='M', job='Engineer')
                                name: Adam age: 45 other: {'gender': 'M', 'job': 'Engineer'}
                        作用        
                            它可以扩展函数的功能。
                                比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，
                                我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用
                                关键字参数来定义这个函数就能满足注册的需求。
                            和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：
                                >>> extra = {'city': 'Beijing', 'job': 'Engineer'}
                                >>> person('Jack', 24, city=extra['city'], job=extra['job'])
                                name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
                            当然，上面复杂的调用可以用简化的写法：
                                >>> extra = {'city': 'Beijing', 'job': 'Engineer'}
                                >>> person('Jack', 24, **extra)
                                name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}
                                **extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
                            注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。
                命名关键字参数()   
                        定义
                            对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数，
                            命名关键字参数可以限制关键字可变参数的名字      
                        表示 
                            和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符'*,', '*,'后面的参数被视为命名关键字参数。 
                            如果函数定义中已经有了一个可变参数*args，后面跟着的命名关键字参数就不再需要一个特殊分隔符'*,'了   
                        注意
                            命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：                        
                                def person(name, age, *args, city, job):
                                    print(name, age, args, city, job)
                                >>> person('Jack', 24, 'Beijing', 'Engineer')
                                Traceback (most recent call last):
                                  File "<stdin>", line 1, in <module>
                                TypeError: person() takes 2 positional arguments but 4 were given
                            传入参数名
                                >>> person('Jack', 24, city='Beijing', job='Engineer')
                                Jack 24 () Beijing Engineer
                                由于调用时缺少参数名city和job，Python解释器把这4个参数均视为位置参数，但person()函数仅接受2个位置参数。
                            命名关键字参数可以有缺省值，从而简化调用：
                                def person(name, age, *, city='Beijing', job):
                                    print(name, age, city, job)
                                由于命名关键字参数city具有默认值，调用时，可不传入city参数：
                                >>> person('Jack', 24, job='Engineer')
                                Jack 24 Beijing Engineer
                            使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。
                                如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
                                def person(name, age, city, job):
                                    # 缺少 *，city和job被视为位置参数
                                    pass
       
        参数组合
            在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
            但是请注意，参数定义的顺序必须是：'必选参数、默认参数、可变参数、命名关键字参数和关键字参数。'

            对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
                例：
                    def f1(a, b, c=0, *args, **kw):
                        print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
                    def f2(a, b, c=0, *, d, **kw):
                        print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
                    >>> args = (1, 2, 3, 4)
                    >>> kw = {'d': 99, 'x': '#'}
                    >>> f1(*args, **kw)
                    a = 1 b = 2 c = 3 args = (4,) kw = {'d': 99, 'x': '#'}
                    >>> args = (1, 2, 3)
                    >>> kw = {'d': 88, 'x': '#'}
                    >>> f2(*args, **kw)
                    a = 1 b = 2 c = 3 d = 88 kw = {'x': '#'}
        参数检查
            自定义函数
                调用函数时，如果'参数个数不对'，Python解释器会自动检查出来，并抛出TypeError
                但是如果'参数类型不对'，Python解释器就无法帮我们检查。
            内置函数    

                会同时检查参数的类型和个数，因为已内置检查机制
            数据类型检查可以用 内置函数isinstance() 实现
                def my_abs(x):
                    if not isinstance(x, (int, float)):
                        raise TypeError('bad operand type')
                    if x >= 0:
                        return x
                    else:
                        return -x
                添加了参数检查后，如果传入错误的参数类型，函数就可以抛出一个错误：
                >>> my_abs('A')
                Traceback (most recent call last):
                  File "<stdin>", line 1, in <module>
                  File "<stdin>", line 3, in my_abs
                TypeError: bad operand type
    小结
        定义函数的时候，我们把参数的名字和位置确定下来，函数的接口定义就完成了。对于函数的调用者来说，只需要知道
        '如何传递正确的参数，以及函数将返回什么样的值'就够了，函数内部的复杂逻辑被封装起来，调用者无需了解
        
        默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

        要注意定义可变参数和关键字参数的语法：
            *args是可变参数，args接收的是一个tuple；
            **kw是关键字参数，kw接收的是一个dict。

        以及调用函数时如何传入可变参数和关键字参数的语法：
            可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
            关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
            使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

        命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
            
            定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。
class 函数调用:
	内置函数
    	要调用一个函数，需要知道函数的名称和参数
    	调用函数的时候，如果传入的参数数量不对，会报TypeError的错误
        如果传入的参数数量是对的，但参数类型不能被函数所接受，也会报TypeError的错误
    自定义函数
        调用函数时，如果'参数个数不对'，Python解释器会自动检查出来，并抛出TypeError
        但是如果'参数类型不对'，Python解释器就无法帮我们检查。可以自定义除错机制
    
    在函数内部，可以调用其他函数。
    如果一个函数在内部调用自身本身，这个函数就是递归函数。
        递归函数的优点是定义简单，逻辑清晰。理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。

        使用递归函数需要'注意防止栈溢出'。在计算机中，函数调用是通过栈（stack）这种数据结构实现的，每当进入一个函数
        调用，栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。    

            解决递归调用栈溢出的方法是通过'尾递归优化'，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也
            是可以的。
            尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，
            使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况
            Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。

    