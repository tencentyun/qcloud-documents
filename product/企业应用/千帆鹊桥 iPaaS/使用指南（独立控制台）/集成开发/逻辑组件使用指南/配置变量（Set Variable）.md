## 简介

配置变量（Set Variable）的作用是声明一个变量，并保存在 message 的 variables 中，后续节点可通过 msg.vars.get('name') 形式引用该变量。

## 操作配置

### 参数配置

| 参数   | 数据类型 | 描述         | 是否必填 | 默认值 |
| ----- | ------- | ----------- | ------- | ------ |
| 变量名 | string   | 变量名称     | 是       | 无     |
| 变量值 | any      | 变量的具体值 | 是       | 无     |

### 配置界面

![image-20210325155553571](https://qcloudimg.tencent-cloud.cn/raw/335c300d56335bdd782824aa70051469.png)

### 输出

对 variables 变量的引用，需要使用表达式：msg.vars.get('company')。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承上个组件的 payload                                        |
| error       | <ul><li>执行成功后，error 为空</li><li>执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息</li></ul> |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 上个组件的 variable 信息加上当前组件添加的变量                 |

### 数据预览
<img src="https://qcloudimg.tencent-cloud.cn/raw/2692c10c80d8f86ee29b69f3505f6f44.png" alt="https://qcloudimg.tencent-cloud.cn/raw/2692c10c80d8f86ee29b69f3505f6f44.png" style="zoom:50%;" />

## 案例

1. 添加 Set Variable 组件。
   ![image-20210330173246414](https://qcloudimg.tencent-cloud.cn/raw/94c98067f1bbfbf770b46abade141cb2.png)
2. 在”变量名“处填入变量名称，“变量值”处填入要保存的值。
![image-20210325155553571](https://qcloudimg.tencent-cloud.cn/raw/335c300d56335bdd782824aa70051469.png)
