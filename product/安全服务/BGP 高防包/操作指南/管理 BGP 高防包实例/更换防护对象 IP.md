## 操作场景
BGP 高防包为腾讯云公网 IP 提供更高的 DDoS 防护能力，可支持防护 CVM、CLB、NAT、WAF 等产品和服务。
用户可根据实际业务需求为已绑定设备的 BGP 高防包实例更换防护对象。

## 前提条件
在更换防护对象，您需要成功 [购买 BGP 高防包实例](https://cloud.tencent.com/document/product/1021/31479) 并已为其 [绑定防护对象 IP](https://cloud.tencent.com/document/product/1021/31463)。

## 操作步骤
1. 登录 [DDoS 防护（大禹）管理控制台](https://console.cloud.tencent.com/dayu/overview)，选择【BGP高防包】>【资产列表】，选择地域。
 - 若您的 BGP 高防包实例是独享包，则选择【独享包】页签。
 - 若您的 BGP 高防包实例是共享包，则选择【共享包】页签。
2. 单击目标 BGP高防包实例所在行的【更换设备】。
3. 在【绑定设备】页面，根据实际防护需求选择【关联设备类型】与【选择关联机器】。
  - 若您的 BGP 高防包实例是独享包，仅支持绑定一个关联机器。
   ![](https://main.qcloudimg.com/raw/049933bb5ee7a153404213144226b85d.png)
 - 若您的 BGP 高防包实例是共享包，【关联设备类型】与【选择关联机器】均允许多选，【选择关联机器】数量不得超过 [购买 BGP 高防包实例](https://cloud.tencent.com/document/product/1021/31479) 时设置的【IP 数量】。
 ![](https://main.qcloudimg.com/raw/398b590808a3690a1c76b4e40c6b15ad.png)
4. 单击【确定】。
