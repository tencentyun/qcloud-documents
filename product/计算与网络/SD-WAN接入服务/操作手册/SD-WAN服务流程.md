![](https://qcloudimg.tencent-cloud.cn/raw/9a0462ef84001d6a437d2b6ac699e74a.png)

## 准备阶段（POC 测试）
在本阶段需要您向腾讯云侧反馈具体的业务需求，腾讯侧依据需求制定相应的验证性测试（POC 测试）方案，下来您根据 POC 测试方案执行测试，POC 测试完成进入正式商用阶段。

### 了解客户需求
1. 您可以通过如下两种方式联系腾讯云商务经理。
 -  方式一：联系与您对接的腾讯云商务经理。
 - 方式二：请提交 [工单申请](https://console.cloud.tencent.com/workorder/category) 进行购买。
2. 梳理您的业务需求反馈于腾讯云商务经理。
业务包括使用场景、接入点列表、接入方式、带宽需求、时延需求和丢包需求等。

### 制定客户 POC 测试专属方案。
腾讯侧依据您的业务需求设计相应的专属 POC 测试方案。

### 执行 POC 测试。
1. 申请测试设备和测试金。
依据 POC 测试方案，您需要联系腾讯云商务经理申请 POC 测试设备和测试金。审核通过后腾讯云向您派发 POC 测试设备。
2. 在 [SD-WAN 控制台](https://console.cloud.tencent.com/sas/edge) 创建 Edge 实例，详情请参见 [新建 Edge 实例](https://cloud.tencent.com/document/product/1277/47255) 。
3. 收到设备后请将设备连线、安装并激活，详情请参见 [安装 Edge 设备](https://cloud.tencent.com/document/product/1277/66361) 。
4. 使用测试金购买测试带宽，详情请参见[ 购买带宽](https://cloud.tencent.com/document/product/1277/66362) 。
5. 创建云联网实例并与 Edge 实例关联。
 - 创建云联网实例请参见[ 新建云联网实例](https://cloud.tencent.com/document/product/877/18752)。
 - Edge 实例关联云联网实例请参见 [关联云联网](https://cloud.tencent.com/document/product/1277/47262)。
6. 进行 POC 测试。
如果测试结果达到 POC 测试方案预期结果，POC 测试完成。通常 POC 测试时长为1个月。
7. 退还 POC 测试设备，转正式使用。
POC 测试完成，您需要退还测试设备，购买正式商用设备。 
>?建议退还设备时仅拆除设备，控制台上 Edge 实例配置不要修改，方便正式商用设备到货后，即插即用。
>

## 正式使用	
本阶段为正式商用阶段。完成 POC 测试后，您需要联系您对应的腾讯商务购买正式 Edge 设备，并在到货后完成设备安装、带宽购买等。
>?如果您收到正式设备后不想采用 POC 测试阶段的配置，您可以参考 POC 测试阶段流程进行配置，或者参见[ 快速入门 ](https://cloud.tencent.com/document/product/1277/47301)或者[ 最佳实践 ](https://cloud.tencent.com/document/product/1277/61812)进行配置。下文为采用 POC 测试阶段配置的场景。
>
1. [ 购买 Edge 设备](https://cloud.tencent.com/document/product/1277/64713)，Edge 设备预计14天内送达。
2. 收到设备后请按照 POC 测试阶段设备连线方式接入设备并在控制台激活。
3. 在控制台 [更换/绑定设备 SN](https://cloud.tencent.com/document/product/1277/64770)。
4. SD-WAN 设备安装完成后、Edge 实例绑定 SN 后，您还需要购买带宽，才能进行资源访问，详情请参见 [购买带宽](https://cloud.tencent.com/document/product/1277/66362) 。
5. 如果需要关联新的云联网实例，则需要新建云联网实例，然后在 SD-WAN 控制台关联。
	- 创建云联网实例请参见 [新建云联网实例](https://cloud.tencent.com/document/product/877/18752)
	- Edge 实例关联云联网实例请参见 [关联云联网](https://cloud.tencent.com/document/product/1277/47262)
6. 连通性测试。
如果您可以访问到所需的腾讯云资源或者目的端资源，表示 SD-WAN 网络畅通；如果不通，可提交 [工单申请](https://console.cloud.tencent.com/workorder/category) 寻求帮助。


## 售后服务
本阶段为售后服务阶段。您在使用正式的 SD-WAN 接入服务后，有任何的设备问题及其他 SD-WAN 使用问题可联系腾讯侧技术支持人员咨询 [ 售后服务](https://cloud.tencent.com/document/product/1277/64713#.E5.94.AE.E5.90.8E.E6.9C.8D.E5.8A.A1)。
