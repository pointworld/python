'数据类型'
    数据
        计算机()顾名思义就是可以 做数学计算的机器()，因此，计算机程序理所当然地可以处理'各种数值'。但是，计算机能处理的远不止数值，
        还可以处理'文本、图形、音频、视频、网页等各种各样的数据'，不同的数据，需要定义不同的数据类型。在Python中，能够直接
        处理的数据类型有以下几种：

    class 整数():
    	各种进制数
    	...
    class 浮点数:
    	小数
    	...
    class 字符串:
    	字符串是以单引号''或双引号""括起来的'任意文本'
    	请注意，''或""本身只是一种表示方式，'不是字符串的一部分'
    	如果"'"本身也是一个字符，那就可以用""括起来 比如"I'm OK"
    	如果字符串内部既包含"'"又包含'"'怎么办？可以用转义字符 '\ '来标识 比如：'I\'m \"OK\"!'
    class 列表:    
    	定义
    	    列表 list 是一种有序的集合，可以随时添加和删除其中的元素。
    	    列表 list 中元素的数据类型可以不同，也可以是另一个 list
    	种类
    	    一维列表
    	    n 维列表
    	表示

    	    用 list=[] 表示，[] 内部用逗号分隔元素
    	操作
    	    访 通过索引访问元素
    	        可以用索引来访问list中每一个位置的元素，记得索引是从0开始的，要确保索引不要越界，
    	        最后一个元素的索引是 len(list) - 1，可以用 -1 作为索引，表示最后一个元素，并可以此类推用索引 0-i 获取倒数第 i 个元素
    	        如 list[i] 访问第 i+1 个元素 
            总 获取列表元素总个数	    
    	        用 len() 函数可以获得list元素的个数
    	        如 len(list) 获取列表中元素总个数
    	    添 向 list 中 追加元素到末尾（append）
    	        list是一个可变的有序表，所以，可以往list中追加元素到末尾
    	        list.append(element)  # 注意 element 的数据类型表示方法
    	    插 向 list 中 指定位置插入元素（insert）

    	        list.insert(i, element)  # i 为索引，element 为元素
    	    删 删除 list 元素（pop）
    	        list.pop() # 删除 list 中最后的一个元素并显示该元素
    	        list.pop(i) # i 为索引，删除索引为 i 的元素
    	    替 替换 list 中的某个元素

    	        list[i] = new_element # 直接将 新元素 赋值给对应的索引位置
    	    排 排序 list.sort()

    	        对于可变对象，比如list，对list进行操作，list内部的内容是会变化的，比如：
                    >>> a = ['c', 'b', 'a']
                    >>> a.sort()
                    >>> a
                    ['a', 'b', 'c']
    	    
    	    问题

    	        如何操作多维 list 中的元素
    class 元组:
    	定义
    	    
    	    另一种有序列表叫元组：tuple。tuple 和 list 非常类似，但是 tuple 一旦初始化就不能修改
    	种类
    	    一维元组
    	    n 维元组
    	表示
    	    用 tuple=() 表示，() 内部用逗号分隔元素
    	    一个元素的表示方法， tuple=(element,) # 只有1个元素的tuple定义时必须加一个逗号
    	        要定义一个只有1个元素的tuple，如果你这么定义：
                >>> t = (1)
                >>> t
                1
                定义的不是tuple，是1这个数！这是因为括号()既可以表示tuple，又可以表示数学公式中的小括号，这就产生了歧义，因此，
                Python规定，这种情况下，按小括号进行计算，计算结果自然是1。
                所以，只有1个元素的tuple定义时必须加一个逗号,，来消除歧义：
                >>> t = (1,)
                >>> t
                (1,)
                Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号。
    	操作
    	    无 append(), insert() 这样的方法 # 当然也可以实现
    	    其他获取元素的方法和 list 一样
    	意义
    	    因为tuple不可变，所以代码更安全。
    	    如果可能，能用tuple代替list就尽量用tuple。
    	注意
    	    tuple 不可变是指 存储指向 不可变
    	        '可变的'tuple
                    >>> t = ('a', 'b', ['A', 'B'])
                    >>> t[2][0] = 'X'
                    >>> t[2][1] = 'Y'
                    >>> t
                    ('a', 'b', ['X', 'Y'])
                    这个tuple定义的时候有3个元素，分别是'a'，'b'和一个list。不是说tuple一旦定义后就不可变了吗？怎么后来又变了？
                    别急，我们先看看定义的时候tuple包含的3个元素：                 
                    当我们把list的元素'A'和'B'修改为'X'和'Y'后，tuple变为：             
                    表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，所以，
                    tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，
                    但指向的这个list本身是可变的！
                '不可变的' tuple    
                    理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。
                    即：tuple 中不能存在像 list 类的可变元素
    class 字典:    
    	定义
    	    dict 全称dictionary，在其他语言中也称为 map，使用键-值(key-value)存储，具有'极快的'查找速度 -- hash 算法实现
    	    一个 key 只能对应 一个 value
    	        why so fast to find
    	            '为什么dict查找速度这么快？'
    	            因为dict的实现原理和查字典是一样的。假设字典包含了1万个汉字，我们要查某一个字，一个办法是把字典从第一页往后翻，直到
    	            找到我们想要的字为止，这种方法就是在list中查找元素的方法，list越大，查找越慢。
                    
                    第二种方法是先在字典的索引表里（比如部首表）查这个字对应的页码，然后直接翻到该页，找到这个字。无论找哪个字，这种查
                    找速度都非常快，不会随着字典大小的增加而变慢。
                    
                    dict就是第二种实现方式，给定一个名字，比如'Michael'，dict在内部就可以直接计算出Michael对应的存放成绩的“页码”，也就
                    是95这个数字存放的内存地址，直接取出来，所以速度非常快。
                    你可以猜到，这种key-value存储方式，在放进去的时候，必须根据key算出value的存放位置，这样，取的时候才能根据key直接
                    拿到value。
        表示  
            用 dict={} 表示，内部元素以键值对 key:value 的形式表示，以逗号分隔不同的 键值对

        操作
            存
                dict[key]=value 
            取
                dict.get(key)
            判 判断 key 是否存在
                >>> d['Jack'] = 90
                >>> d['Jack']
                90
                >>> d['Jack'] = 88
                >>> d['Jack']
                88
                如果key不存在，dict就会报错：
                    >>> d['Thomas']
                    Traceback (most recent call last):
                      File "<stdin>", line 1, in <module>
                    KeyError: 'Thomas'
                要避免key不存在的错误，有两种办法，一是通过in判断key是否存在：
                    >>> 'Thomas' in d
                    False
                二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value：
                    >>> d.get('Thomas')
                    >>> d.get('Thomas', -1)
                    -1
                注意：返回None的时候Python的交互式命令行不显示结果
            删 pop(key)
                要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
                >>> d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
                >>> d.pop('Bob')
                75
                >>> d
                {'Michael': 95, 'Tracy': 85}
            注意
                请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

                和list比较，dict有以下几个特点：           
                1.	查找和插入的速度极快，不会随着key的增加而变慢；
                2.	需要占用大量的内存，内存浪费多。

                而list相反：
                1.	查找和插入的时间随着元素的增加而增加；
                2.	占用空间小，浪费内存很少。

                所以，dict是用空间来换取时间的一种方法。
                dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，'正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象'。
                这是'因为dict根据key来计算value的存储位置'，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个'通过key计算位置的算法称为哈希算法（Hash）。'
                '要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key'。而list是可变的，就不能作为key
    class 集合:
    	定义
    	    set 和 dict 类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在 set 中，没有重复的key且元素之间是无序的。
    	表示
    	    用 set=() 表示 # 要创建一个 set，需要提供一个 list 作为输入集合
    	    例：
                >>> s = set([1, 2, 3])
                >>> s
                {1, 2, 3}
                注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。
                重复元素在set中自动被过滤            ：
                >>> s = set([1, 1, 2, 2, 3, 3])
                >>> s
                {1, 2, 3}
        操作
            添 set.add(key) 
                通过 add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
                >>> s.add(4)
                >>> s
                {1, 2, 3, 4}
                >>> s.add(4)
                >>> s
                {1, 2, 3, 4}
            删 set.remove(key)
                通过 remove(key)方法可以删除元素：
                >>> s.remove(4)
                >>> s
                {1, 2, 3}
            交 & 、并 |
                set可以看成数学意义上的无序和无重复元素的集合，因此，两个 set 可以做数学意义上的交集、并集等操作：
                >>> s1 = set([1, 2, 3])
                >>> s2 = set([2, 3, 4])
                >>> s1 & s2
                {2, 3}
                >>> s1 | s2
                {1, 2, 3, 4}
                set和dict的唯一区别仅在于没有存储对应的value，但是，'set的原理和dict一样，所以，同样不可以放入可变对象'，因为无法判断两个可变对象
                是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。
    class 布尔值:
        定义
            布尔值 bool 和布尔代数的表示完全一致，一个布尔值只有 True、False 两种值，要么是 True，要么是 False，在Python中，可以直接用 True、False 表示
            布尔值（请注意大小写），也可以通过布尔运算计算出来
                >>> True
                True
                >>> False
                False
                >>> 3 > 2
                True
                >>> 3 > 5
                False
        bool 运算 and、or、not
            and 运算是与运算，只有所有都为 True，and 运算结果才是 True：
                >>> True and True
                True
                >>> True and False	
                False
                >>> False and False
                False
                >>> 5 > 3 and 3 > 1
                True
            or 运算是或运算，只要其中有一个为 True，or 运算结果就是 True：
                >>> True or True
                True
                >>> True or False
                True
                >>> False or False
                False
                >>> 5 > 3 or 1 > 3
                True
            not 运算是非运算，它是一个单目运算符，把 True 变成 False，False 变成 True：
                >>> not True
                False
                >>> not False
                True
                >>> not 1 > 2
                True
        应用
            布尔值经常用在条件判断中，比如：
            if age >= 18:
                print('adult')
            else:
                print('teenager')
    class 空值:    
    	定义

            None 空值是Python里一个特殊的值，用 None 表示。None 不能理解为 0，因为 0是有意义的，而 None 是一个特殊的空值。
        空值与布尔值的区别
                进行逻辑判断（比如if）时，Python当中等于 False 的值并不只有 False 一个，它也有一套规则。对于基本类型来说，基本上每个类型都存在一个值
                会被判定为 False。大致是这样：
                    布尔型，False 表示 False，其他为 True
                  	整数和浮点数，0表示 False，其他为 True
                  	字符串和类字符串类型（包括bytes和unicode），空字符串表示 False，其他为 True
                  	序列类型（包括 tuple，list，dict，set 等），空表示 False，非空表示 True
                  	None 永远表示 False
                自定义类型则服从下面的规则：
                    1.	如果定义了 __nonzero__()方法，会调用这个方法，并按照返回值判断这个对象等价于True还是False
                    2.	如果没有定义 __nonzero__()方法但定义了 __len__()方法，会调用 __len__()方法，当返回 0时为 False，否则为 True（这样就跟内置类型为空时对应 False 相同了）
                    3.	如果都没有定义，所有的对象都是 True，只有 None 对应 False                            
                    
                    所以回到问题，not None 的确会返回 True。不过一定要警惕的是，if a is None 和 if a，if a is not None 和 if not a 不可以随便混用，前面也说过了，
                    它们在很多时候是不同的，比如说当a是一个列表的时候if not a其实是判断a为 None 或者为空。

'数据操作'

    转义字符
                转义字符'\ '可以转义很多字符，比如
                        '\n'表示换行，  为了简化，Python允许用'''...'''的格式表示多行内容
                        '\t'表示制表符，
                        若字符'\ '本身也要转义，用'\\'表示的字符就是'\ '
                r''表示''内部的字符串默认不转义, 但最后一个"'"前不能出现'\ '
                r''''''表示''' '''内部的字符串默认不转义, 但最后一个"'''"前不能出现'\ '
    格式化数据
                格式化的字符串输出(用%实现):
                常见的占位符有:
                           %d   整数
                           %f    浮点数
                           %s    字符串
                           %x   十六进制整数
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

'数据类型转换' 
    >>> int('123')
    123
    >>> int(12.34)
    12
    >>> float('12.34')
    12.34
    >>> str(1.23)
    '1.23'
    >>> str(100)
    '100'
    >>> bool(1)
    True
    >>> bool('')
    False
