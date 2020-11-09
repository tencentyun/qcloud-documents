## 简介
Go SDK 提供获取请求预签名 URL 接口，详细操作请查看本文示例。



## 获取请求预签名 URL 

```go
func (s *ObjectService) GetPresignedURL(ctx context.Context, httpMethod, name, ak, sk string, expired time.Duration, opt interface{}) (*url.URL, error)
```

#### 参数说明
| 参数名称           | 类型                         | 描述                            |
| ------------------ | ---------------------------- | ------------------------------- |
| httpMethod            | string                   | HTTP 请求方法                        |
| name | string           | HTTP 请求路径，即对象键                 |
| ak             | string                       | SecretId                    |
| sk               | string                       | SecretKey         |
| expired            | time.Duration | 签名有效时长             |
| opt    | interface{} | 扩展项，可填 nil |

## 永久密钥预签名请求示例

#### 上传请求示例

[//]: # (.cssg-snippet-get-presign-upload-url)
```go
ak := "COS_SECRETID"
sk := "COS_SECRETKEY"

name := "exampleobject"
ctx := context.Background()
f := strings.NewReader("test")

// 1. 通过普通方式上传对象
_, err := client.Object.Put(ctx, name, f, nil)
if err != nil {
    panic(err)
}
// 获取预签名URL
presignedURL, err := client.Object.GetPresignedURL(ctx, http.MethodPut, name, ak, sk, time.Hour, nil)
if err != nil {
    panic(err)
}
// 2. 通过预签名方式上传对象
data := "test upload with presignedURL"
f = strings.NewReader(data)
req, err := http.NewRequest(http.MethodPut, presignedURL.String(), f)
if err != nil {
    panic(err)
}
// 用户可自行设置请求头部
req.Header.Set("Content-Type", "text/html")
_, err = http.DefaultClient.Do(req)
if err != nil {
    panic(err)
}
```

#### 下载请求示例

[//]: # (.cssg-snippet-get-presign-download-url)
```go
ak := "COS_SECRETID"
sk := "COS_SECRETKEY"
name := "exampleobject"
ctx := context.Background()
// 1. 通过普通方式下载对象
resp, err := client.Object.Get(ctx, name, nil)
if err != nil {
    panic(err)
}
bs, _ := ioutil.ReadAll(resp.Body)
resp.Body.Close()
// 获取预签名URL
presignedURL, err := client.Object.GetPresignedURL(ctx, http.MethodGet, name, ak, sk, time.Hour, nil)
if err != nil {
    panic(err)
}
// 2. 通过预签名URL下载对象
resp2, err := http.Get(presignedURL.String())
if err != nil {
    panic(err)
}
bs2, _ := ioutil.ReadAll(resp2.Body)
resp2.Body.Close()
if bytes.Compare(bs2, bs) != 0 {
    panic(errors.New("content is not consistent"))
}
```

