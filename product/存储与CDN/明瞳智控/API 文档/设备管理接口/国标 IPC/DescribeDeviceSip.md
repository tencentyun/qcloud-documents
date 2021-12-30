## 功能描述
DescribeDeviceSip 用于获取 SIP 服务器信息。

## 请求

#### 请求示例

```plaintext
GET /device/sip?projectId=pj1460606b9752148c4ab182f55163ba7cd HTTP/1.1
Host: iss.<Region>.myqcloud.com
Date: <GMT Date>
Authorization: <Auth String>
Content-Length: <length>
Content-Type: application/xml

```

>? Authorization: Auth String （详情请参见 [请求签名](https://cloud.tencent.com/document/product/1344/50456) 文档）。
>


#### 请求参数

参数的具体内容如下：

|节点名称（关键字）|父节点     |描述                    |   类型    |   是否必选    |
|:---           |:--       |:--                    |   :--     |   :--    |
| projectId | 无 | 项目 ID | String |是|


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
<?xml version="1.0" encoding="utf-8"?>
<Response>
    <RequestId>NjBmYWJkMTNfOTBmYTUwNjRfMTFlY18z</RequestId>
    <SipServerList>
        <SipServer>
            <ServerGbid>34010000002000000010</ServerGbid>
            <NetPort>5060</ServerPort>
            <NetIp/>
            <TimeOut>180</TimeOut>
            <Domain/>
        </SipServer>
    </SipServerList>
</Response> 
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述                  | 类型   |
| :----------------- | :------- | :-------------------- | :----- |
| RequestId          | Response | 请求 ID                | String |
| SipServerList      | Response | SIP 服务器详细信息集合 | Array  |

Array 类型 SipServerList 的具体数据描述如下：

| 节点名称（关键字） | 父节点                 | 描述              | 类型      |
| ------------------ | ---------------------- | ----------------- | --------- |
| SipServer          | Response.SipServerList | SIP 服务器详细信息 | Container |

Container 节点 SipServer 的内容：

| 节点名称（关键字） | 父节点                | 描述                                                         | 类型      |
| :----------------- | :-------------------- | :----------------------------------------------------------- | :-------- |
| ServerGbid | Response.SipServerList.SipServer | SIP 服务器 ID                                         | String    |
| NetPort  | Response.SipServerList.SipServer | SIP 服务器端口                                           | Int    |
| NetIp       | Response.SipServerList.SipServer | SIP 服务器地址                                     | String    |
| TimeOut    | Response.SipServerList.SipServer | 超时时间                                             | Int  |
| Domain | Response.SipServerList.SipServer | SIP 服务器域 | String |

#### 错误码
常见的错误信息请参阅 [错误码](https://cloud.tencent.com/document/product/1344/50457) 文档。

## 实际案例

#### 请求


```plaintext
GET /device/sip?projectId=pj1460606b9752148c4ab182f55163ba7cd  HTTP/1.1
Authorization:q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0*****
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

<?xml version="1.0" encoding="utf-8"?>
<Response>
    <RequestId>NjBmYWJkMTNfOTBmYTUwNjRfMTFlY18z</RequestId>
    <SipServerList>
        <SipServer>
            <ServerGbid></ServerGbid>
            <NetPort>5060</ServerPort>
            <NetIp/>
            <TimeOut>180</TimeOut>
            <Domain/>
        </SipServer>
    </SipServerList>
</Response>
```

