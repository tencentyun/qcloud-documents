# 数据预处理


#### 操作步骤

1. 数据准备完成后，将**数据预处理**（此处为SelectColumn、ReplaceMissing、StringIndexer以及Spliter）拖动至画布中，并右键重命名组件，拼接如下实验。

<img src="https://main.qcloudimg.com/raw/82f3ab3c7de6b65d18d66a4117edc2ef.png" style="zoom:80%">

   2. 点击**选择特征列**，在画布右侧设置区进行参数设置，输入相应特征列序号，并以逗号隔开。

      <img src="https://main.qcloudimg.com/raw/6627141a945f6c9961c4cb0f08c8cf4a.png" style="zoom:80%">
        
      3. 点击**缺失值填充**，在画布右侧设置区进行参数设置，选择特征列和相应的填充方式。

<img src="https://main.qcloudimg.com/raw/76126426184526fa2857dd5c03d7cef3.png" style="zoom:80%">
    
4. 点击**字符串索引**，在初始的数据集中，很多类别变量都是字符串（如男和女），对于这样的特征列，需要将字符串转换为int的形式（如男为0，女为1），便于后续的建模。 

   在这里我们需要对数据中的“sex”和“embarked”列分别做字符串索引，点击相应组件，并在画布右侧的参数设置区中，选择相应的特征列。    
5. 点击**数据切分**，在画布右侧的参数设置区中，输入切分比例0.8，80%作为模型训练集，20%作为模型预测集。
  
6. 点击运行，如下图所示，**数据预处理**成功运行。
  
![https://main.qcloudimg.com/raw/3349882ba5f18b484199c390bc0f3249.png](https://main.qcloudimg.com/raw/3349882ba5f18b484199c390bc0f3249.png)



