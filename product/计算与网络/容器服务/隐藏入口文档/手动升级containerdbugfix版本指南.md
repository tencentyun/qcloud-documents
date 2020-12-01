本文介绍如何手动升级存量节点 Containerd 到新的 bugfix 版本，以及存量 Pod 长时间卡在 Terminating 状态的解决方法。



## 存量节点升级步骤
1. 对于存量节点，可通过依次执行以下命令，升级 Containerd 到 bugfix 版本。
>!该升级动作将会重启 Containerd 服务，但不会重启 Pod，建议不要在 CPU 或者内存使用量过高的节点上执行。
>
``` sh
wget http://static.ccs.tencentyun.com/containerd-1.2.7-1.6.tgz
tar -zxf http://static.ccs.tencentyun.com/containerd-1.2.7-1.6.tgz
cd containerd-1.2.7/bin
systemctl stop containerd
mv containerd containerd-shim containerd-shim-runc-v1 containerd-stress runc /usr/local/bin
systemctl start containerd
```
2. 升级动作完成之后，执行以下命令验证 Containerd 是否升级成功。
``` sh
ctr version
```
返回结果如下，通过查看 Version，可确认节点 Containerd 已从 v1.2.7 升级到 v1.2.7-1-g020228e6，表示升级成功。
```
Client:
     Version: v1.2.7-1-g020228e6
     Revision: 020228e6c438100ca55a854dded7f1ecd700af4f
Server:
     Version: v1.2.7-1-g020228e6
     Revision: 020228e6c438100ca55a854dded7f1ecd700af4f
```



## 故障处理

### Pod 卡在 Terminating 状态
如果 Pod 长时间（2 - 5分钟）卡在 Terminating 状态时，可通过 `journalctl -u containerd ` 命令查看日志。若包含类似如下信息，则可确认该问题是由 Containerd 引起。
```
runc did not terminate sucessfully: container "8076897365b9a6ec9f371180b8fa93aa41bc83fb01bdf903542bb470eefcf47a" does not exist
``` 

### 处理步骤
1. 执行以下命令，查看卡住的容器。
``` shell
ctr -n k8s.io task ls
```
返回结果如下所示，其中 STATUS 为 STOPPED 的容器即为故障容器。
```
TASK                                PID   STATUS
8e5bb8aa3c1d8c574ae772090e7e96aba54827352c118a1ad548c4780a471eac  16440  RUNNING
5ce2a36e23b92d507f9281c46313ba1d67c65c50107eb3b6adbad347b274573a  16442  STOPPED
```
2. 执行以下命令，删除对应的 task，Pod 的状态在下一次 PLEG 时会恢复。
```
ctr -n k8s.io task delete 5ce2a36e23b92d507f9281c46313ba1d67c65c50107eb3b6adbad347b274573a
```
