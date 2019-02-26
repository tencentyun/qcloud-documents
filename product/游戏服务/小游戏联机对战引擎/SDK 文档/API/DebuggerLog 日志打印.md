## DebuggerLog 日志打印

该对象属性如下：

|名称|类型|描述|
|:---|---|---|
|enable|boolean|是否开启控制台日志打印|
|callback|Function|日志回调函数|

将 enable 设为 ture 后，SDK 内部接口关键调用步骤将打印在控制台。设置回调函数后，每一条日志将作为该函数的参数。

**使用示例**

```
MBS.DebuggerLog.enable = true;
MBS.DebuggerLog.callback = (log) => console.log(...log); // 默认值;
```