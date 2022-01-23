## 功能描述
DescribeDevices 用于获取设备列表。

## 请求

#### 请求示例

```plaintext
GET /device?projectId=pj1460606b9752148c4ab182f55163ba7cd HTTP/1.1
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
| pageSize | 无 | 页大小 | Int |否|
| pageNumber | 无 | 页码 | Int |否|

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
    <DeviceList>
        <Device>
            <Gbid></Gbid>
            <Name/>
            <Status>OnLine</Status>
            <Ip/>
            <Port/>
            <Manufacturer/>
            <Enabled/>
            <User/>
            <Pwd/>
            <Type>Ipc</Type>
            <ChannelList>
                <Channel>
                    <ChannelId></ChannelId>
                    <ChannelName></ChannelName>
                    <Manufacturer/>
                    <Enabled>false</Enabled>
                </Channel>
            </ChannelList>
        </Device>
    </DeviceList>
    <TotalCount>2</TotalCount>
    <PageNumber>1</PageNumber>
    <PageSize>10</PageSize>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      |
| :----------------- | :----- | :------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container 节点 Response 的内容：

| 节点名称（关键字） | 父节点   | 描述     | 类型   |
| :----------------- | :------- | :------- | :----- |
| RequestId          | Response | 请求 ID   | String |
| DeviceList         | Response | 设备集合 | array  |
| TotalCount         | Response | 总数     | Int    |
| PageNumber         | Response | 页码         | Int       |
| PageSize           | Response |  页大小        | Int       |

Array 类型 Devicelist 的具体数据描述如下：

| 节点名称（关键字） | 父节点              | 描述         | 类型      |
| ------------------ | ------------------- | ------------ | --------- |
| Device             | Response.DeviceList | 设备详细信息 | Container |

Container 节点 Device 的内容：

| 节点名称（关键字） | 父节点                | 描述                                                         | 类型      |
| :----------------- | :-------------------- | :----------------------------------------------------------- | :-------- |
| Gbid       | Response.DeviceList.Device | 设备 ID                                                  | String    |
| Name            | Response.DeviceList.Device | 设备名字                                                   | String    |
| Status | Response.DeviceList.Device | 设备状态：OnLine、OffLine | String |
| Ip | Response.DeviceList.Device | 设备 IP | String |
| Port | Response.DeviceList.Device | 设备端口 | Int |
| Manufacturer | Response.DeviceList.Device | 设备厂商 | String |
| Enabled | Response.DeviceList.Device | 设备是否在线 | Bool |
| User | Response.DeviceList.Device | 设备用户名 | String |
| Pwd | Response.DeviceList.Device | 设备密码 | String |
| Type | Response.DeviceList.Device | 设备类型：IPC、NVR | String |
| ChannelList | Response.DeviceList.Device | 设备通道集合                                               | Array |

Array 类型 ChannelList 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                 | 描述     | 类型      |
| ------------------ | -------------------------------------- | -------- | --------- |
| Channel            | Response.DeviceList.Device.ChannelList | 通道信息 | Container |

Container 节点 Channel 的内容：

| 节点名称（关键字） | 父节点                | 描述                                                         | 类型      |
| :----------------- | :-------------------- | :----------------------------------------------------------- | :-------- |
| ChannelId | Response.DeviceList.Device.ChannelList.Channel | 通道 ID                                             | String    |
| ChannelName | Response.DeviceList.Device.ChannelList.Channel | 通道名称 | String |
| Manufacturer | Response.DeviceList.Device.ChannelList.Channel | 通道厂商 | String |
| Enabled | Response.DeviceList.Device.ChannelList.Channel | 是否开启拉流 | Bool |

#### 错误码
常见的错误信息请参阅 [错误码](https://cloud.tencent.com/document/product/1344/50457) 文档。

## 实际案例

#### 请求


```plaintext
GET /device?gbid=pj1460606b9752148c4ab182f55163ba7cd&projectId=pj1460606b9752148c4ab182f55163ba7cd  HTTP/1.1
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

<Response>
        <RequestId>NjE5ZWY1ZTNfOTBmYTUwNjRfMTcy****</RequestId>
        <DeviceList>
                <Device>
                        <Gbid>34020000001010000001</Gbid>
                        <Name>dahua</Name>
                        <Status>OffLine</Status>
                        <ChannelList>
                                <Channel>
                                        <ChannelId>34020000001610000001</ChannelId>
                                        <ChannelName>IPC</ChannelName>
                                        <Manufacturer>Dahua</Manufacturer>
                                        <Enabled>false</Enabled>
                                </Channel>
                        </ChannelList>
                        <Ip/>
                        <Port>0</Port>
                        <Manufacturer/>
                        <Enabled>false</Enabled>
                        <User/>
                        <Pwd/>
                        <Type>Ipc</Type>
                </Device>
                <Device>
                        <Gbid>44010300001320000024</Gbid>
                        <Name>44010300001320000024</Name>
                        <Status>OnLine</Status>
                        <ChannelList>
                                <Channel>
                                        <ChannelId>34020000001310000001</ChannelId>
                                        <ChannelName>Camera 01</ChannelName>
                                        <Manufacturer>Hikvision</Manufacturer>
                             
                                        <Enabled>false</Enabled>
                                </Channel>
                        </ChannelList>
                        <Ip/>
                        <Port>0</Port>
                        <Manufacturer/>
                        <Enabled>false</Enabled>
                        <User>44010300001320000024</User>
                        <Pwd>123456</Pwd>
                        <Type>Ipc</Type>
                </Device>
        </DeviceList>
        <TotalCount>2</TotalCount>
        <PageNumber>1</PageNumber>
        <PageSize>10</PageSize>
</Response>
```
