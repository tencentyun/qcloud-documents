The maintenance duration can be set for each instance. Changes to database instances are usually involved in maintenance (such as instance specification upgrades, database version upgrades, etc.). It is recommended to set the maintenance duration of the database in the off peak hours of transactions.
Let's take the database instance specification upgrade as an example. Because the instance specification upgrading involves data migration, after upgrading is completed, flash disconnection within seconds may occur to MySQL database. When upgrading is initiated, the **switching time** can be selected as ''Within maintenance duration", so that the instance specification switching will be enabled within the next **Maintenance duration** after the instance upgrading is completed. It should be noted that when the switching time is selected as the [Within maintenance duration], the switching action will not occur immediately after the database specification upgrading is completed. It will keep synchronized till the instance goes **within maintenance duration** After that, the switching action will be enabled. In this way, the whole instance upgrading time may be extended.

### Set an instance maintenance duration
1. log in to [Cloud Database Console](https://console.cloud.tencent.com/cdb/ ) and find the instance to be modified in the instance list. Click "Management" in the Operation column
![](https://mc.qcloudimg.com/static/img/067a823712584842fc983ab34fa79b55/step1.png)
2. Click [Instance Details]>[Maintenance Duration]> [Modify] on the Instance Details page.
![Maintenance Duration][image-2]
3. After selecting the maintenance time, click [OK] to complete the instance maintenance time settings.
![Modify Maintenance Duration][image-3]


[image-2]:  //mc.qcloudimg.com/static/img/da7f29b04e72c26bac1ddaeaf1d90eed/1.png
[image-3]:  //mc.qcloudimg.com/static/img/bbdebbe19bd1ef5e85d997d5de6a2e06/2.png

