腾讯云物联网设备端 Python SDK 依靠安全且性能强大的数据通道，为物联网领域开发人员提供设备端快速接入云端，并和云端进行双向通信的能力。开发人员只需完成工程的相应配置即可完成设备的接入。

## 前提条件

已在 Explorer 平台创建好产品和设备。
## 引用方式

- 如果您需要通过引用方式进行项目开发，可安装 SDK，如下：
```
pip3 install tencent-iot-device
```
如果您需查看使用的 SDK 版本，使用如下指令：
```
pip3 show --files tencent-iot-device
```
如果您需升级 SDK 版本，使用如下指令：
```
pip3 install --upgrade tencent-iot-device
```
- 如果您需要通过代码集成方式进行项目开发，可访问 [Github](https://github.com/tencentyun/iot-device-python) 下载 Python SDK 源码。

## MQTT 接口

MQTT 的相关接口定义在 [explorer.py](https://github.com/tencentyun/iot-device-python/blob/master/explorer/explorer.py) 类中，支持发布和订阅功能，介绍如下：

| 方法名               | 说明                   |
| :------------------- | :--------------------- |
| connect              | MQTT 连接              |
| disconnect           | 断开 MQTT 连接         |
| subscribe            | MQTT 订阅              |
| unsubscribe          | MQTT 取消订阅          |
| publish              | MQTT 发布消息          |
| registerMqttCallback | 注册 MQTT 回调函数     |
| registerUserCallback | 注册用户回调函数       |
| isMqttConnected      | MQTT 是否正常连接      |
| getConnectState      | 获取 MQTT 连接状态     |
| setReconnectInterval | 设置 MQTT 重连尝试间隔 |
| setMessageTimout     | 设置消息发送超时时间   |
| setKeepaliveInterval | 设置 MQTT 保活间隔     |

## MQTT 网关接口

- 对于无法直接接入以太网网络的设备，可先接入本地网关设备的网络，利用网关设备的通信功能，将代理设备接入 explorer 平台。
- 对于局域网中加入或退出网络的子设备，需通过平台进行绑定或解绑操作。

> !当子设备发起过上线，后续只要网关链接成功，后台就会显示子设备在线，除非设备已发起下线操作。

MQTT 网关的相关接口定义在 [gateway.py](https://github.com/tencentyun/iot-device-python/blob/master/explorer/services/gateway/gateway.py) 类接口中，介绍如下：

| 方法名                     | 说明                     |
| :------------------------- | :----------------------- |
| gatewayInit                | 网关初始化               |
| isSubdevStatusOnline       | 判断子设备是否在线       |
| updateSubdevStatus         | 更新子设备在线状态       |
| gatewaySubdevGetConfigList | 获取配置文件中子设备列表 |
| gatewaySubdevOnline        | 代理子设备上线           |
| gatewaySubdevOffline       | 代理子设备下线           |
| gatewaySubdevBind          | 绑定子设备               |
| gatewaySubdevUnbind        | 解绑子设备               |
| gatewaySubdevSubscribe     | 子设备订阅               |

## 数据模板接口

如果需要使用数据模板功能，需使用 [template.py](https://github.com/tencentyun/iot-device-python/blob/master/explorer/sample/template/example_template.py) 类中的接口，介绍如下：

| 接口名称                         | 接口描述             |
| -------------------------------- | -------------------- |
| templateInit                     | 数据模板初始化       |
| getEventsList                    | 获取设备event列表    |
| getActionList                    | 获取设备action列表   |
| getPropertyList                  | 获取设备property列表 |
| templateSetup                    | 解析数据模板         |
| templateEventPost                | events上报           |
| templateJsonConstructReportArray | 构建上报的json结构   |
| templateReportSysInfo            | 设备信息上报         |
| templateControlReply             | 控制消息应答         |
| templateActionReply              | action消息应答       |
| templateGetStatus                | 获取设备最新状态     |
| templateReport                   | 设备属性上报         |
| clearControl                     | 清除控制             |
| templateDeinit                   | 数据模板销毁         |



## 动态注册接口

如果需要使用动态注册功能，需使用 [explorer.py](https://github.com/tencentyun/iot-device-python/blob/master/explorer/explorer.py) 类中的接口，介绍如下：

| 方法名       | 说明                   |
| :----------- | :--------------------- |
| dynregDevice | 获取设备动态注册的信息 |

## OTA 接口

如果需要使用 OTA 功能，需使用 [explorer.py](https://github.com/tencentyun/iot-device-python/blob/master/explorer/explorer.py) 类中的接口，介绍如下：

| 方法名                  | 说明                                |
| :---------------------- | :---------------------------------- |
| otaInit                 | OTA 初始化                          |
| otaIsFetching           | 判断是否正在下载                    |
| otaIsFetchFinished      | 判断是否下载完成                    |
| otaReportUpgradeSuccess | 上报升级成功消息                    |
| otaReportUpgradeFail    | 上报升级失败消息                    |
| otaIoctlNumber          | 获取下载固件大小等 int 类型信息     |
| otaIoctlString          | 获取下载固件 md5 等 string 类型信息 |
| otaResetMd5             | 重置 md5 信息                       |
| otaMd5Update            | 更新 md5 信息                       |
| httpInit                | 初始化 HTTP                         |
| otaReportVersion        | 上报当前固件版本信息                |
| otaDownloadStart        | 开始固件下载                        |
| otaFetchYield           | 读取固件                            |
