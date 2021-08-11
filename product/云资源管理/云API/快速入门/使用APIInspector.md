API Inspector 是云 API 新推出的一款产品功能，用户可通过此功能查看控制台每一步操作关联的 API 调用情况，并自动生成各语言版本的 API 代码，也可前往 [API Explorer](https://cloud.tencent.com/document/product/1278/46697) 进行在线调试。 


<dx-alert infotype="notice" title="">
 - API Inspector 仅展示公开的 [云 API 3.0](https://cloud.tencent.com/document/api) 接口信息。
 - API Inspector 已在腾讯云多款产品控制台上开放，详情请参见 [支持产品列表](#SupportProducts)。
 - 刷新浏览器当前页面，则会清空刷新前的调用记录。
</dx-alert>


## 功能特性

API Inspector 与 API Explorer 共同成为腾讯云 API 用户学习和调试 API 的一体化解决方案，具有以下特性：
- **自动录制**：如果您想要了解功能背后的 API，可在控制台操作相应的功能时获得相关 API 调用信息，详情请参见 [自动录制 API 调用](#AutomaticRecordingAPI)。                         
- **一键生成**：自动生成各语言的 API 代码片段参数预填充，可直接运行，详情请参见 [一键生成 API 代码](#AutomaticGeneratedAPI)。                         
- **在线调试**：提供 API Explorer 一键在线调试功能，可实现自动生成多语言 SDK 代码、在线调用、发送真实请求及签名串自动生成等功能。降低了 SDK 的使用难度，详情请参见 [API Explorer 在线调试](#APIExplorer)。
- **响应结果**：支持一键查看本次调用的响应结果，详情请参见 [查看响应结果](#ResponseResult)。
 
## 功能介绍
### 开启 API Inspector 功能
请按照以下步骤，开启 API Inspector 功能：
1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/instance/index?rid=1)。      
2. 选择页面上方的<img src="https://main.qcloudimg.com/raw/4d7384619e988df262e740e376ed047c.png" style="margin:-4px 0px"> > 【API】，即可开启 API Inspector 功能。如下图所示：
![](https://main.qcloudimg.com/raw/d64d1c72c6150f03763d55cf84e90ec6.png)      

### 自动录制 API 调用<span id="AutomaticRecordingAPI"></span>
本文以修改实例名称为例，介绍 API Inspector 的自动录制功能：
1. 将某个实例名称修改为 API Inspector，具体操作请参见 [修改实例名称](https://cloud.tencent.com/document/product/213/16562)。
2. 开启 API Inspector 功能，即可查看涉及改名操作的所有 API 调用。如下图所示：
![](https://main.qcloudimg.com/raw/61c3bdd96ef5996e76c8a26aef25ccfd.png)
您可勾选“隐藏Describe类接口”，查看功能核心接口。如下图所示： 
![](https://main.qcloudimg.com/raw/13e7d5ea7d15920bc8b31f7bf834c160.png)


### 一键生成 API 代码<span id="AutomaticGeneratedAPI"></span>
当控制台操作涉及的 API 录制完成后，您可单击 API 名称，一键生成 Java、Python、Node.js、PHP、GO 及 .NET 语言的 API 代码片段及参数预填充。可选择<img src="https://main.qcloudimg.com/raw/c87d07f7c2d1f7519b9b80f19d158e62.png" style="margin:-3px 0px">复制对应格式的代码段，如下图所示：
![](https://main.qcloudimg.com/raw/7b3ec4af4b4c58ff3370636624a388fd.png)


### API Explorer 在线调试<span id="APIExplorer"></span>
您可选择 <img src="https://main.qcloudimg.com/raw/753d4cb89c7dc582b11ed66811143716.png" style="margin:-3px 0px"> 或【前往API Explorer】，使用 API Explorer 工具直接调试对应的功能，也可选择 <img src="https://main.qcloudimg.com/raw/68a84eebfed1c31bf37294902156d986.png" style="margin:-3px 0px"> 查看对应接口文档。如下图所示：
![](https://main.qcloudimg.com/raw/b90455b43fdcaa11e8d5a91acd08f656.png)

### [查看响应结果](id:ResponseResult)
您可选择 <img src="https://main.qcloudimg.com/raw/478d4386a7ef12def9929511521d3a7a.png" style="margin:-3px 0px"> 查看本次调用的响应结果，查看完毕后选择 <img src="https://main.qcloudimg.com/raw/b7c7824e15a02311907f3fae3474cfc7.png" style="margin:-3px 0px"> 收起响应结果。如下图所示：
![](https://main.qcloudimg.com/raw/9c7517241b774e21b8fa5c1cd1895160.png)

## 附录
### [支持产品列表](id:SupportProducts)
目前 API Inspector 功能已在如下产品控制台开放：
<table>
<tr>
<th style="width:15%">产品类别</th>
<th>具体产品</th>
</tr>
<tr>
<td>基础</td>
<td>云服务器、私有网络、批量计算、文件存储、云硬盘、黑石物理服务器1.0、轻量应用服务器、弹性伸缩、容器服务、云函数、内容分发网络、全站加速网络、全球应用加速、消息队列 CKafka、API 网关、短信、腾讯微服务平台 TSF、视频处理、云直播、容器镜像服务、智能编辑、邮件推送</td>
</tr>
<tr>
<td>数据库</td>
<td>云数据库 Redis、云数据库 MongoDB、云数据库 Memcached、数据传输服务、云数据库 MySQL、云数据库 SQL Server、云数据库 PostgreSQL、游戏数据库 TcaplusDB、云数据库 MariaDB</td>
</tr>
<tr>
<td>安全</td>
<td>主机安全、云加密机、密钥管理系统、漏洞扫描服务、数据安全审计、敏感数据处理、堡垒机、数据安全治理中心、验证码、云防火墙、凭据管理系统、流量反欺诈、联邦学习、借贷反欺诈、定制建模、保险反欺诈、营销风控、安全托管服务</td>
</tr>
<tr>
<td>大数据</td>
<td>腾讯云搜</td>
</tr>
<tr>
<td>人工智能</td>
<td>人脸识别、腾讯智能对话平台、智能钛弹性模型服务、人脸融合、图像分析、智能钛机器学习平台、人脸试妆、智能钛机器学习、人像变换、人体分析</td>
</tr>
<tr>
<td>企业应用</td>
<td>物联卡、物联网通信、物联网开发平台、物联网设备身份认证、物联网智能视频服务、云呼叫中心、域名注册、品牌经营管家</td>
</tr>
<tr>
<tr>
<td>行业应用</td>
<td>智聆口语评测、金融联络机器人、数学作业批改、游戏联机对战引擎、英文作文批改、正版曲库直通车、企业收付平台、游戏服务器伸缩、互动白板、正版图库直通车、政务联络机器人、招生通</td>
</tr>
<td>开发者服务</td>
<td>云监控、云拨测、访问管理、云审计、标签、应用与服务编排工作流、云顾问</td>
</tr>
<tr>
<td>方案与支持</td>
<td>小程序 · 云直播</td>
</tr>
</table>






