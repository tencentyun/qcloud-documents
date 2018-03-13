message 参数值应为如下所述的 json 字符串，其总长度不能超过 4096 字节。

## 推送通知定义示例
推送通知：默认展示在手机或设备通知栏。
```
{"content":"this is content","title":"this is title", "vibrate":1}
```
### 完整定义

```
{
"title ":"xxx", // 标题，必填
"content ":"xxxxxxxxx", // 内容，必填
"accept_time": //表示消息将在哪些时间段允许推送给用户，选填
[
{
“start”:{“hour”:”13”,“min”:”00”},
”end”: {“hour”:”14”,“min”:”00”}
},
{
“start”:{“hour”:”00”,”min”:”00”},
”end”: {“hour”:”09”,“min”:”00”}
}
],
"n_id":0, //通知id，选填。若大于0，则会覆盖先前弹出的相同id通知；若为0，展示本条通知且不影响其他通知；若为-1，将清除先前弹出的所有通知，仅展示本条通知。默认为0
"builder_id":0, // 本地通知样式，必填
"ring":1， // 是否响铃，0否，1是，下同。选填，默认1
"ring_raw":"ring", // 指定应用内的声音（ring.mp3），选填
"vibrate":1, // 是否振动，选填，默认1
"lights":1// 是否呼吸灯，0否，1是，选填，默认1
"clearable":1, // 通知栏是否可清除，选填，默认1
"icon_type":0 //默认0，通知栏图标是应用内图标还是上传图标,0是应用内图标，1是上传图标,选填
"icon_res":"xg",// 应用内图标文件名（xg.png）或者下载图标的url地址，选填
"style_id":1 //Web端设置是否覆盖编号的通知样式，默认1，0否，1是,选填
"small_icon":"xg"指定状态栏的小图片(xg.png),选填
"action":{ // 动作，选填。默认为打开app
"action_type ": 1, // 动作类型，1打开activity或app本身，2打开浏览器，3打开Intent
"activity ": "xxx"
"aty_attr ": // activity属性，只针对action_type=1的情况
{
"if":0, // 创建通知时，intent的属性，如：intent.setFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_RESET_TASK_IF_NEEDED);
"pf":0, // PendingIntent的属性，如：PendingIntent.FLAG_UPDATE_CURRENT
}
"browser": {"url": "xxxx ","confirm": 1}, // url：打开的url，confirm是否需要用户确认
“intent”: “xxx”
},
"custom_content":{ // 用户自定义的key-value，选填
"key1": "value1",
"key2": "value2"
}
}
```
## 透传消息定义示例
透传消息：可以由 App 识别的任意透传消息命令，比推送通知更灵活。
```
{"content":"this is content","title":"this is title"}
```
### 完整定义

```
{
"title":"xxx", // 标题，选填
"content ":"xxxxxxxxx", // 内容，选填
"accept_time": //表示消息将在哪些时间段允许推送给用户，选填
[
{
“start”:{“hour”:”13”,“min”:”00”},
”end”: {“hour”:”14”,“min”:”00”}
},
{
“start”:{“hour”:”00”,”min”:”00”},
”end”: {“hour”:”09”,“min”:”00”}
}
],
"custom_content":{ // 用户自定义的key-value，选填
"key1": "value1",
"key2": "value2"
}
}
```
