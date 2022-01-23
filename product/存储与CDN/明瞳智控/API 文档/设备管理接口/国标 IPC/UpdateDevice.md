## 功能描述
UpdateDevice 用于更新设备配置。一次性更新设备数量上限是100。

## 请求

#### 请求示例

```plaintext
PUT /device HTTP/1.1
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
此接口无请求参数。


#### 请求头

此接口仅使用公共请求头部，详情请参见 [公共请求头部](https://cloud.tencent.com/document/product/1344/50451) 文档。

#### 请求体
该请求操作的实现需要有如下请求体。

```plaintext
<Request>
    <Devicelist>
        <Gbid>Gbid</Gbid>
        <Name>Name</Name>
        <User>User</User>
        <Pwd>Pwd</Pwd>
        <Ip>Ip</Ip>
        <Port>Port</Port>
        <Type>Type</Type>
        <Manufacturer></Manufacturer>
    </Devicelist>
    <ProjectId>ProjectId</ProjectId>
</Request>
```

具体数据描述如下：

| 节点名称（关键字） | 父节点 | 描述           | 类型      | 是否必选 |
| ------------------ | ------ | -------------- | --------- | ---- |
| Request            | 无     | 保存请求的容器 | Container | 是   |

Container 类型 Request 的具体数据描述如下：

| 节点名称（关键字） | 父节点  | 描述               | 类型   | 是否必选 |
| ------------------ | ------- | ------------------ | ------ | ---- |
| Devicelist         | Request | 待添加的 device 列表 | Array  | 是   |
| ProjectId          | Request | 项目 ID             | String | 是   |


Array 类型 Devicelist 的具体数据描述如下：

| 节点名称（关键字） | 父节点                    | 描述          | 类型   | 是否必选 | 默认值 | 限制                 |
| ------------------ | ------------------------- | ------------- | ------ | ---- | ------ | -------------------- |
| Gbid               | Request.Devicelist.Device | 设备 ID        | String | 是   | 无       | 无                     |
| Name               | Request.Devicelist.Device | 设备名称      | String | 否   | 无     | 64                   |
| User               | Request.Devicelist.Device | 设备用户名    | String | 否   | 无     | 64                   |
| Pwd                | Request.Devicelist.Device | 设备密码      | String | 否   | 无     | 64                   |
| Ip                 | Request.Devicelist.Device | 设备 IP        | String | 否   | 无     | 64                   |
| Port               | Request.Devicelist.Device | 设备端口      | Int    | 否   | 无     | 数值范围：1025 - 65535 |
| Manufacturer       | Request.Devicelist.Device | 设备厂商      | String | 否   | 无     |  无                    |
| Type               | Request.Devicelist.Device | 设备类型：IPC | String | 否   | Ipc    | 当前只支持 IPC        |



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
            <Ip/>
            <Port/>
            <User/>
            <Pwd/>
            <Manufacturer/>
            <Type>Ipc</Type>
            <Msg/>
        </Device>
    </DeviceList>
    <FailedDeviceList>
        <Device>
            <Gbid></Gbid>
            <Name/>
            <Ip/>
            <Port/>
            <User/>
            <Pwd/>
            <Manufacturer/>
            <Type>Ipc</Type>
            <Msg/>
        </Device>
    </FailedDeviceList>
</Response>
```

具体的数据内容如下：

| 节点名称（关键字） | 父节点 | 描述                                       | 类型      |
| :----------------- | :----- | :----------------------------------------- | :-------- |
| Response           | 无     | 保存结果的容器 | Container |

Container节点Response的内容：

| 节点名称（关键字） | 父节点   | 描述     | 类型   |
| :----------------- | :------- | :------- | :----- |
| RequestId          | Response | 请求 ID   | String |
| DeviceList         | Response | 成功列表 | Array  |
| FailedDeviceList   | Response | 失败列表 | Array  |

Array 类型 Devicelist/FailedDeviceList 的具体数据描述如下：

| 节点名称（关键字） | 父节点                                       | 描述         | 类型      |
| ------------------ | -------------------------------------------- | ------------ | --------- |
| Device             | Response.DeviceList/Request.FailedDeviceList | 设备详细信息 | Container |

Container 类型 Device 的具体数据描述如下：

| 节点名称（关键字） | 父节点                    | 描述               | 类型   | 是否必选 | 默认值 | 限制 |
| ------------------ | ------------------------- | ------------------ | ------ | ---- | ------ | ---- |
| Gbid               | Request.Devicelist.Device | 设备 ID             | String | 是   | 无     | 无   |
| Name               | Request.Devicelist.Device | 设备名称           | String | 否   | 无     | 无   |
| User               | Request.Devicelist.Device | 设备用户名         | String | 否   | 无     | 无   |
| Pwd                | Request.Devicelist.Device | 设备密码           | String | 否   | 无     | 无   |
| Ip                 | Request.Devicelist.Device | 设备 ip             | String | 否   | 无     | 64   |
| Port               | Request.Devicelist.Device | 设备端口           | Int    | 否   | 无     | 无     |
| Manufacturer       | Request.Devicelist.Device | 设备厂商           | String | 否   | 无     | 无     |
| Type               | Request.Devicelist.Device | 设备类型：IPC、NVR | String | 否   | Ipc    | 无     |
| Msg                | Request.Devicelist.Device |  具体信息                  | String | 否   |  无      | 无     |

#### 错误码
常见的错误信息请参阅 [错误码](https://cloud.tencent.com/document/product/1344/50457) 文档。

## 实际案例

#### 请求

```plaintext
PUT /device HTTP/1.1
Authorization: q-sign-algorithm=sha1&q-ak=AKIDZfbOAo7cllgPvF9cXFrJD0**********&q-sign-time=1497530202;1497610202&q-key-time=1497530202;1497610202&q-header-list=&q-url-param-list=&q-signature=28e9a4986df11bed0255e97ff90500557e0*****
Host: iss.ap-beijing.myqcloud.com
Content-Length: 1666
Content-Type: application/xml

<Request>
    <Devicelist>
        <Gbid></Gbid>
        <Name></Name>
        <User></User>
    </Devicelist>
    <Devicelist>
        <Gbid></Gbid>
        <Name></Name>
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
    <RequestId>NjBmOTVhOWZfOTBmYTUwNjRfN2I4****</RequestId>
    <Code>200</Code>
    <Message>OK</Message>
    <DeviceList>
        <Device>
            <Gbid>44010300001320000024</Gbid>
            <Name>44010300001320000024</Name>
            <Ip/>
            <Port/>
            <User>44010300001320000024</User>
            <Pwd>123456</Pwd>
            <Manufacturer/>
            <Type>Ipc</Type>
            <Msg/>
        </Device>
    </DeviceList>
    <FailedDeviceList>
        <Device>
            <Gbid>44010300001320000024</Gbid>
            <Name>44010300001320000024</Name>
            <Ip/>
            <Port/>
            <User>44010300001320000024</User>
            <Pwd>123456</Pwd>
            <Manufacturer/>
            <Type>Ipc</Type>
            <Msg/>
        </Device>
    </FailedDeviceList>
</Response>
```



