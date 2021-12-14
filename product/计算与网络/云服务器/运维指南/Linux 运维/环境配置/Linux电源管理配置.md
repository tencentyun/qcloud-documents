## 操作场景

在 x86 机器中，存在 **APM**（Advanced Power Management，高级电源管理）和 **ACPI**（Advanced Configuration and Power Interface，高级配置和电源接口）两种电源管理方法。ACPI 是 Intel、Microsoft 和东芝共同开发的一种电源管理标准，提供了管理电脑和设备更为灵活的接口，而 APM 是电源管理的老标准。
Linux 支持 APM 和 ACPI，但这两个标准不能同时运行。在缺省情况下，Linux 默认运行 ACPI 。同时，腾讯云也推荐您使用 ACPI 电源管理方法。
Linux 系统在没有安装 ACPI 管理程序时，会导致软关机失败。本文档介绍检查 ACPI 安装情况与安装操作。

## 安装说明

针对 CoreOS 系统，无需安装 ACPI。

## 操作步骤
 
1. 执行以下命令，检查是否安装 ACPI。
```
ps -ef|grep -w "acpid"|grep -v "grep"
```
 - 若不存在进程，则表示未安装 ACPI，请执行下一步。
 - 若存在进程，则表示已安装 ACPI，任务完成。
2. 根据操作系统的类型，执行不同的命令，安装 ACPI。
 - Ubuntu / Debian 系统，执行以下命令：
```
sudo apt-get install acpid
```
 - Redhat / CentOS 系统，执行以下命令：
```
yum install acpid
```
 - SUSE 系统，执行以下命令：
```
in apcid
```



