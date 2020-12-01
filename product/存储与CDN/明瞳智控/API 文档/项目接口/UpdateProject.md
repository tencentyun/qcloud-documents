## 功能描述
UpdateProject 用于更新项目配置。

## 请求
### 请求实例

```shell
PUT /project/<ProjectId>?baseinfo&serviceconf&template&status HTTP/1.1
Host: iss.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

>? Authorization: Auth String （详情请查阅 [请求签名](https://cloud.tencent.com/document/product/436/7778) 文档）。


### 请求头
#### 公共头部
该请求操作的实现使用公共请求头，了解公共请求头详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/460/42865) 文档。
#### 非公共头部
该请求操作无特殊的请求头部信息。

### 请求体
该请求操作的实现需要有如下请求体。


```shell
<Request>
    <Name>ProjectName</Name>
    <Desc>ProjectDesc</Desc>
    <Status>Active</Status>
    <Bucket>
        <Region>ap-beijing</Region>
        <BucketId>bucket-1250000000</BucketId>
        <Prefix>/iss</Prefix>
    </Bucket>
    <ServiceConf>
        <Notify>http://callback.com/notify</Notify>
    </ServiceConf>
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

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 必选 |
| ------------------ | ------ | -------------- | --------- | ---- |
| Request            | 无     | 保存请求的容器 | Container | 是   |

Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- | ----- |
| Mode               | Request | 接入类型                                              | String    | 否   | 1、HTTP |
| Status             | Request | 项目状态                                              | String    | 否   | 1、Active 表示启用 2、Paused 表示停用 |
| Name               | Request | 项目名称 仅支持中文、英文、数字、_、-和*                    | String    | 否   | 1、长度不超过128 |
| Desc               | Request | 项目描述 仅支持中文、英文、数字、_、-和*                    | String    | 否   | 1、长度不超过256 |
| Bucket             | Request | bucket 信息                                             | Container | 否   | 无 |
| ServiceConf        | Request | 服务配置                                                | Container | 否   | 无 |
| TemplateList       | Request | 模板列表                                                | Container | 否   | 无 |


Container 类型 Bucket 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Region             | Request.Bucket | bucket 地区 | String    | 是   | 无  | 无|
| BucketId         | Request.Bucket | bucket 的 ID | String    | 是   | 无  | 无 |
| Prefix             | Request.Bucket | 对象 key 前缀 | String    | 否   | 无  | 无 |


Container 类型 ServiceConf 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Notify             | Request.ServiceConf | 服务回调地址 | String    | 否   | 无  | url地址 |

Container 类型 TemplateList 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| TemplateId         | Request.TemplateList | 模板 ID | String    | 是   | 无  | 无 |
| Tag                | Request.TemplateList | 模板 Tag | String    | 是   | 无  | 1、Snapshot 截图类型、Transcode 转码类型 |
| Status             | Request.TemplateList | 模板启用状态 | String    | 是   | 无  | 1、On 表示启用 2、Off 表示停用 |
| Output             | Request.TemplateList | 模板输出信息 | Container    | 是   | 无  | 无 |
| Notify             | Request.TemplateList | 模板输出通知地址 | String    | 否   | 无  | url 地址 |

Container 类型 Output 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述                                                     | 类型      | 必选 | 默认值       | 限制  |
| ------------------ | ------- | -------------------------------------------------------- | --------- | ---- |---| ---- |
| Region             | Request.TemplateList.Output | bucket 的园区 | String    | 是   | 无  | 无 |
| Bucket             | Request.TemplateList.Output | bucket 的 ID | String    | 是   | 无  | 无 |
| Object             | Request.TemplateList.Output | 输出对象格式 | Container    | 是   | 无  | 1、当模板类型为 Snapshot 时，必须包含 ${Number} 参数。如 Object 为 snapshot-${Number}.jpg |

## 响应

### 响应头

#### 公共响应头
该响应包含公共响应头，了解公共响应头详情请参见 [公共响应头部]( https://cloud.tencent.com/document/product/460/42866) 文档。
#### 特有响应头
该响应无特殊的响应头。

### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```shell
<Response>
    <Name>ProjectName</Name>
    <Desc>ProjectDesc</Desc>
    <ProjectId>pj1460606b9752148c4ab182f55163ba7cd</ProjectId>
    <Mode>HTTP</Mode>
    <Status>Active</Status>
    <Bucket>
        <Region>ap-beijing</Region>
        <BucketId>bucket-1250000000</BucketId>
        <Prefix>/iss</Prefix>
    </Bucket>
    <ServiceConf>
        <Notify>http://callback.com/notify</Notify>
    </ServiceConf>
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
| Name               | Response | 项目名称                                                     | String    |
| Desc               | Response | 项目描述                                                     | String    |
| UpdateTime         | Response | 更新时间                                                     | String    |
| CreateTime         | Response | 创建时间                                                     | String    |
| Mode               | Response | 接入类型                                                     | String    |
| Status             | Response | 项目状态                                                     | String    |
| UpdateTime         | Response | 更新时间                                                     | String    |
| CreateTime         | Response | 创建时间                                                      | String    |
| Bucket             | Response | 参考请求中的 Bucke t参数                                         | Container |
| ServiceConf        | Response | 参考请求中的 ServiceConf 参数                                    | Container |
| TemplateList       | Response | 参考请求中的 TemplateList 参数                                   | Container |

### 错误码

该请求无特有错误信息，常见的错误信息请参见 [错误码](https://cloud.tencent.com/document/product/1344/50457) 文档。

## 实际案例

### 更新项目状态信息

```shell
PUT /project/<ProjectId>?status HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host: iss.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml

<Request>
    <Status>Active</Status>
</Request>
```

### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-iss
x-iss-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=

<Response>
    <Name>ProjectName</Name>
    <Desc>ProjectDesc</Desc>
    <ProjectId>pj1460606b9752148c4ab182f55163ba7cd</ProjectId>
    <Mode>HTTP</Mode>
    <Status>Active</Status>
    <Bucket>
        <Region>ap-beijing</Region>
        <BucketId>bucket-1250000000</BucketId>
        <Prefix>/iss</Prefix>
    </Bucket>
    <ServiceConf>
        <Notify>http://callback.com/notify</Notify>
    </ServiceConf>
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
    <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
    <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
</Response>
```

### 更新项目基础信息

```shell
PUT /project/<ProjectId>?baseinfo HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host: iss.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml

<Request>
    <Name>ProjectName</Name>
    <Desc>ProjectDesc</Desc>
</Request>
```

### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-iss
x-iss-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=

<Response>
    <Name>ProjectName</Name>
    <Desc>ProjectDesc</Desc>
    <ProjectId>pj1460606b9752148c4ab182f55163ba7cd</ProjectId>
    <Mode>HTTP</Mode>
    <Status>Active</Status>
    <Bucket>
        <Region>ap-beijing</Region>
        <BucketId>bucket-1250000000</BucketId>
        <Prefix>/iss</Prefix>
    </Bucket>
    <ServiceConf>
        <Notify>http://callback.com/notify</Notify>
    </ServiceConf>
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
    <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
    <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
</Response>
```

### 更新项目服务配置信息

```shell
PUT /project/<ProjectId>?serviceconf HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host: iss.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml

<Request>
    <ServiceConf>
        <Notify>http://callback.com/notify</Notify>
    </ServiceConf>
</Request>
```

### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-iss
x-iss-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=

<Response>
    <Name>ProjectName</Name>
    <Desc>ProjectDesc</Desc>
    <ProjectId>pj1460606b9752148c4ab182f55163ba7cd</ProjectId>
    <Mode>HTTP</Mode>
    <Status>Active</Status>
    <Bucket>
        <Region>ap-beijing</Region>
        <BucketId>bucket-1250000000</BucketId>
        <Prefix>/iss</Prefix>
    </Bucket>
    <ServiceConf>
        <Notify>http://callback.com/notify</Notify>
    </ServiceConf>
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
    <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
    <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
</Response>
```

### 更新项目所有信息

```shell
PUT /project/<ProjectId> HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host: iss.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml

<Request>
    <Name>ProjectName</Name>
    <Desc>ProjectDesc</Desc>
    <Status>Active</Status>
    <ServiceConf>
    </ServiceConf>
    <TemplateList>
    </TemplateList>
</Request>
```

### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-iss
x-iss-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=

<Response>
    <Name>ProjectName</Name>
    <Desc>ProjectDesc</Desc>
    <ProjectId>pj1460606b9752148c4ab182f55163ba7cd</ProjectId>
    <Mode>HTTP</Mode>
    <Status>Active</Status>
    <Bucket>
        <Region>ap-beijing</Region>
        <BucketId>bucket-1250000000</BucketId>
        <Prefix>/iss</Prefix>
    </Bucket>
    <ServiceConf>
    </ServiceConf>
    <TemplateList>
    </TemplateList>
    <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
    <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
</Response>
```


### 更新项目模板信息

```shell
PUT /project/<ProjectId>?template HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0e****
Host: iss.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml

<Request>
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

### 响应

```shell
HTTP/1.1 200 OK
Content-Type: application/xml
Content-Length: 100
Connection: keep-alive
Date: Thu, 15 Jun 2017 12:37:29 GMT
Server: tencent-iss
x-iss-request-id: NTk0MjdmODlfMjQ4OGY3XzYzYzhfMjc=

<Response>
    <Name>ProjectName</Name>
    <Desc>ProjectDesc</Desc>
    <ProjectId>pj1460606b9752148c4ab182f55163ba7cd</ProjectId>
    <Mode>HTTP</Mode>
    <Status>Active</Status>
    <Bucket>
        <Region>ap-beijing</Region>
        <BucketId>bucket-1250000000</BucketId>
        <Prefix>/iss</Prefix>
    </Bucket>
    <ServiceConf>
        <Notify>http://callback.com/notify</Notify>
    </ServiceConf>
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
    <CreateTime>2020-08-05T11:35:24+0800</CreateTime>
    <UpdateTime>2020-08-31T16:15:20+0800</UpdateTime>
</Response>
```
