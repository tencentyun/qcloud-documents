## 操作场景

您可参考本文提供的案例，对数据加工有个总体、感性的认识，同时，也可以复制这些案例中的函数，完成自己的数据加工。

## 注意事项

- v 函数的使用：**v("字段A")**，意思是 value of “字段A”，即字段 A 的值。有些函数的参数是**字段**，有些函数的参数是**字段值**，常见错误是：函数参数为字段值，却没有使用**v函数**取字段值，导致函数执行失败。     
- 分发到多个日志主题，需要提前配好**目标日志主题**及其**目标名称**，目标名称用于**分发函数**。   
- fields_set 函数的使用：通过 fields_set 函数设置字段值，保存数据加工函数处理后的内容。例如 fields_set("A+B",op_add(v("字段A"）,v("字段B")))，意思是将字段 A 的值和字段 B 的值相加，op_add 函数需要借助 fields_set 函数来完成结果的写入和保存。

## 操作场景

您可参考以下案例，完成自己的数据加工。
- [日志过滤和分发](https://cloud.tencent.com/document/product/614/71487)
- [单行文本日志结构化](https://cloud.tencent.com/document/product/614/71488)
- [数据脱敏](https://cloud.tencent.com/document/product/614/71489)
- [嵌套 JSON 的处理](https://cloud.tencent.com/document/product/614/71490)
- [多格式的日志结构化](https://cloud.tencent.com/document/product/614/71491)
- [利用分割符提取日志指定内容](https://cloud.tencent.com/document/product/614/71492)
