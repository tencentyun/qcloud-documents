本文将引导您通过云联网，实现云联网关联跨账号 VPC 的功能。

## 前提条件
- 跨账号双方都具有云联网 [内测资格](https://cloud.tencent.com/apply/p/tp2478t9skn)（本文以账号 A 和账号 B 为例）。
- 需要互联的私有网络 VPC 已创建好。
- 需要互联的各 VPC 子网网段、IDC 网段没有冲突。

## 步骤1：账号 A 创建云联网实例
1. 使用账号 A 登录 [腾讯云控制台](https://console.cloud.tencent.com/) ，选择【云产品】>【网络】>【私有网络】，进入私有网络控制台。
2. 单击左侧目录中的 【云联网】，进入云联网管理页面。
3. 单击【新建】。 
 ![](https://main.qcloudimg.com/raw/4189c3d3af70c389a81159a12198a21c.png)
4. 在弹出框中填写云联网实例名称、备注。
![](https://main.qcloudimg.com/raw/1d7b2a5da13c03e8cc1053b94edb7f30.png)
5. 关联一个网络实例（也可创建好云联网后再关联）。
6. 单击【确定】创建云联网实例。

## 步骤2：VPC 所属账号 B 申请关联云联网
1. 使用账号 B 登录 [腾讯云控制台](https://console.cloud.tencent.com/) ，选择【云产品】>【网络】>【私有网络】，进入私有网络控制台。
2. 在私有网络列表中，单击需要关联至云联网的 VPC 的 ID，进入详情页。
3. 单击【立即关联】。
![](https://main.qcloudimg.com/raw/0ed0b142be6116cf4cf9fa4aff81c611.png)
4. 在弹出框中，选择【其他账号】，并输入账号 A 的账号 ID、云联网实例 ID。
![](https://main.qcloudimg.com/raw/29bbc4c616fd2b6c64b463a6c9a8ec8d.png)
5. 单击【确定】，即可向云联网所属账号发送关联申请。

## 步骤3：云联网账号 A 同意账号 B 的关联申请
1. 使用账号 A 登录 [腾讯云控制台](https://console.cloud.tencent.com/)，选择【云产品】>【网络】>【私有网络】，进入私有网络控制台。 
2. 单击左侧目录中的【云联网】，在列表中找到有待同意申请的云联网实例，单击其 ID 进入详情页。 
3. 在【关联实例】页面，会显示待同意的 VPC 信息，单击【同意】并确认操作，即可将该 VPC 加入到云联网中。 
 ![3](https://main.qcloudimg.com/raw/f63b5f1497e372515521e75f3467eb59.png)

## 步骤4：检查路由表
若所关联的网络实例网段有冲突，则会产生失效路由，查看操作如下：
1. 在云联网列表中，单击要查看路由的云联网 ID，进入详情页。
2. 单击【路由表】，查看该云联网路由表。
3. 检查是否存在状态为失效的路由策略。
 ![](https://main.qcloudimg.com/raw/ae2fb3be44f2f56ab64a257f505b2b4e.png)
4. 路由冲突原则，详情请参见 [路由限制](https://cloud.tencent.com/document/product/877/18679#.E8.B7.AF.E7.94.B1.E9.99.90.E5.88.B6)，如需启用冲突路由，详情请参见 [启用路由](https://cloud.tencent.com/document/product/877/18750)。

## 步骤5：设置跨地域带宽限制（可选）
1. 在云联网列表中，单击需要设置带宽的云联网 ID，进入详情页。
2. 单击【监控】标签页，查看该云联网的监控信息。
3. 选择您要设置出带宽限制的区域。
4. 设置各地域的出带宽上限（默认1Gbps）。
 ![](https://main.qcloudimg.com/raw/e92d2cef0bdf5366054f7fd71415f24a.png)

>?云联网实例间通信可能会产生费用，详情请参见 [计费总览](https://cloud.tencent.com/document/product/877/18676)。

