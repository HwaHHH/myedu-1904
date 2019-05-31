

avar = 'hwa'

def v1():
    print(avar)

def v2():
    global avar
    avar = '真棒'
    print(avar)

if __name__ == '__main__':
    v1()
    v2()