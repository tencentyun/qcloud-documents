您可通过如下视频了解关于 IDC 通过云联网上云的最佳实践。
<div class="doc-video-mod"><iframe src="https://cloud.tencent.com/edu/learning/quick-play/1670-12013?source=gw.doc.media&withPoster=1&notip=1"></iframe></div>

## 步骤1：创建云联网类型的专线网关
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)，在左侧目录中，单击【专线网关】，进入管理页面。
2. 单击【新建】。
3. 在弹出框中，填写网关名称，关联网络选择【云联网】，云联网实例选择【暂不关联】，单击【确定】。
 ![1](https://main.qcloudimg.com/raw/1c2c8a3989764a9eafd3c2f82a5eb5f4.png)
 
## 步骤2：专线网关添加 IDC 网段
1. 在专线网关列表中，找到需要调整的实例“dcg-\***”，单击其 ID，进入详情页。
2. 单击选项卡中【IDC 网段】。
3. 单击【添加】，输入用户 IDC 网段。
![](https://main.qcloudimg.com/raw/a41ea06ab56488433e779c7d3ccb90f6.png)

## 步骤3：创建云联网实例
详细操作步骤，请参考云联网文档 [新建云联网实例](https://cloud.tencent.com/document/product/877/18752)。

## 步骤4：创建专用通道连接云联网专线网关
1. 登录 [专线接入控制台](https://console.cloud.tencent.com/dc/dc)，在左侧目录中，单击【专用通道】，进入管理页面。
2. 单击【+新建】。
3. 在弹出框中，根据页面提示填写相关信息，接入网络选择【云联网】，专线网关选择刚刚创建的云联网专线网关“dcg-\***”。
![](https://main.qcloudimg.com/raw/f12231a395d47d3c942dfeaa1f0d4f10.png)

## 步骤5：关联网络实例
把您希望互联的网络实例（包括 VPC 和专线网关，数量可多个）加载到云联网实例，即可完成云联网内的网络实例互通。详细操作步骤，请参见云联网文档 [关联网络实例](https://cloud.tencent.com/document/product/877/18747)。
