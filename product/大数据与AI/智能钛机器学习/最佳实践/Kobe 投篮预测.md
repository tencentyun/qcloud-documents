# 科比投篮预测

## 场景背景

科比在 2016 年 4 月 12 日星期三的最后一场比赛中为洛杉矶湖人队得到 60 分，标志着他从 NBA 退役。从 17 岁入选 NBA，科比在他的职业生涯中获得了无数的赞誉。
使用 20 年有关科比的投篮命中和投失数据，您能预测哪些投篮能命中篮筐吗？本案例非常适合实践分类基础知识、特征工程和时间序列分析。
训练数据包含了科比在他 20 年职业生涯中所尝试的每个投篮命中的位置和情况。您的任务是训练模型来预测每次投篮是否会投进。

**字段如下：**

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

## 案例相关材料

相关材料下载链接：

[kobe投篮预测demo资料](https://main.qcloudimg.com/raw/7e333d78c73d191bb42f54f1e4c7d390.zip)

## 整体流程

该 Demo 的整体流程如下图所示：

![https://main.qcloudimg.com/raw/d117825267ae3f674b1bbab1e81a3566.png](https://main.qcloudimg.com/raw/d117825267ae3f674b1bbab1e81a3566.png)



本场景共包含6个环节，分别是：

| 1.   | 数据准备       |
| ---- | -------------- |
| 2.   | 将数据进行清洗 |
| 3.   | 数据特征转换   |
| 4.   | 数据特征选择   |
| 5.   | 生成模型       |
| 6.   | 模型评估       |



## 前提条件

- 已完成 [开通服务](https://cloud.tencent.com/document/product/851/19055)
- 已完成 [新建工程和工作流](https://cloud.tencent.com/document/product/851/19069)

## 详细流程

### 1. 上传数据

本案例通过本地输入上传数据

1.在智能钛控制台的左侧导航栏，选择【输入】>【数据源】>【 本地数据】，拖入画布中

![https://main.qcloudimg.com/raw/b24b02d72133c48c2cc2540ee646f262.png](https://main.qcloudimg.com/raw/b24b02d72133c48c2cc2540ee646f262.png)

2.上传数据文件kobe.csv

![https://main.qcloudimg.com/raw/2bc04f30ae29e16e38828c493184f6aa.png](https://main.qcloudimg.com/raw/2bc04f30ae29e16e38828c493184f6aa.png)

3.修改cos路径

目标cos路径自动生成，支持修改，这里修改为：${cos}/kobe_predict/

![https://main.qcloudimg.com/raw/f165f10f58424c853d17066a82842b24.png](https://main.qcloudimg.com/raw/f165f10f58424c853d17066a82842b24.png)

### 2.数据清洗

1.在智能钛控制台的左侧导航栏，选择【组件】>【深度学习】>【 TensorFlow Job】

2.将【 TensorFlow Job】组件拖入画布中，右键单击该组件重命名为：数据清洗

3.填写参数， 其余参数均可默认：

> 程序脚本：上传文件data_cleaning.py

![https://main.qcloudimg.com/raw/62c0721772444dce584137a996834ff2.png](https://main.qcloudimg.com/raw/62c0721772444dce584137a996834ff2.png)

> Python版本：选择Python3.5

![https://main.qcloudimg.com/raw/66c909a8d8322241511b7850a3b2b4c2.png](https://main.qcloudimg.com/raw/66c909a8d8322241511b7850a3b2b4c2.png)

### 3.特征转换

1.在智能钛控制台的左侧导航栏，选择【组件】>【深度学习】>【 TensorFlow Job】

2.将【 TensorFlow Job】组件拖入画布中，右键单击该组件重命名为：特征转换

3.填写参数， 其余参数均可默认：

> 程序脚本：上传文件data_transformation.py

![https://main.qcloudimg.com/raw/694c903c3af1839640f393e25958feb8.png](https://main.qcloudimg.com/raw/694c903c3af1839640f393e25958feb8.png)

> Python版本：选择Python3.5

### 4.特征选择

1.在智能钛控制台的左侧导航栏，选择【组件】>【深度学习】>【 TensorFlow Job】

2.将【 TensorFlow Job】组件拖入画布中，右键单击该组件重命名为：特征选择

3.填写参数， 其余参数均可默认：

> 程序脚本：上传文件feature_selection.py

![https://main.qcloudimg.com/raw/d93eb137811e0bf40f5addb6e695c36f.png](https://main.qcloudimg.com/raw/d93eb137811e0bf40f5addb6e695c36f.png)

> Python版本：选择Python3.5

### 5.分类器

1.在智能钛控制台的左侧导航栏，选择【组件】>【深度学习】>【 TensorFlow Job】

2.将【 TensorFlow Job】组件拖入画布中，右键单击该组件重命名为：分类器

3.填写参数， 其余参数均可默认：

> 程序脚本：上传文件classifier.py

![https://main.qcloudimg.com/raw/9fa50daf0b271ee81a01819f21f70028.png](https://main.qcloudimg.com/raw/9fa50daf0b271ee81a01819f21f70028.png)

> Python版本：选择Python3.5

### 5.模型评估

1.在智能钛控制台的左侧导航栏，选择【输出】>【模型评估】>【 BinaryEvaluator】

2.将【 BinaryEvaluator】组件拖入画布中

3.填写参数， 其余参数均可默认：

> 输入数据：${cos}/kobe_predict/result.csv
>
> 标签列：0
>
> 预测列：1
>
> 抽样率：1.0
>
> 并行数：10
>
> 预测阈值：0.5

![https://main.qcloudimg.com/raw/b1460953cd4668e6b3a32fd11fb14fd6.png](https://main.qcloudimg.com/raw/b1460953cd4668e6b3a32fd11fb14fd6.png)

![https://main.qcloudimg.com/raw/ff49584b3630485723ccc723bb8982e8.png](https://main.qcloudimg.com/raw/ff49584b3630485723ccc723bb8982e8.png)

## 操作说明

请放上运行工作流链接
