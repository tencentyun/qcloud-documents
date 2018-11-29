### 上传文件时，出现“error code:-97, error message:ERROR_PROXY_AUTH_FAILED”等错误怎么办？

自定义域名不支持上传，只支持下载。建议避免使用自定义域名上传。

### 上传文件至存储桶，已存在同名文件，是直接覆盖还是新增不同版本的文件？

目前暂不支持版本控制功能，上传相同名称的文件至存储桶，会直接覆盖已存在的同名文件。

### COS 分块上传方式，最小分块大小是多少呢？

每块最小1MB。详情请查阅 [规格与限制](https://cloud.tencent.com/document/product/436/14518) 文档。

### 大文件分片上传过程中，签名失效后是否可以换签名继续上传分片？

可以。

### 进行上传下载等操作时，报错“403 Forbidden”、权限拒绝等该如何处理？

请按照以下步骤逐步排查问题：

1. 请检查您的以下配置信息是否正确：
   BucketName、APPID、Region、SecretId、SecretKey 等。
2. 确保上述信息正确的前提下，请检查是否使用子账号操作，若使用子账号请检查主账号是否已对子账号授权。否则，请先登录主账号对子账号授权。授权操作参考文档：[访问管理权限设置相关案例](https://cloud.tencent.com/document/product/436/12514)。
3. 若使用临时密钥进行操作，请检查当前操作是否在获取临时密钥时设置的 Policy 中。否则请修改相关 Policy 设置。
4. 若以上步骤仍无法解决问题，请 [提交工单](https://console.cloud.tencent.com/workorder/category?level1_id=83&level2_id=84&source=0&data_title=%E5%AF%B9%E8%B1%A1%E5%AD%98%E5%82%A8%20COS&step=1) 联系我们。