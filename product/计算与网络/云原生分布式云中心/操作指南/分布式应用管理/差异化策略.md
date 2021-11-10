## 简介

**分布式应用管理**支持将 K8s 资源分发至多个集群上并统一管理，减少用户重复定义，实现精简化、方便配置。在向多集群发布应用时，经常遇到批量配置、差异化配置、灰度更新、变更回滚等场景，利用**差异化策略**能够很好的解决上述场景，例如：

- 为所有分发的资源打上统一的标签，例如 "apps.my.company/deployed-by: my-platform"。
- 为分发到某个集群上的资源实例配置集群信息，例如 "apps.my.company/running-in: cluster-01"。
- 独立调整应用在每个集群中的副本数目、镜像名称等配置，例如为一个 my-nginx （声明的副本数为 3）的 Deployment 应用，指定分发到集群 cluster-01、集群 cluster-02、集群 cluster-03 上的副本数目分别为 3，5，7。
- 在分发到集群 cluster-01 之前，调整应用在该集群中的一些配置，比如注入一个 Sidecar 容器。
- 遇到如大促、突发流量、紧急扩容等情况，要对应用进行变更时，可以针对指定集群进行变更发布，减小风险范围。支持回滚操作，恢复到变更前的状态。
- 定义了多个差异化配置，通过 priority 优先级来指定不同差异化策略的权重，避免冲突。


## 基本概念
### 差异化策略
**分布式应用管理**提供两种差异化策略用于不同集群间的差异化配置：

#### Globalization 策略

描述 cluster-scoped （集群作用域） 的差异化配置策略，用于不同集群间通用全局配置，比如批量对资源进行无差异化的配置标签。 

#### Localization 策略

描述 namespace-scoped （集群命名空间作用域）的差异化配置策略，单独指定某个集群的配置，比如更改某个集群下 Deployment 的副本数，升级镜像，增加 Sidecar 容器等。

### Priority 优先级

Localization 和 Globalization 两者均支持按照 Priority（优先级）进行管理和配置，优先级的高低通过0 - 1000的数值来定义，值越小，优先级越低，默认是500。
在进行差异化渲染的时候，Clusternet 会按照 Globalization (低优先级) > Globalization (高优先级) > Localization (低优先级) > Localization (高优先级) 的次序，依次将声明的 Override 进行 apply。

### Override 策略

提供了两种 Override 策略：ApplyLater（默认）和 ApplyNow。ApplyLater 表明 Localization/Globalization 差异化策略不会立即生效到资源上，将在随后下一次变更或资源更新的时生效。ApplyNow 表示即时生效，定义的差异化策略将立即匹配到应用对象中，下发到对应的目标集群。

### Override 类型

支持 **MergePatch** 和 **JSONPatch** 两种格式，用于描述指定资源配置的变更。两种格式的定义如下：

- Json Patch [JSON Patch, RFC 6902](https://tools.ietf.org/html/rfc6902)。
- Merge Patch  [JSON Merge Patch, RFC 7386](https://tools.ietf.org/html/rfc7386)。

更多关于两种格式的比较请参见 [JSON Patch and JSON Merge Patch](https://erosb.github.io/post/json-patch-vs-merge-patch/)。

## 配置说明



#### 方式1: 使用YAML

所有通过**分布式应用管理**分发的应用资源都可以配置差异化策略，支持新建、更新和删除差异化策略。
差异化策略支持通过 YAML 方式配置，单击**新建差异化策略**或**更新差异化策略**进入策略编辑页面，编辑 Localization 策略。例如：

```yaml
apiVersion: apps.clusternet.io/v1alpha1
kind: Localization
metadata:
  labels:
    f07d0bec-fac8-4ed1-b4e5-1e2f00111111: Deployment
  name: bb-overrides
  namespace: clusternet-flh9s
spec:
  priority: 300
  feed:
    apiVersion: apps/v1
    kind: Deployment
    name: bb
    namespace: demo
  overridePolicy: ApplyLater
  overrides:
    - name: scale-replicas
      type: JSONPatch
      value: |-
        [
          {
            "path": "/spec/replicas",
            "value": 1,
            "op": "replace"
          }
        ]
```

其中，**spec.feed** 字段描述该差异化策略所关联的应用资源。**spec.overridePolicy** 字段指定 Override 策略是 ApplyLater 还是 ApplyNow。**spec.overrides** 定义要处理的差异化配置，支持 **MergePatch** 和 **JSONPatch** 两种格式，在 **value** 字段处填写 Patch。

上面差异化策略 YAML 配置，表示为 Deployment bb 应用资源进行差异化配置，使用 JSONPatch 格式补丁，将该应用的 **/spec/replicas** 副本数设置为1。该差异化策略的优先级为300，如果有优先级更高的策略同样修改了该应用 **/spec/replicas** 配置，当前策略修改将会被覆盖。

>? **spec.overrides.value** 字段内容遵循 **MergePatch** 和 **JSONPatch** 标准，用户可利用相应工具帮助生成补丁内容，例如 [JSON Patch Builder Online](https://json-patch-builder-online.github.io/)。


#### 方式2: 使用控制台

使用控制台可视化页面配置差异化策略，将在后续版本推出，敬请期待。


## 相关资源

**差异化策略**基于开源多集群应用治理 [Clusternet](https://github.com/clusternet/clusternet) 项目实现，更多信息请访问开源项目网站。
