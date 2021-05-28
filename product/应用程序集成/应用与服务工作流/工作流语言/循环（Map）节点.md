## 概述

**Map 节点**，也称**循环节点**，可以对数组中的每一个元素进行一系列的计算。Map 节点的主要逻辑是对不同的元素进行一系列相同的计算，而 Parallel 节点的逻辑是对于同一个输入进行不同的分支计算。

## 参数

除了 [常用字段](https://cloud.tencent.com/document/product/1272/51544#step3)，Map 节点还支持以下字段:

| 字段                    | 描述                                                         |
| ----------------------- | ------------------------------------------------------------ |
| Iterator（必选）        | Iterator 字段定义对数组的操作。**StartAt** 字段定义第一个循环的节点，**States** 字段每一个数组中的元素可能进入的状态。 |
| ItemsPath （可选）      | 指定 map 节点的循环路径，默认值为$，指定整个输入。            |
| MaxConcurrency （可选） | 最大并发量，控制状态机对数组进行循环时，同时计算的元素数量的最大值，默认值为1。 |
| Parameters（可选）      | 指定作为输入传递的键值对集合。更多详情参考 [输入参数](https://cloud.tencent.com/document/product/1272/55657#Parameters)。    |
| ResultSeclector（可选） | 指定作为输出数据的键值对集合，并传递给 ResultPath。更多详情参考 [结果选择器](https://cloud.tencent.com/document/product/1272/55657#ResultSelector)。 |
| ResultPath（可选）      | 指定输出结果的存储位置，插入到输入数据的指定地址中。更多详情参考 [结果路径](https://cloud.tencent.com/document/product/1272/55657#ResultPath)。 |
| Retry（可选）           | 一个称为重试器的对象的数组，定义遇到运行时错误时的重试策略。更多详情参考 [重试策略](https://cloud.tencent.com/document/product/1272/55663#Retry)。 |
| Catch（可选）           | 一个称为捕获器的对象的数组，用于定义错误。如果节点遇到运行错误并且其重试策略已耗尽或者未定义，则执行该节点。更多详情参考 [异常捕获](https://cloud.tencent.com/document/product/1272/55663#Catch)。 |

## 示例

### 示例1：数组循环计算

在示例中，我们将对 "exam" 键值对应的数组进行循环计算。数组中的每个元素为 JSON 格式。

> !本案例将被循环的元素传送至 Task 节点，Task 节点中所导入的云函数格式必须为 JSON。

```
{
  "Comment": "Map demo",
  "StartAt": "entry",
  "TimeoutSeconds": 10000000,
  "States": {
    "entry": {
      "Type": "Pass",
      "Comment": "初始化",
      "Next": "MapCaculate"
    },
    "MapCaculate": {
      "Type": "Map",
      "InputPath": "$.detail",
      "ItemsPath": "$.exam",
      "ResultPath": "$.detail.exam",
      "MaxConcurrency": 2,
      "Iterator": {
        "StartAt": "Average",
        "States": {
          "Average": {
            "Type": "Task",
            "ResultSelector": {
              "user.$": "$.user",
              "score.$": "$.average"
            },
            "Resource": "qrn:qcs:asw:ap-guangzhou:123456789:sdk:json:qcloud:scf:Invoke/average",
            "End": true
          }
        }
      },
      "End": true
    }
  }
}
```

指定一组输入：
```
{
  "date": "2021-03-14T01:59:00Z",
  "detail": {
    "class": "No-01",
    "exam": [
      { "user": "susu", "score": [90,80,70,60]},
      { "user": "lucy", "score": [80,85,90,95]},
      { "user": "dora", "score": [60,78,93,76]},
      { "user": "jiao", "score": [89,87,79,95]}
    ]
  }
}
```

在 average 函数中，我们对 score 进行求均值后输出：
```
'use strict';
   exports.main_handler = async (event, context) => {
    var sum = 0;
    var score = event["score"];
    for(var i=0; i< score.length; i++){
        sum = sum + score[i];
    }
    return {
        "user": event["user"],
        "average": Math.round(sum/i)
    }
};
```

最终输出信息通过 ResultPath 作用后，如下：
```
{
  "date": "2021-03-14T01:59:00Z",
  "detail": {
    "class": "No-01",
    "exam": [
        {"score":75,"user":"susu"},
        {"score":88,"user":"lucy"},
        {"score":77,"user":"dora"},
        {"score":88,"user":"jiao"}
      ]
   }
}
```

### 示例2：带参数的传递

在上述示例中，如果想要在每次迭代中传递除了迭代数组外的参数，可以通过 Parameters 来定义。
```
{
  "Comment": "Map demo",
  "StartAt": "entry",
  "TimeoutSeconds": 10000000,
  "States": {
    "entry": {
      "Type": "Pass",
      "Comment": "初始化",
      "Next": "MapCaculate"
    },
    "MapCaculate": {
      "Type": "Map",
      "InputPath": "$.detail",
      "ItemsPath": "$.exam",
      "Parameters": {
        "class.$": "$.class",
        "exam.$": "$$.Map.Item.Value"
      },
      "ResultPath": "$.detail.exam",
      "MaxConcurrency": 2,
      "Iterator": {
        "StartAt": "Average",
        "States": {
          "Average": {
            "Type": "Task",
            "ResultSelector": {
              "user.$": "$.user",
              "score.$": "$.average"
            },
            "Resource": "qrn:qcs:asw:ap-guangzhou:123456789:sdk:json:qcloud:scf:Invoke/average",
            "End": true
          }
        }
      },
      "End": true
    }
  }
}
```

这样我们传递给第一次循环的 Task 节点的输入则变为：
```
{
  "class": "No-01",
  "exam": {
    "user": "susu",
    "score": [90, 80, 70, 60]
  }
}
```
