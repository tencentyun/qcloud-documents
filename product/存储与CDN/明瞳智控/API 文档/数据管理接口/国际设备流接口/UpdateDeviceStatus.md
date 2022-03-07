## 功能描述

UpdateDeviceStatus 用于开启设备拉流到对象存储（Cloud Object Storage，COS），或者关闭设备拉流停止上传 COS。

## 启动请求

#### 请求示例

```plaintext
PUT /device?status=on HTTP/1.1
Host: iss.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/1344/50456) 文档）。
>


#### 请求参数

Url 的具体内容如下：

| 节点名称（关键字） | 父节点 | 描述   | 类型   | 是否必选 |
| :----------------- | :----- | :----- | :----- | :--- |
| status             | 无     | 开启 on | String | 是   |




#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1344/50451) 文档。

#### 请求体
只支持单个设备的状态变更，不支持批量变更。


```plaintext
<Request>
    <Devicelist>
        <Gbid>Gbid</Gbid>
    </Devicelist>
    <ProjectId>ProjectId</ProjectId>
</Request>
```


请求体的具体内容如下：

| 节点名称（关键字） | 父节点 | 描述   | 类型   | 是否必选 |
| :----------------- | :----- | :----- | :----- | :--- |
| Request            | 无     | 开启 on | String | 是   |

Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述               | 类型   | 是否必选 |
| ------------------ | ------- | ------------------ | ------ | ---- |
| Devicelist         | Request | 待添加的 device 列表 | Array  | 是   |
| ProjectId          | Request | 项目 ID             | String | 是   |

Array 类型 Devicelist 的具体数据描述如下：

| 节点名称（关键字） | 父节点                    | 描述   | 类型   | 是否必选 | 默认值 | 限制 |
| ------------------ | ------------------------- | ------ | ------ | ---- | ------ | ---- |
| Gbid               | Request.Devicelist.Device | 设备 ID | String | 是   | 无     | 无   |




## 启动响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1344/50452) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```plaintext
<Response>
    <RequestId>NjBmOTVhOWZfOTBmYTUwNjRfN2I4****</RequestId>
    <ChannelList>
        <Channel>
            <ChannelId></ChannelId>
        </Channel>
    </ChannelList>
    <FailedChannelList>
        <Channel>
            <ChannelId/>
            <Msg>Camera offline</Msg>
        </Channel>
    </FailedChannelList>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述                                       | 类型      |
| :----------------- | :----- | :----------------------------------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述     | 类型   |
| :----------------- | :------- | :------- | :----- |
| RequestId          | Response | 请求 ID   | String |
| ChannelList        | Response | 成功列表 | Array  |
| FailedChannelList  | Response | 失败列表 | Array  |

Array 类型 ChannelList 的具体数据描述如下：

| 节点名称（关键字） | 父节点               | 描述         | 类型      |
| ------------------ | -------------------- | ------------ | --------- |
| Channel            | Response.ChannelList | 通道详细信息 | Container |

Container 类型 Channel 的具体数据描述如下：

| 节点名称（关键字） | 父节点                       | 描述   | 类型   |
| ------------------ | ---------------------------- | ------ | ------ |
| ChannelId          | Response.ChannelList.Channel | 通道 ID | String |

Array 类型 FailedChannelList 的具体数据描述如下：

| 节点名称（关键字） | 父节点                     | 描述         | 类型      |
| ------------------ | -------------------------- | ------------ | --------- |
| Channel            | Response.FailedChannelList | 通道详细信息 | Container |

Container 类型 Channel 的具体数据描述如下：

| 节点名称（关键字） | 父节点                       | 描述     | 类型   |
| ------------------ | ---------------------------- | -------- | ------ |
| ChannelId          | Response.ChannelList.Channel | 通道 ID   | String |
| Msg                | Response.ChannelList.Channel | 失败信息 | String |

#### 错误码
常见的错误信息请参阅 [错误码](https://cloud.tencent.com/document/product/1344/50457) 文档。

## 实际案例（启动）


#### 开启设备详情

#### 请求

```plaintext
PUT /device?status=on HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0*****
Host: iss.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml

<Request>
    <Devicelist>
        <Gbid></Gbid>
    </Devicelist>
    <ProjectId>p15a20e50c92f4b089bf11bf77b558809</ProjectId>
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
    <RequestId>NjBmOTVhOWZfOTBmYTUwNjRfN2I4****</RequestId>
    <ChannelList>
        <Channel>
            <ChannelId></ChannelId>
        </Channel>
    </ChannelList>
    <FailedChannelList>
        <Channel>
            <ChannelId/>
            <Msg>Camera offline</Msg>
        </Channel>
    </FailedChannelList>
</Response>
```


## 关闭请求

#### 请求示例

```plaintext
PUT /device?status=off HTTP/1.1
Host: iss.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

<body>
```

>?Authorization: Auth String（详情请参见 [请求签名](https://cloud.tencent.com/document/product/1344/50456) 文档）。


#### 请求参数

Url 参数的具体内容如下：

| 节点名称（关键字） | 父节点 | 描述    | 类型   | 是否必选 |
| :----------------- | :----- | :------ | :----- | :--- |
| status             | 无     | 关闭 off | String | 是   |




#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1344/50451) 文档。

#### 请求体



```plaintext
<Request>
    <Devicelist>
        <Gbid>Gbid</Gbid>
    </Devicelist>
    <ProjectId>ProjectId</ProjectId>
</Request>
```



 请求体的具体内容如下：

| 节点名称（关键字） | 父节点 | 描述   | 类型   | 是否必选 |
| :----------------- | :----- | :----- | :----- | :--- |
| Request            | 无     | 开启 on | String | 是   |

Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述               | 类型   | 是否必选 |
| ------------------ | ------- | ------------------ | ------ | ---- |
| Devicelist         | Request | 待添加的 device 列表 | Array  | 是   |
| ProjectId          | Request | 项目 ID             | String | 是   |

Array 类型 Devicelist 的具体数据描述如下：

| 节点名称（关键字） | 父节点                    | 描述   | 类型   | 是否必选 | 默认值 | 限制 |
| ------------------ | ------------------------- | ------ | ------ | ---- | ------ | ---- |
| Gbid               | Request.Devicelist.Device | 设备 ID | String | 是   | 无     | 无   |



## 关闭响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1344/50452) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```plaintext
<Response>
    <RequestId/>
    <ChannelList>
        <Channel>
            <ChannelId>ChannelId</ChannelId>
            <Msg/>
        </Channel>
    </ChannelList>
    <FailedChannelList>
        <Channel>
            <ChannelId>ChannelId</ChannelId>
            <Msg/>
        </Channel>
    </FailedChannelList>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container节点Response的内容：

| 节点名称（关键字） | 父节点   | 描述     | 类型   |
| :----------------- | :------- | :------- | :----- |
| RequestId          | Response | 请求 ID   | String |
| ChannelList        | Response | 成功列表 | Array  |
| FailedChannelList  | Response | 失败列表 | Array  |

Array 类型 ChannelList/FailedChannelList 的具体数据描述如下：

| 节点名称（关键字） | 父节点               | 描述         | 类型      |
| ------------------ | -------------------- | ------------ | --------- |
| Channel            | Response.ChannelList | 通道详细信息 | Container |

Container 类型 Channel 的具体数据描述如下：

| 节点名称（关键字） | 父节点                       | 描述     | 类型   |
| ------------------ | ---------------------------- | -------- | ------ |
| ChannelId          | Response.ChannelList.Channel | 通道 ID   | String |
| Msg                | Response.ChannelList.Channel | 失败原因 | String |

#### 错误码
常见的错误信息请参阅 [错误码](https://cloud.tencent.com/document/product/1344/50457) 文档。

## 实际案例（关闭）

#### 关闭设备详情

#### 请求

```plaintext
PUT /device?status=off HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0*****
Host: iss.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml

<Request>
    <Devicelist>
    		<Gbid></Gbid>
    </Devicelist>
    <ProjectId></ProjectId>
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
    <RequestId/>
    <ChannelList>
        <Channel>
            <ChannelId></ChannelId>
            <Msg>OK</Msg>
        </Channel>
        <Channel>
            <ChannelId></ChannelId>
            <Msg>OK</Msg>
        </Channel>
    </ChannelList>
</Response>
```


