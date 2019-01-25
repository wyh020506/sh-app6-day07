import pytest, yaml, os


def get_data():
    # 返回 yaml文件数据 [(),(),()]
    # 存储读取数据
    data_list = []
    with open("./Data" + os.sep +"sum.yml", "r") as f:
        data = yaml.load(f)
        for i in data.get("Sum_Data").values():
            # 数据组装
            data_list.append((i.get("a"), i.get("b"), i.get("expect")))
    return data_list
"""
    [(1,2,3), (3,4,7), (4,5,8)]
    
    data ={'Sum_Data': {
            'test_002': {'a': 3, 'b': 4, 'expect': 7}, 
            'test_001': {'a': 1, 'b': 2, 'expect': 3}, 
            'test_003': {'a': 4, 'b': 5, 'expect': 8}}}
    1.data.get(Sum_Data)     
        {
            'test_002': {'a': 3, 'b': 4, 'expect': 7}, 
            'test_001': {'a': 1, 'b': 2, 'expect': 3}, 
            'test_003': {'a': 4, 'b': 5, 'expect': 8}
        } 
    2.data.get(Sum_Data).values()
        [{'a': 3, 'b': 4, 'expect': 7},{'a': 1, 'b': 2, 'expect': 3},{'a': 4, 'b': 5, 'expect': 8}]
    3.循环遍历列表
    for i in data.get(Sum_Data).values():
        data_list = []
        data_list.append((i.get("a"),i.get("b"), i.get("expect")))
    
    
"""


class Test_Yaml:

    @pytest.mark.parametrize("a, b, c", get_data())
    def test_sum_data(self, a, b, c):
        # 判断 a+b==c
        assert a + b == c