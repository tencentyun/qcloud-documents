## Installing Python and Pip

Make sure you have installed the Python environment and Pip tools in your system before installing CLI. For more information, please see [How to Install the Python Environment and Pip Tools](/doc/product/440/6181).

### Installing CLI	
(1) Install CLI by Pip:

```
$ sudo pip install qcloudcli
```

(2) Check whether the qcloudcli is installed successfully:

```
$  qcloudcli --help
NAME:
	qcloudcli
DESCRIPTION:
	The Qcloud Command Line Interface is a unified tool to manage your qcloud services.
```

### Installing Auto Completion of Command Lines
(1) Locate the auto completion script of qcloud_completer and run the command below:

```
$ which qcloud_completer
/usr/bin/qcloud_completer
```

(2) Add the path of qcloud_completer into the auto completion command and run the command below:

```
$ complete -C '/usr/bin/qcloud_completer' qcloudcli
```

(3) Check whether the qcloudcli auto completion script is included. It is included if the following result is obtained:

```
$ complete | grep qcloudcli
complete -C '/usr/bin/qcloud_completer' qcloudcli
```

(4) Use the auto completion function
In the qcloudcli, use TAB key to enable the auto completion function. If the command is unique, it will be completed directly. Otherwise, all available commands are displayed:

```
$ qcloudcli c

cam     cbs     cdb     cdn     cmem    cns     configure   cvm   
```

(5) Make auto completion take effect automatically
To ensure that the auto completion command always takes effect once enabled, you need to write the auto completion command into the profile `~/.bash_profile`:

```
$ vim ~/.bash_profile
```

Append it to the end of the file:
![Alt text](https://mc.qcloudimg.com/static/img/8dae9aa2ac7e733ae71d06fbce11939a/1472882079703.png)


## Upgrading CLI
If you have already installed the qcloudcli, use the Pip's `--upgrade` option to upgrade the qcloudcli to the latest version:

```
$ sudo pip install --upgrade qcloudcli
```

## Uninstalling CLI
If you no longer need to use Tencent Cloud CLI, uninstall it using the following command:

```
$ sudo pip uninstall qcloudcli
```

