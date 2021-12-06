## 功能描述
UpdateStream 用于更新推流配置。

## 请求

#### 请求示例

```plaintext
PUT /stream/<StreamName>?template&switch HTTP/1.1
Host: iss.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

>?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/1344/50456) 文档）。


#### 请求参数
此接口无请求参数。


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1344/50451) 文档。

#### 请求体
该请求操作的实现需要有如下请求体。

```plaintext
<Request>
    <ProjectId>pj1460606b9752148c4ab182f55163ba7cd</ProjectId>
    <Switch>Enabled</Switch>
    <TemplateList>
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
        <Tag>Snapshot</Tag>
        <Status>Off</Status>
        <Output>
            <Region>ap-beijing</Region>
            <BucketId>abc-1250000000</BucketId>
            <Object>snapshot-${Number}.jpg</Object>
        </Output>
        <Notify>http://callback.com/notify</Notify>
    </TemplateList>
    <TemplateList>
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
        <Tag>Snapshot</Tag>
        <Status>On</Status>
        <Output>
            <Region>ap-beijing</Region>
            <BucketId>abc-1250000000</BucketId>
            <Object>snapshot-${Number}.jpg</Object>
        </Output>
        <Notify>http://callback.com/notify</Notify>
    </TemplateList>
</Request>
```

具体数据描述如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 是否必选 |
| ------------------ | ------ | -------------- | --------- | ---- |
| Request            | 无     | 保存请求的容器 | Container | 是   |

Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 | 默认值| 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ----| ---- | ----- |
| Switch             | Request | 推流状态                  | String | 否   | Enabled | Enabled，Disabled |
| TemplateList       | Request | 模板列表                  | Container | 否   | 无 | 模板个数不能超过10个|


Container 类型 TemplateList 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 | 默认值       | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| TemplateId         | Request.TemplateList | 模板 ID | String    | 是   | 无  | 无 |
| Tag                | Request.TemplateList | 模板 Tag | String    | 是   | 无  | Snapshot 截图类型、Transcode 转码类型 |
| Status             | Request.TemplateList | 模板启用状态 | String    | 是   | 无  | 1、On 表示启用，2、Off 表示停用 |
| Output             | Request.TemplateList | 模板输出信息 | Container    | 是   | 无  | 无 |
| Notify             | Request.TemplateList | 模板输出通知地址 | String    | 否   | 无  | url 地址 |

Container 类型 Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 | 默认值       | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Region             | Request.TemplateList.Output | bucket 的地域 | String    | 是   | 无  | 无 |
| Bucket             | Request.TemplateList.Output | bucket 的 ID | String    | 是   | 无  | 无 |
| Object             | Request.TemplateList.Output | 输出对象格式 | Container    | 是   | 无  | 当模板类型为 Snapshot 时，必须包含 ${Number} 参数。如 Object 为 snapshot-${Number}.jpg |

## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1344/50452) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```plaintext
<Response>
    <ProjectId>pj1460606b9752148c4ab182f55163ba7cd</ProjectId>
    <Name>streamName</Name>
    <Duration>5</Duration>
    <Type>HLS</Type>
    <Switch>Enabled</Switch>
    <StreamUrl>rtmp://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/live/streamName</StreamUrl>
    <PlayUrl>http://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/streamName/playlist.m3u8</PlayUrl>
    <Bucket>
        <Region>ap-beijing</Region>
        <BucketId>examplebucket-1250000000</BucketId>
        <Prefix>/streamName</Prefix>
    </Bucket>
    <TemplateList>
        <TemplateId></TemplateId>
        <Tag></Tag>
        <Name></Name>
        <Status></Status>
        <Output>
            <Region>ap-beijing</Region>
            <Bucket>abc-1250000000</Bucket>
            <Object>snapshot-${Number}.jpg</Object>
        </Output>
        <Notify></Notify>
    </TemplateList>
    <TemplateList>
        <TemplateId></TemplateId>
        <Tag></Tag>
        <Name></Name>
        <Status></Status>
        <Output>
            <Region>ap-beijing</Region>
            <Bucket>abc-1250000000</Bucket>
            <Object>snapshot-${Number}.jpg</Object>
        </Output>
        <Notify></Notify>
    </TemplateList>
    <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
    <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述                                       | 类型      |
| :----------------- | :----- | :----------------------------------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |


Container节点Response的内容：

| 节点名称（关键字） | 父节点                | 描述                                                         | 类型      |
| :----------------- | :-------------------- | :----------------------------------------------------------- | :-------- |
| ProjectId          | Response | 项目 Id                                                       | String    |
| Name               | Response | 流名称                                                       | String    |
| Duration           | Response | 录制周期                                                     | String    |
| Type               | Response | 录制格式                                                     | String    |
| Switch             | Response | 推流状态                                                     | String    |
| StreamUrl          | Response | 推流地址                                                     | String    |
| PlayUrl            | Response | 播放地址                                                     | String    |
| UpdateTime         | Response | 更新时间                                                     | String    |
| CreateTime         | Response | 创建时间                                                     | String    |
| TemplateList       | Response | 参考更新项目接口的模板列表                                     | Container |
| Bucket             | Response | 存储 Bucket 信息                                               | Container |

Container 类型 Bucket 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 是否必选 | 默认值       | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Region            | Response.Bucket     | bucket 地域 | String      | 是   | 无 | 无|
| BucketId          | Response.Bucket     | bucket 的 ID | String      | 是   | 无  | 无 |
| Prefix            | Response.Bucket     | 对象 key 前缀 | String      | 否   | 无  | 无 |

Container 节点 TemplateList 的内容：

| 节点名称（关键字） | 父节点                | 描述                                                         | 类型      |
| :----------------- | :-------------------- | :----------------------------------------------------------- | :-------- |
| TemplateId      | Response.TemplateList | 模板 ID                                               | String    |
| Tag             | Response.TemplateList | 模板类型                                               | String    |
| Name            | Response.TemplateList | 模板名称                                               | String    |
| Status          | Response.TemplateList | 模板状态                                               | String    |
| Notify          | Response.TemplateList | 模板回调                                                | String    |
| Output          | Response.TemplateList | 模板输出                                                | Container    |


Container节点 Output 的内容：

| 节点名称（关键字） | 父节点                   | 描述                                                         | 类型   |
| ------------------ | ------------------------ | ------------------------------------------------------------ | ------ |
| Region             | Response.TemplateList.Output | 存储桶的地域                                   | String |
| Bucket             | Response.TemplateList.Output | 存储结果的存储桶                                | String |
| Object             | Response.TemplateList.Output | 结果文件名                               | String |

#### 错误码
常见的错误信息请参阅 [错误码](https://cloud.tencent.com/document/product/1344/50457) 文档。

## 实际案例

#### 案例一：更新推流状态信息

#### 请求



```plaintext
PUT /stream/<StreamName>?switch HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host: iss.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml

<Request>
    <ProjectId>pj1460606b9752148c4ab182f55163ba7cd</ProjectId>
    <Switch>Enabled</Switch>
</Request>
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-iss
x-iss-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<Response>
    <ProjectId>pj1460606b9752148c4ab182f55163ba7cd</ProjectId>
    <Name>streamName</Name>
    <Duration>5</Duration>
    <Type>HLS</Type>
    <Switch>Enabled</Switch>
    <StreamUrl>rtmp://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/live/streamName</StreamUrl>
    <PlayUrl>http://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/streamName/playlist.m3u8</PlayUrl>
    <Bucket>
        <Region>ap-beijing</Region>
        <BucketId>examplebucket-1250000000</BucketId>
        <Prefix>/streamName</Prefix>
    </Bucket>
    <TemplateList>
        <TemplateId></TemplateId>
        <Tag></Tag>
        <Name></Name>
        <Status></Status>
        <Output>
            <Region>ap-beijing</Region>
            <Bucket>abc-1250000000</Bucket>
            <Object>snapshot-${Number}.jpg</Object>
        </Output>
        <Notify></Notify>
    </TemplateList>
    <TemplateList>
        <TemplateId></TemplateId>
        <Tag></Tag>
        <Name></Name>
        <Status></Status>
        <Output>
            <Region>ap-beijing</Region>
            <Bucket>abc-1250000000</Bucket>
            <Object>snapshot-${Number}.jpg</Object>
        </Output>
        <Notify></Notify>
    </TemplateList>
    <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
    <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
</Response>
```

#### 案例二：更新推流模板信息

#### 请求

```plaintext
PUT /stream/<StreamName>?template HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0ea057
Host: iss.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml

<Request>
    <ProjectId>pj1460606b9752148c4ab182f55163ba7cd</ProjectId>
    <TemplateList>
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
        <Tag>Snapshot</Tag>
        <Status>Off</Status>
        <Output>
            <Region>ap-beijing</Region>
            <BucketId>abc-1250000000</BucketId>
            <Object>snapshot-${Number}.jpg</Object>
        </Output>
        <Notify>http://callback.com/notify</Notify>
    </TemplateList>
    <TemplateList>
        <TemplateId>t1460606b9752148c4ab182f55163ba7cd</TemplateId>
        <Tag>Snapshot</Tag>
        <Status>On</Status>
        <Output>
            <Region>ap-beijing</Region>
            <BucketId>abc-1250000000</BucketId>
            <Object>snapshot-${Number}.jpg</Object>
        </Output>
        <Notify>http://callback.com/notify</Notify>
    </TemplateList>
</Request>
```

#### 响应

```plaintext
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-iss
x-iss-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhf****

<Response>
    <ProjectId>pj1460606b9752148c4ab182f55163ba7cd</ProjectId>
    <Name>streamName</Name>
    <Duration>5</Duration>
    <Type>HLS</Type>
    <Switch>Enabled</Switch>
    <StreamUrl>rtmp://examplebucket-1250000000.cos.ap-beijing.myqcloud.com/live/streamName</StreamUrl>
    <PlayUrl>http://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com/streamName/playlist.m3u8</PlayUrl>
    <Bucket>
        <Region>ap-beijing</Region>
        <BucketId>examplebucket-1250000000</BucketId>
        <Prefix>/streamName</Prefix>
    </Bucket>
    <TemplateList>
        <TemplateId></TemplateId>
        <Tag></Tag>
        <Name></Name>
        <Status></Status>
        <Output>
            <Region>ap-beijing</Region>
            <Bucket>abc-1250000000</Bucket>
            <Object>snapshot-${Number}.jpg</Object>
        </Output>
        <Notify></Notify>
    </TemplateList>
    <TemplateList>
        <TemplateId></TemplateId>
        <Tag></Tag>
        <Name></Name>
        <Status></Status>
        <Output>
            <Region>ap-beijing</Region>
            <Bucket>abc-1250000000</Bucket>
            <Object>snapshot-${Number}.jpg</Object>
        </Output>
        <Notify></Notify>
    </TemplateList>
    <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
    <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
</Response>
```
