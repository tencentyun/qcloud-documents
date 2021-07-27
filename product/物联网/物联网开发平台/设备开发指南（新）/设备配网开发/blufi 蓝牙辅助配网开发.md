## 操作场景
### 基本原理
blufi 蓝牙辅助配网是针对 ESP32  Combo 芯片的配网方案，通过 BLE 创建指定的 GATT 服务，手机连接该 GATT SERVER，利用 BLE 的无线通信能力，将物联网设备连接所需的 SSID、PSW 等信息传输给 Wi-Fi+BLE 的 Combo 芯片或模组，使设备顺利接入物联网平台，继而完设备绑定等功能。

目前腾讯连连小程序已支持采用 blufi 蓝牙辅助配网协议进行配网 Demo 开发，并提供相应的 [小程序 SDK](https://www.npmjs.com/package/qcloud-iotexplorer-appdev-sdk)。
blufi 蓝牙辅助方式配网及设备绑定的示例流程图如下：
![img](https://main.qcloudimg.com/raw/b5f24fdace1257807327b29aa21a99f4.png)

## 操作步骤
### 蓝牙辅助配网协议示例
本示例基于 ESP32 腾讯云定制模组配合腾讯连连小程序。

1. 腾讯连连小程序进入配网模式后，则可以在物联网开发平台服务获取到当次配网的 Token。小程序相关操作可以参考 [生成 Wi-Fi 设备配网 Token](https://cloud.tencent.com/document/product/1081/44044)。
2. 使 Wi-Fi+BLE 设备进入蓝牙辅助配网模式，若设备有指示灯在快闪，则说明进入配网模式成功。    
3. 小程序按照提示依次获取 Wi-Fi 列表，输入家里目标路由器的 SSID/PSW，再选择连接 Wi-Fi+BLE 设备蓝牙服务。
4. 手机连接 Wi-Fi+BLE 设备蓝牙服务成功后，小程序作为 GATT Client 会向 Wi-Fi+BLE 设备分别下发设置 Wi-Fi station 模式、下发 SSID 信息、下发 PSW 信息，最后下发 Wi-Fi+BLE 设备连接的 AP 指令。发送完成后，等待 Wi-Fi+BLE 设备回复 Wi-Fi 连接状态及 SSID 信息。
5. 如果步骤4收到设备回复，则说明设备端已收到 Wi-Fi 路由器的 SSID/PSW。此时小程序会将当次配网的token下发给 Wi-Fi+BLE 设备。
6. 设备端在成功连接 Wi-Fi 路由器后，需要通过 MQTT 连接物联网后台，并将小程序发送的配网 Token，通过下面 MQTT 报文上报给后台服务：
```json
    topic: $thing/up/service/ProductID/DeviceName
    payload: {"method":"app_bind_token","clientToken":"client-1234","params": {"token":"6****345****234ee77****e528a0fd"}}
```
设备端也可以通过订阅主题 $thing/down/service/ProductID/DeviceName 来获取 Token 上报的结果。
7. 设备端将 Token 的绑定结果上报至小程序，至此配网结束。
8. 如果设备成功上报了 Token，物联网后台服务已确认 Token 有效性，小程序会提示配网完成，设备添加成功。

### ESP32 使用 蓝牙辅助 配网接口
配网协议在 ESP32 设备端的参考代码，请参见 GitHub 工程 [esp-qcloud](https://github.com/espressif/esp-qcloud/tree/master/src/provisioning)。

