
您可以在控制台中直接修改私有网络中 CVM 实例的内网IP，也可以通过更换 CVM 实例所属的子网来更改实例的内网IP。关于更换子网的操作，请参考[更换子网]()。

## 限制条件

- 修改主网卡的主 IP 会导致关联的云主机自动重启。
- 辅助网卡无法修改主 IP 。

## 操作步骤

- 登录[云主机控制台](https://console.cloud.tencent.com/cvm/index)。
- 选择地域。
- 找到需要查看详情的实例，单击实例ID，进入实例详情页面。
- 在实例详情页，点击【弹性网卡】-【修改主IP】。
![](https://main.qcloudimg.com/raw/8ed95250a179ea85b003df79178087a9.png)
- 在弹出来的修改主 IP 页面输入新的IP，然后点击【确定】，然后等待实例重启完毕即可生效。
![](https://main.qcloudimg.com/raw/a1828fa41fbed3efabd78636f435188a.png)
>注意：只能填入属于当前子网CIDR的内网IP。