## 背景说明
云函数是腾讯云为企业和开发者们提供的无服务器执行环境，具体可参见 [云函数 SCF](https://cloud.tencent.com/product/scf)，下文简称 SCF。

CDW 常见使用场景是将消息中间件的信息同步到 CDW 后再进行分析。本文提供了一种便捷的方法，即使用 SCF 实时的将 Kafka 中的数据导入到 CDW，无需用户维护任何服务。

## 注意事项
- 该云函数目前只能将腾讯云 CKafka 作为数据源，暂不支持自建 Kafka。
- 该云函数目前只能将 CDW 中的某一张表作为目标数据写入，如果有多张表的需求，请按照以下流程每张表创建对应的云函数。

## 使用步骤
1. 创建函数
【运行环境】选择“Python3.6”，【模糊搜索】关键词“ckafka”，选择模板函数“CKafka 数据加载到 CDW”，如下图所示：
![](https://main.qcloudimg.com/raw/70e55179550b09935832dd996dbac934.png)
2. 配置函数
函数配置过程，如下图所示：
![](https://main.qcloudimg.com/raw/ddf1c9b61872c38bc06e3249c26202c5.png)
 - 内存：这个根据实际运行情况来设置，如果在导入过程中出现内存不足的错误，就需要把该参数调大，默认是128MB
 - 环境变量：
 
| 参数         | 必填 | 说明                            |
 | ------------ | ---- | --------------------------------------- |
 | DB_DATABASE  | 是   | 数据库名           |
 | DB_HOST  | 是   | 如果函数是私有网络，并且和 CDW 是在同一子网，则可以填写 CDW 的内网 IP，否则需要填写外网 IP，并配置白名单           |
 | DB_USER  | 是   | 用户名           |
 | DB_PASSWORD  | 是   | 用户密码        |
 | DB_SCHEMA  | 是   | 模式名，如果创建表的时候未指定，通常是 public          |
 | DB_TABLE  | 是   | 表名           |
 | DB_PORT  | 否   | CDW 端口，默认为5436           |
 | MSG_SEPARATOR  | 否   | CKafka 中消费的分隔符，默认为逗号，也就是 csv 格式           |
 
 - 网络：建议启用私有网络，并将 VPC 与子网的值配置与 CDW 相同，如下图为 CDW 对应的值。
 
![](https://main.qcloudimg.com/raw/69f95bd32b0a9057f9880dd6bf22e859.png)

3. 配置触发管理
触发器配置过程，如下图所示：
![](https://main.qcloudimg.com/raw/3ad13178a24acf0e9a5cee2d630b3457.png)

关于触发器参数配置可以参考 [CKafka 触发器](https://cloud.tencent.com/document/product/583/17530)。
