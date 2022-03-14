
## 简介

本文档提供关于 Guetzli 压缩的相关的 API 概览以及 SDK 示例代码。

| API           |  操作描述               |
| :--------------- | :------------------ |
| [开通 Guetzli 压缩](https://cloud.tencent.com/document/product/460/30112) | 对 Bucket 开通 Guetzli 压缩功能   |
| [查询 Guetzli 状态](https://cloud.tencent.com/document/product/460/30111) |用于查询 Guetzli 压缩功能是否开启 |
|[关闭 Guetzli 压缩](https://cloud.tencent.com/document/product/460/30113)  |   用于关闭 Guetzli 压缩功能   |


## 开通 Guetzli 压缩

#### 功能说明

对 Bucket 开通 Guetzli 压缩功能。

#### 方法原型

```go
func (s *CIService) PutGuetzli(ctx context.Context) (*Response, error)
```

#### 请求示例

```go
// 需要填写CIURL
u, _ := url.Parse("https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com")
cu, _ := url.Parse("http://examplebucket-1250000000.pic.ap-guangzhou.myqcloud.com")
b := &cos.BaseURL{BucketURL: u, CIURL: cu}
c := cos.NewClient(b, &http.Client{
	Transport: &cos.AuthorizationTransport{
		SecretID:  os.Getenv("SECRETID"),
		SecretKey: os.Getenv("SECRETKEY"),
	},
})

_, err := c.CI.PutGuetzli(context.Background())
log_status(err)
```

## 查询 Guetzli 状态

#### 功能说明

用于查询 Guetzli 压缩功能是否开启。

#### 方法原型

```go
func (s *CIService) GetGuetzli(ctx context.Context) (*GetGuetzliResult, *Response, error)
```

#### 请求示例

```go
// 需要填写 CIURL
u, _ := url.Parse("https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com")
cu, _ := url.Parse("http://examplebucket-1250000000.pic.ap-guangzhou.myqcloud.com")
b := &cos.BaseURL{BucketURL: u, CIURL: cu}
c := cos.NewClient(b, &http.Client{
	Transport: &cos.AuthorizationTransport{
		SecretID:  os.Getenv("SECRETID"),
		SecretKey: os.Getenv("SECRETKEY"),
	},
})

res, _, err := c.CI.GetGuetzli(context.Background())
if err == nil {
	fmt.Printf("%v\n", res.GuetzliStatus)
}
```

#### 结果说明

```go
type GetGuetzliResult struct {
    GuetzliStatus string
}
```

| 节点名称      | 描述                                                    | 类型   |
| :------------ | :------------------------------------------------------ | :----- |
| GuetzliStatus | 是否开启 Guetzli 压缩功能，拥有 `on` 与 `off` 两种状态。 | String |

## 关闭 Guetzli 压缩

用于关闭 Guetzli 压缩功能。

#### 方法原型

```go
func (s *CIService) DeleteGuetzli(ctx context.Context) (*Response, error)
```

#### 请求示例

```go
// 需要填写CIURL
u, _ := url.Parse("https://examplebucket-1250000000.cos.ap-guangzhou.myqcloud.com")
cu, _ := url.Parse("http://examplebucket-1250000000.pic.ap-guangzhou.myqcloud.com")
b := &cos.BaseURL{BucketURL: u, CIURL: cu}
c := cos.NewClient(b, &http.Client{
	Transport: &cos.AuthorizationTransport{
		SecretID:  os.Getenv("SECRETID"),
		SecretKey: os.Getenv("SECRETKEY"),
	},
})

_, err := c.CI.DeleteGuetzli(context.Background())
```

