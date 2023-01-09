## 功能简介
腾讯云边缘安全加速平台（TencentCloud EdgeOne，下文简称为 EdgeOne）已经接入 Terraform，可以通过 Terraform 来实现快速配置。本文介绍如何使用 Terraform 来配置站点加速。站点加速相关配置的说明，详情请参见 [操作指南](https://cloud.tencent.com/document/product/1552/70863)。

## 前提条件
1. 已完成 Terraform 的安装与配置，操作步骤请参见 [安装和配置 Terraform](https://cloud.tencent.com/document/product/1552/80472)。
2. 已通过 Terraform 接入了站点，操作步骤请参见 [通过 Terraform 创建站点](https://cloud.tencent.com/document/product/1552/82136)。

## 操作步骤
1. 修改 Terraform 配置文件，添加站点加速配置的资源定义。
   您可以在 Terraform Provider 文档页面上查看 [站点加速配置](https://registry.terraform.io/providers/tencentcloudstack/tencentcloud/latest/docs/resources/teo_zone_setting) 的参数定义。以下为示例配置文件 tencent_teo.tf 的内容：
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
  plan_type = "ent"
  tags = {
    "createdBy" = "terraform"
  }
}
resource "tencentcloud_teo_zone_setting" "example" {
  zone_id = tencentcloud_teo_zone.example.id
  # 缓存规则配置
  cache {
    follow_origin {
      switch = "on" # 遵循源站
    }
  }
  # 缓存键配置
  cache_key {
    full_url_cache = "off" # 不开启全路径缓存
    ignore_case    = "on" # 忽略大小写
    query_string {
      switch = "on"
      action = "includeCustom" # 仅使用指定的 URL 参数
      value  = ["param0", "param1"]
    }
  }
  # 域名 https 加速配置
  https {
    ocsp_stapling = "on" # OCSP 配置开启
    tls_version   = ["TLSv1.2", "TLSv1.3"] # 支持的 TLS 协议版本
  }
  # 智能压缩配置
  compression {
    switch     = "on"
    algorithms = ["brotli", "gzip"]
  }
  # 回源时携带客户端IP所属地域信息
  client_ip_header {
    switch      = "on"
    header_name = "EO-Client-IPCountry"
  }
}
```

2. 执行`terraform plan`命令预览配置，可以校验配置是否正确。
```
PS tf-doc> terraform.exe plan
tencentcloud_teo_zone.example: Refreshing state... [id=zone-2ag9gej58j36]
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
Terraform will perform the following actions:
  # tencentcloud_teo_zone_setting.example will be created
  + resource "tencentcloud_teo_zone_setting" "example" {
      + area    = (known after apply)
      + id      = (known after apply)
      + zone_id = "zone-2ag9gej58j36"
      + cache {
          + cache {
              + cache_time           = (known after apply)
              + ignore_cache_control = (known after apply)
              + switch               = (known after apply)
            }
          + follow_origin {
              + switch = "on"
            }
          + no_cache {
              + switch = (known after apply)
            }
        }
      + cache_key {
          + full_url_cache = "off"
          + ignore_case    = "on"
          + query_string {
              + action = "includeCustom"
              + switch = "on"
              + value  = [
                  + "param0",
                  + "param1",
                ]
            }
        }
      + cache_prefresh {
          + percent = (known after apply)
          + switch  = (known after apply)
        }
      + client_ip_header {
          + header_name = "EO-Client-IPCountry"
          + switch      = "on"
        }
      + compression {
          + algorithms = [
              + "brotli",
              + "gzip",
            ]
          + switch     = "on"
        }
      + force_redirect {
          + redirect_status_code = (known after apply)
          + switch               = (known after apply)
        }
      + https {
          + ocsp_stapling = "on"
          + tls_version   = [
              + "TLSv1.2",
              + "TLSv1.3",
            ]
        }
      + ipv6 {
          + switch = (known after apply)
        }
      + max_age {
          + follow_origin = (known after apply)
          + max_age_time  = (known after apply)
        }
      + offline_cache {
          + switch = (known after apply)
        }
      + origin {
          + backup_origins       = (known after apply)
          + cos_private_access   = (known after apply)
          + origin_pull_protocol = (known after apply)
          + origins              = (known after apply)
        }
      + post_max_size {
          + max_size = (known after apply)
          + switch   = (known after apply)
        }
      + quic {
          + switch = (known after apply)
        }
      + smart_routing {
          + switch = (known after apply)
        }
      + upstream_http2 {
          + switch = (known after apply)
        }
      + web_socket {
          + switch  = (known after apply)
          + timeout = (known after apply)
        }
    }
Plan: 1 to add, 0 to change, 0 to destroy.
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.
```

3. 执行`terraform apply`创建站点加速配置。
   执行 apply 命令后 Terraform 会让您再次确认将要执行的动作。在确认无误后输入`yes`二次确认，然后等待命令执行完成。
```
PS tf-doc> terraform.exe apply                                     
tencentcloud_teo_zone.example: Refreshing state... [id=zone-2ag9gej58j36]
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
Terraform will perform the following actions:
  # tencentcloud_teo_zone_setting.example will be created
  + resource "tencentcloud_teo_zone_setting" "example" {
      + area    = (known after apply)
      + id      = (known after apply)
      + zone_id = "zone-2ag9gej58j36"
      + cache {
          + cache {
              + cache_time           = (known after apply)
              + ignore_cache_control = (known after apply)
              + switch               = (known after apply)
            }
          + follow_origin {
              + switch = "on"
            }
          + no_cache {
              + switch = (known after apply)
            }
        }
      + cache_key {
          + full_url_cache = "off"
          + ignore_case    = "on"
          + query_string {
              + action = "includeCustom"
              + switch = "on"
              + value  = [
                  + "param0",
                  + "param1",
                ]
            }
        }
      + cache_prefresh {
          + percent = (known after apply)
          + switch  = (known after apply)
        }
      + client_ip_header {
          + header_name = "EO-Client-IPCountry"
          + switch      = "on"
        }
      + compression {
          + algorithms = [
              + "brotli",
              + "gzip",
            ]
          + switch     = "on"
        }
      + force_redirect {
          + redirect_status_code = (known after apply)
          + switch               = (known after apply)
        }
      + https {
          + ocsp_stapling = "on"
          + tls_version   = [
              + "TLSv1.2",
              + "TLSv1.3",
            ]
        }
      + ipv6 {
          + switch = (known after apply)
        }
      + max_age {
          + follow_origin = (known after apply)
          + max_age_time  = (known after apply)
        }
      + offline_cache {
          + switch = (known after apply)
        }
      + origin {
          + backup_origins       = (known after apply)
          + cos_private_access   = (known after apply)
          + origin_pull_protocol = (known after apply)
          + origins              = (known after apply)
        }
      + post_max_size {
          + max_size = (known after apply)
          + switch   = (known after apply)
        }
      + quic {
          + switch = (known after apply)
        }
      + smart_routing {
          + switch = (known after apply)
        }
      + upstream_http2 {
          + switch = (known after apply)
        }
      + web_socket {
          + switch  = (known after apply)
          + timeout = (known after apply)
        }
    }
Plan: 1 to add, 0 to change, 0 to destroy.
Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.
  Enter a value: yes
tencentcloud_teo_zone_setting.example: Creating...
tencentcloud_teo_zone_setting.example: Creation complete after 1s [id=zone-2ag9gej58j36]
Apply complete! Resources: 1 added, 0 changed, 0 destroyed.
```

4. 检查命令执行结果。
   您可以通过`terraform show`命令检查站点加速配置是否生效，也可以登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone) 来确认。
```
PS tf-doc> terraform state show tencentcloud_teo_zone_setting.example
# tencentcloud_teo_zone_setting.example:
resource "tencentcloud_teo_zone_setting" "example" {
    area    = "overseas"
    id      = "zone-2ag9gej58j36"
    zone_id = "zone-2ag9gej58j36"
    cache {
        follow_origin {
            switch = "on"
        }
        no_cache {
            switch = "off"
        }
    }
    cache_key {
        full_url_cache = "off"
        ignore_case    = "on"
        query_string {
            action = "includeCustom"
            switch = "on"
            value  = [
                "param0",
                "param1",
            ]
        }
    }
    cache_prefresh {
        percent = 90
        switch  = "off"
    }
    client_ip_header {
        header_name = "EO-Client-IPCountry"
        switch      = "on"
    }
    compression {
        algorithms = [
            "brotli",
            "gzip",
        ]
        switch     = "on"
    }
    force_redirect {
        redirect_status_code = 302
        switch               = "off"
    }
    https {
        http2         = "on"
        ocsp_stapling = "on"
        tls_version   = [
            "TLSv1.2",
            "TLSv1.3",
        ]
        hsts {
            include_sub_domains = "off"
            max_age             = 0
            preload             = "off"
            switch              = "off"
        }
    }
    ipv6 {
        switch = "off"
    }
    max_age {
        follow_origin = "on"
        max_age_time  = 600
    }
    offline_cache {
        switch = "on"
    }
    origin {
        backup_origins       = []
        origin_pull_protocol = "follow"
        origins              = []
    }
    post_max_size {
        max_size = 524288000
        switch   = "on"
    }
    quic {
        switch = "off"
    }
    smart_routing {
        switch = "off"
    }
    upstream_http2 {
        switch = "off"
    }
    web_socket {
        switch  = "off"
        timeout = 30
    }
}
