

## 简介

Remove Variable 组件与 Set Variable 组件的作用相反，Remove Variable 组件的作用是删除 message 中的一个指定变量。

## 操作配置

### 参数配置

| 参数     | 数据类型 | 描述             | 是否必填 | 默认值 |
| :------- | :------- | :--------------- | :------- | ------ |
| 变量名称 | string   | 要移除的变量名称 | 是       | 无     |

### 配置界面

![image-20210325145534545](https://main.qcloudimg.com/raw/ab9a378a0900d2c8b4cd0528071d1600/image-20210325145534545.png)

### 输出

输出的 message 中，不再包括删除的变量。组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承上个组件的 payload。                                      |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息。 |
| attribute   | 继承上个组件的 attribute 信息。                                  |
| variable    | 上个组件的 variable 信息中去除删掉的变量。                       |

**输出示例**
输入到 Remove Varaible 中的变量如下：
![image-20210426165649320](https://main.qcloudimg.com/raw/53161e060afb3594a22095ed57e363b0/image-20210426165649320.png)
使用 Remove Variable 删除变量 name 后，如下所示：
![image-20210426165741239](https://main.qcloudimg.com/raw/6cec7de7bfba3708ae9f50c77b3a13a6/image-20210426165741239.png)



## 案例
1. 添加 Remove Variable 组件。
![image-20210330172804271](https://main.qcloudimg.com/raw/f6013c84dfcbbc76b97362868d9c9404/image-20210330172804271.png)
2. 填入要移除的变量名称。
![image-20210330172924688](https://main.qcloudimg.com/raw/065c78d32f78f046911c1e3c239094a5/image-20210330172924688.png)
