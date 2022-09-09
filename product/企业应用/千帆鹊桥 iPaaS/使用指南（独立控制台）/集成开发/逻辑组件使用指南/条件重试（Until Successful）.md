## 简介
条件重试（Until Successful）组件的作用是对其子流执行重试操作。


## 操作指引

根据您创建应用的时间不同，条件重试（Until Successful）组件的配置也不相同，具体如下：

| 配置方法 | 适用场景 | 配置入口 |
|---------|---------|---------|
| [方法一](#method1) | 在2022年9月1日前创建的应用 | 可选择按条件重试|
| [方法二](#method2) | 在2021年9月2日及之后创建的应用 | 仅在满足条件时重试 |


[](id:method1)
##  方法一（2022年9月1日前创建的应用）

### 参数配置

| 参数         | 数据类型                               | 描述                                                         | 是否必填 | 默认值 |
| :----------- | :------------------------------------- | :----------------------------------------------------------- | :------- | ------ |
| 重试条件类型 | 枚举：无；按成功条件重试；按失败条件重 | 重试条件的类型                                               | 是       | 无     |
| 重试条件     | bool                                   | 当重试条件类型为按成功条件重试或按失败条件重试时，定义判断的方法 | 否       | -      |
| 重试次数     | int                                    | 重试次数，取值范围1 - 100                                      | 是       | 3      |
| 重试时间间隔 | int                                    | 重试间隔，取值范围1 - 300，单位：秒                              | 是       | 60     |

![](https://qcloudimg.tencent-cloud.cn/raw/56e6e49a1457a6d01b539a87bdd5d11c.jpg)

### 数据预览

无

### 输入到子流中的 message

| message 属性 | 值                                      |
| ----------- | --------------------------------------- |
| payload     | 继承条件重试上一个组件的 payload       |
| error       | 空                                      |
| attribute   | 继承条件重试上一个组件的 attribute 信息 |
| variable    | 继承条件重试上一个组件的 variable 信息  |

### 输出

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承子流输出的 payload                                        |
| error       | <ul style="margin:0; "><li>执行成功后，error 为空</li><li>执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误描述</li></ul> |
| attribute   | 继承子流的 attribute 信息                                      |
| variable    | 继承子流的 variable 信息                                       |

### 案例

当需要对某类操作进行重试时，可以使用该组件，例如发送 request 请求，当请求失败时，使用 Until Successful 进行重试。

1. 添加 Until Successful 组件，当服务器返回的 statusCode 不等于200时，重新发送请求，设置重试次数为3，重试间隔为5秒。
![](https://qcloudimg.tencent-cloud.cn/raw/ba777fd6f09cca835db28c1ce74e278c.png)
2. 在 Until Successful 组件中添加 Request 组件，用于发送 HTTP 请求。
![](https://qcloudimg.tencent-cloud.cn/raw/0806d306216aaf08320cd7df664c2ea9.png)


[](id:method2)
##  方法二（2022年9月2日及之后创建的应用）


### 参数配置

| 参数         | 数据类型                               | 描述                                                         | 是否必填 | 默认值 |
| :----------- | :------------------------------------- | :----------------------------------------------------------- | :------- | ------ |
| 重试条件     | bool                                   | 定义重试的条件，当满足条件时触发重试| 否       | -      |
| 重试次数     | int                                    | 重试次数，取值范围1 - 100                                      | 是       | 3      |
| 重试时间间隔 | int                                    | 重试间隔，取值范围1 - 300，单位秒                              | 是       | 60     |

![](https://qcloudimg.tencent-cloud.cn/raw/56e6e49a1457a6d01b539a87bdd5d11c.jpg)

### 数据预览

无

### 输入到子流中的 message

| message属性 | 值                                      |
| ----------- | --------------------------------------- |
| payload     | 继承**条件重试**上一个组件的 payload       |
| error       | 空                                      |
| attribute   | 继承**条件重试**上一个组件的 attribute 信息 |
| variable    | 继承**条件重试**上一个组件的 variable 信息  |

### 输出

| message属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承子流输出的 payload                                        |
| error       | <ul style="margin:0; "><li>执行成功后，error 为空</li><li>执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误描述</li></ul> |
| attribute   | 继承子流的 attribute 信息                                      |
| variable    | 继承子流的 variable 信息                                       |

### 案例

当需要对某类操作进行重试时，可以使用该组件，例如发送request请求，当请求失败时，使用Until Successful进行重试

1. 添加 Until Successful 组件，当服务器返回的 statusCode不等于200时，重新发送请求，设置重试次数为3，重试间隔为5秒。
   ![](https://qcloudimg.tencent-cloud.cn/raw/ba777fd6f09cca835db28c1ce74e278c.png)
2. 在 Until Successful 组件中添加 Request 组件，用于发送 HTTP 请求。
   ![](https://qcloudimg.tencent-cloud.cn/raw/0806d306216aaf08320cd7df664c2ea9.png)
