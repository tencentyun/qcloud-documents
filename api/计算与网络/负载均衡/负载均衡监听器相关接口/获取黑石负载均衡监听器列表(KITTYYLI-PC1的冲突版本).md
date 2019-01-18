## 1. 接口描述
域名:lb.api.qcloud.com
接口名:DescribeBmLoadBalancerListeners

获取黑石负载均衡监听器列表

## 2. 输入参数
| 参数名称 | 必选  | 类型 | 描述 |
|---------|---------|---------|---------|
| loadBalancerId | 是 | String | 负载均衡器ID|
| listenerIds.n | 否 | String | 监听器ID|
| protocol | 否 | Int | 监听器协议类型，2:TCP,3:UDP|
| loadBalancerPort | 否 | Int | 监听器端口|


## 3. 输出参数
| 参数名称 | 类型 | 描述 |
|---------|---------|---------|
| code | Int | 错误码, 0: 成功, 其他值: 失败|
| message | String | 错误信息|
| listenerSet.loadBalancerPort | Int | 负载均衡器监听端口| 
| listenerSet.instancePort | Int | 后端服务器监听端口| 
| listenerSet.protocol | Int | 监听器协议类型，2:TCP,3:UDP| 
| listenerSet.status | Int | 监听器的状态，包括：<br>0：绑定中，1：绑定成功，2：绑定失败，3：解绑中，4：解绑失败| 
| listenerSet.listenerName | String | 监听器名称| 
| listenerSet.listenerId | String | 监听器ID| 
| listenerSet.sessionExpire | Int | 会话保持时间| 
| listenerSet.healthSwitch | Int | 是否开启了检查：1（开启）、0（关闭）。| 
| listenerSet.timeOut | Int | 响应超时时间 | 
| listenerSet.intervalTime | Int | 检查间隔 | 
| listenerSet.healthNum | Int | 健康阀值 | 
| listenerSet.unhealthNum | Int | 不健康阀值| 


## 4. 示例
输入
<pre>
https://lb.api.qcloud.com/v2/index.php?Action=DescribeBmLoadBalancerListeners
&loadBalancerId=lb-k6p4918n
&<a href="https://cloud.tencent.com/doc/api/229/6976">公共请求参数</a>
</pre>
输出
```
{
    "code":"0",
    "message":"",
    "listenerSet":[
        {
            "loadBalancerPort":"80",
            "instancePort":"80",
            "protocol":"2",
            "status":"1",
            "listenerName":"1",
            "listenerId":"lbl-odn5baps",
            "sessionExpire":"900",
            "healthSwitch":"1",
            "timeOut":"6",
            "intervalTime":"10",
            "healthNum":"8",
            "unhealthNum":"8"
        }
    ],
    "totalCount":"1"
}
```

