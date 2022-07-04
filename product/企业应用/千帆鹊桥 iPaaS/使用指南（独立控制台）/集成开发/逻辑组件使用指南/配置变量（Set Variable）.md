### 配置变量（Set Variable）

#### 1. 简介

Set Variable的作用是声明一个变量，并保存在message的variables中，后续节点可通过msg.vars.get('name')形式引用该变量

#### 2. 操作配置

##### 参数配置

| 参数   | 数据类型 | 描述         | 是否必填 | 默认值 |
| :----- | :------- | :----------- | :------- | ------ |
| 变量名 | string   | 变量名称     | 是       | 无     |
| 变量值 | any      | 变量的具体值 | 是       | 无     |

##### 配置界面

![image-20210325155553571](https://qcloudimg.tencent-cloud.cn/raw/335c300d56335bdd782824aa70051469.png)

##### 输出

对variables变量的引用，需要使用表达式：msg.vars.get('company')

组件输出的message信息如下：

| message属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承上个组件的payload                                        |
| error       | 执行成功后，error为空；执行失败后，error为dict类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的attribute信息                                  |
| variable    | 上个组件的variable信息加上当前组件添加的变量                 |

##### 数据预览
<img src="https://qcloudimg.tencent-cloud.cn/raw/2692c10c80d8f86ee29b69f3505f6f44.png" alt="https://qcloudimg.tencent-cloud.cn/raw/2692c10c80d8f86ee29b69f3505f6f44.png" style="zoom:50%;" />

#### 3. 案例

1. 添加Set Variable组件

   ![image-20210330173246414](https://qcloudimg.tencent-cloud.cn/raw/94c98067f1bbfbf770b46abade141cb2.png)

2. 在”变量名“处填入变量名称，"变量值"处填入要保存的值

![image-20210325155553571](https://qcloudimg.tencent-cloud.cn/raw/335c300d56335bdd782824aa70051469.png)
