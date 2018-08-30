## 概述
服务迁移是为方便用户迁移入云而研发的，通过服务迁移能将计算机磁盘中的操作系统、应用程序以及应用数据等迁移到腾讯云云服务器或云硬盘的便捷迁入工具，包含离线迁移、在线迁移等。其中离线迁移包括离线实例迁入和离线数据迁入。

## 操作指南
### 迁移前提
1. 在您使用本功能前，请确保您已经开通了服务迁移权限，若您需要开通权限，请联系商务经理，并提交相关信息至工单系统申请。
2. 离线迁移需要腾讯云对象存储（COS）的支持，获取目前 COS 支持的地域可参考 [COS 可用地域](https://cloud.tencent.com/document/product/436/6224)，请确保您所在地域在支持范围内。

### 迁移准备
> **注意：** 
> 目前腾讯云的服务迁移支持的镜像格式有：qcow2，vpc，vmdk，raw。建议使用压缩的镜像格式，可以节省传输和迁移的时间。

1. 请根据镜像制作文档制作一份需要迁移服务器的镜像文件。Windows 系统请参考 [Windows 镜像制作文档](https://cloud.tencent.com/document/product/213/17815)，Linux 系统请参考 [Linux 镜像制作文档](https://cloud.tencent.com/document/product/213/17814)。
> **注意：** 
> 上传镜像的 COS 地域需要与您将迁入的云主机地域保持一致。
2. 将制作的镜像文件上传到 COS。由于镜像文件一般较大，网页上传容易断线，建议使用 COSCMD 上传镜像，请参考 [COSCMD 工具文档](https://cloud.tencent.com/document/product/436/10976)。
3. 获取镜像上传的 COS 地址。在 [对象存储控制台](https://console.cloud.tencent.com/cos5/bucket) 中，找到您刚刚上传好的镜像文件，并查看文件信息，获取文件链接。
4. 准备需要迁入的云服务器（CVM）。[前往购买>>](https://buy.cloud.tencent.com/cvm?tab=custom&step=1&regionId=8)


### 离线实例迁移
1. 登录腾讯云，打开 [云服务器控制台](https://console.cloud.tencent.com/cvm/overview)，在左侧导航单击【服务迁移】>【离线实例迁移】。
 ![](https://main.qcloudimg.com/raw/3337617927dcf1e458d9334c77263cf9.png)
2. 单击【新建】，准备建立实例迁移任务。
3. 确认做好迁入准备之后，填写任务名称、COS 链接和需要迁入的云服务器等迁入配置信息，单击【完成】，成功建立迁移任务。
![](https://main.qcloudimg.com/raw/d91b69ed4aab7220feecd431e60c006d.png)
4. 查看迁移任务的进度。
![](https://main.qcloudimg.com/raw/4791b4dcf1dec9472dd4b9047213ef93.png)


### 离线数据迁移
1. 登录腾讯云，打开 [云服务器控制台](https://console.cloud.tencent.com/cvm/overview)，在左侧导航单击【服务迁移】>【离线数据迁移】。
2. 单击【新建】，准备建立数据迁移任务。
3. 确认做好迁入准备之后，填写任务名称、COS 链接和需要迁入的云服务器等迁入配置信息，单击【完成】，成功建立迁移
![](https://main.qcloudimg.com/raw/008d39ef47a97ca3b6fc073ba420f575.png)



## 常见问题
1. **上传 COS 和迁移的耗时太久？**
上传的耗时与镜像文件的大小、带宽的大小等因素有关。建议使用压缩的镜像格式（qcow2 或 vhd），可以节省传输和迁移的时间。

2. **为什么迁移任务失败了？**
 * 目前腾讯云的服务迁移支持的镜像格式有：qcow2，vpc，vmdk，raw，请确认您的镜像格式满足上述之一。
 * 请确认您的镜像文件已经完整上传到 COS 中，并保证文件没有损坏。
 * 迁移需要保证目的云主机/云硬盘处于正常使用期，处于到期状态的设备将无法完成迁移。


