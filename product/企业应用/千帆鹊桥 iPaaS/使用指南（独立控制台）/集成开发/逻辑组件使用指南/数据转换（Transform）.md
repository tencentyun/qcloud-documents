### 数据转换（Transform）

#### 1. 简介

Transform组件可以对message消息进行数据编排和格式转换，支持payload、attribute和variable的修改。

#### 2. 操作配置

##### 参数配置
| 参数   | 数据类型 | 描述         | 是否必填 | 默认值 |
| :----- | :------- | :----------- | :------- | ------ |
| payload | any   | 配置的Payload     | 否       | 无     |
| attribute | dict      | 配置的attribute | 否       | 无     |
| variable | dict      | 配置的变量 | 是       | 无     |

##### 配置界面
<img src="https://qcloudimg.tencent-cloud.cn/raw/1242216723c3429a570cbd939fe83b94.png" alt="https://qcloudimg.tencent-cloud.cn/raw/1242216723c3429a570cbd939fe83b94.png" style="zoom:50%;" />

##### 输出

组件输出的message信息如下：

| message属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 如果“输出信息”中添加了payload，输出为payload中的执行结果，否则继承上一个组件的payload |
| error       | 执行成功后，error为空；执行失败后，error为dict类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 类型为dict，如果“输出信息”中添加了attributes，输出为attributes的执行结果，否则继承上一个组件的attribute |
| variable    | 如果“输出信息”中添加了variables，输出为上一个组件的variable加上transform中新增的variable，否则继承上一个组件的variable |

#### 3. 案例

##### 设置payload

1. 添加payload

![image-20210426173059453](https://main.qcloudimg.com/raw/429a9243b81d2a00eddcd31876f1636d/image-20210426173059453.png)


##### 设置attribute

1. 添加attributes，编辑attributes，attributes的类型为dict，因此表达式的输出需要保证类型为dict。

![image-20210426174817312](https://qcloudimg.tencent-cloud.cn/raw/5c7781cbb4a269a3e8fa70835e44d089.png)

##### 设置variable

1. 添加variables，“变量名称”处填入要声明的变量名字。

   ![image-20210426174902089](https://qcloudimg.tencent-cloud.cn/raw/7b3dddda0505e01ef53d6a34779a2656.png)

2. 添加表达式，编辑变量数据

   ![image-20210426175013126](https://qcloudimg.tencent-cloud.cn/raw/77e13942865f7728a727dabae5f78d70.png)
