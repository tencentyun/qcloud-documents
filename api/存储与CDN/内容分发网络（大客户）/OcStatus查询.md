## 1. 接口描述
本接口（GetCdnEdgeStatus）用于查询腾讯云CDN边缘节点状态。

接口请求域名：<font style="color:red">cdn.api.qcloud.com</font>

<font color="orange">数据高敏感接口，通过白名单管控，请注意数据安全。</font>

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数](https://www.qcloud.com/doc/api/231/4473)页面。其中，此接口的Action字段为 GetCdnEdgeStatus。

| 参数名称 | 是否必选 | 类型     | 描述                |
| ---- | ---- | ------ | ----------------- |
| host  | 否   | String | 需要查询的域名 |

**注意事项**

+ 若不填充域名，则拉取到该客户默认接入平台的所有边缘节点列表；
+ 若填充域名，则拉取到该域名接入平台的边缘节点列表；
+ 每一个域名资源平台有所差异，因此拉取到的边缘节点不完全一致；
+ CDN会自动剔除故障节点，因此返回的均为状态正常的边缘节点信息。

## 3. 输出参数
| 参数名称     | 类型     | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://www.qcloud.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 |
| message  | String | 模块错误信息描述，与接口相关。                          |
| codeDesc | String | 英文错误信息，或业务侧错误码。                          |
| data     | Object | 返回结果数据，ip列表                               |

#### data数据说明
| 参数名称     | 类型     | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| city | String | 城市，中文 |
| isp | String | 运营商，中文 |
| prov | String | 省份，中文 |




## 4. 示例
### 4.1 输入示例
> host=www.test.com

### 4.2 GET 请求
GET 请求需要将所有参数都加在 URL 后（逗号进行转码）：
```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetCdnEdgeStatus
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462436277
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXX
&host=www.test.com
```

### 4.2 POST请求
POST请求时，参数填充在HTTP Requestbody中，请求地址：
```
https://cdn.api.qcloud.com/v2/index.php
```
参数支持 formdata、xwwwformurlencoded 等格式，参数数组如下：

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

### 4.3 返回示例

```
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
       "ocs": [
            	{
                	"city": "呼和浩特",
                	"isp": "电信",
                	"prov": "内蒙古"
            	},
               ...
            ]
    }
}
```


