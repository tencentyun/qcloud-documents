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

