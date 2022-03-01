import requests
import base64
import glob
import os
import sys

# 定义token地址
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=b5tzPsMmh3Iv0B3qFkAXcgzl&client_secret=AQbiZDu99lIEe1G8nhCnCG8x2Eyhn2V1'
# 请求token
response = requests.get(host)
if response:
    # 提取token
    access_token = response.json()['access_token']
    # 获取当前脚本文件名
    cur_file = os.path.basename(sys.argv[0])
    # 获取除脚本外的文件列表
    dir_content = [x for x in os.listdir(".") if x != cur_file]
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_seg"
    i = 0
    for f in dir_content:
        i = i + 1
        img = open(f, 'rb')
        img = base64.b64encode(img.read())
        # 定义param
        params = {"image":img,"type":"foreground"}
        # 拼接人像分割API地址
        request_url = request_url + "?access_token=" + access_token
        # 定义header
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        print("正在移除第",i,"张背景...")
        # 请求人像分割接口
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            # 获取回调的base64值
            imgdata = base64.b64decode(response.json()['foreground'])
            # 以原名保存为png文件
            file = open(f.split(".")[0]+'.png','wb')
            file.write(imgdata)
            file.close()
            print('完成！')