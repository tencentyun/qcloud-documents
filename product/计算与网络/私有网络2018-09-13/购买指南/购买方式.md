本文将为您详细介绍私有网络收费产品的购买方式。
## 控制台购买
### NAT 网关 
您可通过 [腾讯云官方网站](https://cloud.tencent.com/) 进行 NAT 网关的购买。
下面将为您介绍在官网购买 NAT 网关的具体操作。
1. 登录腾讯云官网，进入 [NAT 网关 产品介绍页](https://cloud.tencent.com/product/nat)。
2. 单击【立即体验】，进入私有网络控制台。
 ![](https://main.qcloudimg.com/raw/922847ad5a7224562283d37289fb87dd.png)
3. 单击左侧目录中的【NAT 网关】，在 NAT 网关页面，单击【新建】。
 ![](https://main.qcloudimg.com/raw/c044612141982974b43c71e367f373db.png)
4. 在弹框中依次输入或确定参数：网关名称、网关类型、所属网络、弹性 IP ，单击【创建】即可。
 ![](https://main.qcloudimg.com/raw/b08af08229d92a988d5648caff64a479.png)

更多 NAT 网关相关操作，请参考文档 [快速入门](https://cloud.tencent.com/document/product/552/18186)。

### VPN 连接
您可通过 [腾讯云官方网站](https://cloud.tencent.com/) 进行 VPN 连接的购买。
下面将为您介绍在官网购买 VPN 连接的具体操作。
1. 登录腾讯云官网，进入 [VPN 连接产品介绍页](https://cloud.tencent.com/product/eni)。
2. 单击【立即体验】，进入私有网络控制台。
 ![](https://main.qcloudimg.com/raw/30070de2da8ea8ab54cf79e9cb285571.png)
3. 选择地区和私有网络，单击【新建】。
 ![](https://main.qcloudimg.com/raw/d66f044c69f656279038c723f0849c84.png)
4. 在弹窗中填写网关名称，选择所属网络、带宽上限、计费方式后，单击【创建】即可。
 ![](https://main.qcloudimg.com/raw/faf03795d9a4aacecbc99f642e1e8b23.png)

### 对等连接
1. 登录 [腾讯云控制台](https://console.cloud.tencent.com/) ，选择【云产品】>【云计算与网络】>【私有网络】，进入私有网络控制台。
2. 单击左侧目录中的【对等连接】，进入管理页面。
3. 在列表上方选择地域和私有网络，单击【新建】。
 ![](https://main.qcloudimg.com/raw/57786db314c63e45265a9656d6ef4671.png)
4. 输入名称，选择对端地域、对端账户类型及对端私有网络。
 - 当对端账户类型为 “ 我的账户 ” 时，直接从下拉列表中选择。
 - 当对端账户类型为 “ 其他账户 ” 时，需要手动输入对端账户的账号 ID 和 VPC 的 ID。
 ![](https://main.qcloudimg.com/raw/a5e601765747a100a60e7845bf2553b8.png)
5. 选择带宽上限
 - 同地域对等连接带宽无上限，**不可修改**。
 - 跨地域对等连接可以选择带宽上限。如需更大的跨地域带宽，请提 [工单申请](https://console.cloud.tencent.com/workorder/category)。
6. 单击【创建】，同账户内 VPC 进行连接，新建后对等连接立即生效。
>**注意：**
>跨地域的对等连接费用，由对等连接申请方支付。

## API 购买
详情请参见 [私有网络 API](https://cloud.tencent.com/document/product/215/15755)。