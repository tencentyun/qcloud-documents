## 场景背景

该 Demo 是基于 QQ 游戏的需求设计的场景，对互联网公司的用户流失预测具有参考意义。QQ 游戏客户流失率预测模型是基于玩家的年龄、Q 龄、玩家等级、所在地等信息预测玩家的流失率。其业务意义在于帮助 QQ 游戏提前做客户挽留，提高挽留成功率及降低挽留成本。

## 案例相关材料
相关材料下载链接：
 - [train.txt](https://main.qcloudimg.com/raw/b907e4fc8ff62cfd5607a1f7a1f226f6.zip)

 - [feature_conf.json](https://main.qcloudimg.com/raw/e5d3f7dad72e4277eda6c5f4068b851b.zip)

 - [predict.txt](https://main.qcloudimg.com/raw/c473403056ed88b940273865bafd4472.zip)

## 整体流程

该 Demo的整体流程如下图所示：
![](https://main.qcloudimg.com/raw/a80a0557d6b3331218922993c50361db.png)


流程包含 8 个环节，分别是：


1. [将训练数据从本地上传到 COS](#jump1)                  
2. [对训练数据做特征处理](#jump2)                       
3. [将特征处理后的训练数据切分成训练集和测试集](#jump3)
4. [训练流失率预测模型](#jump4)                         
5. [将验证数据从本地上传到 COS](#jump5)                  
6. [对验证数据做特征处理](#jump6)                       
7. [在验证数据集上验证流失率预测模型](#jump8)           
8. [生成模型评估结果](#jump8)                           

## 流程详解

### 新建工程和工作流

1. 登录 [TI-ONE](https://tio.cloud.tencent.com)控制台，进入 TI-ONE 项目列表页。单击【+新建工程】。
![](https://main.qcloudimg.com/raw/632a3f15ff510e33dbb90061371a7db9.png)

2. 填写工程名称和工程描述等相关信息。
![](https://main.qcloudimg.com/raw/e8b2d533ede8e55b24c63c96ade15825.png)

3. 登录腾讯云[对象存储控制台](https://console.cloud.tencent.com/cos)，单击【储存桶列表】>【创建储存桶】。
![](https://main.qcloudimg.com/raw/e4cdfaa79d7881d63df4e88f80cdfce2.png)

4. 创建成功后在新建工程页下拉列表处选取储存桶。
![](https://main.qcloudimg.com/raw/645d2203a91e7ea715d41769a964dc74.png)

5. 单击新建工程页面的 API 密钥管理链接，进入 COS 控制台，单击【密钥管理】-【云 API 密钥链接】进入密钥界面。
![](https://main.qcloudimg.com/raw/3697b0510ed3e6403150e0b4ce3632f2.png)

6. 单击新建密钥进行密钥创建-复制创建好的 SecretId 和 Secretkey，在新建工程页面粘贴，单击保存。
![](https://main.qcloudimg.com/raw/51d455f62142ca9d18f5ee623e6221ef.png)

7. 完成新建工程后，单击“+号”新建工作流。
![](https://main.qcloudimg.com/raw/11c67f72ffef272fafcf5554284fee42.png)

8. 输入工作流名称。
![](https://main.qcloudimg.com/raw/9f6021b778ab1e413fb8707ddb78bac6.png)

9. 单击确认，进入画布。
![](https://main.qcloudimg.com/raw/39115fe695132ca714a34d2019b60cea.png)


<span id = "jump1"></span>
### 上传训练数据

1. 左边栏选择：输入>数据源>本地输入。

2. 拖入画布，填写参数。
![](https://main.qcloudimg.com/raw/b9047014b6da6bbd510b9326084ebfb5.png)

3. 数据文件：选择本地文件“train.txt”并上传。
![](https://main.qcloudimg.com/raw/ff7c3cc87986bc34ebef746b4c56b98c.png)

4. 目标 COS 路径自动生成，支持修改。
![](https://main.qcloudimg.com/raw/96c199716203d914f976477d782d2024.png)

<span id = "jump2"></span>
### 训练集特征处理

1. 左边栏选择：算法>机器学习算法>特征转换>Dummy。

2. 右键重命名：训练特征集处理。

3. 特征上传配置：上传本地文件 feature_conf.json。
![](https://main.qcloudimg.com/raw/c2acba9b4df722d9aecf0329ebae5d8a.png)

4. 输入参数：
 - 输入输出路径根据连线自动生成，无需用户填写。
 - 负样本抽样率：1.0
 - 并行数：100
 - 特征频次阈值：2
 - num-executors：5
 - 其余使用默认值。
![](https://main.qcloudimg.com/raw/6298ed456b7f9fc9aa56f171855e0073.png)

<span id = "jump3"></span>
### 数据切分

1. 左边栏选择：算法>机器学习算法>数据预处理>Splitter。

2. 右键重命名：数据切分。

3. 填写参数：
 - 输入输出路径根据连线自动生成，无需用户填写。
 - 并行数：11
 - 切分比例：0.7
 - num-executors：10
 - 其余使用默认值。
![](https://main.qcloudimg.com/raw/c881a2d543287c40a8ed7bf9ebdbe67a.png)

<span id = "jump4"></span>
### 训练流失率模型

1. 左边栏选择：算法>机器学习算法>分类>SparseLogicalRegression。

2. 右键重命名：流失率训练模型。

3. 填写参数：
 - 输入数据根据连线自动生成。
 -  并行率：10
 -  验证集数据若未生成，则需要用户手动将上一组件与本组件相连，重新点开参数配置栏，验证集数据根据连线自动生成。
 - 子模型数：2
 - L1正则系数：0.001
 -   rho：0.01
 -   最大迭代次数：20
 -   num-executors： 10
 -   其余使用默认值。
![](https://main.qcloudimg.com/raw/52816ed70a54212124244d9bebe11c4a.png)


<span id = "jump5"></span>
### 上传验证数据

1. 左边栏选择：输入>数据源>本地输入。

2. 填写参数：

 1.  数据文件选择上传 predict.txt。
 2.  COS 目标路径自动生成，支持修改。

![](https://main.qcloudimg.com/raw/c353ebf65058c54e3388de926f043af0.png)



> **注意：**
> 从训练特征集处理到验证数据源的连线并非代表这里有数据流传输，只是因为后面的验证集特征处理会用到训练特征集处理的产出物，所以要确保验证特征集处理的开始时间在训练特征集处理结束之后。

<span id = "jump6"></span>
### 验证集特征预处理

1. 左边栏选择：算法 >机器学习算法>特征转换>Dummy。

2. 右键重命名：验证集特征处理。

3. 上传特征配置：feature_conf.json，在本案例中，验证集的该配置文件与训练集一致，所以不需要重新上传，只需要选择已上传的配置文件，单击确定即可。
![](https://main.qcloudimg.com/raw/ecb06c317768369c458d79ef986715fa.png)

4. 填写参数：
 -  输入输出路径根据连线自动生成，无需用户填写。
 -  负样本抽样率：1.0
 -  并行数：100
 -  特征频次阈值：2
 -  num-executors：10
 -  其余使用默认值。
![](https://main.qcloudimg.com/raw/46245981b981192a2d7df27f815a9c89.png)

<span id = "jump7"></span>
### 模型验证

1. 单击流失率训练模型旁边的小圈。

2. 填写参数：
 - 模型运行方式设为“自动运行”。
 - 将验证集特征处理组件与模型小圈连线，输入输出路径根据连线自动生成。
 - 并行数：10
 - num-executors： 10
 - 其余使用默认值。
![](https://main.qcloudimg.com/raw/f7e538121772dc5be9b753737db8b8c3.png)


<span id = "jump8"></span>
### 模型评估

1. 左边栏选择：算法>机器学习算法>输出>BinaryEvaluator。

2. 右键重命名：模型评估。

3. 填写参数：
 - 输入输出路径根据连线自动生成，无需用户填写。
 - 标签列：0
 -  预测列：1
 -  抽样率：1.0
 - 并行数：20
 - 预测阈值：0.5
 - num-executors： 10
 - 其余使用默认值。
![](https://main.qcloudimg.com/raw/f21ca1a2ed68a49344bb72c67bb6c256.png)



## 操作说明

### 保存工作流

单击工具条上的磁盘图标，保存工作流。
![](https://main.qcloudimg.com/raw/2070d9fb0c6b1a8f6eac2588c87baff2.png)


### 运行完整流程

单击工具条上的“三角”箭头，运行完整的流程。
![](https://main.qcloudimg.com/raw/e31c6d962366e3c65f262abd4376f223.png)

### 从指定环节开始运行

右键单击要运行的环节，选择“起点运行”，从该环节开始向下执行。
![](https://main.qcloudimg.com/raw/c157776ebf8411ffd9c6efe2f7ddb178.png)


### 查看中间结果

运行完成后，右键单击数据处理的组件，可以查看中间结果。
![](https://main.qcloudimg.com/raw/400adbc7a77ca2790e32f49e1223d638.png)
单击 COS 链接，可以获取完整的中间结果。

### 异常处理

当环节节点上出现感叹号，说明流程出现异常，鼠标悬浮于组件，可以查看失败原因。
![](https://main.qcloudimg.com/raw/553671ee5ffedb770066dde966004462.png)

右键单击该环节选择“Spark 控制台”查看日志，可以查看具体错误原因：
![](https://main.qcloudimg.com/raw/a09f2f70c7fe65703e6689ce0a572dd0.png)
