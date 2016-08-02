## 1. 接口描述
域名：dayu.api.qcloud.com
接口名：RefreshDayuUrl

Url刷新

## 2. 输入参数
| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| urls.n  | 否 | String | 需要刷新的URL列表，此处可以传入Url数组。与dirs参数互斥，不能同时传入|
| dirs.n  | 否 | String | 需要刷新的目录列表，此处可以传入dirs数组。与urls参数互斥，不能同时传入|



## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码。0：成功，其他值：失败|
| message | String | 错误信息|
| data | Array | 返回的数组 |

**data结构**

| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| data.log_id | String | 刷新日志ID | 


## 4. 示例
输入
```
https://dayu.api.qcloud.com/v2/index.php?Action=RefreshDayuUrl
&urls.0=http://www.qq.com/index.html
```
输出
```
{
    "code":"0",
    "message":"",
    "data":{
        "log_id":"2156"
    }
}
```

