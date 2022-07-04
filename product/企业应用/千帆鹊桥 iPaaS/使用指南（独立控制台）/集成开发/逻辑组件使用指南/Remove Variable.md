### Remove Variable

#### 1. 简介

Remove Variable组件与Set Variable组件的作用相反，Remove Variable组件的作用是删除message中的一个指定变量。

#### 2. 操作配置

##### 参数配置

| 参数     | 数据类型 | 描述             | 是否必填 | 默认值 |
| :------- | :------- | :--------------- | :------- | ------ |
| 变量名称 | string   | 要移除的变量名称 | 是       | 无     |

##### 配置界面

![image-20210325145534545](https://qcloudimg.tencent-cloud.cn/raw/ed66b946bc366e104cc364dfba38ef37.png)

##### 输出

输出的message中，不再包括删除的变量

组件输出的message信息如下：

| message属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承上个组件的payload                                        |
| error       | 执行成功后，error为空；执行失败后，error为dict类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的attribute信息                                  |
| variable    | 上个组件的variable信息中去除删掉的变量                       |

##### 数据预览

无

#### 3. 案例

1. 添加Remove Variable组件

![image-20210330172804271](https://qcloudimg.tencent-cloud.cn/raw/e761cd9561567cde138c327891b25ced.png)

2. 填入要移除的变量名称

![image-20210330172924688](https://qcloudimg.tencent-cloud.cn/raw/920f42cfec2bf38feb675775ceca237f.png)
