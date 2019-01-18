
Linux 系统在没有安装 ACPI 管理程序时会导致软关机失败。本文档介绍检查 ACPI 安装情况与安装操作。
## ACPI 介绍
 - 概述：ACPI（Advanced Configuration and Power Interface），高级配置与电源管理。是 Intel、Microsoft 和东芝共同开发的一种电源管理标准。 
 - 比较：在x86机器中，存在两种电源管理方法，**APM** (Advanced Power Management，高级电源管理)和 **ACPI** (Advanced Configuration and Power Interface，高级配置和电源接口)。APM 是老标准，而 ACPI 则提供了管理电脑和设备更为灵活的接口。Linux支持这两种协议，不过有时还需要手工配置。另外，两个标准不能同时运行。缺省情况下 Linux 运行 ACPI 。腾讯云推荐您使用 ACPI 电源方案。
 - CoreOS 系统说明：CoreOS 系统无需安装。
 
## 检查方法
输入命令检查 ACPI 是否安装：`ps -ef|grep -w "acpid"|grep -v "grep"`

 - 若无进程存在，则表示没有安装，需要进行下一步骤安装此模块。
 - 若有进程存在，则表示已经安装，无需进行下一步骤。

## 安装方法
输入命令安装 ACPI 模块。

- Ubuntu / Debian 系统下：`sudo apt-get install acpid`

- Redhat / CentOS 系统下：`yum install acpid`

- SUSE 系统下：`in apcid`
