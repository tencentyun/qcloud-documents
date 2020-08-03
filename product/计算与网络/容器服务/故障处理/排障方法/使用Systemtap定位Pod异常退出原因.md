本文介绍如何使用 Systemtap 工具定位 Pod 异常问题原因。

## 准备工作
请对应您使用节点的操作系统，按照以下步骤进行相关软件包安装：

### Ubuntu 操作系统
1. 执行以下命令，安装 Systemtap。
```bash
apt install -y systemtap
```
2. 执行以下命令，检查所需待安装项。
```
stap-prep
```
返回示例结果如下：
```bash
Please install linux-headers-4.4.0-104-generic
You need package linux-image-4.4.0-104-generic-dbgsym but it does not seem to be available
 Ubuntu -dbgsym packages are typically in a separate repository
 Follow https://wiki.ubuntu.com/DebuggingProgramCrash to add this repository
apt install -y linux-headers-4.4.0-104-generic
```
3. 根据上述返回结果可知目前需要 dbgsym 包，但已有软件源中并不包含，需使用第三方软件源安装。 请执行以下命令，安装 dbgsym。
```bash
    sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys C8CAB6595FDFF622
    
    codename=$(lsb_release -c | awk  '{print $2}')
    sudo tee /etc/apt/sources.list.d/ddebs.list << EOF
    deb http://ddebs.ubuntu.com/ ${codename}      main restricted universe multiverse
    deb http://ddebs.ubuntu.com/ ${codename}-security main restricted universe multiverse
    deb http://ddebs.ubuntu.com/ ${codename}-updates  main restricted universe multiverse
    deb http://ddebs.ubuntu.com/ ${codename}-proposed main restricted universe multiverse
    EOF
    
    sudo apt-get update
```
4. 配置好软件源后，再次运行以下命令。
```
stap-prep
```
返回示例结果如下：
```bash
Please install linux-headers-4.4.0-104-generic
Please install linux-image-4.4.0-104-generic-dbgsym
```
5. 依次执行以下命令，安装提示所需的包。
```bash
apt install -y linux-image-4.4.0-104-generic-dbgsym
```
```bash
apt install -y linux-headers-4.4.0-104-generic
```

### CentOS 操作系统
1. 执行以下命令，安装 Systemtap。
```bash
yum install -y systemtap
```
2. 向软件源 `/etc/yum.repos.d/CentOS-Debug.repo` 配置文件中输入以下内容并保存，本文以默认未安装 `debuginfo` 为例。
```bash
[debuginfo]
name=CentOS-$releasever - DebugInfo
baseurl=http://debuginfo.centos.org/$releasever/$basearch/
gpgcheck=0
enabled=1
protect=1
priority=1
```
3. 执行以下命令检查所需待安装项，并进行相关项的安装。
>?该命令将会安装 `kernel-debuginfo`。
>
```
stap-prep
```
4. 执行以下命令，检查节点是否已安装多个版本 `kernel-devel`。
```
rpm -qa | grep kernel-devel
```
返回结果如下：
```
kernel-devel-3.10.0-327.el7.x86_64
kernel-devel-3.10.0-514.26.2.el7.x86_64
kernel-devel-3.10.0-862.9.1.el7.x86_64
```
若存在多个版本，则只需保留与当前内核版本相同的版本。假设当前内核版本为 `3.10.0-862.9.1.el7.x86_64`，结合上述返回结果需执行以下命令删除多余版本。
>!
>- 可通过执行 `uname -r` 命令查看内核版本。 
>- 需确保 `kernel-debuginfo` 和 `kernel-devel` 均已安装并且安装版本与当前内核版本相同。
>
```
rpm -e kernel-devel-3.10.0-327.el7.x86_64 kernel-devel-3.10.0-514.26.2.el7.x86_64
```


## 问题分析
若 Pod 因异常被停止时，可以使用 Systemtap 来监视进程的信号发送进行问题定位。该过程工作原理如下：
1. Systemtap 将脚本转换为 C 语言代码，调用 gcc 将其编译成 Linux 内核模块并通过 `modprobe` 加载到内核。
2. 根据脚本内容在内核进行 hook。此时即可通过 hook 信号的发送，找出容器进程停止的真正原因。

## 问题定位

### 步骤1：获取异常 Pod 中重新自动重启的容器 pid
1. 执行以下命令，获取容器 ID。
```
kubectl describe pod <pod name>
```
返回结果如下：
```bash
......
Container ID:  docker://5fb8adf9ee62afc6d3f6f3d9590041818750b392dff015d7091eaaf99cf1c945
......
Last State:     Terminated
	Reason:       Error
	Exit Code:    137
	Started:      Thu, 05 Sep 2019 19:22:30 +0800
	Finished:     Thu, 05 Sep 2019 19:33:44 +0800
```
2. <span id="getPid"></span>执行以下命令，通过获取到的 Container ID 反查容器主进程的 pid。
```bash
docker inspect -f "{{.State.Pid}}" 5fb8adf9ee62afc6d3f6f3d9590041818750b392dff015d7091eaaf99cf1c945
```
返回结果如下：
```
7942
```

### 步骤2：根据容器退出状态码缩小排查范围
通过步骤1中返回信息中的 `Exit Code` 可以获取容器上次退出的状态码。本文以137为例，进行以下分析：
- 如果进程是被外界中断信号停止的，则退出状态码将在129 - 255之间。
- 退出状态码为137则表示进程是被 `SIGKILL` 信号停止的，但此时仍不能确定进程停止原因。

### 步骤3：使用 Systemtap 脚本定位异常原因
假设引发异常的问题可复现，则可以使用 Systemtap 脚本监视容器停止原因。
1. 创建 `sg.stp` 文件，输入以下 Systemtap 脚本内容并保存。
```bash
global target_pid = 7942
probe signal.send{
	if (sig_pid == target_pid) {
		printf("%s(%d) send %s to %s(%d)\n", execname(), pid(), sig_name, pid_name, sig_pid);
		printf("parent of sender: %s(%d)\n", pexecname(), ppid())
		printf("task_ancestry:%s\n", task_ancestry(pid2task(pid()), 1));
	}
}
```
>!变量 `pid` 的值需替换为 [步骤2](#getPid) 中获取的容器主进程 pid，本为以7942为例。
>
2. 执行以下命令，运行脚本。
```bash
stap sg.stp
```
当容器进程因异常停止时，脚本可捕捉到事件，并执行输出如下：
```yaml
pkill(23549) send SIGKILL to server(7942)
parent of sender: bash(23495)
task_ancestry:swapper/0(0m0.000000000s)=>systemd(0m0.080000000s)=>vGhyM0(19491m2.579563677s)=>sh(33473m38.074571885s)=>bash(33473m38.077072025s)=>bash(33473m38.081028267s)=>bash(33475m4.817798337s)=>pkill(33475m5.202486630s)
```
 
## 解决方法
通过观察 `task_ancestry` ，可以看到停止进程的所有父进程。例如，此处可以看到一个名为 `vGhyM0` 的异常进程，该现象通常表明程序中存在木马病毒，需要进行相关病毒清理工作以确保容器正常运行。

