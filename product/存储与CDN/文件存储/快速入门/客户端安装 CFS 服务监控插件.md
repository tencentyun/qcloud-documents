##客户端安装 CFS 服务监控插件
CFS 服务监控插件是集成在腾讯云云监控组件上的一个插件，用于监控 CFS 文件系统的性能及客户端连接。强烈建议您在需要使用 CFS 文件存储的云主机或容器等客户端上安装 CFS 服务监控插件，以方便您更好的管理 CFS 服务。

**在安装 CFS 服务监控插件前，请确保您的客户端已经安装腾讯云平台的云监控组件，查看[云监控组件安装操作指引](https://cloud.tencent.com/document/product/248/6211) 。**

## 操作系统支持

CFS 服务监控插件目前支持在以下平台上运行，其他 Linux 内核版本系统可能会存在兼容性问题。

| 操作系统 | 版本                           |
| -------- | ------------------------------ |
| CentOS   | CentOS 7.5 64位                |
|          | CentOS 7.4 64位                |
|          | CentOS 7.3 64位                |
|          | CentOS 7.2 64位                |
|          | CentOS 6.9 64位                |
|          | CentOS 6.9 32位                |
|          | CentOS 6.8 64位                |
| Ubuntu   | Ubuntu Server 16.04.1 LTS 64位 |

### 功能说明

插件主要功能及原理如下

- 原理：插件读取数据来源为 /proc/self/mountstats 以及 /var/log/messages 中 NFS 相关日志，读取数据为性能、状态及挂载参数相关数据，不涉及用户实际业务数据。
- 主要功能：读取使用 CFS 的客户端挂载点状态，对挂载点做可用性探测并收集性能相关数据；

## Linux 安装指引

您在登录 Linux 实例后，可以执行以下命令来获取并安装 CFS 服务监控插件。

###1.下载插件
通过以下命令，下载 CFS 服务监控插件到客户端当前目录下。

```
##下载 CFS 服务监控插件
wget http://update2.agent.tencentyun.com/update/cfs_barad_plugin_installer_release_v1.0
```

###2.修改插件格式
通过以下命令，将 CFS 服务监控插件修改为可执行类型。

```
##修改文件类型
chmod +x cfs_barad_plugin_installer_release_v1.0
```

![CFS插件修改类型-linux](/工作文件/github/qcloud-documents/product/存储与CDN/文件存储/图片/CFS插件修改类型-linux.png)

###3.安装插件
通过以下命令，安装 CFS 服务监控插件，并返回安装成功。

```
##安装插件
./cfs_barad_plugin_installer_release_v1.0
```

![CFS插件安装成功-linux](/工作文件/github/qcloud-documents/product/存储与CDN/文件存储/图片/CFS插件安装成功-linux.png)

## Windows 安装指引

Windows 客户端暂未支持，敬请期待。



## 监控来访客户端

在 [CFS控制台](https://console.cloud.tencent.com/cfs) , 点击文件系统名称进入文件系统详情，选择 "已挂载客户端"， 可以查看到已挂载该文件系统的客户端信息，若客户端未安装插件则无法获取信息。注，客户端信息展示会有1-3分钟的延迟。
![](/已挂载客户端详情.png)
