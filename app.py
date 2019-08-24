import json
from cmdb.types import get_instance

# jsonstr = """{
#     "type" : "cmdb.types.IP",
#     "value": "192.168.1.11",
#     "option":{
#         "prefix":"192.16" ,
#         "ends":"51"
#     }
# }"""
# obj = json.loads(jsonstr)  #将字符串json序列化,返回dict
# print(jsonstr, obj, type(obj))
#
# type = obj.get("type")
# print("type is ", type)
#
#
# print(get_instance(type, **obj["option"]).stringify(obj['value']))















