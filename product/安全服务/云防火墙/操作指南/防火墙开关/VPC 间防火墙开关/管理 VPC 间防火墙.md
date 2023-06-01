VPC 间防火墙创建完成后，您可以管理 VPC 间防火墙或防火墙实例。


## 查看概况

1. 登录 [云防火墙控制台](https://console.cloud.tencent.com/cfw/switch/vpc)，在左侧导航栏中，选择**防火墙开关** > **VPC 间开关**。
2. 在 VPC 间开关页面，单击**防火墙实例**，进入到防火墙实例页面，可以查看已经创建好的防火墙和其部署的防火墙实例信息。
>?实例规格：当前防火墙实例的带宽上限和下发规则数上限，详情您可以参考 [实例规格](https://cloud.tencent.com/document/product/1132/46929#.E5.AE.9E.E4.BE.8B.E8.A7.84.E6.A0.BC.3Ca-id.3D.22sl.22.3E.3C.2Fa.3E)。
>
![](https://qcloudimg.tencent-cloud.cn/raw/34e29f61c197dd41ca2f92365ccaeefa.jpg)


## 查看关联开关
在防火墙实例页面，单击**开关数量**，跳转至防火墙开关页面，可自动筛选出当前防火墙关联的开关。
![](https://qcloudimg.tencent-cloud.cn/raw/70cd790e159c7c45b63c68138bc70e3e.jpg)

## 配置实例
1. 在防火墙实例页面，鼠标悬浮至需要配置的 VPC 间防火墙右侧的**操作**，选择**配置实例**。
![](https://qcloudimg.tencent-cloud.cn/raw/9ab020aa9382b7df085fd8da43aca09e.jpg)
2. 支持调整创建时的初始配置，包含防火墙实例名称、实例的规格以及每个实例接入的网络实例；也可以新增 VPC 间防火墙实例。
![](https://qcloudimg.tencent-cloud.cn/raw/06898f92da554f4f5b8ab311bd91ecfd.jpg)
3. 如果有新增接入的 VPC，将会自动根据创建 VPC 间防火墙时的网络配置执行；如果选择了自定义创建引流子网方式，还需要手动填写新增 VPC 的子网 CIDR。
>!防火墙网络配置不支持修改。
>
![](https://qcloudimg.tencent-cloud.cn/raw/83f1cb0197ae4d4d39641c10a0e18c85.jpg)

## 销毁 VPC 间防火墙
在防火墙实例页面，鼠标悬浮至需要配置的 VPC 间防火墙右侧的**操作**，选择**销毁防火墙**，二次确认后即可。
>!若您选择了自定义路由请确认已手动恢复路由。
>
![](https://qcloudimg.tencent-cloud.cn/raw/140c453ca085b6161f9f114bd4170c4d.jpg)
