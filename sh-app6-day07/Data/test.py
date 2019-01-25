import yaml
with open("./data.yml", "r") as f:
    # 读取yaml文件，返回字典
    data = yaml.load(f)
    print(data)



