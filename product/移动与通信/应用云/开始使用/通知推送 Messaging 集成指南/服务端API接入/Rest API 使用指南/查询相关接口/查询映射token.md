查询应用某帐号映射的 token（查看帐号-token 对应关系）
URL 路径：`http://接口域名/v2/application/get_app_account_tokens?params`

### 请求参数
除了 [通用参数](https://cloud.tencent.com/document/product/666/15603) 外，还包括如下参数：

|参数名|	类型|	必需|	默认值|	描述|
|-|-|-|-|-|
|account|	string	|是|	无|	帐号|

### 响应结果
在通用返回结果参数中，result 字段的 json 如下：
```
{
 "tokens":["token1","token2"]
}
```
### 示例
MD5 加密前 url 用作生成 sign，Rest Api Url 为最终请求的 url（以下为 Android 推送示例，需替换通用参数后使用）。
#### MD5 加密前：

```
GETopenapi.xg.qcloud.com/v2/application/get_app_account_tokensaccess_id=2100240957account=easonshipushtestaccounttimestamp=1502699212f255184d160bad51b88c31627bbd9530
```

#### Rest Api Url:
```
http://openapi.xg.qcloud.com/v2/application/get_app_account_tokens?access_id=2100240957&account=easonshipushtestaccount&timestamp=1502699212&sign=015ef9e7fde208f2d12674f731e13e8c
```.qcloud
