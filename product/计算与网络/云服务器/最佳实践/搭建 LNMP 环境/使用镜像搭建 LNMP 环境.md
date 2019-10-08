## 操作场景
LNMP 环境代表 Linux 系统下 Nginx + MySQL + PHP 网站服务器架构。本文档介绍如何在 Linux 操作系统的腾讯云云服务器（CVM） 上通过镜像完成 LNMP 环境搭建。

## 前提条件
已登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。

## 操作步骤
### 创建云服务器
>!此步骤针对全新购买云服务器。如果您已购买云服务器，请跳过此步骤，并通过 [更换系统镜像](#change) 搭建 LNMP 环境。
>
1. 在实例的管理页面，单击【新建】。
2. 根据页面提示选择机型，并选择【镜像市场】>【从镜像市场选择】。如下图所示：
 ![](https://main.qcloudimg.com/raw/bd6bbe11ae49f5a398612d495422086f.png)
3. 在弹出的“选择镜像”窗口中，在左侧搜索框中输入 LNMP 并单击<img src="https://main.qcloudimg.com/raw/124eb3377f07070061fa6cd419f49abf.png" style="margin:-3px 0px">。如下图所示：
>?
>-  本文以下图所示 LNMP 环境系统镜像为例，您可根据实际需求进行选择。
>- 单击镜像名可查看镜像详情。
>
![](https://main.qcloudimg.com/raw/3dcee56060fdabbdc3b92d01f6480df9.png)
根据您的实际需求选择镜像，单击【免费使用】。
4. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成 CVM 的购买。

<span id="change"></span>
### 更换系统镜像
1. 本文通过重装系统来更换系统镜像，请参考 [重装系统](https://cloud.tencent.com/document/product/213/4933) 了解注意事项。
2. 在需要安装 LNMP 环境的实例行中，选择【更多】>【重装系统】。如下图所示：
![](https://main.qcloudimg.com/raw/5511e072094665f9cad318f777907c96.png)
3. 在弹出的“重装系统”窗口中，选择【服务市场】，在下拉列表的搜索框中输入 LNMP。如下图所示：
![](https://main.qcloudimg.com/raw/9ba4d5292e9ab5e1b2789ef171cf09fc.png)
4. 根据您的实际需求选择镜像，可同时调整磁盘大小，确认配置后单击【开始重装】。

### 环境配置验证
>!
>- 云服务器实例状态处于运行中时，即可进行测试。
>- 系统镜像不同，验证步骤会有一定区别，请您根据实际情况进行调试。
>
1. 在实例的管理页面，找到待启动的云服务器实例，并记录该云服务器实例的公网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/aeff0a3a2401527d488fb582cb121e2b.png)
2. 在浏览器中访问如下地址，查看环境配置是否成功。
```
http://云服务器实例的公网 IP/phpinfo.php
```
页面显示如下，则说明环境配置成功。
![](https://main.qcloudimg.com/raw/fc3d72b5c5522cd942dfceab7ca8bc8a.png)
