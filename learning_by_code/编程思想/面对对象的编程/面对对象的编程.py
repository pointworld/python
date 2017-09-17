'在Python中，所有数据类型都可以视为对象'，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的 类(Class)的概念。
面向对象的设计思想是从自然界中来的，因为在自然界中，类(Class) 和 实例(Instance) 的概念是很自然的。Class是一种抽象概念，
比如我们定义的Class——Student，是指学生这个概念，而 实例(Instance) 则是一个个具体的Student，比如，Bart Simpson和
Lisa Simpson是两个具体的Student。
所以，面向对象的设计思想是'抽象出Class，根据Class创建Instance'
面向对象编程(Object-Oriented Programming, OOP)
    定义

        是一种程序设计思想。OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
    特点
        '面向对象的抽象程度又比函数要高'，因为一个Class既包含数据，又包含操作数据的方法。
        '数据封装、继承和多态'是面向对象的三大特点
过程与对象的区别()
    面向过程的程序设计()
        面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续
        切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。
    面向对象的程序设计()
        而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，
        计算机程序的执行就是一系列消息在各个对象之间传递。

    例子说明
        面向过程和面向对象在程序流程上的不同之处
                假设我们要处理学生的成绩表，为了表示一个学生的成绩
            采用面向过程的程序设计思想
                面向过程的程序可以用一个 dict 表示：
                std1 = { 'name': 'Michael', 'score': 98 }
                std2 = { 'name': 'Bob', 'score': 81 }
                而处理学生成绩可以通过函数实现，比如打印学生的成绩：
                def print_score(std):
                    print('%s: %s' % (std['name'], std['score']))
            采用面向对象的程序设计思想
                我们首选思考的不是程序的执行流程，而是Student这种数据类型应该被视为一个对象，这个对象拥有name和score这两个属性（Property）。
                如果要打印一个学生的成绩，首先必须创建出这个学生对应的对象，然后，给对象发一个print_score消息，让对象自己把自己的数据打印出来。
                class Student(object):                

                    def __init__(self, name, score):
                        self.name = name
                        self.score = score                

                    def print_score(self):
                        print('%s: %s' % (self.name, self.score))
                给对象发消息实际上就是调用对象对应的关联函数，我们称之为 对象的方法(Method)。面向对象的程序写出来就像这样：
                bart = Student('Bart Simpson', 59)
                lisa = Student('Lisa Simpson', 87)
                bart.print_score()
                lisa.print_score()

类和实例(Class and Instance)
    定义()
        面向对象最重要的概念就是 类(Class) 和 实例(Instance)，必须牢记'类是抽象的模板'，而'实例是根据类创建出来的一个个具体的“对象”'，
        每个对象都拥有相同的方法，但各自的数据可能不同。        
    表示()
        类(Class) 
            class 类名(继承类):

            定义类是通过 class 关键字
            class 后面紧接着是 类名，类名通常是'大写开头'的单词
            类名后面紧接着是 (object) ，表示该类是从哪个类继承下来的 
            最后别忘了冒号 :   
        实例(Instance)
            创建实例是通过 类名+() 实现的
类属性和类方法(Class property and Class Method)
    定义
                直接在class中定义的属性和方法，即类属性和类方法
                在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。
    表示
                类属性 
        			直接在class中定义属性，这种属性是类属性，归类所有：
        			class Student(object):
        			    name = 'Student'
        			当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。来测试一下：
        			>>> class Student(object):
        			...     name = 'Student'
        			...
        			>>> s = Student() # 创建实例s
        			>>> print(s.name) # 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性
        			Student
        			>>> print(Student.name) # 打印类的name属性
        			Student
        			>>> s.name = 'Michael' # 给实例绑定name属性
        			>>> print(s.name) # 由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性
        			Michael
        			>>> print(Student.name) # 但是类属性并未消失，用Student.name仍然可以访问
        			Student
        			>>> del s.name # 如果删除实例的name属性
        			>>> print(s.name) # 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
        			Student
        			从上面的例子可以看出，在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是
        			当你删除实例属性后，再使用相同的名称，访问到的将是类属性。        
                类方法 # 可以实现数据封装，访问类的数据, 或是给类增加新的方法
                                def method1(self,argument1,argument2,...,argumentn)
                                    pass
                                def method2(self,argument1,argument2,...,argumentn)
                                    pass
                                ...     
                                和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数，其他参数正常传入。
                                除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。
                                方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据。

                                内部数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节。
    访问限制 # 参考变量与函数的作用域，同理可以把类的属性和方法变为私有属性和方法，只有内部可以访问，外部不能访问
                函数与变量的作用域() # 实现代码封装和抽象的一种方法
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
                class 内部访问限制
                            在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。
                            但是，从前面Student类的定义来看，'外部代码还是可以自由地修改一个实例的name、score属性：'
                            >>> bart = Student('Bart Simpson', 98)
                            >>> bart.score
                            98
                            >>> bart.score = 59
                            >>> bart.score
                            59
                            如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个
                            私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：
                            class Student(object):            

                                def __init__(self, name, score):
                                    self.__name = name
                                    self.__score = score            

                                def print_score(self):
                                    print('%s: %s' % (self.__name, self.__score))
                            改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量.__name和实例变量.__score了：
                            >>> bart = Student('Bart Simpson', 98)
                            >>> bart.__name
                            Traceback (most recent call last):
                              File "<stdin>", line 1, in <module>
                            AttributeError: 'Student' object has no attribute '__name'
                            这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。
                            但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：
                            class Student(object):
                                ...            

                                def get_name(self):
                                    return self.__name            

                                def get_score(self):
                                    return self.__score
                            如果又要允许外部代码修改score怎么办？可以再给Student类增加set_score方法：
                            class Student(object):
                                ...            

                                def set_score(self, score):
                                    self.__score = score
                            你也许会问，原先那种直接通过bart.score = 59也可以修改啊，为什么要定义一个方法大费周折？因为在方法中，可以对参数做检查，
                            避免传入无效的参数：
                            class Student(object):
                                ...            

                                def set_score(self, score):
                                    if 0 <= score <= 100:
                                        self.__score = score
                                    else:
                                        raise ValueError('bad score')
                            需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以
                            直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
                            有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，
                            当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
                            双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成
                            了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：
                            >>> bart._Student__name
                            'Bart Simpson'
                            但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
                            总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。
                            最后注意下面的这种错误写法：
                            >>> bart = Student('Bart Simpson', 98)
                            >>> bart.get_name()
                            'Bart Simpson'
                            >>> bart.__name = 'New Name' # 设置__name变量！
                            >>> bart.__name
                            'New Name'
                            表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量
                            已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。不信试试：
                            >>> bart.get_name() # get_name()内部返回self.__name
                            'Bart Simpson'
实例属性和实例方法(Instance property and Instance Method)
    定义
                由于Python是动态语言，根据类创建的实例可以任意绑定属性和方法，这就是动态语言的灵活性。
                给实例绑定属性的方法是 通过实例变量(动态绑定)，或者 通过self变量实现(静态绑定)
                给一个实例动态绑定的属性和方法，对另一个实例是不起作用的
    表示
                实例属性
                                通过self变量实现 # 通过 __init__ 方法实现 静态绑定
                    	            def __init__(self, property1, property2, ..., propertyn)
                    	                self.property1=property1
                    	                self.property2=property2
                    	                ...
                    	                self.propertyn=propertyn
                    	                
                    	                注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建
                    	                的实例本身。
                    	                有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例
                    	                变量传进去        
                                通过实例变量实现 # 动态绑定
            				先定义class：
            				class Student(object):
            				    pass
            				然后，尝试给实例绑定一个属性：
            				>>> s = Student() # s 是实例变量
            				>>> s.name = 'Michael' # 动态给实例绑定一个属性
            				>>> print(s.name)
            				Michael        	
                实例方法
        			给实例绑定一个方法：
        				>>> def set_age(self, age): # 定义一个函数作为实例方法
        				...     self.age = age
        				...
        				>>> from types import MethodType
        				>>> s.set_age = MethodType(set_age, s) # 给实例绑定一个方法
        				>>> s.set_age(25) # 调用实例方法
        				>>> s.age # 测试结果
        				25
        			但是，给一个实例绑定的方法，对另一个实例是不起作用的：
        				>>> s2 = Student() # 创建新的实例
        				>>> s2.set_age(25) # 尝试调用方法
        				Traceback (most recent call last):
        				  File "<stdin>", line 1, in <module>
        				AttributeError: 'Student' object has no attribute 'set_age'
        			为了给所有实例都绑定方法，可以给class绑定方法：
        				>>> def set_score(self, score):
        				...     self.score = score
        				...
        				>>> Student.set_score = set_score
        			给class绑定方法后，所有实例均可调用：
        				>>> s.set_score(100)
        				>>> s.score
        				100
        				>>> s2.set_score(99)
        				>>> s2.score
        				99
        			通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。
                例子 
                                class Student(object):
                                    pass
                                >>> bart = Student()
                                >>> bart
                                <__main__.Student object at 0x10a67a590>
                                >>> Student
                                <class '__main__.Student'>
                                可以看到，变量bart指向的就是一个Student的实例，后面的0x10a67a590是内存地址，每个object的地址都不一样，而Student本身则是一个类。        
                                '可以自由地给一个实例变量绑定属性'，比如，给实例bart绑定一个name属性：
                                >>> bart.name = 'Bart Simpson'
                                >>> bart.name
                                'Bart Simpson'
                                给类绑定属性
                                由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建
                                实例的时候，就把name，score等属性绑上去：
                                class Student(object):            
                                   def __init__(self, name, score):
                                        self.name = name
                                        self.score = score
                                注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建
                                的实例本身。
                                有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例
                                变量传进去：
                                >>> bart = Student('Bart Simpson', 59)
                                >>> bart.name
                                'Bart Simpson'
                                >>> bart.score
                                59
类属性和实例属性区别()

    属性就是属于一个对象的数据或者函数元素，可以通过我们熟悉的据点属性标识法来访问。

    类属性

        类属性包含类的数据属性和方法属性（函数），类属性只与其定义的类相关。 
        访问类的字典属性__dict__可以获得类属性。

            class Test(object):
                v = 0.1

                def test(self):
                    pass

            >Test.__dict__
            >{'__module__': '__main__', '__dict__': <attribute '__dict__' of 'Test' objects>, 'v': 0.1, 'test': <function test at 0x2ee3cf8>, '__weakref__': <attribute '__weakref__' of 'Test' objects>, '__doc__': None}
            除了定义的v, test, __init__ 属性外，还有一些特殊的类属性。

            attribute   desc
            __name__    类的名字字符串
            __doc__ 类的文档字符串
            __bases__   类的基类元组
            __dict__    类的属性
            __module__  类定义所在的模块
            __class__   类对象对应的类
    实例属性

        类实例化后具有的属性，通过__dict__方法可以获取实例属性。

            class Test(object):
                v = 0.1
                def __init__(self):
                    self.info = 'test'


            t = Test()
            >t.__dict__
            >{'info': 'test'}
            严格来说，实例属性应只包含数据属性。

            但其实我们可以给实例增加方法属性。

            class Test(object):
                pass

            t = Test()
            def fun():
                pass
            t.f = fun
            >t.__dict__
            >{'f': <function __main__.fun>}
    类属性和实例属性区别

        下面举几个例子说明

            class Test(object):
                v = 1

            t = Test()
            print t.v       # 类属性，1
            print Test.v    # 类属性，1
            t.v = 2         # 修改实例属性，此处类属性不变（当且仅当实例属性为不可变对象）
            print t.v       # 实例属性，2
            print Test.v    # 类属性，1
            del t.v         # 删除实例属性
            print t.v       # 访问类属性，1
            Test.v = 2      # 修改类属性
            print Test.v    # 访问类属性，2
            print t.v       # 访问类属性，2
         注意：

            1.内建函数dir可以用来查看类属性和实例属性，但得到的内容比预期要多。 
            2.虽然类属性不是实例属性，但类的实例可以访问类的属性。 
            3.不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。
关于Python类属性与实例属性的讨论()
        标题名字有点长。
            之所以想写这个文章是因为碰巧看到网上一篇关于Pyhon中类属性及实例属性区别的帖子。因为我之前也被这个问题困扰过，今天碰巧看到了
            这篇帖子，发现帖子的作者只是描述了现象，然后对原因的解释比较含糊，并没有从根本上解释这个问题，所以才想写一下我对这个问题的想法。

        问题描述

            为了方便对比，我还是使用原帖子的例子：

            class AAA():  
                aaa = 10  

            # 情形1   
            obj1 = AAA()  
            obj2 = AAA()   
            print obj1.aaa, obj2.aaa, AAA.aaa   

            # 情形2  
            obj1.aaa += 2  
            print obj1.aaa, obj2.aaa, AAA.aaa   

            # 情形3  
            AAA.aaa += 3  
            print obj1.aaa, obj2.aaa, AAA.aaa  
            情形1的结果是：10 10 10；
            情形2的结果是：12 10 10；
            情形3的结果是：12 13 13；

        首先为什么会有这个问题呢？
            因为aaa属性被称为类属性，既然是类属性，那么根据从C++/Java这种静态语言使用的经验来判断，类属性应该是为其实例所共享的。很自然的，既然是共享关系，
            那么从类的层次改变aaa的值，自然其实例的aaa的值也要跟着变化了。
            可是情形3的情况却说明，上面的说法是错的。
            错哪里呢？
        要从Python的类属性讲起

        Python中类属性的含义

            Python属于动态强类型的语言，在很多地方和静态语言不同，因此，不能把静态语言的规则套到动态语言上来。其中，类属性就是一个很好的例子。
            Python中属性的获取
            对于属性，我们通常采用'类.属性或实例.属性'的形式调用。
            例如上例中的AAA.aaa属于类.属性形式，obj1.aaa属于实例.属性的形式
            Python中属性的设置
            对于'属性的设置我们通常采用类.属性 = 值或实例.属性 = 值的形式'
            例如obj1.aaa = 3

            上例中obj1.aaa += 2等价于obj1.aaa = obj1.aaa + 2，这句话包含了属性获取及属性设置两个操作

            OK，重点来了，Python中属性的获取和设置的机制与静态语言是不同的，正是背后机制的不同，导致了Python中类属性不一定是为其实例所共享的

        Python中属性查找机制

            'Python中属性的获取存在一个向上查找机制'，还是拿上面的例子做说明：
            'Python中一切皆对象'，AAA属于类对象，obj1属于实例对象，从对象的角度来看，AAA与obj1是两个无关的对象，但是，Python通过下面的
            查找树建立了类对象AAA与实例对象obj1、obj2之间的关系。
            如图所示

                    AAA
                     |
                   -----
                  |     |  
                obj1   obj2
            (图画的不好，见谅 -.-!!!)
            当调用AAA.aaa时，直接从AAA获取其属性aaa。
            但是情形1中调用obj1.aaa时，Python按照从obj1到AAA的顺序由下到上查找属性aaa。
            值得注意的这时候obj1是没有属性aaa的，于是，Python到类AAA中去查找，成功找到，并显示出来。所以，从现象上来看，AAA的属性aaa确实是共享给
            其所有实例的，虽然这里只是从查找树的形式模拟了其关系。

        Python中的属性设置

            原帖子的作者也指出问题的关键在于情形2中obj1.aaa += 2。
            为什么呢？
            上面我们指出obj.aaa += 2包含了属性获取及属性设置两个操作。即obj1.aaa += 2等价于obj1.aaa = obj1.aaa + 2。
            其中等式右侧的obj.aaa属于属性获取，其规则是按照上面提到的查找规则进行，即，这时候，获取到的是AAA的属性aaa，所以等式左侧的值为12。
            第二个操作是属性设置，即obj.aaa = 12。当发生属性设置的时候，obj1这个实例对象没有属性aaa，因此会为自身动态添加一个属性aaa。
            由于从对象的角度，类对象和实例对象属于两个独立的对象，所以，这个aaa属性只属于obj1，也就是说，这时候类对象AAA和实例对象aaa各自有一个属性aaa。
            那么，在情形3中，再次调用obj1.aaa时，按照属性调用查找规则，这个时候获取到的是实例对象obj1的属性aaa，而不是类对象AAA的属性aaa。

        对问题探讨的总结

            到这里就可以完满解释上面的问题：
            1. Python中属性的获取是按照'从下到上的顺序'来查找属性；
            2. Python中的'类和实例是两个完全独立的对象'；
            3. Python中的'属性设置是针对对象本身进行的'；

        对情形1的解释

            因为Python中的属性获取是按照从下到上的顺序来查找的，所以在情形1：

            obj1 = AAA()  
            obj2 = AAA()
            实例对象obj1和obj2不存在属性aaa。
            证明如下：

            >>> obj1.__dict__
            {}
            >>> obj2.__dict__
            {}
            所以，此时，obj1.aaa, obj2.aaa, AAA.aaa实质上都是指AAA.aaa。因此，输出同样的结果。

        对情形2的解释

            因为Python中的类和实例是两个完全独立的对象且Python中的属性设置是针对对象本身进行的，所以在情形2：

            obj1.aaa += 2  
            实质上是对实例对象obj1设置了属性aaa，并赋值为12。证明如下：

            >>> obj1.aaa = 3
            >>> obj1.__dict__
            {'aaa': 3}
            >>> obj2.__dict__
            {}
            因此，再次调用obj1.aaa时，将获取到的是实例对象obj1的属性aaa，而不是类对象AAA的属性aaa。而对于实例对象obj2，
            由于其并没有属性aaa，所以调用obj2.aaa时，获取到的是AAA的属性aaa。

        对情形3的解释

            顺利理解了前两个情形，那么第3个情形就很容易了，改变AAA的属性aaa只能影响到类对象AAA和实例对象obj2，不能影响obj1，
            因为，obj1存在aaa，在获取时，不会获取到AAA的属性。

        写在最后的话
            
            问题本身很简单，但是通过对这个问题的探讨，可以深入理解Python作为一个动态语言，在OOP的机制上与静态语言的差别。
            最关键的地方在于两点：
            1. 理解Python是如何利用'查找树的机制'来模仿类及实例之间的关系；
            2. 理解动态语言是可以动态设置属性的

封装继承与多态()
    封装()
        封装内部逻辑，数据和操作
        在定义类时绑定的方法即实现了封装
    继承()
            继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写。
            在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，新的class称为子类（Subclass），而被继承的class称为
            基类、父类或超类（Base class、Super class）。
            比如，我们已经编写了一个名为Animal的class，有一个 run()方法可以直接打印：
            class Animal(object):
                def run(self):
                    print('Animal is running...')
            当我们需要编写Dog和Cat类时，就可以直接从Animal类继承：
            class Dog(Animal):
                pass            

            class Cat(Animal):
                pass
            对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类。Cat和Dog类似。
            继承有什么好处？最大的好处是子类获得了父类的全部功能。由于Animial实现了 run()方法，因此，Dog和Cat作为它的子类，什么事也没干，
            就自动拥有了 run()方法：
            dog = Dog()
            dog.run()            

            cat = Cat()
            cat.run()
            运行结果如下：
            Animal is running...
            Animal is running...
            当然，也可以对子类增加一些方法，比如Dog类：
            class Dog(Animal):            

                def run(self):
                    print('Dog is running...')            

                def eat(self):
                    print('Eating meat...')
            继承的第二个好处需要我们对代码做一点改进。你看到了，无论是Dog还是Cat，它们 run()的时候，显示的都是Animal is running...，符合
            逻辑的做法是分别显示Dog is running...和Cat is running...，因此，对Dog和Cat类改进如下：
            class Dog(Animal):            

                def run(self):
                    print('Dog is running...')            

            class Cat(Animal):            

                def run(self):
                    print('Cat is running...')
            再次运行，结果如下：
            Dog is running...
            Cat is running...
    多态()
            当子类和父类都存在相同的 run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。这样，我们
            就获得了继承的另一个好处：多态。
            要理解什么是多态，我们首先要对数据类型再作一点说明。当我们定义一个class的时候，我们实际上就定义了一种数据类型。我们定义的数据类
            型和Python自带的数据类型，比如 str、list、dict 没什么两样：
            a = list() # a是list类型
            b = Animal() # b是Animal类型
            c = Dog() # c是Dog类型
            判断一个变量是否是某个类型可以用isinstance()判断：
            >>> isinstance(a, list)
            True
            >>> isinstance(b, Animal)
            True
            >>> isinstance(c, Dog)
            True
            看来a、b、c确实对应着list、Animal、Dog这3种类型。
            但是等等，试试：
            >>> isinstance(c, Animal)
            True
            看来c不仅仅是Dog，c还是Animal！
            不过仔细想想，这是有道理的，因为Dog是从Animal继承下来的，当我们创建了一个Dog的实例c时，我们认为c的数据类型是Dog没错，但c同时也是
            Animal也没错，Dog本来就是Animal的一种！
            所以，在继承关系中，如果一个实例的数据类型是某个子类，那它的数据类型也可以被看做是父类。但是，反过来就不行：
            >>> b = Animal()
            >>> isinstance(b, Dog)
            False
            Dog可以看成Animal，但Animal不可以看成Dog。
            要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个Animal类型的变量：
            def run_twice(animal):
                animal.run()
                animal.run()
            当我们传入Animal的实例时，run_twice()就打印出：
            >>> run_twice(Animal())
            Animal is running...
            Animal is running...
            当我们传入Dog的实例时，run_twice()就打印出：
            >>> run_twice(Dog())
            Dog is running...
            Dog is running...
            当我们传入Cat的实例时，run_twice()就打印出：
            >>> run_twice(Cat())
            Cat is running...
            Cat is running...
            看上去没啥意思，但是仔细想想，现在，如果我们再定义一个Tortoise类型，也从Animal派生：
            class Tortoise(Animal):
                def run(self):
                    print('Tortoise is running slowly...')
            当我们调用run_twice()时，传入Tortoise的实例：
            >>> run_twice(Tortoise())
            Tortoise is running slowly...
            Tortoise is running slowly...
            你会发现，新增一个Animal的子类，不必对run_twice()做任何修改，实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地
            正常运行，原因就在于多态。
            多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，因为Dog、Cat、Tortoise……都是Animal
            类型，然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，因此，传入的任意类型，只要是Animal类或者子类，就会自动
            调用实际类型的run()方法，这就是多态的意思：
            对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，而具体调用的run()方法是作用
            在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，这就是多态真正的威力：调用方只管调用，不管细节，而当我们
            新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
            对扩展开放：允许新增Animal子类；
            对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
            继承还可以一级一级地继承下来，就好比从爷爷到爸爸、再到儿子这样的关系。而任何类，最终都可以追溯到根类object，这些继承关系
            看上去就像一颗倒着的树。
操作()
	获取对象信息
	    使用 type() # 返回对应的Class类型
	        基本类型都可以用 type()判断
	        如果一个变量指向函数或者类，也可以用 type()判断
	        例
				首先，我们来判断对象类型，使用type()函数：
				基本类型都可以用type()判断：
				>>> type(123)
				<class 'int'>
				>>> type('str')
				<class 'str'>
				>>> type(None)
				<type(None) 'NoneType'>
				如果一个变量指向函数或者类，也可以用type()判断：
				>>> type(abs)
				<class 'builtin_function_or_method'>
				>>> type(a)
				<class '__main__.Animal'>
				但是type()函数返回的是什么类型呢？它返回对应的Class类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
				>>> type(123)==type(456)
				True
				>>> type(123)==int
				True
				>>> type('abc')==type('123')
				True
				>>> type('abc')==str
				True
				>>> type('abc')==type(123)
				False
				判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
				>>> import types
				>>> def fn():
				...     pass
				...
				>>> type(fn)==types.FunctionType
				True
				>>> type(abs)==types.BuiltinFunctionType
				True
				>>> type(lambda x: x)==types.LambdaType
				True
				>>> type((x for x in range(10)))==types.GeneratorType
				True
	    使用 isinstance() # 一个对象是否是某种类型
			对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数
			能用type()判断的基本类型也可以用isinstance()判断
			并且还可以判断一个变量是否是某些类型中的一种
			例
				对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
				我们回顾上次的例子，如果继承关系是：
				object -> Animal -> Dog -> Husky
				那么，isinstance()就可以告诉我们，一个对象是否是某种类型。先创建3种类型的对象：
				>>> a = Animal()
				>>> d = Dog()
				>>> h = Husky()
				然后，判断：
				>>> isinstance(h, Husky)
				True
				没有问题，因为h变量指向的就是Husky对象。
				再判断：
				>>> isinstance(h, Dog)
				True
				h虽然自身是Husky类型，但由于Husky是从Dog继承下来的，所以，h也还是Dog类型。换句话说，isinstance()判断的是一个对象是否是该类型本身，或者位于该类型的父继承链上。
				因此，我们可以确信，h还是Animal类型：
				>>> isinstance(h, Animal)
				True
				同理，实际类型是Dog的d也是Animal类型：
				>>> isinstance(d, Dog) and isinstance(d, Animal)
				True
				但是，d不是Husky类型：
				>>> isinstance(d, Husky)
				False
				能用type()判断的基本类型也可以用isinstance()判断：
				>>> isinstance('a', str)
				True
				>>> isinstance(123, int)
				True
				>>> isinstance(b'a', bytes)
				True
				并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
				>>> isinstance([1, 2, 3], (list, tuple))
				True
				>>> isinstance((1, 2, 3), (list, tuple))
				True
	    使用 dir() # 获得一个对象的所有属性和方法
		如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
				>>> dir('ABC')
				['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', 
				'__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__',
				 '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__',
				  '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 
				  'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 
				  'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 
				  'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 
				  'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
	类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
			在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，
				下面的代码是等价的：
				>>> len('ABC')
				3
				>>> 'ABC'.__len__()
				3
			我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
				>>> class MyDog(object):
				...     def __len__(self):
				...         return 100
				...
				>>> dog = MyDog()
				>>> len(dog)
				100
			剩下的都是普通属性或方法，比如lower()返回小写的字符串：
				>>> 'ABC'.lower()
				'abc'
			仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
				>>> class MyObject(object):
				...     def __init__(self):
				...         self.x = 9
				...     def power(self):
				...         return self.x * self.x
				...
				>>> obj = MyObject()
				紧接着，可以测试该对象的属性：
				>>> hasattr(obj, 'x') # 有属性'x'吗？
				True
				>>> obj.x
				9
				>>> hasattr(obj, 'y') # 有属性'y'吗？
				False
				>>> setattr(obj, 'y', 19) # 设置一个属性'y'
				>>> hasattr(obj, 'y') # 有属性'y'吗？
				True
				>>> getattr(obj, 'y') # 获取属性'y'
				19
				>>> obj.y # 获取属性'y'
				19
				如果试图获取不存在的属性，会抛出AttributeError的错误：
				>>> getattr(obj, 'z') # 获取属性'z'
				Traceback (most recent call last):
				  File "<stdin>", line 1, in <module>
				AttributeError: 'MyObject' object has no attribute 'z'
				可以传入一个default参数，如果属性不存在，就返回默认值：
				>>> getattr(obj, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404
				404
				也可以获得对象的方法：
				>>> hasattr(obj, 'power') # 有属性'power'吗？
				True
				>>> getattr(obj, 'power') # 获取属性'power'
				<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
				>>> fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
				>>> fn # fn指向obj.power
				<bound method MyObject.power of <__main__.MyObject object at 0x10077a6a0>>
				>>> fn() # 调用fn()与调用obj.power()是一样的
				81

高级特性()
	如多重继承、定制类、元类等概念
	使用 __slots__  # 限制实例能添加的属性，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
		限制实例的属性，比如，只允许对Student实例添加name和age属性。
			为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
			class Student(object):
			    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
			然后，我们试试：
			>>> s = Student() # 创建新的实例
			>>> s.name = 'Michael' # 绑定属性'name'
			>>> s.age = 25 # 绑定属性'age'
			>>> s.score = 99 # 绑定属性'score'
			Traceback (most recent call last):
			  File "<stdin>", line 1, in <module>
			AttributeError: 'Student' object has no attribute 'score'
			由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
		使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
			>>> class GraduateStudent(Student):
			...     pass
			...
			>>> g = GraduateStudent()
			>>> g.score = 9999
		除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。		
	？使用@property # Python内置的@property装饰器负责把一个方法变成属性调用
		在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
			s = Student()
			s.score = 9999
		这显然不合逻辑。为了限制score的范围
			通过调用方法实现
				可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：
				class Student(object):				

				    def get_score(self):
				         return self._score				

				    def set_score(self, value):
				        if not isinstance(value, int):
				            raise ValueError('score must be an integer!')
				        if value < 0 or value > 100:
				            raise ValueError('score must between 0 ~ 100!')
				        self._score = value
				现在，对任意的Student实例进行操作，就不能随心所欲地设置score了：
				>>> s = Student()
				>>> s.set_score(60) # ok!
				>>> s.get_score()
				60
				>>> s.set_score(9999)
				Traceback (most recent call last):
				  ...
				ValueError: score must between 0 ~ 100!
				但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。
			通过@property装饰器把一个方法变成属性调用实现
				有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必须要做到的！
				还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责
				把一个方法变成属性调用的：
				class Student(object):				

				    @property
				    def score(self):
				        return self._score				

				    @score.setter
				    def score(self, value):
				        if not isinstance(value, int):
				            raise ValueError('score must be an integer!')
				        if value < 0 or value > 100:
				            raise ValueError('score must between 0 ~ 100!')
				        self._score = value
				@property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身
				又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：
				>>> s = Student()
				>>> s.score = 60 # OK，实际转化为s.set_score(60)
				>>> s.score # OK，实际转化为s.get_score()
				60
				>>> s.score = 9999
				Traceback (most recent call last):
				  ...
				ValueError: score must between 0 ~ 100!
				注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。
				还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：
				class Student(object):				

				    @property
				    def birth(self):
				        return self._birth				

				    @birth.setter
				    def birth(self, value):
				        self._birth = value				

				    @property
				    def age(self):
				        return 2015 - self._birth
				上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。				

			@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。	
	多重继承 # 通过多重继承，一个子类就可以同时获得多个父类的所有功能
		
		class 类名(,Superclass1，Superclass2，...):
	定制类
                        看到类似__slots__这种形如__xxx__的变量或者函数名就要注意，这些在Python中是有特殊用途的。
                        __slots__ 我们已经知道怎么用了，__len__()方法我们也知道是为了能让class作用于len()函数。
                        除此之外，Python的class中还有许多这样有特殊用途的函数，可以帮助我们定制类。
                        __str__ 和 __repr__
                                        我们先定义一个Student类，打印一个实例：
                                        >>> class Student(object):
                                        ...     def __init__(self, name):
                                        ...         self.name = name
                                        ...
                                        >>> print(Student('Michael'))
                                        <__main__.Student object at 0x109afb190>
                                        打印出一堆<__main__.Student object at 0x109afb190>，不好看。
                                        怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了：
                                        >>> class Student(object):
                                        ...     def __init__(self, name):
                                        ...         self.name = name
                                        ...     def __str__(self):
                                        ...         return 'Student object (name: %s)' % self.name
                                        ...
                                        >>> print(Student('Michael'))
                                        Student object (name: Michael)
                                        这样打印出来的实例，不但好看，而且容易看出实例内部重要的数据。
                                        但是细心的朋友会发现直接敲变量不用print，打印出来的实例还是不好看：
                                        >>> s = Student('Michael')
                                        >>> s
                                        <__main__.Student object at 0x109afb310>
                                        这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序
                                        开发者看到的字符串，也就是说，__repr__()是为调试服务的。
                                        解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：
                                        class Student(object):
                                            def __init__(self, name):
                                                self.name = name
                                            def __str__(self):
                                                return 'Student object (name=%s)' % self.name
                                            __repr__ = __str__
                        __iter__
                                        如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，
                                        Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
                                        我们以斐波那契数列为例，写一个Fib类，可以作用于for循环：
                                        class Fib(object):
                                            def __init__(self):
                                                self.a, self.b = 0, 1 # 初始化两个计数器a，b            

                                            def __iter__(self):
                                                return self # 实例本身就是迭代对象，故返回自己            

                                            def __next__(self):
                                                self.a, self.b = self.b, self.a + self.b # 计算下一个值
                                                if self.a > 100000: # 退出循环的条件
                                                    raise StopIteration();
                                                return self.a # 返回下一个值
                                        现在，试试把Fib实例作用于for循环：
                                        >>> for n in Fib():
                                        ...     print(n)
                                        ...
                                        1
                                        1
                                        2
                                        3
                                        5
                                        ...
                                        46368
                                        75025
                        __getitem__
                                        Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
                                        >>> Fib()[5]
                                        Traceback (most recent call last):
                                          File "<stdin>", line 1, in <module>
                                        TypeError: 'Fib' object does not support indexing
                                        要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
                                        class Fib(object):
                                            def __getitem__(self, n):
                                                a, b = 1, 1
                                                for x in range(n):
                                                    a, b = b, a + b
                                                return a
                                        现在，就可以按下标访问数列的任意一项了：
                                        >>> f = Fib()
                                        >>> f[0]
                                        1
                                        >>> f[1]
                                        1
                                        >>> f[2]
                                        2
                                        >>> f[3]
                                        3
                                        >>> f[10]
                                        89
                                        >>> f[100]
                                        573147844013817084101
                                        但是list有个神奇的切片方法：
                                        >>> list(range(100))[5:10]
                                        [5, 6, 7, 8, 9]
                                        对于Fib却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
                                        class Fib(object):
                                            def __getitem__(self, n):
                                                if isinstance(n, int): # n是索引
                                                    a, b = 1, 1
                                                    for x in range(n):
                                                        a, b = b, a + b
                                                    return a
                                                if isinstance(n, slice): # n是切片
                                                    start = n.start
                                                    stop = n.stop
                                                    if start is None:
                                                        start = 0
                                                    a, b = 1, 1
                                                    L = []
                                                    for x in range(stop):
                                                        if x >= start:
                                                            L.append(a)
                                                        a, b = b, a + b
                                                    return L
                                        现在试试Fib的切片：
                                        >>> f = Fib()
                                        >>> f[0:5]
                                        [1, 1, 2, 3, 5]
                                        >>> f[:10]
                                        [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
                                        但是没有对step参数作处理：
                                        >>> f[:10:2]
                                        [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
                                        也没有对负数作处理，所以，要正确实现一个__getitem__()还是有很多工作要做的。
                                        此外，如果把对象看成dict，__getitem__()的参数也可能是一个可以作key的object，例如str。
                                        与之对应的是__setitem__()方法，把对象视作list或dict来对集合赋值。最后，还有一个__delitem__()方法，用于删除某个元素。
                                        总之，通过上面的方法，我们自己定义的类表现得和Python自带的list、tuple、dict没什么区别，这完全归功于动态语言的“鸭子类型”，不需要强制继承某个接口。
                        __getattr__
                                        正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。比如定义Student类：
                                        class Student(object):            

                                            def __init__(self):
                                                self.name = 'Michael'
                                        调用name属性，没问题，但是，调用不存在的score属性，就有问题了：
                                        >>> s = Student()
                                        >>> print(s.name)
                                        Michael
                                        >>> print(s.score)
                                        Traceback (most recent call last):
                                          ...
                                        AttributeError: 'Student' object has no attribute 'score'
                                        错误信息很清楚地告诉我们，没有找到score这个attribute。
                                        要避免这个错误，除了可以加上一个score属性外，Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。修改如下：
                                        class Student(object):            

                                            def __init__(self):
                                                self.name = 'Michael'            

                                            def __getattr__(self, attr):
                                                if attr=='score':
                                                    return 99
                                        当调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，这样，我们就有机会返回score的值：
                                        >>> s = Student()
                                        >>> s.name
                                        'Michael'
                                        >>> s.score
                                        99
                                        返回函数也是完全可以的：
                                        class Student(object):            

                                            def __getattr__(self, attr):
                                                if attr=='age':
                                                    return lambda: 25
                                        只是调用方式要变为：
                                        >>> s.age()
                                        25
                                        注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找。
                                        此外，注意到任意调用如s.abc都会返回None，这是因为我们定义的__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，
                                        抛出AttributeError的错误：
                                        class Student(object):            

                                            def __getattr__(self, attr):
                                                if attr=='age':
                                                    return lambda: 25
                                                raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
                                        

                                        >>> class Test(object):
                                            a=1
                                            def __init__(self,name):
                                                self.name=name
                                            def __getattr__(self,value):
                                                if value=='address':
                                                    return 'China'
                                                print('Test has no attribute %s'%value)
                                               
                                        >>> t=Test('point')
                                        >>> t.ddd
                                        Test has no attribute ddd
                                        >>> t.address
                                        'China'
                                        >>> t.a
                                        1
                                        >>>             
                                        这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
                                        这种完全动态调用的特性有什么实际作用呢？作用就是，可以针对完全动态的情况作调用。
                                        举个例子：
                                        现在很多网站都搞REST API，比如新浪微博、豆瓣啥的，调用API的URL类似：
                                        •	http://api.server/user/friends
                                        •	http://api.server/user/timeline/list
                                        如果要写SDK，给每个URL对应的API都写一个方法，那得累死，而且，API一旦改动，SDK也要改。
                                        利用完全动态的__getattr__，我们可以写出一个链式调用：
                                        class Chain(object):            

                                            def __init__(self, path=''):
                                                self._path = path            

                                            def __getattr__(self, path):
                                                return Chain('%s/%s' % (self._path, path))            

                                            def __str__(self):
                                                return self._path            

                                            __repr__ = __str__
                                        试试：
                                        >>> Chain().status.user.timeline.list
                                        '/status/user/timeline/list'
                                        这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！
                                        还有些REST API会把参数放到URL中，比如GitHub的API：
                                        GET /users/:user/repos
                                        调用时，需要把:user替换为实际用户名。如果我们能写出这样的链式调用：
                                        Chain().users('michael').repos
                                        就可以非常方便地调用API了。有兴趣的童鞋可以试试写出来。
            
                        内建函数
                            setattr(object,name,value):

                                        作用：设置object的名称为name（type：string）的属性的属性值为value，属性name可以是已存在属性也可以是新属性。
                            getattr(object,name,default):
                                        作用：返回object的名称为name的属性的属性值，如果属性name存在，则直接返回其属性值；如果属性name不存在，则触发AttribetError异常或
                                        当可选参数default定义时返回default值。        
                        对比Python中__getattr__()和 __getattribute__()获取属性的用法

                                    __getattr__ 会在没有查找到相应实例属性（或方法）时被调用，如果在 __getattr__ 方法内没有查找到对应的属性，则返回 默认值 None，IDE 中不会显示；
                                    如果在 __getattr__ 中定义了方法，则调用不存在的方法时会使用 __getattr__ 内定义的方法

                                    这篇文章主要介绍了对比Python中__getattr__和 __getattribute__获取属性的用法,注意二者间的区别,__getattr__只作用于不存在的属性,需要的朋友可以参考下
                                    相信大家觉得大多数时候我们并不太需要关注getattribute和getattr的一些细节(至少我自己吧)，
                                    一般情况下消费我们自定义的类的时候，我们对类的结构都了解，不会刻意偏离，造成一些属性访问的错误。
                                    不过作为一个有好奇心有追求有气质的python宝宝，怎么可能不稍稍研究一下呢。好吧，其实是在github上读到一个开源项目sinaweibopy的源码才看的，
                                    代码挺有意思，正好当作一个实用的例子，来看看如何自定义实现gettattr让代码更加的动态优雅：
                                    # 例子在原来的基础上简化了一下，排除依赖和干扰，详细参见原项目
                                    class UrlGenerator(object):
                                      def __init__(self, root_url):
                                        self.url = root_url
                                     
                                      def __getattr__(self, item):
                                        if item == 'get' or item == 'post':
                                          print self.url
                                        return UrlGenerator('{}/{}'.format(self.url, item))
                                     
                                     
                                    url_gen = UrlGenerator('http://xxxx')
                                    url_gen.users.show.get
                                     
                                    >>> http://xxxx/users/show
                                    充分利用getattr会在没有查找到相应实例属性时被调用的特点，方便的通过链式调用生成对应的url，源代码中在碰到http method的时候返回一个
                                    可调用的对象更加的优雅，链式的操作不仅优雅而且还能很好的说明调用的接口的意义（restful的接口啦）。
                                    示例
                                    1.__getattr__示例： 
                                    class Test(object):
                                      def __init__(self,name):
                                        self.name = name
                                      def __getattr__(self, value):
                                        if value == 'address':
                                          return 'China'
                                     
                                    if __name__=="__main__":
                                      test = Test('letian')
                                      print test.name
                                      print test.address
                                      test.address = 'Anhui'
                                      print test.address
                                    运行结果： 
                                    letian
                                    China
                                    Anhui
                                    如果是调用了一个类中未定义的方法，则__getattr__也要返回一个方法，例如： 
                                    class Test(object):
                                      def __init__(self,name):
                                        self.name = name
                                      def __getattr__(self, value):
                                        return len
                                     
                                    if __name__=="__main__":
                                      test = Test('letian')
                                      print test.getlength('letian')
                                    运行结果： 
                                    6
                                    2.__getattribute__示例： 
                                    class Test(object):
                                      def __init__(self,name):
                                        self.name = name
                                      def __getattribute__(self, value):
                                        if value == 'address':
                                          return 'China'
                                         
                                     
                                    if __name__=="__main__":
                                      test = Test('letian')
                                      print test.name
                                      print test.address
                                      test.address = 'Anhui'
                                      print test.address
                                    运行结果： 
                                    None
                                    China
                                    China
                                    深入思考
                                    既然能通过定制类的getattr自定义方法来实现一些优雅的功能，自然我们也要对它有一些了解，包括和它相似的自定义方法getattribute
                                    1. 用作实例属性的获取和拦截
                                    当访问某个实例属性时， getattribute会被无条件调用，如未实现自己的getattr方法，会抛出AttributeError提示找不到这个属性，如果自定义了
                                    自己getattr方法的话，方法会在这种找不到属性的情况下被调用，比如上面的例子中的情况。所以在找不到属性的情况下通过实现自定义的getattr方法
                                    来实现一些功能是一个不错的方式，因为它不会像getattribute方法每次都会调用可能会影响一些正常情况下的属性访问：
                                    class Test(object):
                                      def __init__(self, p):
                                        self.p = p
                                     
                                      def __getattr__(self, item):
                                        return 'default'
                                     
                                    t = Test('p1')
                                    print t.p
                                    print t.p2
                                     
                                    >>> p1
                                    >>> default
                                    2. 自定义getattribute的时候防止无限递归
                                    因为getattribute在访问属性的时候一直会被调用，自定义的getattribute方法里面同时需要返回相应的属性，通过self.__dict__取值会继续向下调用
                                    getattribute，造成循环调用：
                                    class AboutAttr(object):
                                      def __init__(self, name):
                                        self.name = name
                                     
                                      def __getattribute__(self, item):
                                        try:
                                          return super(AboutAttr, self).__getattribute__(item)
                                        except KeyError:
                                          return 'default'
                                    这里通过调用绑定的super对象来获取队形的属性，对新式类来说其实和object.__getattribute__(self, item)一样的道理:
                                    默认情况下自定义的类会从object继承getattribute方法，对于属性的查找是完全能用的
                                    getattribute的实现感觉还是挺抽象化的，只需要绑定相应的实例对象和要查找的属性名称就行
                                    3.同时覆盖掉getattribute和getattr的时候，在getattribute中需要模仿原本的行为抛出AttributeError或者手动调用getattr
                                    class AboutAttr(object):
                                      def __init__(self, name):
                                        self.name = name
                                     
                                      def __getattribute__(self, item):
                                        try:
                                          return super(AboutAttr, self).__getattribute__(item)
                                        except KeyError:
                                          return 'default'
                                        except AttributeError as ex:
                                          print ex
                                     
                                      def __getattr__(self, item):
                                        return 'default'
                                     
                                    at = AboutAttr('test')
                                    print at.name
                                    print at.not_exised
                                     
                                    >>>test
                                    >>>'AboutAttr' object has no attribute 'not_exised'
                                    >>>None
                                    上面例子里面的getattr方法根本不会被调用，因为原本的AttributeError被我们自行处理并未抛出，也没有手动调用getattr，所以访问
                                    not_existed的结果是None而不是default.                    
                        __call__
                                        一个对象实例可以有自己的属性和方法，当我们调用实例方法时，我们用 instance.method() 来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
                                        任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：
                                        class Student(object):
                                            def __init__(self, name):
                                                self.name = name            

                                            def __call__(self):
                                                print('My name is %s.' % self.name)
                                        调用方式如下：
                                        >>> s = Student('Michael')
                                        >>> s() # self参数不要传入
                                        My name is Michael.
                                        __call__()还可以定义参数。对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
                                        '如果你把对象看成函数，那么函数本身其实也可以在运行期动态创建出来，因为类的实例都是运行期创建出来的'，这么一来，我们就模糊了对象和函数的界限。
                                        那么，怎么判断一个变量是对象还是函数呢？其实，更多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有
                                        __call__()的类实例：
                                        >>> callable(Student())
                                        True
                                        >>> callable(max)
                                        True
                                        >>> callable([1, 2, 3])
                                        False
                                        >>> callable(None)
                                        False
                                        >>> callable('str')
                                        False
                                        通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
    元类(metaclass)
    	type()函数既可以返回一个对象的类型，又可以创建出新的类型, 如：
			>>> def fn(self, name='world'): # 先定义函数，可以定义多个
			...     print('Hello, %s.' % name)
			...
			>>> Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class
			>>> h = Hello()
			>>> h.hello()
			Hello, world.
			>>> print(type(Hello))
			<class 'type'>
			>>> print(type(h))
			<class '__main__.Hello'>
		    创建过程
				要创建一个class对象，type()函数依次传入3个参数：
				1.	class的名称；
				2.	继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
				3.	class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。可以定义多函数并绑定；
				通过type()函数创建的类和直接写class是完全一样的，因为Python解释器遇到class定义时，仅仅是扫描一下class定义的语法，然后调用type()
				函数创建出class。
				正常情况下，我们都用class Xxx...来定义类，但是，type()函数也允许我们动态创建出类来，也就是说，动态语言本身支持运行期动态创建类，
				这和静态语言有非常大的不同，要在静态语言运行期创建类，必须构造源代码字符串再调用编译器，或者借助一些工具生成字节码实现，本质上
				都是动态编译，会非常复杂。
		除了使用type()动态创建类以外，要控制类的创建行为，还可以使用metaclass。
		元类
			定义
				metaclass，直译为元类，简单的解释就是：
				当我们定义了类以后，就可以根据这个类创建出实例，所以：先定义类，然后创建实例。
				但是如果我们想创建出类呢？那就必须根据metaclass创建出类，所以：先定义metaclass，然后创建类。
				连接起来就是：先定义metaclass，就可以创建类，最后创建实例。
				所以，metaclass允许你创建类或者修改类。换句话说，你可以把类看成是metaclass创建出来的“实例”。
				metaclass是Python面向对象里最难理解，也是最难使用的魔术代码。正常情况下，你不会碰到需要使用metaclass的情况，
				所以，以下内容看不懂也没关系，因为基本上你不会用到。				
			创建类
				我们先看一个简单的例子，这个metaclass可以给我们自定义的MyList增加一个add方法：
				定义ListMetaclass，按照默认习惯，metaclass的类名总是以Metaclass结尾，以便清楚地表示这是一个metaclass：
				metaclass是类的模板，所以必须从`type`类型派生：
					class ListMetaclass(type):
					    def __new__(cls, name, bases, attrs):
					        attrs['add'] = lambda self, value: self.append(value)
					        return type.__new__(cls, name, bases, attrs)
				有了ListMetaclass，我们在定义类的时候还要指示使用ListMetaclass来定制类，传入关键字参数metaclass：
					class MyList(list, metaclass=ListMetaclass):
					    pass
					第一个参数list表示，继承ilst列表的所有功能；
				当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，要通过ListMetaclass.__new__()来创建
				'在此，我们可以修改类的定义，比如，加上新的方法，然后，返回修改后的定义。'
					__new__()方法接收到的参数依次是：
					1.	当前准备创建的类的对象；
					2.	类的名字；
					3.	类继承的父类集合；
					4.	类的方法集合。
				测试一下MyList是否可以调用add()方法：
					>>> L = MyList()
					>>> L.add(1)
					>> L
					[1]
				而普通的list没有add()方法：
					>>> L2 = list()
					>>> L2.add(1)
					Traceback (most recent call last):
					  File "<stdin>", line 1, in <module>
					AttributeError: 'list' object has no attribute 'add'
				动态修改有什么意义	
					动态修改有什么意义？直接在MyList定义中写上add()方法不是更简单吗？正常情况下，确实应该直接写，通过metaclass修改纯属变态。
					但是，总会遇到需要通过metaclass修改类定义的。ORM就是一个典型的例子。
					ORM全称“Object Relational Mapping”，即对象-关系映射，就是把关系数据库的一行映射为一个对象，也就是一个类对应一个表，这样，
					写代码更简单，不用直接操作SQL语句。
					要编写一个ORM框架，所有的类都只能动态定义，因为只有使用者才能根据表的结构定义出对应的类来。
			应用 # 让我们来尝试编写一个ORM框架
				编写底层模块的第一步，就是先把调用接口写出来。
					比如，使用者如果使用这个ORM框架，想定义一个User类来操作对应的数据库表User，我们期待他写出这样的代码：
					class User(Model): # 定义 User类 ，父类为Model
					    # 定义类的属性到列的映射：
					    id = IntegerField('id') # 创建IntegerField类 的实例，实例有一个参数'id'，赋值给变量 id，作为User类的类属性
					    name = StringField('username') # 创建 StringField类 的实例，实例有一个参数'username'，赋值给变量 name，作为User类的类属性
					    email = StringField('email') # 创建 StringField类 的实例，赋值给变量 email，实例有一个参数'email'，作为User类的类属性
					    password = StringField('password') # 创建 StringField类 的实例，实例有一个参数'password'，赋值给变量 password，作为User类的类属性				
				# 创建一个实例：

					u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd') # 创建 User类 的实例，赋值给 变量 u
				# 保存到数据库：

					u.save()
				其中，父类Model和属性类型StringField、IntegerField是由ORM框架提供的，剩下的魔术方法比如save()全部由metaclass自动完成。

					虽然metaclass的编写会比较复杂，但ORM的使用者用起来却异常简单。
				现在，我们就按上面的接口来实现该ORM。
					首先来定义Field类，它负责保存数据库表的字段名和字段类型：
						class Field(object): # 定义 Field类						

						    def __init__(self, name, column_type): # 实例化属性，通过 __init__ 方法给实例绑定属性; 在创建实例的时候，不能传入
						                                           # 空的参数了，必须传入与__init__方法匹配的参数, 但self不需要传
						                                           # Python解释器自己会把实例变量传进去           
						        self.name = name # name属性绑定
						        self.column_type = column_type # columntype属性绑定				

						    def __str__(self): # __str__方法用于将值转化为适于人阅读的形式<实例类名：实例属性name值>，而且方便看出实例内部重要的数据
						                       # 当打印实例时，调用__str__方法，显示 return语句返回的信息
						                       # 返回结果   <实例类名：实例属性name值>
						        return '<%s:%s>' % (self.__class__.__name__, self.name)  
					在Field的基础上，进一步定义各种类型的Field，比如StringField，IntegerField等等：
						class StringField(Field): # 定义 StringField类，父类为Field, 继承父类所有功能					
						    def __init__(self, name): # 实例化属性，通过 __init__ 方法给实例绑定属性; 在创建实例的时候，不能传入
						                              # 空的参数了，必须传入与__init__方法匹配的参数, 但self不需要传
						                              # Python解释器自己会把实例变量传进去
						        super(StringField, self).__init__(name, 'varchar(100)')	# 执行父类实例化函数，column_type属性绑定值为'varchar(100)'				
						class IntegerField(Field):	# 定义 IntegerField类，父类为Field, 继承父类所有功能				
						    def __init__(self, name): # 实例化属性，通过 __init__ 方法给实例绑定属性; 在创建实例的时候，不能传入
						                              # 空的参数了，必须传入与__init__方法匹配的参数, 但self不需要传
						                              # Python解释器自己会把实例变量传进去
						        super(IntegerField, self).__init__(name, 'bigint') # 执行父类实例化函数，column_type属性绑定值为 'bigint'
					下一步，就是编写最复杂的ModelMetaclass了：
						class ModelMetaclass(type):	# 定义Model的元类，元类从`type`类型派生					

						    def __new__(cls, name, bases, attrs): # __new__方法用于创建类或修改类，接收参数依次为 待创建类的对象，
						                                          # 待创建类的名字，待创建类继承的父类集合，待创建类的方法集合
						        if name=='Model': #　如果待创建类的名字为 'Model'
						            return type.__new__(cls, name, bases, attrs) # 类名是Model则返回并退出该创建类的过程，不对类名为Model的类进行修改
						        print('Found model: %s' % name) # 若类名不是Model, 则输出 'Found model: 类名'
						                                        # 排除Model后，这里只剩 Model的子类 User了，即打印信息 Found model:User
						        mappings = dict() # 创建一个字典，并赋值给变量 mappings 					         
						        for k, v in attrs.items(): # 用变量 K, v 遍历类（User）的属性项，
						        						   # 这里只剩 Model的子类 User了，故遍历的是User类
						            if isinstance(v, Field): # 判断类属性项的值 v 的类型是否是Field类 的实例
						                                     # User类有4个类属性的值继承自 Field类，分别是
						                                     # IntegerField('id')，StringField('username')，StringField('email')，StringField('password')
						                print('Found mapping: %s ==> %s' % (k, v)) # 若条件成立，则输出 Found mapping: 类属性项的键==>类属性项的值
						                										   # 这里的类属性项的值是Field类的4种子类的实例，打印实例时，调用父类Field的__str__方法
						                                                           # 因为字典是无序的，因此打印输出的时候也是无序的
						                                                           # 结果可能为：				
						                                                           # Found mapping: email ==> <StringField:email>
					                                                               # Found mapping: password ==> <StringField:password>
					                                                               # Found mapping: id ==> <IntegerField:uid>
					                                                               # Found mapping: name ==> <StringField:username>
						                mappings[k] = v # 将类属性项的键和值存储到 mappings字典中,此时的mappings如下
						                				# mappings={'id':IntegerField('id'),'name':StringField('username'),'email':StringField('email'),
						                				# 'password':StringField('password')}              
						        for k in mappings.keys(): # 用变量 k 遍历 mappings字典的所有类属性项的键   
						            attrs.pop(k) # 删除并弹出类（User）属性中和mappings字典同名的键--即删除该同名类属性
						            			 # 避免下一步将mappings字典保存在类（User）属性中时出现重复
						        attrs['__mappings__'] = mappings # 将mappings字典作为值存储在类（User）属性中，键为 '__mappings__'
						        attrs['__table__'] = name # 将name存储在类（User）属性中，键为 '__table__'，这里的name值为 User
						        return type.__new__(cls, name, bases, attrs) # 类创建或修改完毕，返回修改后的类
					以及基类Model：
						class Model(dict, metaclass=ModelMetaclass): # 创建 Model类，该类继承 dict类的所有功能并要通过 ModelMetaclass.__new__()来创建	
																	 # Model类只继承 dict类的所有功能，因为元类__new__()方法中排除了对Model类的修改			

						    def __init__(self, **kw): # 实例化属性，通过 __init__ 方法给实例绑定属性; 在创建实例的时候，不能传入
						                              # 空的参数，必须传入与__init__方法匹配的参数, 但self不需要传
						                              # Python解释器自己会把实例变量传进去
						                              # kw是关键字参数，kw接收的是一个dict
						        super(Model, self).__init__(**kw) # ？调用父类(dict)的实例化函数，这个类首先继承了dict类，所以会先调用dict的构造函数，
						                                          # 把attr都写到自己的属性里						

						    def __getattr__(self, key): # __getattr__()方法，动态返回一个属性或方法，只有在没有找到属性或方法的情况下，才调用__getattr__，
						                                # 已有的属性或方法，不会在__getattr__中查找。
						                                 
						        try:
						            return self[key]
						        except KeyError: # 注意到__getattr__默认返回就是None。要让class只响应特定的几个属性，我们就要按照约定，抛出AttributeError
						                         # 的错误
						            raise AttributeError(r"'Model' object has no attribute '%s'" % key)	# 创建的Model类实例（应用Model实例化函数创建）
						            																	# 中没有此属性					

						    def __setattr__(self, key, value): # __setattr__()方法，动态创建属性或方法，只有在没有找到类的属性或方法的情况下才创建新属性
						                                       # 或方法，已有的属性或方法，不会通过__setattr__创建
						        self[key] = value # 给key赋值value					
    											  # Model从dict继承，所以具备所有dict的功能，同时又实现了特殊方法__getattr__()和__setattr__()，因此又可以
    											  # 像引用普通字段那样写：
    											  # >>> user['id']
    											  # 12345
    											  # >>> user.id
    											  # 12345

						    def save(self): # 保存函数
						        fields = [] # 定义字段列表
						        params = [] # 定义参数列表
						        args = [] # 定义值列表
						        for k, v in self.__mappings__.items(): # 遍历User类实例的__mappings__属性（实例u,具备User类的属性）
						        									   # __mappings__属性值为
						                                               # mappings={'id':IntegerField('id'),'name':StringField('username'),'email':
						                                               # StringField('email'),'password':StringField('password')}  
						                				 
						            fields.append(v.name) # v是Field类的4个子类的实例，IntegerField('id')等
						            					  # v.name是子类实例的实例属性为name的值，即子类实例的参数值
						            					  # 分别可能是 'id'，'username'，'email'，'password'  
						            					  # 因为字典是无序的
						            params.append('?') # ？将？添加到params列表中，作为占位符
						            args.append(getattr(self, k, None)) # 根据__mappings__中的k值获取实例u属性dict中的value值并添加到args值列表中     
						        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params)) # 构建SQL语句
						        print('SQL: %s' % sql) # 打印sql
						        print('ARGS: %s' % str(args)) # 打印值
					当用户定义一个class User(Model)时，Python解释器首先在当前类User的定义中查找metaclass，如果没有找到，就继续在父类Model中
					查找metaclass，找到了，就使用Model中定义的metaclass的ModelMetaclass来创建User类，也就是说，metaclass可以隐式地继承到子类，
					但子类自己却感觉不到。
				在ModelMetaclass中，一共做了几件事情：
					1.	排除掉对Model类的修改；
					2.	在当前类（比如User）中查找定义的类的所有属性，如果找到一个Field属性，就把它保存到一个__mappings__的dict中，同时从类属性
						中删除该Field属性，否则，容易造成运行时错误（实例的属性会遮盖类的同名属性）；
					3.	把表名保存到__table__中，这里简化为表名默认为类名。
					在Model类中，就可以定义各种操作数据库的方法，比如save()，delete()，find()，update等等。
					我们实现了save()方法，把一个实例保存到数据库中。因为有表名，属性到字段的映射和属性值的集合，就可以构造出INSERT语句。
				编写代码试试：
					u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd')
					u.save()
					输出如下：
					Found model: User
					Found mapping: email ==> <StringField:email>
					Found mapping: password ==> <StringField:password>
					Found mapping: id ==> <IntegerField:uid>
					Found mapping: name ==> <StringField:username>
					SQL: insert into User (password,email,username,id) values (?,?,?,?)
					ARGS: ['my-pwd', 'test@orm.org', 'Michael', 12345]
					可以看到，save()方法已经打印出了可执行的SQL语句，以及参数列表，只需要真正连接到数据库，执行该SQL语句，就可以完成真正的功能。
					不到100行代码，我们就通过metaclass实现了一个精简的ORM框架。
			小结

					metaclass是Python中非常具有魔术性的对象，它可以改变类创建时的行为。这种强大的功能使用起来务必小心。
