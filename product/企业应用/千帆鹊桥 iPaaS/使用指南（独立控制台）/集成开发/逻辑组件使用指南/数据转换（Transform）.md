## 简介

数据转换（Transform）组件可以对 message 消息进行数据编排和格式转换，支持 payload、attribute 和 variable 的修改。

## 操作配置

### 参数配置
| 参数   | 数据类型 | 描述         | 是否必填 | 默认值 |
| :----- | :------- | :----------- | :------- | ------ |
| payload | any   | 配置的 Payload     | 否       | 无     |
| attribute | dict      | 配置的 attribute | 否       | 无     |
| variable | dict      | 配置的变量 | 是       | 无     |

### 配置界面
<img src="https://qcloudimg.tencent-cloud.cn/raw/1242216723c3429a570cbd939fe83b94.png" alt="https://qcloudimg.tencent-cloud.cn/raw/1242216723c3429a570cbd939fe83b94.png" style="zoom:50%;" />

### 输出

组件输出的message信息如下：

| message属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 如果“输出信息”中添加了 payload，输出为 payload 中的执行结果，否则继承上一个组件的payload |
| error       | <ul><li>执行成功后，error 为空</li><li>执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息</li></ul> |
| attribute   | 类型为 dict，如果“输出信息”中添加了 attributes，输出为 attributes 的执行结果，否则继承上一个组件的 attribute |
| variable    | 如果“输出信息”中添加了 variables，输出为上一个组件的 variable 加上 transform 中新增的 variable，否则继承上一个组件的 variable |

## 案例

### 设置 payload
添加 payload。
![image-20210426173059453](https://main.qcloudimg.com/raw/429a9243b81d2a00eddcd31876f1636d/image-20210426173059453.png)


### 设置 attribute
添加 attributes，并编辑 attributes，attributes 的类型为 dict，因此表达式的输出需要保证类型为 dict。
![image-20210426174817312](https://qcloudimg.tencent-cloud.cn/raw/5c7781cbb4a269a3e8fa70835e44d089.png)

### 设置 variable
1. 添加 variables，“变量名称”处填入要声明的变量名字。
   ![image-20210426174902089](https://qcloudimg.tencent-cloud.cn/raw/7b3dddda0505e01ef53d6a34779a2656.png)
2. 添加表达式，编辑变量数据。
   ![image-20210426175013126](https://qcloudimg.tencent-cloud.cn/raw/77e13942865f7728a727dabae5f78d70.png)
