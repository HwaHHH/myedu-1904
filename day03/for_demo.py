
def for_demo():
    for i in range(5):
        print('Hello World')
        print(i)

def for_demo1():
    for i in range(5,20,3):
        print(i)
    for i in range(20,5,-4):
        print(i)

def for_demo2():
    alist=['h','w','a',1,3,85,7]
    for i in alist:
        print(i)

    for i in range(len(alist)):
        print(alist[i])

def for_for():
    for i in range(8):
        print('再见')
        for j in range(3):
            print('好的',end=',')
        print('\n')

if __name__ == '__main__':
    for_for()