回调接口可以让您的系统直接收到腾讯云的告警通知，提供将告警信息通过 HTTP 的 POST 请求推送到用户公网可访问的 url 的功能，用户可基于回调接口推送的告警信息做进一步的处理。

## 使用方法

* 回调接口：用户需要提供能接收 HTTP POST 请求的，公网可访问的 url 地址，作为回调地址。

* 回调触发：触发逻辑与告警短信、邮件一致，当用户创建的告警策略被触发、告警策略恢复时，均会通过回调接口发送告警消息。回调接口也支持重复告警。

* 绑定回调接口：用户可在创建告警策略第三步：关联告警接收组的时候点击展开高级选项，配置回调接口，也可在告警策略详情页内添加回调接口。一个告警策略组只可绑定一个告警回调 url。

* 返回内容：向用户绑定的 url 发出告警信息后，我们需要接收到以下的返回内容，以表明用户已成功接收信息；否则我们将重复发送告警信息，最多发送三次。

  > sessionId, 用于鉴别回调请求
  >
  > retCode，用于判断请求是否发送成功
```
{
    sessionId: "xxxxxxxx",
    retCode: 0
}
```


## 回调参数

回调接口通过 HTTP 的 POST 请求发送 JSON 格式的数据，参数如下：
```
{
       "sessionId": "xxxxxxxx",
       "alarmStatus": 1,
       "alarmObjInfo": {
            "region": "gz",  // 不分地域的产品不展示
            "namespace": "qce/cvm",      // 产品的名字空间
            "dimensions": {               // dimensions字段里的内容不同产品有差异
                "unInstanceId": "ins-o9p3rg3m",  
                "objId":"xxxxxxxxxxxx",
            }
       }
       "alarmPolicyInfo": {
                "policyId": "policy-n4exeh88",   // 告警策略组ID
                "policyType": "cvm_device",     // 告警策略类型
                "policyName": "test",      // 告警策略组名称
                "conditions": {
                    "metricName": "cpu usage",         // 指标名称
                    "metricShowName": "CPU 利用率",       // 指标展示名称
                    "calcType": ">",              // 无阈值的指标不展示
                    "calcValue": "90",            // 无阈值的指标不展示
                    "currentValue": "100",       // 无阈值的指标不展示
                    "unit": "%",                 // 无阈值的指标不展示
                    "period": "60",              // 无阈值的指标不展示
                    "periodNum": "1",            // 无阈值的指标不展示
                    "alarmNotifyType": "continuousAlarm",    // 是否支持重复告警,无阈值的指标不展示
                    "alarmNotifyPeriod": 300                 // 重复告警的频率,无阈值的指标不展示
                }
                "firstOccurTime": "2017-03-09 07:00:00",     // 第一次触发告警的时间
                "durationTime": 500,       // 告警持续时间（单位：s）
                "recoverTime": "0"     // 告警恢复时间（未恢复时为0）
        }
}
```