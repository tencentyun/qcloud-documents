## Terraform 是什么？
[Terraform](https://www.terraform.io/) 是一款使用 Go 编写、运行在客户端、开源的资源编排工具。基于 HashiCorp Plugin 的架构设计，赋予 Terraform 高度可扩展的特性。目前腾讯云也基于 Terraform Plugin 实现了 TencentCloud Provider，支持通过 Terraform 管理腾讯云上资源。示意图如下：
![](https://qcloudimg.tencent-cloud.cn/raw/69ea96aa85a163700d360676fa01abd8.png)

[TencentCloud Provider](https://github.com/tencentcloudstack/terraform-provider-tencentcloud) 基于 tencentcloud-sdk-go 实现，目前已经提供了超过183个 Resource 和158个 Data Source，覆盖计算、存储、网络、容器服务、负载均衡、中间件、数据库、云监控等超过30款产品，已满足众多用户的基本上云需求。

您可通过 EdgeOne 提供的 [Terraform 文档](https://registry.terraform.io/providers/tencentcloudstack/tencentcloud/latest/docs/resources/teo_zone) 及 [Terraform 编写样例](https://github.com/tencentcloudstack/terraform-provider-tencentcloud/tree/master/examples/tencentcloud-teo)，来快速了解并开始使用 Terraform。


## Terraform 优势
### 多云编排
Terraform 适用于多云方案，您可将相类似的基础结构部署到腾讯云、其他云提供商或本地数据中心。开发人员能够使用相同的工具和相似的配置文件同时管理不同云提供商的资源。

### 基础设施及代码
基础设施可以使用高级配置语法 HCL 进行描述，使得基础设施能够被代码化和版本化，从而可以进行共享和重复使用。示例如下：
```terraform
# 以 NS 接入方式创建站点 example.com  
resource "tencentcloud_teo_zone" "zone" {
  zone_name      = "example.com"
  # 通过 zone_available_plans 查询您可用的套餐信息
  plan_type      = "<your-plan-type>"
  type           = "full"
  paused         = false
  cname_speed_up = "enabled"
}

# 创建 example.com 的 DNS 记录
resource "tencentcloud_teo_dns_record" "dns_record" {
  zone_id     = tencentcloud_teo_zone.zone.id
  type        = "A"
  name        = "example.com"
  # 开启 CDN 加速服务
  mode        = "proxied"
  content     = "<your-backend-ip>"
  ttl         = 60
}
```

### 执行计划
Terraform 具备 “Planning” 步骤，执行 terraform plan 命令后 Terraform 会生成执行计划。执行计划会显示当调用 apply 时 Terraform 的状态，您可通过该能力在 Terraform 操作基础设施时避免任何意外。示例如下：
```
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # tencentcloud_teo_dns_record.dns_record will be created
  + resource "tencentcloud_teo_dns_record" "dns_record" {
      + cname         = (known after apply)
      + content       = "<your-backend-ip>"
      + created_on    = (known after apply)
      + domain_status = (known after apply)
      + id            = (known after apply)
      + locked        = (known after apply)
      + mode          = "proxied"
      + modified_on   = (known after apply)
      + name          = "example.com"
      + priority      = (known after apply)
      + type          = "A"
      + status        = (known after apply)
      + ttl           = 60
      + zone_id       = (known after apply)
    }

  # tencentcloud_teo_zone.zone will be created
  + resource "tencentcloud_teo_zone" "zone" {
      + area                    = (known after apply)
      + cname_speed_up          = "enabled"
      + cname_status            = (known after apply)
      + created_on              = (known after apply)
      + id                      = (known after apply)
      + modified_on             = (known after apply)
      + name                    = "example.com"
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

Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.
```

### 自动变更
您可在基础设施上通过最少的人工干预工作，应用复杂的变更集。通过前文中的执行计划及资源拓扑，您可准确获取 Terraform 动态，避免可能的人为错误。

## 远程状态管理
Terraform 引入了远程状态存储机制 Backend，目前腾讯云可通过 [对象存储 COS](https://cloud.tencent.com/document/product/436) 来管理用户的 tfState 文件，避免将文件保存在本地，造成丢失。同时，远程存储使多人同时对 Terraform 资源进行管理成为可能。

 
