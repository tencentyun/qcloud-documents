
## 简介

删除变量（Remove Variable）组件与配置变量（Set Variable）组件的作用相反，Remove Variable 组件的作用是删除 message 中的一个指定变量。

## 操作配置

### 参数配置

| 参数     | 数据类型 | 描述             | 是否必填 | 默认值 |
| :------- | :------- | :--------------- | :------- | ------ |
| 变量名称 | string   | 要移除的变量名称 | 是       | 无     |

### 配置界面

![image-20210325145534545](https://qcloudimg.tencent-cloud.cn/raw/ed66b946bc366e104cc364dfba38ef37.png)

### 输出

输出的 message 中，不再包括删除的变量。组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承上个组件的 payload。                                        |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息。 |
| attribute   | 继承上个组件的 attribute 信息。                                  |
| variable    | 上个组件的 variable 信息中去除删掉的变量。                       |

### 数据预览

无

## 案例

1. 添加 Remove Variable 组件。
![image-20210330172804271](https://qcloudimg.tencent-cloud.cn/raw/e761cd9561567cde138c327891b25ced.png)
2. 填入要移除的变量名称。
![image-20210330172924688](https://qcloudimg.tencent-cloud.cn/raw/920f42cfec2bf38feb675775ceca237f.png)
