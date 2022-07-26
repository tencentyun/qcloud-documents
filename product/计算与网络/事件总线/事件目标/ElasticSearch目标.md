
通过事件规则，您可以将收集到的事件投递到指定的投递目标完成处理与消费，目前事件总线支持 ElasticSearch（以下简称为 ES）作为投递目标，满足后续的分析与数据持久化需求。


## 操作场景
ES 事件目标可以更好地支持 ETL 场景与数据分析场景，尤其是针对日志数据的处理、分析、转储；同时后续能够满足 CSV 等结构化数据交付的需求。


## 主要功能
- 支持自定义事件投递，自定义事件上报方案。
- 支持 ES6、ES7 等不同版本的 ElasticSearch。
- 支持自定义索引名前缀、索引轮换功能，自动生成目标索引名称。
- 针对 DTS 场景，支持自定义 DTS 事件配置。


## 操作指南
在投递目标之前，选择合适的事件集，您可以选择云服务事件集和自定义事件集。
- [云服务事件集](https://cloud.tencent.com/document/product/1359/68200)：用于接收云服务告警、审计等类型事件，如希望配置告警，您需要在该事件集下绑定告警规则。
- [自定义事件集](https://cloud.tencent.com/document/product/1359/69028)：用于接收业务自定义事件，如消息队列事件处理、微服务架构解耦等，需要主动投递事件到对应事件集。

当事件源产生事件后，会根据指定事件规则投递到 ES 事件目标中，进行数据的分析、处理等操作。


### 配置事件集
1. 登录事件总线控制台，选择左侧导航栏中的 [事件集](https://console.cloud.tencent.com/eb)。
2. 单击**新建事件集**，根据页面提示填写相关信息。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/77e2d4af5ef7d4216059ccffec2e1c2e.png)
 - **事件追踪**：需选择**默认投递**，事件总线会自动为您将命中规则但投递失败的事件，上报至指定日志集。
3. 单击**确定**。
4. 在事件集列表页，单击进入已经创建完成的事件集。
5. 在**事件集详情 > 基本信息**中，选择事件连接器右侧的**添加**。
6. 在“新建事件连接器”弹窗中，据页面提示填写相关信息。本文以 [配置 DTS 连接器](https://cloud.tencent.com/document/product/1359/72306) 为例。如下图所示： 
![](https://qcloudimg.tencent-cloud.cn/raw/999f89e87c2f7dc6d0ea6373e4f635f8.png)
 
### 配置事件规则
1. 登录事件总线控制台，选择左侧导航栏中的 [事件集](https://console.cloud.tencent.com/eb)。
2. 在事件集列表页，选择已经创建完成的事件集。
3. 在事件集详情页，单击**管理事件规则**。
4. 在事件规则列表页，单击**新建事件规则**。如下图所示：
![enter image description here](https://qcloudimg.tencent-cloud.cn/raw/715519a283796f6afe64dc3a71290008.png)
	- **事件匹配**：用于事件的过滤筛选。在此处定义何种事件可以被匹配触发，可以配置自定义事件匹配模式，或者选择已有的模板规则。本文选择**数据订阅（DTS)**，即所有来自数据订阅（DTS）的事件都可以通过匹配。所有来自 TDMQ 消息队列的事件都可以通过匹配。
	- **事件目标**：事件最终触发的目标。在绑定投递目标时，本文选择 **Elasticsearch**。
5. 单击**完成**，创建成功后即可在事件规则列表页查看。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/99fe5a391fe0cc0d1b7a707d9ce31c16.png)
 
 

### 流程测试
1. 登录 Mysql 实例，以新建数据表为例。
```
CREATE TABLE IF NOT EXISTS `runoob_tbl`(
   `runoob_id` INT UNSIGNED AUTO_INCREMENT,
   `runoob_title` VARCHAR(100) NOT NULL,
   `runoob_author` VARCHAR(40) NOT NULL,
   `submission_date` DATE,
   PRIMARY KEY ( `runoob_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
```
2. 查看 ES 日志记录。如下图所示：
![enter image description here](https://qcloudimg.tencent-cloud.cn/raw/ab3af686121971a71cd7b6714f59cd59.png)
3. 登录 Kibana 查看记录，投递成功。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/566c8345b3d399494fd47f961b54b15d.png)
