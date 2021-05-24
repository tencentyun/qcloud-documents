

## 简介

Raise Error 组件用来抛出异常，中断流的执行。该组件可以单独使用，也可以搭配 Try 组件使用。单独使用时，命中 Raise Error，集成流会抛出错误，中断执行。搭配 Try 组件使用时，可以在 Catch 中捕获 Raise Error 定义的异常，然后执行 Catch 中配置的子流。

## 操作配置

### 参数配置

| 参数     | 数据类型 | 描述               | 是否必填 | 默认值 |
| :------- | :------- | :----------------- | :------- | ------ |
| 错误类型 | string   | 用户自定义错误类型 | 是       | 无     |
| 错误描述 | tring    | 错误的描述信息     | 是       | 无     |

### 配置界面

![image-20210325145241012](https://main.qcloudimg.com/raw/98d93f6e5d269deac785374daf4d2f5f/image-20210325145241012.png)

### 输出

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承上个组件的 payload。                                        |
| error       | error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息。 |
| attribute   | 继承上个组件的 attribute 信息。                                  |
| variable    | 继承上个组件的 variable 信息。                                  |

## 案例
1. 添加 Raise Error 组件。
   ![image-20210330172601275](https://main.qcloudimg.com/raw/2616ca59ef09181e60964624875e2697/image-20210330172601275.png)
2. 填入错误类型和对应的错误描述。
   ![image-20210330172647344](https://main.qcloudimg.com/raw/7d76328cde2dddce937104b757fc3a28/image-20210330172647344.png)
3. 输出。
   ![image-20210426164825796](https://main.qcloudimg.com/raw/3727809c4bc33d154c6ac046acf7d56e/image-20210426164825796.png)
