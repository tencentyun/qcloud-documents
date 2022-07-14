## 操作场景
如果需要对物理主机绑定弹性公网 IP 与外网访问进 ACL 控制，需要创建弹性公网 IP ACL。本文档主要指导您如何创建、修改和删除弹性公网 IP ACL 以及 ACL 规则设置等相关内容。

## 前提条件
已登录 [腾讯云控制台](https://console.cloud.tencent.com/)。

## 操作步骤
### 创建弹性公网 IP ACL
1. 选择 **[黑石私有网络](https://console.cloud.tencent.com/vpcbm)** 选项卡，选择**外网安全** > **弹性公网 IP ACL**。
2. 单击左上角**新建**，在弹出框中依次输入或确定以下参数：
 - 名称
 - 状态方式
3. 选择结束后单击**确认**，即可完成弹性公网 IP ACL 的创建。


### 修改弹性公网 IP ACL
弹性公网 IP ACL 创建后，可以对其属性进行修改。
1. 选择 **[黑石私有网络](https://console.cloud.tencent.com/vpcbm)** 选项卡，选择**外网安全** > **弹性公网 IP ACL**。
2. 在弹性公网 IP ACL 列表页中，单击需要修改的弹性公网 IP ACL ID。
3. 进入详情页，在基本信息中完成以下属性修改：
 - 修改弹性公网 IP ACL 名称；
 - 修改弹性公网 IP ACL 状态方式，更改后实时生效。


### 删除弹性公网 IP ACL
弹性公网 IP ACL 创建后，可以对其进行删除；
1. 选择 **[黑石私有网络](https://console.cloud.tencent.com/vpcbm)** 选项卡，选择**外网安全** > **弹性公网 IP ACL**。
2. 在弹性公网 IP ACL 列表页中，选择需要删除的弹性公网 IP ACL 操作列**删除**。


### ACL 规则设置
1. 选择 **[黑石私有网络](https://console.cloud.tencent.com/vpcbm)** 选项卡，选择 **外网安全** > **弹性公网 IP ACL**。
2. 在弹性公网 IP ACL 列表页中单击需要修改的弹性公网 IP ACL ID 进入详情页，在 ACL 规则中完成 ACL 规则设置：
 - 入站规则设置：定协议类型、目标端口（访问黑石物理主机端口）、来源 IP，设定允许/拒绝策略；
 - 出站规则设置：指定协议类型、目标端口（访问外部主机端口）、目标 IP，设定允许/拒绝策略。


### 关联弹性公网 IP
1. 选择 **[黑石私有网络](https://console.cloud.tencent.com/vpcbm)** 选项卡，选择**外网安全** > **弹性公网 IP ACL**。
2. 在弹性公网 IP ACL 列表页中单击需要修改的 弹性公网 IP ACL ID 进入详情页，在关联弹性公网 IP 中，完成弹性 IP 设置：
 - 关联弹性 IP。
 - 解除弹性 IP。


### 在弹性公网 IP 控制台进行 ACL 操作
1. 选择 **[黑石私有网络](https://console.cloud.tencent.com/vpcbm)** 选项卡，单击**弹性公网 IP**。
2. 在弹性公网 IP 列表页中，选择需要修改的弹性公网 IP 操作列**更多**选项卡，单击**关联 ACL**。
3. 在关联 ACL 中选择加入的弹性公网 IP ACL。

