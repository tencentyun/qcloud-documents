可以在 Application.onCreate 中调用如下类似代码以启动 QAPM
```
QAPM apm = QAPM.getInstance(getApplication(), "cdaefbda-52242", "2.1.3");
//uuid:设置上报数据里的UUID，用于标记该版本被混淆堆栈的mapping。
//        此UUID为用户自主生成，跟产品的某个版本挂钩，即同一个版本号编译出来的包，mapping是同一个文件。
//        因此，建议采用“产品ID + 版本号”作为入参的方式生成UUID，具体生成函数各产品可以自行决定，建议最终生成UUID格式的字符串（格式类似e6ae1282-ceb8-4237-89bd-2d23d00a8e33）。
//uin: 设置上报数据里附带的QQ号。即上报的用户账号。
//host:设置上报数据到哪个集群。请向 QAPM 负责同学（kangtian）申请一个集群域名
apm.set("uuid", "e6ae1282-ceb8-4237-89bd-2d23d00a8e33").set("uin", "11223344");
//如果需要进入调试模式请开启debug
//apm.set("uuid", "e6ae1282-ceb8-4237-89bd-2d23d00a8e33").set("uin", "11223344").set("debug", true); 
apm.run();
```
>注意：
>SDK 只监控与上报本进程（即初始化它的那个进程）的信息，如果有多个进程需要监控，得各初始化一次。

