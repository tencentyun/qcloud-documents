![](https://mc.qcloudimg.com/static/img/c90b78acfb2e1501d0c94f6546efbd2e/image.png)

## Balance Forewarning
We will estimate the remaining available period of your account based on your usage of pay-by-usage resources under your account and your balance over the past 24 hours. We will send you a balance forewarning message if the period is less than 5 days. The forewarning message will be sent by email and SMS to Tencent Cloud account creator and all the collaborators.

## Arrears Forewarning

For Cloud Message Queue (CMQ), fees are deducted on the hour. (For more information on billing, please see [Price Overview](/doc/product/406/4563)). When your account balance is a negative value (Point 1 in the figure above), we will notify Tencent Cloud account creator and all the collaborators via email and SMS.

## Arrears Processing

- Within 2 hours from the point when your balance becomes negative, your CMQ remains usable and continues to deduct fees.

- 2 hours later (Point 2 in the figure above), CMQ will stop services (only query for details is available) and billing.

- After CMQ stops services, any operation for CMQ features will become unavailable. When the account balance has been topped up to an amount greater than 0, CMQ service will become available. Unprocessed and accumulated message data will be automatically released based on the expiration time of the message set in the queue, and the released data cannot be recovered. If all messages in the queue have expired, the queue will be deleted automatically.

- Tencent Cloud account creator and all the collaborators will be notified of the deletion of CMQ queues via email and SMS.

> Note:
> 
1) When you do not use pay-by-usage resources any longer, please terminate them promptly to avoid further fee deduction. 
2) After the resource is terminated, the data will be cleared and cannot be recovered. 
3) Actual resource consumption of users may change, so there may be some error in the balance forewarning. 
4) The msgRetentionSeconds of the queue identifies the maximum available time of the message in the queue. Whether or not the message has been retrieved after being sent to the queue, it will be deleted after the period of time specified in this parameter.

