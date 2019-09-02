## Types of Alarms

There are four types of Tencent Cloud Monitor alarms， including basic monitor alarm, cloud automated testing alarm, custom message alarm and custom monitor alarm

| Alarm Type                      | Description                              |
| ------------------------------- | ---------------------------------------- |
| Basic alarm                     | Alarms regarding the basic monitoring metrics supported by Tencent Cloud, such as CVM CPU utilization, disk utilization and so on. |
| Cloud automated testing alarm | Alarms created by the automated testing tasks that were configured by users in the [Cloud Automated Testing](https://cloud.tencent.com/document/product/280) console. |
| Custom message alarm            | Alarms created by the Cloud Monitor [Custom Message](https://cloud.tencent.com/document/product/248/6218) service that is used by users. |
| Custom monitor alarm            | Alarms created by the Cloud Monitor [Custom Monitor](https://cloud.tencent.com/document/product/248/6214) service that is used by users |

## Alarm Channel

Currently, Tencent Cloud supports sending alarm messages via SMS and email.

All alarms are sent via these two channels by default. If you just want to receive alarms from one channel, you can go to the Tencent Cloud console and check if your email/mobile phone has been correctly configured and verified.

There is a quota limit for the SMS channel (no limit for email channel). Once the SMS quota is reached, alarms will no longer be sent via this channel.


## SMS Quota

Currently there is a quota limit for Tencent Cloud's SMS alarm channel. The quota consists of free quota and additional quota purchased by the user.

The system will notify the user when the monthly SMS quota has been exhausted, in which case alarms in that month will no longer be sent via the SMS channel. The email channel is not affected.

Users can purchase additional SMS quota if the free amount is not enough to satisfy their need.

## Quota Type

| Quota Type | Description  | 
|---------|---------|
| Free quota | Each month, users are provided with a fixed amount of free SMS quota to send alarm SMS.| 
| Additional quota|Additional SMS quota could be purchased by users when the free quota is not enough to satisfy their demand.|

## Free Quota Details

|Alarm type | Free quota amount| Distribution rule |
|---------|---------|---------|
| Basic alarm | 1000 messages/month | Quota is reset to 1000 at the first day of each month, regardless of the remaining quota in the previous month |
|Cloud automated testing alarm|1000 messages/month|Quota is reset to 1000 at the first day of each month, regardless of the remaining quota in the previous month|
|Custom message alarm|1000 messages/month|Quota is reset to 1000 at the first day of each month, regardless of the remaining quota in the previous month|
|Custom monitor alarm|1000 messages/month|Quota is reset to 1000 at the first day of each month, regardless of the remaining quota in the previous month|


## Billing Mode of Additional Quota

There are different quotas for different types of alarms, therefore you need to purchase quotas for basic alarms, cloud automated testing alarms, custom message alarms and custom monitor alarms separately.

|Additional Quota Amount|Additional Quota Price|
|---------|---------|
|< 100 messages| 0.055|
|≥ 100 messages, < 500 messages	|0.052|
|≥ 500 messages, < 1000 messages|0.050|
|≥ 1000 messages|0.045|

>Deduction rule: When alarm messages are sent, the quota will be deducted from the free quota first, then from the additional quota if the free quota has been exhausted

>Quota validity: Alarm quota has a long-term validity. There is no time limit for purchased quota.

## Quota Calculation

1.The quotas for different alarm types are independent from each other and are calculated separately. That is, every developer has a fixed free alarm SMS quota for every alarm type in each month. If you have used up the SMS quota for one alarm type, SMS quota for other alarm types won't be affected.

2.The amount deducted from the quota is determined by the actual number of messages received by users. For example, if a user configured 10 recipients for receiving a certain alarm message (i.e. a total of ten messages will be sent to the 10 recipients when the alarm is triggered), 10 messages will be deducted from the corresponding SMS quota.

Note: If a user configured repetitive alarm feature, there are 10 users in the recipient group of a certain alarm, and the alarm is configured to be sent repeatedly every hour. If the alarm lasts for 24 hours, the amount deducted from message quota will be 10*24=240. Please be aware of your SMS quota usage when you use the repetitive alarm feature.

3.When alarm messages are sent, the quota will be deducted from the user's free quota first, then from the additional quota if the free quota has been used up.