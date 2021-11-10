## 操作场景

本文档主要指导您如何申请自有域名，并购买绑定高防 IP，回源到 MGOBE 提供的域名上，实现游戏对战引擎结合高防能力，清洗异常流量，保障业务稳定可用。

## 操作步骤

### 步骤1：申请自有域名

<dx-alert infotype="explain" title="">
若您有已备案的域名，可直接跳过此步骤前往 [步骤2](#test2)。
</dx-alert>

#### 1.1 获取域名

您可前往 [域名注册](https://dnspod.cloud.tencent.com/) 或从其他服务上处获取域名。

#### 1.2 域名备案

您可参考 [网站备案](https://cloud.tencent.com/product/ba) 进行域名备案。

[](id:test13)
#### 1.3 配置证书

您可参考 [SSL 证书](https://console.cloud.tencent.com/ssl) 购买证书或者上传证书。


[](id:test2)
### 步骤2：结合高防服务

#### 2.1 购买高防服务

您可购买 [DDoS 高防 IP](https://cloud.tencent.com/product/ddos-advanced?/product/ddos-bgpip)，根据业务需求选择不同的规格套餐。购买成功后可在 [DDoS 防护控制台-实例列表](https://console.cloud.tencent.com/ddos/antiddos-advanced/package) 查看**高防 IP**等信息。

<dx-alert infotype="explain" title="">
您购买好高防服务后，请 [联系我们](https://cloud.tencent.com/document/product/1038/33359) 支持您配置回源域名。
</dx-alert>


#### 2.2 自有域名解析

您可参考 [快速添加域名解析](https://cloud.tencent.com/document/product/302/3446)，将域名解析到购买的高防 IP 上。

#### 2.3 配置回源域名

1. 登录 [DDoS 防护控制台](https://console.cloud.tencent.com/ddos/antiddos-advanced/access/l4)，在左侧导航栏单击**业务接入**。
2. 在“业务接入”页面，单击**域名接入**>**添加域名**。
![](https://main.qcloudimg.com/raw/315d2987ff294e027156e770851e2c02.jpg)
3. 在添加“转发规则”页面中，根据实际需求配置2条转发规则，以下以配置433端口为例。
<img src="https://main.qcloudimg.com/raw/c042c6154a9fc767debc96c624f60532.png"  style="width: 65%;"><br>
	- 关联高防 IP：选择之前购买的高防实例 IP。
	- 域名：填写自有域名。
	- 协议：选择 https，配置两条转发规则，一个端口配置443，另一个端口配置5443。
	- 证书来源：腾讯云托管证书.
	- 证书：选择 [配置证书](#test13) 上购买或者上传的证书。
	- 回源方式：选择域名回源。
	- 源站域名：格式为 `MGOBE 控制台游戏域名:端口号（与上方协议端口保持一致）`。

<dx-alert infotype="explain" title="">
- 需要添加2个转发规则，一个对应443端口，一个对应5443端口。
- 源站域名：通过 **[MGOBE 控制台](https://console.cloud.tencent.com/minigamecloud)**>**游戏概览**>**基础信息**>**域名**获取。
</dx-alert>

4. 验证域名接入成功
[DDoS 防护控制台](https://console.cloud.tencent.com/ddos/antiddos-advanced/access/l7) 确认域名“接入状态”为成功。
![](https://main.qcloudimg.com/raw/7882a3d8949e6cf10b3d92b0953a24e6.png)

#### 2.4 本地验证

转发配置完成后，DDoS 高防 IP 将按照转发规则将相关端口的报文转发到源站的对应端口。为了最大程度保证业务的稳定，建议在全面切换业务之前先进行本地测试。具体的验证方法如下：
测试联通性和 IP 是否是高防 IP。
```
ping  <自有域名>
```

### 步骤3：游戏基本功能测试

将游戏客户端域名替换为自有域名，测试 MGOBE 功能是否正常。

