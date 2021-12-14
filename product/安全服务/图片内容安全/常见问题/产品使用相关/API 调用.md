### 有相关的 demo 可以直接运行吗？
您可以使用 [API Explorer](https://console.cloud.tencent.com/api/explorer?Product=cvm&Version=2017-03-12&Action=DescribeZones&SignVersion=) 进行在线参数调试，或通过 [ SDK 中心](https://cloud.tencent.com/document/sdk) 下载 SDK 包到本地进行使用。

### 已开通图片内容安全，PHP 后台怎么调用服务？
您可以参考 [图片内容安全 API 文档](https://cloud.tencent.com/document/product/1125/53276)，使用 API Explorer 进行在线参数调试，或通过 [SDK 中心](https://cloud.tencent.com/document/sdk) 下载 SDK 包到本地进行使用。

### 是否支持离线 SDK？
不支持。您可以使用  [API Explorer](https://console.cloud.tencent.com/api/explorer?Product=cvm&Version=2017-03-12&Action=DescribeZones&SignVersion=) 进行在线参数调试，或通过 [SDK 中心](https://cloud.tencent.com/document/sdk) 下载 SDK 包到本地进行使用。

### 是否提供 SDK ？
用户可通过 [SDK 中心]((https://cloud.tencent.com/document/sdk)) 使用对应的资源。


### 小程序如何使用该服务审核用户上传的图片？
小程序支持 API 接入，具体接入流程需由客户自己开发。接口说明请参考 [API文档](https://cloud.tencent.com/document/product/1125/53273)。

### cms.ap-guangzhou.tencentcloudapi.com 接口只支持 HTTPS 请求吗？
是的，目前只支持 HTTPS 请求。

### 刷新签名接口收费吗？
不收费。

### 有支持批量图片检测的接口吗？
没有，目前接口仅支持单张检测。如需批量检测图片，需要用户自己写脚本进行测试。

### 图片审核 API 接口 Biztype 字段，可以由用户设定吗？
可以由用户自己设定，但需后台配置才会产生。Biztype 可以是英文字母、数字、下划线的组合，长度为3-32个字符，用户在配置前告知需要配置的格式，一旦配置后，无法更改。

### 图片审核 API 接口图片 Review 字段，是否每个标签都会输出？
只有机审后有分数输出的标签才会输出；广告、二维码等标签则不会输出。
