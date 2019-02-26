Callback API allows your system to directly receive alarm notifications from Tencent Cloud. By using HTTP POST requests, the API provides a feature of pushing alarm messages to publicly accessible URLs. Users may proceed further based on the alarm messages pushed by the callback API.

## Usage

* Callback API: Users need to provide a URL address which is able to receive HTTP POST requests, and is accessible through the public network, as the callback address.

* Trigger callback: The trigger policy is the same as that of alarm SMS and emails. Alarm message will be sent via the callback API when the alarm policy created by user is triggered and the alarm policy recovers. Repetitive alarm feature is also supported by the callback API.

* Bind callback API: Users may configure callback API by clicking "Show Advanced Options" during the third step of creating alarm policy (Associate Alarm Recipient Group), or add callback API from the Alarm Policy Details page. You can only bind one alarm callback URL to each alarm policy group.

* Response content: After sending alarm message to the URL that is bound by user, we need to receive the following response content in order to make sure the user has successfully received the message. Otherwise we will send the alarm message repeatedly (up to three times).

  > sessionId, used to authenticate callback request
  >
  > retCode, used to determine whether the request has been successfully sent
```
{
    sessionId: "xxxxxxxx",
    retCode: 0
}
```


## Callback Parameter

The callback API will send data in JSON format via HTTP POST requests. The parameters are as follows:
```
{
       "sessionId": "xxxxxxxx",
       "alarmStatus": 1,
       "alarmObjInfo": {
            "region": "gz",  // This is not displayed for products that are not region-specific
            "namespace": "qce/cvm",      // Product namespace
            "dimensions": {               // The content in the "dimension" field varies for different products
                "unInstanceId": "ins-o9p3rg3m",  
                "objId":"xxxxxxxxxxxx",
            }
       }
       "alarmPolicyInfo": {
                "policyId": "policy-n4exeh88",   // Alarm Policy Group ID
                "policyType": "cvm_device",     // Alarm policy type
                "policyName": "test",      // Alarm policy group name
                "conditions": {
                    "metricName": "cpu usage",         // Metric Name
                    "metricShowName": "CPU utilization",       // Displayed metric name
                    "calcType": ">",              // This is not displayed for metrics without threshold
                    "calcValue": "90",            // This is not displayed for metrics without threshold
                    "currentValue": "100",       // This is not displayed for metrics without threshold
                    "unit": "%",                 // This is not displayed for metrics without threshold
                    "period": "60",              // This is not displayed for metrics without threshold
                    "periodNum": "1",            // This is not displayed for metrics without threshold
                    "alarmNotifyType": "continuousAlarm",    // Whether repetitive alarm is supported. This is not displayed for metrics without threshold
                    "alarmNotifyPeriod": 300                 // Frequency for repetitive alarm. This is not displayed for metrics without threshold
                }
                "firstOccurTime": "2017-03-09 07:00:00",     // Time point when the alarm is triggered for the first time
                "durationTime": 500,       // Alarm duration (unit: second)
                "recoverTime": "0"     // Alarm recovery time (0 when not recovered)
        }
}
```
