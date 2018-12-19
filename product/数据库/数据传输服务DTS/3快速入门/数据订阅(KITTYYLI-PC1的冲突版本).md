# 数据订阅说明
## 1. 功能说明
数据传输服务DTS提供了基于binlog的增量数据订阅功能，仅需几步简单操作，即可订阅云数据库TencentDB的增量更新数据：
* 在腾讯云DTS控制台购买并创建TencentDB实例的订阅通道。
* 使用DTS数据订阅SDK连接这个订阅通道，订阅并消费增量数据。

## 2. 使用限制
**目前数据订阅功能尚在部分地域灰度中，仅支持云数据库MySQL(TencentDB for MySQL)。**

支持地域：

|地域|是否支持数据订阅|
|:--:|:--:|
|广州|支持|
|上海|支持|
|北京|支持|
|香港|—|
|Open专区|—|
|新加坡|—|
|多伦多|—|
|硅谷|—|
|深圳金融|—|
|上海金融|—|

## 3. 创建数据订阅通道
登录数据传输服务控制台，进入数据订阅页面。

* 点击控制台右上角“新建数据订阅” 开始订阅通道配置。
![][img-1]
* 选择源TencentDB实例所在地域
![][img-2]
* 开通成功后，进入控制台，为刚才购买的额数据订阅通道初始化配置。
![][img-3]
* 选择源TencentDB实例
![][img-4]
* 选择所需的同步类型及库表。
![][img-5]
	DTS数据订阅的订阅对象粒度细分为库、表。即用户可以选择订阅某些库或者是订阅某几张表。
	DTS将订阅数据类型细分为数据更新、结构更新。如果只选择订阅对象及数据更新的话，那么只能订阅到insert/delete/update三种数据变更内容，如果需要订阅结构更新（DDL），那么需要选择订阅数据类型中的结构变更。一旦订阅了结构更新，那么DTS会将整个TencentDB实例的所有结构变更拉取出来，用户需要使用SDK过滤需要的数据。
* 当选择完订阅对象后，即可启动订阅通道。

## 4. 修改消费时间点
  
DTS支持在消费的过程中，随时修改消费时间点。一旦修改完消费时间点，那么下游SDK拉取到的增量数据从修改后的消费时间点开始。修改的消费时间点必须在订阅通道的数据范围之内。DTS目前只支持在控制台修改消费点，不支持在SDK中指定消费位点。
修改消费时间点操作步骤如下：
* 停止SDK消费进程。
![][img-6]

* 修改消费时间点
当需要修改通道消费时间点时，将鼠标挪到这个通道的消费时间点上，会出现“配置”字样，点击此进入修改页面。
![][img-7]
![][img-8]


* 重启SDK消费进程。
当修改完消费位点后，即可重启本地的SDK消费进程，此时SDK会从修改的消费位点开始订阅增量数据。

## 5. 修改订阅对象
DTS支持在订阅消费的过程中，动态增加/减少订阅对象。如果增加了订阅对象，那么修改完成后，订阅通道会从当前时间拉取新增订阅对象的增量数据。如果减少订阅对象，那么修改完成后，SDK中将无法再订阅到这个对象的数据。
修改订阅对象操作步骤如下：

* 修改订阅对象入口
![][img-9]

* 修改订阅对象
![][img-10]


## 6. 使用SDK消费数据
请查看[SDK使用指南](/document/product/571/8776)





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
