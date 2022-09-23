## 简介

配置 Payload（Set Payload）可以设置 message 中的 payload 属性。支持表达式和字面量两种输入形式，如果是字面量形式，需要先选择数据类型，再在输入框中填入字面量。如果需要输入表达式，选择 any 类型，写入表达式即可。

## 操作配置

### 参数配置

| 参数 | 数据类型 | 描述                  | 是否必填 | 默认值 |
| --- | ------- | -------------------- | ------- | ------ |
| 值   | any      | payload 中要保存的数据 | 是       | 无     |

### 配置界面
![image-20210325155210080](https://qcloudimg.tencent-cloud.cn/raw/774471abbf9307ef28b712e7a7281992.png)

### 输出

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 用户填入的数据                                               |
| error       | <ul><li>执行成功后，error 为空</li><li>执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息</li></ul> |
| attribute   | 继承上个组件的 attribute 信息                                  |
| variable    | 继承上个组件的 variable 信息                                   |

### 数据预览
<img src="https://qcloudimg.tencent-cloud.cn/raw/a93e9f4e885a5258dd6c7917cf0b4170.png" alt="https://qcloudimg.tencent-cloud.cn/raw/a93e9f4e885a5258dd6c7917cf0b4170.png" style="zoom:50%;" />

## 案例

1. 添加 Set Payload 组件。
   ![image-20210330173057043](https://qcloudimg.tencent-cloud.cn/raw/22c8b774530626f1f1dfcdc4dc24587f.png)
2. 填入要设置的数据。
   ![image-20210330173121330](https://qcloudimg.tencent-cloud.cn/raw/9fb13c4332cd9215db9581225a269dce.png)
