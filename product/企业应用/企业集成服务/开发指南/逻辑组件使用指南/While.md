

## 简介

While 组件是循环类组件，While 组件支持的最大循环次数为10000。与 For Each 组件不同，While 组件的循环并不依赖数据集，而是使用条件语句判断循环是否需要继续，当循环条件为 True 时，会继续循环，直到返回 False 或达到最大的循环次数。我们将输入到 While 组件的 message 消息称作父 message，While 组件中配置的子流，会生成子 message，子 message 只继承父 message 的 variable 变量，并且父 message 的消息内容，全部保存在变量 rootMessage 中，如果要在子流中访问父 message 的 payload，使用表达式 msg.vars.get('rootMessage').payload。当 While 组件执行完成后，只有子流中的 variable 变量可以传递出来，并添加到父 message 中，继续向下传递。

## 操作配置

### 参数配置

| 参数         | 数据类型 | 描述                                                         | 是否必须 | 默认值  |
| :----------- | :------- | :----------------------------------------------------------- | :------- | ------- |
| 循环条件     | bool     | 返回 True，则继续执行循环；返回 False，终止循环。                      | 是       | 无      |
| 计数器       | string   | 计数器是一个变量，该变量负责存储当前的迭代次数，从0开始，此处填入变量名称，msg.vars.get('#计数器变量#') 即可使用；例如：当计数器变量使用默认值 counter 时，第1次循环，msg.vars.get('counter') 值为0，第2次循环，msg.vars.get('counter') 值为1。 | 是       | counter |
| 最大循环次数 | int      | 最大循环次数，超过后终止循环，最大值为10000。                  | 是       | 10000   |

### 配置界面

![image-20210325194354426](https://main.qcloudimg.com/raw/4ab33d4af62767a26a02f8dbf7acb7fe/image-20210325194354426.png)

### 输入到子流中的 message

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 空。                                                           |
| error       | 空。                                                           |
| attribute   | 空。                                                           |
| variable    | 继承主流中的 variable 数据，同时新增两个变量，分别为计数器和根信息，若用户使用默认值，可使用表达式 msg.vars.get('counter') 和 msg.vars.get('rootMessage') 进行访问。 |

### 输出

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承上个组件的 payload。                                        |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息。 |
| attribute   | 继承上个组件的 attribute 信息。                                  |
| variable    | 上个组件的 variable 信息加上 While 中子流新增的 variable 变量。      |

## 案例

使用 While 组件，我们可以执行一些数据的筛选，例如：从服务端返回的数据列表中筛选符合业务需求的数据。
1. 使用 Request 组件请求服务端数据。 
   ![image-20210406143357399](https://main.qcloudimg.com/raw/389007f788cf6218b888dc755d7bfe24/image-20210406143357399.png)
2. 声明保存结果的变量。
![image-20210406143524162](https://main.qcloudimg.com/raw/cf338dd81ff32634274998fc3ca4dbe4/image-20210406143524162.png)
3. 添加 While 组件，循环结束的条件是“result”变量不为空，计数器使用默认“counter”。
   ![image-20210406143713507](https://main.qcloudimg.com/raw/327cc5af56fa66e3cef266aa043f4c3c/image-20210406143713507.png)
![image-20210406143830753](https://main.qcloudimg.com/raw/de50a963af4b6eca7ad6690dfc905fda/image-20210406143830753.png)
4. 添加 variable 变量，筛选数据。
   ![image-20210406144420113](https://main.qcloudimg.com/raw/0016706db63ced2ae77c18ab842756f1/image-20210406144420113.png)
   ![image-20210406144243165](https://main.qcloudimg.com/raw/9e7c4ce5cdec17fa2ba8111985fd8ff0/image-20210406144243165.png)
5. index 变量获得数组下标，payload 中的 data 为数组类型，根据下标获取数据，判断数据是否符合要求。若符合，则返回结果。Whlie 组件的下个节点可使用 msg.vars.get('result') 获得 While 子流中筛选到的数据。
   ![image-20210406144218828](https://main.qcloudimg.com/raw/62083312aac929c159721ca827479d68/image-20210406144218828.png)

