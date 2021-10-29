您可通过如下视频了解关于 IDC 通过云联网上云的最佳实践。
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/1670-12013?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 步骤1：创建云联网类型的专线网关
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)，在左侧目录中，单击【专线网关】，进入管理页面。
2. 单击【新建】。
3. 在弹出框中，填写网关名称，关联网络选择【云联网】，云联网实例选择【暂不关联】，单击【确定】。
 ![](https://main.qcloudimg.com/raw/779d51771344c0bad90b5a76a0154879.png)
 
## 步骤2：专线网关添加发布网段
1. 在专线网关列表中，找到需要调整的实例“dcg-\***”，单击其 ID，进入详情页。
2. 单击选项卡中【发布网段】。
3. 单击【新建】，输入用户发布网段。
![](https://main.qcloudimg.com/raw/1145030e32101278bec3348d2e436167.png)

## 步骤3：创建云联网实例
详细操作步骤，请参考云联网文档 [新建云联网实例](https://cloud.tencent.com/document/product/877/18752)。

## 步骤4：创建专用通道连接云联网专线网关
1. 登录 [专线接入控制台](https://console.cloud.tencent.com/dc/dc)，在左侧目录中，单击【专用通道】，进入管理页面。
2. 单击【+新建】。
3. 在弹出框中，根据页面提示填写相关信息，接入网络选择【云联网】，专线网关选择刚刚创建的云联网专线网关“dcg-\***”。
![](https://main.qcloudimg.com/raw/4ab1e79ebf07f674c83b6b14f0e64210.png)

## 步骤5：关联网络实例
把您希望互联的网络实例（包括 VPC 和专线网关，数量可多个）加载到云联网实例，即可完成云联网内的网络实例互通。详细操作步骤，请参见云联网文档 [关联网络实例](https://cloud.tencent.com/document/product/877/18747)。

