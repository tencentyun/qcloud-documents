短视频 SDK License 用于激活短视频 SDK 的使用权限，用户可以在控制台申请测试版短视频 License 或续期、查看等操作。

## 注意事项

- 首次申请测试版 License，**试用期为14天，可免费续期一次，合计28天**。
- 测试版 License 使用权限对应正式版短视频 SDK License 中的基础版，支持开放**短视频基础版 SDK** 能力，更多详细的功能说明请参见 [SDK 功能及对应的 License 版本](https://cloud.tencent.com/document/product/584/9368#sdk-.E5.8A.9F.E8.83.BD.E5.8F.8A.E5.AF.B9.E5.BA.94.E7.9A.84-license-.E7.89.88.E6.9C.AC)。



## 创建测试 License
1. 进入 [云点播控制台](https://console.cloud.tencent.com/vod/license)，左侧菜单中选择 【License 管理】 >【[短视频 SDK License](https://console.cloud.tencent.com/vod/license/video)】。
![](https://main.qcloudimg.com/raw/5d890d1d2d6f3ce5286317538c80246e.png)
2. 单击 【立即申请】，根据实际需求填写 App Name、Package Name 和 Bundle ID，单击【确定】。
![](https://main.qcloudimg.com/raw/8e6769fc04c34ba57678792bb4915d64.png)
3. 测试版 License 成功创建后，页面会显示生成的 License 信息。在 SDK 初始化配置时需要传入 Key 和 LicenseUrl 这两个参数，请妥善保存以下信息。
![](https://main.qcloudimg.com/raw/0ac6de97cc06ca5698718d18d3f08e17.png)

> ? 测试版 License 有效期内可单击右侧的【编辑】，进入修改 Bundle ID 和 Package Name 信息，单击【确定】即可保存。

## 续期测试版 License

您可以在 [云点播控制台](https://console.cloud.tencent.com/vod/license) 查看测试版 License 的有效期，测试版的 License 全程有效期为28天。当首次试用14天的测试版 License 临近到期，需对其续期1次，步骤如下：
1. 进入【[短视频 SDK License](https://console.cloud.tencent.com/vod/license/video)】页面，在试用版 License 区域，单击右上角的【续期】。
![](https://main.qcloudimg.com/raw/47338f81aa5cddda2e397c268a5ab414.png)
2. 弹框提示“续期成功”后，即完成测试版 License 续期14天操作。
![](https://main.qcloudimg.com/raw/bfc310e48f927b1d88e0eee5670b30d2.png)
>? 您的测试版 License 体验完28天后到期，请前往 [购买正式版 License](https://cloud.tencent.com/document/product/266/50290#.E8.B4.AD.E4.B9.B0.E6.AD.A3.E5.BC.8F.E7.89.88-license)。



## 升级测试版 Licnese
若您需将当前的测试版 License 升级为精简版 License/基础版 License，步骤如下：

1. 进入云点播控制台，选择 【License 管理】 >【[短视频 SDK License](https://console.cloud.tencent.com/vod/license/video)】。
2. 选择您的测试版 License，单击![](https://main.qcloudimg.com/raw/2e0a61cbd90bb3b25a44cb154b121afb.png)展开 License 信息，单击【升级到精简版/正式版】。
![](https://main.qcloudimg.com/raw/1bb66ca76ff6cfec114509b302040394.png)
3. 选择当前账户可绑定的资源包，单击【确定升级】。
![](https://main.qcloudimg.com/raw/4c6e9f4e653e020eb10a3fdfdcf6bb10.png)
>!  
> - 若无已购买资源包，请单击【购买页】前往选购流量资源包10TB、流量资源包50TB、流量资源包200TB中的任意一种。
> - 各规格资源包均有对应的 SDK License 版本，具体请参见 [价格总览](https://cloud.tencent.com/document/product/584/9368)。
3. 升级成功后，即可生成对应的正式版 License。
![](https://main.qcloudimg.com/raw/8f9ff0231e9fa0fdf677e0b6b1212409.png)
