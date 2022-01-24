GooseFS 日志上报功能

## GooseFS 日志上报介绍
GooseFS 日志上报功能支持将 GooseFS 运行日志上报到腾讯云的日志服务（CLS）或 Elasticsearch 中。本文将介绍如何将 GooseFS 的运行日志上报到这两种日志系统中。

## 准备工作

### 部署 GooseFS 集群
GooseFS 的部署请参考：[GooseFS 部署指南](https://cloud.tencent.com/document/product/436/57223)

### GooseFS 上报日志到 ES
#### 创建 ES
GooseFS 日志上报依赖于第三方采集系统平台，下面以 Elasticsearch Service（简称：ES）为例说明：
- 创建 ES 集群，具体创建方式参考：[ES 集群创建](https://cloud.tencent.com/document/product/845/19536)
- 访问 ES 集群，具体访问方式参考：[ES 集群访问](https://cloud.tencent.com/document/product/845/19537)

#### 配置 filebeat
- 配置日志采集目录，编辑 GooseFS 部署根目录下的 $GOOSEFS_HOME/conf/filebeat.yml文件
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
  ------------------------------
  说明：
  paths：配置要采集的日志路径，多个日志文件使用通配符*。
  fields.type：自定义类型名。
  multiline.pattern：多行合并规则。
```

- 配置 ES 日志采集平台账号
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
  ------------------------------
  说明：
  hosts：ES对外提供服务地址。
  username：ES登录用户名。
  password：ES登录密码。
  index：ES日志输出索引。例如：master的index是：GooseFS-master-2022.01.18，worker的index是：GooseFS-worker-2022.01.18等。
```
- 启动 filebeat，进入 GooseFS 部署根目录下的 $GOOSEFS_HOME/filebeat，执行命令：
```
./goosefs-filebeat -c filebeat.yml
```
filebeat 启动完成之后，会实时采集 GooseFS 服务产生的日志上报到 ES 平台，通过 ES 平台可以查看具体上报的日志信息，如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/485e670cdc4360d52397919140a6cd3a.png)

### GooseFS 上报日志到 CLS
#### 创建 CLS 主题
GooseFS 日志上报依赖于第三方采集系统平台，下面以日志服务（Cloud Log Service）（简称：CLS）为例说明：
- 创建 CLS 主题，具体创建方式参考：[CLS 一分钟入门指南](https://cloud.tencent.com/document/product/614/55242)

#### 配置 filebeat
- 配置日志采集目录，编辑 GooseFS 部署根目录下的 $GOOSEFS_HOME/conf/filebeat.yml文件
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
  ------------------------------
  说明：
  paths：配置要采集的日志路径，多个日志文件使用通配符*。
  fields.type：自定义类型名。
  multiline.pattern：多行合并规则。
```

- 配置 CLS 日志采集平台账号
```
output.kafka:
  hosts: ["sh-producer.cls.tencentcs.com"]
  topic: "a99cf1de-81d4-47a-97xxxxx-xxxx"
  version: "0.11.0.0"
  compression: "none"
  username: "cc098474-b387-381xxxx-xxxxx"
  password: "secretId#secretKey"
  ------------------------------
  说明：
  hosts：CLS 平台的可用地域。
  topic：CLS 平台创建日志主题时分配的日志主题ID。
  version：CLS 平台服务支持 kafka 的版本，默认值：0.11.0.0。
  username：CLS 平台创建日志主题时分配的日志集ID。
  password：SecretId#SecretKey，SecretId和SecretKey是云管理账号下 APP密钥管理 中分配的密钥。
```
- 启动 filebeat，进入 GooseFS 部署根目录下的 $GOOSEFS_HOME/filebeat，执行命令：
```
./goosefs-filebeat -c filebeat.yml
```
filebeat 启动完成之后，会实时采集 GooseFS 服务产生的日志上报到 CLS 平台，通过 CLS 平台可以查看具体上报的日志信息，如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/6e1110050db635fe8523fa0d4bf76255.png)

### 开启 GooseFS 审计日志上报
如果需要上报 GooseFS 服务的审计日志，需要开启审计日志配置，操作如下：
- 编辑 GooseFS 部署目录下的 $GOOSEFS_HOME/conf/goosefs-site.properties文件，添加如下配置项（可选）：
```
goosefs.master.audit.logging.enabled=true
```
- 使用如下命令将文件 $GOOSEFS_HOME/conf/goosefs-site.properties 拷贝到所有 worker 节点
```
goosefs copyDir conf/
```
- 启动 GooseFS 集群
```
./bin/goosefs-start.sh all
```