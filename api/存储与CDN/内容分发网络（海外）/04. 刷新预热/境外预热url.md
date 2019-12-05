## 1. 接口描述
本接口（CdnOverseaPushser）提交境外 CDN URL预热任务。

接口请求域名：<font style="color:red">cdn.api.qcloud.com</font>

**接口说明：**
+ 每一个客户每天能够提交的境外 CDN 预热资源上限为1000条，每一个客户每次提交的境外 CDN 预热资源上限为 20 条；
+ 若默认上限无法满足您的业务需求，请联系我们为您调整配额；

[调用Demo](https://cloud.tencent.com/document/product/228/1734)

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数](https://cloud.tencent.com/doc/api/231/4473)页面。其中，此接口的Action字段为CdnOverseaPushser。

| 参数名称   | 是否必选 | 类型     | 描述                        |
| ------ | ---- | ------ | ------------------------- |
| urls.n | 是    | String | 需要进行预热的资源URL；支持预热一个或多个URL |

**注意事项：**

+ 提交的URL格式需要以 http:// 或 https:// 为前缀；

+ 支持预热一个或多个 URL，预热多个URL时，参数传入方式可参考：

  ```
  urls.0=http://www.abc.com/1.jpg&urls.1=http://www.abc.com/2.jpg
  ```

+ 提交的URL可以属于不同的域名，CDN会以域名维度来拆分不同任务进行预热；

+ 预热会导致回源带宽较高，请根据源站带宽来拆分提交预热任务；

## 3. 输出参数
| 参数名称     | 类型     | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 |
| message  | String | 模块错误信息描述，与接口相关。                          |
| codeDesc | String | 英文错误信息，或业务侧错误码。                          |
| data     | Array | 返回结果数据数组                                   |

**data字段说明**

| 参数名称    | 类型     | 描述          |
| ------- | ------ | ----------- |
| task_id | String | 提交的预热任务ID信息 |

## 4. 示例
### 4.1 输入示例
> urls.0: http://www.test.com/1.jpg

### 4.2 GET 请求
GET 请求需要将所有参数都加在 URL 后：
```
https://cdn.api.qcloud.com/v2/index.php?
Action=CdnOverseaPushser
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462436277
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXX
&urls.0=http%3A%2F%2Fwww.test.com%2F1.jpg
```

### 4.2 POST请求
POST请求时，参数填充在HTTP Requestbody中，请求地址：
```
https://cdn.api.qcloud.com/v2/index.php
```
参数支持 formdata、xwwwformurlencoded 等格式，参数数组如下：

```
array (
	'Action' => 'CdnOverseaPushser',
	'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
	'Timestamp' => 1462782282,
	'Nonce' => 123456789,
	'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
	'urls.0' => 'http://www.test.com/1.jpg'
)
```

### 4.3 返回示例
```
{
	"code": 0,
	"message": "",
	"codeDesc": "Success",
	"data": [{
		"task_id": 7,
		"date": "2016-06-21 20:24:47"
	}]

}

```
