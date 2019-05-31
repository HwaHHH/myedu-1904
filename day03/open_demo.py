def open_write():
    a = open('test.text','w+')
    for i in range(3):
        a.write('bilibili\n')

if __name__ == '__main__':
    open_write()