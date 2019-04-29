## 接口描述
本接口（DeleteJob）用于删除训练任务。

## 输入参数
以下请求参数列表仅列出了接口请求参数，其它参数见公共请求参数。

| 参数名称 | 是否必选 | 类型 | 描述 |
|---|---|---|---|
| Name | 是 | String | 任务名称。 |
| Cluster | 是 | String | 运行任务的集群。 |

##  输出参数
|参数名称|类型|描述|
|---|---|---|
| RequestId | String | 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。|

## 错误码
| 错误码 | 描述 |
|---|---|
| Internal Error | 内部错误。|
| InvalidParameter | 参数错误。|
| ResourceNotFound | 资源不存在。|

## 示例

#### 输入：
```
http://stia.tencentcloudapi.comAction=DeleteJob
&Name=test-job
&Cluster=ap-beijing&Signature=g92Zha76wgSrO1oyapmm6ShndeE%3D
&公共请求参数

```
#### 输出：
```
{
	"Response": {
		"RequestId": "xxxxxxxx - xxxx - xxxx - xxxx - xxxxxxxxxxxx"
	}
}
```
