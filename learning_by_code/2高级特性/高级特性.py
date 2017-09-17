但是在Python中，代码不是越多越好，而是越少越好。代码不是越复杂越好，而是越简单越好。
基于这一思想，我们来介绍Python中非常有用的高级特性，1行代码能实现的功能，决不写5行代码。
'请始终牢记，代码越少，开发效率越高。'

切片(slice)操作符
    定义
        访问和截取某集合中的元素，替代通过循环方式，获得该集合的子集
    表示
        [开始索引:结束索引:step]   
            第一个参数 表示开始索引
                开始索引为闭区间，若开始索引为第一个元素的索引 0时，可以省略
            第二个参数 表示结束索引
                最后一个索引可以表示为 -1
                结束索引为开区间，若结束索引为最后一个元素的索引 -1时，'可以省略，此时为闭区间'; '结束索引不省略则为开区间'，不会取出结束索引对应的元素
            第三个参数 表示截取方向'和或'截取间隔
                step 默认值为 1，从左往右依次取值，起点为开始索引，终点为结束索引
                step 值不为正整数且不为 1时，从左往右间隔 step 依次取值，起点为开始索引，终点为结束索引
                若 step值为 负整数时，从右往左间隔 step 依次取值，此时第二个参数为开始索引（开区间），第一个参数为结束索引（闭区间）
迭代(Iteration)-- for ... in 循环遍历
    定义
        如果给定一个可迭代对象(如 list 或 tuple)，我们可以通过 for ... in 循环来遍历这个可迭代对象(如 list 或 tuple)，这种遍历我们称为 迭代(Iteration)。
        Python中任何可迭代对象都可以作用于 for 循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用 for 循环
    如何判断一个对象是可迭代对象呢？方法是通过collections模块的Iterable类型判断：
        >>> from collections import Iterable
        >>> isinstance('abc', Iterable) # str是否可迭代
        True
        >>> isinstance([1,2,3], Iterable) # list是否可迭代
        True
        >>> isinstance(123, Iterable) # 整数是否可迭代
        False
    如果要对list实现类似Java那样的下标循环怎么办？Python内置的 enumerate 函数可以把一个 list 变成索引-元素对，这样就可以在 for 循环中同时迭代索引和元素本身：
        >>> for i, value in enumerate(['A', 'B', 'C']):
            print(i, value)
        0 A
        1 B
        2 C
    for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
        >>> for x, y in [(1, 1), (2, 4), (3, 9)]:
            print(x, y)
        1 1
        2 4
        3 9
列表生成式(List Comprehensions)
    定义
        
        即List Comprehensions，是Python内置的非常简单却强大的可以用来创建list的生成式。
    表示

        [表达式 for 表达式中的变量 in 可迭代对象 '... for 表达式中的变量 in 可迭代对象' 'if 条件'] # for 循环可以只有一个，if 条件可以省略
    作用

        用表达式中的变量 通过 for in 循环遍历 可迭代对象中的元素，将表达式作用于可迭代对象中的元素，返回一个新的列表
    例1：
            举个例子，要生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]可以用list(range(1, 11))：
            >>> list(range(1, 11))
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
            但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
            >>> L = []
            >>> for x in range(1, 11):
            ...    L.append(x * x)
            ...
            >>> L
            [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
            但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
            >>> [x * x for x in range(1, 11)]
            [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
            写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来，十分有用，多写几次，很快就可以熟悉这种语法。
            for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
            >>> [x * x for x in range(1, 11) if x % 2 == 0]
            [4, 16, 36, 64, 100]
            还可以使用两层循环，可以生成全排列：
            >>> [m + n for m in 'ABC' for n in 'XYZ']
            ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
            三层和三层以上的循环就很少用到了。
            运用列表生成式，可以写出非常简洁的代码。例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：
            >>> import os # 导入os模块，模块的概念后面讲到
            >>> [d for d in os.listdir('.')] # os.listdir可以列出文件和目录
            ['.emacs.d', '.ssh', '.Trash', 'Adlm', 'Applications', 'Desktop', 'Documents', 'Downloads', 'Library', 'Movies', 'Music', 
            'Pictures', 'Public', 'VirtualBox VMs', 'Workspace', 'XCode']
            for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
            >>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
            >>> for k, v in d.items():
            ...     print(k, '=', v)
            ...
            y = B
            x = A
            z = C
            因此，列表生成式也可以使用两个变量来生成list：
            >>> d = {'x': 'A', 'y': 'B', 'z': 'C' }
            >>> [k + '=' + v for k, v in d.items()]
            ['y=B', 'x=A', 'z=C']
            最后把一个list中所有的字符串变成小写：
            >>> L = ['Hello', 'World', 'IBM', 'Apple']
            >>> [s.lower() for s in L]
            ['hello', 'world', 'ibm', 'apple']
    例2：
        >>> tiangan = '甲乙丙丁戊己庚辛壬癸'
        >>> dizhi = '子丑寅卯辰巳午未申酉戌亥'
        >>> jiazi = [m + n for i,m in enumerate(tiangan) for j,n in enumerate(dizhi) if (i%2==1 and j%2==1) or (i%2==0 and j%2==0) ]
        >>> print(jiazi)
        ['甲子', '甲寅', '甲辰', '甲午', '甲申', '甲戌', '乙丑', '乙卯', '乙巳', '乙未', '乙酉', '乙亥', '丙子', '丙寅', '丙辰', '丙午', '丙申', 
        '丙戌', '丁丑', '丁卯', '丁巳', '丁未', '丁酉', '丁亥', '戊子', '戊寅', '戊辰', '戊午', '戊申', '戊戌', '己丑', '己卯', '己巳', '己未', 
        '己酉', '己亥', '庚子', '庚寅', '庚辰', '庚午', '庚申', '庚戌', '辛丑', '辛卯', '辛巳', '辛未', '辛酉', '辛亥', '壬子', '壬寅', '壬辰',
         '壬午', '壬申', '壬戌', '癸丑', '癸卯', '癸巳', '癸未', '癸酉', '癸亥']
        >>> 
生成器(generator)
    定义

        在Python中，这种一边循环一边计算的机制，称为生成器：generator。
    表示
        把一个列表生成式的'[]'改成'()'，就创建了一个generator
        如果一个函数定义中包含 yield 关键字，那么这个函数就不再是一个普通函数，而是一个generator
            yield 的作用就是把一个函数变成一个 generator，带有 yield 的函数不再是一个普通函数，Python 解释器会将其视为一个 generator。
    获取生成器的迭代值
        next(generator)
            通过 next()函数获得generator的下一个返回值，generator保存的是算法，每次调用 next(g) ，就计算出g的下一个元素的值，直到计算到最后
            一个元素，没有更多的元素时，抛出 StopIteration的错误。
        for 循环迭代

            创建了一个generator后，基本上永远不会调用next()，而是通过 for 循环来迭代它，因为generator也是可迭代对象, 并且不需要关心 StopIteration 的错误
    获取 return 语句的返回值
        next() 直到计算到最后一个元素，没有更多的元素时，抛出 StopIteration的错误，即 return 语句的返回值

        但是用 for 循环调用generator时，发现拿不到generator的 return 语句的返回值。如果想要拿到返回值，必须捕获 StopIteration 错误，返回值包含
        在 StopIteration 的 value 中
    生成器的执行流程

        generator和普通函数的执行流程不一样。

        函数是顺序执行

            遇到 return 语句或者最后一行函数语句就返回, 如果在 return 后返回一个值，那么这个值为 StopIteration 异常的说明，不是程序的返回值。
        生成器是调用执行
            而变成generator的函数，在每次调用 next()的时候执行，遇到 yield 语句返回，yield 后面的代码不被执行，再次执行时从上次返回的 yield 
            语句处继续执行。看起来就好像一个函数在正常执行的过程中被 yield 中断了数次，每次中断都会通过 yield 返回当前的迭代值。
    用法
        send()
                生成器函数最大的特点是可以接受外部传入的一个变量，并根据变量内容计算结果后返回。
                这是生成器函数最难理解的地方，也是最重要的地方，实现后面我会讲到的协程就全靠它了。
                def gen():
                    value=0
                    while True:
                        receive=yield value
                        if receive=='e':
                            break
                        value = 'got: %s' % receive                
                g=gen()
                print(g.send(None))     
                print(g.send('aaa'))
                print(g.send(3))
                print(g.send('e'))		
                执行流程：
                    1.	通过g.send(None)或者 next(g)可以启动生成器函数，并执行到第一个yield语句结束的位置。
                    此时，执行完了yield语句，但是没有给receive赋值。
                    yield value会输出初始值0
                    注意：在启动生成器函数时只能send(None),如果试图输入其它的值都会得到错误提示信息。
                    2.	通过g.send('aaa')，会传入aaa，并赋值给receive，然后计算出value的值，并回到while头部，执行yield value语句有停止。
                    此时yield value会输出"got: aaa"，然后挂起。
                    3.	通过g.send(3)，会重复第2步，最后输出结果为"got: 3"
                    当我们g.send('e')时，程序会执行break然后推出循环，最后整个函数执行完毕，所以会得到StopIteration异常。
                最后的执行结果如下：
                    0
                    got: aaa
                    got: 3
                    Traceback (most recent call last):
                    File "h.py", line 14, in <module>
                      print(g.send('e'))
                    StopIteration
        throw()    
            用来向生成器函数送入一个异常，可以结束系统定义的异常，或者自定义的异常。
            throw()后直接跑出异常并结束程序，或者消耗掉一个 yield，或者在没有下一个 yield 的时候直接进行到程序的结尾            
        yield from  生成器嵌套
            yield产生的函数就是一个迭代器，所以我们通常会把它放在循环语句中进行输出结果。
            有时候我们需要把这个yield产生的迭代器放在另一个生成器函数中，也就是'生成器嵌套'
    yield 关键字与 return 的区别
        生成器函数的核心是 yield 关键字。它最简单的调用形式看起来像一个 return 申明，不同之处在于普通 return 会返回值并终止函数的执行，
        而 yield 会返回一个值给循环调用此生成器的代码并且只是暂停执行生成器函数。

               

