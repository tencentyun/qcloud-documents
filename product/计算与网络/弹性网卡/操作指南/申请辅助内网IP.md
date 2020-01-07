如需实现单网卡多 IP，您可为弹性网卡申请辅助内网 IP，操作如下：
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 单击左侧目录中的【IP 与网卡】>【弹性网卡】，进入弹性网卡列表页。
3. 单击需要申请辅助内网 IP 的实例 ID，进入详情页。
4. 单击选项卡中的【IPv4 地址管理】，查看已绑定的内网 IP 和弹性公网 IP。
![](https://main.qcloudimg.com/raw/389bb0d1260164ea9e9330077de42e30.png)
5. 单击【分配内网 IP】，在弹出框中选择自动分配，或手动填写要分配的内网 IP 地址。
>?如果您选择手动填写，请确认填写内网 IP 在所属子网网段内，且不属于系统保留 IP。
>例如，所属子网网段为：`10.0.0.0/24`，则可填的内网 IP 范围 为：`10.0.0.2 - 10.0.0.254`。
>
![](https://main.qcloudimg.com/raw/1c9e2d055fb464d22559bf7e1d922a64.png)
6. 登录上述弹性网卡绑定的云服务器，配置辅助内网 IP 使其生效，可参考如下操作：
 - **Linux 云服务器**
    1. 在云服务器中执行如下命令配置辅助内网 IP：
```
# 如 ip addr add 10.0.0.2/24 dev eth0
ip addr add 内网IP/CIDR位数 dev eth0
```
     2. 执行 `ip addr` 命令，即可查看已配置的 IP 信息，如下图所示。
![](https://main.qcloudimg.com/raw/98b7e2e0d683644e9694390c4b0ef733.png)
 - **Windows 云服务器**
    1. 进入操作系统的【控制面板】>【网络和 Internet】>【网络和共享中心】，单击命名为“以太网”的网卡进行编辑。
    ![](https://main.qcloudimg.com/raw/56b44bec57750b8e86a9c7f7aba40041.png)
		2. 在“以太网状态”弹窗中，单击【属性】。
		3. 在“以太网属性”弹窗中，选中【Internet 协议版本4（TCP/IPv4）】并单击【属性】。
    ![](https://main.qcloudimg.com/raw/b224af9ef0d18ca24f8e799f9c5023df.png)
		4. 在 “Internet 协议版本4（TCP/IPv4）属性”弹窗中，配置主内网 IP，填写实际的主内网 IP 地址、子网掩码、网关和 DNS 地址，如下图所示。
		>?
		>- 在输入完主内网 IP 地址后，单击“子网掩码”输入框会自动填充，无需手动输入。
		>- 网关为子网网段的首个 IP，如子网网段为：`10.0.0.0/24`，则网关为：`10.0.0.1`。
		>- DNS 地址可参见 [内网 DNS](https://cloud.tencent.com/document/product/213/5225#.E5.86.85.E7.BD.91-dns)。
		>
    ![](https://main.qcloudimg.com/raw/4eabd315ff7c23f564ef4ac191c3d0ae.png)
		5. 单击【高级】，配置辅助内网 IP。
		6. 在“高级 TCP/IP 设置”弹窗中的 “IP 地址”模块下，单击【添加】。
		7. 在 “TCP/IP 地址”弹窗中，填写辅助内网 IP，子网掩码，单击【确定】，如下图所示。 
    ![](https://main.qcloudimg.com/raw/c6a9b7c0145eb1cd2372066408d78844.png)
		8. 在 “Internet 协议版本4（TCP/IPv4）属性”弹窗中，单击【确定】。
		9. 在“以太网属性”弹窗中，单击【确定】即可完成配置。
		10. 在“以太网状态”弹窗中，单击【详细信息】，可查看已配置的 IP 信息，如下图所示。
		![](https://main.qcloudimg.com/raw/911924933205e901ed8b852a5240cfef.png)
		
 
