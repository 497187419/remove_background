import requests
import base64
import os
import sys

def get_access_token():
    """获取百度 AI 接口的访问令牌"""
    host = 'https://aip.baidubce.com/oauth/2.0/token'
    params = {
        'grant_type': 'client_credentials',
        'client_id': 'b5tzPsMmh3Iv0B3qFkAXcgzl',
        'client_secret': 'AQbiZDu99lIEe1G8nhCnCG8x2Eyhn2V1'
    }
    try:
        response = requests.get(host, params=params)
        return response.json()['access_token']
    except Exception as e:
        print(f"获取token失败：{str(e)}")
        sys.exit(1)

def process_image(image_path, access_token):
    """处理单张图片"""
    try:
        with open(image_path, 'rb') as img:
            img_base64 = base64.b64encode(img.read())
        
        request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_seg"
        params = {
            "image": img_base64,
            "type": "foreground"
        }
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(f"{request_url}?access_token={access_token}", 
                               data=params, 
                               headers=headers)
        
        if response.status_code == 200:
            imgdata = base64.b64decode(response.json()['foreground'])
            output_file = f"{os.path.splitext(image_path)[0]}.png"
            with open(output_file, 'wb') as f:
                f.write(imgdata)
            return True
        return False
    except Exception as e:
        print(f"处理图片 {image_path} 失败：{str(e)}")
        return False

def main():
    # 获取token
    access_token = get_access_token()
    
    # 获取当前目录下所有图片文件
    current_script = os.path.basename(sys.argv[0])
    image_files = [f for f in os.listdir(".") 
                   if f != current_script and 
                   f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    
    if not image_files:
        print("当前目录下没有找到图片文件")
        return
    
    # 处理所有图片
    for i, image_file in enumerate(image_files, 1):
        print(f"正在处理第 {i} 张图片：{image_file}...")
        if process_image(image_file, access_token):
            print(f"图片 {image_file} 处理完成！")
        else:
            print(f"图片 {image_file} 处理失败！")

if __name__ == "__main__":
    main()