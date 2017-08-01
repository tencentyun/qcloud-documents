## 1. Create Alarm Rules

Now we create an alarm rule based on the metric and statistical type: send an alarm about the process with 80% or higher CPU utilization for 2 statistical periods and the machine ip. In this example, we use API for creation. Users can also create in CCM console.

>Note: For more information on how to generate Signature parameter, please see API [Authentication](https://www.qcloud.com/doc/api/255/4278)

```
#curl -k "https://monitor.api.qcloud.com/v2/index.php?Action=CreateAlarmRule
&SecretId=AKIDlgRMo1j074b1l6nwReIvSk3sO0ssGQlC
&Nonce=14971
&Timestamp=1457430090
&Region=gz
&namespace=proc_monitor
&metricName=proc_cpu
&dimensionNames.0=proc_name
&dimensionNames.1=ip
&period=300
&statistics=max
&constancy=2
&threshold=80
&operatorType=>
&Signature=aGftupI7YXRRInk9JT9tru7FzKM%3D
&receiversId=8888"
```
The following values will be returned:

```
# { "code": 0,  "message": "", "data": { "alarmRuleId": "policy-eqzqq79naz" } }
```

The cloud API returns an alarm rule ID: policy-eqzqq79naz, which is required for the further operations on the alarm rules. You can query this ID using DescribeAlarmRuleList in case you forget.

Note:

- You need to bind an alarm receiving group (receiversId) (ID is 8888) during configuration. If this parameter is left empty, the alarm message will not be sent to any user. You can use the API BindAlarmRuleReceivers to bind a specific monitoring object to receive the alarm SMS messages and emails.

- The parameter isWild is not specified in the above calling. A non-wildcard rule is created by default. The non-wildcard will become effective if you bind a specific alarm object. If isWild=1 is specified, a wildcard rule is created. The rule is valid for all the objects without the need to bind a specific object.

## 2. Bind Alarm Rule to Monitoring Object
In this example, we use API for creation. Users can also create in CCM console.

>Note: For more information on how to generate Signature parameter, please see API [Authentication](https://www.qcloud.com/doc/api/255/4278)

```
#curl -k "https:// monitor.api.qcloud.com/v2/index.php?Action=BindAlarmRuleObjects
&SecretId=AKIDlgRMo1j074b1l6nwReIvSk3sO0ssGQlC
&Nonce=8573
&Timestamp=1457431999
&Region=gz
&alarmRuleId=policy-eqzqq79naz
&dimensions.0.name=ip
&dimensions.0.value=1.2.3.5
&dimensions.1.name=proc_name
&dimensions.1.value=daemon2
&Signature=wxreGK7XUZQtLluaKUbUAwbQbtI%3D"
```

The following values will be returned:

```
# { "code": 0, "message": "" }
```
　　
Since the rule we just created is a non-wildcard rule, here we bind the object ip=1.2.3.5&proc_name=daemon2 to the alarm rule. CCM will determine whether to send an alarm to the object and send an alarm to the receiving group (ID is 8888) when triggering the alarm rule.



