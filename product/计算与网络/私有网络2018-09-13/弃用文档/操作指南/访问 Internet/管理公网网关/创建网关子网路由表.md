网关子网和普通子网不能关联同一张路由表，需要新建一张独立的网关路由表，并将这张路由表关联到创建的网关子网（路由策略可以只保留默认的 Local 策略）。
1. 创建自定义路由表（可以只保留默认的 Local 策略），详情请参见 [创建自定义路由表](https://cloud.tencent.com/document/product/215/20124)。
2. 配置路由（可选，原因：路由策略可只保留默认的 Local 策略，该路由自动生成），详情请参见 [修改路由表](https://cloud.tencent.com/document/product/215/20123)。
