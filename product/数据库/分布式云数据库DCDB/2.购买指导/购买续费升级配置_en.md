>This feature is not available until formal billing.

## Purchasing Instance

Click and select the instance to purchase in the Tencent Cloud product purchase page. You can purchase up to 64 shards in the page each time. Submit a ticket to purchase more.

> Initialization is required for the purchased instances to function normally.

## Upgrading Instance

>Upgrade operation will upgrade current DCDB instances to a higher specification. Since distributed database is composed of multiple shards, instance upgrade solutions include "Add Shard" and "Upgrade Shard". The service does not stop during the upgrade process, but some of the shards may become read-only for several seconds, so it is recommended to upgrade your instances during off-peak business hours.

### Adding Shard
Go to **Console** -> **Distributed Cloud Database** and click **Add Shard**. Select the number of new shards to be added and their specifications to complete the upgrade process. **The feature is not supported for the current version, but will become available on August 1st, 2017.**
![](//mccdn.qcloud.com/static/img/b9cff4d43c31ffac56b2296945ac2337/image.png)
![](//mccdn.qcloud.com/static/img/6742591dcd12c8f56e6a11cdf0670e79/image.png)

### Upgrading Shard
This operation upgrades the specification of a single shard to a higher level without adding new shards. **The feature is not supported for the current version and will become available on August 1st, 2017.**

1.	Go to **Console** -> **Distributed Cloud Database**, click **Management** to enter the management page, choose **Shard Management** and click on the shard to be upgraded to complete the upgrade process.
![](//mccdn.qcloud.com/static/img/d77ef38bc7becc785decbd51fd285b84/image.png)
![](//mccdn.qcloud.com/static/img/0bb016e4be65e8865a86cd4f4eb20c59/image.png)

**Upgrade fee = (Target specification unit price - Original specification unit price) x Remaining usage period**

## Renewing Instance

### 1. Renewal

Renewal means to extend the usage period of DCDB instance. You can do this in the following ways:

- Go to **Console** -> **Distributed Database** -> **DCDB** -> **More** -> **Batch Renew**, select the instance to be renewed, and click **Renew**, **Batch Renew**, or **Configure Auto Renew**.
- Go to **User Center** -> **Renewal Management** -> **Distributed Database (DCDB)**, select the instance(s) to be renewed, and click **Renew** or **Batch Renew**
- Go to **User Center** -> **Renewal Management** -> **Distributed Database (DCDB)** to renew the instance automatically.

> The Auto Renew feature will automatically renew instance upon expiration, which requires sufficient balance in your account. Auto renewal will not be automatically reattempted if it fails.

### 2. Renewal Fee

Renewal fee = Monthly price of instance x Renewal period (month) + (Monthly price of instance/30 x Renewal period (day))

>Note: The renewal fee for a period less than a month is calculated based on monthly price and the number of days to renew. For example, an instance with a monthly price of 60 CNY expires on April 5th. Suppose you want to renew the instance to May 20th, then the expiration date is adjusted to the 20th day of each month, and the renewal fee is 90 CNY (60+60÷30×15).

