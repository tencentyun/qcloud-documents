## 功能描述
DescribeStream 用于查看国标实时流地址。

## 请求

#### 请求示例

```plaintext
GET /device/stream?gbid=34020000001320000184&projectId=p15a20e50c92f4b089bf11bf77b558809 HTTP/1.1
Host: iss.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

```

>?Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/1344/50456) 文档）。


#### 请求参数

参数的具体内容如下：

|节点名称（关键字）|父节点     |描述                    |   类型    |   是否必选    |
|:---           |:--       |:--                    |   :--     |   :--    |
| projectId   | 无        | 项目 Id                 | String     | 是 |
| gbid  | 无        | 国标 id              | String | 是 |
| outProtocol | 无 | 流播放协议：rtmp、hls、rtc、flv | String | 否，不填默认 flv |

#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1344/50451) 文档。



#### 请求体
该请求的请求体为空。


## 响应

#### 响应头

此接口仅返回公共响应头部，详情请参见 [公共响应头部](https://cloud.tencent.com/document/product/1344/50452) 文档。

#### 响应体
该响应体返回为 **application/xml** 数据，包含完整节点数据的内容展示如下：

```plaintext
<Response>
    <RequestId>NjBmOTVhOWZfOTBmYTUwNjRfN2I4****</RequestId>
    <Code>200</Code>
    <Message>OK</Message>
    <ChannelList>
        <Channel>
            <ChannelId></ChannelId>
            <Status>offline</Status>
        </Channel>
    </ChannelList>
</Response>
<Response>
    <Code>200</Code>
    <Message>OK</Message>
    <ChannelList>
        <Channel>
            <ChannelId></ChannelId>
            <Status>online</Status>
            <UrlList>
                <Url>
                    <Type>flv</Type>
                    <StreamUrl></StreamUrl>
                </Url>
            </UrlList>
        </Channel>
    </ChannelList>
</Response>


```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述     | 类型   |
| :----------------- | :------- | :------- | :----- |
| RequestId          | Response | 请求 id   | String |
| Code               | Response | 错误码   | Int    |
| Message            | Response | 错误描述 | String |
| ChannelList        | Response | 成功列表 | Array  |

Array 类型 ChannelList 的具体数据描述如下：

| 节点名称（关键字） | 父节点               | 描述         | 类型      |
| ------------------ | -------------------- | ------------ | --------- |
| Channel            | Response.ChannelList | 通道详细信息 | Container |

Container 类型 Channel 的具体数据描述如下：

| 节点名称（关键字） | 父节点                       | 描述       | 类型   |
| ------------------ | ---------------------------- | ---------- | ------ |
| ChannelId          | Response.ChannelList.Channel | 通道 id     | String |
| Status             | Response.ChannelList.Channel | 通道状态   | String |
| UrlList            | Response.ChannelList.Channel | 流信息列表 | Array  |

Array 类型 UrlList 的具体数据描述如下：

| 节点名称（关键字） | 父节点                               | 描述       | 类型      |
| ------------------ | ------------------------------------ | ---------- | --------- |
| Url                | Response.ChannelList.Channel.UrlList | 流详细信息 | Container |

Container 类型 Url 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                   | 描述   | 类型   |
| ------------------ | ---------------------------------------- | ------ | ------ |
| Type               | Response.ChannelList.Channel.UrlList.Url | 类型   | String |
| StreamUrl          | Response.ChannelList.Channel.UrlList.Url | 流地址 | String |

#### 错误码

常见的错误信息请参阅 [错误码](https://cloud.tencent.com/document/product/1344/50457) 文档。

## 实际案例

#### 请求


```plaintext
GET /device/stream?gbid=34020000001320000184&projectId=p15a20e50c92f4b089bf11bf77b558809 HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0*****
Host: iss.ap-beijing.myqcloud.com
Content-Length: 0
Content-Type: application/xml

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
    <RequestId>NjBmOTVhOWZfOTBmYTUwNjRfN2I4OF8y</RequestId>
    <Code>200</Code>
    <Message>OK</Message>
    <ChannelList>
        <Channel>
            <ChannelId></ChannelId>
            <UrlList>
                <Url>
                    <Type>flv</Type>
                    <StreamUrl></StreamUrl>
                </Url>
            </UrlList>
        </Channel>
        <Channel>
            <ChannelId></ChannelId>
            <UrlList>
                <Url>
                    <Type>flv</Type>
                    <StreamUrl></StreamUrl>
                </Url>
            </UrlList>
        </Channel>
        <Channel>
            <ChannelId></ChannelId>
            <UrlList>
                <Url>
                    <Type>flv</Type>
                    <StreamUrl></StreamUrl>
                </Url>
            </UrlList>
        </Channel>
    </ChannelList>
</Response>
```
