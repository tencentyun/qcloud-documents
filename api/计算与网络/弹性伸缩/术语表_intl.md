To allow you to get familiar with auto scaling services more quickly, we provide the definitions of some commonly used terms in the following table:

| Term | Full Name | Full Name | Description |
|---------|---------|---------|---------|
| AS | Auto Scaling | [Auto Scaling](https://cloud.tencent.com/doc/product/377/3154) | A management service that can automatically adjust computing resources based on users' business needs and policies.  |
| scalingGroup | Scaling Group | [Scaling Group](https://cloud.tencent.com/doc/product/377/3155#1.-.E4.BC.B8.E7.BC.A9.E7.BB.84)| A collection of CVM instances that follow the same rule and apply to the same scenario. Auto scaling group defines information such as the maximum and minimum number of CVM instances included.  |
| scalingConfiguration | Scaling Configuration | [Scaling Configuration](https://cloud.tencent.com/doc/product/377/3155#2.-.E5.90.AF.E5.8A.A8.E9.85.8D.E7.BD.AE) | The scaling configuration is a template for automatically creating a CVM. It contains image IDs, types of CVM instance, types and capacity of system disk and data disk, key pair, security group, etc. Scaling configuration must be specified when creating a scaling group. Once the scaling configuration is created, you cannot edit its attributes.  |
| scalingScheduledTask | Scaling Scheduled Task | [Scaling Scheduled Task](https://cloud.tencent.com/doc/product/377/3155#3.-.E5.AE.9A.E6.97.B6.E4.BB.BB.E5.8A.A1) | A type of auto scaling activity. The CVM instance is automatically added or reduced at a fixed time point, which is supported for repeating periodically. |
| scalingPolicy | Scaling Alarm Policy | [Scaling Alarm Policy](https://cloud.tencent.com/doc/product/377/3155#5.-.E5.91.8A.E8.AD.A6.E4.BC.B8.E7.BC.A9) |The CVM instance is automatically added or reduced according to cloud monitor metrics (e.g. CPU, memory, network traffic). |
| cooldown | Cooldown Period | [Cooldown Period](https://cloud.tencent.com/doc/product/377/3155#6.-.E5.86.B7.E5.8D.B4.E6.97.B6.E9.97.B4) | A period of time when the corresponding scaling group is locked after a scaling activity is completed. During this period, this scaling group cannot execute other scaling activities. |


