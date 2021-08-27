目前支持的 Python 开发语言包括如下版本：
* Python 2.7
* Python 3.6

## 函数形态

Python 函数形态一般如下所示：
```python
import json

def main_handler(event, context):
    print("Received event: " + json.dumps(event, indent = 2)) 
    print("Received context: " + str(context))
    return("Hello World")
```

## 执行方法

在创建 SCF 云函数时，均需要指定执行方法。使用 Python 开发语言时，执行方法类似 `index.main_handler`，此处 `index`表示执行的入口文件为 `index.py` ，`main_handler`表示执行的入口函数为 `main_handler` 函数。在使用 本地 zip 文件上传、COS 上传等方法提交代码 zip 包时，请确认 zip 包的根目录下包含有指定的入口文件，文件内有定义指定的入口函数，文件名和函数名和执行方法处填写的能够对应，避免因为无法查找到入口文件和入口函数导致的执行失败。

## 入参

Python 环境下的入参包括 event 和 context，两者均为 Python dict 类型。
* event：使用此参数传递触发事件数据。
* context：使用此参数向您的处理程序传递运行时信息。

## 返回和异常

您的处理程序可以使用 `return` 来返回值，根据调用函数时的调用类型不同，返回值会有不同的处理方式。
* 同步调用：使用同步调用时，返回值会序列化后以 JSON 的格式返回给调用方，调用方可以获取返回值已进行后续处理。例如通过控制台进行的函数调试的调用方法就是同步调用，能够在调用完成后捕捉到函数返回值并显示。
* 异步调用：异步调用时，由于调用方法仅触发函数就返回，不会等待函数完成执行，因此函数返回值会被丢弃。

同时，无论同步调用还是异步调用，返回值均会在函数日志中 `ret_msg` 位置显示。

您可以在函数内使用 `raise Exception` 的方式抛出异常。抛出的异常会在函数运行环境中被捕捉到并在日志中以 `Traceback` 的形式展示。

## 日志
您可以在程序中使用 `print` 或使用 `logging` 模块来完成日志输出。例如，如下函数：
```python
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
def main_handler(event, context):
    logger.info('got event{}'.format(event))
    print("got event{}".format(event))
    return 'Hello World!'  
```

输出内容您可以在函数日志中的 `log` 位置查看。

## 如何安装依赖

请参考 [依赖安装](https://cloud.tencent.com/document/product/583/39780)。


## 已包含的库及使用方法

### COS SDK

云函数的运行环境内已包含 [COS 的 Python SDK](https://cloud.tencent.com/document/product/436/12269)，具体版本为 `cos_sdk_v5`（推荐）和 `cos_sdk_v4`。

可在代码内通过如下方式引入 COS SDK 并使用：
- 对于 `cos_sdk_v5` 版本：
```
import qcloud_cos_v5
```
```
from qcloud_cos_v5 import CosConfig 
from qcloud_cos_v5 import CosS3Client
```

- 对于 `cos_sdk_v4` 版本：
```
import qcloud_cos
```
```
from qcloud_cos_v4 import CosClient
from qcloud_cos_v4 import DownloadFileRequest
from qcloud_cos_v4 import UploadFileRequest
```

更详细的 COS SDK 使用说明见 [COS Python SDK 说明](https://cloud.tencent.com/document/product/436/12269)。

## Python 2 或 3？
您可以在函数创建时，通过选择运行环境中的 `Python 2.7` 或 `Python 3.6` 选择您所期望使用的运行环境。

您可以在 [这里](https://wiki.python.org/moin/Python2orPython3) 查看 Python 官方对 Python 2 或 Python 3 语言选择的建议。

Python 3 云端运行时已支持的库如下表：
>?若您需要使用表中尚未支持的库，请在本地安装并打包上传后使用。详情请参见 [安装依赖库](https://cloud.tencent.com/document/product/583/39780#python-.E8.BF.90.E8.A1.8C.E6.97.B6)。
>

|库名称|版本|
| -------------------------------- |---------------|
| absl-py                |0.2.2|
| asn1crypto              |0.24.0|
| astor                  |0.7.1|
| bleach                   |1.5.0|
| certifi             |2019.3.9|
| cffi                     |1.12.2|
| chardet                   |3.0.4|
| cos-python-sdk-v5       |1.6.6|
| cryptography           |2.6.1|
| dicttoxml             |1.7.4|
| gast                     |0.2.0|
| grpcio                  |1.13.0|
| html5lib           |0.9999999|
| idna                      |2.8|
| iniparse                   |0.4|
| Markdown                 |2.6.11|
| mysqlclient             |1.3.13|
| numpy                    |1.15.0|
| Pillow                    |6.0.0|
| pip                       |9.0.1|
| protobuf                  |3.6.0|
| psycopg2-binary           |2.8.2|
| pycparser                  |2.19|
| pycurl                   |7.43.0|
| PyMySQL                   |0.9.3|
| pytz                     |2019.1|
| qcloud-image              |1.0.0|
| qcloudsms-py              |0.1.3|
| requests                 |2.21.0|
| serverless-db-sdk         |0.0.1|
| setuptools               |28.8.0|
| six                      |1.12.0|
| tencentcloud-sdk-python  |3.0.65|
| tencentserverless         |0.1.4|
| tensorboard               |1.9.0
| tensorflow                |1.9.0
| tensorflow-serving-api    |1.9.0|
| termcolor                 |1.1.0
| urllib3                  |1.24.2
| Werkzeug                 |0.14.1
| wheel                    |0.31.1|

Python 2 云端运行时已支持的库如下表：

|库名称|版本|
| -------------------------------- |---------------|
| absl-py                      | 0.2.2     |
| asn1crypto                   | 0.24.0    |
| astor                        | 0.7.1     |
| backports.ssl-match-hostname | 3.4.0.2   |
| backports.weakref            | 1.0.post1 |
| bleach                       | 1.5.0     |
| cassdk                       | 1.0.2     |
| certifi                      | 2017.11.5 |
| cffi                         | 1.12.2    |
| chardet                      | 3.0.4     |
| cos-python-sdk-v5            | 1.6.6     |
| cryptography                 | 2.6.1     |
| dicttoxml                    | 1.7.4     |
| enum34                       | 1.1.6     |
| funcsigs                     | 1.0.2     |
| futures                      | 3.2.0     |
| gast                         | 0.2.0     |
| grpcio                       | 1.13.0    |
| html5lib                     | 0.9999999 |
| idna                         | 2.6       |
| iniparse                     | 0.4       |
| ipaddress                    | 1.0.22    |
| Markdown                     | 2.6.11    |
| mock                         | 2.0.0     |
| mysqlclient                  | 1.3.13    |
| nose                         | 1.3.7     |
| numpy                        | 1.14.5    |
| ordereddict                  | 1.1       |
| pbr                          | 4.1.0     |
| Pillow                       | 6.0.0     |
| pip                          | 18        |
| protobuf                     | 3.6.0     |
| psycopg2-binary              | 2.8.2     |
| pyaml                        | 2019.4.1  |
| pycparser                    | 2.19      |
| pycurl                       | 7.43.0.1  |
| pygpgme                      | 0.3       |
| PyMySQL                      | 0.9.3     |
| pytz                         | 2019.1    |
| PyYAML                       | 5.1       |
| qcloud-image                 | 1.0.0     |
| qcloudsms-py                 | 0.1.3     |
| requests                     | 2.18.4    |
| serverless-db-sdk            | 0.0.1     |
| setuptools                   | 39.1.0    |
| six                          | 1.11.0    |
| tencentcloud-sdk-python      | 3.0.65    |
| tencentserverless            | 0.1.4     |
| tensorboard                  | 1.9.0     |
| tensorflow                   | 1.9.0     |
| tensorflow-serving-api       | 1.9.0     |
| termcolor                    | 1.1.0     |
| urlgrabber                   | 3.10.2    |
| urllib3                      | 1.22      |
| Werkzeug                     | 0.14.1    |
| wheel                        | 0.31.1    |


## 更多指引
您可参考以下文档，使用相关功能：
- [使用 SCF 连接数据库](<https://cloud.tencent.com/document/product/583/38012>)
- [网络配置管理](<https://cloud.tencent.com/document/product/583/38202>)
- [角色与授权](<https://cloud.tencent.com/document/product/583/32389>)




