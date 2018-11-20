## 接口描述
本接口用于人脸融合，用户上传人脸图片，获取与模板融合后的人脸图片。


### 说明

| 概念     | 解释               |
| ------ | ---------------- |
| appid  | 项目 ID， 接入项目的唯一标识，可在 [账号信息](https://console.cloud.tencent.com/developer) 或 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 中查看。 |

### 调用 URL
支持 http 和 https 两种协议：

`http://aiconsole.cloud.tencent.com/fuseapi/face`

`https://aiconsole.cloud.tencent.com/fuseapi/face`

## 请求包 header
所有请求都要求含有下表列出的头部信息：

| 参数名          | 必选 | 值                                        | 描述                                       |
| -------------- |--- |---------------------------------------- | ---------------------------------------- |
| Host          | 是 | aiconsole.cloud.tencent.com              | 服务器域名。                                |
| Content-Length| 否 | 包体总长度                                | 整个请求包体内容的总长度，单位：字节（Byte）。 |
| Content-Type  | 是 | application/json                         | 参数类型 。                                 |
| Authorization | 是 | 鉴权签名                                  | 用于 [**鉴权**](https://cloud.tencent.com/document/product/641/12409)  的签名。 |

> **注意：**
> - 每个请求的包体大小限制为 6MB；
> - 所有接口都为 POST 方法；
> - 不支持 .gif 这类的动图。

## 请求参数
使用 application/json 格式。

| 参数名    | 必选 | 类型     | 说明    |
| ------ | ---- | ------ | ------- |
| appid  | 是   | string | 项目 ID，可在 [账号信息](https://console.cloud.tencent.com/developer) 查看。   |
| uin    | 是   | string | 账号 ID，可在 [账号信息](https://console.cloud.tencent.com/developer) 查看。|
| project_id    | 是   | string | 活动 ID，可在 [控制台](https://console.cloud.tencent.com/ai/facemerge)查看。 |
| model_id    | 是   | string | 素材 ID，可在 [控制台](https://console.cloud.tencent.com/ai/facemerge)查看。 |
| img_data    | 是   | string | 图片 base64 数据。请确保人脸为正脸，无旋转。若某些手机拍摄后人脸被旋转，请使用图片的 EXIF 信息对图片进行旋转处理。图片大小不超过 500k，分辨率不超过 1080\*1080。 |
| rsp_img_type    | 是   | string | 返回图像方式（url 或 base64) ，二选一。 |


## 响应参数

| 字段                 | 类型     | 说明      |
| ------------------ | ------ | ------- |
| ret | int | 错误码 |
| img_url               | string    | rsp_img_type 为 url 时，返回结果的 url，  rsp_img_type 为 base64 时返回 base64 数据。   |

## 示例

- [单击下载 PHP 代码 demo>> ](https://main.qcloudimg.com/raw/e6601ec77d988a193a06cb940595da97.php)
- [单击下载 Java 代码 demo>>](https://main.qcloudimg.com/raw/74c360901626b508e2efd937d47a988e.java)

### 请求

```
{
	"rsp_img_type":"url",
	"project_id":"xxxxxxxx",
	"appid":"xxxxxxxx", 
	"uin":"xxxxxxxx",
	"img_data":"xxxxxxxx",
	"model_id":"xxxxxxxx"
}

```

> **注意：**
> 若选择 base64 进行图片数据传送，请勿在 base64 数据中包含头部。



### 响应

```
{
	"img_url":"http://activity-10053123.image.myqcloud.com/XXXX",
	"ret":"0"
}
```


## 错误码

| **错误码** | **含义**                              |
| ------- | ----------------------------------- |
| 1000       | 无人脸。                               |
| 0       | 成功。                              |
| -1       | 用户身份不合法。                               |
| -3       | 图片尺寸太大。                                |
| -4       | 识别人脸出错。                              |
| -5       | 平台内部错误。                 |
| -6       | 必填的参数字段或者值有误。                        |
| -7       | 鉴权信息过期。                        |
| -8       | 模板无人脸。                                |
| -1000       | 必填的参数字段或者值有误。                                |
| -1001       | 图像处理错误。                                |
| -1002       | 读写 CKV 出错。                                |
| -1003       | 读写 REDIS 出错。                                |
| -1004       | 保存结果图片出错。                                |
| -1005       | 下载用户图片出错。                                |
| -1007       | 服务器内部逻辑出错。                                |
| -1008       | 人脸检测失败。                                |
| -1009       | 请求值不是规范的 json 格式。                                |
| -2011~-2015       | 访问频率超出限制。                                |
| -2100       | http 头错误。                                |
| -2102       | 图片操作功能不存在。                                |
| -2103       | 图片操作功能无权限。                                |
| -20001      |  鉴权信息为空。                            |
| -20002      |  鉴权信息解析错误。                            |
| -20003      |  鉴权失败。                            |
| -20004      |  操作太频繁，触发频控。                           |
| -20005      |  后端服务故障。                           |
| -20006      |  参数格式不是 json 格式。                            |
| -20007      |  素材 ID（model_id）传入为空。                            |
| -20008      |  活动 ID（project_id）传入为空。                            |
| -20009      |  图片数据（image_data）传入为空。                            |
| -20010      |  返回图片类型（rsp_img_type)为空。                            |
| -20011      |  appid 传入为空。                            |
| -20012      |  uin 传入为空。                            |
