
## 操作场景

Ingress 是从 Kubernetes 集群外部访问集群内部服务的入口，您可以通过配置转发规则，实现不同 URL 可以访问到集群内不同的 Service。

## 前置条件

1. 已创建容器服务 TKE 集群。相关操作详情请参见 [创建 TKE 集群](https://cloud.tencent.com/document/product/457/54231)。
2. 已在集群内创建 Deployment 等工作负载，以及 Service 资源。相关操作详情请参见 [Deployment 管理](https://cloud.tencent.com/document/product/457/31705)。
3. 已购买 Nginx Ingress 网关实例，相关操作详情请参见 [网关实例管理](https://cloud.tencent.com/document/product/1364/79817)。Nginx Ingress 网关实例必须和后端 TKE 容器集群处于同一地域和同一 VPC 下。
4. 已添加为 Nginx Ingress 网关实例添加后端服务集群，相关操作详情请参见 [服务管理](https://cloud.tencent.com/document/product/1364/79929)。

## 操作步骤

### 控制台操作指引

1. 登录 [微服务引擎控制台](https://console.cloud.tencent.com/tse)，在左侧导航栏单击**云原生 API 网关** > Nginx Ingress，单击目标 Nginx Ingress 网关实例，进入实例详情页。
2. 在顶部菜单栏选择 **Ingress 管理**，单击**新建**。
3. 在新建页面配置以下参数：
![](https://qcloudimg.tencent-cloud.cn/raw/19bf7c0bcc200583183155a9707e3ce6.png)
<table>
<thead>
<tr>
<th>参数</th>
<th>是否必填</th>
<th>说明</th>
</tr>
</thead>
<tbody><tr>
<td>Ingress</td>
<td>是</td>
<td>Ingress 名称，最长63个字符，只能包含小写字母，数字及分隔符，且必须以小写字母开头，数字和小写字母结尾。</td>
</tr>
<tr>
<td>服务来源</td>
<td>是</td>
<td>选择后端服务集群，如需添加后端集群，请前往<b>服务管理</b>页面添加。</td>
</tr>
<tr>
<td>命名空间</td>
<td>是</td>
<td>选择命名空间。</td>
</tr>
<tr>
<td>域名</td>
<td>否</td>
<td>填写域名，如果缺省，可以通过<b>访问控制</b>页面中提供的内网/公网地址访问。</td>
</tr>
<tr>
<td>协议</td>
<td>是</td>
<td>支持 HTTP 协议，HTTPS 协议已在开发中</td>
</tr>
<tr>
<td>转发规则</td>
<td>是</td>
<td>配置转发规则。</td>
</tr>
<tr>
<td>annotation</td>
<td>否</td>
<td>默认添加注解：<br>kubernetes.io/ingress.class : tse-nginx-ingress<br><br>nginx.ingress.kubernetes.io/use-regex : true<br><br>为 Nginx Ingress 对象配置注解，详情可参见 <a href="https://github.com/kubernetes/ingress-nginx/blob/main/docs/user-guide/nginx-configuration/annotations.md">官方文档</a></td>
</tr>
</tbody></table>

### Kubectl 操作指引

示例如下：

```
metadata:
  name: 
  annotations:
    kubernetes.io/ingress.class: "tse-nginx-ingress". 
```
