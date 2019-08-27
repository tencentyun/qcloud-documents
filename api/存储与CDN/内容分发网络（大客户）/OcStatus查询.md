## 接口描述
**GetCdnEdgeStatus** 用于查询腾讯云 CDN 边缘节点 IP、省份、运营商、状态等信息。

请求域名：<font style="color:red">cdn.api.qcloud.com</font>

<font color="orange">数据高敏感接口，通过白名单管控，请注意数据安全。</font>

>!
+ 指定域名查询，获取该域名调度所至的加速平台，对应边缘节点列表；
+ 每一个域名资源平台有所差异，因此拉取到的边缘节点不完全一致。

[查看调用示例](https://cloud.tencent.com/document/product/228/1734)

## 入参说明
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 [公共请求参数](https://cloud.tencent.com/doc/api/231/4473) 页面。其中，此接口的 Action 字段为 GetCdnEdgeStatus。

| 参数名称 | 是否必选 | 类型     | 描述      |
| ---- | ---- | ------ | ------- |
| host | 否    | String | 需要查询的域名 |

## 出参说明
| 参数名称     | 类型     | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的 [公共错误码](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 |
| message  | String | 模块错误信息描述，与接口相关。                          |
| codeDesc | String | 英文错误信息，或业务侧错误码。                          |
| data     | Object | 返回结果数据，IP 列表                              |

### 详细说明

#### data

| 参数名称 | 类型     | 描述     |
| ---- | ------ | ------ |
| city | String | 城市，中文  |
| isp  | String | 运营商，中文 |
| prov | String | 省份，中文  |
| ip   | String | 节点 IP  |


## 调用案例
### 示例参数
```
host:www.test.com
```

### GET 请求
GET 请求需要将所有参数都加在 URL 后：
```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetCdnEdgeStatus
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462436277
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXX
&host=www.test.com
```

### POST 请求
POST请求时，参数填充在 HTTP Request-body 中，请求地址：
```
https://cdn.api.qcloud.com/v2/index.php
```
参数支持 form-data、x-www-formurl-encoded 等格式，参数数组如下：

```
array (
	'Action' => 'GetCdnEdgeStatus',
	'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
	'Timestamp' => 1462782282,
	'Nonce' => 123456789,
	'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
	'host' => ''www.test.com
)
```

### 结果示例

示例中的结果仅供参考。

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
       "ocs": [
            	{
                	"city":"呼和浩特",
                	"isp":"电信",
                	"prov":"内蒙古",
                	"ip":"1.1.1.1"
            	},
               ...
            ]
    }
}
```


