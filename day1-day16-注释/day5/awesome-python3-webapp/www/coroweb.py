#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''在正式开始Web开发前，我们需要编写封装一个Web框架
    aiohttp已经是一个Web框架了，为什么我们还需要自己封装一个？原因是从使用者的角度来说，aiohttp相对比较底层
    编写一个URL的处理函数需要这么几步：
    第一步，编写一个用@asyncio.coroutine装饰的函数：
    @asyncio.coroutine
    def handle_url_xxx(request):
        pass
    第二步，传入的参数需要自己从request中获取：
    url_param = request.match_info['key']
    query_params = parse_qs(request.query_string)
    最后，需要自己构造Response对象：
    text = render('template', data)
    return web.Response(text.encode('utf-8'))
    这些重复的工作可以由框架完成
'''

__author__ = 'Michael Liao'

import asyncio, os, inspect, logging, functools
from urllib import parse
from aiohttp import web
from apis import APIError

# 模块信息
        # asyncio 模块 -- 异步IO
        # os 模块
        # inspect 模块 -- 用于检查运行模块的一些基本信息
                                # inspect模块 涨姿势了，把函数查了一遍户口本，这就是自省吧。
                                # inspect - Get useful information from live Python objects.
                                # This module encapsulates the interface provided by the internal special
                                # attributes (co_*, im_*, tb_*, etc.) in a friendlier fashion.
                                # It also provides some help for examining source code and class layout.
        # logging 模块 -- 记录或输出信息
        # functools 模块 -- 高阶函数模块, 为高阶函数提供支持，提供常用的高阶函数, 如wraps
        # urllib 模块 -- 操作URL--利用程序去执行各种HTTP请求--抓取URL内容
                                # urllib.parse - Parse (absolute and relative) URLs   
                                # NAME  urllib
                                #                
                                # PACKAGE CONTENTS
                                # error
                                # parse
                                # request
                                # response
                                # robotparser
        #urllib.parse -- 从urllib导入解析模块
        # aiohttp 模块 -- Web框架使用了基于asyncio的aiohttp，这是基于协程的异步模型
        # apis 模块 -- #导入自定义的api错误模块，简单的错误异常处理

# ======================定义@get/post装饰器--给http请求添加请求方法和请求路径属性================================

# @get/post装饰器函数，在handlers模块中被引用，其作用是给http请求添加请求方法和请求路径这两个属性 

            # 装饰器实质 -- 接受被装饰的函数作为装饰器函数中的参数，执行装饰器函数

                        # 其实就是一个以函数为参数的函数。只不过用了一种比较优雅的方式 @
                        # 函数装饰器是一个函数，接受被装饰的函数作为参数，返回一个新的函数，其中的逻辑你可以随便加进去
                        # 调用被装饰的函数，执行的却是装饰器函数（装饰器内部可以调用被装饰的函数并在装饰器内部执行） 
            # 这是个三层嵌套的decorator（装饰器），目的是可以让decorator本身传入参数
# 将一个函数func映射为一个URL处理函数 
def get(path):
    '''
    Define decorator @get('/path')
    '''
    def decorator(func):
                        # python内置的functools.wraps装饰器作用是把原始函数func的__name__等属性复制到 wrapper()函数中，使装饰后的函数的__name__属性值保持不变
                        # 否则，有些依赖函数签名的代码执行就会出错。
                        # 该装饰器的作用是解决一些函数签名的问题
                        # 比如若没有该装饰器, wrapper.__name__将为"wrapper"
                        # 加了装饰器,wrapper.__name__就等于func.__name__                        
                        # 知道这个功能后，你可以视这句代码不存在，以便后续代码的理解

                        # functools.wraps(func) 指调用functools模块的wraps函数，wraps函数的参数是func函数
                        # @ 表示调用某个装饰器函数 
                        # @functools.wraps(func) 表示调用functools模块里的wraps(func)函数作为装饰器，该装饰器带有参数 func 
                                    # 装饰器不带参数
                                                # def a_d(func):
                                                #     def wrapper(*args, **kw):
                                                #         pass
                                                #         return func(*args, **kw)
                                                #     return wrapper
                                                # @a_d
                                                # def f:
                                                #     pass 
                                                # 等价于
                                                # def f:
                                                #   pass 
                                                # f = a_d(f)    
                                                # 调用f函数，执行的却是a_d函数
                                    # 装饰器带参数
                                                # def log(text):
                                                #     def decorator(func):
                                                #         @functools.wraps(func) # 把原始函数func的__name__等属性复制到 wrapper()函数中
                                                #         def wrapper(*args, **kw):
                                                #             pass
                                                #             return func(*args, **kw)
                                                #         return wrapper
                                                #     return decorator      
                                                # @log('execute')
                                                # def now():
                                                #     pass 
                                                # 等价于
                                                # now = log('execute')(now)
                                                # 调用now函数，执行的是log函数                                                
        @functools.wraps(func)
                        # 
                        # def wraps(wrapped,
                        #           assigned = WRAPPER_ASSIGNMENTS,
                        #           updated = WRAPPER_UPDATES):
                        #     """Decorator factory to apply update_wrapper() to a wrapper function
                        #        
                        #        Returns a decorator that invokes update_wrapper() with the decorated
                        #        function as the wrapper argument and the arguments to wraps() as the
                        #        remaining arguments. Default arguments are as for update_wrapper().
                        #        This is a convenience function to simplify applying partial() to
                        #        update_wrapper().
                        #     """
                        #     return partial(update_wrapper, wrapped=wrapped,
                        #                    assigned=assigned, updated=updated)        
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'GET'
                    # 请求方法
                    # 通过装饰器给函数func加上__method__属性, 用于表示http method
                    # wrapper.__method__ = func.__method__
                    # 即 func.__method__ = 'GET' 
        wrapper.__route__ = path   # 访问函数的属性通过getattr(func, '__route__', None) 方法
                    # 请求路径
                    # 通过装饰器给函数func加上__route__属性, 用于表示path
                    # wrapper.__route__ = func.__route__
                    # 即 func.__route__ = 'POST'
        return wrapper
    return decorator
                # 若用 @get('/path') 装饰器去装饰一个函数名为 foo 的函数
                # 即
                # @get('/path')
                # def foo():
                #     pass
                # 调用foo函数后，执行过程为
                # 执行 get('/path')(foo) 函数
                # 结果 foo函数就自带了 __method__ 和 __route__两个属性，即包含请求方法'GET'和请求路径'/path'
# 与@get类似
def post(path):
    '''
    Define decorator @post('/path')
    '''
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'POST'
        wrapper.__route__ = path
        return wrapper
    return decorator

# ======================下面五个函数是针对fn函数（即上面被装饰的func函数）的参数做一些处理（提取和判断）================================

# inspect模块的一些用法
            # # test
            # import inspect
            # def fn(a, b=0, *args, c=1, d, **kw):
            #     pass
            # a = inspect.signature(fn)
            # print("inspect.signature(fn) 是: %s" % a)
            # params  = a.parameters
            # print("signature.paramerters.parameters 是: %s" % params)
            # print('\n')
            # for name, param in params.items():
            #     print("signature.paramerters.parameters.items()返回的两个值分别是: %s和%s" % (name, param))
            #     ee = param.kind
            #     print("Parameter.kind属性是: %s" % ee)
            #     gg = param.default
            #     print("Parameter.default的值是: %s" % gg)
            # print("\n")
            # ff = inspect.Parameter.KEYWORD_ONLY
            # print("inspect.Parameter.KEYWORD_ONLY的值是: %s" % ff)

            # 结果：
            # inspect.signature(fn) 是: (a, b=0, *args, c=1, d, **kw)
            # signature.paramerters.parameters 是: OrderedDict([('a', <Parameter "a">), ('b', <Parameter "b=0">), ('args', <Parameter "*args">), ('c', <Parameter "c=1">), ('d', <Parameter "d">), ('kw', <Parameter "**kw">)])
            
            # signature.paramerters.parameters.items()返回的两个值分别是: a和a
            # Parameter.kind属性是: POSITIONAL_OR_KEYWORD
            # Parameter.default的值是: <class 'inspect._empty'>
            # signature.paramerters.parameters.items()返回的两个值分别是: b和b=0
            # Parameter.kind属性是: POSITIONAL_OR_KEYWORD
            # Parameter.default的值是: 0
            # signature.paramerters.parameters.items()返回的两个值分别是: args和*args
            # Parameter.kind属性是: VAR_POSITIONAL
            # Parameter.default的值是: <class 'inspect._empty'>
            # signature.paramerters.parameters.items()返回的两个值分别是: c和c=1
            # Parameter.kind属性是: KEYWORD_ONLY
            # Parameter.default的值是: 1
            # signature.paramerters.parameters.items()返回的两个值分别是: d和d
            # Parameter.kind属性是: KEYWORD_ONLY
            # Parameter.default的值是: <class 'inspect._empty'>            
            # signature.paramerters.parameters.items()返回的两个值分别是: kw和**kw
            # Parameter.kind属性是: VAR_KEYWORD
            # Parameter.default的值是: <class 'inspect._empty'>

            # inspect.Parameter.KEYWORD_ONLY的值是: KEYWORD_ONLY

# 返回函数fn的命名关键字参数且没有指定默认值
def get_required_kw_args(fn):
    args = [] # 定义一个空的list，用来储存fn的参数名
                # # test
                # import inspect
                # def fn(a, b=0, *args,c=1,d, **kw):
                #     pass
                # def get_required_kw_args(fn):
                #     args = []  
                #     params = inspect.signature(fn).parameters
                #     for name, param in params.items():
                #         if param.kind == inspect.Parameter.KEYWORD_ONLY and param.default == inspect.Parameter.empty:
                #             args.append(name)
                #     print('args= ', args)
                #     return tuple(args)
                # print(get_required_kw_args(fn))
                # 结果：
                # args=  ['d']
                # ('d',)    
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY and param.default == inspect.Parameter.empty:
            args.append(name)
    return tuple(args)
# 返回函数fn的命名关键字参数，不需要满足没有默认值这个条件
def get_named_kw_args(fn):
    args = []
                # # test
                # import inspect
                # def fn(a, b=0, *args,c=1,d, **kw):
                #     pass
                # def get_named_kw_args(fn):
                #     args = []
                #     params = inspect.signature(fn).parameters
                #     for name, param in params.items():
                #         if param.kind == inspect.Parameter.KEYWORD_ONLY:
                #             args.append(name)
                #     print(args)
                #     return tuple(args)
                # print(get_named_kw_args(fn))
                # 结果：
                # ['c', 'd']
                # ('c', 'd')
    params = inspect.signature(fn).parameters
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            args.append(name)
    return tuple(args)
# 判断fn函数是否有命名关键字参数，有返回 True，没有返回 None
def has_named_kw_args(fn):
    params = inspect.signature(fn).parameters
                # # test
                # import inspect
                # def fn(a, b=0, *args,c=1,d, **kw):
                #     pass
                # def has_named_kw_args(fn):
                #     params = inspect.signature(fn).parameters
                #     for name, param in params.items():
                #         if param.kind == inspect.Parameter.KEYWORD_ONLY:
                #             return True  
                # print(has_named_kw_args(fn))
                # 结果：
                # True    
    for name, param in params.items():
        if param.kind == inspect.Parameter.KEYWORD_ONLY:
            return True
# 判断fn函数是否有可变关键字参数，有返回 True，没有返回 None
def has_var_kw_arg(fn):
    params = inspect.signature(fn).parameters
                # # test
                # import inspect
                # def fn(a, b=0, *args, c=1, d, **kw):
                #     pass
                # def has_var_kw_arg(fn):
                #     params = inspect.signature(fn).parameters
                #     for name, param in params.items():
                #         if param.kind == inspect.Parameter.VAR_KEYWORD:
                #             return True
                # print(has_var_kw_arg(fn))
                # 结果：
                # True    
    for name, param in params.items():
        if param.kind == inspect.Parameter.VAR_KEYWORD:
            return True
# 判断fn的参数中是否有符合条件的request参数
def has_request_arg(fn):
    sig = inspect.signature(fn) # 这里之所以拆成两行，是因为后面raise语句要用到sig
    params = sig.parameters　　　　　
    found = False # 默认没有找到
    for name, param in params.items():
        if name == 'request': # 找到参数名为request的参数后把found设置为True
            found = True 
            continue 
                        # continue 语句(执行缩进语句块时，遇到 continue 则结束本轮循环，后续循环中的语句不会执行（注意是当前循环中的后续代码不是当前if语句块）直接开始下一轮循环)

                        # 这里的设计比较巧妙
                        # POSITIONAL_OR_KEYWORD 表示参数是位置参数和或默认参数类型，如fn(a), fn(a,b), fn(a=1), fn(a, b=1), fn(a=1,b=1) 皆符合条件（默认参数不能放在位置参数前面）

                        # ****
                        # 其实按POSITIONAL_OR_KEYWORD的词义来理解，该参数类型包括位置参数和关键字参数，位置可理解为占位或定位的意思，用占位来理解更贴切，即占几个位置
                        # 注意区别 占位参数(POSITIONAL)-- 可变占位参数(VAR_POSITIONAL)，关键字参数(KEYWORD)--命名关键字参数(KEYWORD_ONLY)--可变关键字参数(VAR_KEYWORD)
                        # 关键字参数可以认为是默认参数
                        # ****
                        
                        # 以上面对参数类型的解释为前提，我们来分析这里的具体情况
                                    # # test
                                    # import inspect,os,logging,functools
                                    # def fn0(a, b = 1, *args, **kw): # 不存在request参数 -- 返回 False
                                    #     pass
                                    # def fn1(a, request, *args, **kw): # 存在request且为占位参数，位置在最后 -- 返回 True
                                    #     pass
                                    # def fn2(a, request, c, *args, **kw): # 存在request且为占位参数，位置不在最后 -- 报错
                                    #     pass
                                    # def fn3(a, request, c = 3, *args, **kw): # 存在request且为占位参数，位置不在最后 -- 报错
                                    #     pass
                                    # def fn4(a, request = 1, *args, **kw): # 存在request且为关键字参数，位置在最后 -- 返回 True
                                    #     pass
                                    # def fn5(a, request = 1, b = 2, *args, **kw): # 存在request且为关键字数参，位置不在最后 -- 报错
                                    #     pass
                                    # def fn6(a, b = 1, *args,d, request, **kw): # 存在request且为命名关键字参数 -- 返回 True
                                    #     pass
                                    # def fn7(a, b = 1, *args, d, request, f,  **kw): # 存在request且为命名关键字参数 -- 返回 True
                                    #     pass
                                    # def fn8(a, b = 1,*args, d, request, f = 6, **kw): # 存在request且为命名关键字参数 -- 返回 True
                                    #     pass
                                    # def fn9(a, b = 1, *args, d, request = 5, **kw): # 存在request且为命名关键字参数 -- 返回 True
                                    #     pass
                                    # def fn10(a, b = 1, *args, d, request = 5, f = 6, **kw): # 存在request且为命名关键字参数 -- 返回 True
                                    #     pass
                                    # def has_request_arg(fn):
                                    #     sig = inspect.signature(fn)
                                    #     params = sig.parameters
                                    #     found = False
                                    #     for name, param in params.items():
                                    #         if name == 'request':
                                    #             found = True
                                    #             continue
                                    #         if found and (param.kind != inspect.Parameter.VAR_POSITIONAL and param.kind != inspect.Parameter.KEYWORD_ONLY and param.kind != inspect.Parameter.VAR_KEYWORD):
                                    #             raise ValueError('request parameter must be the last named parameter in function: %s%s' % (fn.__name__, str(sig)))
                                    #     return found
                                    # #print(has_request_arg(fn0)) #False
                                    # #print(has_request_arg(fn1)) #True
                                    # #print(has_request_arg(fn2)) #抛出错误
                                    # #print(has_request_arg(fn3)) #抛出错误
                                    # #print(has_request_arg(fn4)) #True
                                    # #print(has_request_arg(fn5)) #抛出错误
                                    # #print(has_request_arg(fn6)) #True
                                    # #print(has_request_arg(fn7)) #True
                                    # #print(has_request_arg(fn8)) #True
                                    # #print(has_request_arg(fn9)) #True
                                    # #print(has_request_arg(fn10)) #True                        
                        # 第一种情况 -- 函数fn参数中不存在参数名为request的参数，返回 found默认值 False                     
                        # 第二种情况 -- 函数fn参数中存在request参数且类型是POSITIONAL_OR_KEYWORD，若该参数位置不在POSITIONAL_OR_KEYWORD参数中的最后，抛出错误
                        # 第三种情况 -- 函数fn参数中存在request参数且类型是POSITIONAL_OR_KEYWORD，若该参数位置在POSITIONAL_OR_KEYWORD参数中的最后，则返回 True       
                        # 第四种情况 -- 函数fn参数中存在request参数且类型是VAR_POSITIONAL 或 KEYWORD_ONLY 或 VAR_KEYWORD，返回 True  

                        # 由于参数名具有唯一性，即同一个函数不能存在相同的参数名（如果存在会报错）
        if found and (param.kind != inspect.Parameter.VAR_POSITIONAL and param.kind != inspect.Parameter.KEYWORD_ONLY and param.kind != inspect.Parameter.VAR_KEYWORD):
            raise ValueError('request parameter must be the last named parameter in function: %s%s' % (fn.__name__, str(sig)))
    return found

# ==========定义RequestHandler类--请求处理器，用来封装一个URL处理函数（在handler模块中），定义了__call__()方法，因此可以将其实例视为函数=================

# 定义RequestHandler
    # RequestHandler顾名思义--请求处理器--处理URL的请求
    # URL的处理函数不一定是一个coroutine，因此我们用RequestHandler()来封装成一个URL处理函数
    # RequestHandler是一个类，由于定义了__call__()方法，因此可以将其实例视为函数。
    # RequestHandler目的就是分析URL函数需要接收的参数，和从request中获取必要的参数，调用URL函数，
    # 然后把结果转换为web.Response对象，这样，就完全符合aiohttp框架的要求：
    # 知道了__call__方法和__init__的区别，RequestHandler就是个普通类，没有什么特别的技巧  

    # 这个RequestHandler ，其实应该叫 RequestHandlerAdapter才对。  

    # 它是个适配器，它把用户自定义参数的各种奇形怪状handler适配成了标准的 handler(request)调用。
'''
    没有开发文档坑死人。  

    廖大的意思是想把URL参数和GET、POST方法得到的参数彻底分离。  

    GET、POST方法的参数必需是KEYWORD_ONLY
    URL参数是POSITIONAL_OR_KEYWORD
    REQUEST参数要位于最后一个POSITIONAL_OR_KEYWORD之后的任何地方    

    正确的写法是： 

    @get('/{template}/')
    async def home(template, *, tag='', page='1', size='10'):
        # 这里会传进去两个参数：template=bootstrap, tag=Refactoring
       pass
    如果有request参数，它可以放在template之后的任何地方，没有看错，就是这么随便。
   
    RequestHandler也可以把任何参数都变成self._func(**kw)的形式。那问题来了，那kw的参数到底要去哪里去获取呢？
    request.match_info的参数： match_info主要是保存像@get('/blog/{id}')里面的id，就是路由路径里的参数
    GET的参数： 像例如/?page=2
    POST的参数： api的json或者是网页中form
    request参数： 有时需要验证用户信息就需要获取request里面的数据
    说到这里应该很清楚了吧，RequestHandler的主要作用就是构成标准的app.router.add_route第三个参数
    '''
class RequestHandler(object):
    def __init__(self, app, fn):
                    # 实例化属性，通过 __init__ 方法给实例绑定属性; 在创建实例的时候，不能传入
                    # 空的参数了，必须传入与__init__方法匹配的参数, 但self不需要传
                    # Python解释器自己会把实例变量传进去        
        #私有属性绑定 -- 类似_xxx和__xxx这样的函数或变量是非公开的（private），'不应被外部模块引用'，只在模块内部使用
        self._app = app # _app属性绑定 -- app的值在app模块中的init(loop)函数中被处理和赋值
        self._func = fn # _func属性绑定 -- fn -- handler模块中被装饰器装饰的函数，也是上述参数被处理的函数
        # 以下即为上面定义的一些对fn函数参数进行处理的判断函数与获取函数
        self._has_request_arg = has_request_arg(fn)  # 绑定是否有符合条件的request参数
        self._has_var_kw_arg = has_var_kw_arg(fn)  # 绑定是否有可变关键字参数
        self._has_named_kw_args = has_named_kw_args(fn)  # 绑定是否有命名关键字参数
        self._named_kw_args = get_named_kw_args(fn)   # 绑定函数fn的所有命名关键字参数
        self._required_kw_args = get_required_kw_args(fn)  # 绑定函数fn中没有指定默认值的所有命名关键字参数
    
    # 一个类定义了__call__()方法，可以像调用函数一样调用其实例
    # 此处参数为request，可以参考flask模块中request的使用（from flask import request, 参考教程--使用Web框架）
    # request 源于 LocalProxy(builtins.object)--werkzeug.local--e:\unzip files\python\lib\site-packages\werkzeug\local.py
    async def __call__(self, request):
        # 这里RequestHandler类主要是对handler进行封装，获取request中传入的参数并传入handler中。
        kw = None # kw 默认为None，假设不存在可变关键字参数
        if self._has_var_kw_arg or self._has_named_kw_args:
        # 如果实例的_has_var_kw_arg属性（是否有可变关键字参数）或_has_named_kw_args（是否有命名关键字参数）属性有一个条件为真
            if request.method == 'POST': # 如果request的方法属性为 POST
                if not request.content_type: # content_type是request提交的消息主体类型，没有就返回 丢失消息主体类型 
                    return web.HTTPBadRequest('Missing Content-Type.')
                ct = request.content_type.lower() 
                            # 如果request的content_type属性存在，将其值全部小写后赋值给 变量 ct
                            # lower函数的作用是把字符串转化为小写
                if ct.startswith('application/json'): 
                            # 如果request.content_type（消息主体类型）的值开头为application/json，则说明request.content_type（消息主体类型）是个json对象
                            # application/json表示消息主体是序列化后的json字符串
                    params = await request.json() 
                                 # 用 json方法读取request信息，返回结果为一个字典类型  ??????
                                 # request.json方法的作用是读取request body, 并以json格式解码
                    if not isinstance(params, dict):  # 解码得到的参数不是字典类型, 返回提示信息
                        return web.HTTPBadRequest('JSON body must be object.')
                    kw = params # post, content type字段指定的消息主体是json字符串,且解码得到参数为字典类型的,将其赋给变量kw
                # 以下2种content type都表示消息主体是表单
                elif ct.startswith('application/x-www-form-urlencoded') or ct.startswith('multipart/form-data'):
                            # 如果request.content_type（消息主体类型）的值开头为application/x-www-form-urlencoded或multipart/form-data
                            # application/x-www-form-urlencoded或multipart/form-data表示消息主体是表单信息
                    params = await request.post() 
                                # request.post方法从request body读取POST参数,即表单信息,并包装成字典赋给kw变量
                                # 浏览器表单信息用post方法来读取
                    kw = dict(**params) # 这儿params不是dict，需要通过dict方法转化成dict，那params到底是什么？
                else: # post的消息主体既不是json对象，又不是浏览器表单，那就只能返回不支持该消息主体类型
                    return web.HTTPBadRequest('Unsupported Content-Type: %s' % request.content_type)
            # http method 为 get的处理
            if request.method == 'GET': # 如果request的方法属性为 GET
                qs = request.query_string 
                            # 获取请求字符串并赋值给变量 qs
                            # request.query_string表示url中的查询字符串
                            # GET 请求的url 一般会附带查询字符串信息
                            # 比如"https://www.google.com/#newwindow=1&q=google",其中q=google就是query_string                  
                if qs: # 如果存在查询字符串
                    kw = dict() # 原来为None的kw变成字典
                    for k, v in parse.parse_qs(qs, True).items(): 
                                # 解析字符串后用for循环迭代
                                # >>> help(parse.parse_qs)
                                # Help on function parse_qs in module urllib.parse:
                                # parse_qs(qs, keep_blank_values=False, strict_parsing=False, encoding='utf-8', errors='replace')
                                #     Parse a query given as a string argument.  
                                #     Arguments:  
                                #     qs: percent-encoded query string to be parsed 
                                #     keep_blank_values: flag indicating whether blank values in
                                #         percent-encoded queries should be treated as blank strings.
                                #         A true value indicates that blanks should be retained as
                                #         blank strings.  The default false value indicates that
                                #         blank values are to be ignored and treated as if they were
                                #         not included.   
                                #     strict_parsing: flag indicating what to do with parsing errors.
                                #         If false (the default), errors are silently ignored.
                                #         If true, errors raise a ValueError exception.
                                #     encoding and errors: specify how to decode percent-encoded sequences
                                #         into Unicode characters, as accepted by the bytes.decode() method.                    
                        kw[k] = v[0] 
                                    # 把解析出来的结果存入kw
                                    # k和v 循环的结果各自用一个元组表示，每次循环k和v都只有一个元素
                                    # v[0] 即表示元组v 的第一个元素，kw[k] 表示字典kw键为k的值
                                    # 这里将 v[0] 的值赋值给 kw[k]，即用字典kw来储存解析结果
        # 如果没有在GET或POST中取得参数，直接把match_info的所有参数提取到kw
        if kw is None: #经过以上步骤，如果kw为空
            kw = dict(**request.match_info) # 直接把request中的match_info的所有参数提取到kw
        else: # 如果kw不为None
            # 如果不存在可变关键字参数和存在命名关键字参数，把所有命名关键字参数提取出来 
            if not self._has_var_kw_arg and self._named_kw_args:
                # remove all unamed kw:
                copy = dict()
                for name in self._named_kw_args: # 用name变量循环遍历由命名关键字参数名组成的tuple
                    # self._named_kw_args的值是一个 tuple（即get_named_kw_args(fn)函数的返回值）
                    if name in kw: # 如果有命名关键字参数名和kw字典（经POST和GET条件处理后得到）中的键重复
                        copy[name] = kw[name] # 则将kw字典中对应键的值 赋值 给另一个空字典cope中的键
                kw = copy # 即将kw字典中存在键和命名关键字参数名相同的项储存到另一个字典中
            # check named arg:
            # 把match_info的参数提取到kw，检查URL参数和HTTP方法得到的参数是否有重合
            for k, v in request.match_info.items(): # 循环遍历request.match_info中的所有参数
                if k in kw: # 如果request.match_info中的键名存在于kw字典中，发出重复参数警告
                    logging.warning('Duplicate arg name in named arg and kw args: %s' % k)
                kw[k] = v  # 用math_info中的值覆盖kw中的原值
        # 若存在符合条件的request参数, 则把request参数提取到kw        
        if self._has_request_arg:
            kw['request'] = request # 如果有request参数，就把这个参数存入kw
        # check required kw:
        # 若存在有未指定默认值的命名关键字参数, 且参数名未在kw中,返回丢失参数信息
        if self._required_kw_args:
            for name in self._required_kw_args:
                if not name in kw: # kw必须包含全部未指定默认值的命名关键字参数，如果发现遗漏则说明有参数没传入
                    return web.HTTPBadRequest('Missing argument: %s' % name)
        logging.info('call with args: %s' % str(kw))
        # 以上过程即为从request中获得必要的参数=====================================

        # 以下调用handler处理,并返回response.=======================================
        try:
            r = await self._func(**kw)
            return r
        except APIError as e:
            return dict(error=e.error, data=e.data, message=e.message)
#
    # add_static是用户处理如图片、js、css等静态资源的，仅供开发环境中方便使用，生产环境一般
    # 使用nginx或CDN之类的，
    # 这块我也还没有搞清楚，没办法梳理
#向app中添加静态文件目录，app = web.Application   
def add_static(app):
    # os.path.abspath(__file__), 返回当前脚本的绝对路径(包括文件名)
    # os.path.dirname(), 去掉文件名,返回目录路径
    # os.path.join(), 将分离的各部分组合成一个路径名
    # 因此以下操作就是将本文件同目录下的static目录(即www/static/)加入到应用的路由管理器中    
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
    app.router.add_static('/static/', path)
    logging.info('add static %s => %s' % ('/static/', path))

# 再编写一个add_route函数，用来注册一个URL处理函数
        # 将处理函数注册到app上
        # 处理将针对http method 和path进行
def add_route(app, fn):
    method = getattr(fn, '__method__', None) # 获取fn.__method__属性,若不存在将返回None
    path = getattr(fn, '__route__', None)  # 同上，这里是路径属性
    # http method 或 path 路径不存在, 将无法进行处理,因此报错
    if path is None or method is None:
        raise ValueError('@get or @post not defined in %s.' % str(fn))
    if not asyncio.iscoroutinefunction(fn) and not inspect.isgeneratorfunction(fn):
        fn = asyncio.coroutine(fn) # 如果函数即不是一个协程也不是生成器，那就把函数变成一个协程
    logging.info('add route %s %s => %s(%s)' % (method, path, fn.__name__, ', '.join(inspect.signature(fn).parameters.keys())))
    app.router.add_route(method, path, RequestHandler(app, fn)) #把函数注册到app
                # app 在同目录下的app.py中的init(loop)中
                # router = web_urldispatcher.UrlDispatcher() -- 源于 aiohttp.web.py 中的Appication类
                # add_route()和add_stastic()方法 -- 源于 aiohttp.web_urldisptcher.py中UrlDispatcher类
'''把多次add_route()注册的调用，变成自动扫描
    最后一步，把很多次add_route()注册的调用：  

    add_route(app, handles.index)
    add_route(app, handles.blog)
    add_route(app, handles.create_comment)  

    变成自动扫描： 

    自动把handler模块的所有符合条件的函数注册了:
    add_routes(app, 'handlers')
    add_routes()定义如下：
    '''
# 将handlers模块中所有请求处理函数提取出来交给add_route去处理
def add_routes(app, module_name):
    #因为handlers模块在当前目录下，所以在app.py中传入的module_name是handlers
    #假设handlers模块在handler目录下，那传入的module_name就是handler.handlers        
    n = module_name.rfind('.') # n 记录模块名中最后一个 . 的位置
    if n == (-1): #-1表示没有找到，说明模块在当前目录下，直接导入
        mod = __import__(module_name, globals(), locals())
        # __import__()的作用同import语句,python官网说强烈不建议这么做
        # __import__(name, globals=None, locals=None, fromlist=(), level=0)
        # name -- 模块名
        # globals, locals -- determine how to interpret the name in package context
        # fromlist -- name表示的模块的子模块或对象名列表
        # level -- 绝对导入还是相对导入,默认值为0, 即使用绝对导入, 正数值表示相对导入时,导入目录的父目录的层数        
    else:
        name = module_name[n+1:] # 当module_name为handler.handlers时，[n+1:]就是取.后面的部分，也就是handlers
        mod = getattr(__import__(module_name[:n], globals(), locals(), [name]), name) 
        # 以下语句表示, 先用__import__表达式导入模块以及子模块
        # 再通过getattr()方法取得子模块名, 如datetime.datetime
        # 这就是这种情况下导入handlers模块的方式，我也不是很懂
    
    for attr in dir(mod): #dir (mod)应该是mod的所有属性，然后通过for循环来遍历
        if attr.startswith('_'): 
        # 忽略以_开头的属性与方法,_xx或__xx或__xx__(前1或2个下划线)指示方法或属性为私有的, __xx__指示为特殊变量
        # 私有的,能引用(python并不存在真正私有),但不应引用;特殊的,可以直接应用,但一般有特殊用途            
        # 以下划线开头，则不是我们想要的，直接跳过进入下一个循环
            continue
        fn = getattr(mod, attr) # 排除私有和特殊属性后，就把其他属性提取出来
        if callable(fn): # 查看提取出来的属性是不是函数
            # 如果fn是函数
            # 获取fn的__method__属性与__route__属性并提取出来 
            # 此脚本开头的@get与@post装饰器就为fn加上了__method__与__route__        
            method = getattr(fn, '__method__', None)
            path = getattr(fn, '__route__', None)
            # if isinstance(fn, types.FunctionType) and hasattr(fn, '__method__') and hasattr(fn, '__route__'):
            if method and path: # 如果是函数，有__method__和__route__属性
                add_route(app, fn) # 就这样一层一层地把请求处理函数给筛选出来，然后交给add_route去处理
'''最后，在app.py中加入middleware、jinja2模板和自注册的支持：

    app = web.Application(loop=loop, middlewares=[
        logger_factory, response_factory
    ])
    init_jinja2(app, filters=dict(datetime=datetime_filter))
    add_routes(app, 'handlers')
    add_static(app)

    middleware是一种拦截器，一个URL在被某个函数处理前，可以经过一系列的middleware的处理。  

    一个middleware可以改变URL的输入、输出，甚至可以决定不继续处理而直接返回。middleware的用处就
    在于把通用的功能从每个URL处理函数中拿出来，集中放到一个地方。例如，一个记录URL日志的logger可
    以简单定义如下：    

    @asyncio.coroutine
    def logger_factory(app, handler):
        @asyncio.coroutine
        def logger(request):
            # 记录日志:
            logging.info('Request: %s %s' % (request.method, request.path))
            # 继续处理请求:
            return (yield from handler(request))
        return logger
    而response这个middleware把返回值转换为web.Response对象再返回，以保证满足aiohttp的要求：  

    @asyncio.coroutine
    def response_factory(app, handler):
        @asyncio.coroutine
        def response(request):
            # 结果:
            r = yield from handler(request)
            if isinstance(r, web.StreamResponse):
                return r
            if isinstance(r, bytes):
                resp = web.Response(body=r)
                resp.content_type = 'application/octet-stream'
                return resp
            if isinstance(r, str):
                resp = web.Response(body=r.encode('utf-8'))
                resp.content_type = 'text/html;charset=utf-8'
                return resp
            if isinstance(r, dict):
'''
"""
有了这些基础设施，我们就可以专注地往handlers模块不断添加URL处理函数了，可以极大地提高开发效率。            

RequestHandler
                        发表于 2016年6月19日

                        web框架
                        现在写的这个博客是采用MVC框架，也就是 Model-View-Controller （模型-视图-控制器），day5的主要任务
                        是建立View（网页）和Controller（路由）之间的桥梁。具体的方法就是通过request（请求）来达到交互的
                        目的。web框架会把Controller的指令构造成一个request发送给View，然后动态生成前端面页；用户会在前端
                        页面进行某些操作，然后通过request传送回后端，在传回后端之前会经过对request的解析，转变成后端可以
                        处理的事务。day5就是要对这些request进行标准化处理的实现。只有清楚理解了这一点才能更好重构我们的代码。

                        response_factory
                        虽然response_factory是完全没有必要重构的，但也要特别拿出来说一下，它和其他的factory装饰器都不同，它
                        是把Controller（路由）的各种处理结果转化成一个标准HTTP request（请求）的工厂函数。如果不写
                        response_factory的话，所有的 request（请求）都必须在Controller（路由）创建，为了省去很多不必要的麻烦，
                        才写了 response_factory ，Controller（路由）只负责发出指令，而 response_factory负责把指令统一生成 
                        request（请求）。

                        RequestHandler
                        如果说response_factory是Controller（路由） → View（网页）的桥梁，那RequestHandler就是View（网页）
                         → Controller（路由）的桥梁了，它也是day5重构的重点。先来看看RequestHandler具体要实现什么功能。

                        获取Controller（路由）所需的参数列表
                        把 request（请求）携带的数据解析成Controller（路由）的参数
                        检查解析的参数是否正确
                        最后把参数传送给Controller（路由）
                        原来的代码过于复杂，我就不一一贴出来了，我只是想讲讲我为何要这么重构RequestHandler，原来的代码并不需
                        要写这些复杂，我并不认同前置验证会比后置验证更加高级，而且有一些验证是根本不合理的。只要能顺利实现上
                        面四点要求，基本怎么实现都可以的。


                        获取参数表

                        获取Controller（路由）所需的参数列表是非常简单的事情，一行代码的事就不多说了。

                        # 获取函数的参数表
                        required_args = inspect.signature(self._func).parameters
                        重中之重就是把 request数据解析成Controller要求的参数然后检查解析的参数的正确性，因为这两步基本是相辅
                        相成的，我没有办法把它们分开讲，为什么这么重要？因为处理得不好，很容易产生被黑客攻击的漏洞。发生 
                        request（请求）并不是浏览器的专利，如果是稍微懂编程语言的人，构造一个不例规的 request（请求）是一件轻
                        而易举的事情，所以这两点一定要处理好。



                        参数来源

                        先看看一个 Controller（路由）要求的参数有哪些， 主要有三个来源：

                        网页中的GET和POST方法（比如获取/?page=10，还有json或form的数据。）
                        request.match_info（比如获取@get('/api/{table}')装饰器里面的参数）
                        def __call__(self, request)（获取request参数）
                        顺序能变吗？不能！你若读过我的代码，就会发现我重构之后的代码和廖老师在获取参数的顺序都是一致的，只不
                        过我简化了逻辑泥团，将事先检验改成事后检验而已。
                        最容易改变，或者说最容易被用户操纵的就是GET和POST方法的参数，万一你已经获取了request.match_info和
                        request的参数，用户只要网址后面加入/?table=users&request=XXX就可以轻易替换你原本的参数，所以，网页GET
                        和POST的参数必须最先加入参数字典的，request.match_info的参数取于url相对比较难修改，但request应该是最迟
                        才获取的，这点非常重要！只要你明白这个逻辑，代码可以重构得非常清爽。

                        # 获取从GET或POST传进来的参数值，如果函数参数表有这参数名就加入
                        kw = {arg: value for arg, value in request.__data__.items() if arg in required_args}

                        # 获取match_info的参数值，例如@get('/blog/{id}')之类的参数值
                        kw.update(dict(**request.match_info))

                        # 如果有request参数的话也加入
                        if 'request' in required_args:
                            kw['request'] = request


                        统一解析request数据

                        其中GET和POST的数据获取，我写一个data_factory去处理，本来廖老师也有写了这个工厂函数，但不知道为什么没
                        有用上，那真是可惜。 这个data_factory的主要功能就是把GET和POST的数据绑定在request.__data__上。

                        async def data_factory(app, handler):
                            async def parse_data(request):
                                logging.info('data_factory...')
                                if request.method == 'POST':
                                    if not request.content_type:
                                        return web.HTTPBadRequest(text='Missing Content-Type.')
                                    content_type = request.content_type.lower()
                                    if content_type.startswith('application/json'):
                                        request.__data__ = await request.json()
                                        if not isinstance(request.__data__, dict):
                                            return web.HTTPBadRequest(text='JSON body must be object.')
                                        logging.info('request json: %s' % request.__data__)
                                    elif content_type.startswith(('application/x-www-form-urlencoded', 'multipart/form-data')):
                                        params = await request.post()
                                        request.__data__ = dict(**params)
                                        logging.info('request form: %s' % request.__data__)
                                    else:
                                        return web.HTTPBadRequest(text='Unsupported Content-Type: %s' % content_type)
                                elif request.method == 'GET':
                                    qs = request.query_string
                                    request.__data__ = {k: v[0] for k, v in parse.parse_qs(qs, True).items()}
                                    logging.info('request query: %s' % request.__data__)
                                else:
                                    request.__data__ = dict()
                                return await handler(request)
                            return parse_data


                        参数检查

                        只要统一获取得所有的参数的之后，检验参数变得非常简单，只要检查Controller（路由）要求的参数没有缺失就可
                        以了，如果所要求的参数没有获取而且这个参数是没有默认值的，就需要报错了。为什么不处理参数过多的情况？当
                        参数多过所求参数时，系统会自动报错的。

                        # 检查参数表中有没参数缺失
                        for key, arg in required_args.items():
                            # request参数不能为可变长参数
                            if key == 'request' and arg.kind in (arg.VAR_POSITIONAL, arg.VAR_KEYWORD):
                                return web.HTTPBadRequest(text='request parameter cannot be the var argument.')
                            # 如果参数类型不是变长列表和变长字典，变长参数是可缺省的
                            if arg.kind not in (arg.VAR_POSITIONAL, arg.VAR_KEYWORD):
                                # 如果还是没有默认值，而且还没有传值的话就报错
                                if arg.default == arg.empty and arg.name not in kw:
                                    return web.HTTPBadRequest(text='Missing argument: %s' % arg.name)


                        传参

                        最后就是简单传入参数给Controller（路由）即可。

                        logging.info('call with args: %s' % kw)
                        try:
                            return await self._func(**kw)
                        except APIError as e:
                            return dict(error=e.error, data=e.data, message=e.message)
                        RequestHandler的整个处理流程就是这样子了，重构完成后是否觉得整个逻辑都比较通顺了？下面是代码参考：

                        RequestHandler
                        data_factory
                        '''
                        '''
                        RequestHandler
                        我遇到的第二个难点就是RequestHandler，因为RequestHandler看起来是一个类，但又不是一个类，从本质上
                        来说，它是一个函数，那问题来了，这个函数的作用到底是什么呢？
                        如果大家有仔细看day2的hello world的例子的话，就会发现在那个index函数里是包含了一个request参数的，
                        但我们新定义的很多函数中，request参数都是可以被省略掉的，那是因为新定义的函数最终都是被RequestHandler
                        处理，自动加上一个request参数，从而符合app.router.add_route第三个参数的要求，所以说RequestHandler
                        起到统一标准化接口的作用。
                        接口是统一了，但每个函数要求的参数都是不一样的，那又要如何解决呢？得益于factory的理念，我们很容易
                        找一种解决方案，就如同response_factory一样把任何类型的返回值最后都统一封装成一个web.Response对象。
                        RequestHandler也可以把任何参数都变成self._func(**kw)的形式。那问题来了，那kw的参数到底要去哪里去获取呢？
                        request.match_info的参数： match_info主要是保存像@get('/blog/{id}')里面的id，就是路由路径里的参数
                        GET的参数： 像例如/?page=2
                        POST的参数： api的json或者是网页中form
                        request参数： 有时需要验证用户信息就需要获取request里面的数据
                        说到这里应该很清楚了吧，RequestHandler的主要作用就是构成标准的app.router.add_route第三个参数，还有
                        就是获取不同的函数的对应的参数，就这两个主要作用。只要你实现了这个作用基本上是随你怎么写都行的，当然
                        最好加上参数验证的功能，否则出错了却找不到出错的消息是一件很头痛的是事情。在这个难点的我没少参考同学
                        的注释，但觉得还是把这部分的代码太过复杂化了，所以我用自己的方式重写了RequestHandler，从老师的先检验
                        再获取转换成先获取再统一验证，从逻辑上应该是没有问题，但大幅度简化了程序。
                        参考代码：https://github.com/moling3650/mblog/blob/master/www/app/frame/__init__.py

                        如果method == 'GET'时，参数就是查询字符串，也就是request.query_string
                        如果method == 'POST'时，有两种可能，Ajax的json和html的form(表单)，分别对应request.json()和
                        request.post()。 data_factory的主要作用就是把这些参数统一绑定在request.__data__上。

                        流留66
                        Created at 2016-9-24 21:23, Last updated at 2016-9-24 21:23
                        在RequestHandler里，init是初始化用的，在生成实例的时候执行，而call是模拟()的调用，需要在实例上应用，在下面这句代码里:

                          app.router.add_route(method, path, RequestHandler(func))

                          RequestHandler这个类并没有创建实例，是不是意味着call并没有执行，在我的代码里貌似是这样的。
                          小白一只，卡在这里好几天了，希望能解决我的疑惑。。。

                        灰_手
                        Created at 2016-9-24 22:50, Last updated at 2016-9-24 22:50
                        你理解错了，RequestHandler(func)就是一个实例，只不过没有给它命名，最终会在factorys的response_factory调用。

                        r = await handler(request)
                        这里的request也就是__call__(request)的参数。

                        '''
                        >>> class Foo(object):
                            def __init__(self):
                                print('__init__executed')
                            def __call__(self):
                                print('__call__ executed')
                        >>> Foo()
                        __init__executed
                        <__main__.Foo object at 0x02F5D550>
                        >>> isinstance(Foo(),Foo)
                        __init__executed
                        True
                        >>> Foo()()
                        __init__executed
                        __call__ executed
                        >>> f=Foo()
                        __init__executed
                        >>> f()
                        __call__ executed
                        '''
                        '''
                        Handler 的文档
                        A request handler can be any callable that accepts a Request instance as its only argument and returns a 
                        StreamResponse derived (e.g. Response) instance:

                        def handler(request):
                            return web.Response()
                        A handler may also be a coroutine, in which case aiohttp.web will await the handler:

                        async def handler(request):
                            return web.Response()
                        add_route() also supports the wildcard HTTP method, allowing a handler to serve incoming requests on a 
                        path having any HTTP method:

                        app.router.add_route('*', '/path', all_handler)
                        我开始的时候就没用RequestHandler,就用上边文档里这种朴素的handler写法跑通了。
                        然后才加入RequestHandler,这样出问题的时候好定位。

                        上方文档里说了handler的要求，任何一个方法可以接收Request实例，能返回StreamResponse子类实例的都可以作为
                        handler用。

                        def foo_handler(request):
                            return web.Response()

                        就这样随手写一个就合格。
                        既然你理解_init__ 和__call__的区别
                        你不知道handler怎么跟RequestHandler(func)关联上的。

                        handler=RequestHandler(app,fn)
                        app.router.add_route(method,path,handler)
                        这不就联结起来了么？

                        你问handler为什么不执行？

                        那就得看你有没有认真抄代码了，可能前边代码的锅，你不能硬甩到handler上。
                        你多来点log，一步一步的分析下去，实战项目最难的就是这部分了。
                        '''
                        """
