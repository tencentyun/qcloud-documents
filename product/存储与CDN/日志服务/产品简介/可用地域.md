## 概述

用户在使用日志服务过程中可选择在不同地域创建日志集与日志主题。地域是指物理的数据中心的地理区域，不同地域之间网络完全隔离。用户可以根据自己的业务场景以及目标用户所在的地理位置，选择就近的地域存储，以降低日志数据的访问时延、提高访问速度。 


#### 深圳/上海金融专区特别说明

针对金融行业监管要求定制的合规专区，具有高安全，高隔离性的特点。目前日志服务已支持深圳、上海金融专区。已认证通过的金融行业客户可提工单申请使用专区，详情请参见 [金融专区介绍](https://cloud.tencent.com/document/product/304/2766)。


## 可用地域及简称

| 地域     | 地域简称        | 请求域名                         |
| -------- | --------------- | -------------------------------- |
| 北京     | ap-beijing      | ap-beijing.cls.myqcloud.com      |
| 上海     | ap-shanghai     | ap-shanghai.cls.myqcloud.com     |
| 广州     | ap-guangzhou    | ap-guangzhou.cls.myqcloud.com    |
| 成都     | ap-chengdu      | ap-chengdu.cls.myqcloud.com      |
| 深圳金融 | ap-shenzhen-fsi | ap-shenzhen-fsi.cls.myqcloud.com |
| 上海金融 | ap-shanghai-fsi | ap-shanghai-fsi.cls.myqcloud.com |
| 多伦多   | na-toronto      | na-toronto.cls.myqcloud.com      |



## 注意事项

如果日志服务中接入了其他云产品，请您尽量选择与其他云产品相同地域的日志集。相同地域的云产品之间通过内网读写数据，能有效降低延迟和提高访问速度。
