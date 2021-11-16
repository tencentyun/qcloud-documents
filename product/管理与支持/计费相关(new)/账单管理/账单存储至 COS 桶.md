## 简介

腾讯云提供定期将账单数据以文件形式存储至您指定的对象存储（Cloud Object Storage，COS）存储桶的功能。对于账单明细数据量级很大（例如每月账单明细量级超过20w）的客户，通过 API 调用账单数据效率较低，建议您开通账单数据存储功能，通过存储桶中获取账单文件进行分析。

>? 该功能可能产生费用，详情请参见 [COS 计费计费概述](https://cloud.tencent.com/document/product/436/16871)。
>


## 开启账单存储至 COS 功能

1. 在 [账单概览](https://console.cloud.tencent.com/expense/bill/overview) 页面，将**账单数据存储**设置为 ![](https://main.qcloudimg.com/raw/48d005ca49e683a3370212a71599ddd4.png)。
![](https://main.qcloudimg.com/raw/867d2593c09f06dc3fd80b525d0c1f5e.png)
2. 同意服务角色授权。
在弹出的窗口中，单击**进入授权**，并在授权页面，同意授权。
<img src="https://main.qcloudimg.com/raw/30d935403805ae73cdb1763300666cef.png" style="width: 70%"/></br>
3. 设置存储信息。
根据实际需求，选择需要存储到 COS 桶的文件类型，将其存到特定的 COS 桶。如果您存在集团成员账号，也可以选择成员账号的账单文件，将其存至您的 COS 桶中。
<img src="https://main.qcloudimg.com/raw/f1f27951392a135d9304cf9186d54066.png" style="width: 70%"/></br>
账单文件类型
 - 日明细账单：用户开通后，Day+1上午3点（每月1日出账日为20点），新增的账单明细会存储到 COS 存储 Bucket 中。
 例如：4月6日，将会增加一个4月1日 - 4月5日的汇总账单；4月8日，将会增加一个4月1日 - 4月7日的汇总账单。
 - 月明细账单：每个月2号更新一份完整的上月份账单明细，如数据量过大，则拆分成多个 CVS 文件。


## 其他操作

- **关闭账单存储功能或更换存储桶**：如用户需要关闭账单功能，可参考如下操作进行关闭。
 1. 将**账单数据存储**设置为 ![](https://main.qcloudimg.com/raw/ab69e4e4f7e979b04d67ea3d55b2a718.png)。
 2. 在弹出的窗口中，单击**关闭存储桶**。
 3. 在弹出的提示窗口中，单击**确认关闭**，即可关闭该功能。关闭后，该桶保留旧数据，不再写入新数据。
- **更换存储桶**：如用户需要更换存储桶，可选择需要更换的存储桶，单击**保存**即可。历史数据保留在旧桶，新数据将在 Day+1之后写入新桶。


## 相关链接
- 添加成员账号：可参考集团账号功能 [添加组织成员](https://cloud.tencent.com/document/product/850/58721)，系统默认勾选**查看账单**权限，即可在账单存 COS 配置界面选择到子账号。
- COS API 获取账单压缩包名称：[GET Bucket（List Objects）](https://cloud.tencent.com/document/product/436/7734)。
- COS API 下载压缩包：[GET Object](https://cloud.tencent.com/document/product/436/7753)。
