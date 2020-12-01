移动直播 SDK 推荐配合腾讯云直播服务使用，购买指定直播流量资源包，即送移动直播基础版 License 1年使用权限，资源包与 SDK License 版本对应关系请参见 [价格总览](https://cloud.tencent.com/document/product/454/8008)。


## 测试版 License
### 申请测试版 License
您可以免费申请测试版 License（基础版，免费测试有效期为14天，可续期1次，共28天）体验测试，具体步骤如下：
1. 登录云直播控制台，在左侧菜单中选择 【直播 SDK】>[【License】](https://console.cloud.tencent.com/live/license)。
![](https://main.qcloudimg.com/raw/e16e131d2a235c6f902b9337da1742ec.png)
2. 单击【立即申请】，填写【Package Name】为 Android 的包名，【Bundle Id】为 iOS 的 Bundle ID。
![](https://main.qcloudimg.com/raw/47e2bdbf8b4c6f1bc5989f18a2817e69.png)
>? 若无 Package Name 或 Bundle Id，可填写“-”。
3. 单击【确定】。
 创建成功后，页面会显示生成的 License 信息。请记录 Key 和 LicenseUrl，便于在 SDK 初始化时使用。
![](https://main.qcloudimg.com/raw/06454ee5f8fa11377fadb67cd04a0291.png)

>?测试版 License 有效期内可单击右侧的【编辑】，进入修改 Bundle ID 和 Package Name 信息，单击【确定】即可保存。

### 续期测试版 License
测试版 License 初次申请默认有效期默认为14天，期满后您可续期**1次**，单击测试版 License 右侧的【编辑】进入修改界面，单击【确定】重新保存即可续期14天。
>! 测试版 License 有效期共28天，只能续期一次。若您需继续使用，请购买正式版 License。

<span id="buy"></span>
## 正式版 License
### 购买正式版 License
1. 购买指定规格的 [直播流量包](https://buy.cloud.tencent.com/mobilelive?urlctr=yes&basepack=10tb)，获得赠送1年有效期的正式直播基础版 License 使用权限，具体价格请参见 [价格总览](https://cloud.tencent.com/document/product/454/8008)。
![](https://main.qcloudimg.com/raw/d6a7bc7cc3594f980ee7f59278440b51.png)
2. 进入[【移动直播 License】](https://console.cloud.tencent.com/live/license) ，单击【新增License】按钮，选择已购买的流量包绑定有效期，并单击【确定并继续完成License设置】。
![](https://main.qcloudimg.com/raw/189744d9f0cb088c3b456c6c88a9f2f0.png)
>! **选择直播流量包仅用于直播基础版 License 绑定流量包的有效期，流量包的流量可用于当前账号所有 License 直播流量消耗。**
	例如，您的标准直播服务是日结流量计费，在2020年01月01日购买了10TB的直播流量包，为直播 App 创建了直播 License A；在2020年02月01日购买了50TB的直播流量包，为另一个直播 App 创建了直播 License B。
则 A 和 B 可共用60TB的流量，其中10TB流量包和 License A 都在2021年01月01日到期，50TB流量包和 License B 都在2021年02月01日到期。
4. 填写正式版 License 的信息，【Package Name】为 Android 的包名，【Bundle Id】为 iOS 的 Bundle ID。
5. 单击【确定】即可。
![](https://main.qcloudimg.com/raw/c52b885a82ca1f8ff2e58e0114831c99.png)
>?
>-  单击【确定】前需要再次确认 Bundle ID 和 Package Name，如与提交到商店的不一致请提前进行修改，**一旦提交成功将无法再修改 License 信息**。
>- **正式版 License 不支持信息修改**，若您需要修改 License 信息，购买资源包后请勿用于续期 License，请单击【新增 License】重新新增 License 绑定新的包名信息。



### 续期正式版 License
您可以登录 [移动直播 License](https://console.cloud.tencent.com/live/license) 页面查看 License 的有效期，若您的正式版 License 已到期，可进行如下操作进行续期：
1. 购买指定规格的 [直播流量包](https://buy.cloud.tencent.com/mobilelive?urlctr=yes&basepack=10tb)，赠送1年有效期的正式直播基础版 License 使用权限，具体价格请参见 [价格总览](https://cloud.tencent.com/document/product/454/8008)。
2. 进入[【移动直播 License】](https://console.cloud.tencent.com/live/license) ，选择您需续期的正式版 License，单击右侧的【续费】。
3. 选择已购买的流量包绑定有效期，单击【确定】即可。
![](https://main.qcloudimg.com/raw/22803f423ec8afc91ad6e19ab7535de3.png)
>! **选择流量包仅用于直播基础版 License 绑定流量包的有效期，流量包的流量可用于当前账号所有 License 直播流量消耗。**
	例如，您的标准直播服务是日结流量计费，在2020年01月01日购买了10TB的直播流量包，为直播 App 创建了直播License C；在2020年05月01日购买了50TB的直播流量包，则该流量包可用于新增 License D，或者将 License C 的有效期更新为2020年5月1日 - 2021年5月1日。


## 企业版 License
相比于专业版，企业版增加了基于腾讯优图实验室专利技术的人脸特效功能。使用企业版 License 可以开启优图实验室的 AI 功能，具体详情请参见 [美颜特效](https://cloud.tencent.com/product/x-magic)。
