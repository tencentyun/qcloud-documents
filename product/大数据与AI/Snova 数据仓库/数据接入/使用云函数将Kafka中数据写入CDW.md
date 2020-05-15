## 使用云函数(SCF)将Kafka中的数据写入到云数据仓库(CDW)

### 背景说明
云函数是腾讯云为企业和开发者们提供的无服务器执行环境，具体可参见 [云函数 SCF](https://cloud.tencent.com/product/scf)，下文简称SCF。

将消息中间件的信息同步到CDW在进行分析，是CDW比较常见的使用场景，本文提供了一种便捷的方法，使用SCF准实时的将Kafka中的数据导入到CDW，而无需用户维护任何服务。

### 注意事项
1. 该云函数目前只能将腾讯云CKafka作为数据源，暂不支持自建Kafka。
2. 该云函数目前只能将CDW中的某一张表作为目标数据写入，如果有多张表的需求，请按照以下流程每张表创建对应的云函数。

### 使用步骤
1. 创建函数

运行环境选择 "Python3.6"， 搜索关键词 "ckafka"，选择模板函数 "CKafka数据加载到CDW"，如下图所示：

![](https://main.qcloudimg.com/raw/70e55179550b09935832dd996dbac934.png)


2. 配置函数
函数配置过程，如下图所示：

![](https://main.qcloudimg.com/raw/9358c232f22ded7f1b8b8fe5f32cb7b9.png)

 - 内存：这个根据实际运行情况来设置，如果在导入过程中出现内存不足的错误，就需要把该参数调大，默认是128MB
 - 环境变量：
 
 | 参数         | 必填 | 说明                            |
 | ------------ | ---- | --------------------------------------- |
 | DB_DATABASE  | 是   | 数据库名           |
 | DB_HOST  | 是   | 如果函数是私有网络，并且和CDW是在同一子网，则可以填写CDW的内网IP，否则需要填写外网IP，并配置白名单           |
 | DB_USER  | 是   | 用户名           |
 | DB_PASSWORD  | 是   | 用户密码        |
 | DB_SCHEMA  | 是   | 模式名，如果创建表的时候未指定，通常是public          |
 | DB_TABLE  | 是   | 表名           |
 | DB_PORT  | 否   | CDW端口，默认为5436           |
 | MSG_SEPARATOR  | 否   | CKafka中消费的分隔符，默认为逗号，也就是csv格式           |
 
 - 网络：建议启用 私有网络，并将vpc与子网的值配置与CDW相同，如下图为CDW对应的值
 
![](https://main.qcloudimg.com/raw/e988ccea354220fb2e2bd021e24c46f9.png)

3. 配置触发管理
触发器配置过程，如下图所示：

![](https://main.qcloudimg.com/raw/491fd215c31cbe491b862d8d81d7693d.png)

关于触发器参数配置可以参考 [CKafka触发器](https://cloud.tencent.com/document/product/583/17530)
