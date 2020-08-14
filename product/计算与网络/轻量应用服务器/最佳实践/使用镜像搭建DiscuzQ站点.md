## 操作场景
Discuz! Q 是全球成熟度最高、覆盖率最大的社区论坛软件系统之一。腾讯云轻量应用服务器 Lighthouse 提供 Discuz! Q 应用镜像，其中已集成宝塔 Linux 面板、MySQL、Nginx 和 PHP 软件，您可以使用它构建移动端社区。
>?Discuz! Q 应用镜像底层基于 CentOS 7.6 64位操作系统。实例创建完成后将会自动下载并安装最新版的 Discuz! Q 软件。


## 操作步骤
1. 登录 [轻量应用服务器控制台](https://console.cloud.tencent.com/lighthouse)。
2. 单击【新建】，进入轻量应用服务器购买页面。如下图所示：
![](https://main.qcloudimg.com/raw/f279bcd90f120c2b511655591ae4cc7b.png)
	- **地域**：建议选择靠近目标客户的地域，降低网络延迟、提高您的客户的访问速度。例如目标客户在 “深圳”，地域选择 “广州”。
	- **镜像**：选择 “Discuz! Q v1.0” 应用镜像。
	- **实例套餐**：按照所需的服务器配置（CPU、内存、系统盘、峰值带宽、每月流量），选择一种实例套餐。
	- **实例名称**：自定义实例名称，若不填则默认使用所选镜像名称。批量创建实例时，连续命名后缀数字自动升序。例如，填入名称为 LH，数量选择3，则创建的3个实例名称为 LH1、LH2、LH3。
	- **购买时长**：默认1个月。
	- **购买数量**：默认1台。
3. 单击【立即购买】，并根据页面提示提交订单完成支付，返回轻量应用服务器控制台。
4. 待实例创建完成后，在服务器列表中，选择并进入该实例的详情页。
您可以在此页面查看 Discuz! Q 应用的各项配置信息。
5. 选择【应用管理】页签，进入应用管理详情页。
6. <span id="Step6"></span>在“应用内软件信息”栏中，单击<img src="https://main.qcloudimg.com/raw/6603ab4f907562addb1c01596c6296cd.png">，复制获取 Discuz! Q 的管理员帐户密码的命令。
7. 在“应用内软件信息”栏中，单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/f98e022191f1fcb49698fa2db2f519ff.png)
8. <span id="Step8"></span>在弹出的登录窗口中，粘贴 [步骤6](#Step6) 复制的管理员密码，按 **Enter**。
如下图所示即可获取 Discuz! Q 管理员账号（admin）和对应的密码，请妥善保管并记录。
![](https://main.qcloudimg.com/raw/1a809d9ca378835675299e37a1c9cebd.png)
9. 关闭登录窗口，并返回该实例的应用管理详情页。
10. 在“应用内软件信息”栏中，单击 Discuz! Q 的【后台访问地址】。如下图所示：
![](https://main.qcloudimg.com/raw/bd7302b9dd9f100dbab7a2d87aa41345.png)
11. 在新打开的浏览器窗口中，输入 [步骤8](#Step8) 记录的账号和密码，单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/01192dbc6dd0522e873c5c93241f17af.png)
即可根据实际需要，对 Discuz! Q 进行管理、自定义和配置。

## 相关操作
### 修改管理员账号密码
您可参考以下步骤，修改 Discuz! Q 管理员账号（admin）的密码：
1. 在“应用内软件信息”栏中，单击 Discuz! Q 的【前台访问地址】。
2. 在新打开的浏览器窗口中，选择底部菜单栏中的<img src="https://main.qcloudimg.com/raw/30f96457f5daeed05440989ab41e9405.png" style="margin:-3px 0">。
3. 进入 Discuz! Q 登录页面，输入 [步骤8](#Step8) 记录的账号和密码，单击【登录】。如下图所示：
![](https://main.qcloudimg.com/raw/1be6cea0343be72db7bc5f663c9852c8.png)
4. 成功登录后，选择底部菜单栏中的<img src="https://main.qcloudimg.com/raw/30f96457f5daeed05440989ab41e9405.png" style="margin:-3px 0">，进入个人信息页面。
5. 在个人信息页面中，选择【我的资料】并单击密码所在行右侧的【修改>】。如下图所示：
![](https://main.qcloudimg.com/raw/e0ba02f7810264e29f5d9900b2332f98.png)
6. 在修改密码界面设置新密码后单击【提交】即可完成密码修改。


### 查看其他配置信息
在 Discuz! Q 实例的应用管理详情页，您除了可以查看 Discuz! Q 的配置信息，还可以查看其他配置信息。例如宝塔Linux面板登录信息、 MySQL 数据库管理员密码、实例中各个软件的安装路径等。如下图所示：
![](https://main.qcloudimg.com/raw/46dfb1a9fdbbc8191e697744b8a04103.png)

### 安装 SSL 证书
您可通过以下方式，为您的实例安装 SSL 证书：
- 方式1：Discuz! Q 实例创建完成后，使用实例中内置的宝塔 Linux 面板安装 SSL 证书。详情可参考宝塔 Linux 面板官方文档。
- 方式2：可参考 [安装 SSL 证书](https://cloud.tencent.com/document/product/1207/47027) 文档为您的 Discuz! Q 实例安装 SSL 证书并开启 HTTPS 访问。
