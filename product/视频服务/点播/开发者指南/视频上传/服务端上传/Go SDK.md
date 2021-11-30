对于在服务端上传视频的场景，云点播提供 Go SDK 来实现。上传流程请参见 [服务端上传指引](https://cloud.tencent.com/document/product/266/9759)。

## 集成方式

### 使用 go get 引入
```json
go get -u github.com/tencentcloud/tencentcloud-sdk-go
go get -u github.com/tencentyun/cos-go-sdk-v5
go get -u github.com/tencentyun/vod-go-sdk
```

### 通过源码包安装
如果项目中需要直接引用源码，可以直接下载源码导入项目中使用：

* [从 Github 访问](https://github.com/tencentyun/vod-go-sdk)
* [单击下载 Go SDK](https://github.com/tencentyun/vod-go-sdk/archive/master.zip)

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
调用上传方法，传入接入点地域及上传请求。
```
rsp, err := client.Upload("ap-guangzhou", req)
if err != nil {
    fmt.Println(err)
    return
}
fmt.Println(*rsp.Response.FileId)
fmt.Println(*rsp.Response.MediaUrl)
```

>?上传方法根据用户文件的长度，自动选择普通上传以及分片上传，用户不用关心分片上传的每个步骤，即可实现分片上传。

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
首先 [创建任务流模板](https://cloud.tencent.com/document/product/266/33819) 并为模板命名，发起任务流时，可以用任务流模板名设置`Procedure`参数，上传成功后会自动执行任务流。
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
    req.Procedure = common.StringPtr("Your Proceducre Name")
    
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

### 指定存储地域
在 [控制台](https://console.cloud.tencent.com/vod) 确认已经开通目标存储地域，若没有开通可以参考 [上传存储设置](/document/product/266/14059)，最后通过`StorageRegion`属性设置存储地域的 [英文简称](/document/product/266/9760#.E4.B8.8A.E4.BC.A0.E5.AD.98.E5.82.A8)。
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
    req.StorageRegion = common.StringPtr("ap-chongqing")
    
    rsp, err := client.Upload("ap-guangzhou", req)
    if err != nil {
        fmt.Println(err)
        return
    }
    fmt.Println(*rsp.Response.FileId)
    fmt.Println(*rsp.Response.MediaUrl)
}
```

### 指定分片并发数
分片并发数是针对大文件，拆分成多个分片同时进行上传。分片并发上传的优势在于可以快速完成单个文件的上传，SDK 会根据用户文件的长度，自动选择普通上传以及分片上传，用户不用关心分片上传的每个步骤，即可实现分片上传。而文件的分片并发数通过`ConcurrentUploadNumber`参数进行指定。
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
    req.ConcurrentUploadNumber = common.Uint64Ptr(5)
    
    rsp, err := client.Upload("ap-guangzhou", req)
    if err != nil {
        fmt.Println(err)
        return
    }
    fmt.Println(*rsp.Response.FileId)
    fmt.Println(*rsp.Response.MediaUrl)
}
```

### 使用临时证书上传
传入临时证书的相关密钥信息，使用临时证书验证身份并进行上传。
```
package main

import (
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentyun/vod-go-sdk"
	"fmt"
)

func main() {
    client := &vod.VodUploadClient{}
    client.SecretId = "Credentials TmpSecretId"
    client.SecretKey = "Credentials TmpSecretKey"
    client.Token = "Credentials Token"
    
    req := vod.NewVodUploadRequest()
    req.MediaFilePath = common.StringPtr("/data/video/Wildlife.mp4")
    
    rsp, err := client.Upload("ap-guangzhou", req)
    if err != nil {
        fmt.Println(err)
        return
    }
    fmt.Println(*rsp.Response.FileId)
    fmt.Println(*rsp.Response.MediaUrl)
}
```


### 设置代理上传
设置上传代理，涉及协议及数据都会经过代理进行处理，开发者可以借助代理在自己公司内网上传文件到腾讯云。
```
package main

import (
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentyun/vod-go-sdk"
	"fmt"
    "net/http"
    "net/url"
)

func main() {
    client := &vod.VodUploadClient{}
    client.SecretId = "your secretId"
    client.SecretKey = "your secretKey"
    proxyUrl, _ := url.Parse("your proxy url")
	client.Transport = &http.Transport{
		Proxy: http.ProxyURL(proxyUrl),
	}
    
    req := vod.NewVodUploadRequest()
    req.MediaFilePath = common.StringPtr("/data/video/Wildlife.mp4")
    
    rsp, err := client.Upload("ap-guangzhou", req)
    if err != nil {
        fmt.Println(err)
        return
    }
    fmt.Println(*rsp.Response.FileId)
    fmt.Println(*rsp.Response.MediaUrl)
}
```

### 自适应码流文件上传
本 SDK 支持上传的自适应码流格式包括 HLS 和 DASH，同时要求 manifest（M3U8 或 MPD）所引用的媒体文件必须为相对路径（即不可以是 URL 和绝对路径），且位于 manifest 的同级目录或者下级目录（即不可以使用`../`）。在调用 SDK 上传接口时，`MediaFilePath`参数填写 manifest 路径，SDK 会解析出相关的媒体文件列表一并上传。

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
    req.MediaFilePath = common.StringPtr("/data/video/prog_index.m3u8")
    
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

## 接口描述
上传客户端类`VodUploadClient`

| 属性名称      | 属性描述                   | 类型      | 必填   |
| --------- | ---------------------- | ------- | ---- |
| SecretId   | 云 API 密钥 ID。        | String | 是    |
| SecretKey | 云 API 密钥 Key。 | String  | 是    |

上传请求类`VodUploadRequest`

| 属性名称      | 属性描述                   | 类型&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; | 必填   |
| --------- | ---------------------- | ------- | ---- |
| MediaFilePath   | 待上传的媒体文件路径。必须为本地路径，不支持 URL。| String 指针 | 是    |
| MediaType   | 待上传的媒体文件类型，可选类型请参见 [媒体上传综述](https://cloud.tencent.com/document/product/266/9760#.E5.AA.92.E4.BD.93.E7.B1.BB.E5.9E.8B)，若 MediaFilePath 路径带后缀可不填。        | String 指针 | 否    |
| MediaName   | 上传后的媒体名称，若不填默认采用 MediaFilePath 的文件名。      | String 指针 | 否    |
| CoverFilePath   | 待上传的封面文件路径。必须为本地路径，不支持 URL。 | String 指针 | 否    |
| CoverType   | 待上传的封面文件类型，可选类型请参见 [媒体上传综述](https://cloud.tencent.com/document/product/266/9760#.E5.AA.92.E4.BD.93.E7.B1.BB.E5.9E.8B)，若 CoverFilePath 路径带后缀可不填。        | String 指针 | 否    |
| Procedure   | 上传后需要自动执行的任务流名称，该参数在创建任务流（[API 方式](/document/product/266/33897) 或 [控制台方式](https://console.cloud.tencent.com/vod/video-process/taskflow)）时由用户指定。具体请参考 [任务流综述](https://cloud.tencent.com/document/product/266/33475#.E4.BB.BB.E5.8A.A1.E6.B5.81)。       | String 指针 | 否    |
| ExpireTime   | 媒体文件过期时间，格式按照 ISO 8601 标准表示，详见 [ISO 日期格式说明](https://cloud.tencent.com/document/product/266/11732#52)。        | String 指针 | 否    |
| ClassId   | 分类 ID，用于对媒体进行分类管理，可通过 [创建分类](https://cloud.tencent.com/document/product/266/31772) 接口，创建分类，获得分类 ID。        | int64 指针 | 否    |
| SourceContext   | 来源上下文，用于透传用户请求信息，上传回调接口将返回该字段值，最长250个字符。        | String 指针 | 否    |
| SubAppId   | 云点播 [子应用](/document/product/266/14574) ID。如果要访问子应用中的资源，则将该字段填写为子应用 ID，否则无需填写该字段。        | uint64 指针 | 否    |
| StorageRegion   | 存储地域，指定预期希望存储的地域，该字段填写为存储地域的 [英文简称](/document/product/266/9760#.E4.B8.8A.E4.BC.A0.E5.AD.98.E5.82.A8)。        | String 指针 | 否    |
| ConcurrentUploadNumber   | 分片并发数，针对大文件分片时有效。        | Integer | 否    |

上传响应类 `VodUploadResponse`

| 属性名称      | 属性描述                   | 类型      |
| --------- | ---------------------- | ------- |
| Response   | 上传返回结果信息。        | struct |
| Response.FileId   | 媒体文件的唯一标识。        | String 指针 |
| Response.MediaUrl | 媒体播放地址。 | String 指针  |
| Response.CoverUrl | 媒体封面地址。 | String 指针  |
| Response.RequestId | 唯一请求 ID，每次请求都会返回。定位问题时需要提供该次请求的 RequestId。 | String 指针  |

上传方法 `VodUploadClient.Upload(region string, request *VodUploadRequest)`

| 参数名称      | 参数描述                   | 类型      | 必填   |
| --------- | ---------------------- | ------- | ---- |
| region   | 接入点地域，即请求到哪个地域的云点播服务器，不同于存储地域，具体参考支持的 [地域列表](https://cloud.tencent.com/document/product/266/31756#.E5.9C.B0.E5.9F.9F.E5.88.97.E8.A1.A8)。        | String | 是    |
| request   | 上传请求。        | VodUploadRequest 指针 | 是    |

## 错误码表

| 状态码         | 含义               |
| ----------- | ----------------- |
| InternalError       | 内部错误。 |
| InvalidParameter.ExpireTime       | 参数值错误：过期时间。 |
| InvalidParameterValue.CoverType       | 参数值错误：封面类型。     |
| InvalidParameterValue.MediaType       | 参数值错误：媒体类型。           |
| InvalidParameterValue.SubAppId       | 参数值错误：子应用 ID。              |
| InvalidParameterValue.VodSessionKey       | 参数值错误：点播会话。              |
| ResourceNotFound       | 资源不存在。              |


