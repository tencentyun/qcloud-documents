## 场景背景

金融机构识别欺诈性的信用卡交易是非常重要的，这样客户不需要为他们没有实际发生的交易付费。

训练样本集包含欧洲信用卡持卡人于 2013 年 9 月通过信用卡进行的交易。该数据集提供两天内发生的交易，其中在 284,807 笔交易中有 492 起欺诈行为。数据集非常不平衡，正样本（欺诈）占所有交易的 0.172％。

由于数据脱敏原因，原始特征都以 V1，V2，...V28 表示，唯一保留业务含义的特征是“时间”和“金额”。“时间”指每个交易与数据集中第一笔交易之间经过的秒数。“金额”是交易金额。特征“类”是标签，在欺诈的情况下其值为 1，否则为 0。

本案例的目标是识别训练样本中的欺诈性信用卡交易。

## 整体流程

该 Demo 的整体流程如下图所示：
![](https://main.qcloudimg.com/raw/cc1b00036ee7a18cfcc04582e80be9d5.png)
包含9个环节，分别是：

| 序号 | 环节                                       |
| ---- | ------------------------------------------ |
| 1.   | 将数据从本地上传到 COS                     |
| 2.   | 将数据拆分成训练集和验证集                 |
| 3.   | 对训练数据做特征处理                       |
| 4.   | 将特征处理后的训练数据切分成训练集和测试集 |
| 5.   | 训练信用卡交易欺诈识别模型                 |
| 6.   | 对验证数据做特征处理                       |
| 7.   | 在验证数据集上验证信用卡交易欺诈识别模型   |
| 8.   | 生成模型混淆矩阵                           |
| 9.   | 生成模型 ROC 曲线                          |

接下来详细说明各环节。

## 流程详解

### 新建工程和工作流
1. 登录 [TI-ONE](https://tio.cloud.tencent.com)，输入腾讯云账号和密码，进入 TI-ONE 项目列表页。单击【+新建工程】图标新建工程。
  ![](https://main.qcloudimg.com/raw/632a3f15ff510e33dbb90061371a7db9.png)

2. 填写工程名称和工程描述等相关信息。
  ![](https://main.qcloudimg.com/raw/e8b2d533ede8e55b24c63c96ade15825.png)

3. 登录腾讯云控制台，进入 [对象存储控制台](https://console.cloud.tencent.com/cos)，单击【储存桶列表】-【创建储存桶】。
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
  ![](https://main.qcloudimg.com/raw/d964fae352d82a546743b86491e8865a.png)

9. 单击确认，进入画布。
  ![](https://main.qcloudimg.com/raw/39115fe695132ca714a34d2019b60cea.png)

### 上传训练数据

1. 左边栏选择：输入-\>数据源-\>本地输入。

2. 拖入画布，填写参数。
  ![](https://main.qcloudimg.com/raw/b060166791646928ef1a914a6ae3c057.png)

3. 上传数据文件：选择本地文件“data.txt”并上传。
  ![](https://main.qcloudimg.com/raw/af1ad00af24c41e57239dfd999807cbe.png)

> 目标 COS 路径自动生成，支持修改。

### 拆分出验证集

1. 左边栏选择：算法 -\>机器学习算法-\>数据预处理-\>Splitter。

2. 右键重命名：拆分出验证集。

3. 填写参数：
 - 输入输出路径根据连线自动生成，无需用户填写。
 - 并行数：11
 - 切分比例：0.2
 - num-executors：10
 - 其余使用默认值。
  ![](https://main.qcloudimg.com/raw/342553c0946651a5702ea9c3f008068f.png)



### 训练集特征处理

1. 左边栏选择：算法 -\>机器学习算法-\>特征转换-\>Dummy。

2. 右键重命名：训练特征集处理。

3. 特征上传配置：上传本地文件 feature_conf.json。
  ![](https://main.qcloudimg.com/raw/1151d24bd27527861431cc315bd0e05b.png)

4. 填写参数：
 - 输入输出路径根据连线自动生成，无需用户填写。
 - 负样本抽样率：0.01
 - 并行数：100
 - 特征频次阈值：2
 - num-executors：10
 - 其余使用默认值。
  ![](https://main.qcloudimg.com/raw/951f186b56081d0140b92e6d41bb525d.png)

### 切分出测试集

1. 左边栏选择：算法 -\>机器学习算法-\>数据预处理-\>Splitter。

2. 右键重命名：切分出测试集。

3. 填写参数
 - 输入输出路径根据连线自动生成，无需用户填写。
 - 并行数：11
 - 切分比例：0.7
 - num-executors：10
 - 其余使用默认值。
  ![](https://main.qcloudimg.com/raw/a89300af972605cdaa0a4e577f7d5df5.png)

### 训练信用卡交易欺诈识别模型

1. 左边栏选择：算法-\>机器学习算法-\>分类-\>SparseLogicalRegression。

2. 右键重命名：欺诈识别模型。

3. 填写参数：
 - 输入数据根据连线自动生成。
 - 并行率：10
 - 验证集数据若未生成，则需要用户手动将上一组件与本组件相连，重新点开参数配置栏，验证局数据根据连线自动生成。
 - 子模型数：2
 - L1正则系数：0.001
 - rho：0.01
 - 最大迭代次数：20
 - num-executors： 10
 - 其余使用默认值。
  ![](https://main.qcloudimg.com/raw/475afe7c4cc19af70df455eaefaf47bb.png)

### 验证集特征处理

1. 左边栏选择：算法 -\>机器学习算法-\>特征转换-\>Dummy。

2. 右键重命名：验证集特征处理。

3. 上传特征配置：feature_conf.json，在本案例中，验证集的该配置文件与训练集一致，所以不需要重新上传，只需要选择已上传的配置文件，单击确定即可。
  ![](https://main.qcloudimg.com/raw/e214887ddfac6209da52530cbd8d61c8.png)

4. 填写参数：
 - 输入输出路径根据连线自动生成，无需用户填写。
 - 负样本抽样率：0.01
 - 并行数：100
 - 特征频次阈值：2
 - num-executors：10
 - 其余使用默认值。
  ![](https://main.qcloudimg.com/raw/e403d3c78a4771c365e5236fe0bf3567.png)

### 模型验证

1. 单击流失率训练模型旁边的小圈。

2. 填写参数：
 - 模型运行方式设为“自动运行”。
 - 输入输出路径根据连线自动生成，无需用户填写。
 - 并行数：10
 - num-executors： 10
 - 其余使用默认值。
  ![](https://main.qcloudimg.com/raw/d7c5801ed34b6366a62c74b7caabb40b.png)


### 生成模型混淆矩阵

1. 左边栏选择：输出-\>模型评估-\>BinaryEvaluator。

2. 右键重命名：混淆矩阵。

3. 填写参数：
 - 输入路径根据连线自动生成，无需用户填写。
 - 标签列：0
 - 预测列：1
 - 抽样率：1.0
 - 并行数：20
 - 预测阈值：0.5
 - num-executors： 10
 - 其余使用默认值。
  ![](https://main.qcloudimg.com/raw/ba4716da34d7af3fc6ce73c5f465bd71.png)



### 生成模型ROC曲线

1. 左边栏选择：输出-\>模型评估-\>ROC。

2. 右键重命名：AUC。

3. 填写参数：
 - 输入路径根据连线自动生成，无需用户填写。
 - 标签列：0
 - 预测列：1
 - num-executors： 10
 - 其余使用默认值。
  ![](https://main.qcloudimg.com/raw/46c84623bd54085fa0bbc9c29e702491.png)

## 操作说明

### 保存工作流

单击工具条上的磁盘图标，保存工作流，如图：
![](https://main.qcloudimg.com/raw/aa310dd99fa0b0c82ee5c4a2bae3faca.png)

### 运行完整流程

单击工具条上的“三角”箭头，运行完整的流程，如图：
![](https://main.qcloudimg.com/raw/c4ec0c93329f4d09eb3dc1c805fa35f2.png)

### 从指定环节开始运行

右键单击要运行的环节，选择“起点运行”，从该环节开始向下执行：
![](https://main.qcloudimg.com/raw/d8b76e3e0cd0dc1614e56ceb2a9cc3b8.png)

### 查看中间结果 

运行完成后，右键单击数据处理的组件，可以查看中间结果。
![](https://main.qcloudimg.com/raw/6881b0e735a7151439e7333b26a137aa.png)
单击 COS 链接，可以获取完整的中间结果。


### 异常处理

当环节节点上出现感叹号，说明流程出现异常。鼠标悬浮于组件，可以查看失败原因。
![](https://main.qcloudimg.com/raw/028ccced2cb600ef7e51b0f4ae1bb62f.png)
右键单击该环节选择“Spark 控制台”查看日志，可以查看具体错误原因。
![](https://main.qcloudimg.com/raw/4d31ab110056c4d1ccc8b460eb557c26.png)
