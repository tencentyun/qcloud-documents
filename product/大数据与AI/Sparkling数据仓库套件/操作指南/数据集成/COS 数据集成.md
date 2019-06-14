## 操作场景
云数据仓库套件 Sparkling 支持多样化的数据接入方式和数据源管理。数据接入方式包括：
- 关系型数据库（RDBMS）接入：可以通过 RDBMS 数据接入方式将云数据库 MySQL 、分布式数据库 TDSQL 中的数据接入到 Sparkling 中。
- 腾讯云对象存储（COS）数据接入：可以通过生成账户密钥，建立存储桶（bucket）的方式进行 COS 数据接入。
- 腾讯云消息队列（CKafka）数据接入：可以通过 Kafka 数据接入方式将腾讯云 CKafka 中的数据接入 Sparkling 中。

本节将为您介绍 COS 数据接入方法。更多关于 COS 的信息请参见 [COS 产品介绍](https://cloud.tencent.com/document/product/436)。

## 操作步骤
登录 [Sparkling 控制台](https://sparkling.cloud.tencent.com)，在左侧导航单击【数据】进入数据接入页面，按以下操作步骤完成 COS 数据接入：
![](https://main.qcloudimg.com/raw/4486aaefec174caad540075c7834e0c7.png)

### 1. 数据源配置
- 数据类型：选择【COS】数据类型。
- 地域：选择 COS 存储桶所在地域。
- 授权方式：选择用户密钥授权。
- SecretID/SecretKey：填写您已生成的密钥，可在 [API密钥管理](https://console.cloud.tencent.com/cam/capi) 中生成并查看。
- 存储桶：填写您在 COS 中已生成的存储桶名称和您的 APPID，单击【浏览存储桶】查看当前存储桶下的数据并选择要导入的数据文件。数据文件导入方式支持【文件夹导入】和【文件导入】两种方式。
>?存储桶名称需要按<目标存储桶名称-APPID>格式填写，例如：sparkling-12334513，桶名和 APPID 可在账户信息中查看。

 - **文件夹导入方式**：单击所选文件夹，左下角显示所选文件夹所包含文件个数及大小，确认信息无误后单击【确认】。![](https://main.qcloudimg.com/raw/0f0dfbfbc88d0da774a57eb5449a7e15.png)

 - **文件导入方式** ：单击所选文件，左下角显示所选文件名称及大小，确认信息无误后单击【确认】。
![](https://main.qcloudimg.com/raw/e564c24bc3f03e88fcd2cdef613606c2.png)

- 文件格式：支持 CSV、TSV、PARQUET、ORC、AVRO、JSON及其他自定义分隔符日志的文件。
>?  COS 导入 JSON 文件时要求将 JSON 文件的每条记录必须用换行符分割。

- 字段分隔符：选择是否将第一行作为表头字段名。
 
###  2. 数据预览
确认信息无误后，单击【下一步】进行数据预览，本页默认显示前五行数据。![](https://main.qcloudimg.com/raw/0b3d79583b30d2646200c31f051090c9.png)

### 3. 目标配置
确认目标配置，输入标题（新建表表名）及描述，选择存储格式后单击【下一步】进入任务预览页面。![](https://main.qcloudimg.com/raw/7bafa130bcd1fdd12f4fa1845527d85b.png)

### 4.  预览
任务预览无误后单击【完成】即可。![](https://main.qcloudimg.com/raw/2492b3c4939d4eb3f0daebf0a9935be7.png)
