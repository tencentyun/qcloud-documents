## 场景背景

科比在 2016 年 4 月 12 日星期三的最后一场比赛中为洛杉矶湖人队得到 60 分，标志着他从 NBA 退役。从 17 岁入选 NBA，科比在他的职业生涯中获得了无数的赞誉。
使用 20 年有关科比的投篮命中和投失数据，您能预测哪些投篮能命中篮筐吗？本案例非常适合实践分类基础知识、特征工程和时间序列分析。
训练数据包含了科比在他 20 年职业生涯中所尝试的每个投篮命中的位置和情况。您的任务是训练模型来预测每次投篮是否会投进。

字段如下：

| **字段名**         | **取值类型** | **取值举例**                                                 |
| ------------------ | ------------ | ------------------------------------------------------------ |
| action_type        | 枚举         | Jump Shot/Running Jump Shot/Layup Shot/Reverse Dunk Shot/Slam Dunk Shot |
| combined_shot_type | 枚举         | Jump Shot/Layup/Dunk                                       |
| game_event_id      | 数值         | 1/2//3/……                                                  |
| game_id            | 数值         | 20000012/20000047/……                                       |
| lat                | 数值         | 33.9343/34.0163/……                                         |
| loc_x              | 数值         | -157/138/0/……                                            |
| loc_y              | 数值         | 175/-11/0/……                                              |
| lon                | 数值         | -118.1028/-118.2938/……                                    |
| minutes_remaining  | 数值         | 0/1/2/3/4/5/6/7/8/9/10/11                         |
| period             | 数值         | 1/2/3/4/5/6/7                                          |
| playoffs           | 数值         | 0/1                                                         |
| season             | 字符串       | 2004-5-1/2007-8-1/2015-16/……                              |
| seconds_remaining  | 数值         | 0\~59                                                        |
| shot_distance      | 数值         | 0/45/79/……                                                |
| target             | label        | 0/1                                                         |
| shot_type          | 枚举         | 2PT Field Goal/3PT Field Goal                               |
| shot_zone_area     | 枚举         | Right Side(R)/Left Side(L)/Left Side Center(LC)/Right Side Center(RC)/Center©/Back Court(BC) |
| shot_zone_basic    | 枚举         | Mid-Range/Restricted Area/In The Paint (Non-RA)/Above the Break 3/…… |
| shot_zone_range    | 枚举         | 16-24 ft./8-16 ft./Less Than 8 ft./24+ ft./……            |
| team_id            | 数值         | 1610612747                                                   |
| team_name          | 字符串       | Los Angeles Lakers                                           |
| game_date          | 日期         | 2000-10-31/2014-12-21/……                                   |
| matchup            | 字符串       | LAL vs. IND/LAL vs. SAC/LAL vs. UTA/LAL vs. SAC/……       |
| opponent           | 字符串       | SAC/PHX/……                                                 |
| shot_id            | 数值         | 1/2/3/4/5/……                                          |

## 案例相关材料
相关材料下载链接：
[Kobe投篮预测 Demo 材料.zip](https://main.qcloudimg.com/raw/5c5a9b493b948241cf4d9d1e955febfb/Kobe%E6%8A%95%E7%AF%AE%E9%A2%84%E6%B5%8BDemo%E6%9D%90%E6%96%99.zip)（包含：train.txt、feature_conf.json、predict.txt）

## 整体流程

该 Demo 的整体流程如下图所示：
![](https://main.qcloudimg.com/raw/c0b76a52418263b5033e48fde20030a2.png)

包含 8 个环节，分别是：

1. [将训练数据从本地上传到 COS](#jump1)
2. [对训练数据做特征处理](#jump2)
3. [将特征处理后的训练数据切分成训练集和测试集](#jump3)
4. [训练 Kobe 投篮预测模型](#jump4)
5. [将验证数据从本地上传到 COS](#jump5)
6. [对验证数据做特征处理](#jump6)
7. [在验证数据集上验证 Kobe 投篮预测模型](#jump7)
8. [生成模型评估结果](#jump8)


## 流程详解

### 新建工程和工作流

1. 登录 [TI-ONE](https://tio.cloud.tencent.com)控制台，进入 TI-ONE 项目列表页。单击【+新建工程】。
    ![](https://main.qcloudimg.com/raw/3cdde89b99dab1f0acf605e05383583d.png)
2. 填写工程名称和工程描述等相关信息。
    ![](https://main.qcloudimg.com/raw/e8b2d533ede8e55b24c63c96ade15825.png)
3. 登录腾讯云[对象存储控制台](https://console.cloud.tencent.com/cos)，单击【存储桶列表】>【创建存储桶】。
    ![](https://main.qcloudimg.com/raw/0a83a1b11edf7cd3d875b13e5e6086f3.png)
4. 创建成功后在新建工程页下拉列表处选取储存桶。
    ![](https://main.qcloudimg.com/raw/645d2203a91e7ea715d41769a964dc74.png)
5. 单击新建工程页面的 API 密钥管理链接，进入 COS 控制台，单击【密钥管理】>【云 API 密钥链接】进入密钥界面。
    ![](https://main.qcloudimg.com/raw/6dad73a787505e4e6f8af670424d330e/5a.png)
6. 单击新建密钥进行密钥创建-复制创建好的 SecretId 和 Secretkey，在新建工程页面粘贴，单击保存。
    ![](https://main.qcloudimg.com/raw/51d455f62142ca9d18f5ee623e6221ef.png)
7. 完成新建工程后，单击“+号”新建工作流。
    ![](https://main.qcloudimg.com/raw/11c67f72ffef272fafcf5554284fee42.png)
8. 输入工作流名称。
     ![](https://main.qcloudimg.com/raw/e9fb02f1e334a1622cdb64af8e99f6b5.png)
9. 单击确认，进入画布。
    ![](https://main.qcloudimg.com/raw/668c1e0bd960838c7015443d1a097938/9a.png)






### 上传训练数据

1. 左边栏选择：输入>数据源>本地输入。
2. 拖入画布，填写参数。
    ![](https://main.qcloudimg.com/raw/4f0e510dcbe2a4f489149c2f801f03e3.png)
3. 上传数据文件：选择本地文件“train.txt”并上传。
![](https://main.qcloudimg.com/raw/3fe44dd549ba73ce959d2110aced66f5.png)
>**注意：**目标 COS 路径自动生成，支持修改。


### 训练集特征处理

1. 左边栏选择：算法>机器学习算法>特征转换>Dummy。
2. 右键重命名：训练特征处理。
3. 特征生成配置：上传本地文件 feature_conf.json。
    ![](https://main.qcloudimg.com/raw/ef901ab45ee6127e7ac884615a9e9b36.png)
4. 填写参数：
 - 输入输出路径根据连线自动生成，无需用户填写。
 - 负样本抽样率：1.0
 - 并行数：100
 - 特征频次阈值：2
 - 其余使用默认值。
    ![](https://main.qcloudimg.com/raw/cd68130908f7bdb5a87b3b00ff1c9ddc.png)


### 数据拆分

1. 左边栏选择：算法>机器学习算法>数据预处理>Splitter。
2. 右键重命名：训练数据拆分。
3. 填写参数
 - 输入输出路径根据连线自动生成，无需用户填写。
 - 并行数：11
 - 切分比例：0.7
 - 其余使用默认值。
    ![](https://main.qcloudimg.com/raw/91700070a7e58feab2b6fdfa2f1f4020.png)


### 训练投篮预测模型

1. 左边栏选择：算法>机器学习算法>分类>SparseLogicalRegression。
2. 右键重命名：投篮预测训练模型。
3. 填写参数：
 - 输入数据根据连线自动生成。
 - 并行数：10
 - 验证集数据若未生成，则需要用户手动将上一组件与本组件相连，重新点开参数配置栏，验证集数据根据连线自动生成。
 - 子模型数：2
 - L1 正则系数：0.001
 - rho：0.01
 - 最大迭代次数：20
 - 其余使用默认值。
    ![](https://main.qcloudimg.com/raw/ab313a03b34d21bc3c78f7a9d561092c/kobe%E6%8A%95%E7%AF%AE%20%E8%AE%AD%E7%BB%83%E6%AD%A5%E9%AA%A43.png)


### 上传验证数据

1. 左边栏选择：输入>数据源>本地输入。
2. 填写参数：
 - 数据文件选择上传 predict.txt。
 - COS 目标路径自动生成，支持修改。
    ![](https://main.qcloudimg.com/raw/fbd21bb7f46d42c39c433ada184438bc.png)


> **注意：**
> 从训练特征集处理到验证数据源的连线并非代表这里有数据流传输，只是因为后面的验证集特征处理会用到训练特征集处理的产出物，所以要确保验证特征集处理的开始时间在训练特征集处理结束之后。


### 验证集特征预处理

1. 左边栏选择：算法>机器学习算法>特征转换>Dummy。
2. 右键重命名：验证集特征处理。
3. 上传特征配置：feature_conf.json，在本案例中，验证集的该配置文件与训练集一致，所以不需要重新上传，只需要选择已上传的配置文件，单击确定即可。
    ![](https://main.qcloudimg.com/raw/47ba93c53368adcbeff7fdaf456f6e24.png)
4. 填写参数：
 - 输入输出路径根据连线自动生成，无需用户填写。
 - 负样本抽样率：1.0
 - 并行数：100
 - 特征频次阈值：2
 - 其余使用默认值。
    ![](https://main.qcloudimg.com/raw/c0a5c5030925adacf77cb86b46ee3bc1.png)


### 模型验证

1. 单击投篮预测模型旁边的小圈。
2. 填写参数：
 - 模型运行方式设为“自动运行”。
 - 将验证集特征处理组件与模型小圈连线，输入输出路径根据连线自动生成。
 - 并行数：10
 - 其余使用默认值。
    ![](https://main.qcloudimg.com/raw/ee772f14c6393891c62ee94a8e734753.png)


### 模型评估

1. 左边栏选择：输出>模型评估>BinaryEvaluator。
2. 右键重命名：模型评估。
3. 填写参数：
 - 输入输出路径根据连线自动生成，无需用户填写。
 - 标签列：0
 - 预测列：1
 - 抽样率：1.0
 - 并行数：20
 - 预测阈值：0.5
 - 其余使用默认值。
    ![](https://main.qcloudimg.com/raw/4a54d7eba7bc6f323cef9369b4a08951.png)


## 操作说明

### 保存工作流

单击工具条上的磁盘图标，保存工作流。
![](https://main.qcloudimg.com/raw/e6c1c7e4daf1553ff4b6fec8f28f0bc6.png)

### 运行完整流程

单击工具条上的“三角”箭头，运行完整的流程。
![](https://main.qcloudimg.com/raw/aa76d80e4e31eaaabfb204b10ec1161f.png)

### 从指定环节开始运行

右键单击要运行的环节，选择“起点运行”，从该环节开始向下执行。
![](https://main.qcloudimg.com/raw/8c8d13294c755e8284839dd44bbc4f26.png)


### 查看中间结果


运行完成后，右键单击数据处理的组件，可以查看中间结果。
![](https://main.qcloudimg.com/raw/38bd9e266d6d767968190c0a89f65fae.png)

单击 COS 链接，可以获取完整的中间结果。


### 异常处理

当环节节点上出现感叹号，说明流程出现异常。鼠标悬浮于组件，可以查看失败原因。
![](https://main.qcloudimg.com/raw/5442900d9885083c49eab44ae069b4dc.png)

右键单击该环节选择“Spark 控制台”查看日志，可以查看具体错误原因。
![](https://main.qcloudimg.com/raw/5af904db6c303497feb22c988f3908b6.png)
