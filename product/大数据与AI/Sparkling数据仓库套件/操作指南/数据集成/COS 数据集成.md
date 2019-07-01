本节将为您介绍 COS 数据接入方法。更多关于 COS 的信息请参见 [COS 产品介绍](https://cloud.tencent.com/document/product/436)。

## 操作步骤
登录 [Sparkling 控制台](https://sparkling.cloud.tencent.com)，在左侧导航单击【数据】进入数据接入页面，按以下操作步骤完成 COS 数据接入：
![](https://main.qcloudimg.com/raw/4486aaefec174caad540075c7834e0c7.png)

### 1. 数据源配置
- **文件夹导入方式**
a. 数据类型：选择【COS】数据类型
b. 地域：选择 COS 存储桶所在地域。
c. 授权方式：选择用户密钥授权。
d. SecretID/SecretKey：填写您已生成的密钥，可在 [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 中生成并查看。
e. 存储桶：填写您在 COS 中已生成的存储桶名称和您的 APPID，单击【浏览存储桶】查看当前存储桶下的数据并选择要导入的数据文件。数据文件导入方式支持【文件夹导入】和【文件导入】两种方式。
>?存储桶名称需要按<目标存储桶名称-APPID>格式填写，例如：sparkling-12334513，桶名和 APPID 可在账户信息中查看。

 f.单击所选文件夹，左下角显示所选文件夹所包含文件个数及大小，确认信息无误后单击【确认】。![](https://main.qcloudimg.com/raw/0f0dfbfbc88d0da774a57eb5449a7e15.png)
g. 文件格式：支持 CSV、TSV、PARQUET、ORC、AVRO、JSON 及其他自定义分隔符日志的文件。
>?  COS 导入 JSON 文件时要求将 JSON 文件的每条记录必须用换行符分割。

 h. 字段分隔符：选择是否将第一行作为表头字段名。
- **文件导入方式**
a. 前面的操作同“文件夹导入方式”的步骤 a - e。
b. 单击所选文件，左下角显示所选文件名称及大小，确认信息无误后单击【确认】。![](https://main.qcloudimg.com/raw/e564c24bc3f03e88fcd2cdef613606c2.png)
c. 后面的操作同“文件夹导入方式”的步骤 g、h。
 
###  2. 数据预览
确认信息无误后，单击【下一步】进行数据预览，本页默认显示前五行数据。![](https://main.qcloudimg.com/raw/0b3d79583b30d2646200c31f051090c9.png)

### 3. 目标配置
确认目标配置，输入标题（新建表表名）及描述，选择存储格式后单击【下一步】进入任务预览页面。![](https://main.qcloudimg.com/raw/7bafa130bcd1fdd12f4fa1845527d85b.png)

### 4.  预览
任务预览无误后单击【完成】即可。
<img src="https://main.qcloudimg.com/raw/c7ae4a9d04b4590012c37d718fd2e3cc.png" style="zoom:70%">
