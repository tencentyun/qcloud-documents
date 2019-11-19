
## 搜索服务

搜索服务广泛地存在于我们身边，例如我们生活中用的百度，工作中用的wiki搜索，淘宝时用的商品搜索等，这些场景的数据具有数据量大、结构化、读多写少等特点，而传统的数据库的事务特性在搜索场景并没有很好的使用空间，并且在全文检索方面速度慢（如like语句）。因此，Elasticsearch应运而生。

Elasticsearch是一个广泛应用于全文搜索领域的开源搜索引擎，它可以快速地索引、搜索和分析海量的文本数据。腾讯云ES是基于Elasticsearch构建的高可用、可伸缩的云端托管Elasticsearch服务，对结构化和非结构化的数据都有良好的支持，同时还提供了简单易用的 RESTful API 和各种语言的客户端，方便快速搭建稳定的搜索服务。

本文将针对搜索场景，使用《[腾讯云ES官方文档](https://cloud.tencent.com/document/product/845)》作为语料，介绍如何使用腾讯云ES+SCF快速搭建搜索服务。先贴一个搜索服务界面：

![image](https://main.qcloudimg.com/raw/c837b6b478b53cc821765588a9403744.png)

## 资源准备

只需要一个ES集群！在腾讯云购买一个ES集群，集群的规模根据搜索服务的QPS和存入的文档的数据量而定。具体可以参考《[节点类型存储配置建议](https://cloud.tencent.com/document/product/845/19551)》

## 部署搜索服务

我们使用腾讯云**免费**的SCF工具部署搜索服务的前端界面和后台服务

1. 在云函数->[函数服务界面](https://console.cloud.tencent.com/scf/list?rid=1&ns=default)左上角首先选择你购买ES集群的地域
 
    ![image](https://main.qcloudimg.com/raw/d98dcd24f674935914871be83aaddb73.png)
 
1. 新建一个函数服务，**记住你设置的函数名称哦**，然后点击下一步 -> 完成

    ![image](https://main.qcloudimg.com/raw/c9ff79b265643115d55ca073b8249ed5.png)
    
1. 在**函数配置**界面点击右上角的**编辑**，开启**内网访问**，并选择你创建ES所选的VPC，然后点击保存

    ![image](https://main.qcloudimg.com/raw/17c97bb43e97c3a98cf465bff8203a4f.png)
    
1. 首先将[代码zip包](https://es-bot-1254139681.cos.ap-guangzhou.myqcloud.com/myserver.zip)下载到本地。然后在**函数代码**界面的**提交方法**中选择上传本地zip包，并选择刚下载的zip包，点击保存：

    ![image](https://main.qcloudimg.com/raw/0585fdb55356ee2e81d015d32f567e9a.png)
    
1. 在**函数代码**界面修改代码。需要修改的文件有`index.py`和`index.html`：

    * `index.py`中的`es_endpoint`修改为你的ES集群的内网地址，填写格式如：`http://10.0.3.14:9200`
    
    * `index.py`中的`es_password`修改为白金版ES密码，如果不是白金版则不修改
    
    * `index.html`中的`server_name`修改为你创建的SCF函数的函数名称，默认为`myserver`

    ![image](https://main.qcloudimg.com/raw/92e0188267f8e15c7ae507002a0124e3.png)
    
    ![image](https://main.qcloudimg.com/raw/c035a9fc3a4247230ad2b1cc49e9f253.png)
    
    **【注意】样例默认使用`es_corpus_0126`作为索引名，请确保样该索引没有业务在使用，如需修改，可在`index.py`中修改`es_index`变量**
    
1. 在**触发方式**界面点击“添加触发方式”，按截图所示添加API网关触发器，并启用集成响应，然后点击保存

    ![image](https://main.qcloudimg.com/raw/531aea97319ee8705d2fb3bce6f57ab1.png)

1. 可以在**触发方式**中看到函数的“访问路径”，点击这个路径就可以访问页面了

    ![image](https://main.qcloudimg.com/raw/f3fe6be8f20aff7506890ad883427ca9.png)

1. 上传《[腾讯云ES官方文档](https://cloud.tencent.com/document/product/845)》样例数据。点击搜索框上方的文字，自动导入数据

    ![image](https://main.qcloudimg.com/raw/0db08312785053527dc5b3935d7ce1b5.png)

1. 至此，一个基于腾讯云ES的简单的问答搜索服务后台就部署完成了。开始你的搜索之旅吧！

## 了解更多

### 停用词和用户词典导入

停用词不会被ES检索；用户词典在分词的时候将保留该词。在上面的案例中，我们导入了默认的[停用词库](https://es-bot-1254139681.cos.ap-guangzhou.myqcloud.com/stopwords.dic)和[用户词典](https://es-bot-1254139681.cos.ap-guangzhou.myqcloud.com/user_dict.dic)，你也可以通过ES集群详情页->高级配置->更新词典导入自己的停用词和用户词典

![image](https://main.qcloudimg.com/raw/ab9410ad5485ae8f279558606de6510f.png)

### 同义词配置

同义词配置需要在创建索引时指定，支持Solr和WordNet两种同义词格式，可以参考《[Solr synonyms](https://www.elastic.co/guide/en/elasticsearch/reference/6.4/analysis-synonym-tokenfilter.html#_solr_synonyms)》对格式的介绍