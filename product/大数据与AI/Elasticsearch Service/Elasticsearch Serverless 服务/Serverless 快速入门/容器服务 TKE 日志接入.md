## 前提条件
已创建腾讯云账号，创建账号可参考 [注册腾讯云](https://cloud.tencent.com/document/product/378/17985)。
如使用子账号登录，请确保该账号具备 ES 的读写权限。

## 操作步骤
### 登录控制台
1. 登录 [ES 控制台](https://console.cloud.tencent.com/es)。
2. 在顶部菜单栏，选择地域，当前已支持北京、上海、广州、南京地域。
3. 在左侧导航栏 Serverless 模式下选择**日志分析**。


### 创建项目空间
1. 单击**项目空间管理 > 新建空间**。
2. 输入项目空间名称，支持1-20个中文、英文、数字、下划线或分隔符"-"。
3. 单击**确认**，校验无误即可成功创建项目空间。
![](https://qcloudimg.tencent-cloud.cn/raw/0a2e62e549be4ff057a3de37c0dcac38.png)

>? 在 Elasticsearch Serverless 日志分析中，您可仅 [创建索引](https://cloud.tencent.com/document/product/845/90392)，后续通过 API 进行数据写入或者在对应索引的“数据接入”Tab 页进行 CVM 或 TKE 等数据源接入。您也可在创建索引时同时进行数据接入，完成一站式的 CVM 日志接入、TKE 日志接入。以下为您介绍一站式的 TKE 日志接入操作。

### TKE 日志接入
在 Serverless 日志分析首页选择**容器服务TKE**，进入TKE 日志接入页面。
![](https://qcloudimg.tencent-cloud.cn/raw/fcaef07f387120a6e7c3235c6f6ecbc2.png)

#### 数据接入
数据源以及采集设置：
- 私有网络 VPC：必选。TKE 集群所在的私有网络。
- 待采集 TKE 集群 ID：必选。需采集的 TKE 集群的 ID，TKE 集群需要是运行中状态且为标准集群。
- 命名空间：必选。第一个下拉可选择 包含/不包含。第二个下拉可选择命名空间，支持多选，不支持选择不包含全部命名空间。
- Pod 标签：选填。支持创建多个 Pod 标签，标签之间是逻辑 与 关系。
- 容器名称：选填。填写的容器名称必须在采集目标集群及命名空间之下，为空时，Filebeat 会采集命名空间下符合 Pod 标签的全部容器。

![](https://qcloudimg.tencent-cloud.cn/raw/137179aa8955da443a1aff3d5246f81c.png)

#### 索引设置
- 索引名称：长度为1-100，支持小写字母,数字, -, _, ;, @, &, =, !, ', %, $, ., +, (, )。
- 所属项目空间：该索引所在的项目空间，您可将同一个业务的索引都归属到某个项目空间下以便于管理。
- 可用区及子网：索引网络所在的可用区及子网（私有网络 VPC 默认与容器服务 TKE 一致）。
- 存储时长：您可设置数据的存储时长，默认选择存储30天，同时也支持设置为永久保存。

![](https://qcloudimg.tencent-cloud.cn/raw/ed43cbde06fc0effb10ecf8626c1045c.png)


#### 高级设置
- **用户名密码**
该用户名密码用于 ES 登录认证以及 Kibana 访问。
	- 默认开启**系统默认**，将自动生成索引的用户名密码，密码可在后续索引访问控制中进行修改。
	- 选择**自定义**，用户名长度为1-30个字符，支持英文、数字、下划线" _ "和分隔符" - "，密码长度为8到20位，需包括大写字母、小写字母、数字和符号（如 -!@#$%&^*+=_:;,.? 等）四类中的三类。

- **Kibana 公网访问 IP**
Kibana 公网访问 IP 白名单，用于标识允许哪些 IP 访问 Kibana，勾选后，平台将自动将当前 IP 地址加入到白名单中，您也可在索引创建完成后，在**基础信息 > 访问控制**模块自行设置。

![](https://qcloudimg.tencent-cloud.cn/raw/143a4b547c42800237aa1988f66f62a0.png)
