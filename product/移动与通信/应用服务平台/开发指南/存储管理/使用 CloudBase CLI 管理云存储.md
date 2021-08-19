使用 CloudBase CLI 命令行界面交互工具，您可以非常方便的管理项目的云存储资源，例如批量上传/下载文件/文件夹，获取文件访问链接与信息，设置/获取云存储的权限等。

## 下载文件/文件夹

您可以使用下面的命令来下载文件：

```sh
cloudbase storage download cloudPath localPath
```

下载文件夹时，需要指定 `--dir` 参数。

例如以下命令，会将云存储根目录下的 **cloudbase** 目录中的所有文件，下载到本地 **download** 目录中：

```sh
cloudbase storage download cloudbase ./download --dir
```

## 上传文件/文件夹

您可以使用下面的命令将本地电脑的文件或文件夹上传到云存储，当 CLI 检测到 **localPath** 为文件夹时，会自动上传文件内的所有文件，如果重复上传会覆盖。

```sh
cloudbase storage upload localPath cloudPath
```

当不传入 cloudPath，文件会上传到云端的根目录下，同时文件夹的层次结构会被保留，例如下面的命令会把项目根目录的 download 文件夹里的内容直接上传到云存储的根目录里，download 的子文件夹会成为云存储的二级目录。

```sh
cloudbase storage upload ./download
```

## 删除文件/文件夹

如果您想删除云存储里的文件或文件夹，可以使用下面的命令，删除文件夹时，需要指定 --dir 参数。

```sh
# 删除文件
cloudbase storage delete cloudPath

# 删除文件夹
cloudbase storage delete cloudPath --dir
```

## 获取文件/文件夹信息

在不打开云开发控制台或网页控制台，您也可以通过 Cloudbase Cli 工具了解云存储里的文件夹或文件的信息，例如在终端里输入以下命令可以列出云存储里的文件夹里的所有文件信息，例如大小、修改时间、key、Etag 等信息。

```sh
cloudbase storage list cloudPath
```

## 列出文件夹内文件列表

例如您可以直接使用以下命令打印云存储根目录里的所有文件，其中二级目录里的文件会用路径的方式显示。

```
cloudbase storage list cloudPath
```

## 参考

更多详细信息请参见 [CloudBase CLI 命令行工具](https://cloud.tencent.com/document/product/876/41539)。

