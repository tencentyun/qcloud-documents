

## 简介

For Each 是循环控制结构，类似于编程语言中的 for/foreach，在 For Each 中可以配置子流，对指定的数据集进行循环处理，但是无法指定循环次数。使用该组件时，数据集填写待遍历的数据，计数器中填入一个变量名称，默认为 counter，该变量存储当前的迭代次数。根信息中同样填入一个变量名称，默认为 rootMessage，该变量中保存主流的 message 信息，For Each 中配置的子流可使用 msg.vars.get('rootMessage') 访问主流中的 message。

## 操作说明

### 参数配置

| 参数   | 数据类型           | 描述                                                         | 是否必填 | 默认值      |
| :----- | :----------------- | :----------------------------------------------------------- | :------- | ----------- |
| 数据集 | string、list、dict、int | 待遍历的数据：<br><li>当类型为 string 时，遍历字符串的每个字符；<br><li>当类型为 list 时，遍历 list 的每个元素；<br><li>当类型为 dict 时，遍历 dict 中的 value；<br><li>当数据集类型为 int 时，例如3，实际遍历的数据集为[0,1,2]。 | 是       | 无          |
| 计数器 | string             | 计数器是一个变量，该变量存储当前的迭代次数，从0开始，填入变量名称，msg.vars.get('#计数器变量#') 即可使用；例如：当计数器变量使用默认值 counter 时，第1次循环，msg.vars.get('counter') 值为0，第2次循环，msg.vars.get('counter') 值为1。 |否      | counter     |
| 根信息 | string             | 根信息同样是一个变量，填入变量名称，根信息中保存主流的 message 信息，msg.vars.get('#根信息名称#').payload 即可访问主流的 payload 数据。当使用默认值 rootMessage 时，使用 msg.vars.get('rootMessage').payload 即可在 For Each 的子流中访问主流的 payload 数据。 | 否       | rootMessage |

### 配置界面

![image-20210325142639861](https://main.qcloudimg.com/raw/8580d530f9f61e1d1dc352de8aa2d814/image-20210325142639861.png)

### 输入到子流中的 message

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 数据集中的元素，例如：待迭代的数据集为[1,2,3]，第一次循环，子流中 payload 的数据为1，第二次循环为2；待迭代的数据集为 dict 类型，{"key":"key1", "value":"value1"}，第一次循环，子流中的 payload 为 key1，第二次为 value1。 |
| error       | 空。                                                           |
| attribute   | 空。                                                           |
| variable    | 继承主流中的 variable 数据，同时新增两个变量，一个是计数器，一个是根信息，若用户使用默认值，可使用表达式 msg.vars.get('counter') 和 msg.vars.get('rootMessage') 访问。若 For Each 中使用了 Set Variable，则在子流执行过程中，新增的变量也会添加到 varaible 中。 |

### 输出
For Each 组件输出的 message 中，保留了 For Each 上一个组件的 payload 和 attributes 信息，只有 For Each 中子流使用的 variable 变量会传递出来。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 继承 For Each 上一个组件输出的 payload。                        |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息。 |
| attribute   | 继承上 For Each 上一个组件输出的 attribute 信息。                  |
| variable    | For Each 上一个组件输出的 variable 变量加上 For Each 子流中声明的 variable 变量。 |

## 案例
使用 For Each 组件遍历列表，为列表中的元素添加序号及前缀，列表元素及前缀从 HTTP 请求的参数中获得，操作步骤如下：
1. 添加 For Each 组件，数据集从 HTTP 请求的参数中获得，计数器设置为“index”，根信息使用默认变量“rootMessage”。
![image-20210330151906179](https://main.qcloudimg.com/raw/09144969ec8513f3fd4b31739691e425/image-20210330151906179.png)
2. 配置数据集。
 ![image-20210330152245223](https://main.qcloudimg.com/raw/bd5776bf002fbb688c363505df901040/image-20210330152245223.png)
3. 设置计数器。
 ![image-20210330152127647](https://main.qcloudimg.com/raw/7a0185fc240eddf2179447b6a09ce5fb/image-20210330152127647.png)
4. 在 For Each 组件中加入 Set Variable 组件，用于处理业务逻辑。
 ![image-20210330170426250](https://main.qcloudimg.com/raw/51068c8835c0d84df5d7c09f85047d58/image-20210330170426250.png)
 - 如下图所示，第二行是从 msg.vars 中获取当前的索引值，第三行是从 HTTP 请求中获取前缀，第四行将拼接完成的字符串赋值到 result 变量中。
  ![image-20210330170546205](https://main.qcloudimg.com/raw/3e60b88a6dabdd5da3722ad322b554a4/image-20210330170546205.png)
5. 在 For Each 组件后加入 Set Payload 组件，将结果输出。
   ![image-20210330170918588](https://main.qcloudimg.com/raw/cbc2244a0e8feba9bbc4cddfbff6c8cb/image-20210330170918588.png)
   ![image-20210330170947582](https://main.qcloudimg.com/raw/01ccfca739419a0f4f86283231025d7c/image-20210330170947582.png)
6. 输出效果。
  ![image-20210330170759237](https://main.qcloudimg.com/raw/7edd6023f217199e6b643f315577609f/image-20210330170759237.png)
