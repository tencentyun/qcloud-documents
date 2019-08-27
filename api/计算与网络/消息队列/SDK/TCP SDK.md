CMQ 目前已开放基于 TCP 协议的 SDK 调用，支持普通消息、事务消息、延迟消息、异步消息的收发功能。其中，事务消息特性仅通过 TCP 方式实现。
TCP 协议目前支持公网访问以及私有网络的 CVM 内网访问方式，暂时不支持基础网络的内网访问方式。
本文主要介绍 TCP SDK 使用方式，提供 Demo 工程的安装、下载、配置及运行示例，帮助工程师快速搭建 CMQ 测试工程。
## TCP 协议优势
- **更少的计算资源**
HTTP 针对请求鉴权，每次请求都需要签名；TCP 针对链接鉴权，只需要建立连接的时候对链接鉴权，节约客户端计算资源。
- **更安全的客户端线程**
HTTP 客户端非线程安全；TCP 客户端线程安全，多个线程可使用相同的链接，节省链接资源。
- **更高效的传输效率**
TCP 传输提高有效数据占比，在相同客户端下，拥有更高的吞吐量和 QPS，相比 HTTP 具有更高效的传输效率。
- **更优的使用体验**
TCP 支持异步接口，支持回调。
- **更多样的特性支持**
TCP 支持 CMQ 最新的分布式消息事务。

## Demo工程使用
### 准备 Demo 环境
1. **安装 IDE**
您可以安装 IntelliJ IDEA 或者 Eclipse，本文以 IntelliJ IDEA 为例进行说明。
请在 [下载 IntelliJ IDEA Ultimate 版本](https://www.jetbrains.com/idea/)，并参考 IntelliJ IDEA 说明进行安装。
2. **下载 Demo 工程**
请在 [下载 CMQ 的 Demo 工程](https://github.com/tencentyun/cmq-java-tcp-sdk) 到本地，解压后即可看到本地新增的 cmq-java-tcp-sdk-master 文件夹。

### 配置 Demo 工程
1. **创建资源**
您需要在控制台创建所需消息队列资源，包括 CMQ 队列名、SecretID、SecretKey。
具体创建过程请参考 [队列模型快速入门](https://cloud.tencent.com/document/product/406/8436) 和 [主题模型快速入门](https://cloud.tencent.com/document/product/406/8437)。
2. **导入 Demo 工程文件**
在 IDEA 的开机界面打开文件夹。
![](https://main.qcloudimg.com/raw/8a3ba96ef290ad50f6f0d20c01594f5d.png)
打开文件夹后，文件层级关系如下，Demo 工程文件存于 Demo 文件夹下。
![](https://main.qcloudimg.com/raw/1fc9235f7ae621fec4105fb173725d89.png)
3. **配置 Demo 参数**<span id="peizhi"></span>
修改文件 NameServer 地址、密钥对及消息队列名，NameServer 地址请参考 [NameServer 对照表](#Nameserver)。
以 ProducerDemo 为例，配置如下：
```
producer.setNameServerAddress(“对应的NameSever”)；
producer.setSecretID(“获取的SecretID”)
producer.setSecretKey(“获取的SecretKey”)
String queue = “创建的队列名”
```
具体图示如下：
![](https://main.qcloudimg.com/raw/7bee345ab49daac395329ff70d3be787.png)

### 运行 Demo
#### 使用队列模型收发消息
 1. [配置 Demo 参数](#peizhi)。
 2. 执行文件 ProducerDemo，成功后显示日志如下：
 ![](https://main.qcloudimg.com/raw/151a28f513b8eebe78eea9e47fe2b732.png)
 ProducerDemo 支持普通消息、延时消息、异步消息的发送。
![](https://main.qcloudimg.com/raw/75fae413af9db02c612f0e9f49230c98.png)
 3. 执行文件 ConsumerDemo，可接收消息。

#### 使用主题模型收发消息
 1. 运行 PublishDemo 类以主题模型进行消息发送。
 2. 运行 SubscriberDemo 类以主题模式进行消息接收。

#### 收发事务消息
 1. 运行 ProducerTransactionDemo 类进行事务消息发送。
 2. 运行 SubscriberTransactionDemo 类进行事务消息接收。

## Nameserver 对照表<span id="Nameserver"></span>
| 地区     | 公网地址   | VPC 地址       |    
| -------- | ------------ | -------------------------- | 
| 印度     | http://cmq-nameserver-in.tencentcloudapi.com | http://cmq-nameserver-vpc-in.api.tencentyun.com | 
| 北京     | http://cmq-nameserver-bj.tencentcloudapi.com| http://cmq-nameserver-vpc-bj.api.tencentyun.com |   
| 上海     |http://cmq-nameserver-sh.tencentcloudapi.com| http://cmq-nameserver-vpc-sh.api.tencentyun.com |  
| 广州     | http://cmq-nameserver-gz.tencentcloudapi.com | http://cmq-nameserver-vpc-gz.api.tencentyun.com |  
| 北美     | http://cmq-nameserver-ca.tencentcloudapi.com| http://cmq-nameserver-vpc-ca.api.tencentyun.com |   
| 成都     | http://cmq-nameserver-cd.tencentcloudapi.com | http://cmq-nameserver-vpc-cd.api.tencentyun.com|    
| 重庆     | http://cmq-nameserver-cq.tencentcloudapi.com | http://cmq-nameserver-vpc-cq.api.tencentyun.com |    
| 中国香港     |http://cmq-nameserver-hk.tencentcloudapi.com | http://cmq-nameserver-vpc-hk.api.tencentyun.com |    
| 韩国     | http://cmq-nameserver-kr.tencentcloudapi.com | http://cmq-nameserver-vpc-kr.api.tencentyun.com |     
| 俄罗斯   | http://cmq-nameserver-ru.tencentcloudapi.com | http://cmq-nameserver-vpc-ru.api.tencentyun.com|     
| 新加坡   | http://cmq-nameserver-sg.tencentcloudapi.com                 | http://cmq-nameserver-vpc-sg.api.tencentyun.com          |     
| 上海金融 | http://cmq-nameserver-shjr.tencentcloudapi.com | http://cmq-nameserver-vpc-shjr.api.tencentyun.com  |
| 深圳金融 | http://cmq-nameserver-szjr.tencentcloudapi.com | http://cmq-nameserver-vpc-szjr.api.tencentyun.com|     
| 泰国     | http://cmq-nameserver-th.tencentcloudapi.com| http://cmq-nameserver-vpc-th.api.tencentyun.com |     
| 美东     | http://cmq-nameserver-use.tencentcloudapi.com | http://cmq-nameserver-vpc-use.api.tencentyun.com        |  
| 美西     | http://cmq-nameserver-usw.tencentcloudapi.com | http://cmq-nameserver-vpc-usw.api.tencentyun.com |     
