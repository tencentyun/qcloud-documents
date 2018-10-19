# Data Subscription Description
## 1. Feature Description
TencentDB Service for Transmission (DTS) provides a binlog-based incremental data subscription feature that allows subscription of incremental update data from TencentDB with several simple steps:
* Purchase and create subscription channel for TencentDB instance from the Tencent Cloud DTS console.
* Use DTS data subscription SDK to connect to this subscription channel to subscribe to and consume incremental data.

## 2. Service Limit
**For now, data subscription feature is unavailable in some regions, and is only supported for Cloud Database MySQL (TencentDB for MySQL).**

Supported regions:

| Region | Supported |
|:--:|:--:|
| Guangzhou | Yes |
| Shanghai | Yes |
| Beijing | Yes |
| Hong Kong | - |
| Open Zone | - |
| Singapore | - |
| Toronto | - |
| Silicon Valley | - |
| Shenzhen Finance | - |
| Shanghai Finance | - |

## 3. Create Data Subscription Channel
Log in to DTS console and go to the Data Subscription page.

* Click "New Data Subscription" in the upper right corner to start configuring a subscription channel.
![][img-1]
* Select the region where the source TencentDB instance is located
![][img-2]
* Once the channel is enabled, go to the console and complete initial configuration for the data subscription channel you just purchased.
![][img-3]
* Select the source TencentDB instance
![][img-4]
* Select your desired synchronization type and database table.
![][img-5]
	The granularity of subscription objects for DTS data subscription includes two levels: database and table. That is, a user may choose to subscribe to certain databases or tables.
	If you only choose subscription object and data update, you will only receive changes regarding three types of data: insert/delete/update. To subscribe to structure update (DDL), you need to select structure change in subscription data type. If you subscribe to structure update, the DTS will pull all structural changes of the entire RDS instance, in which case you need to filter the data using SDK.
* The subscription channel can be enabled when subscription object is selected.

## 4. Change Consumption Time Point
  
When using DTS, you can change consumption time point at any time during consumption process. Once the consumption time point is changed, downstream incremental data pulled by the SDK will start from the new consumption time point. The new consumption time point must fall within the data range of the subscription channel. For now, you can only change consumption time point in the DTS console. You cannot specify consumption time point in the SDK.
Change consumption time point by following the steps below:
* Stop SDK consumption process.
![][img-6]

* Change consumption time point
To change the consumption time point of a channel, move your cursor to the consumption time point to see "Configure" option, and click on it to enter the configuration page.
![][img-7]
![][img-8]


* Restart SDK consumption process.
You can restart the local SDK consumption process after the consumption time point is changed. At this point, the SDK will start subscribing to incremental data from the new consumption time point.

## 5. Change Subscription Object
When using DTS, you can dynamically add/reduce subscription objects during consumption. When you save change after a subscription object is added, the subscription channel will pull incremental data of the added subscription object, from the current time. When you save change after a subscription object is deleted, the SDK will no longer subscribe to data of this object.
Change subscription object by following the steps below:

* Entry for changing subscription object
![][img-9]

* Change subscription object
![][img-10]


## 6. Use SDK to Consume Data
Refer to [SDK User Guide](/document/product/571/8776)





[img-1]://mc.qcloudimg.com/static/img/03c52107eccbcc933e11cce9e07502df/1.png
[img-2]://mc.qcloudimg.com/static/img/5765b22b7cfd67768c8568a6cdb504f2/2.png
[img-3]://mc.qcloudimg.com/static/img/927fb3ec5f9c2026338a2cb85efd8744/3.png
[img-4]://mc.qcloudimg.com/static/img/f245a6cbcaeba3a19f5863203371cf0d/4.png
[img-5]://mc.qcloudimg.com/static/img/72c3a022ddb73535a49f4dfa53061c50/5.png
[img-6]://mc.qcloudimg.com/static/img/092b59bdade021f1c3d1ce0740161d62/6.png
[img-7]://mc.qcloudimg.com/static/img/f17f7720f13a33ed26b525dcd683046c/7.png
[img-8]://mc.qcloudimg.com/static/img/c86c4736a65766917a675b3def08883e/8.png
[img-9]://mc.qcloudimg.com/static/img/1ba4f66502db932c7066e8cbcc0da877/9.png
[img-10]://mc.qcloudimg.com/static/img/1602a9e4bf8a2e4668146d69e27dd940/10.png
[img-11]://mc.qcloudimg.com/static/img/1eb73f016d3bb7d0820ddf33a15e1569/11.png
[img-12]://mc.qcloudimg.com/static/img/c88d2d0ca2ec0b7cd29fade9262352ae/12.png
[img-13]://mc.qcloudimg.com/static/img/664293491411378f95bc238e620103d2/13.png
[img-14]://mc.qcloudimg.com/static/img/e7dc19b7a6918a8c1ef8e7a4b620d4d0/14.png

