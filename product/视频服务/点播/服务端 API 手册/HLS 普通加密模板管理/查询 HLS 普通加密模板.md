## 接口名称
QuerySimpleAesTemplate

## 功能说明
查询 HLS 普通加密模板。

## 请求方式

#### 请求域名
`vod.api.qcloud.com`

#### 最高调用频率
100次/分钟

#### 参数说明
| 参数名称 | 必填 | 类型 | 说明 |
|---------|---------|---------|---------|
| SubAppId | 否 | Integer | 点播 [子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。 |
| COMMON_PARAMS | 是 | - | 请参见 [公共参数](/document/api/213/6976)。 |

#### 请求示例
<pre>
https://vod.api.qcloud.com/v2/index.php?Action=QuerySimpleAesTemplate
&ampCOMMON_PARAMS
</pre>

## 接口应答

#### 参数说明
| 参数名称 | 类型 | 说明 |
|---------|---------|---------|
| code | Integer | 错误码，0：成功；其他值：失败。 |
| message | String | 错误信息。 |
| data | Array | HLS 普通加密模板列表。 |
| data.definition | Integer | HLS 普通加密模板的模板 ID。 |
| data.get_key_url | String | HLS 普通加密模板的 GetKeyURL。 |

#### 错误码说明
| 错误码 | 含义说明|
|---------|---------|
| 4000 - 7000 | 请参见 [公共错误码](https://cloud.tencent.com/document/api/213/6982)。  |
| 1000 | 无效参数。  |
| 10702 | 内部错误。  |

#### 应答示例

```javascript
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": [
        {
            "definition": 10,
            "get_key_url": "http://xxx.com/getNotification1.php"
        },
        {
            "definition": 11,
            "get_key_url": "http://xxx.com/getNotification2.php"
        },
        {
            "definition": 12,
            "get_key_url": "http://xxx.com/getNotification3.php"
        }
    ]
}

```




