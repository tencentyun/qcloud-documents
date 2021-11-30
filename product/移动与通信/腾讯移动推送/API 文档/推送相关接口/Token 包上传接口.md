## 接口说明

**请求方式**：POST。

```plaintext
服务地址/v3/push/package/upload
```

接口服务地址与服务接入点一一对应，请选择与您的应用服务接入点对应的 [服务地址](https://cloud.tencent.com/document/product/548/49157)。

**接口功能**：用户需要通过文件的方式，对批量设备 Token 上传 Token 包文件， 然后对 Token 包中的文件进行推送。

## 请求参数 

| 参数名 | 类型      | 是否必须 | 参数说明                                                     |
| ------ | --------- | -------- | ------------------------------------------------------------ |
| file   | form-data | 是       | <li>Token 包文件名：长度限制为 [1,100]</li><li>Token 包格式及大小： 支持 `zip\txt\csv` 文件；大小保持在100MB以内</li><li>压缩包中可含有： 单个 `.txt` 或 `.csv` 文件 (不能嵌套文件夹)</li><li>`.txt` 文件要求：（1）编码为 UTF-8；（2）每行一个 Token，有效 Token 长度为36位</li><li>`.csv` 文件要求：（1）只能有一列；（2）每行一个 Token，有效 Token 长度为36位</li> |

## 响应参数

| 参数名   | 类型    | 是否必须 | 参数说明                                                     |
| -------- | ------- | -------- | ------------------------------------------------------------ |
| retCode  | Integer | 是       | 错误码                                                       |
| errMsg   | String  | 是       | 请求出错时的错误信息                                        |
| uploadId | Integer | 是       | 当上传文件成功时，将返回一个正整数 uploadId ，代表上传文件 ID，提供给推送接口进行 Token 包推送 |


## 请求示例

#### Curl  示例

```xml
curl -X POST 
https://api.tpns.tencent.com/v3/push/package/upload 
   
-H 'Authorization: Basic  应用的认证信息' 
-F 'file=@C:\上传文件绝对路径'
```



#### Python  示例

```python
import requests

url = "https://api.tpns.tencent.com/v3/push/package/upload"

files = {'file':open('文件名', 'rb')}
upload_data={"fileName":"文件绝对地址"}

headers = {
    'Authorization': "Basic 应用鉴权信息",
    }

response = requests.request("POST", url, data=upload_data, headers=headers, files=files, verify=False)
print(response.text.encode('utf-8'))
```

>! 应用的认证信息，请参见 [Basic Auth 认证](https://cloud.tencent.com/document/product/548/39062) 文档。
>

