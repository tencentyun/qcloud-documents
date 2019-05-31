Queue/Topic的原始Log存放于COS对象存储中。创建Queue/Topic时，默认不启动Logging功能，若启动，需要选定某个bucket，bucket由客户自行创建。费用由腾讯云对象存储收取，具体的计费方式请参考 [COS 计费项总览](https://cloud.tencent.com/doc/product/430/5871)。

消息的操作日志以分钟为单位，按照固定的命名规则，生成一个对象写入指定的Bucket中。

日志文件以 json 格式保存，用户可以直接下载文件进行处理。

> 注意：
> 
1) CMQ推送日志到用户的 Bucket 会延迟大约15-30分钟

>2) 考虑到由客户直接分析原生log难度较大，CMQ推出了日志轨迹的能力，即CMQ在用户的原生LOG上聚合出日志轨迹，供快速定位问题
