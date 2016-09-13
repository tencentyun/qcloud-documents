当Linux系统没有安装acpi管理程序时会导致软关机失败。因此，请先确保您的云服务器上安装了acpi(linux电源管理)模块。

## 检查方法
使用如下命令检查acpi是否安装：

```
ps -ef|grep -w "acpid"|grep -v "grep"
```

如果没有进程存在则表示没有安装，需要进行下一步骤安装此模块。若已有进程则可忽略下一步骤。

## 安装方法
使用如下命令安装acpi模块。

1) Ubuntu/Debian系统下

```
sudo apt-get install acpid
```

2) Redhat/CentOS系统下

```
yum install acpid
```

3) SUSE系统下

```
in apcid
```
>注：CoreOS系统下不存在此问题