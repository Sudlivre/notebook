import yaml
import os

"""
f = open('./res/config.yml', 'r', encoding='utf-8')
cont = f.read()
x = yaml.load(cont)
print(type(x))
print(x)
print(x['DB'])
print(x['DataBase'])
print(x['HuLuWa'])
"""

fw = open('./res/write_config.yml', 'w', encoding='utf-8')
data = {"Cookie":{'domain': ['.yiyao.cc', 'test'], 'expiry': 1521558688.480118, 'httpOnly': False, 'name': '_ui_', 'path': '/', 'secure': False, 'value': 'HSX9fJjjCIImOJoPUkv/QA=='}}
yaml.dump(data, fw)


