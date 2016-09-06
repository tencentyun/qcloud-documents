在启动了Linux类型的实例后，您可以连接并登录它。根据您本地的操作系统和 CVM 实例是否可被 Internet 访问，不同情况下可以使用不同的登录方式，具体内容可参考下表：
<table><tbody>
<tr><th>本地操作系统类型</th><th> Linux 云服务器实例有公网 IP</th><th> Linux 云服务器实例没有公网 IP</th></tr>
<tr><td>Windows</td><td>VNC 登录<br>PUTTY登录<br>密钥登录</td><td rowspan="3">VNC登录</td></tr>
<tr><td>Linux</td><td>VNC 登录<br>SSH 登录<br>密钥登录</td></tr>
<tr><td>Mac OS</td><td>VNC 登录<br>SSH 登录<br>密钥登录</td></tr>
</tbody></table>

## 先决条件
使用密码登录到云服务器时，需要使用管理员帐号和对应的密码；使用密钥登录到云服务器时需要创建并下载私钥。

### 使用 PUTTY 和 SSH 登录的先决条件
- 管理员账号：对于不同类型的Linux实例，管理员帐号不同，如下表。

|实例操作系统 |管理员帐号|
|--|--|
|SUSE/CentOS/Debian| root|
|Ubuntu|ubuntu|

- 密码：
  - 若用户在启动实例时选择【自动生成密码】，则初始密码由系统随机分配。您可以登录[腾讯云控制台](https://console.qcloud.com/)，点击右侧站内信按钮，查收新购买的服务器页面中将包含云主机登录管理员帐号及初始密码，如下图所示。
  ![](//mccdn.qcloud.com/img56a20f10a373a.png)
  - 若用户在启动实例时选择了自定义密码，则密码为用户在购买云服务器实例时指定的密码。有关密码的更多内容，如忘记登录密码怎么办，请参考[登录密码]()。

### 使用密钥登录的先决条件

需要使用 SSH 密钥登录，您首先创建SSH密钥、下载私钥并绑定到Linux云服务器上。有关密钥的更多内容，请参阅 [安全登录]()。
![](//mccdn.qcloud.com/img56a5d553bddcf.png)

登录[腾讯云控制台](https://console.qcloud.com)，点击【云服务器】-【SSH密钥】进入密钥窗口。点击【创建密钥】按钮，输入密钥名创建一个新密钥。创建完密钥后，点击【下载】按钮，下载私钥。

然后右键选择刚创建的密钥ID，选择绑定需要登录的 Linux 服务器进行绑定。

## 本地为Windows时：使用远程登录软件登录Linux实例

本地Windows计算机可以使用一些远程登录软件登录远程Linux实例，本例中选择使用 PUTTY，用户也可以选择其他类型的登录软件。
### 安装Windows远程登录软件
从本地Windows机器登录到Linux云服务器时，需要使用客户端软件建立连接。这里使用PUTTY为例，参考下载地址：http://www.putty.nl/download.html

### 使用Putty连接Linux云服务器
打开Putty客户端，在PuTTY Configuration 窗口中输入以下内容：
- Host Name：云服务器的公网IP（登录[腾讯云控制台云服务器页面](https://console.qcloud.com/cvm)，可在列表页及详情页中获取主机公网IP）。
- Port：云服务器的端口，必须填22。（请确保云主机22端口已开放，详见查看[安全组](http://www.qcloud.com/doc/product/213/%E5%AE%89%E5%85%A8%E7%BB%84%E6%93%8D%E4%BD%9C%E6%8C%87%E5%8D%97)及网络ACL）
- Connect type：选择“SSH”。

全部输入完后，点击“Open”，创建一个新对话。
![](//mccdn.qcloud.com/img56a5d38a4ffbc.png)

在Putty会话窗口中，输入[先决条件]()中获得的管理员帐号，按回车键。再输入[先决条件]()中获取的登录密码，回车完成登录过程。
![](//mccdn.qcloud.com/img56a5d47b8b5da.png)

## 本地为Linux时：使用SSH登录Linux实例
