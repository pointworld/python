#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Models for user, blog, comment.
'''

__author__ = 'Point'

import time, uuid
            # UUID--Universally Unique IDentifier，全局唯一标识符，uuid模块中的uuid.uuid()函数用来随机生成一个UUID 
            # UUID是128位的全局唯一标识符，通常由32字节的字符串表示
            # 它可以保证时间和空间的唯一性，也称为GUID，全称为：
                        # UUID —— Universally Unique IDentifier      Python 中叫 UUID
                        # GUID —— Globally Unique IDentifier          C#  中叫 GUID           
            # hex：指定32个字节的字符串以创建UUID对象
            # uuid4()--基于随机数，由伪随机数得到，有一定的重复概率，该概率可以计算出来，不涉及网络主机名，仅生成一个随机UUID，因此从隐私保护角度uuid4()更加安全。
            # uuid.uuid4().hex 即指定32个字节的字符串来随机生成一个UUID
     
            # uuid模块在Python 2.5以后引入，接口包括：不可变对象UUID（UUID类）和函数uuid1()、uuid3()、uuid4()和uuid5()，后面的四个函数用于生成 
            # RFC 4122 规范中指定的第1、3、4、5版UUID。使用uuid1()或uuid4()可以获得一个唯一的ID，uuid1()包含了主机的网络名称，uuid4()不涉及网络主机名，
            # 仅生成一个随机UUID，因此从隐私保护角度uuid4()更加安全。
from orm import Model, StringField, BooleanField, FloatField, TextField

def next_id():
        
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)
                # 这个id主要由当前时间戳和uuid.uuid4().hex产生的一个随机32位的字符串表示，已保证获得唯一id的效果

                # %015d 和 %s 为格式化数据的表示方法
                # %015d 表示一个15位的整数，位数不够在前面补0
                # %s永远起作用，它会把任何数据类型转换为字符串
                # time.time() 函数返回当前时间的时间戳(相对于1970.1.1 00:00:00以秒计算的偏移量)
                # uuid.uuid4().hex 即指定32个字节的字符串来随机生成一个UUID
                # 例
                            # import uuid, time

                            # print("time.time() 函数返回当前时间的时间戳(相对于1970.1.1 00:00:00以秒计算的偏移量)")
                            # print(time.time())
                            # print(time.time()*1000)
                            # print(int(time.time()*1000))

                            # print("%15d 和 %015d 的区别")
                            # print('%15d'%(int(time.time()*1000)))
                            # print('%015d'%(int(time.time()*1000)))

                            # print("uuid.uuid4()和uuid.uuid4().hex的区别")
                            # print(uuid.uuid4())
                            # print(uuid.uuid4().hex)

                            # print("'%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)最终结果：")
                            # print('%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex))

                            # 结果如下
                            # time.time() 函数返回当前时间的时间戳(相对于1970.1.1 00:00:00以秒计算的偏移量)
                            # 1488851212.4598403
                            # 1488851212464.8435
                            # 1488851212469

                            # %15d 和 %015d 的区别
                            #   1488851212483
                            # 001488851212489

                            # uuid.uuid4()和uuid.uuid4().hex的区别
                            # c67bf1e6-0b0f-4a32-a04c-c1955c05e254
                            # 88d35ca4a95446318dcd2c574b076955

                            # '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)最终结果：
                            # 0014888512125247bd3584bf1d24d53b3c5d1b1f60dc489000

# 这是一个用户名的表
class User(Model): # 该 User类继承自orm框架中的Model基类，Model基类又继承了 dict类和 Model元类
    # 定义User类的默认类属性，属性查找方式--由下到上查找对象树，实例属性和覆盖类属性，类属性会覆盖基类属性，但元类可以定制或修改类属性
    __table__ = 'users' # 表名为 users

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)') # 用户id
                # 在编写ORM时，给一个Field增加一个default参数可以让ORM自己填入缺省值，非常方便。并且，缺省值可以作为函数对象传入，在调用save()时自动计算
                # 主键id的缺省值是函数next_id
    email = StringField(ddl='varchar(50)') # 用户邮箱
    passwd = StringField(ddl='varchar(50)') # 用户密码
    admin = BooleanField() # 管理员，True表示该用户是管理员，否则不是
    name = StringField(ddl='varchar(50)') # 用户名
    image = StringField(ddl='varchar(500)') # 用户头像
    created_at = FloatField(default=time.time) # 用户创建时间
                # 创建时间默认是为当前时间
                # 创建时间created_at的缺省值是函数time.time，可以自动设置当前日期和时间
                # 日期和时间用float类型存储在数据库中，而不是datetime类型，这么做的好处是不必关心数据库的时区以及时区转换问题，排序非常简单，
                # 显示的时候，只需要做一个float到str的转换，也非常容易。

# 这是一个博客的表
class Blog(Model):
    __table__ = 'blogs'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)') # 作者id
    user_name = StringField(ddl='varchar(50)') # 作者名
    user_image = StringField(ddl='varchar(500)') # 作者上传的图片
    name = StringField(ddl='varchar(50)') # 文章名
    summary = StringField(ddl='varchar(200)') # 文章概要
    content = TextField() # 文章正文
    created_at = FloatField(default=time.time) # 文章创建时间

# 这是一个评论的表
class Comment(Model):
    __table__ = 'comments'

    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)') 
    blog_id = StringField(ddl='varchar(50)') # 博客id
    user_id = StringField(ddl='varchar(50)') # 评论者id
    user_name = StringField(ddl='varchar(50)') # 评论者名字
    user_image = StringField(ddl='varchar(500)') # 评论者上传的图片
    content = TextField() # 评论内容
    created_at = FloatField(default=time.time) # 评论时间 