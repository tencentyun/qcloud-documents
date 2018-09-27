## topic配置说明

新版本CKafka实例支持对topic进行细粒度的参数配置，如下所示：

||参数名||默认值||参数范围||说明||
||cleanup.policy||delete||delete/compact||支持日志按保存时间删除，或者日志按key压缩（kafka connect时需要使用compact模式）|
||min.insync.replicas||1||-||当producer设置request.required.acks为-1时，min.insync.replicas指定replicas的最小数目||
||unclean.leader.election.enable||false||true/false||指定是否能够设置不在ISR中replicas作为leader||
||segment.ms||||1day-7days||Segment分片滚动的时长，单位ms, 最小86400000ms ||
||retention.ms||||60000ms-7days||topic维度的消息保留时间（非独占的实例暂不开放）||
