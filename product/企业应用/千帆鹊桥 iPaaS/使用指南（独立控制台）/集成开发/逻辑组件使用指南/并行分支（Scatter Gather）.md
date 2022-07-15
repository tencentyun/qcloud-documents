## 简介
并行分支（Scatter Gather）支持并行执行多个任务。 该组件中，可以添加多个分支，每个分支中都可以配置子流以独立执行任务。

## 操作配置

### 参数配置

| 参数    | 数据类型   | 描述                                                                                                                                                                 | 是否必填 | 默认值         |
|:------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----|-------------|
| 最大并行数 | int    | 并行执行的任务数，取值范围为2~8。实际并行数取分支数和最大并行数之间较小值                                                                                                                             | 是    | 4           |
| 根信息   | string | 根信息是一个变量，这里填入变量名称，根信息中保存了主流的Message信息。msg.vars.get('#根信息名称#').payload即可访问主流的payload数据。当使用默认值rootMessage时，使用msg.vars.get('rootMessage').payload即可在子流中访问主流的payload数据 | 是    | rootMessage |

### 配置界面

![img_26.png](https://qcloudimg.tencent-cloud.cn/raw/fb9e0d4cdeac2bd4a6b25d924456c805.png)

### 数据预览
无

### 输入到子流中的 Message

| Message 属性 | 值                        |
|-----------|--------------------------|
| payload   | 继承主流 Message 中的 payload 信息   |
| error     | 空                        |
| attribute | 继承主流 Message 中的 attribute 信息 |
| variable  | 集成主流的变量                  |

### 输出

并行分支的输出结果中，不会包含处理逻辑中使用的 variable 变量，最终输出的只有 payload 里的数据。
输出的 payload 是 dict 类型变量，里边汇总了各分支处理的结果。

组件输出的 Message 信息如下：

| Message 属性 | 值                                                                                                |
|-----------|--------------------------------------------------------------------------------------------------|
| payload   | dict 类型，key 是分支的编号，从"1"开始，value 是分支执行完成后的结果（最后一个组件输出的Payload）                                       |
| error     | <ul><li>执行成功后，error 为空</li><li>执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息</li></ul> |
| attribute | 不改变输入 attribute                                                                                   |
| variable  | 不改变输入变量                                                                                          |

## 案例

当需要并行执行不同的任务时，使用并行分支比较合适。例如：要根据用户订单数据，去查询客户信息及产品信息，可以配置两个分支，一个执行客户信息查询，一个执行产品信息查询。

1. 添加并行分支组件，添加2个分支，配置默认即可。
   ![img_27.png](https://qcloudimg.tencent-cloud.cn/raw/009a52bf38d251a4c5abf6bf2c110e63.png)
2. 第一个分支配置客户信息查询，第二个分支配置产品信息查询，这里用两个简单的 HTTP 请求模拟。
   ![img_28.png](https://qcloudimg.tencent-cloud.cn/raw/74e0d999634b0e327af3ee565876f963.png)
3. 执行完成后查看并行分支的输出，切换到专家模式，可以看到 Payload 为包含2个 key 的字典。
key "1"代表分支1的结果，即查询到的客户信息；key "2"代表分支2的结果，即查询到的产品信息。
   ![img_29.png](https://qcloudimg.tencent-cloud.cn/raw/4c295691dc2538eefb9d84a651a24956.png)
