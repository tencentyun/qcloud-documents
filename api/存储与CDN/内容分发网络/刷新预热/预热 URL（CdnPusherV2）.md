**URL 预热接口目前已开放内测，欢迎提交 [工单申请](https://console.cloud.tencent.com/workorder/category) 使用接口。**

## 接口描述
**CdnPusherV2** 将指定 URL 资源主动推送至 CDN 节点。
请求域名：`cdn.api.qcloud.com`
+ 默认情况下，每一个账号每日可预热资源1000条，每次最多可提交20条。
+ 内测用户子账号可使用自有 SecretId、SecretKey 预热有权限的资源。
+ 提交的 URL 必须以 `http://` 或 `https://` 开头。
+ 提交的 URL 中域名的状态需要为【已启动】或【部署中】。
+ 预热会导致回源带宽较高，请根据源站带宽来拆分提交预热任务。
+ 调用频次限制为10000次/分钟。
+ 接口已支持子账号调用。

查看 [调用示例](https://cloud.tencent.com/document/product/228/1734)。

## 入参说明
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见 [公共请求参数](https://cloud.tencent.com/doc/api/231/4473) 页面。其中，此接口的 Action 字段为 CdnPusherV2。

| 参数名称      | 是否必选 | 类型    | 描述                           |
| --------- | ---- | ----- | ---------------------------- |
| urls.n    | 是    | Array | 需要进行预热的资源 URL 列表               |
| limitRate | 否    | Int   | 预热限速（单位为Mbps）<br/>最小限速为1Mbps |

#### 详细说明
+ 限速是针对域名维度进行，若设置了限速为1Mbps，假设预热资源 `http://www.abc.com/1.mkv` 时，向域名 `www.abc.com` 配置的源站拉取资源时，全网节点总回源速度会控制在1Mbps左右。
+ 提交的 URL 会根据域名聚合为不同的 task，返回多个 task_id。

## 出参说明
| 参数名称     | 类型     | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | 公共错误码，0表示成功，其他值表示失败。<br/>详情请参见错误码页面 [公共错误码](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 |
| message  | String | 模块错误信息描述，与接口相关。                          |
| codeDesc | String | 英文错误信息，或业务侧错误码。<br/>详情请参见错误码页面 [业务错误码。](https://cloud.tencent.com/document/product/228/5078#2.-.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) |
| data     | Object | 返回结果数据。                                   |

#### data 详细说明

| 参数名称     | 类型     | 描述        |
| -------- | ------ | --------- |
| task_ids | Object | 提交的任务 ID 信息。 |

#### task_ids 详细说明

| 参数名称    | 类型     | 描述      |
| ------- | ------ | ------- |
| task_id | Int    | 提交的任务 ID。 |
| date    | String | 提交任务的日期。 |

## 调用案例
### 示例参数
```
> urls.0: http://www.test.com/1.jpg
> urls.1: http://www.abc.com/1.jpg
> limitRate: 1
```

### GET 请求
GET 请求需要将所有参数都加在 URL 后：
```
https://cdn.api.qcloud.com/v2/index.php?
Action=CdnPusherV2
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462436277
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXX
&urls.0=http://www.test.com/1.jpg
&urls.1=http://www.abc.com/1.jpg
&limitRate=1
```

>!GET 请求大小限制为32KB，超出大小限制则会返回状态码501。若需提交较多 URL，可采用 POST 请求。

### POST请求
POST 请求时，参数填充在 HTTP Requestbody 中，请求地址：

```
https://cdn.api.qcloud.com/v2/index.php
```

参数支持 form-data 等格式，参数数组如下：

```
array (
	'Action' => 'CdnPusherV2',
	'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
	'Timestamp' => 1462782282,
	'Nonce' => 123456789,
	'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
	'urls.0' => 'http://www.test.com/1.jpg',
	'urls.1' => 'http://www.abc.com/1.jpg',
    'limitRate'  => 1
)
```

>!POST 请求大小限制为1MB，超出大小限制则会返回状态码501。若需提交较多 URL，请拆分为多批次提交。

### 返回示例
```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "task_ids": [
            {
                "task_id": 41773,
                "date": "20180327"
            },
            {
                "task_id": 41774,
                "date": "20180327"
            }
        ]
    }
}
```
