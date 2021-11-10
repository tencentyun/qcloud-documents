关联跨账号私有网络，需要由跨账号 VPC 侧发起申请，云联网所在账号同意 / 拒绝申请即可。 
操作流程如下图所示：
![](https://main.qcloudimg.com/raw/60807add361682ba1472ce05ec9095df.png)

## 申请加入云联网（VPC 账号操作）
1. 登录 [私有网络控制台](https://console.cloud.tencent.com/vpc/vpc?rid=1)。 
2. 在列表中找到需要加入云联网的私有网络 VPC，单击其 ID 进入详情页，单击**立即关联**。
![](https://main.qcloudimg.com/raw/6ce503139704f389e85437908d162cae.png)
3. 在弹窗中，填写对端的账号 ID 和云联网 ID，单击**确定**，提交申请 。
 ![](https://main.qcloudimg.com/raw/26b68cca5e5d406cc2d75c121c6deef1.png)

## 同意申请（云联网账号操作）
1. 登录 [云联网控制台](https://console.cloud.tencent.com/vpc/ccn)，在列表中找到有待同意申请的云联网实例，单击其 ID 进入详情页。 
2. 在“关联实例”页面，会显示待同意的 VPC 信息，单击**同意**并确认操作，即可将该 VPC 加入到云联网中。 
![](https://main.qcloudimg.com/raw/33495ecf47a3d5f6004740ef3c236dd0.png)

## 检查路由表（可选）
同意申请并关联成功后，您还需检查路由表，避免该实例与云联网中已有实例因网段冲突而导致路由未生效的情况。 
相关操作请参见 [检查路由表](https://cloud.tencent.com/document/product/877/18756)。

## 设置跨域互通带宽（可选）
相关操作请参见 [设置跨域互通带宽](https://cloud.tencent.com/document/product/877/18759)。


