短视频 SDK License 用于激活短视频 SDK 的使用权限，用户可以在控制台上对短视频 SDK 进行新增、升级和续期。更多详细的短视频 SDK 功能说明，请参见 [短视频 UGSV](https://cloud.tencent.com/document/product/584/9366)。

## 购买正式版 License
当测试版 License 试用28天到期后，请前往 [云点播控制台](https://console.cloud.tencent.com/vod/license) 购买正式版 License。当您购买 [流量资源包10T](https://buy.cloud.tencent.com/vod)、[流量资源包50T](https://buy.cloud.tencent.com/vod)、[流量资源包200T](https://buy.cloud.tencent.com/vod) 中的任意规格，系统都会赠送对应短视频 License 一个。您需要通过 [云点播控制台](https://console.cloud.tencent.com/vod/license/video) 将此 License 与流量资源包绑定即可创建成功，其有效期与流量资源包一致，支持升级、续期以及变更等操作。

短视频 SDK License 版本与您需要购买的云点播套餐包对应关系如下：

| 短视频 SDK 版本 | 套餐包 |
|---------|---------|
| [精简版 SDK（UGC_Smart）](https://cloud.tencent.com/document/product/584/9366#sdk) |[云点播流量资源包 10TB](https://buy.cloud.tencent.com/vod?t=ugsv&from=console-license-bottom-ugsv)| 
| [基础版 SDK（UGC）](https://cloud.tencent.com/document/product/584/9366#sdk) |[云点播流量资源包50TB或200TB](https://buy.cloud.tencent.com/vod?t=ugsv&from=console-license-bottom-ugsv) | 
| [企业版 SDK（UGC_Enterprise）](https://cloud.tencent.com/document/product/584/9366#sdk) |[参见申请企业版本 License](#enterpriseli) | 
| [企业版 Pro SDK（EnterprisePro）](https://cloud.tencent.com/document/product/584/9366#sdk) |[参见申请企业版本 License](#enterpriseli) | 

>!**购买点播套餐包并绑定 License 后，请确认 [Bundle ID 和 Package Name](https://cloud.tencent.com/document/product/266/49972#que5) 无误，一旦提交，License 信息不能再做修改。**


## 新增短视频 License
开通云点播服务后，通过购买点播流量资源包可获取短视频 SDK License（一年授权使用） 。请参见 [点播流量资源包与短视频 SDK License 对照表](https://cloud.tencent.com/document/product/266/33149#.E7.9F.AD.E8.A7.86.E9.A2.91-sdk-license)。

### 步骤1：添加短视频 License
1. 进入 [短视频 License](https://console.cloud.tencent.com/vod/license) ，单击【新增 License】，进入短视频 License 新增页。
![](https://main.qcloudimg.com/raw/ff6252ca1182fb17682fb6c4891c36c2.png)
2. 请选择当前账户可用的资源包来绑定。若提示无可用资源包，请单击【购买页】前往选购流量资源包10TB、流量资源包50TB或流量资源包200TB中的任意一种。请参见 [点播流量资源包与短视频 SDK License 对照表](https://cloud.tencent.com/document/product/266/33149#.E7.9F.AD.E8.A7.86.E9.A2.91-sdk-license)。
![](https://main.qcloudimg.com/raw/0db35cf7b4722c4eebea35fb41ca6cf9.png)
3. 单击【确认并继续完成 License 设置】跳转到 License 设置页。

### 步骤2：绑定短视频 License
1. 请录入 App Name、Package Name 以及 Bundle ID。
![](https://main.qcloudimg.com/raw/4e431708c0e9043b98059cd136666700.png)
2. 单击【确定】即可。

>! 正式版 License 一经绑定不能再做修改。

## 续期正式版 License
您可以在 [云点播控制台](https://console.cloud.tencent.com/vod/license) 查看 License 的有效期，正式版本的 License 有效期为一年。若您对指定 License 进行续期，请保证已购买流量资源包的情况下，操作如下：
1. 进入 [短视频 License](https://console.cloud.tencent.com/vod/license) ，选择您需要续期的 License，单击右上角的【续期】，进入短视频 License 续期页。
2. 选择当前账户可绑定的资源包，**License 有效时间和对应的绑定资源包有效时间一致**。
![](https://main.qcloudimg.com/raw/60a091abeda3993222829f32898262a8.png)
3. 单击【确认续期】即可。

**示例**
用户在2019年02月02日购买流量资源包50TB的有效期为2019.02.02 - 2020.02.01，其赠送的短视频基础版 SDK License 有效期为2019.02.02 - 2020.02.01。
若用户需要进行续期，续期流量资源包200TB的有效期为2019.07.02 - 2020.07.01，其赠送的短视频基础版 SDK License 有效期为2019.07.02 - 2020.07.01。

## 升级正式版 License
目前仅支持短视频 License 由精简版升级至基础版，升级的 License 为对应的资源包赠送的 License 规格。请参见 [点播流量资源包与短视频 SDK License 对照表](https://cloud.tencent.com/document/product/266/33149#.E7.9F.AD.E8.A7.86.E9.A2.91-sdk-license)。

**示例**
用户已购买流量资源包10TB（赠送精简版 License），如需从精简版 License 升级至基础版 License，则控制台需要存在50TB或200TB流量资源包以满足升级条件。

短视频 SDK License 用于激活短视频 SDK 的使用权限，用户可以在控制台申请测试版短视频License 或续期、查看等操作。更多详细的短视频 SDK 功能说明，请参见 [短视频 UGSV](https://cloud.tencent.com/document/product/584/9366)。

## 查看正式版 License
在 License 设置成功后稍等一段时间（依据网络情况而定），可以通过调用以下方法查看 License 信息。

- iOS：
```
NSLog(@"%@", [TXUGCBase getLicenceInfo]);
```
- Android：
```
TXUGCBase.getInstance().getLicenceInfo(context);

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

## 申请测试版 License
您可以申请测试版 License 免费体验各项功能，其使用权限对应正式版短视频 SDK License 中的基础版。首次申请试用14天，可免费续期一次，合计28天。请参见 [点播流量资源包与正式版短视频 SDK License 对照表。](https://cloud.tencent.com/document/product/266/33149#.E7.9F.AD.E8.A7.86.E9.A2.91-sdk-license)申请步骤如下：

### 步骤1：创建测试 License
1. 进入 [云点播控制台](https://console.cloud.tencent.com/vod/license)，左侧菜单中选择 【License 管理】 >【[短视频 SDK License](https://console.cloud.tencent.com/vod/license/video)】。
![](https://main.qcloudimg.com/raw/ebf58d7dcc70e2fa3db512d55f69686f.png)
2. 单击 【立即申请】跳转到 License 设置页，请录入 App Name、Package Name 以及 Bundle ID。
![](https://main.qcloudimg.com/raw/623c6e65bf01922ff98436fa4d6e05bf.png)
3. 单击【免费创建】即可。

### 步骤2：保存测试  License
当免费测试版 License 成功创建后，页面会显示生成的 License 信息，在 SDK 初始化配置时需要传入 Key 和 LicenseUrl 这两个参数，请妥善保存以下信息。
![](https://main.qcloudimg.com/raw/47e51c894db9d9f75b9a91c138a88920.png)


## 续期测试版 License
您可以在 [云点播控制台](https://console.cloud.tencent.com/vod/license) 查看测试版 License 的有效期，测试版的 License 全程有效期为28天。当首次试用14天的测试版 License 临近到期，需对其续期1次，步骤如下：
### 步骤1：申请续期 License
进入【[短视频 SDK License](https://console.cloud.tencent.com/vod/license/video)】页面，在试用版 License 区域，单击右上角的【续期】。
![](https://main.qcloudimg.com/raw/089a73cd3619a2633184e343da0e1835.png)
### 步骤2：完成续期 License
弹出气泡提示续期成功后，随即右上角的【续期】 消失，便完成测试版 License 续期14天的操作。
![](https://main.qcloudimg.com/raw/b1a65e43cbf6360ee23bd140dba53c2d.png)
>?您的测试版 License 体验完28天后到期，请前往 [购买正式版 License](https://buy.cloud.tencent.com/vod)。

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
