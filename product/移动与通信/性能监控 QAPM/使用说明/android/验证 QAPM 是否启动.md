验证  QAPM 是否启动，可在 run 调用前调用
```
apm.set("debug", true);
```

例如：
```
QAPM apm = SNGAPM.getInstance(getApplication(), 1000, "2.3.0");
QAPM.set("uuid", "e6ae1282-ceb8-4237-89bd-2d23d00a8e33").set("uin", "11223344").set("host", "QAPM.qq.com");
apm.run();
```
那么在启动时候会看到类似如下的日志输出
```
D/QAPM_MagnifierSDK: Magnifier SDK Start success, LEAKINSPECTOR : true, IO : true, DB : true, LOOPER : true, CEILING : true, BATTERY : false
```
APP 使用一段时间后, 登录到 QAPM 主页，可以看到内存泄漏、触顶、卡顿的等上报。