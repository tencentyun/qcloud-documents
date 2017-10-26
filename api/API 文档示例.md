## 接口描述
#### 功能描述
云硬盘的 AttachCbsStorages 接口用于在指定的云主机上挂载指定的弹性云盘。

#### 使用限制
- 只支持弹性云盘。云硬盘类型可以通过 DescribeCbsStorages（查询云硬盘信息）接口查询，见输出参数中 portable 字段解释。
- 云硬盘必须处于非挂载状态，且状态为 normal。云硬盘挂载状态可以通过 DescribeCbsStorages（查询云硬盘信息）接口查询，见输出参数中 storageStatus、attached 字段解释。
- 云主机已挂载弹性云盘数量可以通过 DescribeInstancesCbsNum（查询云主机已挂载弹性云盘数量）接口查询，见输出参数中 maxAttachNum、count 字段解释。

#### 请求域名：
AttachCbsStorages 接口请求域名为：`cbs.api.qcloud.com`

## 请求
语法示例
```
https://cbs.api.qcloud.com/v2/index.php?
<公共请求参数>
&Action=AttachCbsStorages
&storageIds.0=<storageId>
&uInstanceId=<uInstanceId>
```

### 请求参数
以下请求参数列表为该接口请求参数，其它公共请求参数参见 [公共请求参数](https://cloud.tencent.com/document/product/240/8320)。

|参数名称|		描述 |类型	| 必选|
|------|-------|-------|------|
|storageIds	|	将要被挂载的弹性云盘ID。通过DescribeCbsStorages（查询云硬盘信息）接口查询。单次最多可操作10块弹性云盘|Array[String]	|是|
|uInstanceId	|云服务器实例ID，云盘将被挂载到此云服务器上。通过DescribeInstances（查看实例列表）接口查询|String	|是	|

## 响应
该响应体返回为 JSON 数据，包含完整节点数据的内容展示如下：
```
{
    "code":"0",
    "message":"",
    "detail":{
        "disk-a2dbffgk":{
            "code":"0",
            "message":"ok"
        },
        "taskId":"2377970"
    }
}
```
### 响应参数

|参数名称|		描述 |类型	| 
|------|-------|-------|
|code	|公共错误码，0 表示成功，其他值表示失败。详见错误码页面|Int	|
|message|	错误信息，详见错误码页面|String	|
|detail|	见批量异步任务接口返回格式|Array[object]	|


## 错误码
以下错误码为该接口的业务逻辑错误码，更多公共错误码详见[云硬盘错误码](https://cloud.tencent.com/document/product/362/4207)

|错误代码	|英文描述	|错误描述|
|-----|-------|--------|
|9003|	InvalidParameter|	参数错误|
|16007|	IncorrectInstanceStatus.DiskTypeInvalid|	当前云硬盘不支持此操作|
|16008|	IncorrectInstanceStatus.OnlySupportElasticCloudDisk	|只能处理弹性云盘|

## 实际示例
### 请求
```
https://cbs.api.qcloud.com/v2/index.php?
<公共请求参数>
&Action=AttachCbsStorages
&storageIds.0=disk-a2dbffgk
&uInstanceId=ins-9spojch6

```
### 响应
```
{
    "code":"0",
    "message":"",
    "detail":
		{
        "disk-a2dbffgk":
				{
            "code":"0",
            "message":"ok"
        },
     "taskId":"2377970"
    }
}
```