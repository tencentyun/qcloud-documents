如需实现单网卡多 IP，您可为弹性网卡申请辅助内网 IP，操作如下：
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。
2. 单击左侧目录中的【IP 与网卡】>【弹性网卡】，进入弹性网卡列表页。
![](https://main.qcloudimg.com/raw/4075af8d7e9655ab5306e5152e1a79ce.png)
3. 单击需要申请辅助内网 IP 的实例 ID，进入详情页。
4. 单击选项卡中的【IPv4 地址管理】，查看已绑定的内网 IP 和弹性公网 IP。
![](https://main.qcloudimg.com/raw/c360781a44e6a7f976c5fd3bf0b87bd0.png)
5. 单击【分配内网 IP】，在弹出框中选择自动分配，或手动填写要分配的内网 IP 地址。
>?如果您选择手动填写，请确认填写内网 IP 在所属子网网段内，且不属于系统保留 IP。
>例如，所属子网网段为：`10.0.0.0/24`，则可填的内网 IP 范围 为：`10.0.0.2 - 10.0.0.254`。
>
![](https://main.qcloudimg.com/raw/ca59f63d94bf1d6694e69373b35fce9f.png)
