
Terraform 语言具备惯用的样式约定，建议用户始终遵循约定，以确保不同团队编写的文件和模块之间的一致性。同时自动格式化工具也需应用约定，可以使用 `terraform fmt` 进行格式化。

## 代码约束
- 每个嵌套级别缩进两个空格。
- 当具有单行值的多个参数出现在同一嵌套级别的连续行上时，需对齐等号。例如：
```
  ami           = "abc123"
  instance_type = "t2.micro"
```
- 当参数和块同时出现在块体中时，需将所有参数一起放在顶部，使用一个空行将其与块分开，在空行下面放置嵌套块。
- 参数与内嵌块之间需空一行分隔。
- 对于同时包含参数和 `"meta-arguments"`（由 Terraform 语言语义定义）的块，需列出所有元参数，并放置在其他参数与块之间，上下分别使用空行分开。例如：
```
resource "tencentclould_instance" "example" {
  count = 2 # meta-argument first

  ami           = "abc123"
  instance_type = "t2.micro"

  network_interface {
    # ...
  }

  lifecycle { # meta-argument block last
    create_before_destroy = true
  }
}

```
- 顶级块应始终由一个空行彼此分隔。嵌套块也需使用空行分隔，除非将相同类型的相关块组合在一起（如资源中的多个供应器块）。
- 避免将多个相同类型的块与其他不同类型的块分开，除非这些块类型是由语义定义的以形成一个族。
