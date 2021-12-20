该属性是一个 object，记录了 SDK 全部错误码，具体的 key 和 value 与错误码文档相对应。详情请参见 [错误码](https://cloud.tencent.com/document/product/1038/33317)。该对象结构示例如下：
```
ErrCode = {
	//返回成功
	EC_OK: 0,
	//请求包格式错误
	EC_REQ_BAD_PKG: 1,
	// 其他错误码
	// ...
}
```


