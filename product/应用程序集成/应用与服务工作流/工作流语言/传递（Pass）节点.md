## 概述

**Pass 节点**，也称**传递节点**，实现从输入到输出的传递，不执行其他工作。 Pass 节点在构造和调试工作流时非常有用。

## 参数

除了 [常见字段](https://cloud.tencent.com/document/product/1272/51544#step3) 之外，Pass 节点还包含以下字段：

| 字段                   | 描述                                                         |
| ---------------------- | ------------------------------------------------------------ |
| Result（可选）         | 当前节点的输出数据，并传递到下一个节点。如果存在 ResultPath 字段，则按照 ResultPath 的内容进行筛选后输出。 |
| ResultPath（可选）     | 指定输出数据在输入数据的存储位置。然后将输出数据插入到输入数据中，并将合并后的数据作为最后输出数据。 如果存在 OutputPath 字段，将再次对内容进行筛选后输出。 更多关于结果路径的信息参见 [输入与输出](https://cloud.tencent.com/document/product/1272/55657) 。 |
| Parameters（可选）     | 指定作为输入传递的键值对集合。有关更多信息，请参阅 [输入与输出](https://cloud.tencent.com/document/product/1272/55657)。 |
| ResultSelector（可选） | 指定作为输出数据的键值对集合，并传递给ResultPath。有关更多信息，请参阅 [输入与输出](https://cloud.tencent.com/document/product/1272/55657)。 |

## 示例

以一个 Hello 节点作为工作流示例，如下：

```
{
  "Hello": {
    "Type": "Pass",
    "Comment": "传递",
    "Result": {
      "apple": "4",
      "banana": "8"
    },
    "ResultPath": "$.count",
    "Next": "World"
  }
}
```

假设输入数据为：

```
{
  "name": "Lucy"
}
```

由于该节点为 Pass 节点，因此不执行其他工作，直接输出。输出的数据经过 Result 与 ResultPath 选择后，插入到输入数据的 count 节点中，最终的输出数据为：

```
{
  "name": "Lucy",
  "count": {
    "apple": "4",
    "banana": "8"
  }
}
```

