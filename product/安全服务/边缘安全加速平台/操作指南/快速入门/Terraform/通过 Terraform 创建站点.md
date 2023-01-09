## 功能简介
腾讯云边缘安全加速平台（TencentCloud EdgeOne，下文简称为 EdgeOne）已经接入 Terraform，可以通过 Terraform 来实现快速配置。本文介绍如何使用 Terraform 快速添加 EdgeOne 站点。

## 前提条件
已完成 Terraform 的安装与配置，操作步骤请参见 [安装和配置 Terraform](https://cloud.tencent.com/document/product/1552/80472)。

## 操作步骤
1. 定义通过 Terraform 管理的站点资源。
   您需要编写 Terraform 配置文件，并以`.tf`后缀保存。您可以在 Terraform Provider 文档页面上查看 [EdgeOne 站点资源](https://registry.terraform.io/providers/tencentcloudstack/tencentcloud/latest/docs/resources/teo_zone) 的参数定义。
	 以下为示例配置文件 tencent_teo.tf 的内容：
```terraform
terraform {
  required_providers {
    tencentcloud = {
      source  = "tencentcloudstack/tencentcloud"
      version = ">= 1.78.5"
    }
  }
}
provider "tencentcloud" {
  secret_id  = "<your-secret-id>"
  secret_key = "<your-secret-key>"
  region     = "ap-guangzhou"
}
resource "tencentcloud_teo_zone" "example" {
  zone_name = "example.com"
  plan_type = "<your-plan-type>"
  tags = {
    "createdBy" = "terraform"
  }
}
```

2. 在您保存 Terraform 配置文件的目录下，执行 `terraform init` 命令初始化配置。
   此步骤中，Terraform 会自动检测配置文件中的 provider 字段，并下载最新版本的模块和插件。
   若打印如下信息，则表示初始化成功。
```
Initializing the backend...
Initializing provider plugins...
- Finding tencentcloudstack/tencentcloud versions matching ">= 1.78.5"...
- Installing tencentcloudstack/tencentcloud v1.78.5...
- Installed tencentcloudstack/tencentcloud v1.78.5 (signed by a HashiCorp partner, key ID 84F69E1C1BECF459)
Partner and community providers are signed by their developers.
If you'd like to know more about provider signing, you can read about it here:
https://www.terraform.io/docs/cli/plugins/signing.html
Terraform has created a lock file .terraform.lock.hcl to record the provider
selections it made above. Include this file in your version control repository
so that Terraform can guarantee to make the same selections by default when
you run "terraform init" in the future.
Terraform has been successfully initialized!
```

3. 执行`terraform plan`命令预览配置，可以校验配置是否正确。
```
PS tf-doc> terraform.exe plan
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
Terraform will perform the following actions:
  # tencentcloud_teo_zone.example will be created
  + resource "tencentcloud_teo_zone" "example" {
      + area                    = (known after apply)
      + cname_speed_up          = (known after apply)
      + cname_status            = (known after apply)
      + created_on              = (known after apply)
      + id                      = (known after apply)
      + modified_on             = (known after apply)
      + name_servers            = (known after apply)
      + original_name_servers   = (known after apply)
      + paused                  = (known after apply)
      + plan_type               = "ent"
      + resources               = (known after apply)
      + status                  = (known after apply)
      + tags                    = {
          + "createdBy" = "terraform"
        }
      + type                    = (known after apply)
      + vanity_name_servers_ips = (known after apply)
      + zone_id                 = (known after apply)
      + zone_name               = "example.com"
    }
Plan: 1 to add, 0 to change, 0 to destroy.
───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────
Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.
```

4. 执行`terraform apply`添加 EdgeOne 站点。
   执行 apply 命令后 Terraform 会让您再次确认将要执行的动作。在确认无误后输入`yes`二次确认，然后等待命令执行完成。
```
PS tf-doc> terraform apply
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
Terraform will perform the following actions:
  # tencentcloud_teo_zone.example will be created
  + resource "tencentcloud_teo_zone" "example" {
      + area                    = (known after apply)
      + cname_speed_up          = (known after apply)
      + cname_status            = (known after apply)
      + created_on              = (known after apply)
      + id                      = (known after apply)
      + modified_on             = (known after apply)
      + name_servers            = (known after apply)
      + original_name_servers   = (known after apply)
      + paused                  = (known after apply)
      + plan_type               = "ent"
      + resources               = (known after apply)
      + status                  = (known after apply)
      + tags                    = {
          + "createdBy" = "terraform"
        }
      + type                    = (known after apply)
      + vanity_name_servers_ips = (known after apply)
      + zone_id                 = (known after apply)
      + zone_name               = "example.com"
    }
Plan: 1 to add, 0 to change, 0 to destroy.
Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.
  Enter a value: yes
tencentcloud_teo_zone.example: Creating...
tencentcloud_teo_zone.example: Creation complete after 6s [id=zone-2ag9gej58j36]
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```
5. 修改接入站点的 DNS 配置。
   为使站点生效，以 NS 方式接入则需要修改站点的 NS 服务器，以 CNAME 方式接入则需要添加 TXT 记录作为站点验证。详情请参见 [站点接入方式](https://cloud.tencent.com/document/product/1552/70787)。
   ![](https://qcloudimg.tencent-cloud.cn/raw/25c401d0261cd6e4ed587dfe538f543b.png)
6. 验证站点已生效。
   执行步骤 5 之后等待几分钟，通过`terraform refresh`刷新资源状态，然后执行`terraform show`查看站点是否已经生效。
   以 NS 方式接入站点，生效后`status`字段的值应为`active`，以 CNAME 方式接入的站点，生效后`cname_status`字段的值应为`finished`。
```
PS tf-doc> terraform refresh
tencentcloud_teo_zone.example: Refreshing state... [id=zone-2ag9gej58j36]
PS tf-doc> terraform show   
# tencentcloud_teo_zone.example:
resource "tencentcloud_teo_zone" "example" {
    area                    = "overseas"
    cname_speed_up          = "enabled"
    cname_status            = "pending"
...
    original_name_servers   = []
    paused                  = false
    plan_type               = "ent"
    status                  = "active"
    tags                    = {
        "createdBy" = "terraform"
    }
    type                    = "full"
    vanity_name_servers_ips = []
    zone_id                 = "zone-2ag9gej58j36"
    zone_name               = "example.com"
}
```

## 注意事项
1. 创建站点时，您可以通过 Data Source [zone_available_plans](https://registry.terraform.io/providers/tencentcloudstack/tencentcloud/latest/docs/data-sources/teo_zone_available_plans) 来查询适合您的套餐。
2. 您可以通过 [环境变量](https://registry.terraform.io/providers/tencentcloudstack/tencentcloud/latest/docs#environment-variables) 的方式配置 Terraform，从而避免将云 API 密钥写在 Terraform 配置文件中。
