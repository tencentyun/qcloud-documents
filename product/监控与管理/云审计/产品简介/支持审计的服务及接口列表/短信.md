腾讯云短信（Short Message Service，SMS）沉淀腾讯十多年短信服务技术和经验，为 QQ、微信等亿级平台和10万+客户提供国内短信和国际/港澳台短信服务。国内短信验证秒级触达，99%到达率；国际/港澳台短信覆盖全球200+国家/地区，稳定可靠。腾讯云短信旨在帮助广大开发者快速灵活接入高质量的文本、国际/港澳台短信服务。

下表为云审计支持的短信操作列表：

| 操作名称       | 资源类型       | 事件名称                        |
|------------|------------|-----------------------------|
| 导出发送记录     | consolesms | SMS\_AddDumpLogTask         |
| 取消导出       | consolesms | SMS\_CancelDumpLogTask      |
| 获取应用类型列表   | consolesms | SMS\_GetAllBizList          |
| 获取应用详情     | consolesms | SMS\_GetAPPInfo             |
| 获取应用列表     | consolesms | SMS\_GetAPPList             |
| 获取短信用户回调配置 | consolesms | SMS\_GetCallbackList        |
| 拉频率限制规则    | consolesms | SMS\_GetFreqRule            |
| 频率限制白名单    | consolesms | SMS\_GetFrqWhiteList        |
| 拉取联系人数据    | consolesms | SMS\_GetNewsReceiver        |
| 套餐包列表      | consolesms | SMS\_GetPackageList         |
| 获取告警       | consolesms | SMS\_GetPkgWarningThreshold |
| 获取短信发送列表   | consolesms | SMS\_GetSendList            |
| 获取公告列表     | consolesms | SMS\_GetSMSNotice           |
| 获取短信模版列表   | consolesms | SMS\_GetTPLList             |
| 获取短信签名详细信息 | consolesms | SMS\_GetTPLSignInfo         |
| 短信控制台主页面   | consolesms | SmsQcloudCom                |
