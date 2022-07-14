## 案例背景 
2016年4月14日，科比结束了他传奇的职业生涯。他在最后一场比赛中，独得60分，帮助湖人队取得了胜利。从17岁入选 NBA 开始到此刻光荣退役，科比在他的职业生涯中获得了无数的荣誉。 
通过使用科比职业生涯中投中和投失的数据，您能预测他的哪些投篮能命中篮筐吗？通过本案例，您可以利用腾讯云 TI 平台 TI-ONE 的 TensorFlow 框架训练一个分类模型，来预测科比的某次投篮是否会投进，并通过评估指标检测模型效果。本案例非常适合实践特征工程和分类的知识。 

## 数据集介绍 
该案例的训练数据包含科比在20年职业生涯中所尝试的每个投篮的具体特征信息：动作、位置、日期等。 
**数据集字段信息如下：** 

| **字段名** | **取值类型** | **取值举例** |
| ------------------ | ------------ | ------------------------------------------------------------ |
| action_type | 枚举 | Jump Shot/Running Jump Shot/Layup Shot/Reverse Dunk Shot/Slam Dunk Shot |
| combined_shot_type | 枚举 | Jump Shot/Layup/Dunk |
| game_event_id | 数值 | 1/2/3/…… |
| game_id | 数值 | 20000012/20000047/…… |
| lat | 数值 | 33.9343/34.0163/…… |
| loc_x | 数值 | -157/138/0/…… |
| loc_y | 数值 | 175/-11/0/…… |
| lon | 数值 | -118.1028/-118.2938/…… |
| minutes_remaining | 数值 | 0/1/2/3/4/5/6/7/8/9/10/11 |
| period | 数值 | 1/2/3/4/5/6/7 |
| playoffs | 数值 | 0/1 |
| season | 字符串 | 2004-5-1/2007-8-1/2015-16/…… |
| seconds_remaining | 数值 | 0\~59 |
| shot_distance | 数值 | 0/45/79/…… |
| target | 枚举 | 0/1 |
| shot_type | 枚举 | 2PT Field Goal/3PT Field Goal |
| shot_zone_area | 枚举 | Right Side(R)/Left Side(L)/Left Side Center(LC)/Right Side Center(RC)/Center©/Back Court(BC) |
| shot_zone_basic | 枚举 | Mid-Range/Restricted Area/In The Paint (Non-RA)/Above the Break 3/…… |
| shot_zone_range | 枚举 | 16-24 ft./8-16 ft./Less Than 8 ft./24+ ft./…… |
| team_id | 数值 | 1610612747 |
| team_name | 字符串 | Los Angeles Lakers |
| game_date | 日期 | 2000-10-31/2014-12-21/…… |
| matchup | 字符串 | LAL vs. IND/LAL vs. SAC/LAL vs. UTA/LAL vs. SAC/…… |
| opponent | 字符串 | SAC/PHX/…… |
| shot_id | 数值 | 1/2/3/4/5/…… |

**数据集具体内容抽样展示如下（前八列）：** 
![](https://main.qcloudimg.com/raw/839e2d3e9b8bb72618302a470df46ad6.png) 

## 案例相关材料 
相关材料下载链接：[Kobe 投篮预测 Demo 材料](https://main.qcloudimg.com/raw/c16f2f3c736e434b63341db6026d7425/kobe.zip)。 
该材料包含以下文件： 
- classifier.py：分类模型的分类器文件，用于模型分类。 
- data_cleaning.py：数据预处理阶段的数据清洗代码。 
- data_transformation.py：数据特征转换代码。 
- feature_selection.py：数据特征选择代码。 
- kobe.csv：kobe 投篮具体特征信息的数据集文件。 
请用户下载该案例所需全部材料，并保存到本地以便后面搭建工作流需要。 

## 整体流程 
该 Demo 的整体流程如下： 
<img src="https://main.qcloudimg.com/raw/2d53e3facc1f39457fd33196853e5b4d.png" style="zoom:50%;" />

>!您可以按需自行配置资源参数，不同资源实例类型对应的价格不同。选择资源时，您可以参看资源参数右上角的**计费说明**。



## 详细流程 

#### 一. 上传数据
本案例通过本地数据节点上传所需数据： 
1. 在 [腾讯云 TI 平台 TI-ONE 控制台](https://console.cloud.tencent.com/tione/project/list) 的左侧导航栏，选择【输入】>【数据源】>【 本地数据】，拖入画布中 。
2. 选中【本地数据】，右侧栏会出现节点信息，单击算法 IO 参数中的【数据文件】 上传【案例相关材料】的 kobe.csv。 
3. 修改 COS 路径： 
目标 COS 路径支持用户自定义修改，请将此处修改为`${cos}/kobe_predict/`，否则后续运行系统会报找不到文件的错误。

<img src="https://main.qcloudimg.com/raw/2d97b53fcfed54e383c94259165a10b9.png" style="zoom:50%;" />
<img src="https://main.qcloudimg.com/raw/f5a45bade44051748c46de9484f0ca00.png" style="zoom:78%;" />


#### 二. 数据清洗
此数据清洗功能由【案例相关材料】中的清洗代码 data_cleaning.py 提供，所以此处主要向用户展示如何将自行编写的代码融入工作流中： 
1. 在腾讯云 TI 平台 TI-ONE 控制台的左侧导航栏，选择【框架】>【深度学习】>【 TensorFlow】。 
2. 将【TensorFlow】拖入画布中，并右键单击重命名为“数据清洗”。 
3. 填写参数： 
 - 【组件参数】中的“程序脚本”：上传文件 `data_cleaning.py`详见【案例相关材料】。 
 - 其余参数均可默认。 

<img src="https://main.qcloudimg.com/raw/2a022e929416c1e031f3d3dc431afbd4.png" style="zoom:50%;" />


#### 三. 特征转换
1. 在腾讯云 TI 平台 TI-ONE 控制台的左侧导航栏，选择【框架】>【深度学习】>【 TensorFlow】。 
2. 将【 TensorFlow】拖入画布中，并右键重命名为“特征转换”。 
3. 填写参数： 
 - 程序脚本：上传文件 `data_transformation.py`详见【案例相关材料】。 
 - 其余参数均可默认。 

<img src="https://main.qcloudimg.com/raw/5cebb60df22010b6611f3a37cc1e3832.png" style="zoom:50%;" />

#### 四. 特征选择
此特征选择功能亦由【案例相关材料】中的相关代码 feature_selection.py 提供： 
1. 在 [腾讯云 TI 平台 TI-ONE 控制台](https://console.cloud.tencent.com/tione/project/list) 的左侧导航栏，选择【框架】>【深度学习】>【TensorFlow】。 
2. 将【TensorFlow】拖入画布中，并右键单击重命名为“特征选择”。 
3. 填写参数： 
 - 程序脚本：上传文件 `feature_selection.py` 详见【案例相关材料】。 
 - 其余参数均可默认。 

<img src="https://main.qcloudimg.com/raw/ed656a7d739db690b1449b3840db4b47.png" style="zoom:50%;" />


#### 五. 分类器
此分类器功能亦由【案例相关材料】中的相关代码`classifier.py`提供： 
1. 在腾讯云 TI 平台 TI-ONE 台控制台的左侧导航栏，选择【框架】>【深度学习】>【TensorFlow】。 
2. 将【TensorFlow】拖入画布中，并右键重命名为“分类器”。 
3. 填写参数： 
 - 程序脚本：上传文件 `classifier.py` 详见【案例相关材料】。 
 - 其余参数均可默认。 

<img src="https://main.qcloudimg.com/raw/b0bee0859c870ab74c477281e02ebb46.png" style="zoom:50%;" />

#### 六. 模型评估
1. 在腾讯云 TI 平台 TI-ONE 控制台的左侧导航栏下方，搜索【二分类任务评估】，并拖入画布中。 
2. 单击【二分类任务评估】，在右侧弹框中单击【高级设置】，此处需要手动填写【输入数据】路径（请直接复制填写）：`${cos}/kobe_predict/result.csv`，其余路径根据 IO 连线自动生成。
3. 填写算法 IO 参数：  
 - 标签列：0。 
 - 是否是打分项：否。 
 - 输入数据是否包含 header 信息：否。 
 - 输入数据分隔符：空格。
 - 预测列：1。
 - 其余参数可默认。 

<img src="https://main.qcloudimg.com/raw/2d53e3facc1f39457fd33196853e5b4d.png" style="zoom:50%;" />
<img src="https://main.qcloudimg.com/raw/354e800405376785e4f9d9f656bff412.png" style="zoom:50%;" />


#### 七. 运行调度及模型评估
单击画布上方运行按钮可运行工作流，详情请参考 [运行工作流](https://cloud.tencent.com/document/product/851/34007)。 
运行成功后，右键单击【二分类任务评估】>【评估指标】，即可查看模型效果。
![](https://main.qcloudimg.com/raw/2e2d3809a2bf48bba481a2393c7822da.png)
<img src="https://main.qcloudimg.com/raw/2d53e3facc1f39457fd33196853e5b4d.png" style="zoom:50%;" />
