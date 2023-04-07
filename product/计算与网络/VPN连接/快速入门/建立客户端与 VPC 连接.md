本文为您介绍 Windows、MAC 和 Linux 客户端如何通过 SSL VPN 连接 VPC。

## 背景信息
本文以下图场景为例，为您介绍 Windows、MAC 和 Linux 客户端如何使用 SSL VPN 连接VPC。
![](https://qcloudimg.tencent-cloud.cn/raw/37c49a85bc549c51f1b61af94cb0470b.png)

## 配置流程
客户端通过 SSL VPN 连接 VPC 流程图如下所示：
![](https://qcloudimg.tencent-cloud.cn/raw/b7ee18586c39de9dea92b07ed345672b.png)

## 步骤1：创建 SSL VPN 网关
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击 **VPN 连接** > **VPN 网关**，进入管理页。
3. 在 VPN 网关管理页面，单击**+新建**。
4. 在弹出的新建 VPN 网关对话框中，配置如下网关参数。
<img src="https://qcloudimg.tencent-cloud.cn/raw/1cd66bf3fefeed4f9d201b5d58eac673.png" width="70%"> 
<table>
<tr>
<th>参数名称</th>
<th>参数说明</th>
</tr>
<tr>
<td>网关名称</td>
<td>填写 VPN 网关名称，不超过60个字符。</td>
</tr>
<tr>
<td>所在地域</td>
<td>展示 VPN 网关所在地域。</td>
</tr>
<tr>
<td>可用区</td>
<td>选择当前网关所在的可用区。</td>
</tr>
<tr>
<td>协议类型</td>
<td>选择 SSL。</td>
</tr>
<tr>
<td>带宽上限</td>
<td>请根据业务实际情况，合理设置 VPN 网关带宽上限。</td>
</tr>
<tr>
<td>关联网络</td>
<td>表示您创建私有网络类型的 VPN。</td>
</tr>
<tr>
<td>所属网络</td>
<td>选择 VPN 网关将要关联的具体私有网络。</td>
</tr>
<tr>
<td>SSL 连接数</td>
<td>连接客户端的数量，一个 SSL 客户端仅允许一个用户连接，不支持一个 SSL 客户端连接多个客户。
</td>
</tr>
<tr>
<td>计费方式</td>
<td>SSL VPN 默认为按流量计费。</td>
</tr>
</table>
5. 完成网关参数设置后，单击**创建**。
![](https://qcloudimg.tencent-cloud.cn/raw/412c7cd5c93acbe893a36e02d59ff9dc.png)

## 步骤2：创建 SSL 服务端[](id:step2)
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击 **VPN 连接** > **SSL 服务端**，进入管理页面。
>?一个VPN网关仅支持关联一个SSL 服务端，详情请参见 [使用限制](https://cloud.tencent.com/document/product/554/18982)。
>
3. 在 SSL 服务端管理页面，单击**+新建**。
4. 在弹出的新建 SSL 服务端对话框中，配置如下参数。
<img src="https://qcloudimg.tencent-cloud.cn/raw/7da06337e08966804c1135f3c94e9952.png" width="60%"> 
<table>
<tr>
<th width="15%">参数名称</th>
<th>参数说明</th>
</tr>
<tr>
<td>名称</td>
<td>填写 SSL 服务端名称，不超过60个字符。</td>
</tr>
<tr>
<td>地域</td>
<td>展示 SSL 服务端所在地域。</td>
</tr>
<tr>
<td>VPN 网关</td>
<td>选择创建好的 SSL VPN 网关。</td>
</tr>
<tr>
<td>云端网段</td>
<td>客户移动端访问的云上网段。</td>
</tr>
<tr>
<td>客户端网段</td>
<td>分配给用户移动端进行通信的网段，该网段请勿与腾讯侧 VPC CIDR 冲突，同时也不能与您本地的网段冲突。</td>
</tr>
<tr>
<td>协议</td>
<td>服务端传输协议。</td>
</tr>
<tr>
<td>端口</td>
<td>填写 SSL 服务端用于数据转发的端口。</td>
</tr>
<tr>
<td>认证算法</td>
<td>目前支持 SHA1 和 MD5 两种认证算法。</td>
</tr>
<tr>
<td>加密算法</td>
<td>目前支持 AES-128-CBC、AES-192-CBC 和 AES-256-CBC 加密算法。</td>
</tr>
<tr>
<td>是否压缩</td>
<td>否。</td>
</tr>
</table>
5. 完成网关参数设置后，单击**创建**。
![](https://qcloudimg.tencent-cloud.cn/raw/87db2ba4721774d788ece5334e817d09.png)

## 步骤3：创建 SSL 客户端[](id:step3)
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击 **VPN 连接** > **SSL 客户端**，进入管理页面。
3. 在 SSL 客户端管理页面，单击**+新建**。
4. 在弹出的 SSL 客户端对话框中，配置如下参数。
![](https://qcloudimg.tencent-cloud.cn/raw/348ae4eaa9af64085744a9f4974da7ed.png)
5. 完成 SSL 客户端参数设置后，单击**确定**，当证书状态为可用表示创建完成。
6. 在 SSL 客户端页面，找到已创建的客户端证书，然后在操作列单击**下载配置**。
>?一个 SSL 客户端仅允许一个用户连接，不支持一个 SSL 客户端连接多个客户。
>
![](https://qcloudimg.tencent-cloud.cn/raw/41938c0da569c592f83ef2fe74ecb432.png)

## 步骤4：配置 VPC 内路由
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 在左侧目录中单击路由表，进入管理页面。
3. 在列表中，单击需要修改的路由表 ID，进入详情页，若需新建路由表，可参考 [创建自定义路由表](https://cloud.tencent.com/document/product/215/36682)。
4. 单击**新增路由策略**，在弹出框中，配置路由策略。
![](https://qcloudimg.tencent-cloud.cn/raw/189d4a5e63b367faca0e833bc29e9725.png)
<table>
<tr>
<th>参数名称</th>
<th>参数说明</th>
</tr>
<tr>
<td>目的端</td>
<td>请填写 <a href="#step2">步骤2：创建 SSL 服务端</a> 中创建时配置的客户端网段。</td>
</tr>
<tr>
<td>下一跳类型</td>
<td>选择 VPN 网关。</td>
</tr>
<tr>
<td>下一跳</td>
<td>下一跳选择创建好的具体 SSL VPN 网关实例。</td>
</tr>
</table>

## 步骤5：配置客户端
以下内容为您介绍如何配置 Windows、MAC 及 Linux 客户端。


### Windows 客户端
1. 首先在 OpenVPN 官方下载页面下载并安装 OpenVPN Connect。
![](https://qcloudimg.tencent-cloud.cn/raw/949a9e0031b880397bca986ac8eedfff.png)
2. SSL 客户端安装完成后，选择 “Import Profile” 菜单中的 “FILE” 页面，上传 [步骤3](#step3) 已下载的 SSL 客户端配置文件（.ovpn 格式）。
![](https://qcloudimg.tencent-cloud.cn/raw/f55cc9eebb56b47511a063eb1135556a.png)

### MAC 客户端
1. 首先在 OpenVPN 官方下载页面下载并安装 OpenVPN Connect。 
![](https://qcloudimg.tencent-cloud.cn/raw/d08446a7176b855c0e19a77dd95cfdc3.png)
2. SSL 客户端安装完成后，选择 “Import Profile” 菜单中的 “FILE” 页面，上传 [步骤3](#step3) 已下载的 SSL 客户端配置文件（.ovpn 格式）。
![](https://qcloudimg.tencent-cloud.cn/raw/efade3f1b6290cae59a337e0927fe7c5.png)

### Linux 客户端
1. 打开命令行窗口。
2. 执行以下命令安装 OpenVPN 客户端。
centos 发行版
```
yum install -y openvpn
```
ubuntu 发行版
```
sudo apt-get install openvpn
```
3. 将[ 步骤3 ](#step3)已下载的 SSL 客户端证书解压拷贝至/etc/openvpn/conf/目录。
4. 进入/etc/openvpn/conf/目录，执行以下命令建立 VPN 连接。
```
openvpn --config /etc/openvpn/conf/config.ovpn --daemon
```

## 步骤6：测试连通性
腾讯云侧与用户移动端建立 SSL VPN 连接后，使用 ping 命令检测连通性。
例如：使用 VPC 内的云服务器 ping 客户端网段中的 IP，可以 ping 通表示 VPC 和客户端可以正常通信。
