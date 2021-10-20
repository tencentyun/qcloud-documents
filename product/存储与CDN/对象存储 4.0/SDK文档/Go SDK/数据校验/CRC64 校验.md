## 简介

数据在客户端和服务器间传输时可能会出现错误，COS 除了可以通过 [MD5 和自定义属性](https://cloud.tencent.com/document/product/436/36427) 验证数据完整性外，还可以通过 CRC64 检验码来进行数据校验。

COS 会对新上传的对象进行 CRC64 计算，并将结果作为对象的属性进行存储，随后在返回的响应头部中携带 x-cos-hash-crc64ecma，该头部表示上传对象的 CRC64 值，根据 [ECMA-182标准](https://www.ecma-international.org/publications/standards/Ecma-182.htm) 计算得到。对于 CRC64 特性上线前就已经存在于 COS 的对象，COS 不会对其计算 CRC64 值，所以获取此类对象时不会返回其 CRC64 值。

## 操作说明

目前支持 CRC64 的 API 如下：

- 简单上传接口
	- [PUT Object](https://cloud.tencent.com/document/product/436/7749) 和 [POST Object](https://cloud.tencent.com/document/product/436/14690) ：用户可在返回的响应头中获得文件 CRC64 校验值。
- 分块上传接口
	- [Upload Part](https://cloud.tencent.com/document/product/436/7750)：用户可以根据 COS 返回的 CRC64 值与本地计算的数值进行比较验证。
	- [Complete Multipart Upload](https://cloud.tencent.com/document/product/436/7742)：如果每个分块都有 CRC64 属性，则会返回整个对象的 CRC64 值，如果某些分块不具备 CRC64 值，则不返回。
- 执行 [Upload Part - Copy](https://cloud.tencent.com/document/product/436/8287) 时，会返回对应的 CRC64 值。
- 执行 [PUT Object - Copy](https://cloud.tencent.com/document/product/436/10881) 时，如果源对象存在 CRC64 值，则返回 CRC64，否则不返回。
- 执行 [HEAD Object](https://cloud.tencent.com/document/product/436/7745) 和 [GET Object](https://cloud.tencent.com/document/product/436/7753) 时，如果对象存在 CRC64，则返回。用户可以根据 COS 返回的 CRC64 值和本地计算的 CRC64 进行比较验证。

## SDK 说明

SDK对应接口可通过响应头部获取 CRC64 值，SDK 上传文件时默认会进行 CRC64 校验。

>!  COS Go SDK 版本需要大于等于 v0.7.23。

#### 请求示例
```go
// 将 examplebucket-1250000000 和 COS_REGION 修改为真实的信息
u, _ := url.Parse("https://examplebucket-1250000000.cos.COS_REGION.myqcloud.com")
b := &cos.BaseURL{BucketURL: u}
client := cos.NewClient(b, &http.Client{
    Transport: &cos.AuthorizationTransport{
        SecretID:     "SECRETID",  // 替换为用户的 SecretId，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
        SecretKey:    "SECRETKEY", // 替换为用户的 SecretKey，请登录访问管理控制台进行查看和管理，https://console.cloud.tencent.com/cam/capi
    },
})
// 关闭 CRC64 校验, CRC64 默认开启，强烈不建议用户关闭
// client.Conf.EnableCRC = false

name := "exampleobject"
// 通过字符串上传对象
f := strings.NewReader("test")
// SDK 会自动进行 CRC64 校验。
resp, err := c.Object.Put(context.Background(), name, f, nil)
if err != nil {
	// ERROR
}
// 根据响应头部获取 CRC64
fmt.Printf("CRC64: %v\n", resp.Header.Get("x-cos-hash-crc64ecma"))
```

#### 返回结果说明

| 参数名称        | 参数描述     | 类型   |
| --------------- | ------------ | ------ |
| Response        | HTTP 响应     | Struct |
| Response.Header | HTTP 响应头部 | Struct |
| Response.Body   | HTTP 响应数据 | Struct |

