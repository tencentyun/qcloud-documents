## 功能简介
腾讯云边缘安全加速平台（TencentCloud EdgeOne，下文简称为 EdgeOne）已经接入 Terraform，可以通过 Terraform 来实现快速配置。本文介绍如何使用 Terraform 来配置 EdgeOne 站点的规则引擎，实现子域名差异化配置。

## 前置条件
1. 已完成 Terraform 的安装与配置，操作步骤请参见 [安装和配置 Terraform](https://cloud.tencent.com/document/product/1552/80472)。
2. 已通过 Terraform 接入了站点，操作步骤请参见 [通过 Terraform 创建站点](https://cloud.tencent.com/document/product/1552/82136)。

## 操作步骤
1. 修改 Terraform 配置文件，添加子域名 DNS 记录和规则引擎的资源定义。
   您可以在 Terraform Provider 文档页面上查看 [DNS 记录](https://registry.terraform.io/providers/tencentcloudstack/tencentcloud/latest/docs/resources/teo_dns_record) 和 [规则引擎](https://registry.terraform.io/providers/tencentcloudstack/tencentcloud/latest/docs/resources/teo_rule_engine) 的参数定义。以下为示例配置文件 tencent_teo.tf 的内容：
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
# 子域名 DNS 记录
resource "tencentcloud_teo_dns_record" "rule_record" {
  zone_id = tencentcloud_teo_zone.example.id
  type    = "A"
  name    = "rule.example.com"
  content = "<your-backend-ip>"
  mode    = "proxied"
  ttl     = 300
}
# 子域名差异化配置
resource "tencentcloud_teo_rule_engine" "rule_example" {
  zone_id   = tencentcloud_teo_zone.example.id
  rule_name = "example_rule"
  status    = "enable" # 启用该规则
  rules {
    # 针对 rule.example.com 且文件后缀为 mp3、mp4 的请求
    or {
      and {
        target   = "host"
        operator = "equal"
        values   = [tencentcloud_teo_dns_record.rule_record.name]
      }
      and {
        target   = "extension"
        operator = "equal"
        values   = ["mp4", "mp3"]
      }
    }
    actions {
      # 使用指定 CacheKey
      normal_action {
        action = "CacheKey"
        # CacheKey是大小写敏感的
        parameters {
          name   = "Type"
          values = ["IgnoreCase"]
        }
        parameters {
          name   = "Switch"
          values = ["off"]
        }
        # CacheKey 包含 User-Agent 头
        parameters {
          name   = "Type"
          Values = ["Header"]
        }
        parameters {
          name   = "Switch"
          values = ["on"]
        }
        parameters {
          name   = "Value"
          values = "User-Agent"
        }
      }
    }
    # 增加指定响应头
    actions {
      rewrite_action {
        action = "ResponseHeader"
        parameters {
          action = "add"
          name   = "Added-Header"
          values = ["Added-Value"]
        }
      }
    }
  }
}
```

2. 执行`terraform plan`命令预览配置，可以校验配置是否正确。
```
PS tf-doc> terraform plan
tencentcloud_teo_zone.example: Refreshing state... [id=zone-2ag9gej58j36]
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
Terraform will perform the following actions:
  # tencentcloud_teo_dns_record.rule_record will be created
  + resource "tencentcloud_teo_dns_record" "rule_record" {
      + cname         = (known after apply)
      + content       = "<your-backend-ip>"
      + created_on    = (known after apply)
      + dns_record_id = (known after apply)
      + domain_status = (known after apply)
      + id            = (known after apply)
      + locked        = (known after apply)
      + mode          = "proxied"
      + modified_on   = (known after apply)
      + name          = "rule.example.com"
      + priority      = (known after apply)
      + status        = (known after apply)
      + ttl           = 300
      + type          = "A"
      + zone_id       = "zone-2ag9gej58j36"
    }
  # tencentcloud_teo_rule_engine.rule_example will be created
  + resource "tencentcloud_teo_rule_engine" "rule_example" {
      + id        = (known after apply)
      + rule_id   = (known after apply)
      + rule_name = "example_rule"
      + status    = "enable"
      + zone_id   = "zone-2ag9gej58j36"
      + rules {
          + actions {
              + normal_action {
                  + action = "CacheKey"
                  + parameters {
                      + name   = "Type"
                      + values = [
                          + "IgnoreCase",
                        ]
                    }
                  + parameters {
                      + name   = "Switch"
                      + values = [
                          + "off",
                        ]
                    }
                  + parameters {
                      + name   = "Type"
                      + values = [
                          + "Header",
                        ]
                    }
                  + parameters {
                      + name   = "Switch"
                      + values = [
                          + "on",
                        ]
                    }
                  + parameters {
                      + name   = "Value"
                      + values = [
                          + "User-Agent",
                        ]
                    }
                }
            }
          + actions {
              + rewrite_action {
                  + action = "ResponseHeader"
                  + parameters {
                      + action = "add"
                      + name   = "Added-Header"
                      + values = [
                          + "Added-Value",
                        ]
                    }
                }
            }
          + or {
              + and {
                  + operator = "equal"
                  + target   = "host"
                  + values   = [
                      + "rule.example.com",
                    ]
                }
              + and {
                  + operator = "equal"
                  + target   = "extension"
                  + values   = [
                      + "mp3",
                      + "mp4",
                    ]
                }
            }
        }
    }
Plan: 2 to add, 0 to change, 0 to destroy.
─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────── 
Note: You didn't use the -out option to save this plan, so Terraform can't guarantee to take exactly these actions if you run "terraform apply" now.
```

3. 执行`terraform apply`创建子域名 DNS 记录和规则引擎。
   执行 apply 命令后 Terraform 会让您再次确认将要执行的动作。在确认无误后输入`yes`二次确认，然后等待命令执行完成。
```
PS tf-doc> terraform apply
tencentcloud_teo_zone.example: Refreshing state... [id=zone-2ag9gej58j36]
Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create
Terraform will perform the following actions:
  # tencentcloud_teo_dns_record.rule_record will be created
  + resource "tencentcloud_teo_dns_record" "rule_record" {
      + cname         = (known after apply)
      + content       = "<your-backend-ip>"
      + created_on    = (known after apply)
      + dns_record_id = (known after apply)
      + domain_status = (known after apply)
      + id            = (known after apply)
      + locked        = (known after apply)
      + mode          = "proxied"
      + modified_on   = (known after apply)
      + name          = "rule.example.com"
      + priority      = (known after apply)
      + status        = (known after apply)
      + ttl           = 300
      + type          = "A"
      + zone_id       = "zone-2ag9gej58j36"
    }
  # tencentcloud_teo_rule_engine.rule_example will be created
  + resource "tencentcloud_teo_rule_engine" "rule_example" {
      + id        = (known after apply)
      + rule_id   = (known after apply)
      + rule_name = "example_rule"
      + status    = "enable"
      + zone_id   = "zone-2ag9gej58j36"
      + rules {
          + actions {
              + normal_action {
                  + action = "CacheKey"
                  + parameters {
                      + name   = "Type"
                      + values = [
                          + "IgnoreCase",
                        ]
                    }
                  + parameters {
                      + name   = "Switch"
                      + values = [
                          + "off",
                        ]
                    }
                  + parameters {
                      + name   = "Type"
                      + values = [
                          + "Header",
                        ]
                    }
                  + parameters {
                      + name   = "Switch"
                      + values = [
                          + "on",
                        ]
                    }
                  + parameters {
                      + name   = "Value"
                      + values = [
                          + "User-Agent",
                        ]
                    }
                }
            }
          + actions {
              + rewrite_action {
                  + action = "ResponseHeader"
                  + parameters {
                      + action = "add"
                      + name   = "Added-Header"
                      + values = [
                          + "Added-Value",
                        ]
                    }
                }
            }
          + or {
              + and {
                  + operator = "equal"
                  + target   = "host"
                  + values   = [
                      + "rule.example.com",
                    ]
                }
              + and {
                  + operator = "equal"
                  + target   = "extension"
                  + values   = [
                      + "mp3",
                      + "mp4",
                    ]
                }
            }
        }
    }
Plan: 2 to add, 0 to change, 0 to destroy.
Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.
  Enter a value: yes
tencentcloud_teo_dns_record.rule_record: Creating...
tencentcloud_teo_dns_record.rule_record: Creation complete after 2s [id=zone-2ag9gej58j36#record-2ahmb3w7ssl8]
tencentcloud_teo_rule_engine.rule_example: Creating...
tencentcloud_teo_rule_engine.rule_example: Creation complete after 1s [id=zone-2ag9gej58j36#rule-2ahmb5dhn9qq]
Apply complete! Resources: 2 added, 0 changed, 0 destroyed.
```

4. 检查命令执行结果。
   您可以通过`terraform show`命令检查站点加速配置是否生效，也可以登录 [边缘安全加速平台控制台](https://console.cloud.tencent.com/edgeone) 来确认。
```
PS tf-doc> terraform state show tencentcloud_teo_dns_record.rule_record
# tencentcloud_teo_dns_record.rule_record:
resource "tencentcloud_teo_dns_record" "rule_record" {
    content       = "<your-backend-ip>"
    created_on    = "2022-10-20T06:31:38Z"
    dns_record_id = "record-2ahmb3w7ssl8"
    domain_status = [
        "security",
    ]
    id            = "zone-2ag9gej58j36#record-2ahmb3w7ssl8"
    locked        = false
    mode          = "proxied"
    modified_on   = "2022-10-20T06:31:38Z"
    name          = "rule.example.com"
    priority      = 0
    status        = "active"
    ttl           = 300
    type          = "A"
    zone_id       = "zone-2ag9gej58j36"
}
PS tf-doc> terraform state show tencentcloud_teo_rule_engine.rule_example
# tencentcloud_teo_rule_engine.rule_example:
resource "tencentcloud_teo_rule_engine" "rule_example" {
    id        = "zone-2ag9gej58j36#rule-2ahmb5dhn9qq"
    rule_id   = "rule-2ahmb5dhn9qq"
    rule_name = "example_rule"
    status    = "enable"
    zone_id   = "zone-2ag9gej58j36"
    rules {
        actions {
            normal_action {
                action = "CacheKey"
                parameters {
                    name   = "Type"
                    values = [
                        "IgnoreCase",
                    ]
                }
                parameters {
                    name   = "Switch"
                    values = [
                        "off",
                    ]
                }
                parameters {
                    name   = "Type"
                    values = [
                        "Header",
                    ]
                }
                parameters {
                    name   = "Switch"
                    values = [
                        "on",
                    ]
                }
                parameters {
                    name   = "Value"
                    values = [
                        "User-Agent",
                    ]
                }
            }
        }
        actions {
            rewrite_action {
                action = "ResponseHeader"
                parameters {
                    action = "add"
                    name   = "Added-Header"
                    values = [
                        "Added-Value",
                    ]
                }
            }
        }
        or {
            and {
                operator = "equal"
                target   = "host"
                values   = [
                    "rule.example.com",
                ]
            }
            and {
                operator = "equal"
                target   = "extension"
                values   = [
                    "mp3",
                    "mp4",
                ]
            }
        }
    }
}
```
