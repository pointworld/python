#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Configuration
'''

__author__ = 'Michael Liao'

import config_default

class Dict(dict): # 该类赋予了字典新的功能，能实现类似类属性 x.y 的取值方式操作字典中的键值
    '''
    Simple dict but support access as x.y style.
    '''
    def __init__(self, names=(), values=(), **kw):
        super(Dict, self).__init__(**kw)
        for k, v in zip(names, values):
            self[k] = v

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

def merge(defaults, override):   # 该函数是一个递归函数，负责将defaults内 存在与override重名的键 对应的值 用override对应的值覆盖，返回一个新的二元字典
    # default 和 override 这两个参数在这里是一个二元字典
    r = {}
    for k, v in defaults.items():
        if k in override:
            if isinstance(v, dict):
                r[k] = merge(v, override[k])
            else:
                r[k] = override[k]
        else:
            r[k] = v
    return r

# toDict的主要功能是添加一种取值方式a_dict.key，相当于a_dict['key']，这个功能不是必要的
# 从函数名字上就很清楚了，就是把从经过merge函数处理复写后的dict对象configs转变为文件中
# 从dict基类派生出的Dict类对象，从而实现xxx.key的取值功能
def toDict(d): # 该函数为地柜函数
    D = Dict() # 创建Dict类的实例 D
    for k, v in d.items(): # 用变量 k, v 遍历 参数 d 中的项（参数d 必须是一个字典）
        D[k] = toDict(v) if isinstance(v, dict) else v 
        # 如果 参数d中键对应的值v 类型是 字典，则将 v字典作为 toDict函数的参数执行 toDict(v) 函数，重复执行到v不是一个字典为止
    return D

configs = config_default.configs  # 将config_default模块中configs的值赋值给 configs变量

try: # 执行 try 语句块
    import config_override  # 引入config_override模块
    configs = merge(configs, config_override.configs) # 执行merge函数，将返回值赋值给 configs
except ImportError:
    pass

configs = toDict(configs) # 将try语句块中获得的结果 configs 作为 toDict函数的参数执行，赋值给变量 configs