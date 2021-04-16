
## 操作场景

以 [QQ 小程序开发者工具](https://q.qq.com/wiki/#_4-) 为例，本文介绍使用游戏联机对战引擎 MGOBE API 快速接入对战平台的方法，实现一个 MGOBE 的 Hello World 项目。


## 前提条件

- 已在游戏联机对战引擎控制台创建游戏，并开通联机对战服务，您可参考 [开通服务](https://cloud.tencent.com/document/product/1038/33299)。
- 已获取游戏 gameID 和 secretKey，您可在游戏概览的基本信息里查看。

## 操作步骤

1. 打开 QQ 小程序开发者工具，创建一个小游戏项目。
2. 选择项目目录和建立模板，填写项目名称和 AppID（如无 AppID，可先使用测试号），如下图所示：
   ![create_lib](https://main.qcloudimg.com/raw/1f5bfddfbb751eb4c15fb240718c8dbe.jpg)
3. 在编辑页面，选择【详情】，勾选【不校验合法域名、web-view（业务域名）、TLS 版本以及 HTTPS 证书】，关闭域名校验。如下图所示：
   ![create_lib](https://main.qcloudimg.com/raw/f153098d36d2d837cbfcfe0ca93d6e79.png)
4. 后续步骤请参考 [QQ 小游戏开发文档](https://q.qq.com/wiki/)，使用 QQ 小程序开发者工具创建游戏。


>?其他平台具体步骤请参考： [Cocos Creator](https://docs.cocos.com/creator/manual/zh/getting-started/hello-world.html) 和 [LayaAir](https://ldc2.layabox.com/doc/?nav=zh-ts-1-0-2)。

