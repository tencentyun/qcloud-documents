## 功能介绍

APK 动态打包插件功能识别终端用户请求 URL 中的特定参数，在 CDN 边缘将该参数携带的	信息动态地写入 APK ，实现在 CDN 边缘对 APK 进行动态打包。

> ? 
>+ 当前仅中国境内节点支持 APK 动态打包功能。
>+ 当前仅支持腾讯云 COS 作为源站的 APK 动态打包。
## 适用场景

- App 多渠道投放，如应用市场、网盟、搜索引擎、效果广告，但又不希望手工维护成千上百的渠道包。
- App 热启动，在 APK 包动态插入链接，实现 App 首次激活启动，自动跳转至指定页面。

## 使用流程

1. 登录 CDN 控制台在插件中心中，完成 APK 动态打包插件功能的相关配置。
2. 上传原始 APK 至 COS 源站指定上传目录。
3. 等待 CDN 节点将母包处理完成。
4. 终端用户发起带参数的请求。
5. CDN 边缘返回动态打包之后的 APK 文件。

![](https://main.qcloudimg.com/raw/a954c54bcc94403ad6bfd788bf1c1a48.png)

## 配置指南

### 步骤一：新增动态打包配置

1. 登录 [CDN 控制台](https://console.cloud.tencent.com/cdn)，在菜单栏里选择插件中心，单击**APK 动态打包**插件功能卡片的开关按钮，开通 APK 动态打包，即可进入配置新增页面。
2. 功能开通之后，可以通过卡片底部的**基础配置、用量统计**进入相应的配置列表和用量查看页面。
3. 在基础配置页面，单击**新增配置**，完成对 APK 打包任务的配置。
![](https://qcloudimg.tencent-cloud.cn/raw/f6be79a8d49641662c6afbf0baf78d05.png)
	- 存储桶选择：选择 COS 源站。本功能必须使用 **北京/上海/广州/成都** 的 COS 作为源站。
	- 生效域名：系统将自动全选采用该 COS 作为源站的域名，该域名用于发布 APK 。可自行增删。
	- 上传目录：设置原始 APK 在 COS 上的上传目录。配置完成后，需手动上传原始APK至该目录。
	- 输出目录：设置 CDN 节点处理完母包之后的输出目录。上传原始 APK 后，系统会自动处理、生成同名母包，并将母包上传至该目录。**构造请求 URL 时，请将用户请求指向该目录**，而非上传目录。
	- 签名方式：当前支持对采用 Android V1/V2 签名方式的 APK 进行动态打包，V2签名支持 WALLE/VASDOLLY 等开源多渠道打包方案。同时支持将注释信息写入指定的自定义 Block ID。
	- 重命名参数：重命名参数支持用户下载文件时可根据参数生成新的文件名，不配置时下载文件名与母包的文件名一致。
	- 渠道参数：固定为 `comment`，不可修改。
	- 云函数配置：授权之后，系统将根据配置自动生成云函数。

> !请不要在 SCF 控制台删除该云函数！

### 步骤二：上传原始 APK

登录 [COS 控制台](https://console.cloud.tencent.com/cos5) ，并上传原始 APK 到指定的上传目录

> ?原始 APK 大小不可超过10GB。

### 步骤三：等待母包处理完成

返回 CDN 控制台的 APK 动态打包功能页，单击母包状态查看 CDN 节点对母包的处理进展为“处理完成”即可。
![](https://qcloudimg.tencent-cloud.cn/raw/d8b783efd03769a178e267e3061402de.png)
若处理失败，可查看具体的失败原因。
![](https://qcloudimg.tencent-cloud.cn/raw/62617c12f5c7f70af7c1343c952fb19c.png)

### 步骤四：发布动态打包 URL

母包处理完毕后，即可发布动态打包 URL。具体示例如下：
若任务信息如下：
![](https://qcloudimg.tencent-cloud.cn/raw/5cada38d0f146bbecb5f036ae4a3b7f7.png)

则对应发布的 URL 为：`https://www.example.com/ext/test2_edge_pack.apk?comment=pipeline`。
用户请求该 URL，即可获得 CDN 边缘写入 pipeline 渠道信息之后的 APK 包。
如果配置了重命名参数，则URL可为：`https://www.example.com/ext/test2_edge_pack.apk?comment=pipeline&filename=newfilename`，即用户请求下载后，文件名显示为"newfilename"。


## 费用说明

费用详情，请参见 [APK 动态打包计费规则](https://cloud.tencent.com/document/product/228/75563#apk-.E5.8A.A8.E6.80.81.E6.89.93.E5.8C.85.E8.AF.B7.E6.B1.82.E6.95.B0.E8.AE.A1.E8.B4.B9)。


## 常见问题

1. 上传母包后，通过 src 目录下载发现并未打包渠道信息?
src 是上传目录，通过 scf 处理母包，最终将输出到 ext 目录，需要访问 ext 目录才能自动打包。
2. walle 格式，comment=123456， walle-cli 查询报错，提示 json 格式不对？
walle 的渠道信息格式要求为 json 格式并做 urlencode，后台会将 comment 信息通过 urldecode 后直接打在对应的 blockid-value 里，所以 comment 内容为 urlencode（json）。例如：渠道信息为123456， 则 walle value 为 `{"channel":"123456"}, comment=%7B%22channel%22%3A%22123456%22%7D`。
3. Android客户端取出渠道名会有%00,%00等信息？
%00,%00等信息是边缘打包预留的占位符，解决方式有两种。
	- 处理方式一：可自行处理，删除渠道信息后面的空白符即可。
	- 处理方式二：若使用V2-vasdolly签名方式的，可将vasdolly 的sdk版本升级 3.0.6即可自动去除预留的占位符。
