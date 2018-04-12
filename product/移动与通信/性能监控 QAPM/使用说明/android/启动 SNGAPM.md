可以在 Application.onCreate 中调用如下类似代码以启动 SNGAPM
```
QAPM apm = QAPM.getInstance(getApplication(), 1000, "2.1.3");
//uuid:设置上报数据里的UUID，用于拉取被混淆堆栈的mapping（注：在RDM上编译时，可以通过编译脚本把UUID写到assets或者AndroidManifest.xml里，细节可以咨询RDM的同学）。
//     uuid的获取方式请参考文档--[RDM UUID的设置](http://x.code.oa.com/mobilespectest/QAPM/articles/402)
//uin: 设置上报数据里附带的QQ号。即上报的用户账号。
//host:设置上报数据到哪个集群。请向QAPM负责同学（kangtian）申请一个集群域名
apm.set("uuid", "e6ae1282-ceb8-4237-89bd-2d23d00a8e33").set("uin", "11223344").set("host", "qq.QAPM.com");
//如果需要进入调试模式请开启debug
//apm.set("uuid", "e6ae1282-ceb8-4237-89bd-2d23d00a8e33").set("uin", "11223344").set("host", "qq.QAPM.com").set("debug", true); 
apm.run();
```
>SDK 只监控与上报本进程（即初始化它的那个进程）的信息，如果有多个进程需要监控，得各初始化一次。

