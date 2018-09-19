### 注册自定义事件
自定义事件的注册（配置）包括事件 ID 的注册和事件 ID 下参数信息的注册。
1. 登录 [MTA 前台](http://mta.qq.com/)，选择左边【应用分析】>【事件分析】>【事件列表】； 
2. 选择【新增事件】，按照需求填写事件 ID、key、value 等信息；
3. 可以在查看详情下的“参数”查看事件 ID 下所有参数上报的明细。

### 【次数统计】Key-Value 参数的事件

```java
void StatService.trackCustomKVEvent(Context ctx, String event_id, 
Properties properties)
```

1. 参数
Ctx ：页面的设备上下文
event_id：事件标识
properties Key-Value：参数对，key 和 value 都是 String 类型
2. 调用位置：代码任意处
```java
public void onOKBtnClick(View v) {
// 统计按钮被点击次数，统计对象：OK按钮
Properties prop = new Properties();
    prop.setProperty("name", " OK ");
    StatService.trackCustomKVEvent(this, " button_click", prop);
}
public void onBackBtnClick(View v) {
// 统计按钮被点击次数，统计对象：back按钮
Properties prop = new Properties();
    prop.setProperty("name", " back ");
    StatService.trackCustomKVEvent(this, " button_click", prop);
}
```

### 【次数统计】带任意参数的事件
1. 参数： 
Ctx：页面的设备上下文
event_id：事件标识
args：事件参数
2. 调用位置：代码任意处
```java
public void onClick(View v) {
// 统计按钮被点击次数，统计对象：OK按钮
    StatService.trackCustomEvent(this, "button_click", "OK ");
}
```

### 【时长统计】Key-Value 参数事件

可以指定事件的开始和结束时间来上报一个带有统计时长的事件。
```java
void StatService.trackCustomBeginKVEvent(
Context ctx, String event_id, Properties properties)
void StatService.trackCustomEndKVEvent(
Context ctx, String event_id, Properties properties)
```
1. 参数
Ctx：页面的设备上下文
event_id：事件标识
properties Key-Value：参数对，key 和 value 都是 String 类型
2. 调用位置：代码任意处
```java
public void onClick(View v) {
Properties prop = new Properties();
    prop.setProperty("level", "5");
// 统计用户通关所花时长，关卡等级： 5
// 用户通关前
StatService.trackCustomBeginKVEvent(this, " playTime", prop);
    // 用户正在游戏中….
    // …….
    // 用户通关完成时
StatService.trackCustomEndKVEvent(this, " playTime", prop);
}
```

### 【时长统计】带有统计时长的自定义参数事件

可以指定事件的开始和结束时间来上报一个带有统计时长的事件。

```java
void StatService.trackCustomBeginEvent(
Context ctx, String event_id, String... args)
void StatService.trackCustomEndEvent(
Context ctx, String event_id, String... args)
```
1. 参数
Ctx： 页面的设备上下文
event_id：事件标识
args：事件参数
2. 调用位置：代码任意处
```java
public void onClick(View v) {
    // 统计用户通关所花时长
// 用户通关前
StatService.trackCustomBeginEvent(this, " playTime", "level5");
    // 用户正在游戏中….
    // …….
    // 用户通关完成时
StatService.trackCustomEndEvent(this, " playTime", " level5");
```
>**注意：**
>trackCustomBeginEvent 和 trackCustomEndKvent 必须成对出现，且参数列表完全相同，才能正常上报事件。
