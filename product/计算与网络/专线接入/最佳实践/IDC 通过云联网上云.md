## 步骤 1：创建云联网类型的专线网关
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)，在左侧目录中，单击【专线网关】，进入管理页面。
2. 单击【新建】。
3. 在弹出框中，填写网关名称，关联网络选择【云联网】，云联网实例选择【暂不关联】，单击【确定】。
 ![1](https://main.qcloudimg.com/raw/1c2c8a3989764a9eafd3c2f82a5eb5f4.png)
 
## 步骤 2：专线网关添加 IDC 网段
1. 在专线网关列表中，找到需要调整的实例“dcg-\***”，单击其 ID，进入详情页。
2. 单击选项卡中【IDC 网段】。
3. 单击【添加】，输入用户 IDC 网段。
![2](https://main.qcloudimg.com/raw/1652cfec77d76f9aadecd551942e1e01.png)

## 步骤 3：创建云联网实例
详细操作步骤，请参考云联网文档 [新建云联网实例](https://cloud.tencent.com/document/product/877/18752)。

## 步骤 4：创建专用通道连接云联网专线网关
1. 登录 [专线接入控制台](https://console.cloud.tencent.com/dc/dc)，在左侧目录中，单击【专用通道】，进入管理页面。
2. 单击【+ 新建】。
3. 在弹出框中，根据页面提示填写相关信息，接入网络选择【云联网】，专线网关选择刚刚创建的云联网专线网关“dcg-\***”。
![3](https://main.qcloudimg.com/raw/aa80ea33e85fe2fb4c6ba73683e6ace8.png)

## 步骤 5：关联网络实例
把您希望互联的网络实例（包括 VPC 和专线网关，数量可多个）加载到云联网实例，即可完成云联网内的网络实例互通。详细操作步骤，请参见云联网文档 [关联网络实例](https://cloud.tencent.com/document/product/877/18747)。
