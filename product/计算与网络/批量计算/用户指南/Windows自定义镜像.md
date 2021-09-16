## 操作场景
基于 Windows 系统的业务，需要从官方提供的 Windows Server 基础镜像来制作自定义镜像。本文介绍了 Windows 自定义镜像制作步骤。
您可前往 [云市场](https://market.cloud.tencent.com/products/5310) 查看镜像详细信息，镜像 ID 为 **img-er9shcln**。

## 前提条件
已注册腾讯云账户。若未注册腾讯云账户，可前往 [注册页面](https://cloud.tencent.com/register)。

## 操作步骤
### 通过官方基础镜像创建云服务器
1. 前往云市场，进入 [批量计算 Windows Server 2012 R2（64位中文）基础镜像](https://market.cloud.tencent.com/products/5310) 页面。
2. 单击**免费使用**，进入云服务器购买页面。
3. 根据您的实际需求，选择存储介质、带宽、设置安全组等其他配置，并选择购买完成云服务器的购买。



### 在云服务器上安装业务需要的软件
登录 [云服务器控制台](https://console.cloud.tencent.com/cvm/index) 查看已创建的云服务器详细信息，远程登录后将您的业务依赖的软件全部安装到该服务器上，并简单测试相关调用。



### 制作自定义镜像
1. 选择云服务器所在行右侧**更多** > **选择镜像**。如下图所示：
![](https://main.qcloudimg.com/raw/24419aaa4f798add0d0dbcf0c2dcdd3a.png)
2. 在弹出框中输入镜像名称及描述，单击**制作镜像**即可创建镜像。
3. 镜像创建完成后，单击左侧导航栏中的**镜像**即可查看自定义镜像。如下图所示：
>!您可通过查看镜像信息获取自定义镜像 ID。
>
![](https://main.qcloudimg.com/raw/811c25501f2a73675a11ee3639faa595.png)



### 使用自定义镜像提交测试作业
您可获取并修改官方提供的示例，作为个人账号下可执行的 Batch 计算环境。请参考以下内容了解计算环境各项配置的含义：
```
tccli batch SubmitJob --version 2017-03-12 --Job '{
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
您可使用以下示例代码，参考 [作业配置简介](https://cloud.tencent.com/document/product/599/10523#.E4.BD.9C.E4.B8.9A.E9.85.8D.E7.BD.AE.E7.AE.80.E4.BB.8B) 并补充其中**待替换**信息，将其中的 ImageId 替换为您的自定义镜像 ID。
```
tccli batch SubmitJob --version 2017-03-12  --Job '{"JobName": "TestJob",  "JobDescription": "for test", "Priority": "1", "Tasks": [{"TaskName": "Task1",  "TaskInstanceNum": 1,  "Application": {"DeliveryForm": "LOCAL", "Command":  "python -c \"fib=lambda n:1 if n<=2 else fib(n-1)+fib(n-2); print(fib(20))\" "},  "ComputeEnv": {"EnvType":  "MANAGED", "EnvData": {"InstanceType": "S1.SMALL1",  "ImageId": "待替换" }  }, "RedirectInfo": {"StdoutRedirectPath": "待替换", "StderrRedirectPath":   "待替换"}, "MaxRetryCount":  1 } ] }' --Placement '{"Zone": "ap-guangzhou-2"}'
```



