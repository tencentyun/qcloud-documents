为支持视频播放的权限控制，腾讯云点播推出了防盗链的解决方案，支持 Referer 防盗链和 Key 防盗链两种类型。
## Referer 防盗链
1. 登录腾讯云 [点播控制台](https://console.cloud.tencent.com/video)。
2. 选择【分发播放设置】>【域名管理】。
3. 在目标域名所在行，单击【设置】，进入配置页面。
4. 单击【Referer防盗链】模块中的【编辑】，并开启【启用Referer防盗链】，配置以下选项：
 - 是否允许空 Referer：选择是否允许空 Referer 请求视频（即是否允许在浏览器中直接输入视频 URL 播放视频）。
 - 选择添加对象：选择黑名单或白名单，并填写域名。配置说明请查看 [注意事项](https://cloud.tencent.com/document/product/266/14046#referer)。
![](https://main.qcloudimg.com/raw/040def2f466235c943d2d94b60e32cfe.png)
5. 单击【确定】保存 Referer 防盗链配置，该配置在所有 CDN 节点生效大约需要5分钟。

## Key 防盗链
1. 登录腾讯云 [点播控制台](https://console.cloud.tencent.com/video)。
2. 单击【分发播放设置】>【域名管理】。
3. 在目标域名所在行，单击【设置】，进入配置页面。
4. 单击【Key防盗链】模块中的【编辑】，如下图所示：
 ![](https://main.qcloudimg.com/raw/a53061db324c8cbce895729210ad00cd.png)
5. 开启【启用Key防盗链】，单击【生成KEY】，如下图所示：
 ![](https://main.qcloudimg.com/raw/1b66a9481353e5fd9bfbaf3d6ea3e48e.png)
6. 单击【确定】保存配置，该配置在所有 CDN 节点生效大约需要5分钟。
