## 操作背景
使用 TKE 控制台创建的 Ingress 配置的证书会引用 [SSL 证书](https://console.cloud.tencent.com/ssl) 里托管的证书，如果 Ingress 使用的时间很长，证书可能会面临过期的风险，一旦证书过期，可能就会对线上业务造成很大的影响。所以，我们需要在证书过期前进行续期，本文将介绍如何为 Ingress 证书续期。

## 操作步骤
### 查询快过期的证书

在 [SSL证书-证书管理](https://console.cloud.tencent.com/ssl) 页面按到期时间升序排列显示证书，找到快过期的证书:

<img style="width:80%" src="https://main.qcloudimg.com/raw/d9ec77161d6afae329594d8095f9efce.png" data-nonescope="true">

### 添加新证书

为旧证书续期生成新证书，根据自身情况选择购买证书、申请免费证书或上传证书中一种方式来添加新证书:

<img style="width:80%" src="https://main.qcloudimg.com/raw/53f057b42edca1d97758f0c3a7544fff.png" data-nonescope="true">

### 查看旧证书被哪些 Ingress 引用

鼠标放到旧证书的 `关联资源` 一列的图标上，可以看到有哪些负载均衡器在引用这个证书:

<img style="width:80%" src="https://main.qcloudimg.com/raw/e609ffaae64608ac52eac0808dacefa4.png" data-nonescope="true">

点击负载均衡器的 ID 跳转到负载均衡器详情页面，如果是 TKE Ingress 的负载均衡器，可以看到被打上了 `tke-clusterId` 和 `tke-lb-ingress-uuid` 的标签，分别表示集群 ID 和 Ingress 资源的 UID:

<img style="width:80%" src="https://main.qcloudimg.com/raw/5dc86312c388666bcb05eb2459296649.png" data-nonescope="true">

点击编辑图标，可以展开标签详情:

<img style="width:80%" src="https://main.qcloudimg.com/raw/c401a2d3a6b240c8c4d09e901ee30375.png" data-nonescope="true">

使用 kubectl 查询这个集群 ID 对应集群的 Ingress，过滤 uid 为 `tke-lb-ingress.uuid` 对应值的 Ingress 资源:

```
$ kubectl get ingress --all-namespaces -o=custom-columns=NAMESPACE:.metadata.namespace,INGRESS:.metadata.name,UID:.metadata.uid | grep 1a4b0e4d-9e62-11ea-a329-eec697a28b35
api-prod    gateway      1a4b0e4d-9e62-11ea-a329-eec697a28b35
```

上面命令示例中查询出了该集群中 `api-prod/gateway` 这个 Ingress 引用了这个证书，所以我们需要更新下这个 Ingress。

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