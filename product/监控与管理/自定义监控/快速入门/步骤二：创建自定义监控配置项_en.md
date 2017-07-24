
## 1. Create Custom Namespace
In this example, we use API for creation. Users can also create in CCM console.

>Note: For more information on how to generate Signature parameter, please see API [Authentication](https://www.qcloud.com/doc/api/255/4278)

Execute the following commands to create a namespace:

```
# curl -k https://monitor.api.qcloud.com/v2/index.php?Action=CreateNamespace
          &SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
          &Nonce=54579
          &Timestamp=1457427062
          &Region=gz
          &namespace=proc_monitor
          &Signature=K%2FX6J6hnjTIE25QK8klMZMJWDGk%3D
```
The following values will be returned:

```
# {"code": 0,"message": ""}
```

## 2. Create Custom Metric

Create a metric (proc_cpu) in the namespace (proc_monitor) you just created, and specify the dimension (proc_name, ip) structure that is already configured using the parameter dimensionNames.

In this example, we use API for creation. Users can also create in CCM console.

>Note: For more information on how to generate Signature parameter, please see API [Authentication](https://www.qcloud.com/doc/api/255/4278)

```
# curl -k https://monitor.api.qcloud.com/v2/index.php?Action=CreateMetric
          &SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
          &Nonce=15945
          &Timestamp=1457428021
          &Region=gz
          &namespace=proc_monitor
          &metricName=proc_cpu
          &metricCname=%E8%BF%9B%E7%A8%8Bcpu%E4%BD%BF%E7%94%A8%E7%8E%87
          &unit=percent
          &dimensionNames.0=proc_name
          &dimensionNames.1=ip
          &Signature=8w0Nwaxb6ZNh3ROPmHruaVz1meE%3D
```
The following values will be returned:

```
# { "code": 0, "message": ""}
```

## 3. Create Statistical Type for Metric 
You can add multiple sets of statistical method and period using the parameter statisticsType. Here, we add one set: statistical period is 300 sec, and statistical method is max.

In this example, we use API for creation. Users can also create in CCM console.

>Note: For more information on how to generate Signature parameter, please see API [Authentication](https://www.qcloud.com/doc/api/255/4278)

```
#curl -k https://monitor.api.qcloud.com/v2/index.php?Action=CreateMetricStatisticsType
          &SecretId=AKIDz8krbsJ5yKBZQpn74WFkmLPx3gnPhESA
		  &Nonce=13133
		  &Timestamp=1457428414
		  &Region=gz
		  &namespace=proc_monitor
		  &metricName=proc_cpu
		  &dimensionNames.0=proc_name
		  &dimensionNames.1=ip
		  &statisticsType.0.period=300
		  &statisticsType.0.statistics=max
		  &Signature=hcFFCJcHYiLW0PH%2F%2FuJ%2FgFeDRtY%3D
```
The following values will be returned:

```
# { "code": 0, "message": ""}
```
