

## 简介

Scheduler 是定时器，用于按设定的规则定时触发一条流。图形化 Scheduler 支持三种触发模式：单次触发、周期触发和 Cron 表达式。
- 单次触发模式：支持选择多个指定的时间点触发。
- 周期触发模式：按照固定的周期触发。
- Cron 表达式模式：配置中包含一条或多条 Cron 规则，当任意一条 Cron 规则与当前时间匹配时，该定时器所在的集成流将被触发。

## 操作配置

### 参数配置

| 参数       | 数据类型 | 描述                                             | 是否必填 | 默认值              |
| :--------- | :------- | :----------------------------------------------- | :------- | ------------------- |
| 触发模式   | Int      | 设置触发模式：单次触发，周期触发，Cron 表达式     | 是       | 0（Cron 表达式模式） |
| Cron表达式 | string   | 设置触发规则，例如每分钟触发1次等                | 是       | 无                  |
| 时区       | string   | 指定时区                                         | 是       | UTC+08:00           |
| 排队调度   | bool     | 若勾选当前有未结束的作业时跳过本次执行，则为 true | 否       | false               |

Scheduler 包含一条或多条 cron 规则，当存在多条规则时，使用“\r”分隔，Cron 表达式的配置规则如下：

| 参数     | 含义                       | 取值范围    |
| -------- | -------------------------- | ----------- |
| seconds  | 秒                         | 0 - 59      |
| minutes  | 分钟                       | 0 - 59      |
| hours    | 小时                       | 0 - 23      |
| days     | 日期（选填，默认每天）     | 1 - 31      |
| months   | 月份（选填，默认每月）       | 1 - 12      |
| weekdays | 星期几（选填，默认不指定） | 1 - 7       |
| years    | 年份（选填，默认每年）     | 1970 - 2099 |

在配置 Cron 表达式时，可使用以下运算符：

| 运算符 | 释义 | 
|---------|---------|
| *| 表示任意匹配，例如：`hours="*"` 表示每个小时。 | 
| - | 表示范围，例如：`weekdays="1-5"` 表示周一至周五。 | 
| , | 表示并列，例如：`months="1,3,5,7,8,10,12"` 表示大月。 | 
| / | 表示增量，例如：`hours="8/2"` ，表示8点开始，每两个小时。 | 
| L | 表示最后一个，例如：`weekdays="6L"` ，表示当月最后一个周六。 | 
| ? | 表示不指定。此处有一个约束，即年月日和星期几中至少要有一个为不指定。该约束是为了避免冲突，例如：同时指定2020年2月20日（原本周四）和周三，默认星期几是不指定的。 | 




### 配置界面

<img src="https://qcloudimg.tencent-cloud.cn/raw/263e5910cc68a4b338c0b614c2ff4b67.png" alt="https://qcloudimg.tencent-cloud.cn/raw/263e5910cc68a4b338c0b614c2ff4b67.png" style="zoom:50%;" />


### 输出
 
Scheduler 作为 trigger 组件，是集成流的第一个组件，Scheduler 会生成一个空的 message 消息，触发集成流的运行。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 空，没有值存在。                                               |
| error       | 执行成功后，error 为空；执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息。 |
| attribute   | 空，没有值存在。                                               |
| variable    | 空，没有值存在。                                                 |

## 案例

### 单次触发模式
2025年1月1日0时0分0秒触发一次    
<img src="https://qcloudimg.tencent-cloud.cn/raw/52a5d128e6b8c3af3a91f366c0ed708c.png" alt="https://qcloudimg.tencent-cloud.cn/raw/52a5d128e6b8c3af3a91f366c0ed708c.png" style="zoom:50%;" />

### 周期触发模式

- 每5秒触发一次 
   <img src="https://qcloudimg.tencent-cloud.cn/raw/48bad66b965fec38b331539df17eabe9.png" alt="https://qcloudimg.tencent-cloud.cn/raw/48bad66b965fec38b331539df17eabe9.png" style="zoom:50%;" />
	 
- 每1分钟的0秒触发一次    
   <img src="https://qcloudimg.tencent-cloud.cn/raw/6a796b0e852975faaea6480a6754c694.png" alt="https://qcloudimg.tencent-cloud.cn/raw/6a796b0e852975faaea6480a6754c694.png" style="zoom:50%;" />
   
### Cron 表达式模式
- 每5分钟触发一次  
   <img src="https://qcloudimg.tencent-cloud.cn/raw/0815a446715582a8da037b3a2eca2c46.png" alt="https://qcloudimg.tencent-cloud.cn/raw/0815a446715582a8da037b3a2eca2c46.png" style="zoom:50%;" />

- 每天8点触发  
   <img src="https://qcloudimg.tencent-cloud.cn/raw/12240eb8729ac58102ed84076f17696b.png" alt="https://qcloudimg.tencent-cloud.cn/raw/12240eb8729ac58102ed84076f17696b.png" style="zoom:50%;" />

