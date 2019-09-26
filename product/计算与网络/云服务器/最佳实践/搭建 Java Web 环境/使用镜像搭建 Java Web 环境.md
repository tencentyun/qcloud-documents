## 操作场景
本文档介绍在 Linux 操作系统的腾讯云云服务器（CVM）上使用镜像搭建 Java Web 环境。

## 前提条件
已登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。

## 操作步骤
### 创建云服务器
>!此步骤针对全新购买云服务器。如果您已购买云服务器，请跳过此步骤，并通过 [更换系统镜像](#change) 搭建 Java Web 环境。
>
1. 在实例的管理页面，单击【新建】。
2. 根据页面提示选择机型，并在 “镜像” 中单击【镜像市场】，选择【从镜像市场选择】。如下图所示：
![](https://main.qcloudimg.com/raw/bd6bbe11ae49f5a398612d495422086f.png)
3. 在弹出的【选择镜像】对话框中，在左侧搜索框中输入 Java 并单击<img src="https://main.qcloudimg.com/raw/124eb3377f07070061fa6cd419f49abf.png" style="margin:-3px 0;">。如下图所示：
>?
> - 本文以下图所示 Java 多版本运行环境系统镜像为例，您可根据实际需求进行选择。
> - 单击镜像名可查看镜像详情。
> 
![](https://main.qcloudimg.com/raw/36bf7e7e662d6266c0e19354dbf50f0c.png)
选定镜像后，单击【免费使用】。
4. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成 CVM 的购买。


<span id="change"></span>
### 更换系统镜像
1. 本文通过重装系统来更换系统镜像，请参考 [重装系统](https://cloud.tencent.com/document/product/213/4933) 了解注意事项。
2. 在需要安装 Java Web 环境的实例行中，单击【更多】>【重装系统】。如下图所示：
![](https://main.qcloudimg.com/raw/5511e072094665f9cad318f777907c96.png)
3. 在弹出的“重装系统”窗口中，选择【服务市场】，在下拉列表的搜索框中输入 java。如下图所示：
>?本文使用如下系统镜像，您可根据实际需求进行选择。
>
![](https://main.qcloudimg.com/raw/27cf8d3cc8177f196c5cda0df134a4b6.png)
4. 根据您的实际需求选择镜像，可同时调整磁盘大小，确认配置后单击【开始重装】。

### 环境配置验证
>?
> - 云服务器实例状态处于运行中时，即可进行测试。
> - 系统镜像不同，测试步骤会有一定去区别，请您根据实际情况进行调试。
> 
1. 在实例的管理页面，找到待启动的云服务器实例，并记录该云服务器实例的公网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/aeff0a3a2401527d488fb582cb121e2b.png)
2. 在浏览器中访问如下地址，查看环境配置是否成功。
```
http://云服务器实例的公网 IP:8080
```
页面显示如下，则说明环境配置成功。
![](https://main.qcloudimg.com/raw/24704c2300f4ba98a9942fdf600287e2.png)
