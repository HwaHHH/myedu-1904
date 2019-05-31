

def assert_str():
    try:
        assert '成功' in '操作成功'
        assert '成功'  not in '成功'
    except:
        print('失败')

if __name__ == '__main__':
    assert_str()