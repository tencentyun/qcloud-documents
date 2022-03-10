
模块是包含一组 Terraform 代码的文件夹，是对多个资源的抽象和封装。


## 调用模块
在 Terraform 代码中使用 `module` 块引用模块。一个 `module` 块包含 `module` 关键字、`module` 名称和 `module` 体（`{}`之间的部分）三部分。如下所示：
```bash
module "servers" {
  source = "./app-cluster"

  servers = 5
}
```
`module` 调用可以使用下列参数：
- `source`：指定引用模块的源。
- `version`：指定引用模块的版本号。
- `meta-arguments`：Terraform 0.13开始支持的特性，类似 `resource` 与 `data`，可以用来操作 `module` 的行为，详情请参见 [MetaData](https://cloud.tencent.com/document/product/1213/67074)。


## 参数说明

### Source


`source` 参数用来指定模块源，指定 Terraform 获取子模块源代码的方式。Terraform 在 `terraform init` 的安装步骤中，使用它将源代码下载到本地磁盘上，以便其他 Terraform 命令可以使用。

模块安装程序支持从以下源类型进行安装：
- 本地路径
- TerraformRegistry
- GitHub
- Bitbucket
- Generic Git, Mercurial repositories
- HTTP URLs
- S3 buckets
- GCS buckets
- Modules in Package Sub-directories

本文介绍本地路径、TerraformRegistry 及 GitHub 的使用方法：

#### 本地路径
本地路径可以使用同一项目中的子模块，与其他资源的区别是无需下载相关代码即可使用。例如：
```bash
module "consul" {
  source = "./consul"
}
```

#### TerraformRegistry
Registry 目前是 Terraform 官方推荐的模块仓库方案，采用了 Terraform 定制的协议，支持版本化管理和使用模块。官方提供的 [公共仓库](https://registry.terraform.io/) 中保存和索引了大量公共模块，可以快速搜索到各类官方和社区提供的高质量模块。

公共仓库的模块可以用 `<NAMESPACE>/<NAME>/<PROVIDER>` 形式的源地址来引用，您可在模块介绍中获取确切的源地址。例如：
```bash
module "consul" {
  source = "hashicorp/consul/xxx"
  version = "0.1.0"
}
```
托管在其他仓库的模块，则需在源地址头部添加 `<HOSTNAME>/` 部分，指定私有仓库的主机名。例如：
```bash
module "consul" {
  source = "app.terraform.io/example-corp/k8s-cluster/azurerm"
  version = "1.1.0"
}
```

#### GitHub
若 Terraform 读取 source 参数值，是以 `github.com` 为前缀时，会将其自动识别为一个 GitHub 源。例如，使用 HTTPS 协议克隆仓库：
```bash
module "consul" {
  source = "github.com/hashicorp/example"
}
``` 
如需使用 SSH 协议，则请使用如下地址：
```bash
module "consul" {
  source = "git@github.com:hashicorp/example.git"
}
```

<dx-alert infotype="explain" title="">
GitHub 源的处理与通用 Git 仓库一致，它们获取 git 凭证和通过 ref 参数引用特定版本的方式均一致。如需访问私有仓库，则需额外配置 git 凭证。
</dx-alert>


### Version
使用 registry 作为模块源时，可以使用 `version` 元参数约束使用的模块版本。例如：
```bash
module "consul" {
  source  = "hashicorp/consul/xxx"
  version = "0.0.5"

  servers = 3
}
```
`version` 元参数的格式与 Provider 版本约束的格式一致。在满足版本约束的前提下，Terraform 会使用当前已安装的最新版本的模块实例。若当前没有满足约束的版本被安装过，则会下载符合约束的最新的版本。

`version` 元参数只能配合 registry 使用，支持公共的或私有的模块仓库。其他类型的模块源不一定支持版本化，本地路径模块不支持版本化。
