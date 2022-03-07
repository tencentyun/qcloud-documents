## 功能描述

POST Object restore 接口请求可以对一个归档存储或深度归档存储类型的对象进行恢复（解冻）以便读取该对象内容，恢复出的可读取对象是临时的，您可以设置需要保持可读以及随后删除该临时副本的时间。您可以用 Days 参数来指定临时对象的过期时间，若超出该时间且期间您没有发起任何复制、延长等操作，该临时对象将被系统自动删除。临时对象仅为归档存储类型对象的副本，原始归档存储对象在此期间将始终存在。有关归档存储的进一步说明，请参见 [存储类型 - 归档存储](https://cloud.tencent.com/document/product/436/33417#.E5.BD.92.E6.A1.A3.E5.AD.98.E5.82.A8) 文档。

>? POST Object restore 接口请求存在 QPS 限制，限制为100次/秒。
>

<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=PostObjectRestore&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
        </div>
        <div class="rno-api-explorer-body">
            <div class="rno-api-explorer-cont">
                API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。
            </div>
        </div>
    </div>
</div>


#### 版本控制

当启用版本控制时，该请求操作可以使用 versionId 请求参数指定要恢复的版本 ID，此时将恢复对象的指定版本，否则将恢复指定对象的最新版本。

## 请求

#### 请求示例

```plaintext
POST /<ObjectKey>?restore HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-Type: application/xml
Content-Length: Content Length
Content-MD5: MD5
Authorization: Auth String



[Request Body]
```

>? 
> - Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> 

#### 请求参数

| 名称                         | 描述                                                         | 类型   | 是否必选 |
| ---------------------------- | ------------------------------------------------------------ | ------ | -------- |
| versionId                    | 当启用版本控制时，指定要恢复的版本 ID，如不指定则恢复对象的最新版本 | string | 否       |

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

####  请求体

提交 **application/xml** 请求数据，包含恢复操作的具体参数。

```plaintext
<RestoreRequest>
   <Days>number</Days>
   <CASJobParameters>
       <Tier>Enum</Tier>
   </CASJobParameters>
</RestoreRequest>
```

具体的节点描述如下：

| 节点名称（关键字） | 父节点 | 描述 | 类型 | 是否必选 |
| --- | --- | --- | --- | --- |
| RestoreRequest | 无 | 包含 POST Object restore 操作的所有请求信息 | Container | 是 |

**Container 节点 RestoreRequest 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 | 是否必选 |
| --- | --- | --- | --- | --- |
| Days | RestoreRequest | 指定恢复出的临时副本的有效时长，单位为“天” | number | 是 |
| CASJobParameters | RestoreRequest | 恢复工作参数 | Container | 是 |

**Container 节点 CASJobParameters 的内容：**

| 节点名称（关键字） | 父节点 | 描述 | 类型 | 是否必选 |
| --- | --- | --- | --- | --- |
| Tier | RestoreRequest.CASJobParameters | 恢复时，Tier 可以指定为支持的恢复模式。<br>对于恢复归档存储类型数据，有三种恢复模式，分别为：<br><li>Expedited：极速模式，恢复任务在1 - 5分钟内可完成。<br> <li>Standard：标准模式，恢复任务在3 - 5小时内完成 <br><li>Bulk：批量模式，恢复任务在5 - 12小时内完成。<br>对于恢复深度归档存储类型数据，有两种恢复模式，分别为：<br><li>Standard：标准模式，恢复时间为12 - 24小时。<br><li>Bulk：批量模式，恢复时间为24 - 48小时。 | Enum | 是 |


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

此接口响应体为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 案例一：简单案例（未启用版本控制）

#### 请求

```plaintext
POST /exampleobject?restore HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Fri, 27 Dec 2019 08:19:29 GMT
Content-Type: application/xml
Content-Length: 121
Content-MD5: Nr7RAnRMgrplFvD8bt5+0w==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1577434769;1577441969&q-key-time=1577434769;1577441969&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=restore&q-signature=ed3ee8ca63689dbff4be1533fddc17c0b4d8****
Connection: close



<RestoreRequest>
			<Days>1</Days>
			<CASJobParameters>
				<Tier>Expedited</Tier>
			</CASJobParameters>
</RestoreRequest>
```

#### 响应

```plaintext
HTTP/1.1 202 Accepted
Content-Length: 0
Connection: close
Date: Fri, 27 Dec 2019 08:19:29 GMT
Server: tencent-cos
x-cos-request-id: NWUwNWJlOTFfMjljOTBiMDlfMTQ2MmNfNzAw****
```

#### 案例二：恢复对象的指定版本（启用版本控制）

#### 请求

```plaintext
POST /exampleobject?restore&versionId=MTg0NDUxNjQ1NjM4OTkzNzY3NDk HTTP/1.1
Host: examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Mon, 20 Jan 2020 08:43:40 GMT
Content-Type: application/xml
Content-Length: 121
Content-MD5: Nr7RAnRMgrplFvD8bt5+0w==
Authorization: q-sign-algorithm=sha1&q-ak=AKID8A0fBVtYFrNm02oY1g1JQQF0c3JO****&q-sign-time=1579509820;1579517020&q-key-time=1579509820;1579517020&q-header-list=content-length;content-md5;content-type;date;host&q-url-param-list=restore;versionid&q-signature=f92b1c6753c452bed9ade49739ddb81a0a47****
Connection: close



<RestoreRequest>
			<Days>1</Days>
			<CASJobParameters>
				<Tier>Expedited</Tier>
			</CASJobParameters>
</RestoreRequest>
```

#### 响应

```plaintext
HTTP/1.1 202 Accepted
Content-Length: 0
Connection: close
Date: Mon, 20 Jan 2020 08:43:41 GMT
Server: tencent-cos
x-cos-request-id: NWUyNTY4M2NfZTNjODJhMDlfMWZkM2VfNWZm****
```
