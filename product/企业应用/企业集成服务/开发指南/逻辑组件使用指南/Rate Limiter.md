## 简介

Rate Limiter 属于流控频控类组件，其作用是限制单位时间内（秒、分钟）通过 Rate Limiter 的总次数，从而达到控制流量大小的效果。
Rate Limiter 使用的算法为令牌桶算法，会以一定速度匀速地补充令牌（如：限制每分钟执行10次，则每6秒补充一个令牌）。Rate Limiter 允许在有令牌积累的情况下，短时间内峰值流量达到设置的最大处理次数的两倍。

## 操作配置

### 参数配置

| 参数         | 数据类型 | 描述                                       | 是否必填 | 默认值   | 备注                                                         |
| ------------ | :------- | :----------------------------------------- | :------- | -------- | ------------------------------------------------------------ |
| 时间单位     | 下拉选择 | 限流的时间单位，可选“秒”、“分”             | 是       | 无       |      -                                                        |
| 最大处理次数 | int      | 单位时间内允许的最大处理次数               | 是       | 无       | 在有令牌积累的情况下，短时间内允许的峰值流量为最大处理次数的两倍。 |
| 限流策略     | 单选框   | 可选择“拒绝处理”或者“在xx秒内处理超限部分” | 是       | 拒绝处理 | “拒绝处理”：获取不到令牌直接报错。“在xx秒内处理超限部分”：获取不到令牌时，根据获取令牌所需要的时间进行排队等待，达到削峰填谷的效果。 |

### 界面配置

<img src="https://qcloudimg.tencent-cloud.cn/raw/4beb544305085335274091b01396fd88.png" alt="https://qcloudimg.tencent-cloud.cn/raw/4beb544305085335274091b01396fd88.png" style="zoom:50%;" />

### 输入 message

| message 属性 | 值                                        |
| ----------- | ----------------------------------------- |
| payload     | 继承 Rate Limiter 上一个组件的 payload 信息。   |
| error       | 继承 Rate Limiter上一个组件的 error 信息。     |
| attribute   | 继承 Rate Limiter 上一个组件的 attribute 信息。 |
| variable    | 继承 Rate Limiter 上一个组件的 variable 信息。  |

### 输出 message

| message 属性 | 值                                                           |
| ----------- | ------------------------------------------------------------ |
| payload     | 若能够获取到令牌，payload 的结果为继承 Rate Limiter 上一个组件的 payload。 |
| error       | “直接拒绝”策略下，获取不到令牌，错误信息为”获取不到令牌，触发限流“。”在xx秒内处理超限部分“策略下，超过最大等待时间，错误信息为”获取令牌所需要的时间超过最大等待时间，触发限流“ |
| attribute   | 若能够获取到令牌，attribute 的结果为继承 Rate Limiter 上一个组件的 attribute。 |
| variable    | 若能够获取到令牌，variable 的结果为继承 Rate Limiter 上一个组件的 variable。 |

## 配置案例
### 拒绝处理

- 配置：限制每分最大处理2次。选择“拒绝处理”。

   <img src="https://qcloudimg.tencent-cloud.cn/raw/587cfdb5541eb58b69e218832a2bde7f.png" alt="https://qcloudimg.tencent-cloud.cn/raw/587cfdb5541eb58b69e218832a2bde7f.png" style="zoom:50%;" />

- 若获取不到令牌。

   <img src="https://qcloudimg.tencent-cloud.cn/raw/55cccd2f6a0ef565d486aba41403939a.png" alt="https://qcloudimg.tencent-cloud.cn/raw/55cccd2f6a0ef565d486aba41403939a.png" style="zoom:50%;" />


### 在xx秒内处理超限部分

- 配置：限制每分最大处理2次。选择：“在2分内处理超限部分”。

   <img src="https://qcloudimg.tencent-cloud.cn/raw/0d65e86737a51105b27cd23e02c6aea5.png" alt="https://qcloudimg.tencent-cloud.cn/raw/0d65e86737a51105b27cd23e02c6aea5.png.png" style="zoom:50%;" />


- 若获取不到令牌，并且超过最大等待时间。

   <img src="https://qcloudimg.tencent-cloud.cn/raw/f05bd745c8eaac6941abceb7f0e1a4b6.png" alt="https://qcloudimg.tencent-cloud.cn/raw/f05bd745c8eaac6941abceb7f0e1a4b6.png" style="zoom:50%;" />

   
