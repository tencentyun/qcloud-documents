### Remove Variable

#### 1. 简介

Remove Variable组件与Set Variable组件的作用相反，Remove Variable组件的作用是删除message中的一个指定变量。

#### 2. 操作配置

##### 参数配置

| 参数     | 数据类型 | 描述             | 是否必填 | 默认值 |
| :------- | :------- | :--------------- | :------- | ------ |
| 变量名称 | string   | 要移除的变量名称 | 是       | 无     |

##### 配置界面

![image-20210325145534545](https://main.qcloudimg.com/raw/ab9a378a0900d2c8b4cd0528071d1600/image-20210325145534545.png)

##### 输出

输出的message中，不再包括删除的变量

组件输出的message信息如下：

| message属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承上个组件的payload                                        |
| error       | 执行成功后，error为空；执行失败后，error为dict类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的attribute信息                                  |
| variable    | 上个组件的variable信息中去除删掉的变量                       |

例如，输入到Remove Varaible中的变量如下：

![image-20210426165649320](https://main.qcloudimg.com/raw/53161e060afb3594a22095ed57e363b0/image-20210426165649320.png)

使用Remove Variable删除变量name后，如下所示：

![image-20210426165741239](https://main.qcloudimg.com/raw/6cec7de7bfba3708ae9f50c77b3a13a6/image-20210426165741239.png)



#### 3. 案例

1. 添加Remove Variable组件

![image-20210330172804271](https://main.qcloudimg.com/raw/f6013c84dfcbbc76b97362868d9c9404/image-20210330172804271.png)

2. 填入要移除的变量名称

   ![image-20210330172924688](https://main.qcloudimg.com/raw/065c78d32f78f046911c1e3c239094a5/image-20210330172924688.png)
