短视频 License 用于解锁短视频（精简版/基础版）模块的使用权限，您可以在 [腾讯云视立方控制台](https://console.cloud.tencent.com/vcube) 对短视频 License 进行新增、升级和续期等操作。更多详细的短视频 SDK 功能说明，请参见 [短视频 SDK](https://cloud.tencent.com/document/product/584/9366)。


[](id:test)
## 测试版 License
[](id:creat_test)
### 申请测试版 License

您可以免费申请短视频模块基础版的测试版 License（免费测试有效期为14天，可续期1次，共28天，有效期至到期次日00:00:00为止）体验测试，具体步骤如下：

1. 登录【[腾讯云视立方控制台](https://console.cloud.tencent.com/vcube)】，单击【创建测试 License】。
![](https://main.qcloudimg.com/raw/a623b59b4989ef4d713fc5a2e13927c1.png)
2. 根据实际需求填写 App Name、Package Name 和 Bundle ID，勾选功能模块【短视频】，单击【确定】。
![](https://main.qcloudimg.com/raw/3127c6c454fecae07709f4a82fb41089.png)
3. 测试版 License 成功创建后，页面会显示生成的 License 信息。在 SDK 初始化配置时需要传入 Key 和 License URL 两个参数，请妥善保存以下信息。
![](https://main.qcloudimg.com/raw/149d2109ce77f419b9a154bbcd2ceb63.png)

>? 
>- 测试版 License 有效期内可单击右侧的【编辑】，进入修改 Bundle ID 和 Package Name 信息，单击【确定】即可保存。
>- 若无 Package Name 或 Bundle Id，可填写“-”。


[](id:renew)
### 续期测试版 License

测试版 License 初次申请默认有效期默认为14天，期满后您可续期**1次**。单击功能模块【短视频】右侧的【续期】按钮，选择【确定续期】即可续期该功能模块14天。
![](https://main.qcloudimg.com/raw/42d1eca5dbb43c767b74c49827b73319.png)
>! 测试版 License 有效期共28天，只能续期一次（有效期至到期次日00:00:00为止）。若您需继续使用，请 [购买](https://buy.cloud.tencent.com/vcube) 正式版 License。

[](id:update_test)
### 测试版 License 升级
若您需要将短视频测试版 License 升级成为短视频正式版 License，获得一年的有效的使用期。具体操作如下：

1. 单击测试版 License 短视频模块中的【升级】。
![](https://main.qcloudimg.com/raw/ebe73ffad274284a31ff63d104edac51.png)
2. 进入升级功能模块界面，选择需要绑定的云点播流量资源包，单击【确定】即可升级到短视频（精简版/基础版）的正式版 License。
![](https://main.qcloudimg.com/raw/ce167424d536f3b051a4d3c72be5adb6.png)

>!
> - 短视频测试版 License 升级为**短视频精简版**的正式版 License 仅支持选择 10TB 规格的云点播流量资源包。
> - 短视频测试版 License 升级为**短视频基础版**的正式版 License 可选择 50TB、200TB、1PB 规格的云点播流量资源包。
