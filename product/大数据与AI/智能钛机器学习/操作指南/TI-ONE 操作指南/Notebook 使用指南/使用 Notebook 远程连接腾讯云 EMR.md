## 操作场景
弹性 MapReduce（EMR）是云端托管的弹性开源 Hadoop 服务，支持 Spark、Hbase、Presto 等大数据框架。本文档将向您介绍如何使用 Notebook 远程连接腾讯云的 EMR。

## 操作详情
### 新建 EMR 集群
登录 [EMR 控制台](https://console.cloud.tencent.com/emr) ，单击【创建集群】，选择地域（请选择 TIONE 支持的地域），选择产品版本 【EMR-V2.2.0.tlinux】，勾选可选组件【spark_hadoop2.8 2.4.3】 和 【livy 0.7.0】。
![](https://main.qcloudimg.com/raw/bbd1e9a71bdc88b8a8a86ac1d8e9f213.png)

单击下一步：基础配置，进入硬件配置，请选择合适的机型，并且配置网络的 vpc 和子网。
![](https://main.qcloudimg.com/raw/a2aa76e3e74ca472f5e20220a0525286.png)
单击下一步配置其他集群信息，完成 EMR 集群的创建。


### 查看 livy 服务的 IP
单击左侧的【组件管理】，找到 LIVY 服务。
![](https://main.qcloudimg.com/raw/1960731bc16444a053aaad402e6dda89.png)
查看 LIVY 服务的 IP，记住其一即可。
![](https://main.qcloudimg.com/raw/4cdc138e902d77e91c10b96b22d1327d.png)

### 新建 Notebook 配置 EMR 连接凭据
登录 [腾讯云 TI 平台 TI-ONE 控制台](https://console.cloud.tencent.com/tione/notebook/instance) ，选择与 EMR 集群相同的地域，单击【新增实例】，打开 VPC 选项，请确保此处的 VPC 和子网与新建 EMR 时的选择相同。
![](https://main.qcloudimg.com/raw/ba98aefb04e8fbfa6734e6269a8a22cc.png)

打开 Notebook，在启动界面的最下面找到 Terminal。
![](https://main.qcloudimg.com/raw/35cd31f20118b434f914d0ef22f5f750.png)

修改 ～/.sparkmagic/config.json 文件，替换 kernel_python_credentials、kernel_scala_credentials、kernel_r_credentials url 里的 localhost 为 LIVY 的服务 IP。
![](https://main.qcloudimg.com/raw/93c4d0e0825deec673ac174966fc86e1.png)
如果 EMR 中配置了其他访问相关的设置，例如：auth， kerbersos，您均可在 ～/.sparkmagic/config.json 文件中配置，详情请参见 [config.json GitHub文件](https://github.com/jupyter-incubator/sparkmagic/blob/master/README.md) 。


### 使用 SparkMagic 远程连接 EMR
打开 Notebook 自带的 Example，找到 sparkmagic_pyspark.ipynb，单击 【Create a Copy】，运行示例代码，即将 Spark 程序运行在远程的 EMR 集群中。
![](https://main.qcloudimg.com/raw/e82474c8d75279f37746ff7fd1eeb3c7.png)
您可以在 Notebook 的 Terminal 中手动 curl LIVY 的服务，查看 session 进程。
![](https://main.qcloudimg.com/raw/0b310fb4560d0a4c2be64b1fefaa8068.png)
