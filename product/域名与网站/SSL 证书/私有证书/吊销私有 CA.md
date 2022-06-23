## 操作场景
在已启用的私有 CA 到期前，如您不再需要继续使用私有 CA 签发证书，可在 SSL 证书 [私有 CA 控制台](https://console.cloud.tencent.com/private-ca) 吊销私有 CA。本文将指导您如何吊销私有 CA。

## 注意事项
如已吊销，私有 CA 下已签发的证书会一并吊销。
>?
>- 只有已启用的私有 CA 支持吊销操作。
>- 吊销私有 CA 不支持退款。
>- 吊销私有 CA 后，您将无法继续通过该 CA 申请和签发私有证书。
>

## 操作步骤
1. 登录腾讯云 [私有 CA 控制台](https://console.cloud.tencent.com/private-ca)，进入 “私有 CA” 管理页面。
2. 选择您需要吊销的私有 CA，单击 <img src="https://qcloudimg.tencent-cloud.cn/raw/2a778da88f2967b7115274d776528941.png"/>，即可展开当前私有 CA 的所有子 CA。
3. 选择需要吊销的子 CA，单击**更多＞吊销**。如下图所示：
>?根 CA 和子 CA 均可以吊销。建议您先吊销子 CA，再吊销根 CA。
>
![](https://qcloudimg.tencent-cloud.cn/raw/d668b9f8094b66bd83985c9ae516934e.png)
4. 子 CA 吊销完成后，单击根 CA 操作列下的**更多 > 吊销**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/76365eb09a83dc50a26c24b4adecd3f9.png)
5. 在弹出的确认对话框中，单击**确定**。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/8257cd1a4cd595d5546875aa748b13c7.png)
>?确认吊销后，CA 证书立即吊销。私有 CA 的状态将变更为吊销，您可以将私有 CA 从列表中删除。
