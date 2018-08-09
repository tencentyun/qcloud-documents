宙斯盾 DDoS 高防包可为腾讯云公网 IP 地址提供高防能力。包括 [云服务器](https://cloud.tencent.com/doc/product/213/495)、[负载均衡](https://cloud.tencent.com/doc/product/214/524)、黑石服务器、黑石负载均衡、NAT IP、EIP、GAAP IP 等。DDoS 高防包使用简单，对于业务不可更改 IP 地址，或者有大量 IP 需要防护的场景下，可以快速简单的完成防护配置。目前 DDoS 高防包有单 IP 模式和多 IP 模式。

本文档说明 DDoS 高防包配置接入的步骤。如何选择购买配置，详情请参见 [**产品配置说明**](https://cloud.tencent.com/document/product/685/18798)。

### 流程图
![](https://main.qcloudimg.com/raw/56680ef9138fe084b097b0ca753b9636.png)

### 配置上线

#### 1. 购买 DDoS 高防包
a. 用户进入 [宙斯盾高防控制台](https://console.cloud.tencent.com/gamesec)，在左侧目录中，选择 “DDoS 高防包”，单击【购买】。

![](https://main.qcloudimg.com/raw/f35fd24e82d70a4cc9e4f8a06db8e7ce.png)

b. 选好配置后，单击【立即下单】。

![](https://i.imgur.com/WubfeN7.png)
>弹性防护支持两种计费模式：
>	** 弹性流量包**
 弹性流量包需要预付购买，攻击超过保底防护带宽峰值发生弹性防护用量时，按照弹性流量用量从流量包中扣除。与弹性带宽方式相比，对于攻击频率低、攻击带
宽峰值高而持续时间短的场景，能够显著降低用户的弹性防护费用支出
> **  弹性带宽峰值**
 对于业务被攻击较频繁，攻击持续时间较长的场景，则可以使用按弹性带宽峰值方式计费，弹性带宽按天后付费。
 
![](https://main.qcloudimg.com/raw/73f2289fc484b77fc07ee09d55968535.png)

>弹性防护峰值-弹性计费模式选择为 “弹性流量包” 时，若发生弹性防护，则会从同区域的已购买弹性流量包中扣除弹性发生的流量，若未购买弹性流量包，或弹性流量包额度用完，则弹性防护能力会暂停。若选择 “弹性带宽峰值” 计费方式，则按发生弹性防护用量时，按带宽峰值计费。

c. “弹性流量包” 可以在 “DDoS 高防包” 管理列表下，单击 “弹性流量包管理” 页签，单击【购买弹性流量包】。

![](https://i.imgur.com/x8l5VxC.png)

![](https://i.imgur.com/EsZfSDe.png)


#### 2. 绑定防护IP
a. 单击高防包 ID，进入基本信息页。

![](https://main.qcloudimg.com/raw/619c3476c3f1457aebc12796218823ed.png)

b. 选择 “防护 IP 列表”，单击【添加防护 IP】。

![](
https://main.qcloudimg.com/raw/c8450c45a575ae200ab2e2588805cafb.png)

c. 勾选云服务器 IP 地址，单击【确定】。

![](https://i.imgur.com/UPpqQAY.png)

d. 添加成功后，可以在 “防护 IP 列表” 下看到该 IP，该 IP 地址即可以获得 DDoS 高防包防护了。

![](https://i.imgur.com/hEHODtG.png)
