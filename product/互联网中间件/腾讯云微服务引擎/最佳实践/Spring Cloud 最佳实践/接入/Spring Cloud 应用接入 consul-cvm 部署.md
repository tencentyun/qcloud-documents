## 操作场景
本文介绍如何将通过 CVM 部署的 Spring Cloud 应用接入微服务引擎托管的 consul 注册中心。接入无需修改任何代码。

![](https://qcloudimg.tencent-cloud.cn/raw/a67695fbc7a015912b919f3b900375ee.png)

## 操作步骤
1. 登录至 CVM 实例中，下载并安装 Consul。
<dx-alert infotype="notice" title="">
请选择 1.8.6 版本进行安装。
</dx-alert>
2. 在 CVM 实例中，参考以下脚本创建相关资源并启动 Consul Agent：
<dx-codeblock>
:::  sh
#1 创建数据文件夹
mkdir -p /data/consul/data

#2 创建日志文件夹
mkdir -p /data/consul/log

#3 创建配置文件夹
mkdir -p /data/consul/config

#4 创建配置文件
vim /data/consul/config/config.json
{
    "datacenter": "dc1",
    "data_dir": "/data/consul/data/",
    "node_name": "consul-agent-node",
    "server": false,
    "bind_addr": "{{ GetInterfaceIP \"eth0\" }}",
    "client_addr": "127.0.0.1",
    "log_json": true,
    "log_level": "info",
    "log_rotate_max_files": 10,
    "log_rotate_duration": "24h",
    "log_file": "/data/consul/log/",
    "retry_join": [
        "[TSE Consul Node1 Address]",
        "[TSE Consul Node2 Address]",
        "[TSE Consul Node3 Address]"
    ]
}

#5 启动客户端模式的consul agent
consul agent --config-dir=/data/consul/config

:::
</dx-codeblock>
<dx-alert infotype="notice" title="">
Consul Agent 支持本地模式和局域网模式两种部署模式：
- 本地模式：本地模式请指定 client_addr 为127.0.0.1，需要在每台 CVM 实例部署 Agent。
- 局域网模式：局域网模式请指定 client_addr 为0.0.0.0，只需指定几台 CVM 实例部署 Agent，部署后同一局域网内的 Agent 即可互相连通。
</dx-alert>
3. 准备 Spring Cloud 应用 Jar 包。我们同时为您提供了 Spring Cloud 应用 [Demo 代码库](https://github.com/tencentyun/tse-simple-demo)。
4. 上传 Spring Cloud 应用 Jar 包至 CVM 实例。
5. 指定注册中心地址参数并运行该应用。登录至 CVM 实例中，运行以下命令：
<dx-codeblock>
:::  sh
nohup java 
-Dspring.cloud.consul.host=[TSE Consul Client Agent IP]
-jar [jar包名称] &

:::
</dx-codeblock>
6. [TSE 控制台](https://console.cloud.tencent.com/tse) 验证服务注册。单击进入注册中心实例的服务管理页面，若出现以下页面，则证明服务注册成功。
![](https://qcloudimg.tencent-cloud.cn/raw/52633851a85e28a03eb9a908e94fe176.png)


