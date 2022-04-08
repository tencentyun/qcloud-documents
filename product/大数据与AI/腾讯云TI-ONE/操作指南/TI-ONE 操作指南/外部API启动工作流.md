用户可通过外部 API 调用，启动运行 TI-ONE 中的工作流。如使用场景之一：用户需等待外部数据清洗等操作完成后，才开始启动 TI-ONE 工作流运行算法模型，此时“定时任务”的功能已无法满足用户需求，则可以通过外部 API 调用来自定义工作流启动时间。


**具体操作步骤如下：**
1. 下载由 TI-ONE 平台提供的满足该功能的 [外部调用工作流 jar 包](https://1-1259675134.cos.ap-guangzhou.myqcloud.com/runflow.jar)。
2. 该 jar 包的运行环境：用户需在客户端安装 Java 环境。
3. 用户在 TI-ONE 中搭建工作流，并可通过网页链接找到该工作流的相关信息：流 ID 信息（folwId）和工作流所在地域信息（ap-guangzhou）。
4. 用户在 TI-ONE 提供的 [外部调用工作流 jar 包](https://1-1259675134.cos.ap-guangzhou.myqcloud.com/runflow.jar) 的客户端安装路径下，运行命令：
`java -cp runflow.jar tione.demo.Demo ${secret_id} ${secret_key} ${region} ${flow_id}`
例如：`java -cp runflow.jar tione.demo.Demo xxx yyy ap-shanghai 3035`其中，
 - ${secret_id} 和 ${secret_key} 为个人帐户信息，可在 [腾讯云访问管理](https://console.cloud.tencent.com/cam/capi) 中查看。
 - ${region} 和 ${flow_id} 为用户通过工作流网页链接得到的 TI-ONE 工作流的“流 ID 信息”和“工作流所在地域信息”。
5. 刷新 TI-ONE 对应工作流页面，即可看到已成功开始运行工作流。
