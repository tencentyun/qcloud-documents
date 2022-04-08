

## 简介

Parallel Foreach 用于并行执行任务，Parallel Foreach 对数据集上的元素并行执行相同的处理逻辑，并行数目依赖于用户配置的最大并行数，当元素数目小于等于最大并行数时，并行数等于元素数目，当元素数目大于最大并行数时，并行数为用户配置的最大并行数。处理完成后，每个元素的处理结果按照原始顺序输出到 message 的 payload 中。Parallel Foreach 一般用于批量数据处理的场景，例如：批量查询、批量导入数据等。

## 操作配置

### 参数配置

| 参数       | 数据类型           | 描述                                                         | 是否必填 | 默认值      |
| :--------- | :----------------- | :----------------------------------------------------------- | :------- | ----------- |
| 数据集     | string、list、dict、int | 待遍历的数据：<br><li>当类型为 string 时，遍历字符串的每个字符；<br><li>当类型为 list 时，遍历 list 的每个元素；<br><li>当类型为 dict 时，遍历 dict 中的 value；<br><li>当数据集类型为 int 时，例如3，实际遍历的数据集为[0,1,2]。 | 是       | 无          |
| 最大并行数 | int                | 并行执行的任务数，取值范围为2~8。                              | 是       | 4           |
| 计数器     | string             | 计数器是一个变量，该变量存储当前的迭代次数，从0开始，此处填入变量名称，msg.vars.get('#计数器变量#') 即可使用；例如：当计数器变量使用默认值 counter 时，第1次循环，msg.vars.get('counter') 值为0，第2次循环，msg.vars.get('counter') 值为1。 | 否       | counter     |
| 根信息     | string             | 根信息同样是一个变量，此处填入变量名称，根信息中保存主流的 message 信息，msg.vars.get('#根信息名称#').payload 即可访问主流的 payload 数据。当使用默认值 rootMessage 时，使用 msg.vars.get('rootMessage').payload 即可在 Parallel ForEach 的子流中访问主流的 payload 数据。 | 否       | rootMessage |

### 配置界面
![image-20210325142855462](https://main.qcloudimg.com/raw/215cf32c57eee9ea6cc077a9380db08e/image-20210325142855462.png)

### 输入到子流中的 message

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 数据集中的元素，例如：<li>待处理的数据集为[1,2,3]，第一个并行任务中，子流中 payload 的数据为1，第二个并行任务的 payload 为2；<li>待处理的数据集为 dict 类型，{"key":"key1", "value":"value1"}，第一个并行任务中，子流中的 payload 为 key1，第二个并行任务的 payload 为 value1。 |
| error       | 空。                                                           |
| attribute   | 空。                                                           |
| variable    | 包含两个变量，一个是计数器，一个是根信息，若用户使用默认值，可使用表达式 msg.vars.get('counter') 和 msg.vars.get('rootMessage') 访问。 |

### 输出

Parallel Foreach 的输出结果中，不会包含处理逻辑中使用的 variable 变量，最终输出的只有 payload 里的数据，输出的 payload 是个 list 类型变量，里边包含原始数据集中每个元素迭代处理的结果，顺序与原始数据集一致。attribute 的值继承自上一个组件。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | list 类型，包含了每个数据的处理结果，输出顺序与原始的输入顺序一致。 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息。 |
| attribute   | 继承 Parallel ForEach 上一个组件的 attribute 信息。               |
| variable    | 继承 Parallel ForEach 上一个组件的 variable 信息。                 |

**输出样例**
![image-20210426164542507](https://main.qcloudimg.com/raw/07b743733370085c12a1538acf07fa7b/image-20210426164542507.png)

## 案例
本案例中，我们使用 Parallel Foreach 组件对列表中的数据统一进行加1操作，原始的数据集为[1,2,3,4]。
1. 添加 Parallel Foreach 组件，配置数据集[1,2,3,4]，并设置并行度为4。
   ![image-20210426164025987](https://main.qcloudimg.com/raw/0a49cb73f12fda19dc8b5d492025680c/image-20210426164025987.png)
2. 在 Parallel Foreach 中拖入 Set Payload 组件，对数据集执行加1操作。
   ![image-20210426164228237](https://main.qcloudimg.com/raw/430d54e2b041bc620784bc0a449e36c6/image-20210426164228237.png)
3. 输出结果。
   ![image-20210426164542507](https://main.qcloudimg.com/raw/07b743733370085c12a1538acf07fa7b/image-20210426164542507.png)
