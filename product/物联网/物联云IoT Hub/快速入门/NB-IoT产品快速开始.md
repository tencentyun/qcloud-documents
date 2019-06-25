>?NB-IoT 产品与普通产品的区别，请参考 [产品类型](https://cloud.tencent.com/document/product/634/18348)。

## 应用场景和功能
- 用户有电信 NB-IoT 模组，实现终端到应用平台的上报数据和下发数据，查询数据最后上报时间。  
- 用户只需要在腾讯物联网通信配置（不需要在电信 NB-IoT 平台配置），即可完成上述功能。  
- 用户通过终端串口命令设置 NB-IoT 模组连接运营商网络后，通过 AT 命令上报数据到运营商 NB-IoT 平台，运营商通过回调，将数据发送到物联网通信平台，结合用户配置的规则，转发到用户平台，或者转发到腾讯云组件、云存储等。同理，用户平台调用物联网通信平台 RestAPI，即可将数据下发到终端。
- 对于移动/联通的 NB-IoT 产品其接入方式与 WIFI/2G/3G/4G 等普通产品相同，在控制台创建普通产品类型即可。
![数据流程](https://main.qcloudimg.com/raw/8d320cf009b8f405760a2b12b94e91f5/NB-IoT_freamwork.png)

## 操作步骤
### 创建 NB-IoT 产品和设备
1. 登录 [物联网通信控制台](https://console.cloud.tencent.com/iotcloud)，选择左侧菜单栏【[产品列表](https://console.cloud.tencent.com/iotcloud/products)】。
2. 进入产品列表页面，单击【创建新产品】，即可创建 NB-IoT 产品。  
3. 在弹出添加新产品页面中，根据实际情况填写相关信息，认证方式选择密钥认证。
![](https://main.qcloudimg.com/raw/1b9ba5e7e77e6af33d96ac2db5d66427.png)
4. 创建成功后，即可查看产品的基本信息。  
5. 在【设备列表】下创建设备（NB001），运营商选择电信 NB-IoT。 
![](https://main.qcloudimg.com/raw/b4ad2d17973e47e419b41528c82331d4.png)
6. 单击【管理】可查询设备详情。  


### 创建规则引擎
本示例是将上报的数据转发到用户的应用平台，采用 http post 请求推送，包体为 json。规则引擎同时还支持转发腾讯云存储组件，消息队列等。 
![](https://main.qcloudimg.com/raw/ff7f0c70c574d37d5c27d712c14c5062.png)  
具体步骤请参见 [规则引擎详情](https://cloud.tencent.com/document/product/634/14446)。

### 下载 NB-IoT SDK
SDK 下载地址请参考：[SDK 下载](https://cloud.tencent.com/document/product/634/11928)。

### 配置 C-SDK 示例程序
samples/nbiot/nbiot_sample.c 是上传数据编码和下发数据解码的示例代码。  
- SDK 上传数据编码主要帮助用户将要传输的 payload 编码成 AT 命令传输的数据，其中包括 Topic、鉴权、传输质量控制等字段填充。  
- 下行数据解码主要将 IoT 后台发送的 topic、payload、传输质量等信息解析出来。 

#### 上传数据编码
接口介绍  
`int IOT_NB_setMessage(unsigned char* msg, unsigned int* length, NBIoTSetMessage* nbiotMsg);`  

| 参数名称 | 描述 | 
|---------|---------|
| msg | 生成的十六进制上行消息编码 | 
| length | 十六进制上行消息的长度，以字节为单位 | 
| nbiotMsg | nbiot 终端发送消息的结构体，包括 address、 version、签名类型、过期时间、传输质量、topic、payload、key 等信息  | 


 
#### 下发数据解码
接口介绍  
`int IOT_NB_getMessage(NBIoTGetMessage* nbiotMsg, unsigned char* msg);` 

| 参数名称| 描述 | 
|---------|---------|
| nbiotMsg | nbiot 终端解析出来的消息内容结构体，包括 address、version、签名类型、过期时间、传输质量、topic、payload 等信息  | 
|msg | nbiot 平台发送到设备端的十六进制下行消息编码  |



###  设备接入
1. NB-IoT 模组装物联卡，上电。  
2. 终端通过串口 TTL 发送 AT 命令，配置网络，确认联网状态（以电信 NB-IoT 模组，利尔达 NB05-01 为例，其他模组初始化稍有差异）。 
```
AT+CFUN=0 //关闭射频功能
AT+CGMR //查询固件版本，可选
AT+CGSN=1 //查询IMEI 号，如果返回ERROR,说明模块没有设置IMEI 号，需要以下这步设置IMEI 号
AT+NTSETID=1, 201612091450303 //设置IMEI 号，仅在无IMEI 号时才需要此步骤，只能设置一次，再次设置无效。
AT+NCDP=XX.XX.XX.XX //设置IOT 平台IP 地址，COAP 协议需要用到，电信平台IP地址为117.60.157.137
AT+CGDCONT=1,”IP”,”PCCW” //设置APN, 当前上海OPENLAB 填写”IP”,”PCCW”，其他网络环境请事先确认 
AT+NRB //软重启
AT+CFUN=1 //开启射频全功能
AT+CSCON=1 //设置基站连接通知，可选
AT+CEREG=2 //设置连接核心网通知，可选
AT+NMMI=1 //下行数据通知
AT+CGATT=1 //自动搜网
AT+NUESTATS //查询UE 状态，包括rsrp,sinr,覆盖等级，小区信息等，可选
AT+CGPADDR //查询分配的ip 地址，可以以此判断是否连接到网络  
```
3. 上报数据  
```
AT+NMGS=len,data //发送len 字节数据，如果发送成功，会回复 OK，否则 ERROR
+NNMI:4, AAAA0000 //收到4 回复数据
```
len，data 由 [以上步骤]() 中的 SDK 生成，详细数据格式见 SDK 说明。  
执行 AT+NMGS 命令后，NB-IoT 模组发送完数据后，回复 OK，此时数据已经发给基站，但基站不一定接收成功。  
收到确认上报数据消息 AAAA0000，表示电信平台收到数据。（用户可以根据需要，设置重新上报数据次数，超时等待建议3秒）。  
4. 应用平台接收数据  
应用平台收到 http post 推送数据，body 内容示例如下：
```
{"payload":xxxx, "seq":12345, "timestamp":140000245, "topic":"/xx/xx/xx", "devicename":"xx", "productid":"xx"}
```  
5. 下发数据   
通过 RestAPI 接口下发数据到设备 [发布消息](https://cloud.tencent.com/document/product/634/12278)，RestAPI 发布消息后，终端会收到串口 TTL 返回的数据，如果没有及时收到，原因是 NB-IoT 模组与平台不是长连接，平台不能感知 NB-IoT 模组是否在线，终端主动上报一次数据，下发的消息就会立刻返回。 
 
### 状态查询
物联网通信提供 [查询设备状态](https://cloud.tencent.com/document/product/634/18341) 接口，可以查询设备最后一次上报数据的时间，用户可以根据当前时间对比来判断设备状态。  
例如，用户 NB-IoT 设备上报数据时间间隔为20小时，拉取最后上报数据的时间已经过去三天，即可判断设备状态异常。  









