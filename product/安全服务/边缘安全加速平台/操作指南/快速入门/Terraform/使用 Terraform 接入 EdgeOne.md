本文介绍如何使用 Terraform 快速创建 EdgeOne 站点，并添加一个域名及功能配置。开始操作前，请确认已完成 [安装和配置 Terraform](https://cloud.tencent.com/document/product/1552/80472)。

## 操作步骤
1. 创建 `provider.tf` 文件，指定 provider 配置信息。
```
terraform {
  required_providers {
    tencentcloud = {
      source = "tencentcloudstack/tencentcloud"
      # 通过 version 指定版本
      # version = ">=1.77.6"
    }
  }
}
provider "tencentcloud" {
  region = "ap-guangzhou"
  # secret_id = "my-secret-id"
  # secret_key = "my-secret-key"
}
```
2. 创建 `main.tf` 文件，配置腾讯云 Provider 创建 test.com 站点，选择合适的套餐类型并开启站点加速服务。
```
# 以 NS 接入方式创建站点 test.com  
resource "tencentcloud_teo_zone" "zone" {
  name           = "test.com"
  # 选择套餐
  plan_type      = "sta"
  type           = "full"
  paused         = false
  cname_speed_up = "enabled"
}
# 创建 test.com 的 DNS 记录
resource "tencentcloud_teo_dns_record" "dns_record" {
  zone_id     = tencentcloud_teo_zone.zone.id
  record_type = "A"
  name        = "test.com"
  # 开启 CDN 加速服务
  mode        = "proxied"
  content     = "2.2.2.2"
  ttl         = 80
}
```
3. 执行以下命令，初始化工作目录并下载插件。Terraform 会自动检测 .tf 文件中的 provider 字段，然后通过 Terraform 官方 GitHub 下载最新版本相关资源的模块和插件。
```
terraform init
```
返回信息如下所示：
```
Initializing the backend...
Initializing provider plugins...
- Finding latest version of tencentcloudstack/tencentcloud...
- Installing tencentcloudstack/tencentcloud v1.77.6...
- Installed tencentcloudstack/tencentcloud v1.77.6 (signed by a HashiCorp partner, key ID 84F69E1C1BECF111)
Partner and community providers are signed by their developers.
If you'd like to know more about provider signing, you can read about it here:
https://www.terraform.io/docs/cli/plugins/signing.html
Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.
Terraform has been successfully initialized!
You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.
If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```
2. 执行以下命令，查看执行计划，显示将要创建的资源详情。
```
terraform plan
```
返回信息如下所示：
```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
Terraform will perform the following actions:
  # tencentcloud_teo_dns_record.dns_record will be created
  + resource "tencentcloud_teo_dns_record" "dns_record" {
      + cname         = (known after apply)
      + content       = "2.2.2.2"
      + created_on    = (known after apply)
      + domain_status = (known after apply)
      + id            = (known after apply)
      + locked        = (known after apply)
      + mode          = "proxied"
      + modified_on   = (known after apply)
      + name          = "test.com"
      + priority      = (known after apply)
      + record_type   = "A"
      + status        = (known after apply)
      + ttl           = 80
      + zone_id       = (known after apply)
      + zone_name     = (known after apply)
    }
  # tencentcloud_teo_zone.zone will be created
  + resource "tencentcloud_teo_zone" "zone" {
      + area                    = (known after apply)
      + cname_speed_up          = "enabled"
      + cname_status            = (known after apply)
      + created_on              = (known after apply)
      + id                      = (known after apply)
      + modified_on             = (known after apply)
      + name                    = "test.com"
      + name_servers            = (known after apply)
      + original_name_servers   = (known after apply)
      + paused                  = false
      + plan_type               = "sta"
      + status                  = (known after apply)
      + type                    = "full"
      + vanity_name_servers_ips = (known after apply)
      + vanity_name_servers {
          + servers = (known after apply)
          + switch  = (known after apply)
        }
    }
Plan: 2 to add, 0 to change, 0 to destroy.
───────────────────────────────────────────────────────────────────────────────
Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.<dx-tabs>
```
5. 执行以下命令，创建资源。
```
terraform apply
```
根据提示输入 `yes` 创建资源，返回信息如下所示：
```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
Terraform will perform the following actions:
  # tencentcloud_teo_dns_record.dns_record will be created
  + resource "tencentcloud_teo_dns_record" "dns_record" {
      + cname         = (known after apply)
      + content       = "2.2.2.2"
      + created_on    = (known after apply)
      + domain_status = (known after apply)
      + id            = (known after apply)
      + locked        = (known after apply)
      + mode          = "proxied"
      + modified_on   = (known after apply)
      + name          = "test.com"
      + priority      = (known after apply)
      + record_type   = "A"
      + status        = (known after apply)
      + ttl           = 80
      + zone_id       = (known after apply)
      + zone_name     = (known after apply)
    }
  # tencentcloud_teo_zone.zone will be created
  + resource "tencentcloud_teo_zone" "zone" {
      + area                    = (known after apply)
      + cname_speed_up          = "enabled"
      + cname_status            = (known after apply)
      + created_on              = (known after apply)
      + id                      = (known after apply)
      + modified_on             = (known after apply)
      + name                    = "test.com"
      + name_servers            = (known after apply)
      + original_name_servers   = (known after apply)
      + paused                  = false
      + plan_type               = "sta"
      + status                  = (known after apply)
      + type                    = "full"
      + vanity_name_servers_ips = (known after apply)
      + vanity_name_servers {
          + servers = (known after apply)
          + switch  = (known after apply)
        }
    }
Plan: 2 to add, 0 to change, 0 to destroy.
Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.
  Enter a value: yes
tencentcloud_teo_zone.zone: Creating...
tencentcloud_teo_zone.zone: Creation complete after 4s [id=zone-28jw59kum911]
Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```
6. 执行完毕后，可以登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone) 查看创建的站点和配置，并根据提示修改 NS 服务器地址，修改后单击**完成**即可开启 EdgeOne 安全加速服务。
![](https://qcloudimg.tencent-cloud.cn/raw/25c401d0261cd6e4ed587dfe538f543b.png)

