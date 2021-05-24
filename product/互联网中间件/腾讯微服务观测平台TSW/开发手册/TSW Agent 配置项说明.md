当您使用 TSW 提供的 Java Agent 接入服务时，您可修改 config 文件夹中的 agent.conf 中的配置，实现包括服务接入配置、Agent 日志配置、数据采集规则配置的修改。

| 配置名称 | 是否必填 | 默认值|意义 |
| :--- | :---:  | :---: | :--- |
| agent.service_name | 是 | null| 覆盖顺序：用户设置 > spring.application.name > main class所在类名 |
| agent.is_generate_bytecode_file | 否 | false| 是否生成改动后的 class 文件 |
| agent.max_span_name_length | 否 | 50| span name 最大字符长度 |
| agent.report_baggage | 否 | false|是否上报 span 结构中的 baggage 中内容   |
| agent.ignore_suffix | 否 | .jpg、.jpeg、.js、.css、.png、.bmp、.gif、<br>.ico、.mp3、.mp4、.html、.svg |当 requestURI 中出现这些后缀时，不拦截这个请求|
| agent.exception_depth | 否 | 5  | 当出现错误日志时，exception 截取多少层 |
|agent.max_error_log_length |否| 1000| 错误日志最大字符长度|
| agent.use_full_name_as_span_name |否| false|  是否使用全类名+ 参数全类名作为 span name|
|agent.instance_identify  |否| 本机器 IP | ipv4、eth0 网卡 |
|agent.disable_plugins  |否| null |  不采集调用链 plugin |
|agent.instance_properties  |否| null |实例自定义属性，填写示意： [key1:value2;key2:value2] |
|logging.type  |否| file | 日志输出到文件还是控制台：file,system |
|logging.dir  |否| null | 日志输出路径 |
|logging.level  |否| info | 日志输出级别：debug, info, warn, error |
|logging.file_name  |否| apm-agent.log | 日志文件名称 |
|logging.max_file_size  |否| 50MB | 单个日志文件最大容量  |
|logging.max_history_files| 否| 10| 日志历史文件个数|
|sender.etl_ip| 是 |     null   |   数据收集端 IP   |
|sender.etl_port| 是 |    null      |  数据收集端 port   |
|sender.token| 是 |       null   |    收集端鉴权 token   |
|sender.sender_data_path| 否 |      tsw-client-package/sender/    |  本地数据存放路径     |
|sender.trace_max_upload_num| 否 |    2      |  发送 trace 数据使用线程数据量    |
|sender.trace_max_cache_size| 否 |     10\*1024\*1024（10MB）     |   trace 内存缓冲区大小    |
|sender.print_log_interval| 否 |      1000\*60（60min）   |    发送数据日志在 info 级别下打印时间间隔   |
|sender.max_file_size| 否 |      10\*1024\*1024（10MB）    |    磁盘单个数据文件大小   |
|sender.max_storage_size| 否 |      -1（无限制）   |   1024\*1024\*1024（1GB）磁盘单个类型总数据限制   |
|sender.grpc_heartbeat_period| 否 |      20（s）   |    上报连接心跳检查周期   |
|sender.flush_interval| 否 |      1000（ms）  |    磁盘刷盘间隔   |
|scheduled.scheduled_package_scan |  否  | null  | @EnableScheduling 扫描包及子报，注意 @EnableScheduling 与 @Scheduled 需要在同一类|
|spring.controller_package_scan | 否 | null  |     @Controlle/@RestController 扫描包路径   |
|mysql.ignoreinitspan | 否  |   true | 忽略在数据库初始化连接时产生的 span|
