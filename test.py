'''
Author: Gang Hu
Personal Email: huyingguo2007@hotmail.com
Work/School Email: ghu3@ur.rochester.edu
Date: 2024-08-25 02:00:29
LastEditTime: 2024-09-05 16:04:39
LastEditors: Gang Hu
FilePath: \Packages\test.py
Description: 
'''
def greeting(name: str, excited: bool = False) -> str:
    '''
    description: The function takes a name and an optional boolean argument, excited, which defaults to False. It should return a greeting message. If excited is True, the message should be in all caps and end with three exclamation marks. Otherwise, it should end with a period.
    param {str} name is the name of the person to greet
    param {bool} excited is a flag indicating whether to be excited
    return {*} a greeting message
    '''
    
    message = 'Hello, {}'.format(name)
    if excited:
        message += '!!!'
    return message


def does_not_return_square(x):
    '''
    description: The function does not return anything
    '''
    x * x

def f():
    n = 2
    # breakpoint()
    # print([x for x in range(10) if x % n == 0])
    exec('print([x for x in range(10) if x % n == 0])')

# def f():
#     n = 2

#     def g(it):
#         lst = []
#         for x in it:
#             if x % n == 0:
#                 lst.append(x)
#         return lst
#     print(g(range(10)))


if __name__ == '__main__':
    # does_not_return_square(5)
    # print(does_not_return_square(5))
    f()