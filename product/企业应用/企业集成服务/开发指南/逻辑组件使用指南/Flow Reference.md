

## 简介

Flow Reference 组件用来引用当前应用中的其他集成流。与 Async 不同，Flow Reference 是一个同步动作，当引用的集成流执行完成后，才会继续执行下一个动作，并且 Flow Reference 中的子流执行完成后，message 会传递到主流中，下一个节点基于该子流的 message 继续执行。当 Flow Reference 引用的子流包含 trigger 节点时，如果该子流的执行由 Flow Reference 触发，则该子流的 trigger 节点不会执行，即该子流从第二个节点开始执行。

## 操作说明

### 参数配置

| 参数   | 数据类型 | 描述       | 是否必填 | 默认值 |
| :----- | :------- | :--------- | :------- | ------ |
| 集成流 | String   | 集成流名称 | 是       | 无     |

### 配置界面
![image-20210325142105983](https://main.qcloudimg.com/raw/7eaca90631c9f34001f9d726b9ad5cd8/image-20210325142105983.png)

### 输入到子流中的 message

| message 属性 | 值                                            |
| ----------- | --------------------------------------------- |
| payload     | 继承 Flow Refeference 上一个组件的 payload。      |
| error       | 空。                                            |
| attribute   | 继承 Flow Refeference 上一个组件的 attribute 信息。 |
| variable    | 继承 Flow Refeference 上一个组件的 variable 信息。  |

### 输出

Flow Reference 组件的执行结果，是子流的最后一个组件的输出。组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承 Flow Refeference 中子流输出的 payload。                      |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息。 |
| attribute   | 继承 Flow Refeference 中子流输出的 attribute。                   |
| variable    | 继承 Flow Refeference 中子流输出的 variable。                    |

## 案例
1. 新建一条集成流，名称为 flow2。
![image-20210330143809615](https://main.qcloudimg.com/raw/76189e21768bb221248f6041191ea5fa/image-20210330143809615.png)
![image-20210330143948910](https://main.qcloudimg.com/raw/2adcb4044967634b5805c7dd5647cfad/image-20210330143948910.png)
2. 添加 Flow Reference 组件，在下拉框中选择流 flow2。
 ![image-20210330144057018](https://main.qcloudimg.com/raw/17cc533f713724dd3e9411e460c67c1e/image-20210330144057018.png)
![image-20210330144127196](https://main.qcloudimg.com/raw/e518da991710caf7f822f337bf2429d6/image-20210330144127196.png)
