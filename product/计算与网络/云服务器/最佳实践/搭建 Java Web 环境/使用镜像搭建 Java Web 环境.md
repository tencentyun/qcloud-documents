## 操作场景
本文档介绍在 Linux 操作系统的腾讯云云服务器（CVM）上使用镜像搭建 Java Web 环境。

## 前提条件
已登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index)。

## 操作步骤
### 创建云服务器
>!此步骤针对全新购买云服务器。如果您已购买云服务器实例，可通过 [重装系统](https://cloud.tencent.com/document/product/213/4933) 选择对应的操作系统。
>
1. 在实例的管理页面，单击【新建】。
2. 根据页面提示选择机型，并选择【镜像市场】>【从镜像市场选择】。如下图所示：
弹出“选择镜像”窗口。
![](https://main.qcloudimg.com/raw/bd6bbe11ae49f5a398612d495422086f.png)
3. 在“选择镜像”窗口的左侧搜索框中，输入 Java 并单击<img src="https://main.qcloudimg.com/raw/124eb3377f07070061fa6cd419f49abf.png" style="margin:-3px 0;">。如下图所示：
>?
> - 本文以下图所示 Java 多版本运行环境系统镜像为例，您可根据实际需求进行选择。
> - 单击镜像名可查看镜像详情。
> 
![](https://main.qcloudimg.com/raw/36bf7e7e662d6266c0e19354dbf50f0c.png)
4. 单击【免费使用】。
5. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成 CVM 的购买。


### 环境配置验证
>?
> - 云服务器实例状态处于运行中时，即可进行测试。
> - 搭建 Java Web 环境的系统镜像不同，验证步骤会有一定区别，请您根据实际情况进行调试。
> 
1. 在实例的管理页面，找到待验证的云服务器实例，并记录该云服务器实例的公网 IP。如下图所示：
![](https://main.qcloudimg.com/raw/aeff0a3a2401527d488fb582cb121e2b.png)
2. 在浏览器中访问如下地址，查看环境配置是否成功。
```
http://云服务器实例的公网 IP:8080
```
页面显示如下，则说明环境配置成功。
![](https://main.qcloudimg.com/raw/24704c2300f4ba98a9942fdf600287e2.png)
