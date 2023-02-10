### 静默安装
`/SilentInstall=0`

### 语言
`/Language="en-us"` 可选值为 en-us、zh-cn、zh-tc、ja、ko、ms 分别对应英文，中文简体，中文繁体，日语，韩语和马来语。

### 指定安装路径
`/InstallPath="INSTALL_PATH"`
`INSTALL_PATH` 为要安装的目录。

**安装参数例子**：
`TencentMeetingInstaller.exe /SilentInstall=0 /Language="en-us" /InstallPath=“D:\Tencent”`
通过以上 CMD 命令执行后，安装包会被静默安装到指定路径下，安装语言为英文。

**特殊说明**：
安装包需要管理员权限执行，确保执行命令时有管理员权限。
