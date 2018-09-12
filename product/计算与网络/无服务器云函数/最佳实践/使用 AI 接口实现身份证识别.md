## 概述


## 步骤 1. 创建 COS Bucket
登录 [对象存储控制台](https://console.cloud.tencent.com/cos) 创建一个 Bucket，我们命名为 idcard-detect，并选择北京地域，权限选择“公有读-私有写”。
![](https://main.qcloudimg.com/raw/cb9eda64c0d306051e9120130ba21a4f.png)
## 步骤 2. 开通 AI 接口
前往 [智能图像控制台](https://console.cloud.tencent.com/ai/ocr/idcard) 开通身份证识别功能，单击【开通服务】即可。

## 步骤 3. 创建云函数 SCF
### 创建准备
1. 首先确保在您的系统中已经安装好了 Python 运行环境和 pip 工具，然后在本地创建需要放置函数代码的文件夹，并通过命令行进入该目录下，直接执行命令安装 COS V5 SDK、文字识别 SDK 和 Pillow 库：
```
pip install cos-python-sdk-v5 -t .
pip install qcloud_image -t .
pip install Pillow -t .
```
2. 在函数代码文件夹的根目录下，使用下面的示例代码创建 Python 文件，可以命名为：idcard_detect.py。
3. Python 文件保存后，回到根目录下，对所有文件进行打包（**请注意，不是对外层的文件夹打包**）；另外还需要保证：**idcard_detect.py 存在于根目录下，压缩包需要为 zip 格式**。

#### 示例代码
```
# -*- coding: utf-8 -*-
import json
import os
import logging
import datetime
from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from qcloud_cos import CosServiceError
from qcloud_image import Client
from qcloud_image import CIUrl, CIFile, CIBuffer, CIUrls, CIFiles, CIBuffers
from PIL import Image
import PIL.Image
import sys


logging.basicConfig(level=logging.INFO, stream=sys.stdout)

appid = ****  # 请替换为您的 APPID
secret_id = u'****'  # 请替换为您的 SecretId
secret_key = u'****'  # 请替换为您的 SecretKey
region = u'ap-beijing'
token = ''

config = CosConfig(Secret_id=secret_id, Secret_key=secret_key, Region=region, Token=token)
client = CosS3Client(config)
logger = logging.getLogger()


def resize_image(image_path, resized_path):
    with Image.open(image_path) as image:
        size = float(os.path.getsize(image_path) / 1024 / 1024)
        print size
        if size >= 1:
            image.thumbnail(tuple(x / 2 for x in image.size))
            # image.resize((1024,1024),Image.BILINEAR)
        image.save(resized_path)


def delete_local_file(src):
    logger.info("delete files and folders")
    if os.path.isfile(src):
        try:
            os.remove(src)
        except:
            pass
    elif os.path.isdir(src):
        for item in os.listdir(src):
            itemsrc = os.path.join(src, item)
            delete_file_folder(itemsrc)
        try:
            os.rmdir(src)
        except:
            pass


def main_handler(event, context):
    logger.info("start main handler")
    for record in event['Records']:
        try:
            bucket = record['cos']['cosBucket']['name'] + '-' + str(appid)
            key = record['cos']['cosObject']['key']
            key = key.replace('/' + str(appid) + '/' + record['cos']['cosBucket']['name'] + '/', '', 1)
            download_path = '/tmp/{}'.format(key)
            tmpload_path = '/tmp/resized-{}'.format(key)
            print("Key is " + key)
            print("Get from [%s] to download file [%s]" % (bucket, key))

            # download image from cos
            try:
                response = client.get_object(Bucket=bucket, Key=key, )
                response['Body'].get_stream_to_file(download_path)
            except CosServiceError as e:
                print(e.get_error_code())
                print(e.get_error_msg())
                print(e.get_resource_location())
                return "Fail"

            logger.info("Download file [%s] Success" % key)
            logger.info("Image compress function start")
            starttime = datetime.datetime.now()

            # compress image here
            resize_image(download_path, tmpload_path)
            endtime = datetime.datetime.now()
            logger.info("compress image take " + str((endtime - starttime).microseconds / 1000) + "ms")

            # detect idcard
            print("Start Detection")
            client_card = Client(appid, secret_id, secret_key, record['cos']['cosBucket']['name'])
            client_card.use_http()
            client_card.set_timeout(30)
            res_up = client_card.idcard_detect(CIFiles([tmpload_path]), 0)
            res_down = client_card.idcard_detect(CIFiles([tmpload_path]), 1)
            if res_up["result_list"][0]["code"] == 0 and res_down["result_list"][0]["code"] != 0:
                res_up_print = {
                    "姓名：": res_up["result_list"][0]["data"]["name"],
                    "性别：": res_up["result_list"][0]["data"]["sex"],
                    "出生：": res_up["result_list"][0]["data"]["birth"],
                    "住址：": res_up["result_list"][0]["data"]["address"],
                    "民族：": res_up["result_list"][0]["data"]["nation"],
                    "公民身份证号：": res_up["result_list"][0]["data"]["id"]
                }
                print json.dumps(res_up_print).decode('unicode-escape')
            elif res_up["result_list"][0]["code"] != 0 and res_down["result_list"][0]["code"] == 0:
                res_down_print = {
                    "有效期限：": res_down["result_list"][0]["data"]["valid_date"],
                    "签发机关：": res_down["result_list"][0]["data"]["authority"]
                }
                print json.dumps(res_down_print).decode('unicode-escape')
            else:
                print ("err_message: [%s]" % (res_up["result_list"][0]["message"]))
                print ("err_code: [%s]" % (res_up["result_list"][0]["code"]))
                print ("err_filename: [%s]" % (res_up["result_list"][0]["filename"]))
                delete_local_file(str(download_path))
                delete_local_file(str(tmpload_path))
                return "Detect Fail"

            # delete local file
            delete_local_file(str(download_path))
            delete_local_file(str(tmpload_path))
            return "Success"

        except Exception as e:
            print(e)
            raise e
            return "Detect Fail"
```
> **注意：**
在使用本段代码的时候，需要把 appid、secret_id 和 secret_key 替换为您自己的 APPID、SecretId 和 SecretKey 方能使用，您可以在 [云 API 密钥控制台](https://console.cloud.tencent.com/cam/capi) 中查看对应信息。

### 创建步骤
打包完成后，我们就可以前往 [无服务器云函数控制台](https://console.cloud.tencent.com/scf/list/1) 进行部署。
1. 选择北京地域，单击【新建】，命名函数为 Demo2_IDCard_Detect，函数超时时间修改为 5 秒，内存默认 128MB 即可，单击【下一步】。
2. 选择 **本地上传zip包**，执行方法填写：idcard_detect.main_handler，保存后单击【下一步】。
3. 添加触发方式为 COS 触发，选择之前创建好的 Bucket：idcard-detect，事件类型为文件上传，单击【保存】>【完成】，完成函数部署。

您也可以直接从 [GitHub下载](https://github.com/Masonlu/SCF-Demo/tree/master/Demo2_ID%20Card) 项目文件，并打成 zip 包，通过控制台创建函数并完成部署，请注意在函数代码中需修改 appid、secret_id 和 secret_key 并保存。

## 步骤 4. 测试函数功能
1. 进入对象存储控制台，选择创建好的 Bucket：idcard-detect，单击【上传文件】，选择自己拍好的身份证照片，照片要清晰可读且尽可能大的占满图片，然后上传。
2. 进入无服务器云函数控制台查看执行结果，在 **日志** 中可以看到打印出来的日志信息，包含身份证识别的结果。