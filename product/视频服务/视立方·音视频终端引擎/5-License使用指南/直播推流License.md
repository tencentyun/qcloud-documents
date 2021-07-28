直播推流 License 用于解锁直播推流（RTMP + RTC）模块的使用权限，您可以在 [视立方控制台 ]() 对直播推流 License 进行新增和续期等操作。


[](id:test)
## 测试版 License
[](id:creat_test)
### 申请测试版 License
您可以免费申请直播推流模块的测试版 License（免费测试有效期为14天，可续期1次，共28天，有效期至到期当日的24:00:00为止）体验测试，具体步骤如下：

1. 登录 [视立方控制台]()，单击【创建测试License 】。
![](https://main.qcloudimg.com/raw/11f0a5770a347054652e50773392661b.png)
2. 根据实际需求填写 `App Name`、`Package Name` 和 `Bundle ID`，勾选功能模块【直播推流】，单击【确定】。
![](https://main.qcloudimg.com/raw/cc3c2c51e90cc064dfd34675c0152439.png)
3. 测试版 License 成功创建后，页面会显示生成的 License 信息。在 SDK 初始化配置时需要传入 Key 和 License URL 两个参数，请妥善保存以下信息。
![](https://main.qcloudimg.com/raw/a607509d59a4e244bd4cd2dfd13b6781.png)

>? 
>- 测试版 License 有效期内可单击右侧的【编辑】，进入修改 Bundle ID 和 Package Name 信息，单击【确定】即可保存。
>- 若无 Package Name 或 Bundle Id，可填写“-”。

[](id:renew_test)
### 续期测试版 License
测试版 License 初次申请默认有效期默认为14天，期满后您可续期**1次**，单击功能模块【直播推流】右侧的【续期】，选择【确定续期】即可续期该功能模块14天。
![](https://main.qcloudimg.com/raw/b3cf592b44775dbc416c2b65d68ed1c0.png)

> ? 测试版 License 有效期共28天，**只能续期一次**（有效期至到期当日的24:00:00为止）。若您需继续使用，请购买 [正式版 License](#formal)。


[](id:formal)
## 正式版 License
[](id:creat_formal)
### 购买正式版 License
1. 购买指定规格的 [直播流量包](https://cloud.tencent.com/document/product/1449/56973?!preview&!editLang=zh#live)，获得赠送1年有效期的正式直播推流 License 使用权限（到期当日的00:00:00止）。
2. 进入 [视立方控制台]()，单击【创建应用并绑定 License 】按钮。填写 `App Name`、`Package Name` 和 `Bundle ID` 并勾选功能模块【直播推流】，完成后单击【下一步】。
![](https://main.qcloudimg.com/raw/e6c80bea7a024b9a5390e36556db6aee.png)
3. 进入选择套餐包并绑定 License 界面，选择**未绑定**的直播流量资源包，并单击【确定】即可生成正式版 License。
![](https://main.qcloudimg.com/raw/9677fe7faf19515fb01b8b62daf24ead.png)
>!
> - 单击【确定】前需要再次确认 Bundle ID 和 Package Name，如与提交到商店的不一致请提前进行修改，**一旦提交成功将无法再修改 License 信息**。
> - **选择直播流量包仅用于直播基础版 License 绑定流量包的有效期，流量包的流量可用于当前账号所有 License 直播流量消耗。**
4. 正式版 License 成功创建后，页面会显示生成的正式版 License 信息。在 SDK 初始化配置时需要传入 Key 和 License URL 两个参数，请妥善保存以下信息。
![](https://main.qcloudimg.com/raw/1880ec213b2c8deadbdb65ec672e8b55.png)


[](id:update_formal)
### 更新正式版 License 有效期
您可以登录 [视立方控制台]() 页面查看直播推流正式版 License 的有效期，若您的直播推流正式版 License 已到期，可进行如下操作进行续期：
1. 选择您需要更新有效期的 License，单击直播推流模块内的【更新有效期】。
![](https://main.qcloudimg.com/raw/9685ce96bb720cc91e5cb0038133c2c3.png)
2. 选择**未绑定**过的直播流量资源包（若没有可绑定的资源包，可前往 [资源包购买页]() 购买），单击【确定】即可。
![](https://main.qcloudimg.com/raw/ae487b6af9a14632609d42edf5e26ad6.png)
3. 查看更新后的有效期情况。
>! **直播推流正式版 License 不支持信息修改**，若您需要修改 License 信息，购买资源包后请勿用于 License 有效期的更新，请单击【新增 License】重新新增 License 绑定新的包名信息。

