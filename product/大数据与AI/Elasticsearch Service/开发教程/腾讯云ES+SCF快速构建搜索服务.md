## 搜索服务
搜索服务广泛的存在于我们身边，例如我们生活中用的百度、工作中用的 wiki 搜索、淘宝时用的商品搜索等。这些场景的数据具有数据量大、结构化、读多写少等特点，而传统的数据库的事务特性在搜索场景并没有很好的使用空间，并且在全文检索方面速度慢（如 like 语句）。因此，Elasticsearch 应运而生。

Elasticsearch 是一个广泛应用于全文搜索领域的开源搜索引擎，它可以快速地索引、搜索和分析海量的文本数据。腾讯云 ES 是基于 Elasticsearch 构建的高可用、可伸缩的云端托管 Elasticsearch 服务，对结构化和非结构化的数据都有良好的支持，同时还提供了简单易用的 RESTful API 和各种语言的客户端，方便快速搭建稳定的搜索服务。

本文将针对搜索场景，使用腾讯云 ES 官方文档作为语料，介绍如何使用腾讯云 ES+SCF 快速搭建搜索服务。搜索服务界面示例如下：
![image](https://main.qcloudimg.com/raw/c837b6b478b53cc821765588a9403744.png)

## 资源准备
只需要一个 ES 集群。在腾讯云购买一个 ES 集群，集群的规模根据搜索服务的 QPS 和存入的文档的数据量而定。具体可参考 [集群规格和容量配置评估](https://cloud.tencent.com/document/product/845/19551)。

## 部署搜索服务
使用腾讯云**免费**的 SCF 工具部署搜索服务的前端界面和后台服务。
1. 在【云函数】>【[函数服务](https://console.cloud.tencent.com/scf/list?rid=1&ns=default)】界面左上角首先选择您购买 ES 集群的地域。
![](https://main.qcloudimg.com/raw/acff301e0865deeeae3e07de6275127e.png)
2. 新建一个函数服务，**记住您设置的函数名称**，然后选择【下一步】>【完成】。
![](https://main.qcloudimg.com/raw/a95ad851839e032fad804f9840396e80.png)
3. 在**函数配置**页单击右上角的【编辑】，开启**内网访问**，并选择您创建 ES 所选的 VPC，然后单击【保存】。
![](https://main.qcloudimg.com/raw/911af3571ffa69053edfd1a03dfebd19.png)
4. 首先将 [代码 zip 包](https://es-bot-1254139681.cos.ap-guangzhou.myqcloud.com/myserver.zip) 下载到本地。然后在**函数代码**页的**提交方法**中选择上传本地 zip 包，并选择刚下载的 zip 包，单击【保存】。
![](https://main.qcloudimg.com/raw/c8e23480efafc1b7f949271006939b0b.png)
5. 在**函数代码**页修改代码。需要修改的文件有 `index.py` 和 `index.html`：
 - `index.py` 中的 `es_endpoint` 修改为您的 ES 集群的内网地址，填写格式如：`http://10.0.3.14:9200`。
 - `index.py` 中的 `es_password` 修改为白金版 ES 密码，如果不是白金版则不修改。
 - `index.html` 中的 `server_name`修改为您创建的 SCF 函数的函数名称，默认为 `myserver`。
![image](https://main.qcloudimg.com/raw/92e0188267f8e15c7ae507002a0124e3.png)
![image](https://main.qcloudimg.com/raw/c035a9fc3a4247230ad2b1cc49e9f253.png)
>!样例默认使用 `es_corpus_0126` 作为索引名，请确保该索引没有业务在使用。如需修改，可在 `index.py` 中修改 `es_index` 变量。
6. 在**触发方式**页单击【添加触发方式】，按下图添加 API 网关触发器，并启用集成响应，然后单击【保存】。
![](https://main.qcloudimg.com/raw/065c08837097b564c8b7e58032297d32.png)
7. 可在**触发方式**中看到函数的“访问路径”，单击此路径即可访问页面。
![](https://main.qcloudimg.com/raw/b421c38e4f9b4e25a1bd15a04dcce33e.png)
8. 上传 [腾讯云 ES 官方文档](https://cloud.tencent.com/document/product/845) 样例数据。单击搜索框上方的文字，自动导入数据。
![](https://main.qcloudimg.com/raw/d4be7b12ec7a70a565abfb63ca77d967.png)
9. 至此，一个简单的基于腾讯云 ES 的问答搜索服务后台已部署完成。

## 了解更多
### 停用词和用户词典导入
停用词不会被 ES 检索，用户词典在分词时将保留该词。在上面的案例中，我们导入了默认的 [停用词库](https://es-bot-1254139681.cos.ap-guangzhou.myqcloud.com/stopwords.dic) 和 [用户词典](https://es-bot-1254139681.cos.ap-guangzhou.myqcloud.com/user_dict.dic)，您也可以在 ES 集群详情页的【插件列表】>【更新词典】导入自己的停用词和用户词典。
![](https://main.qcloudimg.com/raw/9fdddd0b2e9e58d228412c0db068802e.png)
![](https://main.qcloudimg.com/raw/d0bc4d4f55bf4896cc720f154ef048fc.png)

### 同义词配置
同义词配置需要在创建索引时指定，支持 Solr 和 WordNet 两种同义词格式，具体可参考 [Solr synonyms](https://www.elastic.co/guide/en/elasticsearch/reference/6.4/analysis-synonym-tokenfilter.html#_solr_synonyms) 对格式的介绍。
