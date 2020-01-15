## 操作场景
直播播放默认通过源码率输出，如果您需要对播放码率进行限制或者设定，可以在转码配置中进行设置。
## 前提条件
已登录 [云直播控制台](https://console.cloud.tencent.com/live)。

## 操作步骤
1. 进入[【域名管理】](https://console.cloud.tencent.com/live/domainmanage)，单击【管理】或需配置的播放域名进入域名管理。
2. 在【模板配置】，查看【录制配置】标签。
3. 单击【编辑】可以选择不同的转码配置模板，为该域名下播放地址指定模板设置的编译方式和码率。
4. 单击【保存】即可。

>>! 
>- 模板配置完后约5分钟 - 10分钟生效。
>- 转码配置模板需要先在 [转码配置](https://cloud.tencent.com/document/product/267/20385) 中创建转码，创建成功后即可在此选择。

![](https://main.qcloudimg.com/raw/33d4edfe69c52c85ac0e82840ab5275a.png)

4. 配置转码模板后，播放 URL 需增加转码模板名称，拼接方式为：`播放地址_转码模板名称`，若未拼接转码模板名称，则播放的为原始直播流内容。
	>例如：原播放地址为`http://domain/AppName/StreamName.flv` ，domain 关联的转码模板名称为 `_hd`。
	>则获取播放转码后的视频，转码播放地址为`http://domain/AppName/StreamName_hd.flv`。

>?如果您需要解绑转码配置，在【模板配置】中，单击【编辑】，取消相应模板的勾选，然后单击【保存】，即可将该模板与域名取消关联。
>![](https://main.qcloudimg.com/raw/4ccc073e94e3afb43dcfd28cb144b029.png)
