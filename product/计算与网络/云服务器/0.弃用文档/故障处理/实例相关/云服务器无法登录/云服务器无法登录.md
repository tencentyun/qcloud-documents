
若您无法连接实例，建议按照如下原因进行排查：


<span id = "jump1"></span>
## 端口问题
**故障现象：**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;端口远程连接失败。
 
**解决方法：**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可能由远程访问端口非默认端口或端口设置不一致所致。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;详见 [端口问题导致无法远程连接](https://cloud.tencent.com/document/product/213/10232) 。

<span id = "jump2"></span>
## CPU/内存占用率高问题
**故障现象：**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用云服务器时，出现无法登录、服务速度变慢、实例突然断开情况。
 
**解决方法：**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;可能存在 CPU 或内存荷载过高的问题，检查资源占用情况。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Windows 云服务器详见 [Windows系统CPU与内存占用率高导致无法登录](https://cloud.tencent.com/document/product/213/10233) 。
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Linux 云服务器详见 [Linux系统CPU与内存占用率高导致无法登录](https://cloud.tencent.com/document/product/213/10310) 。

<span id = "jump3"></span>
## 外网被隔离问题
**故障现象：**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;云服务器出现违规事件或风险事件时，被进行部分隔离。
 
**解决方法：**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;详见 [外网被隔离导致无法远程连接](https://cloud.tencent.com/document/product/213/10318) 。

<span id = "jump4"></span>
## 外网带宽占用高问题
**故障现象：**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;带宽跑满或跑高，导致无法登录。
 
**解决方法：**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;详见 [外网带宽占用高导致无法登录](https://cloud.tencent.com/document/product/213/10334) 。

<span id = "jump5"></span>
## 安全组设置问题
**故障现象：**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;服务器 telnet 无法连接，排查防火墙、网卡 IP 配置无误，回滚系统后仍然无法连接。
 
**解决方法：**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;详见 [安全组设置导致无法远程连接](https://cloud.tencent.com/document/product/213/10337) 。

<span id = "jump6"></span>
## 关联密钥后无法使用密码
**故障现象：**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;云服务器关联密钥后，无法使用密码登录，排查防火墙、网卡 IP 配置无误。
 
**解决方法：**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;云服务器关联密钥后，云服务器 SSH 服务默认关闭用户名密码登录，请您使用密钥登录服务器。 
密钥登录方式可参见 [SSH 密钥](https://cloud.tencent.com/document/product/213/5436) 。 

<span id = "jump7"></span>
## 远程登录网络级别身份验证
**故障现象：**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用 Windows 系统自带远程桌面连接，有时出现无法连接到远程计算机的问题。
 
**解决方法：**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;详见 [远程登录网络级别身份验证](https://cloud.tencent.com/document/product/213/11330) 。

<span id = "jump8"></span>
## xshell 无法密码登录
**故障现象：**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;使用 xshell 进行登录时，无法使用密码登录云服务器。
 
**解决方法：**
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;您在安装系统时已选择密钥登录方式，如何使用密钥可参考 [SSH 密钥](/doc/product/213/6092) 如需采用密码方式登录，可重装系统时选择密码登录，或者进入登录计算机修改 sshd 配置文件。

