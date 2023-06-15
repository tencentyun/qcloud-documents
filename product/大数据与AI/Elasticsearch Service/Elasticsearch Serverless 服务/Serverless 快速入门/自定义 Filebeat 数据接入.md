## Beats 管理-CVM 日志接入
登录 Elasticsearch Service 控制台[ Beats管理 ](https://console.cloud.tencent.com/es/beats) 界面，授权服务相关角色， 在 Filebeat 采集器选择 CVM 日志采集 。
![](https://qcloudimg.tencent-cloud.cn/raw/8e3863377fda25d0cc15ba399482e821.png)
在创建 Filebeat 采集器中，设置采集器信息：
- 采集器名称：自定义采集器的名称，格式为1个 - 50个英文、汉字、数字、连接线（-）或下划线（_）。
- 采集器输出：选择 Serverless 索引，同时选择项目空间及输出的索引名称。
- 用户名密码：Serverless 索引默认开启用户登录认证，您需要填写用户名和密码，使得 Filebeat 有权限向 Serverless 索引中写入数据。用户名默认填充，密码为创建索引时设置，可在索引基础信息页面的访问控制模块中获取。
- 采集器 YML 配置：配置内容如下，更多 YML 配置请参考 [官方文档](https://www.elastic.co/guide/en/beats/filebeat/current/configuration-filebeat-options.html)。
    - type：输入类型，默认为 log，还有 tcp、syslog、stdin 等可选。
    - paths：日志文件路径，需要填写为 CVM 中日志文件的绝对路径。
    - enabled：是否启用该 input 配置，true 为启用，false 则为不启用。

![](https://qcloudimg.tencent-cloud.cn/raw/40cdc0f520dbc441874b977778ae62be.png)
将采集器安装到 CVM 实例，步骤如下：
- 选择要安装采集器的 CVM 实例，完成后单击确定启用。CVM 必须安装自动化助手，仅支持为已安装自动化助手的 CVM 实例下发采集器配置。
- 仅支持选择和 Serverless 索引 在同一 VPC 下的 CVM 实例进行安装，若无法找到目标 CVM 实例，需更改采集器输出。

![](https://qcloudimg.tencent-cloud.cn/raw/d88e379ad7717980cd596951384660ab.png)

## Beats 管理-TKE 日志接入
登录 Elasticsearch Service 控制台 [Beats管理 ](https://console.cloud.tencent.com/es/beats) 界面，授权服务相关角色， 在 Filebeat 采集器选择 TKE日志采集 。
![](https://qcloudimg.tencent-cloud.cn/raw/0da8517cdf29bb97c29dcb80d53936f5.png)
在创建 Filebeat 采集器中，设置采集器信息：
- 采集器名称：自定义采集器的名称，格式为1个 - 50个英文、汉字、数字、连接线（-）或下划线（_）。
- 采集器输出：选择 Serverless 索引，同时选择项目空间及输出的索引名称。
- 用户名密码：Serverless 索引默认开启用户登录认证，您需要填写用户名和密码，使得 Filebeat 有权限向 Serverless 索引中写入数据。用户名默认填充，密码为创建索引时设置，可在索引基础信息页面的**访问控制**模块中获取。

![](https://qcloudimg.tencent-cloud.cn/raw/0c47d7ad1f230cac8e06b4104e525ac8.png)
配置采集来源，步骤如下：
- 所在私有网络 VPC：默认使用上一步采集器输出中 Serverless 索引 的 VPC，且不可更改。
- 待采集 TKE 集群 ID：必选。需采集的 TKE 集群的 ID，TKE 集群需要是运行中状态且为标准集群。
- 命名空间：必选。第一个下拉可选择 包含/不包含。第二个下拉可选择命名空间，支持多选，不支持选择不包含全部命名空间。
- Pod 标签：选填。支持创建多个 Pod 标签，标签之间是逻辑 与 关系。
- 容器名称：选填。填写的容器名称必须在采集目标集群及命名空间之下，为空时，Filebeat 会采集命名空间下符合 Pod 标签的全部容器。
- 日志内容过滤：选填。根据关键字过滤日志，可填多个关键字，以逗号分隔。
- 高级采集配置：选填。个性化设置解析方式、过滤等，一般采用默认配置，详情请参考 [官方文档 ](https://www.elastic.co/guide/en/beats/filebeat/7.17/defining-processors.html)。

![](https://qcloudimg.tencent-cloud.cn/raw/a821c95e70c1d146bbe69663338a4ee3.png)


## 自建 Filebeat 数据采集
**版本说明**
仅支持7.10.2或者7.14.2的 Filebeat 版本。
<table >
<tr>
<th width>类别</th>
<th width>参数项</th>
<th width>参数描述</th>
<th width>填写说明</th>
</tr>
<tr>
<td rowspan="3">Elasticsearch template setting</td>
<td width>setup.template.enabled</td>
<td width>索引模板</td>
<td width>布尔类型，设置为 false，目前不支持设置</td>
</tr>
<tr>
<td width>setup.ilm.enabled</td>
<td width>索引生命周期管理</td>
<td width>布尔类型，设置为 false，目前不支持设置</td>
</tr>
<td width>allow_older_versions</td>
<td width>对 ES 的版本兼容性</td>
<td width>布尔类型，可设为“true”或者是“false”</td>
</tr>
<tr>
<td rowspan="2">output</td>
<td width>protocol</td>
<td width>数据传输协议</td>
<td width>字符串类型，默认为“http”，支持设置为“https”</td>
</tr>
<tr>
<td width>hosts</td>
<td width>索引内网访问地址</td>
<td width>数组类型，如 protocol 选择为“http”，则端口号为80，例如可设置为：[“http://index-xxx.qcloudes.com:80”]；
如 protocol 选择为“https”，则端口号为443，如[“https://index-xxx.qcloudes.com:443”]
</td>
</tr>
</table>

**配置说明**
```
# ============================== Filebeat inputs ===============================

filebeat.inputs:
- type: log
  # Change to true to enable this input configuration.
  enabled: true
  # Paths that should be crawled and fetched. Glob based paths.
  paths:
    - /var/log/*.log
# ============================== Filebeat modules ==============================

filebeat.config.modules:
  # Glob pattern for configuration loading
  path: \${path.config}/modules.d/*.yml

  # Set to true to enable config reloading
  reload.enabled: false

  # Period on which files under path should be checked for changes
  #reload.period: 10s

# ======================= Elasticsearch template setting =======================
setup.template.enabled: false
setup.ilm.enabled: false
  #template setting's value is set to false by default. If you set it to true, an error will be reported when the configuration is submitted


# ================================== General ===================================

# The name of the shipper that publishes the network data. It can be used to group
# all the transactions sent by a single shipper in the web interface.
#name:

# The tags of the shipper are included in their own field with each
# transaction published.
#tags: ["service-X", "web-tier"]

# Optional fields that you can specify to add additional information to the
# output.
#fields:
#  env: staging

# ================================= Processors =================================
processors:
  - add_host_metadata:
      when.not.contains.tags: forwarded

# ================================== Logging ===================================

# Sets log level. The default log level is info.
# Available log levels are: error, warning, info, debug
#logging.level: debug

# At debug level, you can selectively enable logging only for some components.
# To enable all selectors use ["*"]. Examples of other selectors are "beat",
# "publisher", "service".
#logging.selectors: ["*"]
############################# output ######################################
output.elasticsearch:
  # Array of hosts to connect to.
  allow_older_versions: true
  protocol: "http"
  hosts: ["索引内网访问地址"]

  # Authentication credentials - either API key or username/password.
  username: "your index username"
  password: "your index password"
  indices:
  - index: The_index_name
    when.equals:
      fields.type: log


```




