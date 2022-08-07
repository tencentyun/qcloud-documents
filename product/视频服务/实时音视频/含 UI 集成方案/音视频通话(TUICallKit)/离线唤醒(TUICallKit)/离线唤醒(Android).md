离线唤醒功能，能够让您的 App 在后台运行或者离线状态下依然能够收到音视频通话的响铃呼叫，TUICallKit 使用了 **TUIOfflinePush** 组件实现离线唤醒功能。

## 步骤一：配置各厂商的推送平台

1. 注册应用到厂商推送平台：离线推送功能依赖厂商原始通道，您需要将自己的应用注册到各个厂商的推送平台，得到 APPID 和 APPKEY 等参数，具体可参考 [离线推送(Android)](https://cloud.tencent.com/document/product/269/44516) 中的步骤一。
2. M 控制台配置：注册厂商通道需要传入自己的包名，各厂商填入的包名需保持一致，用于消息互通。具体可参考 [离线推送(Android)](https://cloud.tencent.com/document/product/269/44516) 中的步骤二。
3. 离线推送跳转界面，具体可参考 [离线推送(Android)](https://cloud.tencent.com/document/product/269/44516) 中的步骤三。
4. 厂商推送规则，具体可参考 [离线推送(Android)](https://cloud.tencent.com/document/product/269/44516) 中的步骤四。

>! [离线推送(Android)](https://cloud.tencent.com/document/product/269/44516) 中的步骤5~步骤8您不需要参考，TUICallKit 已经帮您完成了后续步骤。

## 步骤二：修改TUICalling工程配置
1. 修改`app/build.gradle` 的应用包名为自己的包名。
```
applicationId '您的应用包名'
```
2. 开`app/build.gradle`中的`plugin`注释，设置`ViVo`接入参数`VIVO_APPKEY`和`VIVO_APPID`。
```
manifestPlaceholders = [
      "VIVO_APPKEY": "",
      "VIVO_APPID" : ""
   ]
```
3. 检查项目级目录下`build.gradle`中的`Huawei`和`Goole(FCM)`的配置是否打开
   - 在项目级目录下添加华为厂商平台下载的`agconnect-services.json`文件
   - 在项目级目录下替换Google的`google-services.json`文件，该文件中的包名需与您的应用包名保持一致
4. 检查`PrivateConstants`文件中厂商参数是否配置正确。

完成以上步骤，运行`TUICalling`工程，您可以体验`TUICalling`离线唤起功能。

## 常见问题

### 1. 收不到通知

1. 用厂商控制台进行推送测试，能成功说明厂商通道没有问题。再检查`TUIOfflinePush`控制台厂商参数配置是否正确，按要求进行填写。（经测试：vivo x9必须在控制台配置消息类别）。
2. 部分手机收到通知会放到`不重要的通知`中，请下拉状态栏，检查是否归纳到`不重要的通知`中
3. 检查`TUIOfflinePush`注册是否成功，过滤以下日志：
```
TUIOfflinePush
```

### 2. 应用在后台时拉不起界面
Android手机由于厂商和平台的限制，在后台唤起界面需要开启`悬浮窗`权限或者`后台拉起界面`的权限，不同机型对权限的开放情况不完全相同。
例如：小米6只需`后台弹出界面`权限，但是红米需要同时打开`后台弹出界面`和`显示悬浮窗`权限。
可以在设置里面手动开启该权限。 开启权限的方法：打开手机设置，找到应用管理，找到您的应用，点击权限，点击悬浮窗并允许。

>? 如遇到该问题，需要做兼容处理，您可以加入我们下方的QQ群进行咨询与反馈~

### 3. 锁屏时无法点亮屏幕
Android手机由于厂商和平台的限制，在锁屏情况下需要不同的权限。请按以下情况进行排查。
**1. 确认打开厂商锁屏下通知权限**
   部分厂商统一做了约束，例如小米锁屏下离线通知到达时未亮屏：在设置-锁屏里，点击开关“锁屏来通知时亮屏”，打开开关。
**2. 确认打开应用锁屏通知权限**
   例如：小米 需要锁屏显示权限。

>？如遇到该问题，需要做兼容处理，您可以加入我们下方的QQ群进行咨询与反馈~

### 其他问题:

如有其他问题，欢迎加入 `TUI组件交流群:592465424` 一起交流及学习~