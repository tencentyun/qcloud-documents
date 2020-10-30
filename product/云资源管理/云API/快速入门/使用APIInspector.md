API Inspector 是云 API 新推出的一款产品功能，用户可通过此功能查看控制台每一步操作关联的 API 调用情况，并自动生成各语言版本的 API 代码，也可前往 [API Explorer](https://cloud.tencent.com/document/product/1278/46697) 进行在线调试。 

>!
>- API Inspector 仅展示公开的 [云 API 3.0](https://cloud.tencent.com/document/api) 接口信息。
> - API Inspector 功能目前处于控制台和用户双维度灰度阶段。
> 控制台目前仅在云服务器控制台的 [实例](https://console.cloud.tencent.com/cvm/instance/index?rid=1)、[专用宿主机](https://console.cloud.tencent.com/cvm/cdh)、[置放群组](https://console.cloud.tencent.com/cvm/ps)、[弹性伸缩](https://console.cloud.tencent.com/autoscaling/group)，[SSH密钥](https://console.cloud.tencent.com/cvm/sshkey) 以及 [回收站](https://console.cloud.tencent.com/cvm/recycler/cvm?rid=1) 菜单中开放。
> - 刷新浏览器当前页面，则会清空刷新前的调用记录。

## 功能特性

API Inspector 与 API Explorer 共同成为腾讯云 API 用户学习和调试 API 的一体化解决方案，具有以下特性：
- **自动录制**：如果您想要了解功能背后的 API，可在控制台操作相应的功能时获得相关 API 调用信息，详情请参见 [自动录制 API 调用](#AutomaticRecordingAPI)。                         
- **一键生成**：自动生成各语言的 API 代码片段参数预填充，可直接运行，详情请参见 [一键生成 API 代码](#AutomaticGeneratedAPI)。                         
- **在线调试**：提供 API Explorer 一键在线调试功能，可实现自动生成多语言 SDK 代码、在线调用、发送真实请求及签名串自动生成等功能。降低了 SDK 的使用难度，详情请参见 [API Explorer 在线调试](#APIExplorer)。
 
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
