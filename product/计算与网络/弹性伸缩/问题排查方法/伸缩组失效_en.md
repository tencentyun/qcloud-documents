The abnormal scaling configuration mentioned earlier means that the templates are damaged due to the scale-up, which invalidates the scaling group.
Similarly, there are some other factors that result in temporary invalidation of the scaling group.

> Note: The scaling group will become valid again when the factors resulting in the invalidation are eliminated.

## How to Identify An Invalid Scaling Group

A red "!" mark beside the scaling group name on the console  indicates the group is invalid.

## Why A Scaling Group Becomes Invalid

Scaling group invalidation is actually a prediction about risks - that machines (purchased manually or through AS) cannot be created in your account environment, or that the associated resources (CLB or VPC) after such creation are deleted.

Scaling group invalidation is actually a mechanism to identify risks in advance, which helps avoid any failure when you have a real scale-out need and therefore greatly improve the security of your cluster.

## Check the Causes for Scaling Group Invalidation

Hover your cursor over the "!" mark beside the scaling group to check the causes:

![](https://mc.qcloudimg.com/static/img/6eb6ec0402cfcc10951b39796ff6d5f0/009.jpg)

## Causes for Scaling Group Invalidation

| No. |  Cause | Description |
| -------- | --------|-------- |
| 1 |   Insufficient balance | No sufficient balance in the account to pay for the resources to scale up |
| 2 | The CLB is deleted | The CLB is deleted, resulting in the inability to register the machines to scale up on CLB |
| 3 | Insufficient CVM quota | Tencent Cloud currently allows a maximum of 30 pay-by usage CVMs for each account in each availability zone |
| 4 | Resources sold out | Pay-by usage CVMs are sold out in the availability zone, and cannot be purchased manually or automatically |
| 5 | VPC or subnet is deleted | The VPC or subnet the scaling group directs to is deleted, resulting in the inability to create machines |

## Effect of Scaling Group Invalidation

The scaling group will not stop working immediately after it becomes invalid:

- Normal scale-down activities will not be affected;
- The limits on maximum and minimum group sizes and expected number of instances will still be applicable;
- The scale-up activities will stop, as your environment no longer has what it takes to create CVMs.

## Recover An Invalid Scaling Group

Below are the measures you can take to recover an invalid scaling group:

| No. |     Cause | Measure |
| -------- | --------|-------- |
| 1 | Insufficient balance | Top up |
| 2 | The CLB is deleted | Redirect to an existing CLB |
| 3 | Insufficient CVM quota| Key customers may apply for a higher quota |
| 4 | Resource sold out | Try again later |
| 5 | VPC or subnet is deleted | Redirect to an existing subnet |

