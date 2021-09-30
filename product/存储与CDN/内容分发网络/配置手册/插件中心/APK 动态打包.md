## 功能介绍

APK 动态打包插件功能识别终端用户请求 URL 中的特定参数，在 CDN 边缘将该参数携带的信息动态地写入 APK ，实现在 CDN 边缘对 APK 进行动态打包。APK 动态打包要求使用腾讯云 COS 作为源站。

>? 
>- APK 动态打包为内测功能， 您可以 [提交申请表](https://cloud.tencent.com/apply/p/1qkg1qkomyyj) 申请试用。如果您已经提交申请，我们将在5个工作日内对您的申请进行审核。
>- 当前仅中国境内节点支持 APK 动态打包功能。


## 适用场景

- App 多渠道投放，如应用市场、网盟、搜索引擎、效果广告，但又不希望手工维护成千上百的渠道包。
- App 热启动，在 APK 包动态插入链接，实现 App 首次激活启动，自动跳转至指定页面。

## 使用流程

1. 登录 CDN 控制台在插件中心中，完成 APK 动态打包插件功能的相关配置。
2. 上传原始 APK 至 COS 源站指定上传目录。
3. 等待 CDN 节点将母包处理完成。
4. 终端用户发起带参数的请求。
5. CDN 边缘返回动态打包之后的 APK 文件。

![](https://main.qcloudimg.com/raw/b26dede3d5ba4947bb5645c4db81f741.png)

## 配置指南

### 步骤一：新增动态打包配置
登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在菜单栏里选择【插件中心】，单击 APK 动态打包插件功能卡片的开关按钮，开通 APK 动态打包，即可进入配置新增页面。功能开通之后，可以通过卡片底部的【基础配置】、【用量统计】进入相应的配置列表和用量查看页面。
![](https://main.qcloudimg.com/raw/1c8a690040b028e7913376d22bf0dccd.png)
- 存储桶选择：选择 COS 源站。本功能必须使用 **北京/上海/广州/成都** 的 COS 作为源站。
- 生效域名：系统将自动全选采用该 COS 作为源站的域名，该域名用于发布 APK 。可自行增删。
- 上传目录：设置原始 APK 在 COS 上的上传目录。配置完成后，需手动上传原始APK至该目录。
- 输出目录：设置 CDN 节点处理完母包之后的输出目录。上传原始 APK 后，系统会自动处理、生成同名母包，并将母包上传至该目录。**构造请求 URL 时，请将用户请求指向该目录**，而非上传目录。
- 签名方式：当前支持对采用 Android V1/V2 签名方式的 APK 进行动态打包，V2签名支持 WALLE/VASDOLLY 等开源多渠道打包方案。同时支持将注释信息写入指定的自定义 Block ID。
- 渠道参数：固定为 `comment`，不可修改。
- 云函数配置：授权之后，系统将根据配置自动生成云函数。

>!请不要在 SCF 控制台删除该云函数！




### 步骤二：上传原始 APK

登录 [COS 控制台](https://console.cloud.tencent.com/cos5) ，并上传原始 APK 到指定的上传目录

>?原始 APK 大小不可超过10GB。


### 步骤三：等待母包处理完成

在 APK 动态打包功能页，单击【母包状态】查看 CDN 节点对母包的处理进展。
![](https://main.qcloudimg.com/raw/88450f16367a81e7c977a339f1de5b1f.png)

### 步骤四：发布动态打包 URL

母包处理完毕后，即可发布动态打包 URL。具体示例如下：

```
存储桶：example.cos.ap-chengdu.myqcloud.com
生效域名：www.example.com
上传目录：/src
输出目录：/ext
渠道参数：comment
渠道名称：pipeline
apk名称：test.apk
```

则对应发布的 URL 为：`https://www.example.com/ext/test.apk?comment=pipeline`。

用户请求该 URL，即可获得 CDN 边缘写入 `pipeline` 渠道信息之后的 APK 包。

## 费用说明

- APK 动态打包属于收费功能，具体费用说明请联系您的腾讯云客户经理索取。
- APK 采用 SCF 触发母包处理任务，超过 SCF 免费试用额度可能会产生云函数费用，具体请见 [SCF免费额度](https://cloud.tencent.com/document/product/583/12282) 。

