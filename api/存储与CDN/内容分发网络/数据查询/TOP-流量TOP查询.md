<font style="color:Brown">接口 GetCdnStatTop 通过入参 statType 不同可指定查询按流量/请求数排序的 TOP 省份、TOP 运营商、TOP URL，此文档对流量 TOP 查询进行详细说明</font>

## 接口描述

**GetCdnStatTop** 用于查询多域名/项目指定时间区间按流量排名的 TOP 1000 URL列表、省份 TOP 排名、运营商 TOP 排名。

请求域名：<font style="color:red">cdn.api.qcloud.com</font>

>!
+ 可一次提交多个域名，查询整体流量TOP1000 URL、省份TOP排名、运营商TOP排名，需填充对应projectId
+ 可一次提交多个项目，查询整体流量TOP1000 URL、省份TOP排名、运营商TOP排名
+ TOP数据从日志中计算获取，数据延迟约 30 分钟
+ 支持查询 90天内的TOP数据
+ 调用频次限制为 100次/分钟
+ 接口已支持子账号调用，权限配置可参考权限 [配置示例](https://cloud.tencent.com/document/product/228/14867)

[查看调用示例](https://cloud.tencent.com/document/product/228/1734)

## 入参说明
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见 [公共请求参数](https://cloud.tencent.com/doc/api/231/4473) 页面。其中，此接口的 Action 字段为 GetCdnStatTop。

| 参数名称       | 是否必选 | 类型     | 描述             |
| ---------- | ---- | ------ | -------------- |
| startDate  | 是    | String | 查询开始时间（日）      |
| endDate    | 是    | String | 查询结束时间（日）      |
| projects.n | 是    | String | 项目 ID           |
| hosts.n    | 否    | String | 域名             |
| statType   | 是    | String | "flux"：表示按流量排序 |


## 出参说明

| 参数名称     | 类型     | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | 公共错误码，0表示成功，其他值表示失败。<br/>详见错误码页面 [公共错误码](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 |
| message  | String | 模块错误信息描述，与接口相关。                          |
| codeDesc | String | 英文错误信息，或业务侧错误码。<br/>详见错误码页面 [业务错误码](https://cloud.tencent.com/document/product/228/5078#2.-.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81)。 |
| data     | Array  | 结果数据，详细说明见下文                             |

### 详细说明

#### data

| 名称             | 类型     | 说明            |
| -------------- | ------ | ------------- |
| province_data  | Array  | 省份排名，结构说明见下文  |
| isp_data       | Array  | 运营商排名，结构说明见下文 |
| url_data       | Array  | URL排名，结构说明见下文 |
| start_datetime | String | 起始日期          |
| end_datetime   | String | 结束日期          |
| stat_type      | String | 排名依据          |
| period         | Int    | 时间粒度          |

#### province_data

| 名称    | 类型     | 说明           |
| ----- | ------ | ------------ |
| id    | Int    | 省份编号         |
| name  | String | 省份名称，如“吉林”   |
| value | Int    | 流量值，单位为 byte |

#### isp_data

| 名称    | 类型     | 说明            |
| ----- | ------ | ------------- |
| id    | Int    | 运营商编号         |
| name  | String | 运营商名称，如“中国移动” |
| value | Int    | 流量值，单位为 byte  |

#### url_data

| 名称    | 类型     | 说明           |
| ----- | ------ | ------------ |
| name  | String | URL          |
| value | Int    | 流量值，单位为 byte |

## 调用案例

### 示例参数

```
startDate：20160503
endDate：20160504
projects.0：0
hosts.0：www.test.com
statType：flux
```

### GET 请求

GET 请求需要将所有参数都加在 URL 后：

```
https://cdn.api.qcloud.com/v2/index.php?
Action=GetCdnStatTop
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462421433
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXXXXX
&startDate=20160503
&endDate=20160504
&hosts.0=www.test.com
&projects.0=0
&statType=flux
```

### POST 请求

POST请求时，参数填充在 HTTP Request-body 中，请求地址：

```
https://cdn.api.qcloud.com/v2/index.php
```

参数支持 form-data、x-www-form-urlencoded 等格式，参数数组如下：

```
array (
  'Action' => 'GetCdnStatTop',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462782282,
  'Nonce' => 123456789,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
  'startDate' => '20160503',
  'endDate' => '20160504',
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
        "start_datetime": "2016-05-03",
        "end_datetime": "2016-05-04",
        "stat_type": "flux",
        "period": 5,
        "province_data": [
            {
                "id": 1051,
                "name": "重庆",
                "value": 207
            }
          ...
        ],
        "isp_data": [
            {
                "id": 2,
                "name": "中国电信",
                "value": 207
            }
          ...
        ],
        "url_data": [
            {
                "name": "www.test.com/robots.txt",
                "value": 212
            },
            {
                "name": "www.test.com/",
                "value": 207
            }
        ]
    }
}
```

