## 1. 接口描述
域名:cdn.api.qcloud.com
接口名:RefreshCdnUrl

url刷新

## 2. 输入参数
| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| urls.n (urls 为数组，此处入参需要填写数组元素 ) | 是 | String | |


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败|
| message | String | 错误信息|


## 4. 示例
输入
```
https://cdn.api.qcloud.com/v2/index.php?Action=RefreshCdnUrl
&urls.0=http://ping.cdn.qcloud.com/xxfdsfdssdfsdfsgfdg
&COMMON_PARAMS
```
输出
```
{
    "code":"0",
    "message":""
}
```

