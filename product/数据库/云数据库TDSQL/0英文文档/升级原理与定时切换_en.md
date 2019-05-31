> Since March 30, 2017, Tencent Cloud has provided timed upgrade switching capacity, to allow your business to be upgraded (switched) automatically at the lows of business. Principles and notes for this capacity are as follows:

## Database Upgrade Principle
When you click CDB for upgrade, cloud ops management system (ChiTu) will perform an upgrade by following the steps below (as shown in the figure below):

![](https://mc.qcloudimg.com/static/img/b746129256a7115a5fd108cbf0baefcd/%7B9EA720D4-E227-4DCB-9E1C-A13B8110CBA5%7D.png)

1. Assign a new instance (hereinafter "new instance") based on the configuration required for upgrade
2. Sync the data and configuration of instance to be upgraded (hereinafter "old instance") to new instance
3. After the synchronization, switch the routing at the Tencent Cloud gateway to the new instance for continuous use.

## Timed Upgrade Switching
As mentioned in the previous section, the last step of instance upgrade configuration is routing switching at the Tencent Cloud gateway. Therefore, we provide a capacity of switching at the specified time, to help clients switch database to a new configuration at the specified time (usually the lows of business), as shown below:

![](https://mc.qcloudimg.com/static/img/47ab9957b5822eef2bacc77701eec9a9/%7B92219BCF-B384-4523-81B9-1B4260779E08%7D.png)

When you set the switching time, please note:

- Generally, the error of switching time is about 15 minutes; (because there may be a large amount of writing requests for large transactions during switching, which will affect the progress of data synchronization, so the system will preferably ensure the synchronization between the old and new instances)
- The maximum length of switching time to be configured is 72 hours, please ensure proper planning;
- Be sure to select the time at the lows of business, so that the stable operation of business will not be affected;
- Please ensure that there is a database reconnection mechanism for business;

## This feature can help you

- **Accurately control the upgrade time and speed, to reduce the time when the business may be interrupted**
- **Make an upgrade plan in advance, to reduce uncontrollable upgrade risks**
- **Provide unattended database maintenance solution, to avoid staying up late for upgrade**


