## 操作场景
目前云原生监控服务支持 Webhook 功能，通过 Webhook 您可以配置企业微信或钉钉接收云原生监控告警信息。

所有能对接 alertmanager Webhook 的开源组件都可以对接云原生监控。目前只支持将告警投递到内网地址（该地址需要和当前实例在同个私有网络中，或可被当前内网访问），无法发送到公网，因此无法直接将告警投递到企业微信/钉钉渠道，需要通过开源组件实现中转，本文将以配置云原生监控告警发送到企业微信为例介绍相关配置流程。





## 操作步骤

### 步骤1：创建企业微信机器人

1. 打开 PC 端企业微信，鼠标右键单击对应群聊，在下拉菜单中单击**添加群机器人**。如下图所示：
![](https://main.qcloudimg.com/raw/88bb689202b4de4a221f12a6a0faeb2f.jpg)
2. 进入群聊，查看群成员，鼠标右键单击机器人，在下拉菜单中单击**查看资料**，获取 Webhook 地址。如下图所示：
![](https://main.qcloudimg.com/raw/d006cc88080ff2428785a188ad64968c.png)

### 步骤2：在内网部署 PrometheusAlert 组件[](id:step2)

1. 执行以下命令在集群内安装 PrometheusAlert，项目地址请参见 [PrometheusAlert](https://github.com/feiyu563/PrometheusAlert)。[](id:step2.1)
```sh
kubectl create ns monitoring
kubectl apply -n monitoring -f https://raw.githubusercontent.com/feiyu563/PrometheusAlert/master/example/kubernetes/PrometheusAlert-Deployment.yaml   
```
安装完之后您可用执行以下命令查看相关资源：
```sh
kubectl get svc -n monitoring
kubectl get deploy -n monitoring
kubectl get cm -n monitoring
```
示例如下图所示：
![](https://main.qcloudimg.com/raw/bd9cc156aa43b3f79256de7b2041f8ea.jpeg)
2. 将 PrometheusAlert 的 Service 修改为内网 LB 访问。
默认创建的 Service 为 ClusterIP 类型，因为云原生监控的 Webhook 地址需要和当前实例在同个私有网络中，或可被当前内网访问，因此需要调整为内网 LB 类型。执行以下命令进行修改：
```sh
kubectl edit svc prometheus-alert-center -n monitoring
```
	1. 修改 Service 类型，根据 [上述步骤](#step2.1) 命令创建的资源文件为 ClusterIP 类型，需要将 spec.type 由 ClusterIP 修改为 LoadBalancer。如下图所示：
	![](https://main.qcloudimg.com/raw/5a22c0d46128d752a8b8253c5b1157cb.jpeg)
	2. 添加 annotations，指定注解`service.kubernetes.io/qcloud-loadbalancer-internal-subnetid: subnet-xxxxxxxx`，即可通过内网 IP 直接访问到后端 Pod。如下图所示：
	![](https://main.qcloudimg.com/raw/1ed08c711c9936982ff17d24eee0a284.png)


### 步骤3：配置 Webhook 告警

1. 登录 [云原生监控控制台](https://console.cloud.tencent.com/tke2/prometheus/list?rid=1)，选择**对应实例** > **告警配置** > **新增告警策略**。
2. 按照提示填写告警相关信息，如下图所示：
![](https://main.qcloudimg.com/raw/8b850b1849862a6e8c610dd7315e3922.jpeg)
在填写中需要注意以下几点：
    - 云原生监控默认的告警内容将被存储在 annotations.content 中，而 PrometheusAlert 的内置模板告警内容从 annotations.description 获取，所以需要在控制台上添加一条 Annotation，key 为 description，value 为告警内容（可以直接将下面的告警内容复制粘贴到 description 的 value）。
    - 告警渠道勾选 Webhook，地址填写`http://{EXTERNAL-IP}:8080/prometheus/router?wxurl=https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=xxx`
        - EXTERNAL-IP 为 [步骤2](#step2) 部署 service 的 EXTERNAL-IP。如下图所示：		
			![](https://main.qcloudimg.com/raw/1bfb5813b05aa0ef594fa374ab482d08.jpeg)
        - 本例发送至企业微信，所以 QueryString 参数为`wxurl={步骤一获取到的企业微信机器人地址}`
        - 其他告警接收方，例如钉钉，则 QueryString 参数为`ddurl={钉钉机器人webhook地址}`
        - 如需同时发送至企业微信、钉钉、飞书等，可在 QueryString 部分拼接，例如`http://{EXTERNAL-IP}:8080/prometheus/router?wxurl={企业微信机器人url}&ddurl={钉钉机器人webhook地址}&fsurl={飞书webhook地址}`
        - 其他接收方配置请参见 [Prometheus接入配置](https://github.com/feiyu563/PrometheusAlert/blob/master/doc/readme/prometheus.md)。
3. 单击发送测试请求，查看是否配置成功。配置成功如下图所示：
![](https://main.qcloudimg.com/raw/7cda5d0b2ca51c3581c33ee36034aba1.jpg)
