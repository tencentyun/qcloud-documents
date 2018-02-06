## 简介
本接口用于人脸融合。


## 说明

| 概念     | 解释               |
| ------ | ---------------- |
| appid  | 项目 ID, 接入项目的唯一标识，可在 [账号信息](https://console.cloud.tencent.com/developer) 或 [云 API 密钥](https://console.cloud.tencent.com/cam/capi) 中查看 |

## 调用 URL
支持 http 和 https 两种协议：

http://aiconsole.cloud.tencent.com/fuseapi/face

https://aiconsole.cloud.tencent.com/fuseapi/face


## 请求包 header
所有请求都要求含有下表列出的头部信息：

| 参数名            | 值                                        | 描述                                       |
| -------------- | ---------------------------------------- | ---------------------------------------- |
| Host           | aiconsole.cloud.tencent.com               | 服务器域名                                |
| Content-Length | 包体总长度                                    | 整个请求包体内容的总长度，单位：字节（Byte）                 |
| Content-Type   | application/json   | 参数类型                                 |
| Authorization  | 鉴权签名                                     | 用于 [**鉴权**](document/product/641/12409) 的签名 |

> **注意：**
> 1、每个请求的包体大小限制为 6MB；
> 2、所有接口都为 POST 方法；
> 3、不支持 .gif 这类的动图。

## 请求参数
使用 application/json 格式。

| 参数名    | 是否必须 | 类型     | 说明    |
| ------ | ---- | ------ | ------- |
| appid  | 必须   | string | 项目 ID，可在 [账号信息](https://console.cloud.tencent.com/developer) 查看   |
| uin    | 必须   | string | 账号 ID，可在 [账号信息](https://console.cloud.tencent.com/developer) 查看|
| project_id    | 必须   | string | 活动 ID |
| model_id    | 必须   | string | 素材 ID |
| img_data    | 必须   | string | 图片 base64 数据 |
| rsp_img_type    | 可选   | string | 返回图像方式（url, base64)，默认 url， base64 则返回 base64 数据 |


## 返回内容

| 字段                 | 类型     | 说明      |
| ------------------ | ------ | ------- |
| ret | int | 错误码 |
| img_url               | string    | rsp_img_type 为 url 时，返回结果的 url,  rsp_img_type 为 base64 时返回 base64 数据   |
| msg            | string | 错误描述  |

## 示例

### 请求包:

```
{
	"rsp_img_type":"url",
	"project_id":"xxxxxxxx",
	"appid":"xxxxxxxx", 
	"uin":"xxxxxxxx",
	"img_data":"xxxxxxxx",
	"model_id":"xxxxxxxx",
}

```


### 回包:

```
{
	"img_url":"http://activity-10053123.image.myqcloud.com/XXXX",
	"ret":"0"
}
```


## 错误码

| **错误码** | **含义**                              |
| ------- | ----------------------------------- |
| -1       | 非法的用户请求                               |
| -3       | 图片尺寸太大                                |
| -4       | 识别人脸出错                              |
| -5       | 内部错误                 |
| -6       | 参数错误                        |
| -7       | 鉴权信息过期                        |
| -8       | 模板无人脸                                |
| -20001      |  鉴权信息为空                            |
| -20002      |  鉴权信息解析错误                            |
| -20003      |  鉴权失败                            |
| -20004      |  操作太频繁，触发频控                            |
| -20005      |  后端服务故障                            |









