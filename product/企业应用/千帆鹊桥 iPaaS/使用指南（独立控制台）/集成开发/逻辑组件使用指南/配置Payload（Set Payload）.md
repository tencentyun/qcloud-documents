### 配置Payload（Set Payload）

#### 1. 简介

Set Payload可以设置message中的payload属性。支持表达式和字面量两种输入形式，如果是字面量形式，需要先选择数据类型，再在输入框中填入字面量。如果需要输入表达式，选择any类型，写入表达式即可

#### 2. 操作配置

##### 参数配置

| 参数 | 数据类型 | 描述                  | 是否必填 | 默认值 |
| :--- | :------- | :-------------------- | :------- | ------ |
| 值   | any      | payload中要保存的数据 | 是       | 无     |

##### 配置界面
![image-20210325155210080](https://qcloudimg.tencent-cloud.cn/raw/774471abbf9307ef28b712e7a7281992.png)

##### 输出

组件输出的message信息如下：

| message属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 用户填入的数据                                               |
| error       | 执行成功后，error为空；执行失败后，error为dict类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息 |
| attribute   | 继承上个组件的attribute信息                                  |
| variable    | 继承上个组件的variable信息                                   |
##### 数据预览
<img src="https://qcloudimg.tencent-cloud.cn/raw/a93e9f4e885a5258dd6c7917cf0b4170.png" alt="https://qcloudimg.tencent-cloud.cn/raw/a93e9f4e885a5258dd6c7917cf0b4170.png" style="zoom:50%;" />
#### 3. 案例

1. 添加Set Payload组件

   ![image-20210330173057043](https://qcloudimg.tencent-cloud.cn/raw/22c8b774530626f1f1dfcdc4dc24587f.png)

2. 填入要设置的数据

   ![image-20210330173121330](https://qcloudimg.tencent-cloud.cn/raw/9fb13c4332cd9215db9581225a269dce.png)
