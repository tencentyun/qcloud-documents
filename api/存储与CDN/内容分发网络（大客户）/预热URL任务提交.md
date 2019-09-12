## 1. 接口描述
本接口（CdnPusherV2）提交URL预热任务。

接口请求域名：cdn.api.qcloud.com

**接口说明：**
+ 每一个客户每天能够提交的预热资源上限为1000条，每一个客户每次提交的预热资源上限为20条；
+ 若默认上限无法满足您的业务需求，请联系我们为您调整配额；
+ 该接口已经接入了CDN子用户鉴权体系，有权限的协作者用户可以使用中自己的SecretId和SecretKey来调用；
+ 通过此接口提交的预热任务可以在控制台进行查看及结果查询。


## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数](https://cloud.tencent.com/doc/api/231/4473)页面。其中，此接口的Action字段为CdnPusherV2。

| 参数名称 | 是否必选 | 类型 | 描述 |
| --------- | ---- | ----- | ------------------------ |
| urls.n | 是 | Array | 需要进行预热的资源URL列表 |
| limitRate | 否 | Int | 预热限速（单位为Mbps），最小限速为1Mbps |

**注意事项：**

+ 提交的URL格式需要以 http:// 或 https:// 为前缀；
+ 提交的URL可以属于不同的域名，CDN会以域名维度来拆分不同任务进行预热；
+ 预热会导致回源带宽较高，请根据源站带宽来拆分提交预热任务；
+ 当预热回源压力较大时，可以通过设置预热限速从一定程度上缓解源站压力；
+ 限速是针对域名维度进行，若设置了限速为1Mbps，假设预热资源 `http://www.abc.com/1.mkv` 时，向域名 `www.abc.com` 配置的源站拉取资源时，全网节点总回源速度会控制在 1Mbps 左右。

## 3. 输出参数
| 参数名称 | 类型 | 描述 |
| -------- | ------ | ---------------------------------------- |
| code | Int | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的[公共错误码](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81)。 |
| message | String | 模块错误信息描述，与接口相关。 |
| codeDesc | String | 英文错误信息，或业务侧错误码。 |
| data | Object | 返回结果数据 |

**data字段说明**

| 参数名称 | 类型 | 描述 |
| -------- | ------ | --------- |
| task_ids | Object | 提交的任务ID信息 |

**task_ids字段说明**

| 参数名称 | 类型 | 描述 |
| ------- | ------ | ------- |
| task_id | Int | 提交的任务ID |
| date | String | 提交任务的日期 |

## 4. 示例
### 4.1 输入示例
```
> urls.0: http://www.test.com/1.txt
> limitRate: 1
```

### 4.2 GET 请求
GET 请求需要将所有参数都加在 URL 后：
```
https://cdn.api.qcloud.com/v2/index.php?
Action=CdnPusherV2
&SecretId=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&Timestamp=1462436277
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXX
&urls.0=http://www.test.com/1.jpg
&limitRate=1
```

### 4.2 POST请求
POST请求时，参数填充在HTTP Requestbody中，请求地址：
```
https://cdn.api.qcloud.com/v2/index.php
```
参数支持 formdata、xwwwformurlencoded 等格式，参数数组如下：

```
array (
'Action' => 'CdnPusherV2',
'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXX',
'Timestamp' => 1462782282,
'Nonce' => 123456789,
'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXX',
'urls.0' => 'http://www.test.com/1.jpg',
'limitRate' => 1
)
```

### 4.3 返回示例
```
{
"code": 0,
"message": "",
"codeDesc": "Success",
"data": {
"task_ids": [
{
"task_id": 20860,
"date": "20161013"
}
]
}
}
```
