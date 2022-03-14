>!因产品策略调整，游戏联机对战引擎后续将与云开发 CloudBase 整合为新产品形态，现将该产品保持维护状态，不再接收新用户使用申请，老用户仍可正常使用。


###  接口描述
SDK 内部日志打印工具，记录接口关键调用步骤。

### 参数说明

|名称|类型|描述|
|:---|---|---|
|enable|boolean|是否开启控制台日志打印|
|callback|Function|日志回调函数|




<dx-alert infotype="explain" title="">
设置回调函数后，每一条日志将作为该函数的参数。
</dx-alert>




### 使用示例

```
MGOBE.DebuggerLog.enable = true;
MGOBE.DebuggerLog.callback = (log) => console.log(...log); // 默认值;
```


