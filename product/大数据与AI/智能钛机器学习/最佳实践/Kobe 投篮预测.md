## 场景背景
科比在 2016 年 4 月 12 日星期三的最后一场比赛中为洛杉矶湖人队得到 60 分，标志着他从 NBA 退役。从 17 岁入选 NBA，科比在他的职业生涯中获得了无数的赞誉。
使用 20 年有关科比的投篮命中和投失数据，您能预测哪些投篮能命中篮筐吗？本案例非常适合实践分类基础知识、特征工程和时间序列分析。
训练数据包含了科比在他 20 年职业生涯中所尝试的每个投篮命中的位置和情况。您的任务是训练模型来预测每次投篮是否会投进。

字段如下：

| **字段名**         | **取值类型** | **取值举例**                                                 |
| ------------------ | ------------ | ------------------------------------------------------------ |
| action_type        | 枚举         | Jump Shot/Running Jump Shot/Layup Shot/Reverse Dunk Shot/Slam Dunk Shot |
| combined_shot_type | 枚举         | Jump Shot/Layup/Dunk                                       |
| game_event_id      | 数值         | 1/2//3/……                                                |
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
[Kobe 投篮预测 Demo 材料.zip](https://main.qcloudimg.com/raw/5c5a9b493b948241cf4d9d1e955febfb/Kobe%E6%8A%95%E7%AF%AE%E9%A2%84%E6%B5%8BDemo%E6%9D%90%E6%96%99.zip)（包含：train.txt、feature_conf.json、predict.txt）

## 整体流程

该 Demo 的整体流程如下：
![](https://main.qcloudimg.com/raw/67e51ef060dfa01b6f0b98fd3c2c8433.png)

该流程包含8个环节，**搭建的任务流须与此整体流程图完全一致，以保证此任务顺利运行**。

1. [上传训练数据](https://cloud.tencent.com/document/product/851/19546#.E4.B8.8A.E4.BC.A0.E8.AE.AD.E7.BB.83.E6.95.B0.E6.8D.AE)
2. [训练集特征处理](https://cloud.tencent.com/document/product/851/19546#.E8.AE.AD.E7.BB.83.E9.9B.86.E7.89.B9.E5.BE.81.E5.A4.84.E7.90.86)
3. [数据拆分](https://cloud.tencent.com/document/product/851/19546#.E6.95.B0.E6.8D.AE.E6.8B.86.E5.88.86)
4. [训练投篮预测模型](https://cloud.tencent.com/document/product/851/19546#.E8.AE.AD.E7.BB.83.E6.8A.95.E7.AF.AE.E9.A2.84.E6.B5.8B.E6.A8.A1.E5.9E.8B)
5. [上传验证数据](https://cloud.tencent.com/document/product/851/19546#.E4.B8.8A.E4.BC.A0.E9.AA.8C.E8.AF.81.E6.95.B0.E6.8D.AE)
6. [验证集特征预处理](https://cloud.tencent.com/document/product/851/19546#.E9.AA.8C.E8.AF.81.E9.9B.86.E7.89.B9.E5.BE.81.E9.A2.84.E5.A4.84.E7.90.86)
7. [模型验证](https://cloud.tencent.com/document/product/851/19546#.E6.A8.A1.E5.9E.8B.E9.AA.8C.E8.AF.81)
8. [模型评估](https://cloud.tencent.com/document/product/851/19546#.E6.A8.A1.E5.9E.8B.E8.AF.84.E4.BC.B0)



## 流程详解
### 新建工程和工作流
1. 登录 [TI-ONE](https://tio.cloud.tencent.com) 控制台，进入 TI-ONE 项目列表页。单击【+新建工程】。
2. 在新建工程页面，填写工程名称和工程描述等相关信息。
3. 登录腾讯云 [对象存储控制台](https://console.cloud.tencent.com/cos)，单击【存储桶列表】>【创建存储桶】。
4. 创建成功后在新建工程页下拉列表处选取储存桶。
    ![](https://main.qcloudimg.com/raw/645d2203a91e7ea715d41769a964dc74.png)
5. 单击新建工程页面的 API 密钥管理链接，进入 COS 控制台，根据页面提示前往访问管理控制台的  [API 密钥管理](https://console.cloud.tencent.com/cam/capi) 界面。
6. 在 API 密钥管理界面，单击【新建密钥】进行密钥创建。复制创建好的 SecretId 和 Secretkey。
7. 在 TI-ONE 新建工程页面，粘贴上一步复制的 SecretId 和 Secretkey，单击【保存】。
8. 完成新建工程后，单击工程下方的“+号”，新建工作流。
9. 输入工作流名称，单击【确认】，进入画布。


### 上传训练数据
1. 在左侧菜单栏，选择【输入】>【数据源】>【本地数据】。
2. 将【本地数据】组件拖入画布，填写参数。
    ![](https://main.qcloudimg.com/raw/4f0e510dcbe2a4f489149c2f801f03e3.png)
3. 在参数配置中，上传数据文件：选择本地文件“train.txt”并上传。
>?目标 COS 路径自动生成，支持修改。


### 训练集特征处理
1. 在左侧菜单栏，选择【算法】>【机器学习算法】>【特征转换】>【Dummy】。
2. 将【Dummy】组件拖入画布，右键单击重命名为：训练特征处理。
3. 特征生成配置：上传本地文件 feature_conf.json。
4. 填写参数：
 - 输入输出路径根据连线自动生成，无需用户填写。
 - 负样本抽样率：1.0
 - 并行数：100
 - 特征频次阈值：2
 - 其余使用默认值。
![](https://main.qcloudimg.com/raw/cd68130908f7bdb5a87b3b00ff1c9ddc.png)

### 数据拆分
1. 在左侧菜单栏，选择【算法】>【机器学习算法】>【数据预处理】>【Splitter】。
2. 将【Splitter】组件拖入画布，右键单击重命名为：训练数据拆分。
3. 填写参数：
 - 输入输出路径根据连线自动生成，无需用户填写。
 - 并行数：11
 - 切分比例：0.7
 - 其余使用默认值。
![](https://main.qcloudimg.com/raw/91700070a7e58feab2b6fdfa2f1f4020.png) 

### 训练投篮预测模型
1. 在左侧菜单栏，选择【算法】>【机器学习算法】>【分类】>【SparseLogicalRegression】。
2. 将【SparseLogicalRegression】组件拖入画布，右键单击重命名为：投篮预测训练模型。
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
1. 在左侧菜单栏，选择【输入】>【数据源】>【本地输入】。
2. 填写参数：
 - 数据文件选择上传 predict.txt。
 - COS 目标路径自动生成，支持修改。
  
> !从训练特征集处理到验证数据源的连线并非代表这里有数据流传输，只是因为后面的验证集特征处理会用到训练特征集处理的产出物，所以要确保验证特征集处理的开始时间在训练特征集处理结束之后。

![](https://main.qcloudimg.com/raw/fbd21bb7f46d42c39c433ada184438bc.png)



### 验证集特征预处理

1. 在左侧菜单栏，选择【算法】>【机器学习算法】>【特征转换】>【Dummy】。
2. 将【Dummy】拖入画布，右键单击重命名为：验证集特征处理。
3. 上传特征配置：feature_conf.json，在本案例中，验证集的该配置文件与训练集一致，所以不需要重新上传，只需要选择已上传的配置文件，单击确定即可。
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
1. 在左侧菜单栏，选择【输出】>【模型评估】>【BinaryEvaluator】。
2. 将【BinaryEvaluator】组件拖入画布，右键单击重命名为：模型评估。
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
