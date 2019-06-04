专用通道支持以下参数的变更：
- **互联地址**
变更互联地址会中断业务，为了业务安全，请您通过 [工单](https://console.cloud.tencent.com/workorder/category) 或架构师预约后台网络工程师进行变更。
- **BGP ASN**
变更 BGP ASN 会中断业务，为了业务安全，请您通过  [工单](https://console.cloud.tencent.com/workorder/category)  或架构师预约后台网络工程师进行变更。
- **带宽**
变更带宽不会中断业务，系统自动覆盖配置。
>**注意：**
>共享专线模式下，专用通道无法申请带宽变更，需由物理专线所有者发起带宽变更。
- **BGP KEY**
变更 BGP KEY 不会中断业务，系统自动覆盖配置。
- **用户 IDC 网段**
支持用户 IDC 网段的修改，系统自动下发配置。

一个通道变更需求可包含多个参数变更内容。若变更涉及“互联地址”或“BGP ASN”，均需要后台网络工程师人工干预；若只有其他 3 个参数的变更，系统将会自动完成配置。

![](https://main.qcloudimg.com/raw/ca7cc2d9e3a9c67b1e832d9873ecea12.png)
