
Terraform 依靠 Provider 插件与云提供商、SaaS 提供者和其他 API 进行交互。Terraform 配置必须声明插件需要哪些提供程序，以便 Terraform 可以安装和使用。此外，某些提供程序需要配置才能使用。本文介绍 Provider 插件配置方法。


## 搜索 Provider
前往 [Terraform 插件列表](https://registry.terraform.io/browse/providers) 页面，搜索并进入 [TencentCloud Provider](https://registry.terraform.io/providers/tencentcloudstack/tencentcloud/latest) 页面查看使用指南。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/9bb034daa2cfde36c489232369db308a.png)

## 下载 Provider
执行以下命令，默认从 Terraform 官方仓库下载最新版本的插件。
```bash
terraform init
```
若需使用历史版本，可通过 `version` 参数指定版本信息。如下所示：
```bash
terraform {
  required_providers {
    tencentcloud = {
      source = "tencentcloudstack/tencentcloud"
      # 通过version指定版本
      version = "1.60.18"
    }
  }
}
```

## Provider 声明
```
provider "tencentcloud" {
  region = "ap-guangzhou"
  secret_id = "my-secret-id"
  secret_key = "my-secret-key"
}
```
