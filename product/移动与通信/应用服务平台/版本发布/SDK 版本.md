

### v1.22.0
- [add] `tcb.registerExtension()`，注册扩展。
- [add] `tcb.invokeExtension()`，使用扩展。
- [add] 签名方式支持 v3选项。

### v1.21.2
- [fix] database aggregate match 操作传参 EJSON 序列化。

### v1.21.1

- [add] request 支持更多细节耗时。
- [add] 支持 getAuthContext。

### v1.20.0
- [add] 新增 TCB 入口静态方法 parseContext（解析云函数 context 参数）。


### v1.19.1
- [fix] database 事务修复 runTransaction api 中 rollback 报错 & 改造 runTransaction 支持自定义返回。


### v1.19.0
- [add] database 新增事务。


### v1.18.0
- [add] wx 支持微信支付云调用。


### v1.17.0
- [fix] database 查询 limit 限制由最大100放至1000。


### v1.16.3
- [fix] 修复 TRIGGER_SRC 变量取值问题。


### v1.16.2
- [fix] 修复 db 函数在 handler 外初始化问题。


### v1.16.1
- [fix] 修复定时触发 API Token 可能失效的问题。


### v1.16.0
- [fix] db 模块替换 lodash 为子模块。
- [fix] db 模块更改 query 传参，为入参必须为对象，且 value 不能均为 undefined。
- [fix] 修复 app.database(env:'xxx') 不生效问题。


### v1.15.0

- [add] 加入执行操作符：expr、jsonSchema。
- [add] 加入逻辑操作符：not。

### v1.14.0
- [add] 新增 cls 日志写入。

### v1.13.0
- [add] 加入查询操作符：all、elemMatch、exists、size、mod。
- [add] 加入更新操作符：push、pull、pullAll、addToSet、rename、max、min。
- [add] 加入 db.command.aggregate.pipeline，用于生产 Aggregate.lookup() 的 pipeline 参数。
- [add] db.command.aggregate.match 支持传入 query。

### v1.12.0
- [add] 加入db.command.project，支持投影操作符。
- [add] 加入db.command.nor。


### v1.11.0
- [add] 新增获取客户端 IP 的接口。
- [add] `auth().getUserInfo()` 返回字段中加入 `customUserId`。


### v1.10.0
- [add] 新增获取登录凭据 Ticket 的接口。


### v1.9.0
- [add] 新增聚合搜索接口。


### v1.8.0
- [add] 新增 getCurrentEnv 方法。


### v1.6.0
- [add] 新增 auth api。
- [add] 文件上传直传。


### v1.4.2
- [fixed] 修复了 doc.set() 对于复杂错误类型的签名错误问题。
- [fixed] db.serverDate() 支持 new 调用。


### v1.4.1
- [fixed] 修复了下载文件接口如果文件名称中有中文会失败的 bug。


### v1.4.0
- [add] 接口加入默认超时时间（15秒）。
- [add] 对超过3秒的数据库慢查询，加入 console.warn。
- [fixed] 修复 serverDate 存取的问题。


### v1.3.0
- [upgrade] 重构了 command 的实现。


### v1.2.2
- [fixed] 修复 GeoPoint 的查询、储存问题。
- [fixed] 修复 db.RegExp 不支持 or 的问题。
- [fixed] 修复 Date 不能使用 query 查询的问题。

### v1.2.1
- [add] 查询支持 db.RegExp
- [fixed] 修复 Date 对象的底层表示，与微信对齐。


### v1.1.8
- [fixed] 修复操作符嵌套报错的问题。


### v1.1.7
- [changed] 正则表达式支持传入 flags。


### v1.1.6
- [add] 查询指令支持正则表达式。


### v1.1.5
- [fixed] 修复了逻辑操作符嵌套使用会报错的 bug。
- [fixed] 修复了 update 嵌套对象部分生效的 bug。


### v1.1.3
- [fixed] 修复了 serverDate 传入参数时的 bug。


### v1.1.3
- [fixed] 修复了数据库读取 serverDate 结构的问题。


### v1.1.2
- [fixed] 修复了数据库 set 的多维对象的操作问题。


### v1.1.0
- [changed] 支持使用多个环境。

### v1.0.31
- [changed] 云函数调用返回的 requestId 可以在云控制台用来查看日志。
- [changed] 数据库地理位置初始化时第一个参数为 longitude，第二个为 latitude。
- [add] 新增条件删除文档接口。


### v1.0.29
- [changed] 更新文档。

### v1.0.24
- [changed] 获取文件下载链接方法参数变更，详情见对应 api 文档。

### v1.0.23
- [fixed] 修复了新增内嵌文档的 bug。


### v1.0.22
- [fixed] update 和 set 传空参数会报错，不再抛出异常。
- [fixed] init 可以传空。
- [changed] 云函数的调用，云函数实际返回的结果从字符串改成了对象，也就是透传云函数返回的结果。


### v1.0.21
- [fixed] update 内嵌文档的操作符使用。


### v1.0.20
- [changed] 修改了集合创建的方法。
- [fixed] 修正了环境 id 的传入 bug。


### v1.0.19
- [changed] 增加了新增集合方法。
- [changed] 增加了文件下载方法。


### v1.0.18
- [changed] 数据库操作的 field() 方法后需要 get() 才能取得数据。
- [changed] 添加了数据库的 serverDate 数据类型。
- [changed] 增加了数据库的更新 (update) 方法的数组操作符 push、pop、shift 和 unshift，增加了 set 指令。
- [changed] 数据库逻辑运算符 and 和 or 支持传入一个数字，作为逻辑运算的参数。

### v1.0.17
- [changed] 对象初始化实例后，init 操作可以传入空参数，这样会使用默认环境。如果需要指定环境(env)或者代理(proxy)，则还是通过 init 方法传入。
- [changed] init 时跟小程序 SDK 保持参数命名一致，envName 改为 env。
- [changed] init 时 mpAppId 不再需要传入。
- [changed] 修复了数据库排序的 bug。
- [changed] 增加了数据库的 count 方法。
- [changed] 修正了文档，修改了文件存储和云函数的返回结果。请参考文档。


### v1.0.9
- [changed] 云函数内使用不需要填写 secretId 和 secretKey，云函数重新部署后生效。
- [changed] 文件上传添加支持 buffer。
- [changed] 修复了嵌套对象的 bug。


