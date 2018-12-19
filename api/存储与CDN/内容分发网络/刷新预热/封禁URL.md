## 接口描述

**ForbidBadUrl**  提交违规 URL 进行批量封禁，封禁后的 URL 通过 CDN 访问会返回 403。

请求域名：<font style="color:red">cdn.api.qcloud.com</font>

**注意事项：**

+ 接口通过白名单控制，如有需要，请联系腾讯云 CDN 团队
+ 每一个账号每日封禁 URL 上限为 3000 条，每次最多可提交 100 条
+ 提交的 URL 中域名必须为该账号下已接入的加速域名
+ 提交的 URL 中域名的状态需要为【已启动】或【部署中】
+ 提交的 URL 必须以 http:// 或 https:// 开头
+ 同一条 URL 封禁、解封的时间间隔需要大于 15 分钟
+ 若 URL 本身不可访问，则不会触发封禁操作，也无法进行解封以及记录查看
+ 调用频次限制为 30次/分钟

[查看调用示例](https://cloud.tencent.com/document/product/228/1734)

## 入参说明
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见[公共请求参数](https://cloud.tencent.com/doc/api/231/4473)页面。其中，此接口的 Action 字段为 ForbidBadUrl。

| 参数名称   | 是否必选 | 类型     | 描述        |
| ------ | ---- | ------ | --------- |
| urls.n | 是    | String | 需要封禁的 URL |

### 详细说明

支持刷新一个或多个 URL，刷新多个URL时，参数传入方式可参考：
```
urls.0=http://www.abc.com/1.jpg&urls.1=http://www.abc.com/2.jpg
```
## 出参说明

| 参数名称     | 类型     | 描述                                       |
| -------- | ------ | ---------------------------------------- |
| code     | Int    | 公共错误码，0表示成功，其他值表示失败。<br/>详见错误码页面的[公共错误码](https://cloud.tencent.com/doc/api/231/5078#1.-.E5.85.AC.E5.85.B1.E9.94.99.E8.AF.AF.E7.A0.81) |
| message  | String | 模块错误信息描述，与接口相关                           |
| codeDesc | String | 英文错误信息，或业务侧错误码。<br/>详见错误码页面[业务错误码](https://cloud.tencent.com/document/product/228/5078#2.-.E6.A8.A1.E5.9D.97.E9.94.99.E8.AF.AF.E7.A0.81) |
| data     | Array  | 详细说明见下文                                  |

### 详细说明

#### data

| 参数名称         | 类型   | 描述                   |
| ------------ | ---- | -------------------- |
| dealing_urls | Int  | 提交成功，已在处理队列中等待封禁的URL |


## 调用案例

### 示例参数
```
urls.0：https://www.test.com/1.jpg
```

### GET 请求

GET 请求需要将所有参数都加在 URL 后：

```
https://cdn.api.qcloud.com/v2/index.php?
Action=ForbidBadUrl
&SecretId=XXXXXXXXXXXXXXXXXX
&Timestamp=1462521223
&Nonce=123456789
&Signature=XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
&urls.0=https%3A%2F%2www.test.com%2F1.jpg
```

### POST 请求

POST请求时，参数填充在 HTTP Request-body 中，请求地址：

```
https://cdn.api.qcloud.com/v2/index.php
```

参数支持 form-data、x-www-form-urlencoded 等格式，参数数组如下：

```
array (
  'Action' => 'ForbidBadUrl',
  'SecretId' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'Timestamp' => 1462864833,
  'Nonce' => 1149033341,
  'Signature' => 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
  'urls.0' => 'https://www.test.com/1.jpg'
)
```
### 结果示例

```json
{
    "code": 0,
    "message": "",
    "codeDesc": "Success",
    "data": {
        "dealing_urls": [
            "https://www.test.com/1.jpg"
        ]
    }
}
```



