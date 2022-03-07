
## 简介

Flow Reference 组件用来引用当前项目下集成应用中的其他集成流。用户可以通过 Flow Reference 组件引用同一项目下不同应用的集成流或当前应用中的其他集成流，减少重复配置的操作。

与 Async 不同，Flow Reference 是一个同步动作，当引用的集成流执行完成后，才会继续执行下一个动作，并且 Flow Reference 中的子流执行完成后，message 会传递到主流中，下一个节点基于该子流的 message 继续执行。当 Flow Reference 引用的子流包含 trigger 节点时，如果该子流的执行由 Flow Reference 触发，则该子流的 trigger 节点不会执行，即该子流从第二个节点开始执行。

## 操作说明

### 参数配置

| 参数   | 数据类型 | 描述       | 是否必填 | 默认值 |
| :----- | :------- | :--------- | :------- | ------ |
| 集成流 | String   | 集成流名称 | 是       | 无     |

### 配置界面
![](https://qcloudimg.tencent-cloud.cn/raw/e24b9d6247d7e043907b186ace34afea.png)

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
2. 对需要被引用的流，设置**共享**集成流的操作。
![](https://qcloudimg.tencent-cloud.cn/raw/7d7787290f5545d0165bb5663431dc66.png)
3. 添加 Flow Reference 组件，在下拉框中选择流 flow2，则对当前集成流设置引用 flow2 集成流完成。
![](https://qcloudimg.tencent-cloud.cn/raw/11c8f8970aec2d07dcf29d3cb7cfad11.png)
 完成后界面如下：
![](https://qcloudimg.tencent-cloud.cn/raw/e34afb8d16a80ac8ce8e7e4a0776e2f4.png)
