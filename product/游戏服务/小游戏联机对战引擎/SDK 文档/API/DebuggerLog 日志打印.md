>!尊敬的腾讯云客户您好，由于产品逻辑已无法满足当前游戏技术发展，游戏联机对战引擎 MGOBE 将于2022年7月1日结束生命周期下线，请您尽快迁移，最晚迁移日期到2022年6月30日，到期后游戏联机对战引擎不再维护。感谢您一直以来的支持与理解！


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


