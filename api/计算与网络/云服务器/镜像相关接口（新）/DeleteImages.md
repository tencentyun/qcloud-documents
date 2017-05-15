# DeleteImages
-------------------

## 1. 接口描述

	用于删除一个或多个指定ID的镜像


注：本接口为改版后的API接口。如需了解旧接口相关信息，请参考：[DeleteImages(旧版)](https://www.qcloud.com/document/api/213/1274)


接口请求域名：<font style="color:red">image.api.qcloud.com</font>


* 当镜像当前状态为`创建中`和`使用中`时, 不允许删除。
* 每个地域最多只支持创建10个自定义镜像，删除镜像可以释放账户的配额。
* 当镜像正在被其它账户分享时，不允许删除。


## 2. 输入参数

以下请求参数列表仅列出了接口请求参数，其它参数可参考[公共请求参数](/document/api/213/6976)。

| 参数名称 |  类型 |是否必选| 描述 |
|---------|---------|---------|---------|
| ImageIds |  array of String |是 | 镜像ID ；必须满足下列限制：<br> * ImageId 必须指定一个状态为 “NORMAL” 的镜像。<br> * 所指定的镜像没有共享给其它账户。


## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| RequestId | String | 唯一请求ID。每次请求都会返回一个唯一的 RequestId，当客户调用接口失败需要后台研发人员处理时需提供该 RequestId。|


## 4. 错误码

> 腾讯云在极少数情况下可能会删减或增加错误码；开发者需要保证应用程序编写的健壮性。

| 错误码 |  描述 |
|---------|---------|
InvalidImageId.InShared|无效的ImageId：镜像被共享中
InvalidImageId.IncorrectState|无效的ImageId：无效的状态
InvalidImageId.NotFound| 无效的ImageId：找不到对应的Image
InvalidImageId.Malformed| 无效的ImageId：格式不合法


要查看更多错误码，见参考[公共错误码]()

## 5. 示例 

>**GET** `https://image.api.qcloud.com/?Action=DeleteImages`
>>&ImageIds.0=img-o3ycss2p<br>
>>&imageIds.1=img-kb1a392d<br>
>>&[公共请求参数](/doc/api/229/6976)

```json

{
    "Response": {
        "RequestID": "354f4ac3-8546-4516-8c8a-69e3ab73aa8a"
    }
}

```



