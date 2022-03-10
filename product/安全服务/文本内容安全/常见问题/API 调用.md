### 文本默认 QPS（每秒请求数）是否可以修改？
可以修改，如有需求可以[ 提交工单](https://console.cloud.tencent.com/workorder/category) 申请修改。

### QPS 是针对账号维度的，还是 Biztype 维度的？
QPS 是针对每个主/子账号纬度的每秒请求数，图片默认是100QPS，文本默认1000QPS，所有 Biztype 共享1000QPS。

### 4.0接口 Biztype 字段，可以由用户自己设定吗？
可以由用户自己设定，但需 [提交工单](https://console.cloud.tencent.com/workorder/category) 后台配置才会产生。Biztype 可以是英文字母、数字、下划线的组合，长度为3-32个字符。用户在配置前告知需要配置的格式，一旦配置后，无法更改。

### 4.0接口 Review 字段，是否每个标签都会输出？
只有机审后有分数输出的标签才会输出，广告、二维码等标签则不会输出。
