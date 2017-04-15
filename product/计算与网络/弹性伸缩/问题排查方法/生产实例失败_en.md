This document provides information about the failure of AS to launch CVM instances, potential causes, and the steps you can take to resolve the issues.

## Causes for Failure of AS to Produce Machines

There are mainly 6 causes for scale-up failures:

| No. | Cause | Description | 
|---------|---------|---------|
| 1 | Scaling configuration failure | A scaling configuration failure occurs because the associated resources (images, snapshots, security groups, etc.) have been deleted. Enter the scaling configuration details page to check the mistakenly deleted resources. The mistakenly deleted resource are marked in red.  | 
| 2 | Abnormal scaling group | This occurs because the associated LB or VPC has been deleted, or the account balance is insufficient.  | 
| 3 | Insufficient CVM purchase quota | Every user has CVM purchase quota. The default quota of pay-by-usage CVM is 30 per availability zone. AS will not be able to produce machines if this quota is exceeded.  | 
| 4 | Model does not exist | The model defined in your scaling configuration is not correct or sold out.  | 
| 5 | Resources sold out |Tencent Cloud resources are sold out (of very rare occurrence).  | 
| 6 | Other background error | Refer to the scaling activity details page for the detailed reasons (of very rare occurrence).  | 

Troubleshooting Steps

### 1. Check the Descriptions of the Reasons

Tencent Cloud AS provides the industry's most descriptive presentation of causes for failed scaling group activities.

You can check the causes directly in the "Scaling Activity" in the scaling group management page:

![](https://mc.qcloudimg.com/static/img/51e997b42d2d7e7ce6d8bf3f2e662411/0.jpg)

### 2. Perform Actions Based on Tips

You can perform actions based on the causes for failed scaling group activities. See the following table.

| No. | Causes | Action | 
|---------|---------|---------|
| 1 | Image is deleted | 	Change scaling configuration | 
| 2 | CLB is deleted | Modify CLB | 
| 3 | Data snapshot is deleted | Change scaling configuration | 
| 4 |Security group is deleted | Change scaling configuration | 
| 5 | Subnet is deleted | Modify the subnet | 
| 6 | Resources sold out | Scale-up operation paused | 
| 7 | Nonexistent model | Change scaling configuration | 
| 8 | Insufficient background resources | Stop scale-up activities| 
| 9 | Insufficient quota | Decrease the number of CVMs to scale up, or send a ticket to apply for a higher quota | 
| 10 | Insufficient balance | Top up | 
| 11 | Key is deleted | Change scaling configuration | 


