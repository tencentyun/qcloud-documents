宙斯盾 DDoS 高防包可为腾讯云公网 IP 地址提供高防能力。包括 [云服务器](https://cloud.tencent.com/doc/product/213/495)、[负载均衡](https://cloud.tencent.com/doc/product/214/524)、黑石服务器、黑石负载均衡、NAT IP、EIP、GAAP IP 等。DDoS 高防包使用简单，对于业务不可更改 IP 地址，或者有大量 IP 需要防护的场景下，可以快速简单地完成防护配置。目前 DDoS 高防包有单 IP 模式和多 IP 模式。

本文档将详细说明 DDoS 高防包配置接入的步骤。如何选择购买配置，详情请参见 [**产品配置说明**](https://cloud.tencent.com/document/product/685/18798)。

## 流程图
![0](https://main.qcloudimg.com/raw/56680ef9138fe084b097b0ca753b9636.png)

## 接入步骤
1. **购买 DDoS 高防包**
a. 用户进入 [宙斯盾高防控制台](https://console.cloud.tencent.com/gamesec)，在左侧目录中，单击【DDoS 高防包】，在 “高防包列表” 的下，单击【购买】。
![1](https://main.qcloudimg.com/raw/3117e8b78bd394bd3afa7e3126adc839.png)
b. 选择好配置，单击【立即下单】。
![](https://main.qcloudimg.com/raw/eabb20d1e28f144d656b8f246b893ae5.png)
弹性防护支持两种计费模式，详情请参见 “产品配置说明” 文档的 [确定高防包配置方案](https://cloud.tencent.com/document/product/685/18798#.E7.A1.AE.E5.AE.9A.E9.AB.98.E9.98.B2.E5.8C.85.E9.85.8D.E7.BD.AE.E6.96.B9.E6.A1.88) 的弹性计费模式、弹性流量包、弹性带宽峰值。
![3](https://main.qcloudimg.com/raw/73f2289fc484b77fc07ee09d55968535.png)
c. 在 “DDoS 高防包” 下，单击【弹性流量包管理】，单击【购买弹性流量包】。
![4](https://main.qcloudimg.com/raw/a8b44642c3f3153f15fa9acb489b4faa.png)
![5](https://main.qcloudimg.com/raw/2cf7230a7be90f44877bb5fdd29a06ff.png)
2. **绑定防护 IP**
a. 在 “DDoS 高防包” 页面的【高防包列表】下，单击高防包 ID，进入基本信息页。
![6](https://main.qcloudimg.com/raw/e3112d0601ccb3b11d7cc0a8fb6db583.png)
b. 在 “DDoS 高防包详情” 页面下，单击【防护 IP 列表】，单击【添加防护 IP】。
![7](https://main.qcloudimg.com/raw/2f323e4e6afbd9e08ffb76631b328f43.png)
c. 在 “添加防护 IP” 弹窗中，勾选好云服务器的 “IP 地址”，单击【确定】。
![8](https://main.qcloudimg.com/raw/0d293932f0b4d96dcc365d0b94b8c2b0.png)
d. 添加成功后，在【防护 IP 列表】下，可以看到该 IP 地址即可以获得 DDoS 高防包防护了。
![9](https://main.qcloudimg.com/raw/75c262c24a13aae92a8b6c036ac369d8.png)
