本文将引导您通过云联网，实现同账号下的 VPC 和 IDC 互通。

## 前提条件
- 您的账号具有云联网 [内测资格](https://cloud.tencent.com/apply/p/tp2478t9skn)。
- 需要互联的 VPC 已创建好。
- 需要互联的各 VPC 子网网段、IDC 网段没有冲突。

## 步骤1：创建云联网实例
1. 登录 [腾讯云控制台](https://console.cloud.tencent.com/) ，选择【云产品】>【网络】>【私有网络】，进入私有网络控制台。
2. 单击左侧目录中的【云联网】，进入云联网管理页面。
3. 单击【新建】。 
 ![](https://main.qcloudimg.com/raw/4189c3d3af70c389a81159a12198a21c.png)
4. 在弹出框中填写云联网实例名称、描述，选择关联实例的 VPC ID，单击【创建】。
![](https://main.qcloudimg.com/raw/4e15ec311c78a1489835a79364c55a7b.png)
5. 关联一个网络实例（也可创建好云联网后再关联）。
6. 单击【确定】创建云联网实例。

## 步骤2：关联网络实例
1. 在云联网列表中，单击需要关联网络实例的云联网 ID，进入详情页。
2. 在新增实例页面下，单击【关联实例】。 
 ![](https://main.qcloudimg.com/raw/26cb82eddf09bc92f9f19903ebbdda26.png)
3. 在弹出框中，选择需要关联的网络实例类型、所属地域和具体实例。
![](https://main.qcloudimg.com/raw/f85ae1242459397ee9339cf89fc01acb.png)
>?如还需关联其他网络实例，可单击【+ 添加】继续关联。
4. 单击【确定】，将所选网络实例加入云联网。

## 步骤3：检查路由表
若所关联的网络实例网段有冲突，则会产生失效路由，查看操作如下：
1. 在云联网列表中，单击要查看路由的云联网 ID，进入详情页。
2. 单击【路由表】，查看该云联网路由表。
3. 检查是否存在状态为失效的路由策略。
 ![](https://main.qcloudimg.com/raw/ae2fb3be44f2f56ab64a257f505b2b4e.png)
4. 路由冲突原则请参考 [路由限制](https://cloud.tencent.com/document/product/877/18679#.E8.B7.AF.E7.94.B1.E9.99.90.E5.88.B6)，如需启用冲突路由，详情请参见 [启用路由](https://cloud.tencent.com/document/product/877/18750)。

## 步骤4：设置跨地域带宽限制（可选）

1. 在云联网列表中，单击需要设置带宽的云联网 ID，进入详情页。
2. 单击【监控】标签页，查看该云联网的监控信息。
3. 选择您要设置出带宽限制的区域。
4. 设置各地域的出带宽上限（默认1Gbps）。
 ![](https://main.qcloudimg.com/raw/e92d2cef0bdf5366054f7fd71415f24a.png)

>?云联网实例间通信可能会产生费用，详情请参见 [计费总览](https://cloud.tencent.com/document/product/877/18676)。
