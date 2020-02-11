## 消息推送工具
您可以使用该工具自助查询收不到离线消息的问题。

1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) ，单击目标应用卡片。
2. 在左侧导航栏选择【开发辅助工具】>【消息推送工具】。
3. 选择离线证书，输入 UserID。
4. 单击【开始发送】，查看发送结果。
  若发送失败，您可以查看具体的失败原因以及解决方案。
  ![](https://main.qcloudimg.com/raw/8331b306bc248fcbedc27aa54d6c14c5.png)
	
## UserSig 工具
### 签名（UserSig）生成工具
系统将会自动获取当前应用的密钥，您只需要填写用户名（UserID）即可使用该工具快速生成签名（UserSig）用于本地跑通 Demo 以及功能调试。如需用于正式业务，请采用 [服务端计算 UserSig](https://cloud.tencent.com/document/product/269/32688#GeneratingdynamicUserSig) 方式。

1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) ，单击目标应用卡片。
2. 在左侧导航栏选择【开发辅助工具】>【UserSig工具】。
3. 在签名（UserSig）生成工具区域，输入用户名。
4. 单击【生成签名（UserSig）】即可生成签名，签名有效期默认为180天。
5. 单击【复制签名（UserSig）】即可粘贴保存签名。
 ![](https://main.qcloudimg.com/raw/83a24d72ec8914e8c1fa308457677e9f.png)

### 签名（UserSig）校验工具
系统将会自动获取当前应用的密钥，您只需要填写 UserID 和 UserSig 即可使用该工具快速校验 UserSig 的有效性。

1. 登录 [即时通信 IM 控制台](https://console.cloud.tencent.com/im) ，单击目标应用卡片。
2. 在左侧导航栏选择【开发辅助工具】>【UserSig工具】。
3. 在签名（UserSig）校验工具区域，输入 UserID 和 UserSig。
   ![](https://main.qcloudimg.com/raw/6a304f8709fe4d91c2358daf667def24.png)
4. 单击【开始校验】，查看校验结果信息。
 - 若校验成功，您可以查看该 UserSig 对应的 SDKAppID、UserID、生成时间、有效期和过期时间。
  ![](https://main.qcloudimg.com/raw/2882d65f9f28df99fe0c911db197fcce.png)
 - 若校验失败，您可以查看具体的失败原因以及解决方案。
  ![](https://main.qcloudimg.com/raw/f9cd08fb30d5ef24633e64bbb97e093d.png)
 
