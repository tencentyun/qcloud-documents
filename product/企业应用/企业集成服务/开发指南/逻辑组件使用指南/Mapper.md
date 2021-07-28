
## 简介
Mapper 组件仅用于操作 [RecordSet]()。它可以对输入的 RecordSet（一种表单数据）进行转换，并生成一个子集。在转换的过程中，还支持 Lookup 功能。

## 配置
Mapper 的配置界面包含三部分：
- 输入信息：会自动展示输入数据的字段和类型信息。
- 输出信息：需要用户配置输出的字段和类型信息。
- 逻辑映射：配置输入和输出字段间的映射关系。
![image-mapper-1](https://main.qcloudimg.com/raw/82182824a9f4933ad711855dd078388e/image-mapper-1.png)

### 输入信息
默认会自动识别`msg.payload`包含的字段以及字段类型进行展示。如果识别的结果不准确，用户也可以主动修改。
![image-mapper-2](https://main.qcloudimg.com/raw/d7807f7587e0bd30ae2bd69762e33dba/image-mapper-2.png)

### 输出信息
需要用户主动配置输出数据要包含的字段和类型。支持用户直接给输出字段进行赋值，支持赋值常量或者表达式：
- 常量：可以设置任意常量值。
- 表达式：在表达式里面可以用 msg.payload 处理所有输入的字段。
![image-mapper-3](https://main.qcloudimg.com/raw/30835ef853d6a936a4e05572fbbf769e/image-mapper-3.png)
![image-mapper-4](https://main.qcloudimg.com/raw/a55e6fb36d7941328de7e57651bbfd52/image-mapper-4.png)


### 逻辑映射
用户指定输入信息和输出信息间的映射关系，用户可以直接连线，也可以新增逻辑映射节点来处理更复杂的转换需求。
![image-mapper-5](https://main.qcloudimg.com/raw/85920999489178db2c06da4650485cce/image-mapper-5.png)
- 直连：输入直接赋值给输出，要确保类型一致。
- 新增映射逻辑：目前支持多种 Lookup 查找功能和表达式处理功能，且使用 Lookup 时可以配置三种查找策略：
 - 每次都重新查找：对于输入的表单数据中的每一行，都重新执行一次查找。
 - 只查找一次：无聊输入的表单数据有多少行，都只执行一次查找。
 - 周期性查找：可以配置一个查找周期。
每个映射逻辑节点，一般可以配置多个输入和输出，类似于一个函数的入参和出参。用户可以将 Mapper 组件输入信息中的字段连线到映射逻辑节点。
![image-mapper-6](https://main.qcloudimg.com/raw/93c5ec9dcf27ca87425404c5ab7ce2be/image-mapper-6.png)
![image-mapper-7](https://main.qcloudimg.com/raw/dea79a5672dd60e75edb9de0afdd981f/image-mapper-7.png)


#### 从状态存储中查找
可以配置从 mapState、valueState、tableState 中查找数据，以 mapState 为例说明。
![image-mapper-8](https://main.qcloudimg.com/raw/c2ca9a56943da17a875da0865b8ddfc4/image-mapper-8.png)
![image-mapper-9](https://main.qcloudimg.com/raw/cad0aeff67e55a841bacc9a2d829656b/image-mapper-9.png)

#### 通过连接器查找
支持通过连接器来查找第三方数据，然后在映射节点内部使用。
![image-mapper-10](https://main.qcloudimg.com/raw/32eb9450f0ebd47e3e62364cd49602dd/image-mapper-10.png)
![image-mapper-11](https://main.qcloudimg.com/raw/486298c6e8c15b66e7e69c081b03258f/image-mapper-11.png)

#### 从其他流中查找
支持从其他流来获取数据，然后在映射节点内使用。
![image-mapper-12](https://main.qcloudimg.com/raw/9e8e402eec47192e6bdbdfda377efee2/image-mapper-12.png)
![image-mapper-13](https://main.qcloudimg.com/raw/3ed91dd138b31413cc5217f491f1044d/image-mapper-13.png)
![image-mapper-14](https://main.qcloudimg.com/raw/cacadc0b2434f44bc181f3edc0cadbd7/image-mapper-14.png)

#### 通过表达式配置
支持通过表达式来转换数据。
![image-mapper-15](https://main.qcloudimg.com/raw/464cd42d7843f05d978c3bfef865e67c/image-mapper-15.png)
![image-mapper-16](https://main.qcloudimg.com/raw/1b8357546963b0b683af4c567e6a3dee/image-mapper-16.png)


## 案例
针对一个学生表进行转换，示例图如下。
![image-mapper-17](https://main.qcloudimg.com/raw/78c6b012ca0682c2eba5df39d87def1b/image-mapper-17.png)
1. 用 RecordSet Encoder 组件创建一个学生表，包含`name, age, address, socre, adult`字段，然后在 RecordSet Encoder 组件里添加 SetPayload 组件，用表达式给学生表添加一些数据。
![image-mapper-18](https://main.qcloudimg.com/raw/8aaee48533e8e08584b9f90398f4eabf/image-filter-9.png)
![image-mapper-19](https://main.qcloudimg.com/raw/56030c67630074aee8488fba756eae02/image-filter-10.png)
2. 用 Mapper 组件进行转换，生成一个新的学生表，包含`code, name, company, homeAddress, isAdult`5个字段，Mapper 组件的整体配置视图如下。
![image-mapper-18](https://main.qcloudimg.com/raw/47216a15709b2dbd7dc40f68c8720db8/image-mapper-18.png)
 - 用表达式转换节点来处理输入信息中的`name, age, score`，然后赋值给输出信息中的`code, name`，配置信息如下。
![image-mapper-19](https://main.qcloudimg.com/raw/50b3fa040b4aa046008cc7a4231dcf60/image-mapper-19.png)
 - 输出信息中的`company`直接设置为常量 gameloft。
 - 输出信息中的`homeAddress`直接设置为表达式 `return "my home: "+msg.payload["address"]`。
 - 输入信息中的`adult`直连输出信息中的`isAdult`。
3. 在调试模式下进行单元测试，并查看结果即可。

