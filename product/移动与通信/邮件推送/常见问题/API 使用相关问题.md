### ReplyToAddresses 这个参数是什么意思？
当邮件成功发送到用户邮箱，且用户点击“回复”按钮之后，该回复内容将回复到的真实邮箱当中（该邮箱能正常接收邮件）。

### 发送邮件报错：FailedOperation.ExceedSendLimit 超出当日总量发送限制。限制是多少？是否可以扩展？
每个账号最大日发送总量限制默认为30万，可以扩展。如需扩展，请联系 [腾讯云技术支持](https://console.cloud.tencent.com/workorder/category)。

### SendEmail接口中，Template.TemplateData 字段应该如何填写？
“`{}`”表示不传变量，详情请参考 API 文档检查 [TemplateData](https://cloud.tencent.com/document/api/1288/51053#Template) 字段格式。
