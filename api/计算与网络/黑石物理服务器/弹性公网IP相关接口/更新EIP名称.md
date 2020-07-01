>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。黑石物理服务器1.0 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/386/18637" target="_blank">黑石物理服务器1.0 API 3.0</a>。**
>

## 功能描述
ModifyEipAlias 接口用于更改弹性公网EIP的别名。用户通过该接口自定义申请到的EIP的别名，方便管理。
 
接口访问域名: bmeip.api.qcloud.com


## 请求
### 请求示例
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=ModifyEipAlias
	&<公共请求参数>
	&eipId=<EIP实例ID>
	&eipName=<更改的EIP别名>
```
### 请求参数

以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数页面](/document/product/386/6718)。其中，此接口的Action字段为 ModifyEipAlias。

|参数名称|必选|类型|描述|
|-------|----|---|----|
| eipId|是|String|EIP实例ID，可以通过[查询EIP列表](/document/product/386/6671)接口查询|
| eipName|是|String|待更改的EIP名称，仅可以使用英文、汉字、数字、连接线"-"或下划线"_"|


## 响应
### 响应示例
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": []
}
```
### 响应参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code |  Int | 错误码, 0: 成功, 其他值: 失败，具体含义可以参考[错误码](/document/product/386/6725)。 |
| message |   String | 错误信息 |


## 错误码
|错误代码|英文提示|错误描述|
|---|---|---|
|9003|ParamInvalid|请求参数不正确|
|9006|InternalErr|内部数据操作异常|
|30009|EipNotExist|操作的EIP记录不存在|

## 实际案例
 
### 输入
```
GET https://bmeip.api.qcloud.com/v2/index.php?
	Action=ModifyEipAlias
	&SecretId=AKIDlfdHxN0ntSVt4KPH0xXWnGl21UUFNoO5
	&Nonce=28900
	&Timestamp=1507791843
	&Region=bj
	&eipId=eip-e791epal
	&eipName=test
	&Signature=pULUe%2F9yFF8Y87tA4%2Fs6WjwoX5c%3D
```

### 输出
```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": []
}

```

