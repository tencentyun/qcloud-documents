## CronJob 管理
### CronJob 简介
一个 CronJob 对象类似于 crontab （cron table）文件中的一行。它根据指定的预定计划周期性地运行一个 Job，格式可以参考 Cron 。

Cron 格式说明
<pre>
# 文件格式说明
#  ——分钟（0 - 59）
# |  ——小时（0 - 23）
# | |  ——日（1 - 31）
# | | |  ——月（1 - 12）
# | | | |  ——星期（0 - 7，星期日=0或7）
# | | | | |
# * * * * *
</pre>

### CronJob 控制台操作指引
#### 创建 CronJob
1. 点击需要部署 CronJob 的集群ID，进入集群详情页面。
2. 点击 CronJob 选项，选择新建 CronJob。
3. 根据指引设置 CronJob 参数，完成创建。
![][createCronJob]

Job对比Deployment、DaemontSet、StatefulSet不同的是可以设置任务的执行策略、重复次数、并行度、失败重启策略。
- 执行策略：Cron格式，设置任务的定期执行策略，
- 重复次数：该Job管理的Pod需要重复执行的次数
- 并行度：该Job并行执行的Pod数量
- 失败重启策略：Pod下容器异常推出后的重启策略， Never：不重启容器，直至Pod下所有容器退出; OnFailure : Pod继续运行，容器将重新启动

#### 查看 CronJob 状态
1. 点击需要部署 CronJob 的集群ID，进入集群详情页面。
2. 点击 CronJob 选项，进入 CronJob 详情。
3. 查看 CronJob详情，观察Pod状态

### kubectl 操作 CronJob 指引
#### Yaml示例
```Yaml
apiVersion: batch/v1beta1
kind: CronJob
metadata:
  name: hello
spec:
  schedule: "*/1 * * * *"
  jobTemplate:
    spec:
      template:
        spec:
          containers:
          - name: hello
            image: busybox
            args:
            - /bin/sh
            - -c
            - date; echo Hello from the Kubernetes cluster
          restartPolicy: OnFailure
```
- kind: 标识该资源是 CronJob 类型
- metadata：该 CronJob 的名称、Label等基本信息
- metadata.annotations: 对 CronJob 的额外说明，腾讯云TKE额外增强能力可以通过该参数设置。
- spec.schedule: 该CronJob执行的Cron的策略。
- spec.jobTemplate: Cron执行的Job模板


#### 创建 CronJob
**方法一**：
1. 准备CronJob Yaml文件， 例如上述文件为cronjob.yaml
2. kubectl安装完成，并且已连接上集群（可直接登录集群节点使用kubectl）
3. 执行命令创建：
```shell
kubectl create -f cronjob.yaml
```
**方法二**：
使用 `kubectl run`快速 创建一个 Cron Job，不需要写完整的配置，如：
```shell
kubectl run hello --schedule="*/1 * * * *" --restart=OnFailure --image=busybox -- /bin/sh -c "date; echo Hello"
```

执行命令验证创建情况：
```shell+-
kubectl get cronjob [NAME]
```
#### 删除 CronJob
1. 执行命令`kubectl delete cronjob [NAME]`
删除将终止正在创建的Job， 已创建的Job不会被终止，已完成的Job也不会被删除，需要删除CronJob创建的Job。

[createCronJob]:https://main.qcloudimg.com/raw/2e4f92f3aa76d1bc5400a379eec6299e.png
