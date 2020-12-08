<span id="que1"></span>
### 续期 License 时出现“license not exist”问题，如何解决？

您可登录【云点播控制台】>[【短视频 SDK License】](https://console.cloud.tencent.com/vod/license/video)根据以下方式排查：
1. 请确认是否在**管理员**页面进行 License 绑定续期。
![](https://main.qcloudimg.com/raw/cb24259d7a672db11bb1ce68f3341390.png)
2. 如果您是在**非管理员**页面下进行操作，请单击 [提交工单](https://console.cloud.tencent.com/workorder/category) ，由腾讯云点播协助您进行 License 变更操作。

<span id="que2"></span>
### License 无法添加/新增，如何解决？
- 确认是否有可绑定的资源包。进入【云点播控制台】>【[资源包](https://console.cloud.tencent.com/vod/assets/packages)】，确认您的账号下是否有可绑定的点播流量 10T、50T 或 200T 资源包中的一种。
- 查看绑定页面是否为**管理员**页面，请选择管理员页面进行绑定。

<span id="que3"></span>
### License 校验失败，如何排查？
建议您可以参考以下几点进行排查：
- 确认您的 License 是否在有效期内。
- 确认 License 信息里的 Package Name 是否与项目里面的包名一致。
- 确认 License 中的 LicenseUrl 协议是否为 HTTPS。

>? 若上述方法无法解决您的问题，建议**卸载应用重新安**装或 [提工单](https://console.cloud.tencent.com/workorder/category) 解决。 

