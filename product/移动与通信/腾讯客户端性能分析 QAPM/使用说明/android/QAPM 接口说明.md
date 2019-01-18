### 设置参数

```
(1)  public static QAPM setProperty(int key, String value)
```

| 参数名                | 解释                                                         |
| --------------------- | ------------------------------------------------------------ |
| key                   | 可选为“PropertyKeyAppId”、“PropertyKeyUserId”、“PropertyKeyAppVersion”、“PropertyKeySymbolId”、“PropertyKeyDebug”。 |
| PropertyKeyAppId      | 产品 ID 为“产品密钥-产品 ID”模式，可从邮件中获取。           |
| PropertyKeyUserId     | 用户账号（比如 QQ 号、微信号等）。                           |
| PropertyKeyAppVersion | 产品版本（以类似“7.3.0.141.r123456”格式填写，后台可以解析出大版本号和 revision）。 |
| PropertyKeySymbolId   | UUID，用于拉取被混淆堆栈的 mapping ,用于做堆栈翻译用，见说明 |
| PropertyKeyLogLevel   | 是否开启调试日志, 可选为 QAPM.LevelOff, QAPM.LevelError, QAPM.LevelWarn, QAPM.LevelInfo, QAPM.LevelDebug, QAPM.LevelVerbos。建议debug模式下开启QAPM.LevelDebug。 |
| 返回值                | QAPM 对象。                                                  |

>?
- SymbolId 用于关联一个版本的符号表，方便后续对该版本上报的堆栈作反混淆，格式需要为 UUID。
- 如何生成 SymbolId 并没有严格限定，只要是与 AppVersion 相关的一种映射方式即可。

下面介绍一种比较简单的方式：

```Java
String version = "2.1";
String symbolId = UUID.nameUUIDFromBytes(version.getBytes()).toString();
```


### 启动监控
```
(2) public static boolean beginScene(String sceneName, int mode)
```

| 参数名           | 解释                                       |
| ------------- | ---------------------------------------- |
| sceneName     | 被监控的场景名                                  |
| mode          | 可选为“ModeAll”、“ModeStable”、“ModeResource”、“ModeDropFrame”|
| ModeAll       | 开启全部监控，包括内存泄漏、文件 IO、数据库 IO、卡顿、触顶、电量、区间性能、流畅度 |
| ModeStable    | 开启适合外网使用的监控，包括卡顿、区间性能、流畅度                |
| ModeResource  | 区间性能监控                                   |
| ModeDropFrame | 流畅度采集                                    |
| 返回值           | 布尔值，表示监控是否开启成功。                          |

>!
- 正式版建议开启 QAPM.ModeStable，研发流程内版本建议开启 QAPM.ModeAll。 
- 确实需要定制开启个别功能时，可使用 ModeLeakInspector、ModeFileIO、ModeDBIO、ModeLooper、ModeCeiling、ModeBattery 中一个到多个，多个使用时采用按为或方式即可，如 ModeLeakInspector | ModeFileIO | ModeDBIO。
- 上述定制功能开启后，不能通过 endScene 关闭。



```
(3) public static boolean beginScene(String sceneName, String extraInfo, int mode)
```

| 参数名       | 解释                                       |
| --------- | ---------------------------------------- |
| sceneName | 见(2)                                     |
| extraInfo | 可选以下项用户定制 —— 若存在未调用 endScene 即再调用 beginScene 的场景，需要填 extraInfo 以区分 |
| mode      | 见(2)                                     |
| 返回值       | 见(2)                                     |


### 结束监控
```
(4) public static boolean endScene(String sceneName, int mode)
```

| 参数名           | 解释                                 |
| ------------- | ---------------------------------- |
| sceneName     | 见(2)                               |
| mode          | 可选为“ModeResource”、“ModeDropFrame”|
| ModeResource  | 区间性能监控                             |
| ModeDropFrame | 流畅度采集                              |
| 返回值           | 布尔值，表示监控是否终止成功。                    |

```
(5) public static boolean endScene(String sceneName, String extraInfo, int mode)
```

| 参数名       | 解释                                       |
| --------- | ---------------------------------------- |
| sceneName | 见(2)                                     |
| extraInfo | 可选以下项:用户定制 —— 见(2) APPLAUNCH —— 用户定制 App 启动的结束点 |
| mode      | 见(4)                                     |
| 返回值       | 见(4)                                     |
