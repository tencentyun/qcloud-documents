请用户按照以下步骤来测试刚刚创建的`GetObjectType`函数。

## 使用 COS 上传文件测试
1. 登录腾讯云控制台，导航至【对象存储服务】,在【Bucket】列表中选择第一步中创建的`TestBucket`Bucket，点击【上传文件】按钮，上传一张[示例图片:testimage.png]()(您可将此示例图片下载到本地并用作测试）：
2. 导航至【无服务器云函数】，选择刚刚创建的`GetObjectType`。
3. 点击【日志】选项卡，观察是否有刚刚上传图片后的函数运行日志。日志中应有 COS 上传文件的文件类型。

## 手动模拟测试
1. 您还可以通过手动输入类似COS触发的测试数据来观察函数运行状态。
在测试函数弹出框中，从测试模版中选择`COS Put Object`，下列数据将出现在窗口中。
需要做以下修改：
- 把`cosObject`中`meta`的`Content-Type`更换成您希望显示的值;
```
{  
   "Records":[  
      {
        "event": {
          "eventVersion":"1.0",
          "eventSource":"qcs::cos",
          "eventName":"event-type",
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
      }
   ]
}  
```

2. 点击【运行】按钮，代码开始运行并将显示测试结果。其中：
- 函数返回值部分将显示运行结果，还将显示代码中 `return` 语句返回的函数执行结果（此时应该返回您刚刚修改的Content-Type值）。
- 运行信息部分将显示函数运行的时间、内存等信息。
- 日志部分将显示函数运行时生成的日志，包括用户代码中的打印语句、函数运行失败trace stack等，将会写入至日志模块。

3. 您可以多运行几次，并点击【日志】选项卡来查看每一次运行的日志信息。