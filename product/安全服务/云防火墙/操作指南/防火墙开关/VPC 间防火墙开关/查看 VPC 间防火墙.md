
## 查看状态监控

VPC 间防火墙状态监控支持统计防火墙整体带宽和各个实例的带宽，可以通过多个入口查询。
1. 登录 [云防火墙控制台](https://console.cloud.tencent.com/cfw/switch/vpc)，在左侧导航栏中，选择**防火墙开关** > **VPC 间开关**。
2. 在 VPC 间开关页面，支持如下三种方法呼出监控面板：
    - 单击状态监控右上角的![](https://qcloudimg.tencent-cloud.cn/raw/02c031118cb0fdc6af321639d5ade74d.jpg)，或单击**防火墙峰值带宽**与**单实例峰值带宽**面板可快速呼出监控面板。
![](https://qcloudimg.tencent-cloud.cn/raw/62a623635c19913fac7db3929a57445d.jpg)
    - 单击**防火墙实例**，选择所需防火墙，单击**操作** > **带宽监控**，可快速呼出监控面板。
  ![](https://qcloudimg.tencent-cloud.cn/raw/da8c6617aa6864b760c1d39e0d173152.jpg)
    - 单击**防火墙实例**，选择所需防火墙实例，单击**状态监控**，可快速呼出监控面板。
![](https://qcloudimg.tencent-cloud.cn/raw/32047bc17b110b576aa8e4663a91aa82.jpg)
3. 在监控面板中，可以基于①防火墙名称或②防火墙实例名称对监控维度进行筛选，也可以通过选择③时间范围修改统计维度。可以看到带宽的④监控曲线，也可以查阅防火墙或实例下所属开关的⑤峰值带宽数据。
>!不同时间范围的统计的最小统计颗粒度不同，可能会与实际峰值有误差，建议以 [腾讯云可观测平台](https://cloud.tencent.com/document/product/248) 的数据或具体防护单元的统计数据为准。
>
![](https://qcloudimg.tencent-cloud.cn/raw/34a05927abcb4996844b365a8614d97c.jpg)
4. 在监控面板中， 单击**查看监控指标**呼出腾讯云可观测平台的侧边栏，查看防火墙实例的全部监控指标数据，包括并发连接数、内网入包量、内网出包量、内网出带宽、内网入带宽。您也可以前往 [腾讯云可观测平台控制台](https://console.cloud.tencent.com/monitor) 查看详细指标或配置相关告警。
![](https://qcloudimg.tencent-cloud.cn/raw/bae436bb10b9fef754f69f8470adafb1.jpg)

## 查看规格信息
在 [防火墙开关页面](https://console.cloud.tencent.com/cfw/switch/vpc/vpc?tab=switch) 的规格信息模块中，可以查看规格信息，包括接入网络实例和 VPC 间防火墙实例。单击规则信息右上角的**升级扩容**，可以跳转到扩容界面。当前版本企业版用户最多可创建1个 VPC 间防火墙，旗舰版用户最多可以创建3个 VPC 间防火墙。
![](https://qcloudimg.tencent-cloud.cn/raw/061da6dc4df9faad178ec642c77e0f67.jpg)
