>? **当前页面接口为旧版 API，未来可能停止维护，目前不展示在左侧导航。云服务器 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 <a href="https://cloud.tencent.com/document/api/213/15689" target="_blank">云服务器 API 3.0</a>。**
>

## 1. 接口描述
域名:vpc.api.qcloud.com
接口名:AttachNetworkInterface

绑定子机与弹性网卡

## 2. 输入参数
| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| vpcId | 是 | String | 私用网络ID或者统一ID，建议使用统一ID|
| networkInterfaceId | 是 | String | 弹性网卡Id|
| instanceId | 是 | String | 子机实例ID|


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败|
| message | String | 错误信息|
| data | Array | 描述（待补充） |
| data.taskId | Int | 描述（待补充）| 


## 4. 示例
输入
<pre>
https://vpc.api.qcloud.com/v2/index.php?Action=AttachNetworkInterface
&vpcId=vpc-lwmzdppp
&subnetId=subnet-fzyzn3r2
&instanceId=xxx-dfgda45
&networkInterfaceId=eni-kbe7jrs9
&<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>
输出
```
{
    "code":"0",
    "message":"",
    "data":{
        "taskId":"17382"
    }
}
```

