
Welcome to use Tencent Cloud Auto Scaling (AS)!
Auto Scaling (AS) can automatically adjust computing resources according to users' business needs and policies. AS can properly increase or decrease CVM instances and complete the configuration based on the scheduled, periodic or monitoring policies specified by users. It can automatically increase CVM instances to ensure smooth and healthy business operations when business demands are soaring, and reduce CVM instances to save resources and costs when business demands are decreasing.
Users can perform such operations such as managing scaling groups and setting scaling configurations. For information on supported operations, please refer to <a href="https://cloud.tencent.com/doc/api/372/API%E6%A6%82%E8%A7%88" title="API Overview">API Overview</a>.
Before using these APIs, please make sure that you have a thorough understanding of <a href="https://cloud.tencent.com/doc/product/377/%E4%BA%A7%E5%93%81%E6%A6%82%E8%BF%B0" title="AS Product Overview">AS Product Overview</a> and [calling methods](https://intl.cloud.tencent.com/document/product/377/8940).

## 1. Glossary
To allow you to get familiar with auto scaling services more quickly, we provide the definitions of some commonly used terms in the following table:

| Term | Full Name | Full Name | Description |
|---------|---------|---------|---------|
| AS | Auto Scaling | [Auto Scaling](https://cloud.tencent.com/doc/product/377/3154) | A management service that can automatically adjust computing resources based on users' business needs and policies.  |
| scalingGroup | Scaling Group | [Scaling Group](https://cloud.tencent.com/doc/product/377/3155#1.-.E4.BC.B8.E7.BC.A9.E7.BB.84) | A collection of CVM instances that follow the same rule and apply to the same scenario.  |
| scalingConfiguration | Scaling Configuration | [Scaling Configuration](https://cloud.tencent.com/doc/product/377/3155#2.-.E5.90.AF.E5.8A.A8.E9.85.8D.E7.BD.AE) | The scaling configuration is a template for automatically creating a CVM. |
| scalingScheduledTask | Scaling Scheduled Task | [Scaling Scheduled Task](https://cloud.tencent.com/doc/product/377/3155#3.-.E5.AE.9A.E6.97.B6.E4.BB.BB.E5.8A.A1) | Perform AS activities as scheduled. |
| scalingPolicy | Scaling Alarm Policy | [Scaling Alarm Policy](https://cloud.tencent.com/doc/product/377/3155#5.-.E5.91.8A.E8.AD.A6.E4.BC.B8.E7.BC.A9) | Automatically perform AS activities based on cloud monitoring metrics. |
| cooldown | Cooldown Period | [Cooldown Period](https://cloud.tencent.com/doc/product/377/3155#6.-.E5.86.B7.E5.8D.B4.E6.97.B6.E9.97.B4) | A period of time when the corresponding scaling group is locked after a scaling activity is completed. |

## 2. API Quick Start
To use AS API, you need to complete at least the following three steps:
1. Create scaling configuration
You can use API [Create Scaling Configuration](/doc/api/372/创建启动配置) to create scaling configuration. It defines the configuration of a CVM instance automatically created through auto scaling.
2. Create a scaling group 
You can use API [Create a Scaling Group](/doc/api/372/创建伸缩组) to create a scaling group. You can specify the number of instances in the scaling group, select a scale-down policy to remove CVM instances, and select whether to add the scaling group to cloud load balance, etc.
3. Create a scaling policy
After creating a scaling group, you need to specify a scaling policy for the group, i.e., a policy to increase or decrease CVM instances according to your actual needs. You can use API [Create an Alarm Policy](/doc/api/372/创建告警策略) to create an alarm trigger policy to perform scaling activities based on cloud monitoring metrics (such as CPU utilization, and memory usage). You can also use API [Create a Scheduled Task](/doc/api/372/创建定时任务) to create a scheduled task that can be used to perform scaling activities as scheduled, and you can also set to execute the scheduled task periodically.

## 3. Service Limits
Currently, all users may use auto scaling service in any scenarios.
