实时音视频控制台支持在线生成签名 UserSig，但此 UserSig 仅用于开发阶段快速测试，正式上线前请将 UserSig 计算逻辑 [迁移到后台服务器](https://cloud.tencent.com/document/product/647/17275#.E6.9C.8D.E5.8A.A1.E7.AB.AF.E5.A6.82.E4.BD.95.E8.AE.A1.E7.AE.97-usersig.EF.BC.9F) 上，以避免加密密钥泄露导致的流量盗用。


[](id:generate)
## 签名（UserSig）生成工具
开发者和腾讯云的服务通过签名（UserSig) 验证建立信任关系。

1. 进入实时音视频控制台，选择左侧栏的【开发辅导工具】>【[UserSig生成&校验](https://console.cloud.tencent.com/trtc/usersigtool)】，查看【签名(UserSig)生成工具】模块。
2. 单击下拉框选择您已创建的应用（SDKAppID），完成后会自动生成对应的密钥（Key）。
3. 填写用户名（UserID）。
3. 单击【生成签名UserSig】，即可立即生成对应的签名 UserSig。
![](https://main.qcloudimg.com/raw/1beace0cb76655168f4b0b9f06eb65e4.png)


[](id:check)
## 签名（UserSig）校验工具
此工具用于校验您使用的签名（UserSig）的有效性。

>! 使用时，请确保请求检验时输入的 SDKAppID、UserID 与 UserSig 的 SDKAppID、UserID 保持一致。

1. 进入实时音视频控制台，选择左侧栏的【开发辅导工具】>【[UserSig生成&校验](https://console.cloud.tencent.com/trtc/usersigtool)】，查看【签名(UserSig)校验工具】模块。
2. 选择需校验的应用（SDKAppID），完成后会自动生成对应的密钥（Key）。
3. 输入用户名（UserID）。
4. 将需校验的签名（UserSig）复制粘贴到【签名(UserSig)】中，单击【开始校验】。
>? 若您是在【签名(UserSig)生成工具】模块中生成的 UserSig，建议单击【复制签名UserSig】进行复制。
>
![](https://main.qcloudimg.com/raw/d8ee8b9c6d1d20ae325ec61964e788d9.png)
5. 校验完成后，您可查看下方的校验结果：
	- 校验成功示例：
	![](https://main.qcloudimg.com/raw/bd68863171529bd72a6bf20cbe628582.png)
	- 校验失败示例：
	![](https://main.qcloudimg.com/raw/0b32a98cad31330a56e5b2f3fa4e282c.png)


## 相关文档
更多 UserSig 相关问题，请参见 [UserSig 相关问题](https://cloud.tencent.com/document/product/647/17275)。
