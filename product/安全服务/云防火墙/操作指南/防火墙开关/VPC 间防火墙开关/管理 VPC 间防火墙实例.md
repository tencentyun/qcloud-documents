VPC 间防火墙创建完成后，您可以单独对 VPC 间防火墙实例进行管理。

1. 登录 [云防火墙控制台](https://console.cloud.tencent.com/cfw/switch/vpc)，在左侧导航栏中，选择**防火墙开关** > **VPC 间开关**。
2. 在 VPC 间开关页面，单击**防火墙实例**，进入到防火墙实例页面。


## 查看实例详情
1 . 在防火墙实例页面，单击**防火墙实例 ID**或单击右侧的**实例详情**。
![](https://qcloudimg.tencent-cloud.cn/raw/631497f94923c7c57faf73e06a926c83.jpg)
2. 在防火墙实例页面，在可以查看实例的相关配置详情。
![](https://qcloudimg.tencent-cloud.cn/raw/027b920d12a82f57ab516b8e421a2689.jpg)


## 查看关联开关
在防火墙实例页面，单击**更多** > **查看防火墙开关**，可以跳转至防火墙开关页面，并自动筛选出当前防火墙实例关联的开关。
![](https://qcloudimg.tencent-cloud.cn/raw/b5ea740d462bb1e7b4f9f37fd658b140.jpg)
>?防火墙实例关联开关取决于开关控制的流量是否会经过这个实例，一个开关可能属于多个实例。


## 销毁 VPC 间防火墙实例

销毁任意防火墙实例，需要关闭当前 VPC 间防火墙的全部开关。

1. 在防火墙实例页面，单击所属 VPC 间防火墙的**开关数量**。
![](https://qcloudimg.tencent-cloud.cn/raw/2575716cb9164ed5d27be56a312e872a.jpg)
2. 跳转至防火墙开关页面，单击**全部关闭**关闭当前防火墙全部开关。
![](https://qcloudimg.tencent-cloud.cn/raw/55b20765726a54f8d0b3123ce138f1f4.jpg)
3. 在防火墙实例页面，单击**更多** > **销毁实例**，二次确认后即会销毁当前防火墙实例。
>?销毁防火墙实例后，当前实例接入的 VPC 将会自动取消接入，已使用配额将归还。
>
![](https://qcloudimg.tencent-cloud.cn/raw/5673f2be8089df7a527de444e79995a8.jpg)


## 重新选择接入实例
重新选择接入实例，需要关闭当前 VPC 间防火墙的全部开关。

1. 在防火墙实例页面，单击所属 VPC 间防火墙的**开关数量**。
![](https://qcloudimg.tencent-cloud.cn/raw/2575716cb9164ed5d27be56a312e872a.jpg)
2. 跳转至防火墙开关页面，单击**全部关闭**关闭当前防火墙全部开关。
![](https://qcloudimg.tencent-cloud.cn/raw/55b20765726a54f8d0b3123ce138f1f4.jpg)
3. 在防火墙开关页面，单击**更多** > **重新选择接入实例**，进入编辑 VPC 间防火墙页面。
>!
>- 当以私有网络模式接入 VPC 间防火墙，支持重新选择接入的 VPC 实例。
>- 云联网模式则接入云联网内的所有 VPC 实例，不支持重新选择。
>
![](https://qcloudimg.tencent-cloud.cn/raw/9b48e99b73cf931f16569c9ef554bada.jpg)
4. 在弹窗中，选择需要重新接入的 VPC，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/f00c052837843616aee27e91c85b427b.jpg)


## ByPass 模式
防火墙支持手动切换至 ByPass 模式，ByPass 模式下当前实例下所有流量均不会过防火墙，所有防火墙配置将失效，**建议在调试时使用**。

在防火墙实例页面，单击**更多** > **开启 ByPass** / **关闭 ByPass**。
>!调试完成请手动关闭 ByPass 模式。
>
![](https://qcloudimg.tencent-cloud.cn/raw/c2b3ad68d954ee622ca3ea9b2cf76174.jpg)

