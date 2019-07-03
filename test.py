# # https://www.cnblogs.com/konglinqingfeng/p/9687349.html
# from multiprocessing import Process
# import json
# import time
# from multiprocessing import  Lock
#
# def show(i):
#     with open('ticket') as f:
#         dic = json.load(f)#load直接打开文件, 不用read, loads操作字符串,需要read
#     print('余票: %s' % dic['ticket'])
#
# def buy_ticket(i,lock):
#     lock.acquire() ##拿到钥匙进门,其他进程阻塞, acqurie和release之间的代码只能被一个进程执行
#     with open('ticket') as f:
#         dic = json.load(f)#load直接打开文件, 不用read, loads操作字符串,需要read
#         time.sleep(0.1)
#     if  dic['ticket'] > 0 :
#         dic['ticket'] -=1
#         print('\033[32m%s买到票了\033[0m'%i) #console改为绿色
#     else:
#         print('\033[31m%s没有买到票了\033[0m'%i) #console改为红色
#     time.sleep(0.1)
#     with open('ticket', 'w') as f:
#         json.dump(dic,f) #修改json文件,减去被买去的票
#     lock.release() #释放钥匙
#
#
# def buy_ticket2(i):
#     with open('ticket') as f:
#         dic = json.load(f)#load直接打开文件, 不用read, loads操作字符串,需要read
#         # time.sleep(0.1)
#     if  dic['ticket'] > 0 :
#         dic['ticket'] -=1
#         print('\033[32m%s买到票了\033[0m'%i) #console改为绿色
#     else:
#         print('\033[31m%s没有买到票了\033[0m'%i) #console改为红色
#     # time.sleep(0.1)
#     time.sleep(2)
#     with open('ticket', 'w') as f:
#         json.dump(dic, f) #修改json文件,减去被买去的票
#
#
# if __name__ == '__main__':
#     # for i in range(10):
#     #     p = Process(target=show, args=(i,))
#     #     p.start()
#     # lock = Lock() #产生钥匙
#     # for i in range(10):
#     #     p = Process(target=buy_ticket, args=(i,lock))
#     #     p.start()
#     for i in range(10):
#         buy_ticket2(i)


# class C(object):
#     def __init__(self):
#         self._x = None
#
#     @property
#     def x(self):
#         """I'm the 'x' property."""
#         return self._x
#
#     @x.setter
#     def x(self, value):
#         assert value > 0
#         self._x = value
#
#     @x.deleter
#     def x(self):
#         del self._x
#
#
# c = C()
# c.x = 1
# print(c.x)


# class B:
#     @classmethod
#     def print_classname(cls):
#         print('Bob')
#
#     @staticmethod
#     def print_staticname():
#         print('my name is bob')
#
#     def print_name(self):
#         print('this name')
#
#
# b = B()
# b.print_classname()  # 调用类方法
# b.print_staticname()  # 调用静态方法
# b.print_name()  # 调用实例方法
# print(B.__dict__)  # 里面有实例方法、静态方法和类方法

# class A(object):
#     # 属性默认为类属性（可以给直接被类本身调用）
#     num = "类属性"
#
#     # 实例化方法（必须实例化类之后才能被调用）
#     def func1(self):  # self : 表示实例化类后的地址id
#         print("func1")
#         print(self)
#
#     # 类方法（不需要实例化类就可以被类本身调用）
#     @classmethod
#     def func2(cls):  # cls : 表示没用被实例化的类本身
#         print("func2")
#         print(cls)
#         print(cls.num)
#         cls().func1()
#
#     # 不传递传递默认self参数的方法（该方法也是可以直接被类调用的，但是这样做不标准）
#     def func3():
#         print("func3")
#         print(A.num)  # 属性是可以直接用类本身调用的
#
#
# # A.func1() 这样调用是会报错：因为func1()调用时需要默认传递实例化类后的地址id参数，如果不实例化类是无法调用的
# A.func2()
# print('-'*100)
# A.func3()


# def hi(name="yasoob"):
#     def greet():
#         return "now you are in the greet() function"
#
#     def welcome():
#         return "now you are in the welcome() function"
#
#     if name == "yasoob":
#         return greet
#     else:
#         return welcome
#
#
# a = hi()
# print(a)
from functools import wraps
#
#
# def a_new_decorator(a_func):
#     @wraps(a_func)
#     def wrapTheFunction():
#         print("I am doing some boring work before executing a_func()")
#
#         a_func()
#
#         print("I am doing some boring work after executing a_func()")
#
#     return wrapTheFunction
#
#
# @a_new_decorator
# def a_function_requiring_decoration():
#     """Hey you! Decorate me!"""
#     print("I am the function which needs some decoration to "
#           "remove my foul smell")
#
#
# a_function_requiring_decoration()
#
# print(a_function_requiring_decoration.__name__)


class Foo(object):
    def __init__(self, func):
        self._func = func

    def __call__(self):
        print('class decorator runing')
        self._func()
        print('class decorator ending')


@Foo
def bar():
    print('bar')


bar()
