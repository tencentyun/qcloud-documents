

## 简介

Logger 组件用来在控制台输出日志，目前支持 DEBUG、INFO、WARN、ERROR 四种日志级别。

## 操作说明

### 参数配置

| 参数     | 数据类型 | 描述                                                         | 是否必填 | 默认值 |
| :------- | :------- | :----------------------------------------------------------- | :------- | ------ |
| 日志级别 | string   | 日志级别，目前支持 DEBUG、INFO、WARN、ERROR，在运行监控中查看日志时，可以根据级别筛选日志。 | 是       | INFO   |
| 日志类别 | string   | 日志分类，由用户自定义。                                       | 否       | 无     |
| 日志内容 | any      | 日志内容可以是 dataway 支持的任意类型，在输出时，系统会自动转为 string。 | 是       | 无     |

### 配置界面

![image-20210325142825600](https://main.qcloudimg.com/raw/9a8608ea1a58c09aa8bf65229e88bcc4/image-20210325142825600.png)

### 输出

Logger 组件只是输出内容到控制台，并不会改变 message 中的内容，输出内容中包括日志级别、日志类别、日志内容。组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承上个组件的 payload。                                       |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息。 |
| attribute   | 继承上个组件的 attribute 信息。                                  |
| variable    | 继承上个组件的 variable 信息。                                   |

![image-20210325110859844](https://main.qcloudimg.com/raw/37058a3e36ff95e7f986a4b92fbe3f17/image-20210325110859844.png)

## 案例
1. 添加 Logger 组件。
![image-20210330172016643](https://main.qcloudimg.com/raw/194b47dbb8f9b37136c87fa5b71a76b2/image-20210330172016643.png)
2. 在日志级别的下拉列表中，选择 INFO，日志内容中填入待打印的数据。
![](https://main.qcloudimg.com/raw/719d011681039d885d438728a8c3c601/image-20210330172055710.png)
3. 在运行监控中查看日志。单击**运行监控**，选择**运行日志**，选择需要查看的集成流，即可看到对应的日志，目前支持查看历史日志和实时日志，历史日志可保留30天。
  ![image-20210330172212930](https://main.qcloudimg.com/raw/508524add9e658a5da384a14abbdca41/image-20210330172212930.png)
