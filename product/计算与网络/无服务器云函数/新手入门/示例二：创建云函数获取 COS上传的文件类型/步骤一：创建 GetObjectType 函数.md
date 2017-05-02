1. 登录腾讯云控制台，选择【对象存储服务】。

2. 点击【Bucket列表】选项卡下的【创建Bucket】按钮，新建一个COS Bucket。

3. 设置COS Bucket的名称如`TestBucket`，选择地域为`华南`，设置访问权限为默认值`公有读私有写`并设置CDN加速为默认值`关闭`，点击【保存】按钮新建一个COS Bucket。

4. 在控制台上导航至【无服务器云函数】，在`广州`地域下点击【创建函数】按钮，进入新建函数页面。

5. 填写函数名称`GetObjectType`，其他配置项保持默认选项即可。

4. 点击【下一步】按钮，进入函数代码编辑页，默认选择【在线编辑】，并在【模版】中选择 `cos-get-object-python` 模版。此时，执行方法和代码将填入模版的默认值：
- 执行方法显示`index.main_handler`。表示无服务器云函数控制台会将此段代码自动保存为`index.py`文件，并压缩该文件上传至 SCF 平台以创建云函数。
- 函数代码显示以下代码片段:

```
import json
import urllib
from qcloud_cos import CosClient
from qcloud_cos import StatFileRequest

print('Start cos demo function')

appid = u'12500000'  #替换为用户的appid，可在控制台【账户信息】中查看
secret_id = u'xirhaow34mnYOG' #替换为用户的云API secret id，可在控制台【云API密钥】中查看
secret_key = u'nxiwemfYUoNu3209nfo' #替换为用户的云API secret key，可在控制台【云API密钥】中查看
region = 'sh'
cos = CosClient(appid,secret_id,secret_key,region)

def main_handler(event, context):
    # Get the object from the event and show its content type
    bucket = event['Records'][0]['cos']['bucket']['name']
    key = urllib.unquote_plus(event['Records'][0]['cos']['object']['key'].encode('utf8'))
    try:
        
        request = StatFileRequest(bucket, key)
        stat_file_ret = cos_client.stat_file(request)
        print("CONTENT TYPE: " + response['data']['custom_headers']['Content-Type'])
        return response['data']['custom_headers']['Content-Type']
    except Exception as e:
        print(e)
        print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
        raise e


```
该示例代码将从`event`参数中获取类似以下形式的数据：
```
{  
   "Records":[  
      {
        "event": {
          "eventVersion":"1.0",
          "eventSource":"qcs::cos",
          "eventName":"ObjectCreated:Put",
          "eventTime":"Unix 时间戳",
          "eventQueue":"qcs:0:scf:sh:appid/10000:testscf",
          "requestParameters":{
            "requestSourceIP": "请求来源 IP 地址",
            "requestHeaders":{
              "Authorization": "上传的鉴权信息"
            }
          }
         },
         "cos":{  
            "cosSchemaVersion":"1.0",
            "cosNotificationId":"设置的或返回的 ID",
            "cosBucket":{  
               "name":"bucketname",
               "appid":"appId",
               "region":"sh",
            },
            "cosObject":{  
               "key":"文件路径",
               "size":"文件大小",
               "meta":{
                 "Content-Type": "text/plain",
                 "x-cos-meta-test": "自定义的 meta",
                 "x-image-test": "自定义的 meta"
               }，
               "url": "访问文件的源站url"
            }
         }
      },
      {
          // Additional events
      }
   ]
}  
```

5. 点击【下一步】按钮，进入触发方式页面。点击【新建触发方式】按钮为函数添加一个新的触发器，选择触发方式为`COS触发`，并选择刚刚创建的`TestBucket`存储桶，事件类型选择为`文件上传`，点击【保存】按钮。

6. 点击底部【完成】按钮，此时控制台会自动生成代码程序包并上传至 SCF 平台以创建云函数。您可以点击云函数列表页中刚刚创建的`GetObjectType`函数进入云函数详情页。

