

## 简介

Until Successful 组件中可以配置子流，该组件的作用是对子流执行重试操作。Until Successful 中可支持3种重试类型：无条件重试、按成功条件重试、按失败条件重试。用户可根据需要配置重试次数，支持的范围为1到100。两次重试之间的时间间隔也可根据需求配置，当前支持的范围为1~300秒。
- 无条件重试：如果重试条件类型为无，则只在子流报错的情况下重试。
- 按成功条件重试：当表达式结果为 false 时重试。
- 按失败条件重试：当表达式结果为 true 时重试。


## 操作配置

### 参数配置

| 参数         | 数据类型                                 | 描述                                                     | 是否必填 | 默认值 |
| :----------- | :--------------------------------------- | :------------------------------------------------------- | :------- | ------ |
| 重试条件类型 | 枚举：无、按成功条件重试、按失败条件重试 | 重试类型，按成功条件重试和按失败条件重试需填入条件表达式 | 是       | 无     |
| 重试次数     | int                                      | 重试次数，取值范围1~100                                  | 是       | 3      |
| 重试时间间隔 | int                                      | 重试间隔，取值范围1~300（单位秒）                          | 是       | 60     |

### 配置界面

![image-20210325173738880](https://main.qcloudimg.com/raw/960b0d7b313bc08ab962f53bdf0451cd/image-20210325173738880.png)

### 输入到子流中的 message

| message 属性 | 值                                            |
| ----------- | --------------------------------------------- |
| payload     | 继承 Until Successful 上一个组件的 payload       |
| error       | 空                                            |
| attribute   | 继承 Until Successful 上一个组件的 attribute 信息 |
| variable    | 继承 Until Successful 上一个组件的 variable 信息  |

### 输出

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承子流输出的 payload                                        |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承子流的 attribute 信息                                      |
| variable    | 继承子流的 variable 信息                                       |

## 案例

当需要对某类操作进行重试时，可以使用该组件，例如发送 request 请求，当请求失败时，使用 Until Successful 进行重试。
1. 添加 Until Successful 组件。
 ![image-20210330174112794](https://main.qcloudimg.com/raw/48c53438dab9ea1c76c7bd01c1d6a7fa/image-20210330174112794.png)
2. 选择按成功条件重试，当服务器返回的 errcode 不等于0时，我们重新发送请求，设置重试次数为3，重试间隔为1秒。
   ![image-20210330174558511](https://main.qcloudimg.com/raw/57d3949caa99c18ddfecf5d52a3d29b1/image-20210330174558511.png)
   ![image-20210330174523917](https://main.qcloudimg.com/raw/b6f3a54775f337544ec65066a44b4a81/image-20210330174523917.png)
3. 在 Until Successful 组件中添加 Request 组件，用于发送 HTTP 请求。
![image-20210330174737022](https://main.qcloudimg.com/raw/a4e9ee497be1f0b91530b0a10666652c/image-20210330174737022.png)
