## Windows 恢复模式的概述

**Windows 系统恢复模式（Recovery）**，是指 Windows 使用自动修复功能。当 Windows 检测到某些系统问题，并认为继续使用对系统造成损坏时，将阻止 Windows 启动，进入到系统恢复选项，以提供给用户进行修复、备份或系统还原等处理的一种状态。
系统恢复选项包含了若干工具，例如“启动修复”、“系统还原”、“ Windows 内存诊断”等，这些工具可以来修复问题、备份数据、执行系统还原等操作。
当用户无法远程登录云服务器，且控制台登录云服务器后出现下图状态，则表示 Windows 云服务器已进入恢复模式。
![](//mc.qcloudimg.com/static/img/e278c336a415066dcb8fc58333395ac3/image.png)

## 进入恢复模式的原因
进入恢复模式有以下常见原因：
- **Windows 运行或者关闭过程中，强行关闭电源。**包括在控制台执行的强行关机操作。关机不慎可能造成系统丢失部分关键的数据从而进入恢复模式。
- **WindowsUpdate 过程中，电源被切断。**更新中的关键数据遗失从而进入恢复模式。
- **系统被木马或病毒损坏。**
- **Windows 的核心服务 BUG 。** Windows 自检发现风险，从而进入恢复模式。
- **系统丢失关键数据或者系统被损坏。**用户可能出现误操作损坏系统文件，从而导致系统进入恢复模式。

## 预防措施
腾讯云推荐用户采取以下预防措施：
 - 关机时，打开控制台观察 Windows 的关机过程。腾讯云软关机使用超时机制，执行软关机以后等待预定的时间系统没有关闭，会返回失败。若关机过程出现缓慢或 WindowsUpdate ，只需等待云服务器关闭即可，不可强行关闭。推荐参考 [关机失败的几种场景](https://cloud.tencent.com/document/product/213/2917#.E5.85.B3.E6.9C.BA.E5.A4.B1.E8.B4.A5.E7.9A.84.E5.87.A0.E7.A7.8D.E5.9C.BA.E6.99.AF)。
 - 检查系统是否存在木马或者病毒等异常程序与进程。
 - 检查系统管理和杀毒软件运行是否正常。
 - 及时更新 Windows 的更新包，特别是一些重要更新和安全更新。
 - 定期检查系统事件日志，核查核心服务是否出错。

## 解决方法
 Windows 进入到恢复模式后，用户可尝试继续启动运行，或自动修复。轻微问题 Windows 可自行修复。执行以下操作：
1. 从 [控制台](https://console.cloud.tencent.com/cvm) 登录云服务器。
2. 出现恢复模式界面，单击【Next】。如下图所示：
![](//mc.qcloudimg.com/static/img/94a1cf0f55d2c449a9d026bbbad5e4cd/image.png)
3. 出现系统恢复选项，单击【Next】，使用默认方案。如下图所示：
![](//mc.qcloudimg.com/static/img/d178865f822d2146eb3bb58f1b851294/image.png)
4. 单击【Restart】，并快速按下键盘【F8】。如下图所示：
![](//mc.qcloudimg.com/static/img/ab2fdd697015fcb7e53b287052086b65/image.png)
5. 选择【正常启动 Windows】。如下图所示：
![](//mc.qcloudimg.com/static/img/8079bcf59132ff587ec5caf46c84f27d/image.png)
若 Windows 无法启动，则请在控制台中重新安装系统，详见 [使用控制台重装系统](https://cloud.tencent.com/document/product/213/4933#.E4.BD.BF.E7.94.A8.E6.8E.A7.E5.88.B6.E5.8F.B0.E9.87.8D.E8.A3.85.E7.B3.BB.E7.BB.9F)。
