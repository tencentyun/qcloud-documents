## 功能描述

COS 支持用户以生命周期配置的方式来管理 Bucket 中 Object 的生命周期。生命周期配置包含一个或多个将应用于一组对象规则的规则集 (其中每个规则为 COS 定义一个操作)。
这些操作分为以下两种：

- **转换操作：**定义对象转换为另一个存储类的时间。例如，您可以选择在对象创建30天后将其转换为低频存储（STANDARD_IA，适用于不常访问）存储类别。同时也支持将数据沉降到智能分层存储（INTELLIGENT_TIERING，访问模式不固定）和归档存储（ARCHIVE，成本更低）。具体参数查看请求示例说明中 Transition 项。
- **过期操作：**指定 Object 的过期时间。COS 将会自动为用户删除过期的 Object。


<div class="rno-api-explorer">
    <div class="rno-api-explorer-inner">
        <div class="rno-api-explorer-hd">
            <div class="rno-api-explorer-title">
                推荐使用 API Explorer
            </div>
            <a href="https://console.cloud.tencent.com/api/explorer?Product=cos&Version=2018-11-26&Action=PutBucketLifecycle&SignVersion=" class="rno-api-explorer-btn" hotrep="doc.api.explorerbtn" target="_blank"><i class="rno-icon-explorer"></i>点击调试</a>
        </div>
        <div class="rno-api-explorer-body">
            <div class="rno-api-explorer-cont">
                API Explorer 提供了在线调用、签名验证、SDK 代码生成和快速检索接口等能力。您可查看每次调用的请求内容和返回结果以及自动生成 SDK 调用示例。
            </div>
        </div>
    </div>
</div>

#### 细节分析

PUT Bucket lifecycle 用于为 Bucket 创建一个新的生命周期配置。如果该 Bucket 已配置生命周期，使用该接口创建新的配置的同时则会覆盖原有的配置。

> !
> - 同一条生命周期规则中不可同时支持 Days 和 Date 参数，请分成两条规则分别传入，具体请参见下文 [实际案例](#.E5.AE.9E.E9.99.85.E6.A1.88.E4.BE.8B)。
> - 开启了 [多 AZ](https://cloud.tencent.com/document/product/436/40548) 配置的存储桶，不支持将多 AZ 存储类型沉降到单 AZ 存储类型。
>- 每个存储桶最多可添加1000条生命周期规则。

## 请求

#### 请求示例

```plaintext
PUT /?lifecycle HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Content-Length: length
Date: GMT Date
Authorization: Auth String 
Content-MD5: MD5
```

>? 
> - Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> 

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。


#### 请求体

该 API 接口请求的请求体具体节点内容为：

```shell
<LifecycleConfiguration>
      <Rule>
            <ID></ID>
            <Filter>
                  <And>
                        <Prefix></Prefix>
                        <Tag>
                              <Key></Key>
                              <Value></Value>
                        </Tag>
                  </And>
            </Filter>
            <Status></Status>
            <Transition>
                  <Days></Days>
                  <StorageClass></StorageClass>
            </Transition>
            <NoncurrentVersionExpiration>
                  <NoncurrentDays></NoncurrentDays>
            </NoncurrentVersionExpiration>
      </Rule>
      <Rule>
            <ID></ID>
            <Filter>
                  <Prefix></Prefix>
            </Filter>
            <Status></Status>
            <Transition>
                  <Days></Days>
                  <StorageClass></StorageClass>
            </Transition>
            <NoncurrentVersionTransition>
                  <NoncurrentDays></NoncurrentDays>
                  <StorageClass></StorageClass>
            </NoncurrentVersionTransition>
      </Rule>
      <Rule>
            <ID></ID>
            <Filter>
                  <Prefix></Prefix>
            </Filter>
            <Status></Status>
            <Expiration>
                  <ExpiredObjectDeleteMarker></ExpiredObjectDeleteMarker>
            </Expiration>
            <NoncurrentVersionExpiration>
                  <NoncurrentDays></NoncurrentDays>
            </NoncurrentVersionExpiration>
      </Rule>
</LifecycleConfiguration>
```

具体内容描述如下：

| 节点名称（关键字）             | 父节点                                                       | 描述                                                         | 类型      | 是否必选 |
| ------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | --------- | -------- |
| LifecycleConfiguration         | 无                                                           | 生命周期配置                                                 | Container | 是       |
| Rule                           | LifecycleConfiguration                                       | 规则描述                                                     | Container | 是       |
| ID                             | LifecycleConfiguration.Rule                                  | 用于唯一地标识规则，长度不能超过255个字符                    | String    | 否       |
| Filter                         | LifecycleConfiguration.Rule                                  | Filter 用于描述规则影响的 Object 集合                        | Container | 是       |
| And                        |   LifecycleConfiguration.Rule<br>.Filter             | 对象筛选器中的一个子集，仅当需要指定多种筛选规则时才需要<br>此元素，例如：同时指定 Prefix 和 Tag 筛选，或同时指定多个 Tag 筛选。|Container|否   |
| Prefix                         | LifecycleConfiguration.Rule<br>.Filter.And                           | 指定规则所适用的前缀。匹配前缀的对象受该规则影响，Prefix <br>最多只能有一个 | String    | 否       |
|  Tag   |    LifecycleConfiguration.Rule<br>.Filter.And   |         标签集合，最多支持10个标签    |   Container  |  否|
|  Key  |    LifecycleConfiguration.Rule<br>.Filter.And.Tag  |    标签的 Key，长度不超过128字节，支持英文字母、数字、空格、加号、<br>减号、下划线、等号、点号、冒号、斜线     |     String	|   否    |
|  Value  |    LifecycleConfiguration.Rule<br>.Filter.And.Tag  |   标签的 Value，长度不超过256字节, 支持英文字母、数字、空格、加号、<br>减号、下划线、等号、点号、冒号、斜线	    |   String	 |  否
| Status                         | LifecycleConfiguration.Rule                                  | 指明规则是否启用，枚举值：Enabled，Disabled                  | String    | 是       |
| Expiration                     | LifecycleConfiguration.Rule                                  | 规则过期属性                                                 | Container | 否       |
| Transition                     | LifecycleConfiguration.Rule                                  | 规则转换属性，用于描述对象何时进行存储类型的转换和转换的存储类型        | Container | 否       |
| Days                           | LifecycleConfiguration.Rule<br>.Transition 或 Expiration      | 指明规则对应的动作在对象最后的修改日期过后多少天操作：<br><li>如果是 Transition，该字段有效值是非负整数<br><li>如果是 Expiration，该字段有效值为正整数，最大支持3650天 | Integer   | 否       |
| Date                           | LifecycleConfiguration.Rule<br>.Transition 或 Expiration      | 指明规则对应的动作在何时操作，支持`2007-12-01T12:00:00.000Z`<br>和`2007-12-01T00:00:00+08:00`这两种格式 | String    | 否       |
| ExpiredObjectDeleteMarker      | LifecycleConfiguration.Rule<br>.Expiration                       | 删除过期对象删除标记，枚举值 true，false                     | String    | 否       |
| AbortIncompleteMultipartUpload | LifecycleConfiguration.Rule                                  | 设置允许分片上传保持运行的最长时间                           | Container | 否       |
| DaysAfterInitiation            | LifecycleConfiguration.Rule<br>.AbortIncompleteMultipartUpload | 指明分片上传开始后多少天内必须完成上传                       | Integer   | 是       |
| NoncurrentVersionExpiration    | LifecycleConfiguration.Rule                                  | 指明非当前版本对象何时过期                                   | Container | 否       |
| NoncurrentVersionTransition    | LifecycleConfiguration.Rule                                  | 指明非当前版本对象何时进行存储类型的转换和转换的存储类型        | Container | 否       |
| NoncurrentDays                 | LifecycleConfiguration.Rule<br>.NoncurrentVersionExpiration <br>或 NoncurrentVersionTransition | 指明规则对应的动作在对象变成非当前版本多少天后执行<br><li>如果是 Transition，该字段有效值是非负整数<br><li>如果是 Expiration，该字段有效值为正整数，最大支持3650天 | Integer   | 否       |
| StorageClass                   | LifecycleConfiguration.Rule<br>.Transition 或 <br>NoncurrentVersionTransition | 指定 Object 沉降后的存储类型，枚举值： STANDARD_IA，MAZ_STANDARD_IA，INTELLIGENT_TIERING，MAZ_INTELLIGENT_TIERING，ARCHIVE，DEEP_ARCHIVE。关于存储类型的介绍，请参见 [存储类型概述](https://cloud.tencent.com/document/product/436/33417) | String    | 是       |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

该响应体为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 请求

```plaintext
PUT /?lifecycle HTTP/1.1
Host:examplebucket-1250000000.cos.ap-beijing.myqcloud.com
Date: Wed, 16 Aug 2017 11:59:33 GMT
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1502855771;1502935771&q-key-time=1502855771;1502935771&q-header-list=content-md5;host&q-url-param-list=lifecycle&q-signature=f3aa2c708cfd8d4d36d658de56973c9cf1c2****
Content-MD5: LcNUuow8OSZMrEDnvndw1Q==
Content-Length: 348
Content-Type: application/x-www-form-urlencoded



<LifecycleConfiguration>
      <Rule>
            <ID>id1</ID>
            <Filter>
                  <Prefix>documents/</Prefix>
            </Filter>
            <Status>Enabled</Status>
            <Transition>
                  <Days>100</Days>
                  <StorageClass>ARCHIVE</StorageClass>
            </Transition>
      </Rule>
      <Rule>
            <ID>id2</ID>
            <Filter>
                  <Prefix>logs/</Prefix>
            </Filter>
            <Status>Enabled</Status>
            <Transition>
                  <Days>10</Days>
                  <StorageClass>STANDARD_IA</StorageClass>
            </Transition>
      </Rule>
</LifecycleConfiguration>
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Date: Wed, 16 Aug 2017 11:59:33 GMT
Server: tencent-cos
x-cos-request-id: NTk5NDMzYTRfMjQ4OGY3Xzc3NGRf****
```
