## 操作场景
设备开发完成后，需要进入设备调试阶段调试设备与云端的通信是否正常。设备调试提供了真实设备在线调试及虚拟设备调试，并可通过控制台查询设备上报的当前数据、历史通信日志、事件及上下线记录等。本文档主要介绍如何进行设备调试。

LoRaWAN 设备调试与其他产品的设备调试的操作步骤基本一致，只有新建设备时有不同，因此本文档中只对新建 LoRaWAN 设备这一步骤进行说明，其他步骤可参考通用的 [LoRaWAN 设备调试](https://cloud.tencent.com/document/product/1081/34741) 文档。


## 前提条件
已完成设备开发。详情请参见 [LoRaWAN 设备开发](https://cloud.tencent.com/document/product/1081/41189)。


## 操作步骤
1. 登录 [物联网开发平台控制台](https://console.cloud.tencent.com/iotexplorer)，设备开发完成后，单击**设备调试**。
2. 进入设备调试环节，单击**新建设备**，填写设备基本信息，单击**保存**，即可完成创建设备。
  - 设备名称：支持英文、数字、下划线的组合，最多不超过48个字符。
  - DevEUI：仅支持16进制字符，长度16位。
  - AppKey（仅限 OTAA 加网方式）：仅支持16进制字符，长度32位。
  - DevAddr（仅限 ABP 加网方式）：仅支持16进制字符，长度8位。
  - NwkSKey（仅限 ABP 加网方式）：仅支持16进制字符，长度32位。
  - AppSKey（仅限 ABP 加网方式）：仅支持16进制字符，长度32位。

DevEUI、AppKey、DevAddr、NwkSKey、AppSKey 一般为 LoRaWAN 节点设备厂商提供。如果是自行开发协议栈，可以按需配置，只要平台和节点实际配置的内容一致即可。
  下图示例中为 OTAA 加网方式，如果需要切换到 ABP 加网方式，可以在**设备开发**界面中调整 “LoRaWAN 参数配置” 中的加网方式。
![](https://main.qcloudimg.com/raw/29ae6692c8716846fab6bb4d79391408.png)
3. 创建成功后，您将会在“设备调试”列表页中，查看到新建成功的设备。


## 查看设备
1. 创建设备成功后，您将会在“设备调试”列表页中，查看到新建成功的设备。
2. 单击设备名称，可以查看设备相关信息、设备信息、设备日志、透传日志等。

### 设备信息
单击**设备信息**，即可查看设备基础的信息、名称、密钥、激活时间、最后上线时间等。
此外，在 ABP 模式下，可在设备信息中选择**禁用帧序号校验（临时调试使用）**以及**重置帧序号**功能。
>?此功能建议用于设备临时调试，以解决设备上传序列号归零导致 MIC 校验错误的问题；不建议用户用于商业应用，存在设备重放攻击的安全隐患。

![ABP设备信息](https://main.qcloudimg.com/raw/9dba8ae4bf9b0b915c0815128f3dfef1.png)

### 设备日志
单击**设备日志**，即可查看该设备上行到云端，并从云端接收的信息，可查看7天以内的设备日志内容。
 - 上行：上行表示设备端向云端上报的数据。
 - 下行：下行表示云端向设备端发送的数据。
![设备日志](https://main.qcloudimg.com/raw/838c36862d32de65d91d096d134c62d8.png)

### 设备透传日志
单击**设备日志（透传数据）**，即可查看数据透传到用户侧的数据内容，以及 LoRaWAN 网络侧内容数据。
![](https://main.qcloudimg.com/raw/ed1e2d35b21f2d28ea3e63cf0c27f063.png)
**示例**
数据内容如下：
```
“eyJtZXRob2QiOiJyZXBvcnQiLCJjbGllbnRUb2tlbiI6IjIwMjEtMDEtMThUMDU6NTE6MDIuMDM4WiIsInBhcmFtcyI6eyJyYXdkYXRhIjoiMDAwMTAyMDMifSwibWV0YUxvUmEiOiJ7XCJmcmFtZVR5cGVcIjoyLFwiZlBvcnRcIjoyLFwiZkNudFwiOjQ2NCxcImZyZXF1ZW5jeVwiOjQ3MDMwMDAwMCxcImRyXCI6NSxcInJzc2lcIjotNTAsXCJzbnJcIjoyNixcInBheWxvYWRTaXplXCI6NH0ifQ==”
```
通过 BASE64 解析成文本的格式如下：
```plaintext
{"method":"report","clientToken":"2021-01-18T05:51:02.038Z","params":{"rawdata":"00010203"},"metaLoRa":"{\"frameType\":2,\"fPort\":2,\"fCnt\":464,\"frequency\":470300000,\"dr\":5,\"rssi\":-50,\"snr\":26,\"payloadSize\":4}"}
```

### 在线调试
当您的真实设备已成功对接到开发平台后，则可使用在线调试对真实设备进行数据收发的测试，具体步骤如下：
1. 单击**在线调试**，即可进入在线调试功能。
2. 在线调试左侧的操控面板是根据设备所属产品的数据模板自动生成，设置需要下发的数据后，单击**发送**，系统会自动触发控制指令到设备端。
3. 设备端接收到指令后，会立刻返回数据到云端并显示在右侧的文本框中。
![](https://main.qcloudimg.com/raw/c2f4fc081b15314d89db2379e203d87a.png)
