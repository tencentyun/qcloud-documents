The abnormal scaling configuration mentioned earlier means that the templates are damaged due to the scale-up, which invalidates the scaling group.
Similarly, there are some other factors that result in temporary invalidation of the scaling group.

> Note: The scaling group will become valid again when the factors resulting in the invalidation are eliminated.

## Indicator for Invalid Scaling Group

A red "!" mark beside the scaling group name on the console indicates the group is invalid.

## Why A Scaling Group Becomes Invalid

Scaling group invalidation is actually a prediction about risks - that machines (purchased manually or through AS) cannot be created in your account environment, or that the associated resources (CLB or VPC) after such creation are deleted.

Scaling group invalidation is actually a mechanism to identify risks in advance, which helps avoid any failure when you have a real scale-out need and therefore greatly improve the security of your cluster.

## Check the Causes for Scaling Group Invalidation

Hover your cursor over the "!" mark beside the scaling group to check the causes:

![](https://mc.qcloudimg.com/static/img/6eb6ec0402cfcc10951b39796ff6d5f0/009.jpg)

## Causes for Scaling Group Invalidation

| No. |  Cause | Description |
| -------- | --------|-------- |
| 1 |   Insufficient account balance | Your account balance is not enough for the resources required for expanding |
| 2 | The CLB is deleted | The CLB is deleted, resulting in the inability to register the machines to scale up on CLB |
| 3 | Insufficient CVM quota | Tencent Cloud currently allows a maximum of 30 postpaid CVMs for each account in each availability zone |
| 4 | Resources sold out | Postpaid CVMs are sold out in the availability zone |
| 5 | VPC or subnet is deleted | The VPC or subnet the scaling group directs to is deleted, resulting in the inability to create machines |

## When A Scaling Group Becomes Invalid

- Capacity expanding is not available;
- Capacity reducing is not affected;
- The limits on maximum and minimum group sizes and expected number of instances work normally;

## Recovering An Invalid Scaling Group

Below are the measures you can take to recover an invalid scaling group:
s
| No. |     Cause | Solution |
| -------- | --------|-------- |
| 1 | Insufficient account balance | Top up your account |
| 2 | The CLB is deleted | Redirect to an existing CLB |
| 3 | Insufficient CVM quota| Apply for a higher quota (please contact our sales representatives) |
| 4 | Resource sold out | Please try another availability zone|
| 5 | VPC or subnet is deleted | Redirect to an existing subnet |

