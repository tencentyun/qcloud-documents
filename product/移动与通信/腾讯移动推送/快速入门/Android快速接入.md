## 简介
在您完成创建产品和 Android 应用之后，可在 [控制台](https://console.cloud.tencent.com/tpns) 处下载配置文件快速接入 SDK，只需四步即可完成推送功能配置，简化接入流程，集成更便捷快速。
## 接入前准备
1. 接入 SDK 之前，需要您前往腾讯移动推送 [控制台](https://console.cloud.tencent.com/tpns) 创建产品和 Android 应用，详细操作可参考 [创建产品和应用](https://cloud.tencent.com/document/product/548/37241) 文档。
2. 应用创建完成后，您可以参考 [申请试用](https://cloud.tencent.com/document/product/548/37241#.E7.94.B3.E8.AF.B7.E8.AF.95.E7.94.A8) / [购买推送服务](https://cloud.tencent.com/document/product/548/37242) 操作文档，为当前应用申请试用权限或者购买推送服务。
3. 完成以上步骤后，前往【产品管理】>【配置管理】页面，点击【配置文件下载】按钮。

![](https://main.qcloudimg.com/raw/78ac01a937d3f11d644ea6146d73a57d.png)
## 配置工程文件
1. 在【配置管理】页面中，单击【快速接入】按钮。
![](https://main.qcloudimg.com/raw/2966b56bb7b6ed808ce34bd19a3c1e4b.png)
2.按照接入指引的操作顺序完成配置，然后点击验证按钮。
![](https://main.qcloudimg.com/raw/7c4cf6eddf838d55a4dfa858ac3d6e3f.png)

3.若出现以下提示，则表示 SDK 接入成功 。
![](https://main.qcloudimg.com/raw/393d62182039f2164517d18b86cdb52a.png)
 - 若出现以下提示，请确认该应用是否开通试用或购买了推送服务。
![](https://main.qcloudimg.com/raw/3c4f5f962bcb07d1383d5b114b8ac15b.png)
 - 若出现以下提示，请确认 App 是否成功注册推送服务，可参考下文 [集成结果验证](#jichengyanzheng) 排查。
![](https://main.qcloudimg.com/raw/ca917f75ce29160e549df5c50876ee00.png)

<span id="jichengyanzheng"></span>
## 集成结果验证
1. 运行 App，过滤"TPush"关键字，查看相关日志：
![](https://main.qcloudimg.com/raw/3534e6c05ab9f6959e6e19d4272dc48b.png)
如出现有类似上图日志，则表明 TPNS-SDK 的插件集成方式已经成功。

2. 推送服务注册成功的日志如下：
```
XG register push success with token:6ed8af8d7b18049d9fed116a9db9c71ab44d5565
```
若未搜索到 Token，请查看注册接口返回的错误码，根据 [错误码对照表](https://cloud.tencent.com/document/product/548/36660) 排查。

## 问题排查指引
1. 插件日志
如果集成出现异常，则将 tpns-configs.json 文件中的  "debug" 字段置为 true，运行命令： 
```
./gradlew --rerun-tasks :app:processReleaseManifest 
```
并通过 "TpnsPlugin" 关键字进行分析
2. sync projects。
![](https://main.qcloudimg.com/raw/30368ed3cb4a25f3c33be46e3c1f2f5d.png)
3. 在项目的 External Libraries 中查看是否有相关依赖。
![](https://main.qcloudimg.com/raw/1de82d05f351939883e1870ae7300c44.png)
