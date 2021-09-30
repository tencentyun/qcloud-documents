本文档将指导您如何在凭据管理系统控制台中删除 CVM SSH 密钥。

## 前提条件
- 已创建 [CVM SSH 密钥的凭据](https://cloud.tencent.com/document/product/1140/60206)。 
- 对凭据进行删除操作之前，需要对凭据进行禁用操作。
- 待删除的凭据未绑定实例。
>? 如果待删除的凭据已绑定实例，您需要在对应的实例中先解除绑定，然后再进行删除操作。

## 操作步骤
1. 登录 [凭据管理系统](https://console.cloud.tencent.com/ssm) 控制台，在左侧导航栏中，单击 **CVM SSH 密钥管理**，进入 CVM SSH 密钥页面。
   ![](https://main.qcloudimg.com/raw/5afcc6fcfee93523a23392d2980103eb.png)
2. 在 CVM SSH 密钥页面中，单击左上角的“区域下拉框”，切换区域。
   ![](https://main.qcloudimg.com/raw/00d49d1edfdf4dfa90446d02be7002b7.png)
3. 在 CVM SSH 密钥页面中，单击搜索框，可通过“标签和凭据名称”等关键字对凭据进行查找。
![](https://main.qcloudimg.com/raw/79d0c4bf2116a2141a0e3433810fe98a.png)
4. 在筛选结果列表中，选择需要删除的凭据，在凭据的右侧操作栏中单击【删除】。
![](https://main.qcloudimg.com/raw/b29d10deea441ea934f3ecf9fbac266a.png)
5. 在删除界面中，可根据实际需求选择 **只删除 SSM 存储的 SSH 密钥** 或**同时删除 SSM 和 CVM 存储的密钥**后，单击**确定**。
![](https://main.qcloudimg.com/raw/510b7382b5d214f9302cdd8f704021c2.png)
