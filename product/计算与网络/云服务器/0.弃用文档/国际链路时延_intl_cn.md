## 问题描述
北美地域云服务器登录时延太长。
因全国国际路由出口较少及某些其他原因，并发数大时，国际链路会非常拥塞并导致访问不稳定，对此腾讯云已经向运营商进行反馈。目前，购买了北美地域云服务器的客户若需要在国内进行管理运维。短时间内您可使用在中国香港地域购买云服务器,然后通过中国香港地域 CVM 进行中转登录的方法解决该问题。

![](//mccdn.qcloud.com/static/img/45317b09510d34fc92eb1cf3f0ac9568/image.png)

## 解决办法
 1. 购买中国香港地域的 Windows 云服务器，在自定义配置页中 [选购](https://buy.cloud.tencent.com/cvm?tabIndex=1)，（ Windows 操作系统可以支持登录北美 Windows 和 Linux 这两类云服务器，推荐选购）作为“跳板机”。
	>**注意：**
	>您需要购买至少 1 Mbps 的带宽，否则跳板机无法登录。

 2. 购买成功后，登录中国香港地域的 Windows 云服务器：
[从 Windows 机器登录有公网 IP 的 Windows 云服务器](/doc/product/213/Windows%E6%9C%BA%E5%99%A8%E7%99%BB%E5%BD%95%E6%9C%89%E5%85%AC%E7%BD%91IP%E7%9A%84Windows%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8)
[控制台 VNC 登录 Windows 云服务器](/doc/product/213/%E6%8E%A7%E5%88%B6%E5%8F%B0VNC%E7%99%BB%E5%BD%95Windows%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8)

 3. 在中国香港地域的 Windows 云服务器内，登录您位于北美地域的 CVM ：

	- 登录北美地域的 Linux 云服务器
[从 Windows 机器使用密码登录有公网 IP 的 Linux 云服务器](/doc/product/213/Windows%E6%9C%BA%E5%99%A8%E4%BD%BF%E7%94%A8%E5%AF%86%E7%A0%81%E7%99%BB%E5%BD%95%E6%9C%89%E5%85%AC%E7%BD%91IP%E7%9A%84Linux%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8)
[从 Windows 机器使用密钥登录有公网 IP 的 Linux 云服务器](/doc/product/213/2036)
  - 登录北美地域的 Windows 云服务器 
[从 Windows 机器登录有公网 IP 的 Windows 云服务器](/doc/product/213/Windows%E6%9C%BA%E5%99%A8%E7%99%BB%E5%BD%95%E6%9C%89%E5%85%AC%E7%BD%91IP%E7%9A%84Windows%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8)
[控制台 VNC 登录 Windows 云服务器](/doc/product/213/%E6%8E%A7%E5%88%B6%E5%8F%B0VNC%E7%99%BB%E5%BD%95Windows%E4%BA%91%E6%9C%8D%E5%8A%A1%E5%99%A8)
