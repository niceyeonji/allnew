import datetime

def datetime_deco(func):
    def decorated():
        print(datetime.datetime.now())
        func()
        print(datetime.datetime.now())
    return decorated

@datetime_deco
def func1():
    print("Main Function1 start")

@datetime_deco
def func2():
    print("Main Function2 start")

@datetime_deco
def func3():
    print("Main Function3 start")

func1()
func2()
func3()

