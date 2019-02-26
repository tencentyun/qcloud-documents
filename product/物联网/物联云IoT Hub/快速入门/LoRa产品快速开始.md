## 1. 应用场景和功能
- 用户有 LoRa 芯片，实现终端到应用平台的上报数据和下发数据，以及转发到腾讯云组件存储、分发、分析使用等。  
- 用户只需要在腾讯物联网通信配置，获取 LoRa 通信相关信息配置到 LoRa 终端，即可在深圳地区连接上腾讯铺设的   LoRa 网关。  
![数据流程](https://main.qcloudimg.com/raw/e8fd5d1c2bc162c9d0dd618553fb570a/LoRa_freamwork.png)

## 2. 操作步骤
### 2.1 创建 LoRa 产品和设备
1. 进入 [控制台](https://console.cloud.tencent.com/iotcloud)  创建 LoRa 产品。  
![](https://main.qcloudimg.com/raw/f6e66177d91dad72cd423cdd714e0197/LoRa_product.png)
2. 创建成功后，可以查看产品的基本信息。  
![](https://main.qcloudimg.com/raw/28d192fec91cf730402391393c154318/LoRa_product_info.png)
3. 在【设备列表】下创建设备（testLoRa1），返回通信相关信息。  
![](https://main.qcloudimg.com/raw/d54cba5ea51a16a508f3c47c6f5de3c3/LoRa_device.png)
![](https://main.qcloudimg.com/raw/33bd588f15bd7dd2f0fffa929bb16b81/LoRa_device_info.png)
4. 单击【管理】可查询设备详情。  
![](https://main.qcloudimg.com/raw/0aa423f1542beaa415e549fb233e5a6e/LoRa_device_info_m.png)

### 2.2 创建规则引擎
本示例是将上报的数据转发到用户的应用平台，采用 http post 请求推送，包体为 json。  
规则引擎同时还支持转发腾讯云存储组件，消息队列等。  
![](https://main.qcloudimg.com/raw/26acf7aa274fe686e857fda1e70b98d2/NB-IoT_forward_app.png)  
具体步骤详见 [规则引擎详情](https://cloud.tencent.com/document/product/634/14446)。
### 2.3 创建网关产品和设备
创建网关产品和设备跟创建 LoRa 产品和设备类似，请参考 [创建 LoRa 产品和设备](https://cloud.tencent.com/document/product/634/30210#2.1-.E5.88.9B.E5.BB.BA-lora-.E4.BA.A7.E5.93.81.E5.92.8C.E8.AE.BE.E5.A4.87)。
### 2.4 网关与 LoRa 建立绑定关系
1. 进入 【控制台】-【产品列表】 下网关产品，单击【子产品】。  
![](https://main.qcloudimg.com/raw/f9bb294a9e4b83b78b14aef60f54a8db/Gateway_sub_product.png)
2. 单击【添加子产品】选择刚创建的 LoRa 产品添加。  
![](https://main.qcloudimg.com/raw/0b660fb0d3e8e1233426a6fc878b2301/Gateway_add_lora_product.png)
3. 在【设备列表】下网关设备，单击【子设备】-【添加子设备】选择刚创建的 LoRa 设备添加。  
![](https://main.qcloudimg.com/raw/7a52e633c5d3510637c1ff2e5bb5d329/Gateway_device_add_lora_device.png)
### 2.5 网关添加发布订阅权限
网关和 LoRa 建立绑定关系之后，网关要代发 LoRa 的消息，还需设置网关权限列表。
添加 Plora/+/+/event 发布权限，Plora/+/+/control 订阅权限。
![](https://main.qcloudimg.com/raw/5e4bf8b2d4ad502a7bee7705eca85688/Gateway_topic_policy.png)
### 2.6 设备接入
通过以上配置，用户获取到 DevEUI、AppKey、NwkKey、AppEUI 等 LoRaWAN 通信的基本信息，就可以连接上腾讯在深圳地区铺设的 LoRa 网络。
