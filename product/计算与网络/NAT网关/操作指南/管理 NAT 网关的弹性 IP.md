创建 NAT 网关后，您可以对网关的弹性公网 IP 进行管理，下面将为您详细介绍管理方法。

## 操作步骤
1. 登录 [NAT 网关控制台](https://console.cloud.tencent.com/vpc/nat?fromNav)。
2. 在列表中单击网关 ID 进入详情页。
3. 选择**关联弹性公网 IP** 标签页 ，在该页面可以查看 NAT 网关上绑定的 EIP 信息，也可以对 NAT 网关的 EIP 进行管理。
![](https://qcloudimg.tencent-cloud.cn/raw/e539f7549b44046e64df17150b5d658d.png)

### 绑定弹性公网 IP
>?
>- 当一个 NAT 网关绑定多个弹性公网 IP 时，系统会自动做负载均衡。
>- 当前仅支持绑定已有弹性公网 IP，不支持新建。需要先去 [公网 IP 控制台](https://console.cloud.tencent.com/cvm/eip) 创建。
>
1. 单击弹性公网 IP 页签上方的**绑定弹性公网 IP**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/ba221a06ad7423a9df27a2a2ee2cab33.png" width="70%">
2. 在**选择 IP**下拉框中选择需要绑定的弹性公网 IP，然后单击**确定**选中一个或者多个弹性公网 IP。
<img src="https://qcloudimg.tencent-cloud.cn/raw/07d8f99a3be7897bceb57eee3bd0ad72.png" width="70%">
3. 单击**确定**完成绑定。


### 调整弹性公网 IP 的带宽
1. 在对应弹性公网 IP 所在行的操作栏中，单击**调整带宽**。
![](https://qcloudimg.tencent-cloud.cn/raw/340ec2e6930018383df2d1e866fd3094.png)
2. 在**调整带宽**弹窗中调整目标带宽，然后单击**确定**
<img src="https://qcloudimg.tencent-cloud.cn/raw/a3dd76926d38c6383a1ecf69cb3ff6c2.png" width="70%">

### 解绑弹性公网 IP
>?当 NAT 网关上只有一个弹性公网 IP 时，不支持解绑操作。
>
1. 在对应弹性公网 IP 所在行的操作栏中，单击**解绑**。
![](https://qcloudimg.tencent-cloud.cn/raw/106f2d8629ddb53feca3d5be805aca31.png)
2. 在**确认解绑该弹性公网 IP** 弹窗中，单击**确定**，完成解绑。
<img src="https://qcloudimg.tencent-cloud.cn/raw/7eae0906caac3676e257010be72b5c9c.png" width="70%">
