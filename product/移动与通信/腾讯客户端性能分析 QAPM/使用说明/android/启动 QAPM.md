QAPM 可以在 MainActivity.onCreate 中调用如下类似代码以启动 QAPM

```
QAPM.setProperty(QAPM.PropertyKeyAppInstance, getApplication());
QAPM.setProperty(QAPM.PropertyKeyAppId, "33e15431-1024").setProperty(QAPM.PropertyKeyAppVersion, "2.1").setProperty(QAPM.PropertyKeySymbolId, "e6ae1282-ceb8-4237-89bd-2d23d00a8e33");
QAPM.setProperty(QAPM.PropertyKeyUserId, "11223344").setProperty(QAPM.PropertyKeyDebug, "true");
QAPM.beginScene(QAPM.SCENE_ALL, QAPM.ModeStabl);
```
>备注：
>SDK 只监控与上报本进程（即初始化它的那个进程）的信息，如果有多个进程需要监控，得各初始化一次。
