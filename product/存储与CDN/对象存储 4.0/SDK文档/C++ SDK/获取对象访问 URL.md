## 简介

本文档提供获取对象访问 URL 的代码示例。

## 获取对象访问 URL

#### 方法原型

```cpp
std::string GetObjectUrl(const std::string& bucket, const std::string& object, bool https = true, const std::string& region);
```

#### 请求示例

```cpp
qcloud_cos::CosConfig config("./config.json");
qcloud_cos::CosAPI cos(config);

std::string bucket_name = "examplebucket-1250000000"; // 替换为用户的存储桶名，由bucketname-appid 组成，appid必须填入，可以在COS控制台查看存储桶名称：https://console.cloud.tencent.com/cos5/bucket
std::string object_name = "exampleobject";
//获取对象https url，region为config.json中配置的地域
cos.GetObjectUrl(bucket_name, object_name);
//获取对象http url，region为config.json中配置的地域
cos.GetObjectUrl(bucket_name, object_name, false);
//获取对象https url, region为ap-shanghai
std::string object_url = cos.GetObjectUrl(bucket_name, object_name, true, "ap-shanghai");  
```

#### 参数说明

| 参数   | 参数描述      | 类型   | 是否必填 |
| ------ | ------------- | ------ | -------- |
| bucket | 存储桶名      | string | 是       |
| object | 对象名        | string | 是       |
| https  | 是否使用 https | bool   | 否       |
| region | 地域名        | string | 否       |

#### 返回结果说明

该方法返回值为对象访问的 URL。
