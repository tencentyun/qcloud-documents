## 功能描述

COS 支持为已存在的存储桶设置对象锁定。GET Bucket ObjectLockConfiguration 接口用于获取已生效的对象锁定配置。

## 请求

#### 请求示例

```plaintext
GET /?object-lock HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String 
```

>? 
> - Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> 

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

该请求的请求体为空。

 

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

```plaintext
<?xml version="1.0" encoding="UTF-8" ?>
<ObjectLockConfiguration>
      <ObjectLockEnabled>Enabled</ObjectLockEnabled> 
      <Rule> 
           <DefaultRetention>
                 <Days>30</Days> 
           </DefaultRetention> 
      </Rule> 
</ObjectLockConfiguration> 
```



具体数据描述如下：

| 节点名称（关键字）      | 父节点                                        | 描述                                    | 类型       |
| ----------------------- | --------------------------------------------- | --------------------------------------- | ---------- |
| ObjectLockConfiguration | 无                                            | 对象锁定配置                            | Container  |
| ObjectLockEnabled       | ObjectLockConfiguration                       | 是否开启对象锁定                        | String     |
| Rule                    | ObjectLockConfiguration                       | 对象锁定规则                            | Containers |
| DefaultRetention        | ObjectLockConfiguration.Rule                  | 对象锁定默认周期                        | Containers |
| Days                    | ObjectLockConfiguration.Rule.DefaultRetention | 对象锁定默认周期时长（范围为1-36500天） | Int        |

 

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

 
