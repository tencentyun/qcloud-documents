本文介绍在腾讯云点播控制台，提交以下 FairPlay 证书信息：

- FPS 证书文件（.cer）
- 私钥文件（.pem）
- 私钥密码
- ASK（Application Secret Key）

如果您还没有申请以上 FairPlay 证书信息，请参考 [如何申请 FairPlay 证书信息](https://cloud.tencent.com/document/product/266/79725)。

## 操作步骤
1. 登录腾讯云点播控制台。

2. 点击展开左侧导航栏`视频处理设置`，点击` 商业级 DRM 配置 `，点击右侧 `编辑`。
   ![image-20220425210931543](https://qcloudimg.tencent-cloud.cn/raw/5ddca328ebc5999c41019dbd5c192449.png)

3. 设置 FPS 证书信息，包括证书文件（`fairplay.cer`）、私钥文件（`privatekey.pem`）、私钥密码、ASK，并点击`保存`。

   ![image-20220425211140740](https://qcloudimg.tencent-cloud.cn/raw/cecd01537367f178377b88fa5ccbed74.png)

4. 保存之后，可以看到 `FairPlay` 的证书信息。

   ![image-20220426191830269](https://qcloudimg.tencent-cloud.cn/raw/a57e9d6da1d93629fdedafdef123fd6b.png)

## 总结

至此，您已经在腾讯云点播控制台完成了 `FairPlay` 证书信息的配置。
