adict = {'username':'admin',"password":"123456"}

def dict_del():
    adict.pop('username')
    print(adict)

    adict['age']=23
    print(adict)

    bdict = {'city':'重庆','phone':'18888888888'}
    adict.update(bdict)
    print(adict)

    cdict = dict(adict,**bdict)
    print(cdict)

def dict_updata():
    adict["password"]='88888888'
    print(adict)

if __name__ == '__main__':
    # dict_updata()
    dict_add()
    # dict_del()
    # print(adict['username'])