## 功能描述

DELETE Bucket inventory 用于删除存储桶中指定的清单任务，用户需提供待删除的清单任务的名称。
有关清单的详细特性，请参见 [清单功能概述](https://cloud.tencent.com/document/product/436/33703)。

> !
> - 调用该请求时，请确保您有足够的权限对存储桶的清单任务进行操作。
> - 存储桶所有者默认拥有该权限，如您无该项权限，请先向存储桶所有者申请该项操作的权限。
> 

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=DeleteBucketInventory&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
        </div>
        <div class="rno-api-explorer-body">
            <div class="rno-api-explorer-cont">
                API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。
            </div>
        </div>
    </div>
</div>


## 请求

#### 请求示例

```shell
DELETE /?inventory&id=inventory-configuration-id HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Authorization: Auth String
```

>? 
> - Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> 

#### 请求参数

调用 DELETE Bucket inventory 需要使用清单任务名称的参数。该参数格式如下：

| 参数 | 描述                                                         | 类型   | 必选 |
| ---- | ------------------------------------------------------------ | ------ | ---- |
| id   | 清单任务的名称。缺省值：None<br/>合法字符：`a-z，A-Z，0-9，-，_，. `| String | 是   |

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。


#### 请求体

该请求的请求体为空。

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。


#### 响应体

该响应体返回为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

下述请求示例展示了从存储桶`examplebucket-1250000000`中删除清单任务 list1。

```shell
DELETE /?inventory&id=list1 HTTP/1.1
Date: Mon, 28 Aug 2018 02:53:38 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1503901499;1503901859&q-key-time=1503901499;1503901859&q-header-list=host&q-url-param-list=inventory&q-signature=761f3f6449c6a11684464f4b09c6f292f0a4****
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
```

#### 响应

上述请求后，COS 返回 204 No Content 的响应表明已成功删除了该存储桶内的清单任务 list1。

```shell
HTTP/1.1 204 No Content 
Server: tencent-cos
Date: Mon, 28 Aug 2018 02:53:40 GMT
x-cos-id-2:0dfafa/DAPDIFdafdsfDdfSFFfdfKKJdafasiuKJK2
x-cos-request-id: NTlhM2I3M2JfMjQ4OGY3MGFfMWE1NF84****
```

