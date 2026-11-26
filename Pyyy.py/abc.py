
# try:
#     a=10
#     b=0
#     result=a/b
#     print(result)
# except:
#     print("somthing went wrong !")
# print("program completed ")

# print("welcome")
# try:
#     num=int(input("entre a number:"))
#     result=100 / num
#     print("result:",result)
# except valueError:
#     print("please entre valid number")
# except ZeroDivsionError:
#     print("you can not divided by zero")
# else:
#     print("program executed successfully")
# finally:
#     print("this is finally execute")


# age = 15
# try:
#     if age<18:
#         raise valueError("you must be 18 or older")
# catch:
#     print("access granted")
# Class invalideExp(try):


# try:
#     age=25
#     if age<18:
#         raise ValueError("age must be18 or older")
#     print("eligible")
# except ValueError as e:
#     print("error:",e)

# print("program completed")

# multiThreding

# import time
# def t1():
#     print("t1 start")
#     time.sleep(2)
#     print("t1 completed")

# def t2():
#     print("t2 start")
#     time.sleep(2)
#     print("t2 completed")

# import threading

# def greet():
#     print("hello from the thread")

# t1=threading.Thread(target=greet) #threding is module and thread is class
# t1.start()
# print("main program")
# def greet():
#     print("hello from the thread")

# t2=threading.Thread(target=greet) #threding is module and thread is class
# t2.start()
# print("main program")
# def greet():
#     print("hello from the thread")

# t3=threading.Thread(target=greet) #threding is module and thread is class
# t3.start()
# print("main program")

# import threading
# import time

# def task():
#     print("start")
#     time.sleep(2)
#     print("after waiting")
# t1=threading.Thread(target=task)
# t1.start()
# t1.join()
# print("completed")

# import threading

# def greet(*name,**age):
#     print("Name is", name)
#     print("age is:", age)


# t1 = threading.Thread(target=greet, args=("Aarav","28"))
# t1.start()
# t1.join()

#synchronization in lock

import threading 

counter =0

def incress_counter
