## 申请测试 License
您可以免费申请测试 License（基础版，免费测试有效期为14天，可续期1次，共28天）体验测试，具体步骤如下：
1. 登录云直播控制台，在左侧菜单中选择 [【直播 SDK】>【License】](https://console.cloud.tencent.com/live/license)。
![](https://main.qcloudimg.com/raw/e16e131d2a235c6f902b9337da1742ec.png)
2. 单击【立即申请】，填写【Package Name】为 Android 的包名，【Bundle Id】为 iOS 的 Bundle ID。
![](https://main.qcloudimg.com/raw/47e2bdbf8b4c6f1bc5989f18a2817e69.png)
3. 单击【确定】。
 创建成功后，页面会显示生成的 License 信息。请记录 Key 和 LicenseUrl，便于在 SDK 初始化时使用。
![](https://main.qcloudimg.com/raw/06454ee5f8fa11377fadb67cd04a0291.png)


<span id="buy"></span>
## 购买正式 License
1. 您可通过购买指定规格的 [直播流量包](https://buy.cloud.tencent.com/mobilelive?urlctr=yes&basepack=10tb)，赠送1年有效期的正式直播基础版 License 使用权限。具体价格请参见 [价格总览](https://cloud.tencent.com/document/product/454/8008)。
![](https://main.qcloudimg.com/raw/42b838a60f9ba786d1c0031db43790c3.png)
2. 进入[【移动直播 License】](https://console.cloud.tencent.com/live/license) ，单击【新增 License】按钮，选择已购买的流量包绑定有效期，并单击【确定并继续完成 License 设置】。
![](https://main.qcloudimg.com/raw/189744d9f0cb088c3b456c6c88a9f2f0.png)
>! 
>- **选择流量包仅用于直播基础版 License 绑定流量包的有效期，流量包的流量可用于当前账号所有 License 直播流量消耗。**
	例如：客户的标准直播服务是日结流量计费，在2020年01月01日购买了10TB的直播流量包，为直播 App 创建了直播 License A；在2020年02月01日购买了50TB的直播流量包，为另一个直播 App 创建了直播 License B。
则 A 和 B 可共用60TB的流量，其中10TB流量包和 License A 都在2021年01月01日到期，50TB流量包和 License B 都在2021年02月01日到期。
4. 填写正式版 License 的信息，【Package Name】为 Android 的包名，【Bundle Id】为 iOS 的 Bundle ID。
5. 单击【确定】即可。
![](https://main.qcloudimg.com/raw/c52b885a82ca1f8ff2e58e0114831c99.png)
>?
>-  单击【确定】前需要再次确认 Bundle ID 和 Package Name，如与提交到商店的不一致请提前进行修改，**一旦提交成功将无法再修改 License 信息**。
>- 若您需要修改 License 信息，购买资源包后请勿用于续期 License，正式 License 不支持信息修改，请单击【新增 License】按钮重新新增 License 绑定新的包名信息。


## 续期正式 License
1. 您可通过购买指定规格的 [直播流量包](https://buy.cloud.tencent.com/mobilelive?urlctr=yes&basepack=10tb)，赠送1年有效期的正式直播基础版 License 使用权限。具体价格请参见 [价格总览](https://cloud.tencent.com/document/product/454/8008)。
2. 进入[【移动直播 License】](https://console.cloud.tencent.com/live/license) ，选择您需续费的正式版 License，单击右侧的【续费】。
3. 选择已购买的流量包绑定有效期，单击【确定】即可。
![](https://main.qcloudimg.com/raw/22803f423ec8afc91ad6e19ab7535de3.png)
>! 
>- **选择流量包仅用于直播基础版 License 绑定流量包的有效期，流量包的流量可用于当前账号所有 License 直播流量消耗。**
	例如：客户的标准直播服务是日结流量计费，在2020年01月01日购买了10TB的直播流量包，为直播 App 创建了直播License C；在2020年05月01日购买了50TB的直播流量包，则该流量包可用于新增 License D，或者将 License C 的有效期更新为2020年5月1日 - 2021年5月1日。




<span id="config"></span>
## 配置 License

在调用 SDK 的相关接口前，您需要调用如下方法配置 License：

- iOS
 建议在 `[AppDelegate application:didFinishLaunchingWithOptions:]` 中添加：
```
[TXLiveBase setLicenceURL:LicenceUrl key:Key];
```
- Android
 建议在 application 中添加：
```
TXLiveBase.getInstance().setLicence(context, LicenceUrl, Key);
```

##  查看 License 信息
License 设置成功后（需稍等一段时间，具体时间长短依据网络情况而定），您可以通过调用以下方法查看 License 信息：

- iOS
```
NSLog(@"%@", [TXLiveBase getLicenceInfo]);
```
- Android
```
TXLiveBase.getInstance().getLicenceInfo();
```

## License 的有效期与续费

您可以登录 [移动直播 License](https://console.cloud.tencent.com/live/license) 页面查看 License 的有效期，
正式版 License 有效期一般为一年。License 到期后您可以在 [移动直播套餐选购](https://buy.cloud.tencent.com/mobilelive?urlctr=yes&basepack=10tb)  页面再次购买。

## 企业版 License
相比于专业版，企业版增加了基于腾讯优图实验室专利技术的人脸特效功能。使用企业版 License 可以开启优图实验室的 AI 功能，更多详情请参见 [美颜特效](https://cloud.tencent.com/product/x-magic)。
使用企业版本 License 时，License 设置方法同 [配置 License](#config)，但工程需要额外进行配置，具体操作请参见：
- [AI 变脸和挂件（iOS）](https://cloud.tencent.com/document/product/454/9018) 
- [AI 变脸和挂件（Android）](https://cloud.tencent.com/document/product/454/9020)

## License 常见问题

### 测试 License 到期后是否可以延期？
测试 License 试用期最多28天，不支持延期，到期后请尽快 [购买正式 License](#buy)。

### 测试 License 能否更改 Android 的 Package Name 和 iOS 的 Bundle ID?
测试 License 能更改 Android 的 Package Name 和 iOS 的 Bundle ID。具体操作：登录控制台，单击测试 License 信息右侧的【编辑】，进入编辑页面即可修改 Android 的 Package Name 和 iOS 的 Bundle ID。

### 正式 License 能否更改 Android 的 Package Name 和 iOS 的 Bundle ID?
正式 License 不能更改 Package Name 和 Bundle ID。

### License 可以同时支持多个 App 吗？
一个 License 只能对应一个 Package Name 和一个 Bundle ID，若多个 App 使用 SDK 功能，需要购买多个资源包新增多个License。
