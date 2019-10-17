## 接口描述
**RefreshCdnUrl** 删除 CDN 全网节点上缓存的指定资源。
请求域名：`cdn.api.qcloud.com`
+ 默认情况下，每一个账号每日可刷新 URL 10000条，每次最多可提交1000条。
+ 全网 URL 刷新生效时间约为5分钟。
+ 提交的 URL 必须以`http://`或`https://`开头。
+ 提交的 URL 中域名必须为该账号下已接入的加速域名。
+ 提交的 URL 中域名的状态需要为“已启动”或“部署中”。
+ 调用频次限制为10000次/分钟。
+ 接口已支持子账号调用，权限配置可参考权限 [配置示例](https://cloud.tencent.com/document/product/228/14867)。

查看 [调用示例](https://cloud.tencent.com/document/product/228/1734)。

## 入参说明
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，详情请参见 [公共请求参数](https://cloud.tencent.com/doc/api/231/4473) 页面。其中，此接口的 Action 字段为 RefreshCdnUrl。

| 参数名称   | 是否必选 | 类型     | 描述                    |
| ------ | ---- | ------ | --------------------- |
| urls.n | 是    | String | 需要刷新的 URL<br/>详情请参见下文 “URL 详细说明” |

#### 详细说明
支持刷新一个或多个 URL，刷新多个 URL 时，参数传入方式可参考：
```
urls.0=http://www.abc.com/1.jpg&urls.1=http://www.abc.com/2.jpg
```

### 过滤参数影响
1. 若域名开启了过滤参数配置，此时提交如下 URL 进行刷新：

 ```
https: //www.test.com/index.php?name=1
https: //www.test.com/index.php?name=2
```

 由于缓存时忽略参数，因此均刷新 URL：```https://www.test.com/index.php```。为节省配额，提交刷新任务时可不带参去重。
2. 若域名关闭了过滤参数配置，此时提交如下 URL 进行刷新：

 ```
https: //www.test.com/index.php?name=1
https: //www.test.com/index.php?name=2
```
 由于缓存时未忽略参数，因此将会删除对应的两个资源。

## 出参说明

| 参数名称     | 类型     | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | 公共错误码，0表示成功，其他值表示失败<br/>详情请参见错误码页面的 [公共错误码](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) |
| message  | String | 模块错误信息描述，与接口相关                           |
| codeDesc | String | 英文错误信息，或业务侧错误码<br/>详情请参见错误码页面 [业务错误码](https://cloud.tencent.com/document/product/228/5078#2.-.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) |
| data     | Array  | 详情请参见下文 “data 详细说明”                                  |

#### data 详细说明
| 参数名称    | 类型     | 描述           |
| ------- | ------ | ------------ |
| count   | Int    | 此次刷新提交的 URL 数目 |
| task_id | String | 此次刷新任务对应的 ID  |


## 调用案例
### 示例参数
```
urls.0：https://www.test.com/1.jpg
```

### GET 请求
GET 请求需要将所有参数都加在 URL 后：
```
https://cdn.api.qcloud.com/v2/index.php?
Action=RefreshCdnUrl
&SecretId=XXXXXXXXXXXXXXXXXX
&Timestamp=1462521223
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&urls.0=https%3A%2F%2www.test.com%2F1.jpg
```

>!GET 请求大小限制为32KB，超出大小限制则会返回状态码501。若需提交较多 URL，可采用 POST 请求。

### POST 请求
POST 请求时，参数填充在 HTTP Request-body 中，请求地址：
```
https://cdn.api.qcloud.com/v2/index.php
```

参数支持 form-data、x-www-form-urlencoded 等格式，参数数组如下：
```
array (
  'Action' => 'RefreshCdnUrl',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462864833,
  'Nonce' => 1149033341,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'urls.0' => 'https://www.test.com/1.jpg'
)
```

>!
- 当需要刷新的 URL 较多时，为避免 GET 请求长度超出限制，建议使用 POST 方式调用此接口。
- POST 请求大小限制为1MB，超出大小限制则会返回状态码501。若需提交较多 URL，请拆分为多批次提交。

### 结果示例
```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "count": 1,
        "task_id": "1480069888795584532"
    }
}
```

```json
{
    "code": 4000,
    "message": "(9110)没有这个域名的信息 cdn no such host",
    "codeDesc": "9110"
}
```

