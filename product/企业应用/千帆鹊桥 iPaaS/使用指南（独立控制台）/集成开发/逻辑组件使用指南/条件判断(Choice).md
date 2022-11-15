## 简介

**条件判断**（Choice）是分支选择语句，基于不同的条件执行不同的动作，类似于 if-else。

条件判断包含两类子节点，“条件分支”和“默认分支”，在条件判断中可以添加多个条件分支节点，每个条件分支节点中都包含一个真值表达式，条件判断组件会对条件分支节点依次逐个判断真值，直到第一个真值表达式满足条件，则执行该条件分支节点中配置的子流。当所有的When条件都无法匹配时，会执行默认分支的动作。

## 操作说明

#### 表达式模式参数配置

在 When 节点中，可以配置条件语句，用来控制分支选择。

| 参数   | 数据类型 | 描述                  | 是否必填 | 默认值 |
|:-----|:-----|:--------------------|:-----|-----|
| 执行条件 | bool | 条件判断，当条件满足时，执行对应的子流 | 是    | 无   |





#### 表达式模式配置界面

<img src="https://qcloudimg.tencent-cloud.cn/raw/38503fb8c0c92ad6aa8b88d8b9198973.png" width="900px"/>


#### 列表模式参数配置

图形化地配置多组比较条件，多组条件之间可以通过逻辑运算符"OR或者"AND"连接。

| 参数   | 数据类型 | 描述                  | 是否必填 | 默认值 |
|:-----|:-----|:--------------------|:-----|-----|
| 值 | any | 值 | 是    | 无   |
| 条件 | 枚举 | 条件，即比较运算符 | 是    | 无   |

#### 列表模式配置界面

<img src="https://qcloudimg.tencent-cloud.cn/raw/3373d10c2e47a21423b43d7ff87ad25e.png" width="500px"/>


#### 数据预览
无

#### 输入到子流中的 Message
完全继承于主流当前的 Message。

#### 输出
完全输出子流最终输出的 Message，包括错误。

## 案例

在该案例中，我们将 score 映射为不同的 level：
- 当 score 大于等于90时，level 为“A”。
- 当 score 大于等于80、小于90时，level 为“B”。
- 当 score 大于等于60、小于80时，level 为“C”。
- 当 score 小于60时，level为“D”。


1. 添加条件判断组件。<br>
<img src="https://qcloudimg.tencent-cloud.cn/raw/cb22d51bd6bf94dd5caabb0b3965fec7.png" width="500px"/>

2. 在现有条件分支的上面，可以添加新的条件分支节点，每个条件分支对应一个 level。
<img src="https://qcloudimg.tencent-cloud.cn/raw/13c3daf922892ff06bc417593e56265f.png" width="900px"/>

3. 在对应的条件分支中设置 level。例如：score >= 90的分支，设置 level 为“A”。
<img src="https://qcloudimg.tencent-cloud.cn/raw/3914d049bef6cb56d2a5a4b5840cb2ab.png" width="900px"/>

4. 配置完成执行单元测试。当 score 值为70时，条件判断执行第三个分支，level 设置为“C”。
![img_39.png](https://qcloudimg.tencent-cloud.cn/raw/9c009ee98e05253ef159a15f64f048cc.png)
显示如下：
![img_40.png](https://qcloudimg.tencent-cloud.cn/raw/60c3979118ee084a62a122fa324a1473.png)
