## 简介

MongoDB 数据备份是腾讯云对象存储（Cloud Object Storage，COS）基于 [云函数（Serverless Cloud Function，SCF）](https://cloud.tencent.com/document/product/583) 为用户提供的数据库备份功能，可以协助用户将 MongoDB 云数据库上的备份文件转存至对象存储进行持久化的保存，以防止数据丢失或损坏。当用户在指定存储桶配置了备份函数规则后，云函数会定期扫描您的 MongoDB 备份文件并将文件转存至存储桶中。

## 注意事项

- MongoDB 数据备份函数备份的是腾讯云 MongoDB 数据库的备份文件，若您此前并未开启 MongoDB 数据库备份，则无法执行备份函数。有关腾讯云 MongoDB 数据库备份的更多信息，可查看 [备份云数据库 MongoDB](https://cloud.tencent.com/document/product/240/7108)。
- 若您此前在对象存储控制台上为存储桶添加了 MongoDB 数据备份规则，可以在 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=1&ns=default) 上看到您所创建的 MongoDB 数据备份函数，请**不要**删除该函数，否则可能导致您的规则不生效。
- 已上线云函数的地域均已支持 MongoDB 数据备份，包括有广州、上海、北京、成都、香港、新加坡、孟买、多伦多、硅谷等，更多支持地域可查看 [云函数产品文档](https://cloud.tencent.com/document/product/583)。

## 操作步骤

1. 登录 [对象存储控制台](https://console.cloud.tencent.com/cos5)。
2. 在左侧导航中，单击【应用集成】，找到【MongoDB 数据备份】。
3. 单击【配置备份规则】，进入规则配置页面。
4. 单击【添加函数】。
>!
> 如果您尚未开通云函数服务，请前往 [云函数控制台](https://console.cloud.tencent.com/scf) 开通云函数服务，按照提示完成服务授权即可。
5. 在弹出的窗口中，配置如下信息：
![](https://main.qcloudimg.com/raw/e6eaa0130a141a2d313e014ef0bd51d7.png)
 - **函数名称**：作为函数的唯一标识名称，创建后不可修改。您可以在 [云函数控制台](https://console.cloud.tencent.com/scf/list?rid=1&ns=default) 上查看该函数。
 - **关联存储桶**：存储 MongoDB 备份文件的存储桶。
 - **触发器周期**：MongoDB 数据备份函数通过定时触发器来触发备份转存操作，触发周期支持每天、每周及自定义周期。
 - **Cron 表达式**：当触发器周期设置为自定义时，可通过 Cron 指定具体的触发周期规则。Cron 当前以 UTC +8 中国标准时间（China Standard Time）运行，即北京时间。详细配置策略请参见 [Cron 相关文档](https://cloud.tencent.com/document/product/583/9708#cron-.E8.A1.A8.E8.BE.BE.E5.BC.8F)。
 - **数据库实例**：当前存储桶所在地域的 MongoDB 数据库实例列表。
 - **投递路径**：备份文件的投递路径前缀，不填写则默认保存在存储桶根路径。
 - **SCF 授权**：MongoDB 数据备份需要授权云函数从您的 MongoDB 备份中读取数据库实例及其备份文件，并将备份文件转存至您指定的存储桶中。因此需要添加此授权。
6. 添加配置后，单击【确认】，即可看到函数已添加完成。
![](https://main.qcloudimg.com/raw/a5b709e3d94050234745763e3a123b1e.png)
您可以对新创建的函数进行如下操作：
 - 单击【查看日志】，查看 MongoDB 数据备份的历史运行情况。当备份出现报错时，您还可以通过单击【查看日志】，快速跳转到云函数控制台查看日志错误详情。
 - 单击【编辑】，修改 MongoDB 数据备份规则。
 - 单击【删除】，删除不使用的 MongoDB 数据备份规则。

