通过SSH连接工作空间
Cloud Studio 工作空间（预置环境）支持 SSH 和 SCP，您可以通过 SSH 连接到工作空间，包括通过命令行终端 SSH 连接工作空间，通过 VSCode 的 [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) 插件连接工作空间等，也可以通过 SCP 命令上传或下载文件。

## 操作步骤
### 步骤1：获取 SSH 命令
“运行中”的工作空间，可以看到 SSH 登录的小图标，单击图标，可以获取 SSH 登录命令。如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/492de6e5a52fb2b606beb0c58e8c5d5b.png)
![](https://qcloudimg.tencent-cloud.cn/raw/925eafbf22a8a59b72b40d47584ab6a1.png)
>?只有预置环境的工作空间才能看到 SSH 连接小图标。

### 步骤2：通过 SSH 命令登录工作空间
您可以通过常见 SSH 登录工具登录到工作空间，例如 Mac 上的 iTerm2，Windows 上的 SecureCRT 等。

#### 通过 iTerm2 登录工作空间
将获取到的 SSH 命令粘贴到 iTerm2 直接执行即可，如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/d856a74d86dc265bf26a689ed1464a22.png)

#### 通过 SecureCRT 登录工作空间
1. 从前端获取 SSH 登录命令后，可以从命令里获取 Hostname 和 Username ，参见下图设置 SecureCRT 连接选项：
![](https://qcloudimg.tencent-cloud.cn/raw/f0a34715fd0841268f12edf54929d5dd.png)
>!首次连接，需要创建密钥对。在上图选择 **PublicKey**，然后单击 **Properties...**，进行创建，单击 **Create Identify File...**，如下图：
>![](https://qcloudimg.tencent-cloud.cn/raw/5f83d6b121d4d33bd864f83528b092bb.png)
2. 按 SecureCRT 的指引进行操作，创建成功后，可以看到已创建的密钥对的一些信息。
![](https://qcloudimg.tencent-cloud.cn/raw/4dbaa506640047286c647e4793b7ac27.png)
3. SecureCRT 连接成功后，效果如下图：
![](https://qcloudimg.tencent-cloud.cn/raw/bd2c4fd3c70151b1c1489aacc394a567.png)

#### 步骤3：通过 VSCode Remote SSH 插件连接工作空间
操作步骤：
1.	给 VSCode 安装 Remote SSH 插件。
![](https://qcloudimg.tencent-cloud.cn/raw/d638684bb363b999d130d68fd305d97f.png)
2.	在 Remote SSH 插件中增加一个连接。
![](https://qcloudimg.tencent-cloud.cn/raw/c7e2b8ba0c90a1fe85f683cd2f710dfd.png)
粘贴获取到的 SSH 命令，然后回车。
![](https://qcloudimg.tencent-cloud.cn/raw/c8c20fc461251e84b0418ccbae1612f7.png)
3.	单击远程主机名右边的按钮，即可连接到工作空间。
![](https://qcloudimg.tencent-cloud.cn/raw/ce04f1bf44fb6bbbdb3bd65225ea6f82.png)
 
### 步骤4：通过 SCP 上传或下载文件
您可以通过 SCP 和工作空间上传或下载文件，SCP 命令格式请参见 [SCP 使用手册](https://man7.org/linux/man-pages/man1/scp.1.html)。
工作空间的 SSH 连接命令格式是：`ssh ${TARGET}`，常用的 SCP 命令是：
- 上传：`scp file ${TARGET}:/path/to/file`
- 下载：`scp ${TARGET}:/path/to/file file`


### 使用示例
- 上传文件到工作空间
假设本地当前目录有个文件：index.html，希望上传到工作空间的 `/root/RemoteWorking/web` 目录（将下面命令中的 `${TARGET}` 替换对应工作空间连接地址）：
![](https://qcloudimg.tencent-cloud.cn/raw/c49d295a935b80165be160e5551bfc8c.png)
- 下载工作空间的文件到本地
假设要把工作空间的 `/root/RemoteWorking/web/index.js` 下载到本地当前目录：
![](https://qcloudimg.tencent-cloud.cn/raw/02c1e3159b1feca75cfaccde7add778d.png)
