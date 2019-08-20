## 简介
Go SDK 提供获取请求预签名 URL 接口，详细操作请查看本文示例。



## 获取请求预签名 URL 

```go
func (s *ObjectService) GetPresignedURL(ctx context.Context, httpMethod, name, ak, sk string, expired time.Duration, opt interface{}) (*url.URL, error)
```

### 参数说明
| 参数名称           | 类型                         | 描述                            |
| ------------------ | ---------------------------- | ------------------------------- |
| httpMethod            | string                   | HTTP 请求方法                        |
| name | string           | HTTP 请求路径，即对象键                 |
| ak             | string                       | SecretId                    |
| sk               | string                       | SecretKey         |
| expired            | time.Duration | 签名有效时长             |
| opt    | interface{} | 扩展项，可填 nil |

## 永久密钥预签名请求示例

### 上传请求示例

```go
ak := "COS_SECRETID"
sk := "COS_SECRETKEY"
u, _ := url.Parse("http://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com")
b := &cos.BaseURL{BucketURL: u}
c := cos.NewClient(b, &http.Client{
   Transport: &cos.AuthorizationTransport{
      SecretID:  ak,
      SecretKey: sk,
   },
})

name := "test/objectPut.go"
ctx := context.Background()
// NewReader create file content
f := strings.NewReader("test")

// 1.Normal add auth header way to put object
_, err := c.Object.Put(ctx, name, f, nil)
if err != nil {
	panic(err)
}
// Get presigned
presignedURL, err := c.Object.GetPresignedURL(ctx, http.MethodPut, name, ak, sk, time.Hour, nil)
if err != nil {
	panic(err)
}
// 2.Put object content by presinged url
data := "test upload with presignedURL"
f = strings.NewReader(data)
req, err := http.NewRequest(http.MethodPut, presignedURL.String(), f)
if err != nil {
	panic(err)
}
// Can set request header.
req.Header.Set("Content-Type", "text/html")
_, err = http.DefaultClient.Do(req)
if err != nil {
	panic(err)
}
```

### 下载请求示例

```go
ak := "COS_SECRETID"
sk := "COS_SECRETKEY"
u, _ := url.Parse("http://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com")
b := &cos.BaseURL{BucketURL: u}
c := cos.NewClient(b, &http.Client{
   Transport: &cos.AuthorizationTransport{
      SecretID:  ak,
      SecretKey: sk,
   },
})

name := "test"
ctx := context.Background()
// 1.Normal add auth header way to get object
resp, err := c.Object.Get(ctx, name, nil)
if err != nil {
	panic(err)
} 
bs, _ := ioutil.ReadAll(resp.Body)
resp.Body.Close()
// Get presigned
presignedURL, err := c.Object.GetPresignedURL(ctx, http.MethodGet, name, ak, sk, time.Hour, nil)
if err != nil {
	panic(err)
} 
// 2.Get object content by presinged url
resp2, err := http.Get(presignedURL.String())
if err != nil {
	panic(err)
}                    
bs2, _ := ioutil.ReadAll(resp2.Body)
resp2.Body.Close()
fmt.Printf("result2 is : %s\n", string(bs2))
fmt.Printf("%v\n\n", bytes.Compare(bs2, bs) == 0)
```
