## 概述

**Parallel 节点**，也称**并行节点**，可以在工作流中创建并行的任务分支，让多个任务并行执行，提高工作流效率。

## 参数

除了 [常用字段](https://cloud.tencent.com/document/product/1272/51544) 外，Parallel 节点还支持以下字段：

| 字段                    | 描述                                                         |
| ----------------------- | ------------------------------------------------------------ |
| Branches（必选）        | Branches 对应的数据为一个数组。数组中的每个元素代表一个工作流的定义。每个分支都必须含有 **States** 和 **StartAt**字段。 |
| Parameters（可选）      | 指定作为输入传递的键值对集合。更多详情参考 [输入参数](https://cloud.tencent.com/document/product/1272/55657#Parameters)。    |
| ResultSeclector（可选） | 指定作为输出数据的键值对集合，并传递给 ResultPath。更多详情参考 [结果选择器](https://cloud.tencent.com/document/product/1272/55657#ResultSelector)。 |
| ResultPath（可选）      | 指定输出结果的存储位置，插入到输入数据的指定地址中。更多详情参考 [结果路径](https://cloud.tencent.com/document/product/1272/55657#ResultPath)。 |
| Retry（可选）           | 一个称为重试器的对象的数组，定义遇到运行时错误时的重试策略。更多详情参考 [重试策略](https://cloud.tencent.com/document/product/1272/55663#Retry)。 |
| Catch（可选）           | 一个称为捕获器的对象的数组，用于定义错误。如果节点遇到运行错误并且其重试策略已耗尽或者未定义，则执行该节点。更多详情参考 [异常捕获](https://cloud.tencent.com/document/product/1272/55663#Catch)。 |

## 示例

以下为 Parallel 结构的实例代码：

```
{
  "Comment": "",
  "StartAt": "Parallel_1",
  "States": {
    "Parallel_1": {
      "Type": "Parallel",
      "Comment": "并行",
      "End": true,
      "Branches": [
        {
          "StartAt": "Pass_1",
          "States": {
            "Pass_1": {
              "Type": "Pass",
              "Comment": "传递",
              "Next": "checkMpsJob_1"
            },
            "checkMpsJob_1": {
              "Type": "Task",
              "Resource": "qrn:qcs:asw:ap-guangzhou:123456789:sdk:json:qcloud:mps:checkMpsJob",
              "End": true
            }
          }
        },
        {
          "StartAt": "Invoke_1",
          "States": {
            "Invoke_1": {
              "Type": "Task",
              "Comment": "invoke scf component",
              "Resource": "qrn:qcs:asw:ap-guangzhou:123456789:sdk:json:qcloud:scf:Invoke/scfDemo",
              "End": true
            }
          }
        }
      ]
    }
  }
}

```

在此实例中，Parallel 进入了两个分支。第一个分支有 “Pass_1” 和 “checkMpsJob_1” 两个节点，第二个分支有 “Invoke_1” 一个节点。节点的定义符合各自类型节点的定义方式。

