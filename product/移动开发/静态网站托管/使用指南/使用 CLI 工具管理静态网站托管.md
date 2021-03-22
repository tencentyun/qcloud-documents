本文为您介绍如何通过 Cloudbase CLI 管理静态网站托管。



## 前提条件

已安装 [Cloudbase CLI](https://docs.cloudbase.net/cli-v1/install.html)。


## 操作步骤

### 查看静态网站服务信息

您可以执行以下命令，展示静态网站的状态，访问域名等信息。
```bash
tcb hosting detail -e envId
```

>? 您需要将命令中的 `envId` 需要替换为您的`环境ID`，请前往 [云开发控制台](https://console.cloud.tencent.com/tcb/env/index)，查看并复制您想要部署的`环境ID`。

### 部署文件

您可以执行以下命令，将文件上传到静态网站的存储空间中的指定路径，当未指定 cloudPath 时，CLI 会将文件上传到根目录。

```bash
tcb hosting deploy localPath cloudPath -e envId
```

**示例如下：**
```bash
# 将当前目录的文件部署到根目录
tcb hosting deploy . -e envId

# 将 static 目录下的 index.js 文件部署到 static/index.js
tcb hosting deploy ./static/index.js static/index.js -e envId
```

### 删除文件和文件夹

您可以执行以下命令，删除静态网站的存储空间中的文件：

```bash
tcb hosting delete cloudPath -e envId
```

您可以执行以下命令，删除静态网站的存储空间中的文件夹：

```bash
tcb hosting delete -d cloudPath -e envId
```

您可以执行以下命令，删除静态网站的存储空间中的所有文件：

```bash
tcb hosting delete / -e envId
```

### 查看文件列表

您可以执行以下命令，部署展示静态网站存储空间中文件：

```bash
tcb hosting list -e envId
```

>? Windows 系统中 localPath 为本地路径形式，是系统可以识别的路径，通常使用`\`分隔符。`cloudPath`是云端文件路径，均需要使用`/`分隔符。
>- `localPath` 为本地文件或文件夹的路径，为 `目录/文件名` 的形式，例如 `./index.js`、`static/css/index.css` 等。
>- `cloudPath` 为文件或文件夹的相对根目录的路径，为 `目录/文件名` 的形式，例如 `index.js`、`static/css/index.js`等。
