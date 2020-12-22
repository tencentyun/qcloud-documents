短视频 SDK License 用于激活短视频 SDK 的使用权限，用户可以在控制台上对短视频 SDK 进行新增、升级和续期。更多详细的短视频 SDK 功能说明，请参见 [短视频 UGSV](https://cloud.tencent.com/document/product/584/9366)。

## 购买正式版 License
当短视频测试版 License 试用28天到期后，请前往 [购买页](https://buy.cloud.tencent.com/vod?p=mp) 购买正式版 License。当您购买 [流量资源包10T](https://buy.cloud.tencent.com/vod)、[流量资源包50T](https://buy.cloud.tencent.com/vod)、[流量资源包200T](https://buy.cloud.tencent.com/vod) 中的任意规格，系统都会赠送对应版本的短视频 License 一个。您需要通过 [云点播控制台](https://console.cloud.tencent.com/vod/license/video) 将赠送的 License 与流量资源包绑定即可使用，方法请参见 [新增短视频 License](#.E6.96.B0.E5.A2.9E.E7.9F.AD.E8.A7.86.E9.A2.91-license)。该 License 有效期与流量资源包一致，支持升级、续期及变更等操作。

短视频 SDK License 版本与您所购买的云点播流量套餐包对应表如下：

| 短视频 SDK 版本 | 流量套餐包 |
|---------|---------|
| [精简版 SDK（UGC_Smart）](https://cloud.tencent.com/document/product/584/9366#sdk) |[云点播流量资源包10TB](https://buy.cloud.tencent.com/vod?t=ugsv&from=console-license-bottom-ugsv)| 
| [基础版 SDK（UGC）](https://cloud.tencent.com/document/product/584/9366#sdk) |[云点播流量资源包50TB或200TB](https://buy.cloud.tencent.com/vod?t=ugsv&from=console-license-bottom-ugsv) | 





## 新增短视频 License
您可通过购买点播流量资源包即可获赠短视频 SDK License（一年授权使用）。请参见 [点播流量资源包与短视频 SDK License 版本对应表](https://cloud.tencent.com/document/product/266/33149#.E7.9F.AD.E8.A7.86.E9.A2.91-sdk-license)。

### 步骤1：添加短视频 License
1. 进入 [短视频 License](https://console.cloud.tencent.com/vod/license) ，单击【新增 License】，进入短视频 License 新增页。
![](https://main.qcloudimg.com/raw/ff6252ca1182fb17682fb6c4891c36c2.png)
2. 请选择当前账户可用的资源包来绑定。若提示无可用资源包，请单击【[购买页](https://buy.cloud.tencent.com/vod?p=mp)】前往选购 [流量资源包10TB](https://buy.cloud.tencent.com/vod?p=mp)、[流量资源包50TB](https://buy.cloud.tencent.com/vod?p=mp) 或 [流量资源包200TB](https://buy.cloud.tencent.com/vod?p=mp) 中的任意一种。请参见 [点播流量资源包与短视频 SDK License 版本对应表](https://cloud.tencent.com/document/product/266/33149#.E7.9F.AD.E8.A7.86.E9.A2.91-sdk-license)。
![](https://main.qcloudimg.com/raw/0db35cf7b4722c4eebea35fb41ca6cf9.png)
3. 单击【确认并继续完成 License 设置】跳转到 License 设置页。

### 步骤2：绑定短视频 License
1. 请录入 App Name、Package Name 以及 Bundle ID。
![](https://main.qcloudimg.com/raw/4e431708c0e9043b98059cd136666700.png)
2. 单击【确定】即可。

>!**购买点播套餐包并绑定 License 后，请确认 [Bundle ID 和 Package Name]( https://cloud.tencent.com/document/product/266/50296#5.E3.80.81license-.E5.BA.94.E8.AF.A5.E5.A6.82.E4.BD.95.E7.A1.AE.E8.AE.A4.E7.BB.91.E5.AE.9A.E5.85.B3.E7.B3.BB.EF.BC.88android-.E7.9A.84-packagename-.E5.92.8C-ios-.E7.9A.84-bundleid.EF.BC.89.3F) 无误，一旦提交，License 信息不能再做修改。**

## 续期正式版 License
您可以在 [云点播控制台](https://console.cloud.tencent.com/vod/license) 查看 License 的有效期，正式版本的 License 有效期为一年。若您对指定 License 进行续期，请保证已购买流量资源包的情况下，操作如下：
1. 进入 [短视频 License](https://console.cloud.tencent.com/vod/license) ，选择将要续期的 License，单击右上角的【续期】，进入短视频 License 续期页。
2. 选择当前账户可绑定的资源包，**License 有效时间和对应的绑定资源包有效时间一致**。
![](https://main.qcloudimg.com/raw/60a091abeda3993222829f32898262a8.png)
3. 单击【确认续期】即可。

**示例**
用户在2019年02月02日购买流量资源包50TB的有效期为2019.02.02 - 2020.02.01，其赠送的短视频 SDK License 基础版有效期为2019.02.02 - 2020.02.01。
若用户需要进行续期，续期流量资源包200TB的有效期为2019.07.02 - 2020.07.01，其赠送的短视频 SDK License 基础版有效期为2019.07.02 - 2020.07.01。

## 升级正式版 License
目前仅支持短视频 License 由精简版升级至基础版，升级后的 License 为对应的资源包所赠送的 License 规格。请参见 [点播流量资源包与短视频 SDK License 版本对应表](https://cloud.tencent.com/document/product/266/33149#.E7.9F.AD.E8.A7.86.E9.A2.91-sdk-license)。

**示例**
若用户已购买流量资源包10TB（默认赠送短视频 License 精简版），如需从精简版 License 升级至基础版 License，则控制台需要存在50TB或200TB流量资源包以满足升级条件。

## 查看正式版 License
在 License 设置成功后稍等一段时间（依据网络情况而定），可以通过调用以下方法查看 License 信息。

- iOS：
```
NSLog(@"%@", [TXUGCBase getLicenceInfo]);
```
- Android：
```
TXUGCBase.getInstance().getLicenceInfo(context);
```


## License 使用方法
在调用 SDK 的相关接口前调用如下所示方法进行 License 的设置。

- iOS 建议在`- [AppDelegate application:didFinishLaunchingWithOptions:]`中添加：
```
[TXUGCBase setLicenceURL:LicenceUrl key:Key];
```
- Android 建议在 application 中添加：
```
TXUGCBase.getInstance().setLicence(context, LicenceUrl, Key);
```
