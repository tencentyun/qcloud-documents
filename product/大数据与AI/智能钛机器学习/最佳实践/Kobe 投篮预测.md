# **Kobe投篮预测**

## 场景背景

2016年4月12日，科比在他的最后一场比赛中为洛杉矶湖人队夺得60分，标志着他从 NBA 退役。从17岁入选 NBA，科比在他的职业生涯中获得了无数的赞誉。
使用科比职业生涯中投篮命中和投失的历史数据，您能预测哪些投篮能命中篮筐吗？通过本案例中，您可以训练一个模型去准确预测科比的某次投篮是否会投进。本案例非常适合实践分类知识、特征工程和时间序列分析。

## 数据集介绍

该案例的训练数据包含科比在20年职业生涯中所尝试的每个投篮的具体特征信息：动作、位置、日期等。

**数据集字段信息如下：**

| **字段名**         | **取值类型** | **取值举例**                                                 |
| ------------------ | ------------ | ------------------------------------------------------------ |
| action_type        | 枚举         | Jump Shot/Running Jump Shot/Layup Shot/Reverse Dunk Shot/Slam Dunk Shot |
| combined_shot_type | 枚举         | Jump Shot/Layup/Dunk                                         |
| game_event_id      | 数值         | 1/2//3/……                                                    |
| game_id            | 数值         | 20000012/20000047/……                                         |
| lat                | 数值         | 33.9343/34.0163/……                                           |
| loc_x              | 数值         | -157/138/0/……                                                |
| loc_y              | 数值         | 175/-11/0/……                                                 |
| lon                | 数值         | -118.1028/-118.2938/……                                       |
| minutes_remaining  | 数值         | 0/1/2/3/4/5/6/7/8/9/10/11                                    |
| period             | 数值         | 1/2/3/4/5/6/7                                                |
| playoffs           | 数值         | 0/1                                                          |
| season             | 字符串       | 2004-5-1/2007-8-1/2015-16/……                                 |
| seconds_remaining  | 数值         | 0\~59                                                        |
| shot_distance      | 数值         | 0/45/79/……                                                   |
| target             | label        | 0/1                                                          |
| shot_type          | 枚举         | 2PT Field Goal/3PT Field Goal                                |
| shot_zone_area     | 枚举         | Right Side(R)/Left Side(L)/Left Side Center(LC)/Right Side Center(RC)/Center©/Back Court(BC) |
| shot_zone_basic    | 枚举         | Mid-Range/Restricted Area/In The Paint (Non-RA)/Above the Break 3/…… |
| shot_zone_range    | 枚举         | 16-24 ft./8-16 ft./Less Than 8 ft./24+ ft./……                |
| team_id            | 数值         | 1610612747                                                   |
| team_name          | 字符串       | Los Angeles Lakers                                           |
| game_date          | 日期         | 2000-10-31/2014-12-21/……                                     |
| matchup            | 字符串       | LAL vs. IND/LAL vs. SAC/LAL vs. UTA/LAL vs. SAC/……           |
| opponent           | 字符串       | SAC/PHX/……                                                   |
| shot_id            | 数值         | 1/2/3/4/5/……                                                 |

**数据集具体内容抽样展示如下：**

![](https://main.qcloudimg.com/raw/f5229a880452b74fcc49aeb1e7049a12.png)

## **案例相关材料**

相关材料下载链接：[Kobe 投篮预测 Demo 材料](https://main.qcloudimg.com/raw/c16f2f3c736e434b63341db6026d7425/kobe.zip)。
该材料包含以下文件：

- classifier.py：分类模型的自定义分类器文件，用于模型分类
- data_cleaning.py：数据预处理阶段的自定义数据清洗代码
- data_transformation.py：自定义数据特征转换代码
- feature_selection.py：自定义数据特征选择代码
- kobe.csv：kobe投篮具体特征信息的数据集文件

请用户下载该案例所需全部材料，并保存到本地以便后面搭建工作流需要。

## **整体流程**
该 Demo 的整体流程如下：

![](https://main.qcloudimg.com/raw/8b95ebd269c35ae066aa9f523e87ece8/1558602795896.png)

## **详细流程**

#### **一. 上传数据**

本案例通过本地数据节点上传所需数据：

1. 在智能钛机器学习平台控制台的左侧导航栏，选择【输入】>【数据源】>【 本地数据】，拖入画布中

2. 在【案例相关材料】中提前下载好的数据文件里找到kobe.csv文件，通过【 本地数据】上传 kobe.csv

![](https://main.qcloudimg.com/raw/90c8c9604556eb39a0d8a9bc2329c2c6.png)

  **![](https://main.qcloudimg.com/raw/0827e9fe277120afd80a5a6aa32b9526.png)**

3. 修改 COS 路径
    目标 COS 路径本为自动生成，无需修改，但支持用户自定义修改，如此处修改为`${cos}/kobe_predict/`

    注意：请务必复制修改此处“目标COS路径”，否则后续运行系统会报找不到文件的错误 

  **![](https://main.qcloudimg.com/raw/d66e2b4764ca4a6363516358e317eaba.png)**

#### **二. 数据清洗**

此数据清洗功能由【案例相关材料】中的清洗代码`data_cleaning.py`提供，所以此处主要向用户展示如何将自行编写的代码融入工作流中：

1. 在智能钛机器学习平台控制台的左侧导航栏，选择【组件】>【深度学习】>【 TensorFlow】
2. 将【 TensorFlow】拖入画布中，并右键单击重命名为“数据清洗”
3. 填写参数：
 - 【组件参数】中的“程序脚本”：上传文件 data_cleaning.py

 - Python 版本：选择 Python 3.5

 - 其余参数均可默认

  **![](https://main.qcloudimg.com/raw/b732149cb72acb244643860ca10f40b7.png)**

  **![](https://main.qcloudimg.com/raw/c0b243f5d30e4d7f57203a72baf19105.png)**

#### **三. 特征转换**

此特征转换功能亦由【案例相关材料】中的相关代码`data_transformation.py`提供：

1. 在智能钛机器学习平台控制台的左侧导航栏，选择【组件】>【深度学习】>【 TensorFlow】
2. 将【 TensorFlow】拖入画布中，并右键重命名为“特征转换”
3. 填写参数：
 - 程序脚本：上传文件 `data_transformation.py`

 - Python版本：选择 `Python 3.5`

 - 其余参数均可默认

  **![](https://main.qcloudimg.com/raw/93e0b8004897f12611f4e16094fe0ab0.png)**

  **![](https://main.qcloudimg.com/raw/c83d8495afaf7f153fe0cf2d9931ee8c.png)**

#### **四. 特征选择**

此特征选择功能亦由【案例相关材料】中的相关代码data_selection.py提供：

1. 在智能钛机器学习平台控制台的左侧导航栏，选择【组件】>【深度学习】>【TensorFlow】
2. 将【TensorFlow】拖入画布中，并右键单击重命名为“特征选择”
3. 填写参数：
 - 程序脚本：上传文件 feature_selection.py

 - Python版本：选择 Python 3.5

 - 其余参数均可默认

![](https://main.qcloudimg.com/raw/ecf79a181e533d9db7baf0519097688f.png)

#### **五. 分类器**

此分类器功能亦由【案例相关材料】中的相关代码`classifier.py`提供：

1. 在智能钛机器学习平台控制台的左侧导航栏，选择【组件】>【深度学习】>【TensorFlow】
2. 将【TensorFlow】拖入画布中，并右键重命名为“分类器”
3. 填写参数：
 - 程序脚本：上传文件 `classifier.py`

 - Python版本：选择 `Python 3.5`

 - 其余参数均可默认

  **![](https://main.qcloudimg.com/raw/09fd804263c4b3a7c6c6af4cc73f0c88.png)**

#### **六. 模型评估**
1. 在智能钛机器学习平台控制台的左侧导航栏，选择【输出】>【模型评估】>【BinaryEvaluator】

2. 将【BinaryEvaluator】拖入画布中

3. 填写参数：

   算法 IO 参数配置：
 - 输入数据：`${cos}/kobe_predict/result.csv`

 - 标签列：0

 - 得分列：1

 - 抽样率：1.0

 - 并行数：10

**![](https://main.qcloudimg.com/raw/12064128bd813d55faf4222a2c9ed83e.png)**


**算法参数和资源参数配置**

 - 预测阈值：0.5

 - 其余参数均可默认

**![](https://main.qcloudimg.com/raw/7d4b25656cfb4e20d4d1258ecf7ad2a0.png)**

#### **七. 运行调度及训练进度查看**

详情请参考 [运行工作流](链接需要更改)。