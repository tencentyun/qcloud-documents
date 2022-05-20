

## 简介

Transform 组件可以对 message 消息进行数据编排和格式转换，支持 payload、attribute 和 variable 的修改，在使用 Transform 编辑 payload 时，需要先在 dataType 中定义要转换的数据类型，然后在 Transform 中绑定该类型，最后对输入消息进行编排，映射到绑定的数据类型上。

## 操作配置

### 参数配置
1. 确定要转换的类型，目前可选的有 payload，attributes，variables。
![image-20210426173059453](https://main.qcloudimg.com/raw/429a9243b81d2a00eddcd31876f1636d/image-20210426173059453.png)
2. 创建新的数据类型。
  ![image-20210426173243709](https://main.qcloudimg.com/raw/ac084b3057038d1385d7d9a0ca290477/image-20210426173243709.png)
  ![image-20210326095704120](https://main.qcloudimg.com/raw/c32a326ee344c8137d154e93ca86b29d/image-20210326095704120.png)
3. 绑定数据类型。
 ![image-20210426173756413](https://main.qcloudimg.com/raw/dbdde9f4ea41e316ca6776b01ba75577/image-20210426173756413.png)
4. 拖动字段，进行匹配。
  ![image-20210426174221561](https://main.qcloudimg.com/raw/b0caa15a188b74d4b2ba0c587ebc756e/image-20210426174221561.png)
5. 当图形转换无法满足业务需求时，可使用脚本输入进行补充。
![image-20210426174333859](https://main.qcloudimg.com/raw/5a5f0a6678a66b584a363f4fba67cbed/image-20210426174333859.png)

### 输出

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 如果“输出信息”中添加 payload，输出为 payload 中的执行结果，否则继承上一个组件的 payload。 |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息。 |
| attribute   | 类型为 dict，如果“输出信息”中添加 attributes，输出为 attributes 的执行结果，否则继承上一个组件的 attribute。 |
| variable    | 如果“输出信息”中添加 variables，输出为上一个组件的 variable 加上 transform 中新增的 variable，否则继承上一个组件的 variable。 |

## 案例
### 设置 payload
1. 添加 payload。
![image-20210426173059453](https://main.qcloudimg.com/raw/429a9243b81d2a00eddcd31876f1636d/image-20210426173059453.png)
2. 添加数据类型。
![image-20210426173243709](https://main.qcloudimg.com/raw/ac084b3057038d1385d7d9a0ca290477/image-20210426173243709.png)
![image-20210326095704120](https://main.qcloudimg.com/raw/c32a326ee344c8137d154e93ca86b29d/image-20210326095704120.png)
3. 绑定数据类型。
![image-20210426173756413](https://main.qcloudimg.com/raw/dbdde9f4ea41e316ca6776b01ba75577/image-20210426173756413.png)
4. 拖动字段，进行匹配。
  ![image-20210426174221561](https://main.qcloudimg.com/raw/b0caa15a188b74d4b2ba0c587ebc756e/image-20210426174221561.png)
5. 若图形化映射无法满足业务需求，可使用脚本进行编辑。
 ![image-20210426174333859](https://main.qcloudimg.com/raw/5a5f0a6678a66b584a363f4fba67cbed/image-20210426174333859.png)

### 设置 attribute
1. 添加 attributes。
   ![image-20210426174620878](https://main.qcloudimg.com/raw/1c506e83823f12b67109b67869f495e1/image-20210426174620878.png)
2. 添加表达式，编辑 attributes，attributes 的类型为 dict，因此表达式的输出需要保证类型为 dict，也可使用图形化编辑，使用方式与设置 payload 相同
   ![image-20210426174817312](https://main.qcloudimg.com/raw/c16189df90884598cbadc28aae54b08c/image-20210426174817312.png)

### 设置 variable
1. 添加 variables，“名称”处填入要声明的变量名字，也可使用图形化编辑，使用方式与设置 payload 相同。
   ![image-20210426174902089](https://main.qcloudimg.com/raw/3ca034ff9c53dfbf0194ad4f9fa0899e/image-20210426174902089.png)
2. 添加表达式，编辑变量数据。
   ![image-20210426175013126](https://main.qcloudimg.com/raw/8ca41d9e7b8e019a4f616085dbedffd8/image-20210426175013126.png)
