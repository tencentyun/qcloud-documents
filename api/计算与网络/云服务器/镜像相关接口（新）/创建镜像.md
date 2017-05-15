# CreateImage
-------------------

## 1. 接口描述

	用于将实例系统盘的当前状态制作成全新的镜像，使用此镜像可以快速创建实例。


注：本接口为改版后的API接口。如需了解旧接口相关信息，请参考：[CreateImage(旧版)](https://www.qcloud.com/document/api/213/1273)


接口请求域名：<font style="color:red">image.api.qcloud.com</font>


* 目标实例需要在关机状态下才可以创建自定义镜像。
* 每个地域最多只支持创建10个自定义镜像。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数可参考[公共请求参数](/document/api/213/6976)。

| 参数名称 |  类型 |是否必选| 描述 |
|---------|---------|---------|---------|
| InstanceId |  String |是 | 需要制作镜像实例的ID 。
| ImageName |  String |是 | 镜像名称 ；必须满足下列限制：<br> * 合法的ImageName，不得超过20个字符<br> * 镜像名称不得重复。
| ImageDescription |  String |否 | 镜像描述 ；合法的Image描述，不得超过60个字符。其默认值为 ``
| Sysprep |  Boolean |否 | 创建镜像时是否启用 SysPrep( Windows only) 。其默认值为 `False`


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId | String | 唯一请求ID。每次请求都会返回一个唯一的 RequestId，当客户调用接口失败需要后台研发人员处理时需提供该 RequestId。|


## 4. 错误码

> 腾讯云在极少数情况下可能会删减或增加错误码；开发者需要保证应用程序编写的健壮性。

| 错误码 |  描述 |
|---------|---------|
|InvalidParameter.ValueTooLarge | 无效参数：参数过长|
|InvalidImageName.Duplicate | 无效的ImageName：与已有镜像重复。|
|MutexOperation.TaskRunning|互斥的操作；之前的任务仍在运行|
|InvalidInstanceId.NotFound| 没有找到相应实例|
|ImageQuotaLimitExceeded| 镜像配额超过了限制|
|InvalidInstance.NotSupported| 不被支持的实例|


要查看更多错误码，见参考[公共错误码]()

## 5. 示例 

>**GET** `https://image.api.qcloud.com/?Action=CreateImage`
>>&InstanceId=ins-6pb6lrmy<br>
>>&[公共请求参数](/doc/api/229/6976)

```json

{
    "Response": {
        "RequestID": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}

```



