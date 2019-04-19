# 算法自动调参
在画布中，组织好某个模型训练的逻辑构建后，可点击上方工具栏的自动调参按钮，启动算法自动调参模式。

https://main.qcloudimg.com/raw/c9865ca18d2e550fe32573c4afcff98a/%E7%AE%97%E6%B3%95%E8%87%AA%E5%8A%A8%E8%B0%83%E5%8F%82%E7%94%BB%E5%B8%83%E6%A6%82%E8%A7%88.jpg

在自动调参的弹窗里，选择需要画布调参的算法，若画布存在多个可调参的算法，请单选一个算法。

https://main.qcloudimg.com/raw/e2365ca90a8c5276e4d153fdda5add00/%E7%AE%97%E6%B3%95%E8%87%AA%E5%8A%A8%E8%B0%83%E5%8F%82%E9%80%89%E6%8B%A9%E8%B0%83%E5%8F%82%E7%AE%97%E6%B3%95.jpg

在调参配置环节，选择某一调参方式，目前TI支持random search、grid search和bayesian optimization三种调参方式。

https://main.qcloudimg.com/raw/f097c4d66715c6178c530da25262d189/%E7%AE%97%E6%B3%95%E8%87%AA%E5%8A%A8%E8%B0%83%E5%8F%82%E5%BC%B9%E7%AA%97.jpg

random search—从指定的分布中采样固定数量的参数设置，为每类超参数定义一个边缘分布，然后在这些参数上采样进行搜索。

Grid search—指在所有候选的参数选择中，通过循环遍历尝试每一种可能性，表现最好的参数就是最终的结果。
bayesian optimization—给定优化的目标函数，通过不断地添加样本点来更新目标函数的后验分布。
完成所有需要自动调参算法后，点击工具栏的运行按钮，启动任务运行。

## 自动调参详情
自动调参的结果查看详情，可通过右键算法节点中的自动调参详情入口进行查看

https://main.qcloudimg.com/raw/3319ada160dad485cf8ffba3d551d0e5/%E7%AE%97%E6%B3%95%E8%87%AA%E5%8A%A8%E8%B0%83%E5%8F%82%E8%AF%A6%E6%83%851.jpg

自动调参详情页面上方展示的是算法的基本运行信息，如训练/验证数据量、开始运行时间、目标列和特征列等；下方分两个模块，一个是模型指标，主要展示了每一迭代的AUC效果，以曲线呈现

https://main.qcloudimg.com/raw/bf698ddabbf903d7d339302b944e5be5/%E7%AE%97%E6%B3%95%E8%87%AA%E5%8A%A8%E8%B0%83%E5%8F%82%E8%AF%A6%E6%83%85%E6%8C%87%E6%A0%87%E6%A6%82%E8%A7%88.jpg

另一个模块展示的是每一轮迭代的信息、AUC值、运行状态及对应迭代的参数，点击参数展示被调的参数这一轮的具体值。

https://main.qcloudimg.com/raw/4a22734271daf738b62571a16c9f7373/%E7%AE%97%E6%B3%95%E8%87%AA%E5%8A%A8%E8%B0%83%E5%8F%82%E8%AF%A6%E6%83%85%E5%8F%82%E6%95%B0%E9%A1%B5.jpg

https://main.qcloudimg.com/raw/062b924b845f65f382249ae2b6621c3d/%E7%AE%97%E6%B3%95%E8%87%AA%E5%8A%A8%E8%B0%83%E5%8F%82%E8%AF%A6%E6%83%852.jpg