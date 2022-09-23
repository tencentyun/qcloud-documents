离线唤醒功能，能够让您的 App 在后台运行或者离线状态下依然能够收到音视频通话的响铃呼叫，TUICallKit 使用 Apple 提供的系统级推送通道（APNs）来进行消息通知。

[](id:step1)
## 步骤一：配置离线推送

1. **申请 APNs 证书**：具体请参见 [离线推送(iOS)](https://cloud.tencent.com/document/product/269/75429#.E6.AD.A5.E9.AA.A41.EF.BC.9A.E7.94.B3.E8.AF.B7-apns-.E8.AF.81.E4.B9.A6) 中的步骤一。
2. **IM 控制台配置**：具体请参见 [离线推送(iOS)](https://cloud.tencent.com/document/product/269/75429#.E6.AD.A5.E9.AA.A42.EF.BC.9A.E4.B8.8A.E4.BC.A0.E8.AF.81.E4.B9.A6.E5.88.B0.E6.8E.A7.E5.88.B6.E5.8F.B0) 中的步骤二。
3. **在 App 每次登录时，向苹果获取 deviceToken**，具体请参见 [离线推送(iOS)](https://cloud.tencent.com/document/product/269/75429#.E6.AD.A5.E9.AA.A43.EF.BC.9Aapp-.E5.90.91.E8.8B.B9.E6.9E.9C.E5.90.8E.E5.8F.B0.E8.AF.B7.E6.B1.82-devicetoken) 中的步骤三。
4. **登录 IM SDK 后上传 deviceToken 到腾讯云**，具体请参见 [离线推送(iOS)](https://cloud.tencent.com/document/product/269/75429#.E6.AD.A5.E9.AA.A44.EF.BC.9A.E7.99.BB.E5.BD.95-im-sdk-.E5.90.8E.E4.B8.8A.E4.BC.A0-devicetoken-.E5.88.B0.E8.85.BE.E8.AE.AF.E4.BA.91) 中的步骤四。

>! [离线推送(iOS)](https://cloud.tencent.com/document/product/269/75429) 中的其他步骤您不需要参考，TUICallKit 已经帮您完成了后续步骤。

[](id:step2)
## 步骤二：配置工程
要在应用程序中添加所需的权限，请在 Xcode 项目中启用推送通知功能。

打开 **Xcode** 项目，在 **Project** > **Target** > **Capabilities** 页面中点击红框中的加号按钮，然后选择并添加 **Push Notifications**，添加后的结果如图中黄框所示：

![](https://qcloudimg.tencent-cloud.cn/raw/b3205de6cf2561b775f037f1f6dc72ac.png)

完成以上步骤，运行您的工程，就可以体验`TUICallKit`离线唤起功能。

## 常见问题
### 1、收不到推送，且后台报错 bad devicetoken？
Apple 的 deviceToken 与当前编译环境有关。如果 [登录 IMSDK 后上传 deviceToken 到腾讯云 ](#uploadDeviceToken) 所使用的证书ID 和 token 不一致，就会报错。

- 如果使用的是 Release 环境编译，则 `- application:didRegisterForRemoteNotificationsWithDeviceToken:`  回调返回的是发布环境的 token，此时 businessID 需要设置生产环境的 [证书ID](#businessid :缺少内容)。
- 如果使用的是 Debug 环境编译，则 `- application:didRegisterForRemoteNotificationsWithDeviceToken:`  回调返回的是开发环境的 token，此时 businessID 需要设置开发环境的证书 ID。

```
V2TIMAPNSConfig *confg = [[V2TIMAPNSConfig alloc] init];
/* 用户自己到苹果注册开发者证书，在开发者帐号中下载并生成证书(p12 文件)，将生成的 p12 文件传到腾讯证书管理控制台，控制台会自动生成一个证书 ID，将证书 ID 传入以下 busiId 参数中。*/
//推送证书 ID
confg.businessID = sdkBusiId;
confg.token = self.deviceToken;
[[V2TIMManager sharedInstance] setAPNS:confg succ:^{

} fail:^(int code, NSString *msg) {

}];
```

### 2、iOS 开发环境下，注册偶现不返回 deviceToken 或提示 APNs 请求 token 失败？
此问题现象是由于 APNs 服务不稳定导致的，可尝试通过以下方式解决：

1. 给手机插入 SIM 卡后使用4G网络测试。
2. 卸载重装、重启 App、关机重启后测试。
3. 打生产环境的包测试。
4. 更换其它 iOS 系统的手机测试。
