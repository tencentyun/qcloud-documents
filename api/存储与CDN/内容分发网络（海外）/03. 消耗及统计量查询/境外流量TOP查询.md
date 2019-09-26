接口 GetCdnOverseaStatTop 通过入参 statType 不同可指定查询按境外流量/境外请求数排序的 TOP URL，此文档对境外流量 TOP 查询进行详细说明。

## 接口描述
**GetCdnOverseaStatTop** 用于查询多域名/项目指定时间区间按流量排名的 TOP 1000 URL 列表。
请求域名：`cdn.api.qcloud.com`

>!
-  可一次提交多个域名，查询整体流量 TOP1000 URLTOP 排名，需填充对应 projectId。
- 可一次提交多个项目，查询整体流量 TOP1000 URLTOP 排名。
- TOP 数据从日志中计算获取，数据延迟约30分钟。
- 支持查询90天内的 TOP 数据。
- 调用频次限制为100次/分钟。
- 接口暂不支持子账号调用。

## 请求参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见 [公共请求参数](https://cloud.tencent.com/doc/api/231/4473) 页面。其中，此接口的 Action 字段为 GetCdnOverseaStatTop。

| 参数名称       | 是否必选 | 类型     | 描述             |
| ---------- | ---- | ------ | -------------- |
| startDate  | 是    | String | 查询开始时间（日）      |
| endDate    | 是    | String | 查询结束时间（日）      |
| projects.n | 是    | String | 项目 ID           |
| hosts.n    | 否    | String | 域名             |
| statType   | 是    | String | "flux"：表示按流量排序 |


## 响应参数

| 参数名称     | 类型     | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | 公共错误码<br/>0：表示成功<br/>其他值：表示失败<br/>详见错误码页面 [公共错误码](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) |
| message  | String | 模块错误信息描述，与接口相关                          |
| codeDesc | String | 英文错误信息，或业务侧错误码<br/>详见错误码页面 [业务错误码](https://cloud.tencent.com/document/product/228/5078#2.-.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。 |
| data     | Array  | 结果数据，详细说明见下文                             |

### 详细说明
#### data

| 参数名称             | 类型     | 说明            |
| -------------- | ------ | ------------- |
| url_data       | Array  | URL 排名，结构说明见下文 |
| start_datetime | String | 起始日期          |
| end_datetime   | String | 结束日期          |
| stat_type      | String | 排名依据          |

#### url_data

| 参数名称    | 类型     | 说明           |
| ----- | ------ | ------------ |
| name  | String | URL          |
| flux | Int    | 流量值，单位为 byte |

## 示例代码
### 示例参数

```
startDate：20180501
endDate：20180502
projects.0：0
hosts.0：www.test.com
statType：flux
```

### GET 请求
GET 请求需要将所有参数都加在 URL 后：

```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetCdnOverseaStatTop
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462421433
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXXXXX
&startDate=20180501
&endDate=20180502
&hosts.0=www.test.com
&projects.0=0
&statType=flux
```

### POST 请求
POST 请求时，参数填充在 HTTP Request-body 中，请求地址：

```
https://cdn.api.qcloud.com/v2/index.php
```

参数支持 form-data、x-www-form-urlencoded 等格式，参数数组如下：

```
array (
  'Action' => 'GetCdnOverseaStatTop',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462782282,
  'Nonce' => 123456789,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
  'startDate' => '20180501',
  'endDate' => '20180502',
  'projects.0' => '0',
  'hosts.0' => 'www.test.com',
  'statType' => 'flux'
)
```

### 结果示例

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "start_datetime": "2018-05-01",
        "end_datetime": "2018-05-02",
        "stat_type": "flux",
        "url_data": [
            {
                "name": "www.test.com/robots.txt",
                "flux": 212
            },
            {
                "name": "www.test.com/",
                "flux": 207
            }
        ]
    }
}
```

