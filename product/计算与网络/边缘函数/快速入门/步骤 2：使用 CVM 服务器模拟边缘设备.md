本文主要介绍如何使用腾讯云 CVM，模拟边缘计算中的边缘设备，并与前一步骤中的云端设备对应。

## 创建 CVM 实例 
1. 登录 [控制台](https://console.cloud.tencent.com/)，通过总览页进入云服务器控制台，在广州地域任意区创建实例，实例规格可以为任意规格，目前最小支持1核1GB的实例。
2. 创建实例时，可选择 CentOS 7.4 或 Ubuntu 16.04.1 作为实例的操作系统。
3. 在选择存储与带宽时，需要勾选【现在购买公网 IP】，确保实例能访问公网。
4. 最后，为实例设置好安全组、配置好密码后，完成购买。

更详细的实例购买流程，参考 [快速入门 Linux 云服务器](https://cloud.tencent.com/document/product/213/2936)。**当前边缘函数仅支持在 Linux 环境中运行，暂不支持在 Windows 环境中运行。**

## 配置 Edge Function Core
Edge Function Core 是运行在边缘设备上的软件包。通过在边缘设备上运行的 Edge Function Core，云函数能被调度到边缘设备上按需运行；同时也支持在边缘端进行边缘网、函数、云端之间的物联网消息转发。Edge Function Core 又简称为 efc、core。

通过如下步骤，完成 Edge Function Core 在设备上的配置及启动：
1. 通过 SFTP 客户端连接在上一步骤中创建的 CVM 实例，将 efc 代码包上传到 CVM 的某个目录下，例如`/root`目录
2. 通过 `tar` 命令解压 efc 代码包到当前目录下，生成如 `efcore-x86-v1.0` 的目录。
3. 切换到解压生成的目录中，可以看到有`certs`，`etc`，`runtime`三个子目录，及 `efc` 可执行文件。
4. 使用编辑器打开`etc/config.json`文件，修改其中`coreThing`结构下的`instanceId`，`username`，`password`，`efHost`这几个 key-value 对的 value 值，使其与云端设备对象的基本信息对应，修改完成后保存。各项 key 的含义及示例值如下。

| key | 含义 | 示例 |
| --- | --- | --- |
| instanceId | 设备 ID | device-g00ufhc6 |
| efHost |  IoT MQ 实例的 MQTT 链接地址 | mqtt-4i9kx1itw.ap-guangzhou.mqtt.tencentcloudmq.com |
| username | IoT MQ 中，针对实例计算出来连接用户名 | AKIDCgOPWjQ6BAxvHtyckhWABJVYSBj548pN |
| password  | IoT MQ 中，针对实例计算出来连接密码 | yohiGUqPDmft8ITPEsobbtL5ktnCilpewnK7T3OUVrE= |

## 启动 Edge Function Core
通过运行代码包根目录下的 efc 可执行文件就可以启动 Edge Function Core。如果此文件无可执行权限，可通过以下命令赋予可执行权限。
```
chmod +x efc
```
您可直接通过以下命令使 efc 在前台（终端中）启动运行，直接查看相关的运行日志和输出。通过此方式启动 efc，efc 会随着终端的退出而退出，一般在调试或测试时通过此方法运行，可以方便的查看日志输出。
```
./efc
```
也可通过以下命令使 efc 在后台运行，同时相关的日志输出会打印至同目录的 nohup.txt 文件中。此方式通常用于将 efc 启动为后台服务，避免终端退出而导致 efc 退出。
```
nohup ./efc &
``` 
