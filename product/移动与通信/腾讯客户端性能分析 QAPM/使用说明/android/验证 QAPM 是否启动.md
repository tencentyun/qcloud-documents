验证  QAPM 是否启动，可在 run 调用前调用
```
apm.set("debug", true);
```

例如：
```
QAPM apm = QAPM.getInstance(getApplication(), "cdaefbda-52242", "2.3.0");
QAPM.set("uuid", "e6ae1282-ceb8-4237-89bd-2d23d00a8e33").set("uin", "11223344");
apm.run();
```
那么在启动时候会看到类似如下的日志输出
```
I/QAPM_Magnifier: QAPM SDK start success! PID: 22199, APM_VERSION: 1.0.0-SNAPSHOT, SWITCH : 63。
I/QAPM_Magnifier: LEAKINSPECTOR : true, IO : false, DB : false, LOOPER : true, CEILING : false, BATTERY : false, SAMPLE : false
```
APP 使用一段时间后, 登录到[QAPM 主页](http://qapm.qq.com)，可以看到内存泄漏、触顶、卡顿的等上报。