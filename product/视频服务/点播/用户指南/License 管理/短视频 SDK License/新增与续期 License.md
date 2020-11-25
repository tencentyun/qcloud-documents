短视频 SDK License 用于激活短视频 SDK 的使用权限，用户可以在控制台上对短视频 SDK 进行新增、升级和续期。更多详细的短视频 SDK 功能说明，请参见 [ 短视频 UGSV](https://cloud.tencent.com/document/product/584/9366)。

## 申请测试版 License

您可以免费申请测试版 License（基础版 License，免费测试有效期为14天，可申请两次，共28天）体验测试，具体步骤如下：

### 步骤1：申请 License
 
1. 进入 [云点播控制台](https://console.cloud.tencent.com/vod/license)，左侧菜单中选择 【License 管理】 >【[短视频 SDK License](https://console.cloud.tencent.com/vod/license/video)】。
![](https://main.qcloudimg.com/raw/d7be56a797addeed6e3959b5ab7f3114.png)
2. 单击 【立即申请】，在 License 管理设置中，请填写对应 App Name、Package Name 以及 Bundle ID。
![](https://main.qcloudimg.com/raw/bdd927a3b000daebb8f4b3b758517764.png)
3. 单击【免费创建】即可。

 
### 步骤2：生成 License 信息
测试 License 成功创建后，页面会显示生成的 License 信息，这里需要记下 Key 和 LicenseUrl，在 SDK 的初始化时需要传入这两个参数。
![](https://main.qcloudimg.com/raw/1c181ff0fe99c93f9c01d09bd1b3ca65.png)

## 新增短视频 License

 ### 步骤1：购买 License
1. 进入 [短视频 License](https://console.cloud.tencent.com/vod/license)，单击【新增 License】，进入短视频 License 新增页。
![](https://main.qcloudimg.com/raw/a925a612f55ce6f0b9db96d541e0d6bf.png)
2. 选择当前账户可绑定的资源包。若无已购买资源包，请单击【购买页】前往选购 [流量资源包10TB](https://buy.cloud.tencent.com/vod)、[流量资源包50TB](https://buy.cloud.tencent.com/vod)、[流量资源包200TB](https://buy.cloud.tencent.com/vod) 中的任意一种。
![](https://main.qcloudimg.com/raw/07384dc91eca502e3ba77469ab2affeb.png)
3. 单击【确认并继续完成 License 设置】，进入 License 设置页。

### 步骤2：配置 License 信息
在 License 设置页填写对应的 App Name、Package Name 以及 Bundle ID，单击【确定】即可。
![](https://main.qcloudimg.com/raw/f4bc43f4f3220dfc493e9758afd2b4f8.png)

>? 创建成功后您可以在 [License 管理页](https://console.cloud.tencent.com/vod/license) 上查阅详细信息。

## 续期短视频 License

您可以在 [云点播控制台](https://console.cloud.tencent.com/vod/license) 查看 License 的有效期，正式版本的 License 有效期为一年。如您需要对指定的 License 续期，请确保已购买资源包的情况下，进行如下操作：
 ### 步骤1：进入续期页
进入【[短视频 License](https://console.cloud.tencent.com/vod/license)】，选择您需要续期的 License，单击右上角的【续期】，进入短视频 License 续期页。
 ### 步骤2：确认续租
选择当前账户可绑定的资源包，单击【确认续期】即可。
	![](https://main.qcloudimg.com/raw/5d1d551707a5a41e69f201ca00ef549d.png)
>?License 有效时间和对应的绑定资源包有效时间一致。
#### 示例

- 用户于2019-02-02购买 [流量资源包50TB](https://buy.cloud.tencent.com/vod) 的有效期为2019-02-02至2020-02-01，赠送基础版 License 有效期则为2019-02-02至2020-02-01。
- 若用户需要进行续期，续期流量资源包200TB的有效期为2019-07-02至2020-07-01，则 License 的有效期为2019-07-02至2020-07-01。
