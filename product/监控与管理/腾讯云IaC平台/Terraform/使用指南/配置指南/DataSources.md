数据源 Data Sources 允许在 Terraform 外部定义，由另一个单独的 Terraform 配置定义或由函数修改的信息。

## 使用 Data Sources
Data Sources 通过一种特殊类型的资源进行访问，该资源使用 `data` 块声明。如下所示：
```bash
data "tencentcloud_availability_zones" "my_favourite_zone" {
  name = "ap-guangzhou-3"
}
```

## 引用 Data Sources

引用 Data Sources 数据的语法是 `data.<TYPE>.<NAME>.<ATTRIBUTE>`。如下所示：
```bash
resource "tencentcloud_subnet" "app" {
  ...
  availability_zone = data.tencentcloud_availability_zones.default.zones.0.name
  ...
}
```
