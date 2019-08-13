## 概要信息
基于 Windows 系统的业务，需要从官方提供的 Windows Server 基础镜像来制作自定义镜像，官方镜像 [链接>>](https://market.cloud.tencent.com/products/5310)，镜像 ID ``img-er9shcln``

## Windows 自定义镜像制作步骤

### 1. 通过官方基础镜像创建云主机

进入[云主机购买页](https://buy.cloud.tencent.com/cvm)。

![](https://mc.qcloudimg.com/static/img/f4c62ba416032b20e17ff9ec3ed15e39/s3.png)
[云市场链接地址>>](https://market.cloud.tencent.com/products/5310)

选择镜像的时候，选择『服务市场』，在搜索栏里搜索『批量计算』，选择Windows Server 2012 的基础镜像（镜像 ID：img-er9shcln），后续存储、网络、其他设置根据提示选择，最后单击『立即购买』创建云主机。

### 2. 在云主机上安装业务需要的软件

在 [云主机控制台](https://buy.cloud.tencent.com/cvm) 查看刚才的创建的云主机信息，远程登录后将您的业务依赖的软件全部安装到该云主机上，并简单测试相关调用。

### 3. 制作自定义镜像

![](https://mc.qcloudimg.com/static/img/270d48a5e64e7ec32e1d710f43123b47/s1.png)

在控制台单击``制作镜像``即可，请耐心等待镜像制作完成

![](https://mc.qcloudimg.com/static/img/e939a39dcebe0c7449c7dacdb33e52ea/s2.png)

这个 ID 就是您的自定义镜像 ID，您可以随时到 [镜像控制台](https://console.cloud.tencent.com/cvm/image) 来查看

### 4. 使用自定义镜像提交测试作业

```
qcloudcli batch SubmitJob --Version 2017-03-12 --Job '{
    "JobName": "TestJob",       // 作业名称
    "JobDescription": "for test ",    // 作业描述
    "Priority": "1",            // 作业优先级
    "Tasks": [                  // 任务列表（本例仅一个任务）
        {
            "TaskName": "Task1",   // 任务1名称
            "Application": {        // 任务执行命令
                "DeliveryForm": "LOCAL",    // 执行本地命令
                "Command": "python -c \"fib=lambda n:1 if n<=2 else fib(n-1)+fib(n-2); print(fib(20))\" "   // 命令具体内容（斐波拉契求和）
            },
            "ComputeEnv": {         // 计算环境配置
                "EnvType": "MANAGED",   // 计算环境类型，托管型和非托管型
                "EnvData": {        // 具体配置（当前托管型，可参照CVM 创建实例说明）
                    "InstanceType": "S1.SMALL1",    // CVM 实例类型
                    "ImageId": "",      // CVM 镜像 ID（替换成您的自定义镜像ID）
                }
            },
            "RedirectInfo": {       // 标准输出重定向配置           
                "StdoutRedirectPath": "cos://dondonbatchv5-1251783334.cosgz.myqcloud.com/logs/",    // 标准输出（需替换）
                "StderrRedirectPath": "cos://dondonbatchv5-1251783334.cosgz.myqcloud.com/logs/"     // 标准错误（需替换）
            }
        }
    ]
}'
--Placement'{
    "Zone": "ap-guangzhou-2"    // 可用区（可能需替换）
}'
```

与快速入门的例子相比，替换其中 ImageId 为您的自定义镜像 ID即可


```
qcloudcli batch SubmitJob --Version 2017-03-12  --Job '{"JobName": "TestJob",  "JobDescription": "for test", "Priority": "1", "Tasks": [{"TaskName": "Task1",  "TaskInstanceNum": 1,  "Application": {"DeliveryForm": "LOCAL", "Command":  "python -c \"fib=lambda n:1 if n<=2 else fib(n-1)+fib(n-2); print(fib(20))\" "},  "ComputeEnv": {"EnvType":  "MANAGED", "EnvData": {"InstanceType": "S1.SMALL1",  "ImageId": "待替换" }  }, "RedirectInfo": {"StdoutRedirectPath": "待替换", "StderrRedirectPath":   "待替换"}, "MaxRetryCount":  1 } ] }' --Placement '{"Zone": "ap-guangzhou-2"}'
```

实际命令行提交请复制上面这段命令到文本，修改里面的『待替换』部分（3处，镜像 ID 和日志地址）即可。




