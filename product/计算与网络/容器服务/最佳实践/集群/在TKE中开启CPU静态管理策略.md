# 在 TKE 中开启 CPU 静态管理策略



## 背景

默认情况下，节点上的 Pod 默认共享节点 CPU 池中所有的 CPU核数， 当节点上运行了很多 CPU 密集的 Pod 时，工作负载可能会切换调度到不同的 CPU 核，  这样就导致有些工作负载的性能明显地受到 CPU 缓存亲和性以及调度延迟的影响。 对此，kubelet 提供了可选的 CPU 管理策略，可以实现某些关键 Pod 的静态绑核，避免 CPU 抢占和切换对业务带来的性能损耗。详情参考：https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/ 。



## TKE 如何开启配置

下面介绍在 TKE 中开启 CPU 静态管理策略的两种方式。

## 一、存量节点开启

### 1. 静态 CPU 策略配置

在 K8S 1.17 版本之前，可供 Pod 独占 CPU 资源数量等于节点的 CPU 总量减去通过 `--kube-reserved` 或 `--system-reserved` 参数保留的 CPU，从 1.17 版本开始，CPU保留列表可以通过 kublet 的 '--reserved-cpus' 参数显式地设置。由于 TKE 的 GA 版本 一般为偶数，所以：

- #### 当 TKE 集群版本小于 1.18 时:

  在节点 `/etc/kubernetes/kubelet` 文件中添加如下配置：

  ```
  ...
  CPU_MANAGER_POLICY="--cpu-manager-policy=static"
  KUBE_RESERVED="--kube-reserved=cpu=xxx,memory=xxx"
  SYSTEM_RESERVED="--system-reserved=cpu=xxx,memory=xxx"
  ...
  ```

  其中， 给 Pods 独占 CPU 可用的资源数量等于节点的 CPU 总量减去通过 `--kube-reserved` 或 `--system-reserved` 参数保留的 CPU，如果保留 CPU 数量设置非整数则向上取整，比如 250m，向上取整就是保留 1 核。

  

  由于 TKE 的 systemd 启动参数环境变量是硬编码，所以这里需要再添加下 kubelet 的启动参数环境变量 `CPU_MANAGER_POLICY` 和`SYSTEM_RESERVED`（`KUBE_RESERVED` 变量默认已经存在了）：

  修改 kubelet 的 systemd 启动文件 `/usr/lib/systemd/system/kubelet.service`, 启动参数添加如下环境变量：

  ```bash
  ...
  ExecStart=/usr/bin/kubelet ... ${CPU_MANAGER_POLICY} ${KUBE_RESERVED} ${SYSTEM_RESERVED} ...
  ...
  ```



- #### 当TKE 集群版本大于等于1.18 :

  在节点 /etc/kubernetes/kubelet 文件中添加如下配置：

  ```
  ...
  CPU_MANAGER_POLICY="--cpu-manager-policy=static"
  RESERVED_CPUS="--reserved-cpus=xxx"
  ...
  ```

  同样修改 kubelet 的 systemd 启动文件 /usr/lib/systemd/system/kubelet.service, 启动参数添加如下环境变量：

  ```bash
  ...
  ExecStart=/usr/bin/kubelet ... ${CPU_MANAGER_POLICY} ${RESERVED_CPUS} ...
  ...
  ```

  --reserved-cpus 参数值为显式指定的用逗号分隔的一组 CPU，如"--reserved-cpus=0,1,2,3"，或 CPU 范围列表 "--reserved-cpus=0-3" 都是可以的。

### 2. 策略配置生效

接下来驱逐节点上的 Pods，并通过删除 kubelet 根目录中的状态文件 `cpu_manager_state` 来手动重置 CPU 管理器：

1. 在 TKE 控制台 【节点列表】-> 【更多】 点【驱逐】选项或手动执行驱逐命令。

2. 在TKE 节点中执行删除 `cpu_manager_state` 文件：

   ```bash
   rm /var/lib/kubelet/cpu_manager_state 
   ```

3. 重启 kubelet 服务：

   ```bash
   systemctl  daemon-reload
   systemctl  restart kubelet
   ```



## 二、新加节点开启（推荐）

通过自定义kubelet 参数的方式完成上述的参数添加，配置的逻辑和上述存量节点一致，目前自定义参数需要开白支持，可联系售后同学帮忙开启即可。

## 总结

上述内容仅描述了如何在 TKE 中开启静态CPU 管理策略， 关于 工作负载的 CPU 静态绑核如何配置和注意事项，请参阅 [static 策略](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/#static-policy)。