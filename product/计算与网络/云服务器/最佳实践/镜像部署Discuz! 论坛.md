## 操作场景
本文档介绍通过在腾讯云云服务器（以下简称 CVM）上安装 Discuz! 镜像来启动并运行一个论坛网站。您将了解如何配置并启动 CVM 云服务器实例，如何获取 Discuz! 用户名和密码，以及如何登录 Discuz! 管理页面。


## 技能要求
腾讯云市场中提供了 Discuz! 镜像，如果您不熟悉 Linux 命令的使用，建议您通过镜像部署 Discuz! 论坛。如果您对 Linux 的使用比较熟悉，并且对业务网站有较高的扩展性需求，您也可以 [手动搭建 Discuz! 论坛](https://cloud.tencent.com/document/product/213/8043)。


## 操作步骤

### 步骤1：创建云服务器使用 Discuz! 镜像



<dx-alert infotype="notice" title="">
如果您想使用已购买的云服务器部署 Discuz!，您可通过 [重装系统](https://cloud.tencent.com/document/product/213/4933)，并选择服务市场中对应的镜像完成环境部署。部分境外地域的云服务器暂不支持通过服务市场重装系统，建议您 [手动搭建 Discuz! 论坛](https://cloud.tencent.com/document/product/213/8043) 或者使用其他地域云服务器进行搭建。
</dx-alert>


1. 登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)，单击实例管理页面的**新建**。
2. 根据页面提示选择机型，并在 “镜像” 中单击**镜像市场**，**从镜像市场选择**。如下图所示：
<dx-alert infotype="notice" title="">
 部分境外地域暂不支持通过镜像市场创建云服务器，若您选择的地域下没有**镜像市场**，请选择其他支持镜像市场的地域。
</dx-alert>
<img src="https://qcloudimg.tencent-cloud.cn/raw/01b281841885cc44f2e9e2da139a68b2.png"/>
3. 在弹出的**镜像市场**对话框中，选择**全部**，输入 **discuz** 并单击 <img src="https://main.qcloudimg.com/raw/70c20e0ff30f88eef20d6b540d6ef804.png" style="margin:-3px 0px">。
4. 按需选择镜像，本文以选择 **Discuz! X-lighthouse 镜像v2.0** 为例，单击**免费使用**。如下图所示：
<dx-alert infotype="explain" title="">
单击镜像名可查看镜像详情。
</dx-alert>
<img src="https://qcloudimg.tencent-cloud.cn/raw/429bd22bdb1091c8fcaf1d44e07699dc.png" style="width:718px"/>
5. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成云服务器的创建。

### 步骤2：安装并启动 Discuz! 论坛
1. 在实例的管理页面，找到运行中的云服务器实例，并复制该云服务器实例的**公网 IP**。如下图所示：
例如，需启动实例的公网 IP 为193.xxx.xxx.136，则只需复制该实例的公网 IP 即可。
![](https://qcloudimg.tencent-cloud.cn/raw/5b07e76b65a60e6990d177f40af229d5.png)
2. 在本地浏览器中访问**公网 IP**，进入Discuz！安装页面。
3. 单击**我同意**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/c25233ad2accabd42b8e814765820f03.png)
4. 在检查安装环境页面，确认当前状态正常，单击**下一步**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/ecd2b765193fcde3a24b473d0c8e19f2.png)
5. 在设置运行环境页面，选择全新安装，单击**下一步**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/68af477dd0b07078a850c8ec8151597e.png)
6. 在创建数据库页面，根据页面提示和实际需求，填写数据库用户名、密码及管理员密码。如下图所示：
<dx-alert infotype="notice" title="">
请记录或保存本页面的数据库信息及管理员信息。
</dx-alert>
<img src="https://qcloudimg.tencent-cloud.cn/raw/8a952e01a70ce950c288513f2013c271.png"/>
<br>主要信息如下：
<ul>
<li><b>数据库用户名</b>：填写 `discuz`。</li>
<li><b>数据库密码</b>：为您的实例 ID，可前往 <a href="https://console.cloud.tencent.com/cvm/instance">云服务器控制台</a> 获取。</li>
<li><b>管理员密码</b>：自定义管理员密码。</li>
<li><b>重复密码</b>：重复输入设置密码。</li>
</ul>
7. 单击**下一步**，开始安装。
8. 安装完成后，单击**您的论坛已完成安装，点此访问**，即可访问论坛。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/c61e31f0a88ffedf53696b0f9cb9ca70.png)


## 常见问题
如果您在搭建 Discuz! 论坛的过程中遇到问题，可参考以下文档进行分析并解决问题：
- 云服务器的登录问题，可参考 [密码及密钥](https://cloud.tencent.com/document/product/213/18120)、[登录及远程连接](https://cloud.tencent.com/document/product/213/17278)。
- 云服务器的网络问题，可参考 [IP 地址](https://cloud.tencent.com/document/product/213/17285)、[端口与安全组](https://cloud.tencent.com/document/product/213/2502)。


