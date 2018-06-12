在此部分中，用户将创建一个函数来实现缩略图程序，并通过控制台/API调用来测试函数。

## 创建 CreateThumbnailDemo SCF 函数
1) 登录[无服务器云函数控制台](https://console.cloud.tencent.com/scf)，在【广州】地域下单击【新建】按钮；

2) 进入函数配置部分，函数名称填写`CreateThumbnailDemo`，剩余项保持默认，单击【下一步】；

3）进入函数代码部分，选择【本地上传zip包】。执行方法填写`CreateThumbnail.main_handler`，选择步骤二：创建部署程序包中创建的 `CreateThumbnailDemo.zip`，单击【下一步】；

4) 进入触发方式部分，此时由于需要先手动测试函数，暂时不添加任何触发方式，单击【完成】按钮。

## 测试 CreateThumbnailDemo SCF 函数
在创建函数时，通常会使用控制台或 API 先进行测试，确保函数输出符合预期后再绑定触发器进行实际应用。

1) 在刚刚创建的 CreateThumbnailDemo 函数详情页中，单击【测试】按钮；

2) 在测试模版下拉列表中选择【COS 上传/删除文件测试代码】

3) 轻微改动测试代码，将 `name`设置为步骤一：准备 COS Bucket 中创建的`mybucket`存储桶名称，将`key`设置为步骤一：准备 COS Bucket 中上传的`/HappyFace.jpg`键值，如下面示例：
```
{  
   "Records":[  
      {
        "event": {
          "eventVersion":"1.0",
          "eventSource":"qcs::cos",
          "eventName":"event-type",
          "eventTime":"Unix 时间戳",
          "eventQueue":"qcs:0:cos:gz:1251111111:cos",
          "requestParameters":{
            "requestSourceIP": "111.111.111.111",
            "requestHeaders":{
              "Authorization": "上传的鉴权信息"
            }
          }
         },
         "cos":{  
            "cosSchemaVersion":"1.0",
            "cosNotificationId":"设置的或返回的 ID",
            "cosBucket":{  
               "name":"mybucket", #set to demo bucket here
               "appid":"appId",
               "region":"gz"
            },
            "cosObject":{  
               "key":"/HappyFace.png", #set to demo file here
               "size":"1024",
               "meta":{
                 "Content-Type": "text/plain",
                 "x-cos-meta-test": "自定义的 meta",
                 "x-image-test": "自定义的 meta"
               },
               "url": "访问文件的源站url"
            }
         }
      }
   ]
}
```

4) 单击【运行】按钮，观察运行结果。如果在结果中发现下载和上传均成功，则此程序运行正常：
![](//mc.qcloudimg.com/static/img/aec9243fd45a41e562b9c17d530740a0/image.png)

5) 前往[对象存储控制台](https://console.cloud.tencent.com/cos4/index)，单击步骤一：准备 COS Bucket 中创建的`mybucketresized`，观察是否有名为`HappyFace.png`的缩略图产生。
![](//mc.qcloudimg.com/static/img/5c4224adcef4231f1469956107f000aa/image.png)

6) 下载该图片，对比观察它和原图片的大小。
