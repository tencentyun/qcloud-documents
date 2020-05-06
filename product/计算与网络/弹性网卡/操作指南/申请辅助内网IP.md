如需实现单网卡多 IP，您可为弹性网卡申请辅助内网 IP，操作如下：
## 步骤一：分配辅助内网 IP
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 单击左侧目录中的【IP 与网卡】>【弹性网卡】，进入弹性网卡列表页。
3. 单击需要申请辅助内网 IP 的实例 ID，进入详情页。
4. 单击选项卡中的【IPv4 地址管理】，查看内网 IP 信息。
![](https://main.qcloudimg.com/raw/c360781a44e6a7f976c5fd3bf0b87bd0.png)
5. 单击【分配内网 IP】，在弹出框中选择自动分配，或手动填写要分配的内网 IP 地址，单击【确定】即可。
>?如果您选择手动填写，请确认填写内网 IP 在所属子网网段内，且不属于系统保留 IP。
>例如，所属子网网段为：`10.0.0.0/24`，则可填的内网 IP 范围 为：`10.0.0.2 - 10.0.0.254`。
>
![](https://main.qcloudimg.com/raw/1c9e2d055fb464d22559bf7e1d922a64.png)

## 步骤二：配置辅助内网 IP
登录上述弹性网卡绑定的云服务器，配置辅助内网 IP 使其生效，可参考如下操作：
### Linux 云服务器
1. 在云服务器中执行如下命令配置辅助内网 IP：
```
# 如 ip addr add 10.0.0.2/24 dev eth0
ip addr add 辅助内网IP/CIDR位数 dev eth0
```
2. 执行 `ip addr` 命令，即可查看已配置的 IP 信息，如下图所示。
![](https://main.qcloudimg.com/raw/98b7e2e0d683644e9694390c4b0ef733.png)

### Windows 云服务器
1. <span id="step1" />执行如下步骤，查看云服务器的 IP 地址、子网掩码和默认网关和 DNS 服务器：
 1. 在操作系统界面，选择左下角的<img src="https://main.qcloudimg.com/raw/87d894e564b7e837d9f478298cf2e292.png" style="margin:-3px 0px;width:25px">，单击 <img src="https://main.qcloudimg.com/raw/f0c84862ef30956c201c3e7c85a26eec.png" style="margin: -3px 0px;">，打开 “Windows PowerShell” 窗口，执行如下命令：
```
ipconfig /all
```
 2. 记录输出的网络接口信息中的 IPv4 地址、子网掩码、默认网关和 DNS 服务器值。
![](https://main.qcloudimg.com/raw/1a4a6f0557ff809a27607fee24549eb3.png)
2. 进入操作系统的【控制面板】>【网络和 Internet】>【网络和共享中心】，单击命名为“以太网”的网卡进行编辑。
![](https://main.qcloudimg.com/raw/56b44bec57750b8e86a9c7f7aba40041.png)
3. 在“以太网状态”弹窗中，单击【属性】。
4. 在“以太网属性”弹窗中，选中【Internet 协议版本4（TCP/IPv4）】并单击【属性】。
![](https://main.qcloudimg.com/raw/b224af9ef0d18ca24f8e799f9c5023df.png)
5. 在 “Internet 协议版本4（TCP/IPv4）属性”弹窗中，填写如下信息：
<table>
<thead>
<tr>
<th>参数名</th>
<th>参数值</th>
</tr>
</thead>
<tbody><tr>
<td>IP 地址</td>
<td>上述 <a href="#step1">步骤1</a> 中的 IPv4 地址。</td>
</tr>
<tr>
<td>子网掩码</td>
<td>上述 <a href="#step1">步骤1</a> 中的子网掩码。</td>
</tr>
<tr>
<td>默认网关</td>
<td>上述 <a href="#step1">步骤1</a> 中的默认网关地址。</td>
</tr>
<tr>
<td>首选 DNS 服务器</td>
<td>上述 <a href="#step1">步骤1</a> 中的 DNS 服务器。</td>
</tr>
<tr>
<td>备用 DNS 服务器</td>
<td>上述 <a href="#step1">步骤1</a> 中的备用 DNS 服务器。如果未列出备用 DNS 服务器，则无需填写此参数。</td>
</tr>
</tbody></table>
<img src="https://main.qcloudimg.com/raw/26fca0d8901235e7be62234c3e684e17.png" />
6. 单击【高级】，配置辅助内网 IP。
7. 在“高级 TCP/IP 设置”弹窗中的 “IP 地址”模块下，单击【添加】。
8. 在 “TCP/IP 地址”弹窗中，填写辅助内网 IP，上述 [步骤1](#step1) 中的子网掩码，单击【添加】，如下图所示。 
![](https://main.qcloudimg.com/raw/1fdcb2fa24e45057c5874dfbb20652bc.png)
9. 在 “Internet 协议版本4（TCP/IPv4）属性”弹窗中，单击【确定】。
10. 在“以太网属性”弹窗中，单击【确定】即可完成配置。
11. 在“以太网状态”弹窗中，单击【详细信息】，可查看已配置的 IP 信息，如下图所示。
![](https://main.qcloudimg.com/raw/172cb1189fe0886d6b0b6483a924f8cd.png)
		
