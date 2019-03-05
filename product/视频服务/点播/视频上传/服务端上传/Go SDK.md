对于在服务端上传视频的场景，腾讯云点播提供了 Go SDK 来实现。上传的流程可以参见 [服务端上传指引](https://cloud.tencent.com/document/product/266/9759)。

## 集成方式

### 使用 go get 引入
```json
go get -u github.com/tencentcloud/tencentcloud-sdk-go
go get -u github.com/tencentyun/cos-go-sdk-v5
go get -u github.com/tencentyun/vod-go-sdk
```

### 通过源码包安装
如果项目中需要直接引用源码，可以直接下载源码导入项目中使用：

* [从 Github 访问 >>](https://github.com/tencentyun/vod-go-sdk)
* [单击下载 Go SDK >>](https://github.com/tencentyun/vod-go-sdk/archive/master.zip)

##  简单视频上传
### 初始化上传对象
使用云 API 密钥初始化 VodUploadClient 实例。

```
import (
	"github.com/tencentyun/vod-go-sdk"
)

client := &vod.VodUploadClient{}
client.SecretId = "your secretId"
client.SecretKey = "your secretKey"
```

### 构造上传请求对象
```
import (
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
)

req := vod.NewVodUploadRequest()
req.MediaFilePath = common.StringPtr("/data/video/Wildlife.mp4")
```

### 调用上传
调用上传方法，传入上传地域及上传请求。
```
rsp, err := client.Upload("ap-guangzhou", req)
if err != nil {
    fmt.Println(err)
    return
}
fmt.Println(*rsp.Response.FileId)
fmt.Println(*rsp.Response.MediaUrl)
```

## 高级功能
### 携带封面
```
package main

import (
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentyun/vod-go-sdk"
	"fmt"
)

func main() {
    client := &vod.VodUploadClient{}
    client.SecretId = "your secretId"
    client.SecretKey = "your secretKey"
    
    req := vod.NewVodUploadRequest()
    req.MediaFilePath = common.StringPtr("/data/video/Wildlife.mp4")
    req.CoverFilePath = common.StringPtr("/data/video/Wildlife-cover.png")
    
    rsp, err := client.Upload("ap-guangzhou", req)
    if err != nil {
        fmt.Println(err)
        return
    }
    fmt.Println(*rsp.Response.FileId)
    fmt.Println(*rsp.Response.MediaUrl)
    fmt.Println(*rsp.Response.CoverUrl)
}
```

### 指定任务流
传入任务流参数，具体的任务流介绍参考 [参数模板与任务流](https://cloud.tencent.com/document/product/266/11700)，上传成功后会自动执行任务流。
```
package main

import (
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentyun/vod-go-sdk"
	"fmt"
)

func main() {
    client := &vod.VodUploadClient{}
    client.SecretId = "your secretId"
    client.SecretKey = "your secretKey"
    
    req := vod.NewVodUploadRequest()
    req.MediaFilePath = common.StringPtr("/data/video/Wildlife.mp4")
    req.Procedure = common.StringPtr("QCVB_SimpleProcessFile(1, 1)")
    
    rsp, err := client.Upload("ap-guangzhou", req)
    if err != nil {
        fmt.Println(err)
        return
    }
    fmt.Println(*rsp.Response.FileId)
    fmt.Println(*rsp.Response.MediaUrl)
}
```

### 子应用上传
传入 [子应用](https://cloud.tencent.com/document/product/266/14574) ID，上传成功后资源只属于具体的子应用。
```
package main

import (
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentyun/vod-go-sdk"
	"fmt"
)

func main() {
    client := &vod.VodUploadClient{}
    client.SecretId = "your secretId"
    client.SecretKey = "your secretKey"
    
    req := vod.NewVodUploadRequest()
    req.MediaFilePath = common.StringPtr("/data/video/Wildlife.mp4")
    req.SubAppId = common.Uint64Ptr(101)
    
    rsp, err := client.Upload("ap-guangzhou", req)
    if err != nil {
        fmt.Println(err)
        return
    }
    fmt.Println(*rsp.Response.FileId)
    fmt.Println(*rsp.Response.MediaUrl)
}
```

## 接口描述
上传客户端类 `VodUploadClient`：

| 属性名称      | 属性描述                   | 类型      | 必填   |
| --------- | ---------------------- | ------- | ---- |
| SecretId   | 云 API 密钥 ID。        | string | 是    |
| SecretKey | 云 API 密钥 Key。 | string  | 是    |

上传请求类 `VodUploadRequest`：

| 属性名称      | 属性描述                   | 类型      | 必填   |
| --------- | ---------------------- | ------- | ---- |
| MediaFilePath   | 媒体文件路径。        | string 指针 | 是    |
| MediaType   | 媒体文件类型，可选类型参考 [视频上传综述](https://cloud.tencent.com/document/product/266/9760#.E6.96.87.E4.BB.B6.E7.B1.BB.E5.9E.8B)，若 MediaFilePath 路径带后缀可不填。        | String 指针 | 否    |
| MediaName   | 媒体名称，若不填默认采用 MediaFilePath 的文件名。      | string 指针 | 否    |
| CoverFilePath   | 封面文件路径。        | string 指针 | 否    |
| CoverType   | 媒体文件类型，可选类型参考 [视频上传综述](https://cloud.tencent.com/document/product/266/9760#.E5.B0.81.E9.9D.A2.E7.B1.BB.E5.9E.8B)，若 CoverFilePath 路径带后缀可不填。        | string 指针 | 否    |
| Procedure   | 任务流，具体的任务流介绍参考[任务流综述](/document/product/266/11700)。        | string 指针 | 否    |
| ExpireTime   | 媒体文件过期时间，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#iso-.E6.97.A5.E6.9C.9F.E6.A0.BC.E5.BC.8F)。        | string 指针 | 否    |
| ClassId   | 分类 ID，用于对媒体进行分类管理，可通过 [创建分类](https://cloud.tencent.com/document/product/266/31772) 接口，创建分类，获得分类 ID。        | int64 指针 | 否    |
| SourceContext   | 来源上下文，用于透传用户请求信息，上传回调接口将返回该字段值，最长 250 个字符。        | string 指针 | 否    |
| SubAppId   | 点播[子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID；否则无需填写该字段。        | uint64 指针 | 否    |

上传响应类 `VodUploadResponse`：

| 属性名称      | 属性描述                   | 类型      |
| --------- | ---------------------- | ------- |
| Response   | 上传返回结果信息。        | struct |
| Response.FileId   | 媒体文件的唯一标识。        | string 指针 |
| Response.MediaUrl | 媒体播放地址。 | string 指针  |
| Response.CoverUrl | 媒体封面地址。 | string 指针  |
| Response.RequestId | 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。 | string 指针  |

上传方法 `VodUploadClient.Upload(region string, request *VodUploadRequest)`：

| 参数名称      | 参数描述                   | 类型      | 必填   |
| --------- | ---------------------- | ------- | ---- |
| region   | 上传地域，具体参考支持的 [地域列表](https://cloud.tencent.com/document/product/266/31756#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。        | string | 是    |
| request   | 上传请求。        | VodUploadRequest 指针 | 是    |

## 错误码列表

| 状态码         | 含义               |
| ----------- | ----------------- |
| InternalError       | 内部错误。 |
| InvalidParameter.ExpireTime       | 参数值错误：过期时间。 |
| InvalidParameterValue.CoverType       | 参数值错误：封面类型。     |
| InvalidParameterValue.MediaType       | 参数值错误：媒体类型。           |
| InvalidParameterValue.SubAppId       | 参数值错误：子应用 ID。              |
| InvalidParameterValue.VodSessionKey       | 参数值错误：点播会话。              |
| ResourceNotFound       | 资源不存在。              |
