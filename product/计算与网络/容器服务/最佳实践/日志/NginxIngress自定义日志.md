

容器服务 TKE 通过集成日志服务 CLS，提供了全套完整的产品化能力，实现 Nginx-ingress 日志采集、消费能力。更多请查看 [Nginx-ingress 日志配置](https://cloud.tencent.com/document/product/457/50505)。若默认的日志索引不符合您的日志需求，您可以自定义日志索引，本文向您介绍如何更新 Nginx Ingress 的日志索引。

## 前提条件

1. Nginx Ingress 为1.1.0及以上版本。请登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，在**集群详情 > 组件管理**中查看 Nginx Ingress 的组件版本。
![](https://qcloudimg.tencent-cloud.cn/raw/26d4c551dde44fae20831f2becd26f59.png)
2. Nginx Ingress 实例为 v0.49.3及以上版本。请登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，在**集群详情 > 服务与路由**中选择 **NginxIngress**，单击实例右侧的**查看YAML**。在 YAML 中，镜像 `ccr.ccs.tencentyun.com/paas/nginx-ingress-controller` 的版本需要大于等于 v0.49.3。
![](https://qcloudimg.tencent-cloud.cn/raw/8edd2d4adfd5f2224355221ab4e4bf8c.png)
- 已开启 Nginx Ingress 日志服务。操作详情见 [TKE Nginx-ingress 采集日志](https://cloud.tencent.com/document/product/457/50505#tke-nginx-ingress-.E9.87.87.E9.9B.86.E6.97.A5.E5.BF.97)。

## 操作步骤

>! 修改日志结构需要了解 Nginx Ingress 的日志流，如日志的输出、日志的采集、日志的索引的配置，其中日志输出和采集缺失或配置出错，都会导致日志修改失败。 


[](id:step1)
### 步骤1：修改 Nginx Ingress 实例的日志输出格式

Nginx Ingress 实例的日志配置在该实例的主配置 ConfigMap 中。ConfigMap 的名称为 `实例名-ingress-nginx-controller`，需要修改的 Key 是 `log-format-upstream`，如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/ef13cea94d0da03b17fca68ad49e431e.png)

#### 示例
在日志中增加两个连续的字符串：`$namespace` 和 `$service_name`，并放在日志内容的最后，添加位置如下图所示：
![](https://qcloudimg.tencent-cloud.cn/raw/8e2ac7866c60bf896cd2895056b5124a.png)

如您需要了解更多 Nginx Ingress 的日志字段，请参考 [文档](https://kubernetes.github.io/ingress-nginx/user-guide/nginx-configuration/log-format/)。

### 步骤2：修改集群内日志采集上报 Agent 的格式

集群内日志采集规则在 logconfigs.cls.cloud.tencent.com 型资源对象中。请登录 [容器服务控制台](https://console.cloud.tencent.com/tke2)，在**集群详情 > 资源对象浏览器**中，您可以找到该资源对象，名称为 `实例名-ingress-nginx-controller`。您可在**编辑YAML**中进行修改。
![](https://qcloudimg.tencent-cloud.cn/raw/6008f437941eba69d429c719ace7fc6d.png) 

需要修改字段包括：

- beginningRegex：日志开始的正则表达式
- keys：日志的字段
- logRegex：日志结束的正则表达式

正则和 Nginx 的日志行格式匹配。建议在 Nginx 已有日志格式后面追加字段，同时声明在 keys 的末尾。并追加该字段的正则解析到 beginningRegex、logRegex 的末尾。

#### 示例
在 keys 后面追加 [步骤1](#step1) 中的两个字段，然后分别在 beginningRegex、logRegex 的末尾增加正则表达式字符串。如下图所示：

![](https://qcloudimg.tencent-cloud.cn/raw/3b15ec6ffc2a44f7eb852800121620aa.png)

### （可选）步骤3：修改 CLS 的日志索引格式 

如果需要检索该字段的能力，则需要在对应日志主题中，添加新字段的索引。您可以在日志服务控制台操作，操作完成之后所有采集到的日志都可以通过索引进行检索。操作详情见 [配置索引](https://cloud.tencent.com/document/product/614/50922)。
 

![](https://qcloudimg.tencent-cloud.cn/raw/cafd4249ccd0602a8a2d19fa71e61943.png)
![](https://qcloudimg.tencent-cloud.cn/raw/b0e2684e118ab2eb159e25e9a0c395cd.png)

## 恢复初始设置

因为修改日志规则步骤较复杂，且涉及到正则表达式，操作过程中有任何一个步骤错误，都可能导致日志采集失败。若日志采集报错，此时建议您恢复原始的日志采集能力，您需要先关闭日志采集功能，然后再次 [开启日志采集](https://cloud.tencent.com/document/product/457/36771)。
