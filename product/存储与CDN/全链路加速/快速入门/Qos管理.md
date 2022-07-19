
欢迎使用全链路加速 FLA，本文档意在帮助您从0到1将全链路加速接入您的业务。如您对本操作指南中的部分配置有所疑问，请与我们取得联系。
接入全链路加速共分为以下四个部分：
![](https://qcloudimg.tencent-cloud.cn/raw/e691fcbd558f6226632f44f1ef8541fa.png)

>!
>- 如您希望只开启HTTP3（QUIC）特性支持或网络测速功能，可选择以 SDK 的方式进行接入，SDK 接入文档会在 [内测申请](https://cloud.tencent.com/apply/p/5yhsncp7q3) 通过后向您提供。
>- 关于如何配置HTTP3（QUIC）特性，请参阅：[全球应用加速—通道管理](https://cloud.tencent.com/document/product/608/67743) 及 [全球应用加速—HTTP/HTTPS 监听器管理](https://cloud.tencent.com/document/product/608/17539)。
>- 当前仅提供 Android 版本 SDK，IOS 版本 SDK 将在后续迭代中尽快上线，敬请期待。


## 全链路加速内测申请（如已通过申请请忽略）
当前全链路加速处于内测阶段，请您填写 [内测申请](https://cloud.tencent.com/apply/p/5yhsncp7q3) 后等待工作人员进行审核，申请通过后将会以短信及站内信的方式向您推送通知。
![](https://qcloudimg.tencent-cloud.cn/raw/75e01d8ea07b889d0e0b9cad894e99a6.png)

## 控制台配置
在您使用全链路加速FLA前，需首先创建应用模板。该模板主要用于配置QoS加速相关策略及方便您对不同业务进行区分。

1.	登录 [全球应用加速控制台](https://console.cloud.tencent.com/gaap)，选择全链路加速子菜单下的 [QoS管理](https://console.cloud.tencent.com/gaap/fla) 模块。
![](https://qcloudimg.tencent-cloud.cn/raw/598bc0182c63720a0a3dab84885ca14d.png)
2.	单击**新建**按钮，创建全链路加速应用模板，填写应用名称（添加后可修改），选择加速类型及加速时长。
![](https://qcloudimg.tencent-cloud.cn/raw/96b8328a11407d0606aae1842a7a2ce2.png)
配置项详解：


| 配置项 |详细说明 | 
|---------|---------|
| 应用名称 | 用于标识您所创建的应用模板。 |
| 加速类型 | QoS 加速保障的最大上/下行带宽。 |
| 应用名称 | 由于不同加速类型支持的最大带宽能力不同，产生的费用不同，请您根据业务实际情况进行选择：<br>1.	游戏类客户建议选择上/下行带宽保障为100-400kbps的加速类型；<br>2.	视频，直播类客户建议选择上行或下行带宽保障为1-4Mbps的加速类型；<br>3.	其他类型客户请根据您的实际业务情况或咨询腾讯云助手进行选择； |
| 加速时长 | 单次 QoS 加速的持续时间。<br>注：计费周期为30分钟/次，如您选择加速时长为60分钟，则相当于2次调用。 |


	

## 绑定 GAAP 通道
由于当前全链路加速 FLA 需配合全球应用加速 GAAP 使用，因此在完成应用模板创建后，需进行绑定 GAAP 通道配置。
1.	创建应用模板后，单击**通道绑定**按钮。
![](https://qcloudimg.tencent-cloud.cn/raw/7efc10c31bd5f82c75b1aea9a5bbf59b.png)
2.	添加需要绑定的 GAAP 通道（可添加多条通道），只支持选择加速区域为中国大陆境内（不含中国香港）的 GAAP 通道。
![](https://qcloudimg.tencent-cloud.cn/raw/88185106fcab0af7264ffb6afd4dc2a0.png)

>!
>- 如果您未创建 GAAP 通道，需先对通道进行配置，完成后再返回“全链路加速管理”控制台进行通道绑定。具体通道配置，请参考：[全球应用加速—快速入门](https://cloud.tencent.com/document/product/608/17849)。
>- 如果您在 GAAP 通道管理中删除了已绑定在  全链路加速管理>应用模板  中的 GAAP 通道，会使该 GAAP 通道失去 QoS 加速效果。

## 选择接入方式
完成控制台配置后，您可选择以 API 或 SDK 两种接入方式将全链路加速应用于您的业务中。具体来说，API 接入只提供 QoS 加速功能，SDK 接入提供全链路加速支持的全部功能。

### API 接入
如果您只希望接入 QoS 加速而不使用全链路加速的其他功能，可以通过调用 API 的方式接入全链路加速。

### SDK 接入
如果您希望使用全链路加速的全部功能，可选择以 SDK 的方式进行接入。当前仅提供 Android 版本 SDK，IOS 版本 SDK 将在后续迭代中尽快上线，敬请期待。

>! API 及 SDK 接入文档会在您的 [内测申请](https://cloud.tencent.com/apply/p/5yhsncp7q3) 通过后向您提供。

## 其他配置
除上述配置外，全链路加速管理控制台为您提供了编辑已创建应用模板，查询 QoS 使用量等相关操作。

1. 您可在全链路加速管理控制台单击**修改**按钮对应用模板进行编辑（修改名称，变更加速类型，变更加速时间）。
![](https://qcloudimg.tencent-cloud.cn/raw/6ad75453cb6d2d0b22be725566547b77.png)
<img src="https://qcloudimg.tencent-cloud.cn/raw/dc87d67d788b81da3b38f614c151fa31.png" width="60%">
2. 您可单击**删除**按钮，删除不再使用的应用模板。
![](https://qcloudimg.tencent-cloud.cn/raw/1dcc7b55d5c0e5113276937687e3cf43.png)
3. 您可单击**统计**按钮，查看不同应用模板下 QoS 加速具体使用情况（不同加速类型、运营商的 QoS 加速调用次数及成功率）。
![](https://qcloudimg.tencent-cloud.cn/raw/b52e0996267e52e2fe4fc78e4d9bb944.png)
![](https://qcloudimg.tencent-cloud.cn/raw/8fa42dada092adbadd7e27fadcfa935c.png)
