Angel 是由腾讯自研并开源的高性能分布式机器学习和图计算平台，它提供了用于特征工程、模型构建、参数调优、模型服务和 AutoML 的全栈设施，包括传统机器学习、深度学习、图表示学习和图神经网络等算法。

###  Spark on Angel
凭借 Angel 强大的 PS Service 能力，Spark on Angel 扩展了 Spark 的参数更新能力，使 Spark 也具备高速训练大模型的能力而不用再顾虑 Spark Driver 的单点性能问题。Spark on Angel 组件一般用来运行用户自己实现的算法。

### 图算法
图算法基于 Spark-on-Angel 系统，利用 Angel 对高维稀疏数据的存储能力和 Spark 对海量数据的处理能力，搭建了端到端的图计算平台，为您提供节点测度（PageRank、Kcore、Closeness），社区发现 LPA，FastUnfolding 和图表示学习 LINE，Word2Vec 等算法。

### PyTONA 算法
PyTONA 算法将 Angel 的参数服务器与深度学习系统 PyTorch 相结合，使用户可以在利用 PyTorch 编写最新推荐模型的同时，利用 Angel 参数服务器的扩展性，进行大规模分布式的推荐模型训练。相比于 TensorFlow，Angel 的参数服务器具备处理高维稀疏离散大模型的能力，PyTorch 则更加轻量，更易于进行新模型的尝试。

### 机器学习算法
腾讯云 TI 平台 TI-ONE 还提供基于 Spark on Ange 的机器学习算法，如分类算法等。如果需要运行 Spark on Angel 自带算法，建议您使用各个算法对应的算法组件。 
