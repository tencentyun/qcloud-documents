

## 简介

Choice 是分支选择语句，基于不同的条件执行不同的动作，类似于 if-else。Choice 下包含两类子节点，分别为 When 和 Default，在 Choice 中可以添加多个 When 节点，每个 When 节点中都包含一个 bool 表达式，Choice 组件会对 When 节点逐个匹配，直到表达式满足条件，则执行该 When 节点中配置的子流。当所有的 When 条件都无法匹配时，会执行 Default 分支的动作。

## 操作说明

### 参数配置
在 When 节点中，可以配置条件语句，用来控制分支选择。

| 参数 | 数据类型 | 描述                                   | 是否必填 | 默认值 |
| :--- | :------- | :------------------------------------- | :------- | ------ |
| 条件 | bool     | 条件判断，当条件满足时，执行对应的子流。 | 是       | 无     |

### 配置界面
![image-20210325142028861](https://main.qcloudimg.com/raw/b206d952c3b7f312d4771605373f4121/image-20210325142028861.png)
![image-20210325142008052](https://main.qcloudimg.com/raw/a99c16ce9717c85acd696f22fd637c50/image-20210325142008052.png)

### 输入到子流中的 message

| message 属性 | 值                                  |
| ----------- | ----------------------------------- |
| payload     | 继承 Choice 上一个组件的 payload。       |
| error       | 空。                                  |
| attribute   | 继承 Choice 上一个组件的 attribute 信息。 |
| variable    | 继承 Choice 上一个组件的 variable 信息。  |

### 输出
Choice 属于流控类组件，输出的 message 是具体执行的子流生成的 message。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承子流输出的 payload。                                       |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息。 |
| attribute   | 继承子流输出的 attribute。                                      |
| variable    | 继承子流输出的 variable。                                       |

## 案例
在该案例中，我们将 score 映射为不同的 level。
- 当 score 大于等于90时，level 为”A“。
- 当 score 大于等于80，小于90时，level 为”B“。
- 当 score 大于等于60，小于80时，level 为”C“。
- 当 score 小于60时，level 为“D”。

**操作步骤：**
1. 添加 Choice 组件。
![image-20210330111731146](https://main.qcloudimg.com/raw/0e90fe3f672339decc5e382d294ee2b2/image-20210330111731146.png)
2. 在 Choice 中添加 When 节点，每个 When 节点都是一个分支条件。
![image-20210330111843827](https://main.qcloudimg.com/raw/d069faa2c6cae77d2a5b983334d7c9b0/image-20210330111843827.png)
3. 在 When 节点中填入判断条件，第一个 When 节点输入 msg.vars.get('score') >= 90，第二个 When 节点输入 msg.vars.get('score') >= 80，第三个 When 节点输入 msg.vars.get('score') >= 60，Default 节点中不用输入条件。
![image-20210330111705982](https://main.qcloudimg.com/raw/39d42d29681140f76ce068bf420db491/image-20210330111705982.png)
4. 在每个 When 节点中，添加 Set Variable 节点，保存 level 值。
![image-20210330112539211](https://main.qcloudimg.com/raw/f4e692c1b451adfdbc708d898cf21166/image-20210330112539211.png)
![image-20210330114207853](https://main.qcloudimg.com/raw/c594b0144928e50963721ca5ae14223c/image-20210330114207853.png)
