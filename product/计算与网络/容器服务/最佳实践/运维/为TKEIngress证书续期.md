## 操作场景
使用 TKE 控制台创建的 Ingress 配置的证书会引用 [SSL 证书](https://console.cloud.tencent.com/ssl) 中托管的证书，若 Ingress 使用时间较长，证书存在过期的风险。一旦证书过期，会对线上业务造成巨大影响，因此需要在证书过期前进行续期，本文将介绍如何为 Ingress 证书续期。

## 操作步骤
### 查询将过期的证书

登录 [SSL 证书控制台](https://console.cloud.tencent.com/ssl)，在【证书管理】页面按到期时间升序排列显示证书，查看即将过期的证书。如下图所示：
![](https://main.qcloudimg.com/raw/0bae29bc1aca5a423b8191f7cb645307.png)

### 添加新证书

为旧证书续期生成新证书，可根据自身情况选择【购买证书】、【申请免费证书】或【上传证书】中的任意一种方式来添加新证书。如下图所示：
![](https://main.qcloudimg.com/raw/e40ef8a2c5b65feb84525d1d00953f5e.png)


### 查看旧证书被哪些 Ingress 引用
1. 登录 [SSL 证书控制台](https://console.cloud.tencent.com/ssl)，选择旧证书右侧的【关联资源】即可查看引用此证书的负载均衡器。如下图所示：
![](https://main.qcloudimg.com/raw/0d5eddfa39dad5ff0746f8b9d117de23.png)
2. 点击负载均衡器的 ID 跳转到【负载均衡】详情页面。如果是 TKE Ingress 的负载均衡器，在标签栏会出现 `tke-clusterId` 和 `tke-lb-ingress-uuid` 的标签，分别表示集群 ID 和 Ingress 资源的 UID。如下图所示：
![](https://main.qcloudimg.com/raw/c7314ab88a9b1e5e8614cd2d6d481a08.png)
3. 在负载均衡器的“基本信息”页面，点击标签行右侧的编辑按钮，即可进入“编辑标签”页面。如下图所示：
![](https://main.qcloudimg.com/raw/a014a893a1bbfbe3105c590d23e8a096.png)
4. 使用 Kubectl 可以查询集群 ID 对应集群的 Ingress，过滤 uid 为 `tke-lb-ingress.uuid` 对应值的 Ingress 资源。参考代码示例如下：
```
$ kubectl get ingress --all-namespaces -o=custom-columns=NAMESPACE:.metadata.namespace,INGRESS:.metadata.name,UID:.metadata.uid | grep 1a******-****-****-a329-eec697a28b35
api-prod    gateway      1a******-****-****-a329-eec697a28b35
```
由查询结果可知，该集群中 `api-prod/gateway` 引用了此证书，因此需要更新这个 Ingress。

### 更新 Ingress

在 TKE 控制台找到上一步中对应的 Ingress 资源，点击 `更新转发配置`:

<img style="width:80%" src="https://main.qcloudimg.com/raw/e73e2a80844a63fcce12dbdeb5cedaea.png" data-nonescope="true">

为新证书 `新建密钥`:

<img style="width:80%" src="https://main.qcloudimg.com/raw/ac0cf5b5261562306ccd058b9c73566e.png" data-nonescope="true">

选择新添加的证书，然后 `创建 Secret`:

<img style="width:80%" src="https://main.qcloudimg.com/raw/20c8607c001e7a867c9c56a95cec894d.png" data-nonescope="true">

修改 Ingress 的 TLS 配置，将证书 Secret 切换成上一步中新创建的 Secret:

<img style="width:80%" src="https://main.qcloudimg.com/raw/e2ce44667f1f8a3437c2bfdaa17e7412.png" data-nonescope="true">

最后点击 `更新转发配置` 后即可完成 Ingress 证书的续期，同理，按照相同步骤更新其它关联了旧证书的 Ingress。
