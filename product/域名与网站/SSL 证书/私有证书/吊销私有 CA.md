## 操作场景
在已启用的私有 CA 到期前，如果您不再需要继续使用私有 CA 签发证书，可以在 SSL 证书服务控制台吊销私有 CA。

## 前提条件
- 私有 CA 下不存在已签发的证书。
- 如在需吊销的私有 CA 证书列表中，存在已签发的证书，您需要先吊销已签发的证书，再吊销 CA。关于吊销证书的具体操作，请参见 [吊销私有证书](https://cloud.tencent.com/document/product/400/72335)。

>?只有已启用的私有 CA 支持吊销操作。吊销私有 CA 不支持退款，吊销私有 CA 后，您将无法继续通过该 CA 申请和签发私有证书。
>
## 操作步骤
1. 登录 [SSL 证书私有 CA 控制台](https://console.cloud.tencent.com/private-ca)，进入私有 CA 列表。
2. 选择您需要吊销的私有 CA，单击操作列下的**更多＞吊销**。
>?根 CA 和子 CA 都可以吊销。建议您先吊销子 CA，再吊销根 CA。
>
 - 根 CA 在操作列单击**更多＞吊销**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/f5ac109c7583a71e44b84d43293b329c.png)
 - 子 CA 在操作列单击**更多＞吊销**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/2010819bed54bfa40e236e078d495214.png)
3. 在弹出的确认对话框中，单击**确定**。
![](https://qcloudimg.tencent-cloud.cn/raw/8257cd1a4cd595d5546875aa748b13c7.png)
>?确认吊销后，CA 证书则立即吊销成功。私有 CA 的状态将变更为吊销，同时可将私有 CA 从列表中删除。
>
