## 1. 接口描述
本接口(RefreshDayuUrl)用于刷新URL列表或目录列表。
接口请求域名：dayu.api.qcloud.com

## 2. 输入参数
以下请求参数列表仅列出了接口请求参数，正式调用时需要加上公共请求参数，见<a href="https://www.qcloud.com/document/product/297/7291" title="公共请求参数">公共请求参数</a>
页面。其中，此接口的Action字段为RefreshDayuUrl。

| 参数名称 | 是否必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| urls.n  | 否 | String | 需要刷新的URL列表，此处可以传入Url数组。与dirs参数互斥，不能同时传入|
| dirs.n  | 否 | String | 需要刷新的目录列表，此处可以传入dirs数组。与urls参数互斥，不能同时传入|

## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 公共错误码，0表示成功，其他值表示失败。详见错误码页面的<a href="https://www.qcloud.com/document/product/297/7297" title="公共错误码">公共错误码</a>。 
| message | String | 模块错误信息描述，与接口相关。|
| data | Array | 返回的数组 |

其中，data参数的构成如下：

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| log_id | String | 刷新日志ID | 

## 4. 示例
<pre>
https://dayu.api.qcloud.com/v2/index.php?Action=RefreshDayuUrl
&<<a href="https://www.qcloud.com/document/product/297/7291">公共请求参数</a>>
&urls.0=http://www.qq.com/index.html
</pre>

返回示例如下：
```
{
    "code":"0",
    "message":"",
    "data":{
        "log_id":"2156"
    }
}
```
