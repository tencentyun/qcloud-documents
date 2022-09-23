
## 简介

Scatter Gather 支持并行执行多个任务，该组件中，有两个核心配置，一个是并行数，目前支持的并行数是2~8个，另一个是 worker，每个 worker 中都可以配置一个待执行的任务。当 worker 数目和并行数不一致时，实际的并行数目是两者中的较小值。Scatter Gather 以上一个节点输出的 message 作为输入，并行执行 worker 中配置的任务。最后的输出以字典呈现，字典的 key 是 worker 的下标，从1开始，value 是对应 worker 执行完成后的 payload，message 中的 attributes 和 variables 都会丢弃。

## 操作配置

### 参数配置

| 参数       | 数据类型 | 描述                                                         | 是否必填 | 默认值      |
| :--------- | :------- | :----------------------------------------------------------- | :------- | ----------- |
| 最大并行数 | int      | 并行执行的任务数，取值范围为2~8。                              | 是       | 4           |
| 根信息     | string   | 根信息同样是一个变量，这里填入变量名称，根信息中保存主流的 message 信息，msg.vars.get('#根信息名称#').payload 即可访问主流的 payload 数据。当使用默认值 rootMessage 时，使用 msg.vars.get('rootMessage').payload 即可在子流中访问主流的 payload 数据。 | 否       | rootMessage |

### 配置界面
![image-20210325151522225](https://main.qcloudimg.com/raw/785500c3bc8f6d77979e4a6e38631032/image-20210325151522225.png)
![image-20210325151540332](https://main.qcloudimg.com/raw/6bc234664109703674f1fedee7436538/image-20210325151540332.png)



### 输入子流中的 message

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承 Scatter Gather 上一个组件的 payload 信息。                    |
| error       | 空。                                                           |
| attribute   | 空。                                                           |
| variable    | 包含两个变量，一个是计数器，一个是根信息，若用户使用默认值，可使用表达式 msg.vars.get('counter') 和 msg.vars.get('rootMessage') 访问。 |

### 输出
worker 的输出结果中不会包含处理逻辑中使用的 variable 变量，最终输出的只有 payload 里的数据，Scatter Gather 的 payload 是汇总每个 worker 的 payload 结果，attribute 和 variabls 保留上一个节点的输出。如图所示："1"表示 worker1 的输出，"2"表示 worker2 的输出。
![image-20210325151823517](https://main.qcloudimg.com/raw/70da499b4ab2d1039acbda8650c6cb81/image-20210325151823517.png)

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | dict 类型，key 是 work 的编号，从"1"开始，value 是 work 执行完成后的结果。 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息。 |
| attribute   | 继承 Scatter Gather 上一个组件的 attribute 信息。                  |
| variable    | 继承 Scatter Gather 上一个组件的 variable 信息。                   |



## 案例
当需要并行执行不同的任务时，使用 Scatter Gather 组件比较合适，假设需要根据用户订单数据，去查询客户信息及产品信息，则可以配置两个 worker，一个执行客户信息查询，一个执行产品信息查询。
1. 添加 Scatter Gather 组件，设置最大并行度为2。
   ![image-20210406104620307](https://main.qcloudimg.com/raw/cd14ee16e97bd273f793859d16378da9/image-20210406104620307.png)
   ![image-20210406104725833](https://main.qcloudimg.com/raw/e92ad6da066f40fb3afbd6a93b86b32a/image-20210406104725833.png)
2. 第一个 worker 配置客户信息查询，第二个 worker 配置产品信息查询，在 Scatter Gather 的输出中，即可看到客户和产品信息。
   ![image-20210406105603113](https://main.qcloudimg.com/raw/57e3d62b6a97e430055c418ec6134522/image-20210406105603113.png)
3. 查询结果，字典中 key 为"1"的元素，保存客户信息，key为“2”的元素，保存产品信息。
   ![image-20210428171556249](https://main.qcloudimg.com/raw/bb71b4e7f0f593405e6aee9db80156e3/image-20210428171556249.png)
