

## 简介

Set Payload 可以设置 message 中的 payload 属性，支持表达式和字面量两种输入形式，如果是字面量形式，需要先选择数据类型，再在输入框中填入字面量。如果需要输入表达式，选择 any 类型，写入表达式即可。

## 操作配置

### 参数配置

| 参数 | 数据类型 | 描述                  | 是否必填 | 默认值 |
| :--- | :------- | :-------------------- | :------- | ------ |
| 值   | any      | payload 中要保存的数据。 | 是       | 无     |

### 输出

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 用户填入的数据。                                               |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息。 |
| attribute   | 继承上个组件的 attribute 信息。                                 |
| variable    | 继承上个组件的 variable 信息。                                   |

![image-20210325155210080](https://main.qcloudimg.com/raw/7c7927e7433ea490f909f66546f39f8e/image-20210325155210080.png)

## 案例
1. 添加 Set Payload 组件。
  ![image-20210330173057043](https://main.qcloudimg.com/raw/f2e0c6c6bdd74585cbca6f9934535136/image-20210330173057043.png)
2. 填入要设置的数据。
 ![image-20210330173121330](https://main.qcloudimg.com/raw/49579bbcf2b8f129cb7fd11df7bc8178/image-20210330173121330.png)
