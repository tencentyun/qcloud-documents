

## 功能介绍

常见的 SMP 处理器存在多个层级，包含线程、物理核、处理器等结构，在开启超线程的情况下，一个物理核上一般会包含2个线程，且同核上的2个线程共享 L2 Cache。
![img](https://qcloudimg.tencent-cloud.cn/raw/78f03451604e627821dcd3d238842ea1.png)        

当高优先级容器与低优先级容器同时运行时，可能会出现高优先级容器的线程与低优先级容器的线程在同一个物理核甚至在同一个超线程 CPU 上执行的情况，在这种情况下，虽然 [CPU 使用优先级](https://cloud.tencent.com/document/product/457/79775) 能保证高优先级容器线程总能抢占低优先级容器的线程，但是只要低优先级容器线程运行，就会占用物理核上共享的 L2 Cache，导致高优先级容器线程的 L2 Cache 受到影响。
![img](https://qcloudimg.tencent-cloud.cn/raw/a971d338af703be251db68285021a874.png)        

为了避免高优先级容器线程的 L2 Cache 受到运行在同一个物理核上的低优先级线程的影响，QoS Agent 引入了超线程隔离机制。在处理器资源富余的情况下，保证高优先级容器线程所在物理核上没有低优先级容器线程的干扰。

在不同场景下的超线程干扰隔离策略：

| **Thread 1** | **Thread 2** | **Action**                                                   |
| ------------ | ------------ | ------------------------------------------------------------ |
| 高优先级     | 高优先级     | 不采取任何行为                                               |
| 高优先级     | 低优先级     | 将 sibling 上的低优先级任务限流并限制负载均衡时低优先级任务迁移到 sibling 上 |
| 低优先级     | 低优先级     | 尝试拉取其它核上的高优先级任务                               |



## **使用方式**

1. 部署 [QoS Agent](https://cloud.tencent.com/document/product/457/79774)。
2. 在集群里的“扩展组件”页面，找到部署成功的 QoS Agent，单击右侧的**更新配置**。
3. 在修改 QoS Agent 的组件配置页面，勾选 **CPU 超线程隔离**。
4. 勾选 **CPU 使用优先级**，用于标识高优先级业务。
5. 单击**完成**。
6. 部署业务。
7. 部署关联该业务的 PodQOS 对象，选择需要使用超线程隔离的 Workload 的 Label，示例如下：
```yaml
apiVersion: ensurance.crane.io/v1alpha1
kind: PodQOS
metadata:
  name: ht-1
spec:
  spec:
  labelselector:
    matchLabels:
      k8s-app: memcached	# 选择需要降低优先级的业务的 Label
  resourceQOS:
    cpuQOS:
      cpuPriority: 0	# 标识为高优先级业务
      htIsolation:
        enable: true	# 开启 CPU 超线程隔离能力。enable 可取 true/false，代表针对 PodQOS 关联到的业务是否开启超线程隔离
```







