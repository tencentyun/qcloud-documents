用户可以编写 SCF 函数来处理 COS Bucket 中的对象创建和对象删除事件。COS 可将事件发布给 SCF 函数并将事件数据作为参数来调用该函数。用户可以在 COS Bucket 中添加存储桶通知配置，该配置可标识触发函数的事件类型和希望调用的函数名称等信息，更多内容请参考 PutBucketNotification 接口。

COS 触发器具有以下特点：

- Push 模型：COS 会监控指定的 Bucket 动作（事件类型）并调用相关函数，将事件数据推送给 SCF 函数。在推模型中使用 Bucket 通知来保存 COS 的事件源映射。
- 异步调用：COS 始终使用异步调用类型来调用函数，结果不会返回给调用方。有关调用类型的更多信息，请参阅[调用类型]()。

## COS 触发器属性

- COS Bucket（必选）：配置的COS Bucket，仅支持选择同地域下的 COS 存储桶。
- 事件类型（必选）：目前支持“文件上传”和“文件删除”两种类型，决定了触发器何时触发函数。例如，选择“文件上传”时，会在该COS Bucket中有文件上传时触发该函数。

## COS 触发器的事件消息结构
在指定的 COS Bucket 发生对象创建或对象删除事件时，会将类似以下的JSON 格式事件数据发送给绑定的 SCF 函数。

```
{  
   "Records":[  
      {
        "event": {
          "eventVersion":"1.0",
          "eventSource":"qcs::cos",
          "eventName":"cos:ObjectCreated:*,
          "eventTime":"1970-01-01T00:00:00.000Z",
          "eventQueue":"qcs:0:cos:gz:1251111111:cos",
          "requestParameters":{
            "requestSourceIP": "111.111.111.111",
            "requestHeaders":{
              "Authorization": "Example"
            }
          }
         },
         "cos":{  
            "cosSchemaVersion":"1.0",
            "cosNotificationId":"设置的或返回的 ID",
            "cosBucket":{  
               "name":"bucketname",
               "appid":"1251111111",
               "region":"gz",
            },
            "cosObject":{  
               "key":"/test.jpg",
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