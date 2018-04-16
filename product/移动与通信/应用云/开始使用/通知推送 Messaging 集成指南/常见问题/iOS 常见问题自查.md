### iOS 是否支持离线保存？
苹果默认支持离线保存一条消息。关于离线保存的时长苹果官方文档没有明确的说明。

### 为何每天看到的全量推送的实发量会有波动，有时高有时低？ 
信鸽后台会根据每天推送时，apns 返回的错误来清理已经过期的无效 Token。这个清理每天都会执行一次，因此第二天的全量推送实发量是已经除去了前一天的过期 Token 的数量，可能会比前一天的实发量少。这是属于正常现象。

### 初始化信鸽接口，出现如下日志 2017-10-26 15:13:38.888951+0800 XG-Demo [2295:1737660] [xgpush]  服务器返回码: 20 
在初始化信鸽的方法中 appid 和 appkey 不要使用宏定义。

### 什么情况会出现推送暂停
每小时最多可创建 30 条全量推送，超过 30 条的推送将被推送暂停，一小时内创建推送内容完全一样的推送，将被推送暂停，推送暂停的任务将不会下发，请视情况重新创建推送。

### 上传证书到管理台失败
#### 验证失败，请刷新后重试
用编辑器打开证书文件，找到 friendlyname 字段如果同行有？，将其修改成别的，保存后重新上传。

#### 不包含 push 参数
制作新的推送证书

#### 文件大小为 0 kb，不能上传
重新转换 pem 格式，信鸽证书制作教程：[iOS 推送证书设置指南](https://cloud.tencent.com/document/product/666/14860) 。

### 终端出现"Error Domain=NSCocoaErrorDomain Code=3000 "未找到应用程序的“aps-environment”的授权字符串" UserInfo=0x16545fc0 {NSLocalizedDescription=未找到应用程序的“aps-environment”的授权字符串}"错误
这是由于 App 证书没有推送权限引起的。请重新配置证书。

### 设备收到消息没有进入回调
iOS 10 会进静默通知的回调方法中。

### 设置/删除标签的时候出现如下错误 exception.name= WupSerializableException exception.reason= -[XGJceOutputStream writeAnything:tag:required:], 349: assert(0) fail!
请在 registerDevice 之后再 setTag/delTag.在 registerDevice 之前进行 tag 操作会出现这个错误。

### Token 和别名（account）的对应关系
一个设备一个 token，token 在注册推送时由苹果下发，一个 token 最多绑定一个 account，一个 account 最多绑定 15 个 token，超出数量时会顶替之前绑定的 token。iOS 的 token 是会变化的，卸载，重装，刷机，重置都会导致 token 发生变化。

### 创建推送成功了，但推送列表没有该条推送的记录
推送列表只展示针对所有设备和批量设备的推送记录。

### 如何播放自定义通知音？
把音频文件放到 bundle 目录下，创建推送时，给 sound 字段传入音频文件名称。

### 使用信鸽服务端 SDK，怎么创建静默推送？
给参数 content-available 赋值 1，同时不使用 setalert。
