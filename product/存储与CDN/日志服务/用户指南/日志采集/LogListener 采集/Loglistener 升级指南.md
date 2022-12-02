## 概述

为了更好的提供日志服务（Cloud Log Service，CLS）的日志采集服务，现支持 LogListener 自动升级、控制台手动升级和脚本半自动升级功能。LogListener 采集端程序版本迭代更新之后，用户无需自主下载新版本安装包进行相关操作的手动升级，只需在控制台预设时间段指定机器组进行 LogListener 自动升级，或对目标机器实行一键手动升级即可。

>? 
> - LogListener 自动升级功能仅在 LogListener 2.5.0 及以上版本开始支持，为了更好的使用体验，建议 [前往安装/升级至最新版本](https://cloud.tencent.com/document/product/614/17414)。
> - 自动升级功能需 Python2 支持，若采集机器上安装的是 Python3，升级过程将无法完整执行。
> - 脚本半自动升级功能需 Python2.7 支持，若采集机器上安装的不是该版本，将无法使用此方式进行升级。
>

采集端程序 LogListener 控制台升级，可以使用自动升级和手动升级。
Agent 升级异常或者因为版本限制无法使用自动升级时，可以使用半自动升级。

## 操作步骤

<span id="AutoUpdate"></span>

### 自动升级

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls)。
2. 在左侧导航栏中，单击**机器组管理**，进入机器组管理页面。
3. 找到需要自动升级的目标机器组，并将鼠标移动至“自动升级”栏下的 ![](https://main.qcloudimg.com/raw/7b707f1dcef1dc117d4446da1265e2c8.png)，单击**立即开启**。
![](https://main.qcloudimg.com/raw/6f900c13067002ef61d47f08236924ee.png)
4. 在弹出的窗口中，开启 LogListener 开关，指定升级时间段（默认为当前时间至后两小时，如08:39～10:39）。
![](https://main.qcloudimg.com/raw/8ab92abd0048de161acf8ac7eaf93e79.png)
5. 单击**确定**，目标机器组的**“自动升级”**栏变为**“已开启”**，即表示开启自动升级 LogListener 成功。
>?
> - 自动升级的时间段可选择任意时间段，系统会在用户指定的时间段每天进行检查。若满足升级条件，则进行自动升级；若不满足升级条件，则不进行操作。
> - 如需对多个机器组进行 LogListener 自动升级，可以勾选多个目标机器组，单击**自动升级**进行批量升级。

<span id="ManualUpdate"></span>
### 手动升级

1. 登录 [日志服务控制台](https://console.cloud.tencent.com/cls)。
2. 在左侧导航栏中，单击**机器组管理**，进入机器组管理页面。
3. 找到需要升级的目标机器组，单击“操作”栏的**立即升级**。
![](https://main.qcloudimg.com/raw/eb994b3aaf2cf8fde387695698ea004d.png)
4. 在弹出的窗口中，勾选**“升级状态”**为**“可升级”**的目标机器，单击**手动更新**。
![](https://main.qcloudimg.com/raw/8bea624ad0b2c4bd63e185487748fce9.png)
系统默认升级至最新版本，当**“升级状态”**为**“已是最新版本”**时，即表示手动升级成功。
<img src="https://main.qcloudimg.com/raw/5921fabe6ad45416cff49bab536fe1af.png" style="width: 87%" />
>? 
> - 当升级状态显示“不支持更新”时，表示不支持在控制台手动更新 LogListener，需要您自主下载新版本安装包进行相关的手动升级操作，详情请参见 [LogListener 安装指南](https://cloud.tencent.com/document/product/614/17414)。
> - 当升级状态显示“心跳异常”时，请 [检查机器组状态](https://cloud.tencent.com/document/product/614/17424)。

### 半自动升级

1. 执行如下命令，确认 Python 版本。
```
python -V
```
若 Python 的版本非2.7，请 [自动升级](#AutoUpdate) 或 [手动升级](#ManualUpdate)。
2. 执行如下命令，下载脚本。
```
wget http://mirrors.tencentyun.com/install/cls/agent-update.py
```
2. 执行如下命令，执行脚本。
```
/usr/bin/python2.7 agent-update.py http://mirrors.tencentyun.com/install/cls/loglistener-linux-x64-x.tar.gz
```
其中，`loglistener-linux-x64-x.tar.gz`中的 x 代表对应升级到的 LogListener 版本号（例如2.7.2）。LogListener 最新版本以 [LogListener 安装指南](https://cloud.tencent.com/document/product/614/17414) 版本为准。如果输入的版本不存在，则下载失败。如果输入的版本低于机器上已安装的当前版本，则更新不生效。

