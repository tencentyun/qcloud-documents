资源是 Terraform 最重要的组成部分。资源通过 resource 块来定义，一个 resource 可以定义一个或多个基础设施资源对象。例如，私有网络 VPC、虚拟机等。

## 资源语法
资源通过 resource 块定义，一个 `resource` 块包含 `resource` 关键字、资源类型、资源名和资源块体三部分。如下所示：
```
    resource "tencentcloud_vpc" "foo" {
        name         = "ci-temp-test-updated"
        cidr_block   = "10.0.0.0/16"
        dns_servers  = ["119.29.29.29", "8.8.8.8"]
        is_multicast = false

        tags = {
            "test" = "test"
        }
    }
```

## 资源引用
通过该语法格式 `<资源类型>.<名称>.<属性>` 引用资源属性。如下所示：
```
tencentcloud_vpc.foo.resource # ci-temp-test-updated
```
