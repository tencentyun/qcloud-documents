## 背景

在日志服务（Cloud Log Service，CLS）使用场景里，从其他日志工具迁移到 CLS 是非常常见的情况。其中，存在用户使用 Grafana 做可视化监控工具，例如 ES + Grafana 的组合。当数据源迁移到 CLS 后，用户依托 Grafana 制作的各种仪表盘资源，搭建的运维工具和平台就都失去了作用。为了避免重建这套体系，需要 CLS 对接 Grafana，替换 ES 数据源。

<img src="https://qcloudimg.tencent-cloud.cn/raw/63698c622e1a382f685777d67334e3c6.png" style="width: 35%"/>

## 安装 CLS-Grafana 插件

CLS 数据源由腾讯云日志服务团队进行维护，已经通过 [官方签名认证](https://grafana.com/grafana/plugins/tencentcloud-monitor-app/)，可以在 Grafana 设置页面一键安装。

具体接入步骤请参考 [CLS 对接 Grafana](https://cloud.tencent.com/document/product/614/52102)。


## 使用 CLS 数据源替换 ES 数据源

### 数据源配置区域对比

- **ES 数据源：**查询语句界面分为顶部的 **Query输入区**和其余的**辅助输入功能区**。 Query 输入区可输入 Lucene 语句，用于对日志进行过滤。辅助输入区通过单击填写，生成 DSL 内容，用于数据聚合，相当于 CLS 的 SQL。
![](https://qcloudimg.tencent-cloud.cn/raw/01b25e1f6dde882285414e2576eb97e2.png)
- **CLS 数据源：**查询语句界面分为**地域与日志主题**选择和**检索分析语句**两个部分。地域与日志主题选择模块可以快速进行日志主题切换，而检索分析语句则用于输入 CLS 查询语句。
CLS 查询语句分为 Lucene 和 SQL 两个部分，两个部分之间使用管道符 “|” 进行分隔。其中 Lucene 部分和 ES 的 Query 输入区内容相同。SQL 输入内容除了支持标准的 SQL 语法外，还支持大量的 SQL 函数，SQL 区域内容和 ES 输入区的辅助输入模块完成对标。更多请参考的 [CLS 语法规则](https://cloud.tencent.com/document/product/614/47044)。
![](https://qcloudimg.tencent-cloud.cn/raw/f2476d55d642da05acf4fb3115985d82.png)


### 操作实践

#### 统计日志条数

对于想要绘制随时间变化的日志条数，ES 数据源将 Metric 选中 Count，GroupBy 选中 Histogram。CLS 的检索语句可以使用  Histogram 结合聚合函数 Count 完成。 类似的，对于 Max、Min、Distinct 等其他 [通用聚合函数](https://cloud.tencent.com/document/product/614/60028) 使用上也完全一致，直接将 Count 函数进行替换即可。
![](https://qcloudimg.tencent-cloud.cn/raw/7bf828cd427a2ed53ffc8b7b50b8b594.png)

#### 查看原始日志

想要直接查看符合条件的日志，ES 数据源需要将 Metric 选中 Logs 模式，而 CLS 只需要输入对于的 Lucene 语句即可。输入语句比对：
![](https://qcloudimg.tencent-cloud.cn/raw/299cd9b4a8685ee6fa0e8d7a3a32a92e.png)
展示效果： 
![](https://qcloudimg.tencent-cloud.cn/raw/4cdd928564a391ff32aa874564476701.png)


#### 聚合统计 - 错误码占比

根据错误码进行聚合，展示各个错误码的日志数量。此处可以看到，语句中包含变量 $path。CLS 数据源插件进行了变量功能的相关适配，允许直接使用 Grafana 的变量能力。
>! 绘制饼图时右侧图表选项请选择 **ValueOptions-AllValues**。
>
![](https://qcloudimg.tencent-cloud.cn/raw/baf6b2a1cdc9fcb0d48b7e87fc858f6f.png)
展示效果： 
![](https://qcloudimg.tencent-cloud.cn/raw/74de498cd7f9b0eb6937331416972bc5.png)

#### 聚合统计 - Top5请求的数量变化情况

ES 数据源中，GroupBy 聚合选项允许填写 Size 值，支持选中出现频率最高的N个值，再进行聚合。
此情况在 CLS 数据源 SQL 中，可以通过 having 语句搭配嵌套子查询实现。
```
*|select histogram( cast(__TIMESTAMP__ astimestamp),interval1hour)as analytic_time,"action",count(*)as countgroupby analytic_time,"action"having"action"in(selectactiongroupbyactionorderbycount(*)desclimit5)orderby analytic_time limit1000
```
![](https://qcloudimg.tencent-cloud.cn/raw/ee245c981ffbe2d3cc58eb38b0c9e737.png)
查询结果可以看到，图中共有5条曲线。
![](https://qcloudimg.tencent-cloud.cn/raw/9221a6d08ab30124560bc65047ea1f89.png)
通过以上的语句搭配使用，已经可以满足大部分的检索分析场景。

#### 统计接口耗时的分段情况

在 ES 数据源仪表盘中，有一个配置项繁多，但场景适用广的例子：根据不同的时间范围，绘制在这个时间范围的请求数量。
这个案例，统计了接口在0到500ms，500ms到2s，2s到5s，以及大于5秒的请求个数。 
![](https://qcloudimg.tencent-cloud.cn/raw/30c17a0247665c0f7479c2397c6729d2.png)

对应的，迁移到 CLS 数据源，也可以使用类似的多条语句进行绘制。但 CLS 本身的 SQL 能力更强，可以将相关的统计处理合并成一条 SQL 语句：
![](https://qcloudimg.tencent-cloud.cn/raw/82279d01cc1349296896413f858761e8.png)
```
urlPath:$path AND region:$region AND action:$action AND returnCode:$returnCode | select histogram( cast(__TIMESTAMP__ as timestamp),interval 1 minute) as analytic_time ,count_if(timeCost<=200) as "0~500ms" ,count_if(500<timeCost and timeCost <=2000) as "500ms~2s" ,count_if(2000<timeCost and timeCost <=5000) as "2s~5s" ,count_if(5000<timeCost) as "超过5s" group by analytic_time order by analytic_time limit 1000
```

类似的场景，我们也可以写出使用估算函数 approx_percentile 分析得出的耗时相关情况。
![](https://qcloudimg.tencent-cloud.cn/raw/59b5c0cd3133fdfa16161c4b3daa91f5.png)
```
urlPath:$path AND region:$region AND action:$action AND returnCode:$returnCode  | select time_series(__TIMESTAMP__, '$__interval', '%Y-%m-%dT%H:%i:%s+08:00', '0') as time ,avg(timeCost) as avg ,approx_percentile(timeCost, 0.50) as P50 ,approx_percentile(timeCost, 0.90) as P90 ,approx_percentile(timeCost, 0.95) as P95 group by time order by time limit 10000
```

#### 模板变量能力

在以上的案例中，不同程度的出现了 Grafana 变量功能的身影。对于变量功能，Grafana 变量的类型种类繁多。常量类型、Textbox 输入框类型对各类数据源来说，是完全相同的，无需进行迁移。这里主要介绍如何迁移 Query 类型变量。

**ES 版本的 $action 变量**：用于展示出现的接口种类，ES 数据源的版本使用 DSL 进行描述，语义上是找到符合 query 条件为`urlPath:$path AND region:$region`的内容，再选取 action 字段，并按照出现次数排序。 
![](https://qcloudimg.tencent-cloud.cn/raw/8f0e9a4afd8e1fc692baca39bae24d89.png)

**CLS 版本的 $action 变量**：使用体验上与在图表编辑的输入行为上，保持一致。选择服务类型为日志服务并选中对应的日志主题后，输入 SQL 语句，即可达到相同效果。
![](https://qcloudimg.tencent-cloud.cn/raw/ec24b032df11d72e95c75aacadee9164.png)

除了使用 CLS 的检索语句进行变量查询，还可以使用云监控的资源查询功能，将腾讯云上的服务资源，作为列表内容进行展示。功能文档可查看 [云监控数据源模板变量功能](https://cloud.tencent.com/document/product/248/54510)。 如使用语句：
```
Namespace=QCE/CLS&Action=DescribeInstances&Region=$region&display=${TopicName}/${TopicId}
```
查询日志主题列表：
![](https://qcloudimg.tencent-cloud.cn/raw/bca65a8312681c5744c0396d927c383b.png)

#### 合并不同地域的请求数据内容

在原本的实现中，部分用户会存在所有数据都存储在同一台 ES 实例上的情况。在使用 CLS 之后，采用就近原则创建了多个日志主题。此时，用户可能会想要将多个日志主题内容合并到图表中。
对于3条来自不同地域的日志查询：
![](https://qcloudimg.tencent-cloud.cn/raw/01a8b657282cdfa747c13caa9ed5f89e.png)
我们可以使用 Transform 模块，实现数据求和的效果，并选用需要的图表进行展示。 
![](https://qcloudimg.tencent-cloud.cn/raw/acc021db37a1015b031301608baa90ea.png)

### 总结

对于存量的 ES 仪表盘，重复以上的迁移步骤，就可以将一个 ES 数据源的仪表盘，完全转化成为 CLS 数据源的仪表盘。
ES 到 CLS 数据源的迁移，可以让用户从自建 ELK 迁移到腾讯云日志服务后，积累的可视化资源得到继续的利用。
转化之后的仪表盘，不仅在能力上完全对标ES数据源版本，还可以结合数据源插件的一些其他能力（如云监控模板变量），更好地与腾讯云生态进行融合。
