import jing.api
import json

'''
这边可以设置一个默认的appkey和secret，当然也可以不设置
注意：默认的只需要设置一次就可以了
'''
jing.setDefaultAppInfo("110bc5b99cfab32454dcaa8022dd8c4f", "612f41079b0241fd8be42576a845084a")

'''
使用自定义的域名和端口（测试沙箱环境使用）
a = top.api.UserGetRequest("gw.api.tbsandbox.com",80)
使用自定义的域名（测试沙箱环境使用）
a = top.api.UserGetRequest("gw.api.tbsandbox.com")
使用默认的配置（调用线上环境）
a = top.api.UserGetRequest()
'''
# a = jing.api.jdUnionOpenCategoryGoodsGet()
a = jing.api.jdUnionOpenGoodsJingfenQuery()

'''
可以在运行期替换掉默认的appkey和secret的设置
a.set_app_info(top.appinfo("appkey","*******"))
'''

# a.param_json = json.dumps({
#     "req": {
#         "parentId": 0,
#         "grade": 0
#     }
# })

a.param_json = json.dumps({
    "goodsReq": {
        "sort": "desc",
        "pageSize": 50,
        "eliteId": 11,
        "sortName": "commission",
        "pageIndex": 1
    }
})

try:
    f = a.getResponse()
    print(f)
except Exception as e:
    print(e)
