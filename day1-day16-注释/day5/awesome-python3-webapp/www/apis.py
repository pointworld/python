#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

'''
JSON API definition.
'''

import json, logging, inspect, functools
        # json 模块--实现对象序列化，反序列化--str--更通用--能在不同的编程语言之间传递对象
                # json.dumps(对象)--把对象序列化为JSON标准格式--返回一个str，内容就是标准的JSON，然后写入文件
                # json.dump(对象)方法可以直接把JSON写入一个file-like Object
                # 如果我们要在不同的编程语言之间传递对象，就必须把对象序列化为标准格式
                # JSON表示出来就是一个字符串，可以被所有语言读取，也可以方便地存储到磁盘或者通过网络传输。
                # JSON不仅是标准格式，并且比XML更快，而且可以直接在Web页面中读取，非常方便。
                # JSON表示的对象就是标准的JavaScript语言的对象
        # logging 模块
        # inspect 模块
# 简单的几个api (应用程序界面) 错误异常类，用于跑出异常
class APIError(Exception): 
    # 定义APIError类，APIError类，父类为Exception，继承父类所有功能，基类为BaseException
    '''
    the base APIError which contains error(required), data(optional) and message(optional).
    '''
    def __init__(self, error, data='', message=''):
        # 实例化属性，通过 __init__ 方法给实例绑定属性在创建实例的时候，不能传入
        # 空的参数，必须传入与__init__方法匹配的参数, 但self不需要传
        # Python解释器自己会把实例变量传进去
        super(APIError, self).__init__(message) 
                    # 执行父类实例化函数
                    # Execption 类 --> BaseException 类 --> type 类 --> object 对象
                    # __init__(self, /, *args, **kwargs)
                    # Initialize self. 
        self.error = error # 给实例绑定error属性
        self.data = data # 给实例绑定data属性
        self.message = message # 给实例绑定message属性

class APIValueError(APIError):
    '''
    Indicate the input value has error or invalid. The data specifies the error field of input form.
    '''
    def __init__(self, field, message=''):
        super(APIValueError, self).__init__('value:invalid', field, message)

class APIResourceNotFoundError(APIError):
    '''
    Indicate the resource was not found. The data specifies the resource name.
    '''
    def __init__(self, field, message=''):
        super(APIResourceNotFoundError, self).__init__('value:notfound', field, message)

class APIPermissionError(APIError):
    '''
    Indicate the api has no permission.
    '''
    def __init__(self, message=''):
        super(APIPermissionError, self).__init__('permission:forbidden', 'permission', message)