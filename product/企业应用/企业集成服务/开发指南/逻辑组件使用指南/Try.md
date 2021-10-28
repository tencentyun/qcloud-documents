

## 简介

Try 组件的作用是捕获错误，可以捕获 Try 中子流运行时抛出的错误和系统错误，也可与 Raise Error 组件搭配使用，捕获用户自定义错误，Raise Error 组件抛出错误后，Try 使用 Catch 捕获，并执行 Catch 中配置的子流。当 Catch 中配置的错误类型为"any"时，可以捕获所有错误。

## 操作配置

### 参数配置

| 参数     | 数据类型 | 描述                                                  | 是否必填 | 默认值 |
| :------- | :------- | :---------------------------------------------------- | :------- | ------ |
| 错误类型 | string   | 流执行过程中抛出的错误类型，配置"any"，可捕获所有错误。 | 是       | 无     |

### 界面配置
当 Try 中配置的子流抛出错误后，Catch 可根据配置的错误类型进行捕获，当 Catch 中配置的错误类型与 Raise Error 抛出的错误类型一致时，执行 Catch 中的补偿策略。
![image-20210325171939391](https://main.qcloudimg.com/raw/cd27e7606d8bc4128a75c606909e2153/image-20210325171939391.png)
![image-20210325171954027](https://main.qcloudimg.com/raw/4aafc76d0f160bda633a24cb44b20134/image-20210325171954027.png)

### 输入到子流中的 message 

| message 属性 | 值                               |
| ----------- | -------------------------------- |
| payload     | 继承 Try 上一个组件的 payload。       |
| error       | 空。                               |
| attribute   | 继承 Try 上一个组件的 attribute 信息。 |
| variable    | 继承 Try 上一个组件的 variable 信息。  |

### 输出

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 若 Try 中子流正常运行，payload 的结果为子流输出的 payload。若抛出错误，且错误被 Cache 捕获，则 payload 的结果为 Cache 中子流输出的 payload。若抛出的错误未被捕获，则流终止运行。 |
| error       | 若抛出错误，error 保存错误信息，为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息。 |
| attribute   | 若 Try 中子流正常运行，attribute 的结果为子流输出的 attribute。若抛出错误，且错误被 Cache 捕获，则 attribute 的结果为 Cache 中子流输出的 attribute。若抛出的错误未被捕获，则流终止运行。 |
| variable    | 若 Try 中子流正常运行，variable 的结果为子流输出的 variable。若抛出错误，且错误被 Cache 捕获，则 variable 的结果为 Cache 中子流输出的 variable。若抛出的错误未被捕获，则流终止运行。 |

## 案例
1. 当查询错误或返回值不满足条件时，抛出错误。
   ![image-20210406115602446](https://main.qcloudimg.com/raw/88e7d3834d0d3078946f177561523ad2/image-20210406115602446.png)
   ![image-20210406115633563](https://main.qcloudimg.com/raw/00bde90f83b8b3967ff089b2f3ec2d22/image-20210406115633563.png)
2. 使用 Try Cache 捕获错误。
   ![image-20210406115759576](https://main.qcloudimg.com/raw/26c58fd377be5ea4364282e0e918498d/image-20210406115759576.png)
