## 功能描述

PUT Bucket replication 用于向已启用版本控制的存储桶中配置存储桶复制规则。如果存储桶已经配置了存储桶复制规则，那么该请求会替换现有配置。

> !
>
> - 使用该接口时，需确保存储桶已经开启版本控制，开启版本控制的 API 文档请参见 [PUT Bucket versioning](https://cloud.tencent.com/document/product/436/19889)  接口文档。
> - 开启了多 AZ 配置的存储桶，不支持将多 AZ 存储类型复制为单 AZ 存储类型，例如标准存储（多 AZ）类型不支持复制为标准存储类型。

## 请求

#### 请求示例

```http
PUT /?replication HTTP/1.1
Host: <BucketName-APPID>.cos.<Region>.myqcloud.com
Date: GMT Date
Content-MD5: MD5
Authorization: Auth String
request body
```

>? 
> - Host: &lt;BucketName-APPID>.cos.&lt;Region>.myqcloud.com，其中 &lt;BucketName-APPID> 为带 APPID 后缀的存储桶名字，例如 examplebucket-1250000000，可参阅 [存储桶概览 > 基本信息](https://cloud.tencent.com/document/product/436/48921#.E5.9F.BA.E6.9C.AC.E4.BF.A1.E6.81.AF) 和 [存储桶概述 > 存储桶命名规范](https://cloud.tencent.com/document/product/436/13312#.E5.AD.98.E5.82.A8.E6.A1.B6.E5.91.BD.E5.90.8D.E8.A7.84.E8.8C.83) 文档；&lt;Region> 为 COS 的可用地域，可参阅 [地域和访问域名](http://cloud.tencent.com/document/product/436/6224) 文档。
> - Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。
> 

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/436/7728) 文档。

#### 请求体

用户在请求体中设置存储桶复制的具体配置信息。配置信息包括存储桶复制规则的启用状态、优先级、复制内容、筛选范围、目标存储桶的存储桶名称和存储地域等信息。

```http
<ReplicationConfiguration>
    <Role>qcs::cam::uin/<OwnerUin>:uin/<SubUin></Role>
    <Rule>
        <Status></Status>
        <Priority></Priority>
        <ID></ID>
        <Filter>
            <And>
                <Prefix></Prefix>
                <Tag>
                    <Key></Key>
                    <Value></Value>
                </Tag>
                <Tag>
                    <Key></Key>
                    <Value></Value>
                </Tag>
            </And>
        </Filter>
        <Destination>
            <Bucket>qcs::cos:<Region>::<BucketName-APPID></Bucket>
            <StorageClass></StorageClass>
        </Destination>
        <DeleteMarkerReplication>
            <Status></Status>
        </DeleteMarkerReplication>
    </Rule>
</ReplicationConfiguration>
```

具体内容描述如下：

| 节点名称（关键字）       | 父节点                                    | 描述                                                         | 类型      | 是否必选 |
| ------------------------ | ----------------------------------------- | ------------------------------------------------------------ | --------- | -------- |
| ReplicationConfiguration | 无                                        | 说明所有复制配置信息                                       | Container | 是       |
| Role                     | ReplicationConfiguration                  | 发起者身份标示：`qcs::cam::uin/<OwnerUin>:uin/<SubUin>`      | String    | 是       |
| Rule                     | ReplicationConfiguration                  | 具体配置信息，最多支持1000个                                 | Container | 是       |
| ID                       | ReplicationConfiguration.Rule             | 用来标注具体 Rule 的名称                                     | String    | 否       |
| Status                   | ReplicationConfiguration.Rule             | 标识 Rule 是否生效，枚举值：Enabled、Disabled                | String    | 是       |
|Priority                   | ReplicationConfiguration.Rule             | 规则执行优先级，用于处理目标存储桶相同、复制规则命中同一个对象的情况。存储桶复制规则必须全部携带 Prority 或全部不携带 Priority。支持设置 1-1000 范围内的正整数，不同规则的 Priority 值不可重复。<li>所有规则都携带 Priority 时，当目标存储桶相同时，不同规则的筛选 prefix 可以存在重叠。不同规则命中同一个对象时，会优先触发 Priority 值最小的规则。<li>所有规则都不携带 Priority 时，不同规则的筛选 prefix 不允许重叠。|Integer    | 否，同一个存储桶的规则必须全部包含Priority 或者全部不包含 Priority      |
|Filter                   | ReplicationConfiguration.Rule             | 筛选待复制对象。存储桶功能将复制符合 Filter 中设置的对象前缀、对象标签的对象     |Container    | 否       |
|And                   | ReplicationConfiguration.Rule             | 筛选待复制对象时，如果同时需要对象前缀与对象标签条件，需要用 And 包装     |Container    | 否       |
| Prefix                   | ReplicationConfiguration.Rule.Filter.And             | 需要复制的对象前缀  | String    | 否       |
| Tag                  | ReplicationConfiguration.Rule.Filter.And             | 筛选待复制对象时，可以用对象标签（支持多个）作为过滤条件，最多支持填入10个标签。添加标签作为筛选条件后，同步删除标记选项必须置为 false	  | String    | 否       |
| Destination              | ReplicationConfiguration.Rule             | 目标存储桶信息                                               | Container | 是       |
| Bucket                   | ReplicationConfiguration.Rule.Destination | 资源标识符：<br>`qcs::cos:<Region>::<BucketName-APPID>`      | String    | 是       |
| DeleteMarkerReplication             | ReplicationConfiguration.Rule | 是否同步删除标记|Container    | 否       |
|Status             | ReplicationConfiguration.Rule. DeleteMarkerReplication | 是否同步删除标记，支持`Disabled`或`Enabled`。默认值为 `Enabled`，即同步删除标记|String    | 否       |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/436/7729) 文档。

#### 响应体

该响应体为空。

#### 错误码

此接口遵循统一的错误响应和错误码，详情请参见 [错误码](https://cloud.tencent.com/document/product/436/7730) 文档。

## 实际案例

#### 案例一：根据前缀筛选的存储桶复制规则
#### 请求

以下 PUT Bucket replication 请求向存储桶`originbucket-1250000000`中添加一条存储桶复制配置。该存储桶复制配置中，指定复制前缀为`testPrefix`的对象内容，目标存储桶为广州的`destinationbucket-1250000000`。

```shell
PUT /?replication HTTP/1.1
Date: Mon, 28 Aug 2017 02:53:38 GMT
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0a1ICvR****&q-sign-time=1503888878;1503889238&q-key-time=1503888878;1503889238&q-header-list=host&q-url-param-list=replication&q-signature=254bf9cd3d6615e89a36ab652437f9d45c5f****
Content-MD5: AAq9nzrpsz5LJ4UEe1f6Q==
Host: originbucket-1250000000.cos.ap-guangzhou.myqcloud.com
Content-Length: 312

<ReplicationConfiguration>
    <Role>qcs::cam::uin/100000000001:uin/100000000001</Role>
    <Rule>
        <Status>Enabled</Status>
        <ID>RuleId_01</ID>
        <Prefix>testPrefix</Prefix>
        <Destination>
            <Bucket>qcs::cos:ap-guangzhou::destinationbucket-1250000000</Bucket>
        </Destination>
    </Rule>
</ReplicationConfiguration>
```

#### 响应

上述请求后，COS 返回以下响应，表明当前该跨地域配置已经成功设置完毕。

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 0
Connection: keep-alive
Date: Fri, 14 Apr 2019 07:06:19 GMT
Server: tencent-cos
x-cos-bucket-region: ap-guangzhou
x-cos-request-id: NWQwMzQ3NmJfMjRiMjU4NjRfOTM4NV82ZDU1****
x-cos-trace-id: OGVmYzZiMmQzYjA2OWNhODk0NTRkMTBiOWVmMDAxODc0OWRkZjk0ZDM1NmI1M2E2MTRlY2MzZDhmNmI5MWI1OWE4OGMxZjNjY2JiNTBmMTVmMWY1MzAzYzkyZGQ2ZWM4MzUyZTg1NGRhNWY0NTJiOGUyNTViYzgyNzgxZTEwOTY=
```

#### 案例二：根据标签筛选的存储桶复制规则
#### 请求

以下 PUT Bucket replication 请求向存储桶`originbucket-1250000000`中添加一条存储桶复制配置。该存储桶复制配置中，指定复制前缀为`test1`、标签为`<111, 232>`的对象，目标存储桶为广州的`destinationbucket-1250000000`。设置标签筛选后，规则内的同步删除对象必须置为 Disabled。

```shell
PUT /?replication HTTP/1.1
Host: originbucket-1250000000.cos.ap-guangzhou.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=AKIDYv3vWrwkHXVDfqkNj*********&q-sign-time=1667303319;1668303369&q-key-time=1667303319;1668303369&q-url-param-list=replication&q-header-list=content-md5;host&q-signature=78c13df3ce3bca422fcb994*****
Content-Md5: Hmy/6lHINHLKhp/PY****
Content-Length: 674
Content-Type: application/x-www-form-urlencoded

<ReplicationConfiguration>
    <Role>qcs::cam::uin/100000000001:uin/100000000001</Role>
    <Rule>
        <Status>Enabled</Status>
        <Filter>
            <And>
                <Prefix>test1</Prefix>
                <Tag>
                    <Key>111</Key>
                    <Value>222</Value>
                </Tag>
            </And>
        </Filter>
        <Destination>
            <Bucket>qcs::cos:ap-guangzhou::destinationbucket-1250000000</Bucket>
            <StorageClass>Standard</StorageClass>
        </Destination>
        <DeleteMarkerReplication>
            <Status>Disabled</Status>
        </DeleteMarkerReplication>
    </Rule>
</ReplicationConfiguration>
```

#### 响应

上述请求后，COS 返回以下响应，表明当前该跨地域配置已经成功设置完毕。
```shell
HTTP/1.1 200 OK
Content-Length: 0
Connection: keep-alive
Date: Tue, 01 Nov 2022 11:49:48 GMT
Server: tencent-cos
x-cos-bucket-region: ap-guangzhou
x-cos-request-id: NjM2MTA3ZGNfNmE1MGI3MDlfYWU5N1*******
```

#### 案例三：设置多个复制到同一目标存储桶、筛选前缀有重叠的规则，通过 Priority 设置生效的优先级
#### 请求

以下 PUT Bucket replication 请求向存储桶`originbucket-1250000000`中添加两条存储桶复制配置规则。
- 规则1：指定复制前缀为`test1`、标签为`<a,	a>`的对象，目标存储桶为广州的`destinationbucket-1250000000`，目标存储类型为`Standard`，规则内的同步删除对象必须置为 Disabled，Priority 为1。
- 规则2:指定复制前缀为`test1`、标签为`<b,b>`的对象，目标存储桶为广州的`destinationbucket-1250000000`，目标存储类型为`Standard_IA`，规则内的同步删除对象必须置为 Disabled，Priority 为2。

用户向存储桶`originbucket-1250000000`上传对象`test1/temp.txt`，上传同时打标签`<a,a>`和`<b,b>`，此时根据 Priority，规则1优先生效，复制到存储桶`destinationbucket-1250000000`对象的类型为`Standard`。

```shell
PUT /?replication HTTP/1.1
Host: originbucket-1250000000.cos.ap-guangzhou.myqcloud.com
Authorization: q-sign-algorithm=sha1&q-ak=AKIDYv3vWrwkHXVDfqkNjoc9PP8a******&q-sign-time=1667309117;1668309167&q-key-time=1667309117;1668309167&q-url-param-list=replication&q-header-list=content-md5;host&q-signature=b5730a15142d4bbc9974e42814918435*******
Content-Md5: OngWIL6wb2pnJZHk*****
Content-Length: 1351
Content-Type: application/x-www-form-urlencoded

<ReplicationConfiguration>
    <Role>qcs::cam::uin/100000000001:uin/100000000001</Role>
    <Rule>
        <Status>Enabled</Status>
        <Priority>1</Priority>
        <Filter>
            <And>
                <Prefix>test1</Prefix>
                <Tag>
                    <Key>a</Key>
                    <Value>a</Value>
                </Tag>
            </And>
        </Filter>
        <Destination>
            <Bucket>qcs::cos:ap-guangzhou::destinationbucket-1250000000</Bucket>
            <StorageClass>Standard</StorageClass>
        </Destination>
        <DeleteMarkerReplication>
            <Status>Disabled</Status>
        </DeleteMarkerReplication>
    </Rule>
    <Role>qcs::cam::uin/100000000001:uin/100000000001</Role>
    <Rule>
        <Status>Enabled</Status>
        <Priority>2</Priority>
        <Filter>
            <And>
                <Prefix>test1</Prefix>
                <Tag>
                    <Key>b</Key>
                    <Value>b</Value>
                </Tag>
            </And>
        </Filter>
        <Destination>
            <Bucket>qcs::cos:ap-guangzhou::destinationbucket-1250000000</Bucket>
            <StorageClass>Standard_IA</StorageClass>
        </Destination>
        <DeleteMarkerReplication>
            <Status>Disabled</Status>
        </DeleteMarkerReplication>
    </Rule>
</ReplicationConfiguration>
```

#### 响应
```shell
HTTP/1.1 200 OK
Content-Length: 0
Connection: keep-alive
Date: Tue, 01 Nov 2022 13:26:23 GMT
Server: tencent-cos
x-cos-bucket-region: ap-guangzhou
x-cos-request-id: NjM2MTFlN2ZfYjA1MGI3MDlfMjQ2ZmZfOWE******
```

