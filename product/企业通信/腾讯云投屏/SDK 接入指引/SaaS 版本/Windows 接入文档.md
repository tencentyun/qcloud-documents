## 操作场景
本文档主要指导您在 Windows 操作系统下，对无线投屏独立安装包进行安装后的调用。


## 前提条件
请从线下销售经理获得无线投屏独立安装包。


## 操作步骤
1. 启动安装包进行安装，完成无线投屏部署。
2. 从以下注册表字段获取无线投屏入口程序。
```
HKEY_CURRENT_USER\Software\Tencent\TencentCloudDisplay\launcher
// 取到的文件路径类似： C:\Users\test\AppData\Local\Tencent\TencentCloudDisplay\TencentCloudDisplay-100001-1.0.0.1\TencentCloudDisplay.exe
```
3. 在需要调起无线投屏的地方，使用步骤2获取到的进程路径，启动无线投屏进程即可。
