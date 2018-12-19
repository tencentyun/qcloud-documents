## Job 管理
### Job 简介
Job 控制器会创建1-N个Pod, 并确保这些Pod安装运行的规则运行结束。 可用于批量计算、数据分析等场景。
Job可通设置重复执行次数、并行度、重启策略等来满足业务述求。
Job完成后， 不再创建新的Pod, 也不删除Pod， 可查看已完成的Pod的日志，直至删除Job时会同时删除Job创建的Pod.

### Job 控制台操作指引
#### 创建 Job
1. 点击需要部署 Job 的集群ID，进入集群详情页面。
2. 点击 Job 选项，选择新建Job。
3. 根据指引设置Job参数，完成创建。

![][createJob]

Job对比Deployment、DaemontSet、StatefulSet不同的是可以设置任务的重复次数、并行度、失败重启策略。
- 重复次数：该Job管理的Pod需要重复执行的次数
- 并行度：该Job并行执行的Pod数量
- 失败重启策略：Pod下容器异常推出后的重启策略， Never：不重启容器，直至Pod下所有容器退出; OnFailure : Pod继续运行，容器将重新启动

#### 查看Job状态
1. 点击需要部署 Job 的集群ID，进入集群详情页面。
2. 点击 Job 选项，进入Job详情。
3. 查看Job 详情，观察Pod状态

#### 删除Job
Job完成后， 不再创建新的Pod, 也不删除Pod， 可查看已完成的Pod的日志，直至删除Job时会同时删除Job创建的Pod.

### kubectl 操作 Job 指引
#### Yaml示例
```Yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: pi
spec:
  completions: 2
  parallelism: 2
  template:
    spec:
      containers:
      - name: pi
        image: perl
        command: ["perl",  "-Mbignum=bpi", "-wle", "print bpi(2000)"]
      restartPolicy: Never
  backoffLimit: 4
```
- kind: 标识该资源是 Job 类型
- metadata：该Job的名称、Label等基本信息
- metadata.annotations: 对Job的额外说明，腾讯云TKE额外增强能力可以通过该参数设置。
- spec.completions: 该Job管理的Pod重复执行次数。
- spec.parallelism: 该Job并行执行的Pod数
- spec.template:  该Job-管理的Pod的详细模板配置
#### 创建Job
1. 准备Job Yaml文件， 例如上述文件为pi.Yaml
2. kubectl安装完成，并且已连接上集群（可直接登录集群节点使用kubectl）
3. 执行命令创建：
```shell
kubectl create -f pi.yaml
```
4. 执行命令验证创建情况：
```shell
kubectl describe jobs/pi
```

#### 删除Job

1. 执行命令`kubectl delete job [NAME]`

[createJob]:https://main.qcloudimg.com/raw/9f07970a2e2f53bbebb9a2df44ee678b.png
