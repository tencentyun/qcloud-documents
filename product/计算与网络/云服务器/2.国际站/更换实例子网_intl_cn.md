
您可以在控制台中直接更换私有网络中 CVM 实例的所属子网。

## 限制条件

- 更换子网会导致关联的云主机自动重启。
- 辅助网卡无法更换子网 。

## 操作步骤

- 登录[云主机控制台](https://console.cloud.tencent.com/cvm/index)。
- 选择地域。
- 找到需要查看详情的实例，单击实例ID，进入实例详情页面。
- 在实例详情页，点击【弹性网卡】,点击主网卡ID。
![](https://main.qcloudimg.com/raw/06f216d4a3ba31586e26792dc3788a0c.png)
- 进入主网卡详情页面，点击【更换子网】。
![](https://main.qcloudimg.com/raw/9f3196503a29b23668334dd8a0774bc6.png)
- 在弹出来的更换子网页面选择新的子网，并且输入新的主IP，然后点击【确定】，然后等待实例重启完毕即可生效。
![](https://main.qcloudimg.com/raw/4234772c49fb11bc12cd5a35cc4a32c8.png)
>注意：
>
>1. 如果尚未在该可用区建立子网，请先新建子网
>2. 只能填入属于当前子网CIDR的内网IP。