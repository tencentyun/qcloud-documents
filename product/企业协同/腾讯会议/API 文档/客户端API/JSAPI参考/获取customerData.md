## 接口描述
- **描述：**获取用户通过专属链接入会时携带的 CustomerData。
- **支持的版本：**3.2.0
- **是否需要鉴权：**需要绑定应用 API 调用者将 `enable_customer_data` 字段设为1（请参见 [客户端 API 绑定扩展应用部](https://cloud.tencent.com/document/product/1095/84398)）

## 参数说明
返回 Promise MeetingCustomerData。

## 代码示例
```plaintext
wemeet.meeting.getCustomerData()
	.then(resp => {
		const { customerData } = resp;
		console.log(customerData); // 入会携带的自定义参数
	})
```



