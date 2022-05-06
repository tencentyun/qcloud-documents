## 吊销私有CA

在已启用的私有CA到期前，如果您不再需要继续使用私有CA签发证书，可以在SSL证书服务控制台吊销私有CA。

## 注意事项
- 私有CA下已签发的证书会一并吊销。

>?只有已启用的私有CA支持吊销操作。吊销私有CA不支持退款。吊销私有CA后，您将无法继续通过该CA申请和签发私有证书。
## 操作步骤
1. 登录腾讯云 [私有CA控制台](https://console.cloud.tencent.com/private-ca)，在私有证书页面，定位到要吊销的私有CA，依次单击操作列下的**更多－＞吊销**。

根CA和子CA都可以吊销。建议您先吊销子CA，然后再吊销根CA。具体操作如下：
- 根CA可以直接在操作列下单击吊销。
  ![](https://qcloudimg.tencent-cloud.cn/raw/f5ac109c7583a71e44b84d43293b329c.png)

- 子CA需要先单击操作列下的下拉图标，然后单击吊销。
  ![](https://qcloudimg.tencent-cloud.cn/raw/2010819bed54bfa40e236e078d495214.png)

3. 在弹出的确认对话框，单击吊销。
   ![](https://qcloudimg.tencent-cloud.cn/raw/8257cd1a4cd595d5546875aa748b13c7.png)

>?确认吊销后，CA证书立即吊销。私有CA的状态将变更为吊销，这时您可以将私有CA从列表中删除。