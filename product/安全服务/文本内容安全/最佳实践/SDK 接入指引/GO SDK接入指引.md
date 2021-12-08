## 支持环境
- 使用 Go 1.9 版本及以上（如使用 go mod 需要 Go 1.14），并设置好 GOPATH 等必须的环境变量。
- 调用地址：`tms.tencentcloudapi.com`。
>!API 支持就近地域接入，本产品就近地域接入的域名为 tms.tencentcloudapi.com，也支持指定地域域名访问，例如：广州地域的域名为tms.ap-guangzhou.tencentcloudapi.com。详细请参考 [图片内容安全-请求结构](https://cloud.tencent.com/document/product/1124/51863)。
>

## 安装 GO SDK
### 方式1：通过 go get 安装（推荐）
推荐使用腾讯云镜像加速下载：

| 系统平台      | 运行命令                                         |
| ------------- | ------------------------------------------------ |
| Linux / MacOS | `export GOPROXY=https://mirrors.tencent.com/go/` |
| Windows       | `set GOPROXY=https://mirrors.tencent.com/go/`    |

v1.0.170后可以按照产品下载，您只需下载基础包和对应的产品包（如 CVM）即可，不需要下载全部的产品，从而加快您构建镜像或者编译的速度。当然您也可以按照之前的方式一次性下载腾讯云所有产品的包。
>?
>- 按需安装方式：仅支持使用 Go Modules 模式进行依赖管理，即环境变量 `GO111MODULE=auto` 或者 `GO111MODULE=on`，并且在您的项目中执行了 `go mod init xxx`。如果您使用 GOPATH，请参考全部安装方式。
>- 全部安装方式：支持 GOPATH 和 Go Modules。
>
<table>
<thead>
<tr>
<th>安装方式</th>
<th>安装说明</th>
<th>运行命令</th>
</tr>
</thead>
<tbody><tr>
<td  rowspan=2 >按需安装（推荐）</td>
<td>安装公共基础包</td>
<td><code>go get -v -u github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common</code></td>
</tr>
<tr>
<td>安装对应的产品包（如 CVM）</td>
<td><code>go get -v -u github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/cvm</code></td>
</tr>
<tr>
<td>全部安装</td>
<td>一次性下载腾讯云所有产品的包</td>
<td><code>go get -v -u github.com/tencentcloud/tencentcloud-sdk-go</code></td>
</tr>
</tbody></table>

>?为了支持 go mod，SDK 版本号从 v3.x 降到了 v1.x。并于2021年05月10日移除了所有 `v3.0.*` 和 `3.0.*`的 tag，如需追溯以前的 tag，请参见项目根目录下的 `commit2tag` 文件。
>
### 方式2：通过源码包安装
前往代码托管地址 [Github](https://github.com/tencentcloud/tencentcloud-sdk-go) 或者 [Gitee](https://gitee.com/tencentcloud/tencentcloud-sdk-go) 下载最新代码，解压后安装到 $GOPATH/src/github.com/tencentcloud 目录下。

## 使用 SDK
以下为 ImageModeration 接口的 Demo 示例（region 配置为广州，实际请按需配置）。
```
package main
import ("fmt"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/errors"
	"github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/common/profile"
	tms "github.com/tencentcloud/tencentcloud-sdk-go/tencentcloud/tms/v20201229") func main() {
	credential: = common.NewCredential("SecretId", "SecretKey", ) cpf: = profile.NewClientProfile() cpf.HttpProfile.Endpoint = "tms.tencentcloudapi.com"
	client,
	_: = tms.NewClient(credential, "ap-guangzhou", cpf) request: = tms.NewTextModerationRequest() response,
	err: = client.TextModeration(request) if _,
	ok: = err.( * errors.TencentCloudSDKError);ok {
		fmt.Printf("An API error has returned: %s", err) return
	}
	if err != nil {
		panic(err)
	}
	fmt.Printf("%s", response.ToJsonString())
}
```
