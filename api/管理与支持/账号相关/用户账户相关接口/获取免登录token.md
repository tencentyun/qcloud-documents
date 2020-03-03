## 1. 接口描述

域名：account.api.qcloud.com
接口名：GetAccountToken

获取免登录token，使用token跳转可以免去登录流程。

## 2. 输入参数

|参数名称|是否必选|类型|描述|
|-------|-------|----|---|
|uin|是|String|免密登录的uin，必须为请求方的主帐号uin或者协作者uin|

## 3. 输出参数

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code| Int| 错误码（0：成功，其他值：失败）。|
| message| String| 错误信息。|
| data| Array| 返回数据|

data是实际数据返回，数据接口如下：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| token| String| 免登录token|

## 4. 示例

输入
<pre>
  https://account.api.qcloud.com/v2/index.php?Action=GetAccountToken
  &uin=9809876615
  &<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>

输出
```
{
    "code": 0,
    "message": "",
    "data": {
        "token": "22f53160ead00947ac5eacf69093c7dd"
    }
}
```

## 5. 使用token跳转流程

* 跳转url为：https://cloud.tencent.com/login/sync?token=22f53160ead00947ac5eacf69093c7dd&s_url=https%3A%2F%2Fconsole.cloud.tencent.com
* token填入使用本api获得的token。
* s_url填入跳转到腾讯云的目标页面。
* token生成后1分钟内有效，同一只能使用一次。
