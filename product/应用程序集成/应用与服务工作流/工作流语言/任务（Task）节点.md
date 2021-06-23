## 概述

**Task 节点**，也称**任务节点**，代表工作流执行的一个基本单元。Task 节点通过将参数传递指定服务的 API 来执行指定服务，工作流中的所有工作将由 Task 节点完成。**Task 节点支持 [全量云 API](https://cloud.tencent.com/api/list) 的服务集成**。

## 参数

除了 [常见字段](https://cloud.tencent.com/document/product/1272/51544#step3) 之外，Task 节点还包含以下字段：

| 字段                    | 描述                                                         |
| ----------------------- | ------------------------------------------------------------ |
| Resource（必选）        | 定义节点执行的任务资源。目前支持腾讯云 API 所有服务。详情参考资源定义。 |
| Parameters（可选）      | 指定作为输入传递的键值对集合。更多详情参考 [输入参数](https://cloud.tencent.com/document/product/1272/55657#Parameters)。    |
| ResultSeclector（可选） | 指定作为输出数据的键值对集合，并传递给 ResultPath。更多详情参考 [结果选择器](https://cloud.tencent.com/document/product/1272/55657#ResultSelector)。 |
| ResultPath（可选）      | 指定输出结果的存储位置，插入到输入数据的指定地址中。更多详情参考 [结果路径](https://cloud.tencent.com/document/product/1272/55657#ResultPath)。 |
| Retry（可选）           | 一个称为重试器的对象的数组，定义遇到运行时错误时的重试策略。更多详情参考 [重试策略](https://cloud.tencent.com/document/product/1272/55663#Retry)。 |
| Catch（可选）           | 一个称为捕获器的对象的数组，用于定义错误。如果节点遇到运行错误并且其重试策略已耗尽或者未定义，则执行该节点。更多详情参考 [异常捕获](https://cloud.tencent.com/document/product/1272/55663#Catch)。 |

## 服务调用

ASW 通过 Task 节点调用云 API 来支持 [全量云 API](https://cloud.tencent.com/api/list) 的服务集成，因此 Task 节点支持腾讯云 API 包含的所有服务。通过 Resource 与 Parameters 来映射云 API 调用所需要的参数字段。规则如下：

1. Resource 定义了要调用的服务接口：
```
qrn:qcs:asw:{服务所在区域}:{Appid}:sdk:json:qcloud:{服务名称}:{服务接口}
```
2. Parameters 定义的是服务接口对应的参数名称。
3. 云函数服务调用 **Invoke**，仅仅支持以下定义：
```
qrn:qcs:asw:{函数所在区域}:{Appid}:sdk:json:qcloud:scf:Invoke/{函数名称}/{函数版本|别名}/{函数命名空间}
```

> ? 函数 [版本](https://cloud.tencent.com/document/product/583/43760)|[别名](https://cloud.tencent.com/document/product/583/36149) 与 [命名空间](https://cloud.tencent.com/document/product/583/35913) 使用默认值时，可以省略成 `qrn:qcs:asw:{函数所在区域}:{Appid}:sdk:json:qcloud:scf:Invoke/{函数名称}` 格式。

### 示例1：调用云函数

以下代码定义了 Sum 节点，Sum 节点中调用了 sum 函数。由于版本别名和命名空间均为默认值，省略不写如下：

```
{
  "Comment": "",
  "StartAt": "sum",
  "States": {
    "Sum": {
      "Type": "Task",
      "Comment": "调用求和函数",
      "Resource": "qrn:qcs:asw:ap-guangzhou:123456789:sdk:json:qcloud:scf:Invoke/sum",
      "End": true
    }
  }
}
```

### 示例2：调用 MPS 任务

以下代码定义了 Mps 节点，Mps 节点中调用了 [**ProcessMedia 接口**](https://cloud.tencent.com/document/product/862/37578)。Parameters 定义了 ProcessMedia 接口需要的参数。如下：

```
{
  "Comment": "",
  "StartAt": "ProcessMedia_1",
  "States": {
    "ProcessMedia_1": {
      "Type": "Task",
      "Resource": "qrn:qcs:asw:ap-guangzhou:123456789:sdk:json:qcloud:mps:ProcessMedia",
      "Parameters": {
        "InputInfo": {
          "Type": "COS",
          "CosInputInfo": {
            "Bucket": "susu-test-123456789",
            "Region": "ap-shanghai",
            "Object": "/video/inputs/05.m2ts"
          }
        },
        "OutputDir": "/video/outputs/",
        "MediaProcessTask": {
          "TranscodeTaskSet": [
            {
              "Definition": 100030
            },
            {
              "Definition": 100040
            }
          ]
        }
      },
      "End": true
    }
  }
}
```

## 服务集成

当使用 Task 节点调用云服务时，您可以选择以下服务集成模式：

- **请求响应模式**：调用服务，ASW 获得HTTP响应后立即进入下一个节点。对于异步服务，ASW 不会等待作业执行完成。默认模式是请求响应模式。
- **同步运行模式**：调用服务，ASW 等待作业完成后才会进入下一个节点。通常这类服务提供了异步执行接口，ASW 调用异步接口成功后会等待，直到相关任务完成并获得了执行结果，才会继续执行下一个节点。

支持的服务集成和服务集成模式：

**标准工作流**

| 服务                                                         | 请求响应 | 同步运行 |
| :----------------------------------------------------------- | :------- | :------- |
| [云函数](https://cloud.tencent.com/product/scf)              | 支持     | 支持     |
| [应用与服务编排工作流](https://cloud.tencent.com/product/asw) | 支持     | 支持     |
| [其他云产品](https://cloud.tencent.com/api/list)             | 支持     | 不支持   |

**快速工作流**

| 服务                                                         | 请求响应 | 同步运行 |
| :----------------------------------------------------------- | :------- | :------- |
| [云函数](https://cloud.tencent.com/product/scf)              | 支持     | 不支持   |
| [应用与服务编排工作流](https://cloud.tencent.com/product/asw) | 支持     | 不支持   |
| [其他云产品](https://cloud.tencent.com/api/list)             | 支持     |  不支持         |


