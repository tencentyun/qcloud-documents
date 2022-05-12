## 远程状态存储机制
状态文件若仅存储在本地，将可能存在以下问题：
 - `tfstate` 文件默认保存在当前工作目录下的本地文件，若计算机损坏导致文件丢失，`tfstate` 文件所对应的资源都将无法管理，产生资源泄漏。
 - 团队成员间无法共享 `tfstate` 文件。


为了解决状态文件的存储和共享问题，Terraform 引入了远程状态存储机制 Backend。Backend 是一种抽象的远程存储接口，类似 Provider，Backend 也支持多种不同的远程存储服务，详情请参见 [Available Backends](https://www.terraform.io/language/settings/backends/local)。Terraform Backend 分为两种：
- **标准**：支持远程状态存储与状态锁。
- **增强**：在标准的基础上支持远程操作（在远程服务器上执行 plan、apply 等操作）。

## 说明事项
- backend 配置更新后需运行 `terraform init` 来验证和配置 backend。
- 未配置 backend 时，Terraform 默认使用本地 backend。例如，`tfstate` 文件默认是存储在本地目录下的。
- backend 配置存在以下重要限制：
 - 一个配置只能提供一个后端块。
 - 后端块不能引用命名值（如输入变量、局部变量或数据源属性）。

## 使用 Backend
`backend` 块嵌套定义在顶级 terraform 块中，本文以使用腾讯云对象存储 COS 服务进行配置。示例如下，如需使用其他存储模式，可前往 [Available Backends](https://www.terraform.io/language/settings/backends/local) 了解更多信息。
```bash
terraform {
  backend "cos" {
    region = "ap-nanjing"
    bucket = "tfstate-cos-1308126961"
    prefix = "terraform/state"
  }
}
```
若您具备 COS 的 `tfstate-cos-1308126961` 桶，则 Terraform 状态信息将会写进文件 `terraform/state/terraform.tfstate` 中。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/2ea32d07eec635faf91890d2b3361dc2.jpg)

 
