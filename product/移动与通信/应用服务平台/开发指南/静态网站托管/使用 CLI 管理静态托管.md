## 查看静态网站服务信息

您可以使用下面的命令查看静态网站的状态，访问域名等信息。

```bash
cloudbase hosting detail -e envId
```

## 部署文件

您可以使用下面的命令将文件上传到静态网站的存储空间中的指定路径，当不指定 cloudPath 时，CLI 会将文件上传到根目录。

```bash
cloudbase hosting deploy localPath cloudPath -e envId
```

```bash
# 将当前目录的文件部署到根目录
cloudbase hosting deploy . -e envId

# 将 static 目录下的 index.js 文件部署到 static/index.js
cloudbase hosting deploy ./static/index.js static/index.js -e envId
```

## 删除文件和文件夹

您可以使用下面的命令删除静态网站的存储空间中的文件：

```bash
cloudbase hosting delete cloudPath -e envId
```

您可以使用下面的命令删除静态网站的存储空间中的文件夹：

```bash
cloudbase hosting delete -d cloudPath -e envId
```

## 查看文件列表

您可以使用下面的命令部署展示静态网站存储空间中文件。

```bash
cloudbase hosting list -e envId
```

>? Windows 系统中 localPath 为本地路径形式，是系统可以识别的路径，通常使用`\`分隔符。`cloudPath`是云端文件路径，均需要使用`/`分隔符。

- `localPath`为本地文件或文件夹的路径，为`目录/文件名`的形式，例如`./index.js`、`static/css/index.css`等。
- `cloudPath`为文件或文件夹的相对根目录的路径，为`目录/文件名`的形式，例如`index.js`、`static/css/index.js`等。
