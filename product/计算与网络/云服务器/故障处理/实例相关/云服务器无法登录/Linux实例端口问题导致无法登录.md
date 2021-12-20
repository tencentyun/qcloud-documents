本文档介绍云服务器因端口问题导致无法远程登录的排查方法和解决方案。


<dx-alert infotype="explain" title="">
以下操作以 CentOS 7.8 系统的云服务器为例。
</dx-alert>



## 检查工具
您可以通过腾讯云提供的以下工具判断无法登录是否与端口和安全组设置相关：
- [自助诊断](https://console.cloud.tencent.com/workorder/check)
- [实例端口验通工具](https://console.cloud.tencent.com/vpc/helper)

如果检测为安全组设置的问题，您可以通过 [实例端口验通工具](https://console.cloud.tencent.com/vpc/helper) 中的**一键放通**功能放通相关端口并再次尝试登录。如果放通端口后还是登录失败，可参考以下内容逐步排查原因。

## 排查思路
### 检查网络连通性
您可以通过本地 Ping 命令，测试网络的连通性。同时使用不同网络环境中（不同网段或不同运营商）的电脑测试，判断是本地网络问题还是服务器端问题。
1. 根据本地计算机的操作系统不同，选择命令行工具的打开方式。
	- **Windows 系统**：单击**开始** > **运行**，输入 cmd，弹出命令行对话框。
	- **Mac OS 系统**：打开 Terminal 工具。
2. 执行以下命令，测试网络连接。
```
ping + 云服务器实例公网 IP 地址
```
可参考 [获取公网 IP 地址](https://cloud.tencent.com/document/product/213/17940) 获取云服务器实例公网 IP。例如，执行 `ping 139.199.XXX.XXX`。
 - 如果网络正常，则返回类似以下结果。
![](https://mc.qcloudimg.com/static/img/9596963f31d642deb9417e0a7c0a4085/image.png)
 - 如果网络异常，则出现**请求超时**提示，请参考 [实例 IP 地址 Ping 不通](https://cloud.tencent.com/document/product/213/14639) 进行排查。

### 检查实例端口连通性
1. 使用 VNC 方式登录云服务器，详情请参见 [使用 VNC 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35701)。
2. 执行以下命令，并按 **Enter**。测试远程端口开启情况，判断端口是否可以访问。
```
telnet + 云服务器实例公网 IP 地址 + 端口号
```
例如，执行 `telnet 119.XX.XXX.67 22`命令，测试22端口的连通性。
 - 正常情况：返回如下图所示信息，22端口可访问。
![](https://main.qcloudimg.com/raw/246134de6829323457dc1d51f85589b8.png)
 - 异常情况：返回类似如下图所示信息，说明22端口不可访问。请检查问题网络相应部分，例如实例的防火墙或安全组是否放通22端口。
 ![](https://main.qcloudimg.com/raw/d6eadfe7638046f0b0c1f15261ea74ab.png)
 

### 检查 sshd 服务
当 [使用 SSH 登录 Linux 实例](https://cloud.tencent.com/document/product/213/35700) 时，提示无法连接或者连接失败。可能是由于 sshd 端口未被监听或 sshd 服务未启动引起。请参考 [无法通过 SSH 方式登录 Linux 实例](https://cloud.tencent.com/document/product/213/37925) 进行排查。
