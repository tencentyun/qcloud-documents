## 1. 接口描述
本接口（GetCdnIps）用于查询指定域名在腾讯云 CDN 资源平台中所有的边缘节点 IP。

接口请求域名：<font style="color:red">cdn.api.qcloud.com</font>

<font color="orange">数据高敏感接口，请注意数据安全。</font>

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 [公共请求参数](https://cloud.tencent.com/doc/api/231/4473) 页面。其中，此接口的 Action 字段为 GetCdnIps。

| 参数名称 | 是否必选 | 类型     | 描述                |
| ---- | ---- | ------ | ----------------- |
| host  | 是    | String | 需要查询的域名 |


>! 每一个域名资源平台有所差异，因此拉取到的边缘节点 IP 不完全一致。

## 3. 输出参数
| 参数名称     | 类型     | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的 [公共错误码](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 |
| message  | String | 模块错误信息描述，与接口相关。                          |
| codeDesc | String | 英文错误信息，或业务侧错误码。                          |
| data     | Object | 返回结果数据，IP 列表。                               |


## 4. 示例
### 4.1 输入示例
> host = www.test.com

### 4.2 GET 请求
GET 请求需要将所有参数都加在 URL 后（逗号进行转码）：
```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetCdnIps
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462436277
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXX
&host=www.test.com
```

### 4.2 POST 请求
POST 请求时，参数填充在 HTTP Requestbody 中，请求地址：
```
https://cdn.api.qcloud.com/v2/index.php
```
参数支持 formdata、xwwwformurlencoded 等格式，参数数组如下：

```
array (
	'Action' => 'GetCdnIps',
	'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
	'Timestamp' => 1462782282,
	'Nonce' => 123456789,
	'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
	'host' => ''www.test.com
)
```

### 4.3 返回示例

注意：示例中 IP 仅供参考。

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "oc_ips": [
			1.1.1.1,
			2.2.2.2,
			...
        ]
    }
}
```


