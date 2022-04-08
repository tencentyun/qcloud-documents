## 简介
GooseFS 日志上报功能支持将 GooseFS 运行日志上报到腾讯云的日志服务（Cloud Log Service，CLS）或 Elasticsearch Service（ES）中。本文将介绍如何将 GooseFS 的运行日志上报到这两种日志系统中。

## 准备工作

部署 GooseFS 集群，GooseFS 的部署请参考 [GooseFS 部署指南](https://cloud.tencent.com/document/product/436/57223)。


## 上报日志

### GooseFS 上报日志到 CLS

#### 创建 CLS 主题

GooseFS 日志上报依赖于第三方采集系统平台，此处以 CLS 为例进行说明。

创建 CLS 主题，详情请参见 [CLS 一分钟入门指南](https://cloud.tencent.com/document/product/614/55242)。

#### 配置 filebeat

1. 配置日志采集目录，编辑 GooseFS 部署根目录下的 $GOOSEFS_HOME/conf/filebeat.yml 文件。
```
- type: log
  enabled: true
  paths:
    - ${path.home}/../logs/job_master.log* 
    
  fields:
    type: "master"
  exclude_files: ['.gz$']

  multiline.pattern: '^[[:space:]]+(at|\.{3})[[:space:]]+\b|^Caused by:'
  multiline.negate: false
  multiline.match: after
```
>?
>- paths：配置要采集的日志路径，多个日志文件使用通配符`*`。
>- fields.type：自定义类型名。
>- multiline.pattern：多行合并规则。
2. 配置 CLS 日志采集平台账号。
```
output.kafka:
  hosts: ["sh-producer.cls.tencentcs.com"]
  topic: "a99cf1de-81d4-47a-97xxxxx-xxxx"
  version: "0.11.0.0"
  compression: "none"
  username: "cc098474-b387-381xxxx-xxxxx"
  password: "secretId#secretKey"
```
>?
>- hosts：CLS 平台的可用地域。
>- topic：CLS 平台创建日志主题时分配的日志主题 ID。
>- version：CLS 平台服务支持 kafka 的版本，默认值：0.11.0.0。
>- username：CLS 平台创建日志主题时分配的日志集 ID。
>- password：SecretId#SecretKey，SecretId 和 SecretKey 是云管理账号下 App 密钥管理中分配的密钥。
>
3. 进入 $GOOSEFS_HOME/filebeat 目录，执行如下命令，启动 filebeat。
```
./goosefs-filebeat -c filebeat.yml
```
4. filebeat 启动完成之后，会实时采集 GooseFS 服务产生的日志上报到 CLS 平台，通过 CLS 平台可以查看具体上报的日志信息。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/6e1110050db635fe8523fa0d4bf76255.png)

### GooseFS 上报日志到 ES

#### 创建 ES

GooseFS 日志上报依赖于第三方采集系统平台，下面以 ES 为例进行说明：
- 创建 ES 集群，具体创建方式请参见：[创建 ES 集群](https://cloud.tencent.com/document/product/845/19536)。
- 访问 ES 集群，具体访问方式请参见：[访问 ES 集群](https://cloud.tencent.com/document/product/845/19537)。

#### 配置 filebeat
1. 配置日志采集目录，编辑 GooseFS 部署根目录下的 $GOOSEFS_HOME/conf/filebeat.yml 文件。
```
- type: log
  enabled: true
  paths:
    - ${path.home}/../logs/job_master.log* 
    
  fields:
    type: "master"
  exclude_files: ['.gz$']

  multiline.pattern: '^[[:space:]]+(at|\.{3})[[:space:]]+\b|^Caused by:'
  multiline.negate: false
  multiline.match: after
```
>?
>- paths：配置要采集的日志路径，多个日志文件使用通配符`*`。
>- fields.type：自定义类型名。
>- multiline.pattern：多行合并规则。
>
2. 配置 ES 日志采集平台账号。
```
output.elasticsearch:
  # Array of hosts to connect to.
  hosts: ["es-nli7xxxxx.public.tencentelasticsearch.com"]

  protocol: "https"

  # Authentication credentials - either API key or username/password.
  #api_key: "id:api_key"
  username: "elasticxxx"
  password: "costestxxx"

  index: "GooseFS-%{[fields.type]}-%{+yyyy.MM.dd}"
```
>?
>- hosts：ES 对外提供服务地址。
>- username：ES 登录用户名。
>- password：ES 登录密码。
>- index：ES 日志输出索引。例如，master 的 index 是 GooseFS-master-2022.01.18，worker 的 index 是 GooseFS-worker-2022.01.18等。
>
3. 进入 $GOOSEFS_HOME/filebeat 目录，执行如下命令，启动 filebeat。
```
./goosefs-filebeat -c filebeat.yml
```
4. filebeat 启动完成后，会实时采集 GooseFS 服务产生的日志上报到 ES 平台，通过 ES 平台可以查看具体上报的日志信息，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/485e670cdc4360d52397919140a6cd3a.png)

### 开启 GooseFS 审计日志上报

如果需要上报 GooseFS 服务的审计日志，则需要开启审计日志配置，操作如下：
1. 编辑 GooseFS 部署目录下的 $GOOSEFS_HOME/conf/goosefs-site.properties 文件，添加如下配置项（可选）。
```
goosefs.master.audit.logging.enabled=true
```
2. 执行如下命令，将文件 $GOOSEFS_HOME/conf/goosefs-site.properties 拷贝到所有 worker 节点。
```
goosefs copyDir conf/
```
3. 启动 GooseFS 集群。
```
./bin/goosefs-start.sh all
```
