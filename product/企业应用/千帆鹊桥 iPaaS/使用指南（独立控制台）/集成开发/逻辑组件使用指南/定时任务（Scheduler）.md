##  简介
定时任务（Scheduler）作为触发器，用于按设定的规则定时触发一条流。图形化 Scheduler 支持以下三种触发模式：
- 单次触发：支持选择多个指定的时间点触发。
- 周期触发：按照固定的周期触发。
- Cron 表达式：配置中包含一条或多条 Cron 规则，当任意一条 Cron 规则与当前时间匹配时，该定时器所在的集成流将被触发。

## 操作配置
### 参数配置

| 参数       | 数据类型 | 描述                                             | 是否必填 | 默认值              |
| --------- | ------- | ----------------------------------------------- | ------- | ------------------- |
| 触发模式   | Int      | 设置触发模式：单次触发，周期触发，Cron表达式     | 是       | 0（Cron表达式模式） |
| Cron 表达式 | string   | 设置触发规则，例如每分钟触发1次等                | 是       | 无                  |
| 时区       | string   | 指定时区                                         | 是       | 亚洲/北京 UTC+08:00           |
| 仅在上次任务执行完后触发   | bool     | 若勾选则仅在上次任务执行完后触发 | 否       | false               |

Scheduler 包含一条或多条 Cron 规则，当存在多条规则时，使用 `\r` 分隔，Cron 表达式的配置规则如下：

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

- `*` 表示任意匹配，例如 `hours="*"` 表示每个小时。
- `-` 表示范围，例如 `weekdays="1-5"` 表示周一至周五。
- `,` 表示并列，例如 `months="1,3,5,7,8,10,12"` 表示大月。
- `/` 表示增量，例如 `hours="8/2"` ，表示8点开始，每两个小时。
- `L` 表示最后一个，例如 `weekdays="6L"` ，表示当月最后一个周六。
- `?` 表示不指定。这里有一个约束，即年月日和星期几中至少要有一个为不指定。这是为了避免冲突，例如同时指定2020年2月20日（原本周四）和周三。默认星期几是不指定的。

### 配置界面

<img src="https://qcloudimg.tencent-cloud.cn/raw/29d7750cb0e6f3b257578f5503241054.png" alt="https://qcloudimg.tencent-cloud.cn/raw/29d7750cb0e6f3b257578f5503241054.png" style="zoom:50%;" />

### 输出

Scheduler 作为 trigger 组件，是集成流的第一个组件，Scheduler 会生成一个空的 message 消息，触发集成流的运行。

组件输出的 message 信息如下：

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 空，没有值存在                                               |
| error       | <ul><li>执行成功后，error 为空</li><li>执行失败后，error 为 dict 类型，包含“Code”和“Description”字段：“Code”字段表示错误类型，“Description”字段表示错误具体信息</li></ul> |
| attribute   | 空，没有值存在                                               |
| variable    | 空，没有值存                                                 |

### 数据预览
<img src="https://qcloudimg.tencent-cloud.cn/raw/81f7584e35c5f7c59d9deee55ce54dd8.png" alt="https://qcloudimg.tencent-cloud.cn/raw/81f7584e35c5f7c59d9deee55ce54dd8.png" style="zoom:50%;" />

## 案例
### 周期触发模式
每30秒触发一次：
<img src="https://qcloudimg.tencent-cloud.cn/raw/1972ae04ae9bf34e0c4a98067a52980e.png" alt="https://qcloudimg.tencent-cloud.cn/raw/1972ae04ae9bf34e0c4a98067a52980e.png" style="zoom:50%;" />

### 单次触发模式
2023年1月1日0时0分0秒触发一次：
<img src="https://qcloudimg.tencent-cloud.cn/raw/d7da174f8f6fbe9d12d4c25b6a82b3e6.png" alt="https://qcloudimg.tencent-cloud.cn/raw/d7da174f8f6fbe9d12d4c25b6a82b3e6.png" style="zoom:50%;" />


### Cron 表达式模式
每5分钟触发一次：
<img src="https://qcloudimg.tencent-cloud.cn/raw/d94891fadc4ae258f85793e40d4cb072.png" alt="https://qcloudimg.tencent-cloud.cn/raw/d94891fadc4ae258f85793e40d4cb072.png" style="zoom:50%;" />

