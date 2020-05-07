## 安装 Python 和 Pip

安装命令行工具前请确保您的系统已经安装了 Python 环境和 Pip 工具，更多内容请参考 [安装 Python 及 pip](https://cloud.tencent.com/document/product/440/6181)。

## 安装命令行工具	
1. 通过 pip 安装命令行工具：
```
$ sudo pip install qcloudcli
```
2. 检验 qcloudcli 是否安装成功：
```
$  qcloudcli --help
NAME:
	qcloudcli
DESCRIPTION:
	The Qcloud Command Line Interface is a unified tool to manage your qcloud services.
```

## 安装命令行自动补齐
1. 找到自动补全脚本 qcloud_completer 位置，运行以下命令：
```
$ which qcloud_completer
/usr/bin/qcloud_completer
```
2. 将 qcloud_completer 所在路径加入系统的自动补全命令，运行以下命令：
```
$ complete -C '/usr/bin/qcloud_completer' qcloudcli
```
3. 观察是否包含 qcloudcli 自动补全脚本，获得类似如下结果证明已包含了 qcloudcli 的自动补全脚本：
```
$ complete | grep qcloudcli
complete -C '/usr/bin/qcloud_completer' qcloudcli
```
4. 使用自动补全功能。
在 qcloudcli 中使用 TAB 键完成自动补全功能。如果命令唯一，则直接补全，否则展示当前所有可用命令：
```
$ qcloudcli c
cam     cbs     cdb     cdn     cmem    cns     configure   cvm   
```
5. 自动补全命令自动生效。
为了保证每次启动自动补全命令均有效，您需要将自动补全的命令写入配置文件`~/.bash_profile`中：
```
$ vim ~/.bash_profile
```
追加到文件末尾即可：
![Alt text](https://mc.qcloudimg.com/static/img/8dae9aa2ac7e733ae71d06fbce11939a/1472882079703.png)


## 升级命令行工具
如果您已经安装有 qcloudcli，请使用 pip 的`--upgrade`选项来升级到最新版本的 qcloudcli：
```
$ sudo pip install --upgrade qcloudcli
```
## 卸载命令行工具
如果您不再需要使用腾讯云命令行工具，可通过以下命令卸载腾讯云命令行工具：
```
$ sudo pip uninstall qcloudcli
```
