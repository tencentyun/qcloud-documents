### TUICallKit 是否可以不引入 IM SDK，只使用 TRTC？
**不可以。**TUIKit 全系组件都使用了腾讯云 IM SDK 做为通信的基础服务，比如通话拨打信令、通话忙线信令等核心逻辑，如果您已经购买有其他 IM 产品，也可以参照 TUICallKit 逻辑进行适配。

### TUICallKit 组件支持自定义铃声吗？
**支持**，调用 [TUICalling#setCallingBell](https://cloud.tencent.com/document/product/647/47748#setCallingBell) 即可。

### CocoaPods 如何安装？
在终端窗口中输入如下命令（需要提前在 Mac 中安装 Ruby 环境）：

```
sudo gem install cocoapods
```

### TUICallKit 是否支持后台运行？
**支持**，如需要进入后台仍然运行相关功能，可选中当前工程项目，在 **Capabilities** 下的设置  **Background Modes** 打开为 **ON**，并勾选 **Audio，AirPlay and Picture in Picture** ，如下图所示：
![](https://main.qcloudimg.com/raw/d960dfec88388936abce2d4cb77ac766.jpg)
