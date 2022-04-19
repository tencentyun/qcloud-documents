
本文介绍如何在腾讯云容器服务的集群里面配置 ExternalDNS。

## 什么是 External DNS

ExternalDNS 将公开的 Kubernetes Service 和 Ingress 与 DNS 提供商同步。

受 Kubernetes 集群内部 DNS 服务器 [Kubernetes DNS](https://github.com/kubernetes/dns) 的启发，ExternalDNS 使 Kubernetes 资源可通过公共 DNS 服务器发现。与 KubeDNS 一样，它从 Kubernetes API 中检索资源列表（Service、Ingress 等），以确定所需的 DNS 记录列表。然而，与 KubeDNS 不同的是，它本身并不是一个 DNS 服务器，而只是用于对接其他 DNS 提供商。更多请查看 [ExternalDNS Readme](https://github.com/kubernetes-sigs/external-dns)。

## 操作步骤

### 配置 API 密钥 的 CAM 权限

在腾讯云 [访问管理控制台](https://console.cloud.tencent.com/cam/overview)，获取 API 密钥的 SecretId 和 SecretKey 信息，确保当前的用户的 CAM 权限拥有以下策略：

```json
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "action": [
                "dnspod:ModifyRecord",
                "dnspod:DeleteRecord",
                "dnspod:CreateRecord",
                "dnspod:DescribeRecordList",
                "dnspod:DescribeDomainList"
            ],
            "resource": [
                "*"
            ]
        },
        {
            "effect": "allow",
            "action": [
                "privatedns:DescribePrivateZoneList",
                "privatedns:DescribePrivateZoneRecordList",
                "privatedns:CreatePrivateZoneRecord",
                "privatedns:DeletePrivateZoneRecord",
                "privatedns:ModifyPrivateZoneRecord"
            ],
            "resource": [
                "*"
            ]
        }
    ]
}
```

### 部署 ExternalDNS 服务

#### 配置 PrivateDNS 或 DNSPod

腾讯 DNS 解析 [DNSPod](https://cloud.tencent.com/document/product/302) 向全网域名提供免费的智能解析服务，拥有海量处理能力、灵活扩展性和安全能力。为您的站点提供稳定、安全、快速的解析体验。

[Private DNS](https://cloud.tencent.com/document/product/1338) 是基于腾讯云私有网络 VPC 的私有域名解析及管理服务，为您提供安全、稳定、高效的内网智能解析服务。支持在私有网络中快速构建 DNS 系统，满足定制化解析需求。

* 如果您想在腾讯云的环境中使用内网的 DNS 服务：
  * 配置下列 YAML 文件中参数：`--tencent-cloud-zone-type=private`   
  * 在 PrivateDNS 控制台创建 DNS 域名。DNS 域名记录中将会包含 DNS 记录。
* 如果您想在腾讯云的环境中使用公网的 DNS 服务：
  * 配置下列 YAML 文件中参数：`--tencent-cloud-zone-type=public`   
  * 在 [DNSPod 控制台](https://console.dnspod.cn) 创建 DNS 域名。DNS 域名记录中将会包含 DNS 记录。
 
#### 在 Kuberentes 集群中部署相关资源对象

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: external-dns
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRole
metadata:
  name: external-dns
rules:
- apiGroups: [""]
  resources: ["services","endpoints","pods"]
  verbs: ["get","watch","list"]
- apiGroups: ["extensions","networking.k8s.io"]
  resources: ["ingresses"] 
  verbs: ["get","watch","list"]
- apiGroups: [""]
  resources: ["nodes"]
  verbs: ["list"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: ClusterRoleBinding
metadata:
  name: external-dns-viewer
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: ClusterRole
  name: external-dns
subjects:
- kind: ServiceAccount
  name: external-dns
  namespace: default
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: external-dns
data:
  tencent-cloud.json: |
    {
      "regionId": "ap-shanghai", # 必填项，集群所在地域的 ID
      "secretId": "******",  
      "secretKey": "******",
      "vpcId": "vpc-******"	# 必填项，集群所在 VPC 的 ID
    }
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: external-dns
spec:
  strategy:
    type: Recreate
  selector:
    matchLabels:
      app: external-dns
  template:
    metadata:
      labels:
        app: external-dns
    spec:
      containers:
      - args:
        - --source=service
        - --source=ingress
        - --domain-filter=external-dns-test.com # 将使 ExternalDNS 仅看到与提供的域匹配的托管区域，省略以处理所有可用的托管区域
        - --provider=tencentcloud
        - --policy=sync # 设置“upsert-only”将阻止 ExternalDNS 删除任何记录
        - --tencent-cloud-zone-type=private # 仅管理私有托管区域。设置“public”以使用公网 DNS 服务
        - --tencent-cloud-config-file=/etc/kubernetes/tencent-cloud.json
        image: ccr.ccs.tencentyun.com/tke-market/external-dns:v1.0.0
        imagePullPolicy: Always
        name: external-dns
        resources: {}
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
        volumeMounts:
        - mountPath: /etc/kubernetes
          name: config-volume
          readOnly: true
      dnsPolicy: ClusterFirst
      restartPolicy: Always
      schedulerName: default-scheduler
      securityContext: {}
      serviceAccount: external-dns
      serviceAccountName: external-dns
      terminationGracePeriodSeconds: 30
      volumes:
      - configMap:
          defaultMode: 420
          items:
          - key: tencent-cloud.json
            path: tencent-cloud.json
          name: external-dns
        name: config-volume
```

## 使用示例

创建名为 nginx 的 Service，示例如下：

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx
  annotations:
    external-dns.alpha.kubernetes.io/hostname: nginx.external-dns-test.com # 公网域名地址
    external-dns.alpha.kubernetes.io/internal-hostname: nginx-internal.external-dns-test.com # 内网域名地址
    external-dns.alpha.kubernetes.io/ttl: "600"
spec:
  type: LoadBalancer
  ports:
  - port: 80
    name: http
    targetPort: 80
  selector:
    app: nginx
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx
spec:
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - image: nginx
        name: nginx
        ports:
        - containerPort: 80
          name: http
```

- `nginx.external-dns-test.com` 将记录服务的 Loadbalancer VIP。
- `nginx-internal.external-dns-test.com` 将记录服务的 ClusterIP。所有的 DNS 记录的 TTL 都是 600。

#### 执行验证

名为 nginx 的 Service 的 ClusterIP 为 `192.168.254.214`， Loadbalancer VIP 为 `129.211.179.31`，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/9cf1709ac78fa73a9ff28c9b4feb72f8.png)


当您在与集群所在同一个 VPC 内节点上， ping 名为 nginx 的 Service 里 annotation 的域名声明时，会自动解析成 ClusterIP 和 Loadbalancer VIP，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/dfaec4597cf7dd9c9702cef897031b51.png)
