
Python SDK 除提供设备的接入功能之外，还提供网关子设备，设备影子等功能。相关功能接口如下。

## MQTT 接口 

MQTT 的相关接口定义在 [hub.py](https://github.com/tencentyun/iot-device-python/blob/master/hub/hub.py) 类中，支持发布和订阅功能；如果需支持设备影子功能，则需使用 [shadow.py](https://github.com/tencentyun/iot-device-python/blob/master/hub/services/shadow/shadow.py) 类及其方法，介绍如下：

| 方法名           | 说明                     |
| ---------------- | ------------------------ |
| connect	           | MQTT 连接                |
| disconnect	           | 断开 MQTT 连接               |
| subscribe           | 	MQTT 订阅                |
| unsubscribe	           | MQTT 取消订阅                |
| publish	           | MQTT 发布消息                |
| registerMqttCallback	           | 注册 MQTT 回调函数               |
| registerUserCallback           | 	注册用户回调函数                 |
| isMqttConnected           | 	MQTT 是否正常连接                |
| getConnectState           | 	获取 MQTT 连接状态               |
| setReconnectInterval           | 	设置 MQTT 重连尝试间隔               |
| setMessageTimout           | 	设置消息发送超时时间                 |
| setKeepaliveInterval           | 	设置 MQTT 保活间隔               |


## MQTT 网关接口 

- 对于无法直接接入以太网网络的设备，可先接入本地网关设备的网络，利用网关设备的通信功能，将代理设备接入 IoT Hub 平台。
- 对于局域网中加入或退出网络的子设备，需通过平台进行绑定或解绑操作。

>!当子设备发起过上线，后续只要网关链接成功，后台就会显示子设备在线，除非设备已发起下线操作。
>
MQTT 网关的相关接口定义在 [gateway.py](https://github.com/tencentyun/iot-device-python/blob/master/hub/services/gateway/gateway.py) 类接口中，介绍如下：

| 方法名               | 说明                     |
| -------------------- | ------------------------ |
| gatewayInit              |	网关初始化             |
| isSubdevStatusOnline              |	判断子设备是否在线             |
| updateSubdevStatus              |	更新子设备在线状态             |
| gatewaySubdevGetConfigList              |	获取配置文件中子设备列表             |
| gatewaySubdevOnline              |	代理子设备上线             |
| gatewaySubdevOffline              |	代理子设备下线             |
| gatewaySubdevBind              |	绑定子设备             |
| gatewaySubdevUnbind              |	解绑子设备             |
| gatewaySubdevSubscribe              |	子设备订阅             |

## 动态注册接口

如果需要使用动态注册功能，需使用  [hub.py](https://github.com/tencentyun/iot-device-python/blob/master/hub/hub.py)  类中的接口，介绍如下：

| 方法名                | 说明                                 |
| --------------------- | ------------------------------------ |
| dynregDevice               |	获取设备动态注册的信息                             |

## OTA接口
如果需要使用OTA功能，需使用 [hub.py](https://github.com/tencentyun/iot-device-python/blob/master/hub/hub.py)  类中的接口，介绍如下：

| 方法名                | 说明                                 |
| --------------------- | ------------------------------------ |
| otaInit               |	OTA 初始化                            |
| otaIsFetching               |	判断是否正在下载                             |
| otaIsFetchFinished               |	判断是否下载完成                             |
| otaReportUpgradeSuccess               |	上报升级成功消息                             |
| otaReportUpgradeFail               | 上报升级失败消息                             |
| otaIoctlNumber               | 获取下载固件大小等 int 类型信息                           |
| otaIoctlString               | 获取下载固件 md5 等 string 类型信息                        |
| otaResetMd5               | 重置 md5 信息                           |
| otaMd5Update               | 更新 md5 信息                           |
| httpInit               | 初始化 http                            |
| otaReportVersion               | 上报当前固件版本信息                             |
| otaDownloadStart               | 开始固件下载                             |
| otaFetchYield               | 读取固件                             |
