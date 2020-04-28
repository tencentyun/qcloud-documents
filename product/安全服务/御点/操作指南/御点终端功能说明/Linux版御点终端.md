Linux 版的御点终端有病毒查杀及文件防护功能。
1. 检查 Linux 的御点是否安装成功，安装步骤请参见 [Linux平台安装部署](https://cloud.tencent.com/document/product/1009/39936)。
2. 使用如下命令检查御点是否运行，如果提示`/usr/local/bin/TavDaemon`，说明御点已经启动。
![](https://main.qcloudimg.com/raw/13ca8cc58a1a9ab434c0df117cccf508.png)

## 本地杀毒
Linux 版御点本地杀毒步骤如下：  
```
bash
cd /usr/local/bin
./TavClient
{"FixType":2,"ScanType":1,"TaskType":1,"SeqId":0}
ScanType: 1 快速扫描
ScanType:2 全盘扫描
```

## Linux 远程终端任务与管理
御点后台管理人员有权限对所有的 Linux 主机进行统一的病毒查杀及实时防护，具体使用说明请参见 [后台控制中心功能说明](https://cloud.tencent.com/document/product/1009/40014)。
![](https://main.qcloudimg.com/raw/15fd966a9afc4cc127e28e9b3dc88618.png)
