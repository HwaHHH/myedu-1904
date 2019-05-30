

alist = ['是打发',2,'你好',6,7,1,3]

def list_sel():
    print(alist[::-1])
    print(alist[4:5])

def list_del():
    alist.pop(1)
    print(alist)

def list_add():
    alist.append('hwa')
    print(alist)

    clist = [7,8,9]
    alist.extend(clist)
    print(alist)

    alist.append(clist)
    print(alist)

def list_update():
    qlist=[5,6,9,2,4,8,0]
    print(qlist)
    qlist[2] = 200
    print(qlist)

def list_order_by():
    slist = [21,54,87,15,16,5,8,48]
    slist.sort()
    print(slist)

    slist.sort(reverse= True)
    print(slist)

def list_distinct():
    vlist = [8,8,9,5,5,4,8,7,2,1,6,5,4]
    vlist = set(vlist)
    print(vlist)

    vlist = list(set(vlist))
    print(vlist)
    print(len(vlist))

def list_work():
    zlist = [3,4,8,6,9]
    print(zlist[2])

    print(zlist[1:4])

    zlist.pop(3)
    print(zlist)

    xlist = [10,88]
    zlist.extend(xlist)
    print(zlist)

    zlist[0] = '5'
    print(zlist)

    print(len(zlist))


if __name__ == '__main__':
    list_update()