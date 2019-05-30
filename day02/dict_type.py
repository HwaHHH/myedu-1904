import json
# 字典


adict = {'username':'admin',"password":"123456"}

def dict_sel():
    print(adict['username'])

def dict_updata():
    adict['username'] = 'hwa'
    print(adict)

def dict_del():
    adict.pop('username')
    print(adict)

def dict_add():
    adict['age'] = 23
    print(adict)
    bdict = {'class':'1904','city':'重庆',"password":"666666"}
    adict.update(bdict)
    print(adict)

    cdict = dict(adict,**bdict)
    print(cdict)

def dict_zh():
    json.dumps(adict)

if __name__ == '__main__':
    dict_zh()