<style rel="stylesheet">
table th:nth-of-type(1){
width:200px;
}</style>
<style rel="stylesheet">
table th:nth-of-type(2){
width:200px;
}</style>
<style rel="stylesheet">
table th:nth-of-type(3){
width:200px;
}</style>
<style rel="stylesheet">
table th:nth-of-type(4){
width:200px;
}</style>
<style rel="stylesheet">
table tr:hover {
background: #efefef; 
</style>
## 基本概念
网络访问控制列表（Access Control List，ACL）是一个子网级别无状态的可选安全层，用于控制进出子网的数据流，可以精确到协议和端口粒度。如下图所示，其规则与 <a href="https://cloud.tencent.com/doc/product/213/500" target="_blank">安全组</a> 相似。但由于网络 ACL 无状态的特性，即使设置入站规则允许某些访问，如果没有设置相应的出站规则会导致无法响应访问。
<div style="text-align:center">
![](//mccdn.qcloud.com/static/img/04de33187d40d6891f7e5c8da120fdc7/image.png)

</div>
## 使用场景
用户可以为具有相同网络流量控制的子网关联同一个网络 ACL，通过设置出站和入站允许规则，对进出子网的流量进行精确控制。例如，您在腾讯云私有网关内托管多层 Web 应用，创建了不同子网分别部署 Web 层、逻辑层和数据层服务，通过网络 ACL 您可以控制这三个子网之间的访问：Web 层子网和数据库层子网无法相互访问，只有逻辑层可以访问 Web 层和数据层子网。

## ACL规则
ACL 规则是网络 ACL 的组成部分。当您在网络 ACL 中添加或删除规则时，更改也会自动应用到与其相关联的子网。
网络 ACL 规则包括以下四个组成部分：
- 协议类型，如 TCP、UDP 和 HTTP 等。
- 目的端口或端口范围。
- 源数据（入站）或目标数据（出站）的 IP 或者 IP 范围（以 CIDR 表示）。
- 策略：允许或拒绝。

腾讯云根据与子网关联的 ACL 入站/出站规则评估数据包，判断数据包是否允许流向/流出子网。

## 规则优先级
网络 ACL 规则的应用顺序保持由规则第一条（列表顶端）开始应用至最后一条（列表末尾）。若有规则/部分规则冲突，默认应用 **位置更前** 的规则。
例如，需要允许所有源 IP 对云服务器所有端口进行访问，同时唯一拒绝源 IP 为 `192.168.200.11/24` 的机器 HTTP 访问 80 端口。则可按以下方式设置：

| 协议类型 | 端口 | 源IP | 策略|
|:---------:|:---------:|:--------:|:------:|
| HTTP |80 | 192.168.200.11/24 | 拒绝|
| ALL |ALL | 0.0.0.0/0 | 允许|

## 临时端口范围
临时端口是客户端发起请求时配置的端口，设置网络 ACL 出站规则时需注意这点。由于网络 ACL 无状态的特性，即使设置入站规则允许某些访问，如果没有设置相应的出站规则会导致无法响应访问。

例如：某客户端向 VPC 内某子网中主机发起请求，该子网关联了网络 ACL。客户端默认配置的端口属于临时端口范围。如果网络 ACL 出站规则中没有设置允许对应临时端口的流量，那么客户端的请求将无法返回。根据客户端的操作系统不同，临时端口范围也随之不同。
- 许多 Linux 内核使用端口 32768-61000
- Windows Server 2003 使用端口 1025-5000
- Windows Server 2008 使用端口 49152-65535

因此，如果一项来自 Internet 上的 Windows XP 客户端的请求访问您的 VPC 内某子网的 Web 服务器，该子网关联了网络 ACL，则您的网络 ACL 必须有相应的出站规则，允许目标端口为 `25-5000`的数据流通过。

## 安全组与网络 ACL 的区别
| 安全组 | 网络 ACL | 
|---------|---------|
|  CVM 实例级别的流量控制（第一防御层） | 子网级别的流量控制（第二防御层） | 
| 支持允许规则和拒绝规则 | 支持允许规则和拒绝规则 | 
| 有状态：返回数据流会被自动允许，不受任何规则的影响 | 无状态：返回数据流必须被规则明确允许 | 
| 只有在启动 CVM 实例的同时指定安全组、或稍后将安全组与实例关联的情况下，操作才会被应用到实例 | 自动应用到关联子网内的所有 CVM 实例（备份防御层，若CVM 实例为绑定安全组，这里可以做备份防御） | 

## 使用约束
关于网络 ACL 您需要了解：
- 一个网络 ACL 可以绑定多个子网，但一个子网同一时间只能绑定一个网络 ACL。
- 网络 ACL 有单独的入站和出站规则，每条规则包括协议类型、端口、源/目的 IP，策略（拒绝/允许）和备注。
- 每个新建网络 ACL 最初都为关闭状态（不允许任何数据流），直至您添加规则为止。
- 网络 ACL 没有任何状态，对允许入站数据流的响应会随着出站数据流规则的变化而改变（反之亦然），亦即您需要分别对请求和响应数据流设置规则。
- 网络 ACL 对所关联子网内的 CVM 实例之间的互访不产生影响。

| 资源| 限制（个） | 
|---------|---------|
| 每个私有网络内网络 ACL 数 | 50|
| 每个网络 ACL 中规则数 | 入站方向：20 条，出站方向：20 条|
| 每个子网关联的网络 ACL 个数 | 1 |
|每个网络 ACL 关联的子网个数|无限制|

## 计费方式
网络 ACL 服务免费。有关私有网络的其他服务费用，可以参考 <a href="https://cloud.tencent.com/doc/product/215/3079" target="_blank">VPC 所有服务计费总览</a>
## 操作指南

### 创建网络 ACL
1) 登录 <a href="https://console.cloud.tencent.com/" target="_blank">腾讯云控制台</a> 点击导航条【私有网络】，进入 <a href="https://console.cloud.tencent.com/vpc/vpc?rid=8" target="_blank">私有网络控制台</a>，左侧选择【安全】-【网络 ACL】选项卡。
2) 点击【新建】按钮，在新建网络 ACL 弹出框中输入名称、选择所属的私有网络，点击确定完成。

###  查看网络 ACL 列表
1)	登录 <a href="https://console.cloud.tencent.com/" target="_blank">腾讯云控制台</a> 点击导航条【私有网络】，进入 <a href="https://console.cloud.tencent.com/vpc/vpc?rid=8" target="_blank">私有网络控制台</a>，左侧选择【安全】-【网络 ACL】选项卡。
2)	在顶部选择地域及私有网络，即可查看属于此私有网络的网络 ACL 列表。

### 增加网络 ACL 规则
1) 登录 <a href="https://console.cloud.tencent.com/" target="_blank">腾讯云控制台</a> 点击导航条【私有网络】，进入 <a href="https://console.cloud.tencent.com/vpc/vpc?rid=8" target="_blank">私有网络控制台</a>，左侧选择【安全】-【网络 ACL】选项卡。
2) 在列表中点击要修改的网络 ACL 的 ID，进入网络 ACL 详情页。
3) 点击【入站规则】或【出站规则】选项卡，在规则列表旁点击【编辑】按钮，在编辑状态下点击【新增一行】按钮。
4) 新增的规则会默认加入规则列表的 **首行**，选择协议类型并输入端口、源 IP/目的 IP 和策略，点击【保存】按钮。新增的规则即会显示在 ACL 规则列表中。

### 删除网络 ACL 规则
1) 登录 <a href="https://console.cloud.tencent.com/" target="_blank">腾讯云控制台</a> 点击导航条【私有网络】，进入 <a href="https://console.cloud.tencent.com/vpc/vpc?rid=8" target="_blank">私有网络控制台</a>，左侧选择【安全】-【网络 ACL】选项卡。
2) 在列表中点击要修改的网络 ACL 的 ID，进入网络 ACL 详情页。
3) 点击【入站规则】或【出站规则】选项卡，在规则列表旁点击【编辑】按钮，在编辑状态下点击 ACL 规则后方的【删除】按钮。
4) 此时本条 ACL 规则置灰。若本次删除属于误操作，则可通过点击【恢复删除】按钮将其恢复。
5) 点击【保存】按钮，保存上述操作。
>注：ACL规则的删除必须保存后才会生效。

### 子网关联网络 ACL
1) 登录 <a href="https://console.cloud.tencent.com/" target="_blank">腾讯云控制台</a> 点击导航条【私有网络】，进入 <a href="https://console.cloud.tencent.com/vpc/vpc?rid=8" target="_blank">私有网络控制台</a>，左侧选择【安全】-【网络 ACL】选项卡。
2) 点击需要关联的网络 ACL 的 ID，进入网络 ACL 详情页。
3) 点击【基本信息】选项卡，在关联子网部分点击【新增关联】按钮。
4) 在关联子网弹出框中，选择需要关联的本私有网络下的子网，点击【确定】按钮，即可成功关联网络 ACL 与子网。

### 子网解关联网络 ACL
1) 登录 <a href="https://console.cloud.tencent.com/" target="_blank">腾讯云控制台</a> 点击导航条【私有网络】，进入 <a href="https://console.cloud.tencent.com/vpc/vpc?rid=8" target="_blank">私有网络控制台</a>，左侧选择【安全】-【网络 ACL】选项卡。
2) 点击需要解关联的网络 ACL 的 ID，进入网络 ACL 详情页。
3) 点击【基本信息】选项卡，在关联子网列表中需要解关联的子网项后点击【解绑】按钮；或勾选所有需要解绑的子网，点击【批量解绑】按钮，即可解绑该子网与网络 ACL。

###  删除网络 ACL
1) 登录 <a href="https://console.cloud.tencent.com/" target="_blank">腾讯云控制台</a> 点击导航条【私有网络】，进入 <a href="https://console.cloud.tencent.com/vpc/vpc?rid=8" target="_blank">私有网络控制台</a>，左侧选择【安全】-【网络 ACL】选项卡。
2) 点击需要删除的网络 ACL 的【删除】按钮，在确认删除弹出框中点击【确定】，即可删除本网络 ACL 及本网络 ACL 的所有规则。
3)	若【删除】按钮置灰，则表示本网络 ACL 正与子网相关联，您需要先解除这些关联后才能进行删除操作。
 
## API 概览
您可以使用 API 操作来设置和管理网络 ACL 相关接口，有关 VPC API 的更多功能可以查看 <a href="https://cloud.tencent.com/doc/api/245/909" target="_blank">VPC 所有 API 概览</a>。

| 接口功能 | Action ID | 功能描述 |
|:---------:|:---------:|:---------:|
| 创建 VPC 网络 ACL | <a href="http://cloud.tencent.com/doc/api/245/%E5%88%9B%E5%BB%BAVPC%E7%BD%91%E7%BB%9CACL" target="_blank">CreateNetworkAcl</a>[CreateNetworkAcl](http://cloud.tencent.com/doc/api/245/%E5%88%9B%E5%BB%BAVPC%E7%BD%91%E7%BB%9CACL) | 创建安全防火墙。 |
| 删除网络 ACL | <a href="http://cloud.tencent.com/doc/api/245/%E5%88%A0%E9%99%A4%E7%BD%91%E7%BB%9CACL" target="_blank">DeleteNetworkAcl</a>) | 删除指定安全防火墙。 |
| 修改网络 ACL 名称 | <a href="http://cloud.tencent.com/doc/api/245/%E4%BF%AE%E6%94%B9%E7%BD%91%E7%BB%9CACL%E5%90%8D%E7%A7%B0" target="_blank">ModifyNetworkAcl</a> | 修改安全防火墙名称。 |
| 查询网络 ACL 列表 | <a href="http://cloud.tencent.com/doc/api/245/%E6%9F%A5%E8%AF%A2%E7%BD%91%E7%BB%9CACL%E5%88%97%E8%A1%A8" target="_blank">DescribeNetworkAcl</a> | 查询 VPC 安全防火墙列表。 |
| 设置网络 ACL 规则 | <a href="http://cloud.tencent.com/doc/api/245/%E8%AE%BE%E7%BD%AE%E7%BD%91%E7%BB%9CACL%E8%A7%84%E5%88%99" target="_blank">ModifyNetworkAclEntry</a> | 设置安全防火墙网络规则。 |
| 网络 ACL 绑定子网 | <a href="http://cloud.tencent.com/doc/api/245/%E7%BD%91%E7%BB%9CACL%E7%BB%91%E5%AE%9A%E5%AD%90%E7%BD%91" target="_blank">CreateSubnetAclRule</a> | 安全防火墙绑定子网。 |
| 网络 ACL 解绑子网 | <a href="http://cloud.tencent.com/doc/api/245/%E7%BD%91%E7%BB%9CACL%E8%A7%A3%E7%BB%91%E5%AD%90%E7%BD%91" target="_blank">DeteleSubnetAclRule</a> | 安全防火墙和子网解绑。 |

