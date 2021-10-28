
如您有自定义的权限管理诉求，您可以通过创建 CAM 自定义策略，并关联至子账号实现自定义授权。您可参考文本并根据实际业务诉求进行配置。

## CAM 元素参考

CAM 自定义策略核心元素包括：操作（action）、资源（resource）、生效条件（condition）以及效力（effect）。

### 1. 操作（action）

描述允许或拒绝的操作。操作可以是 API（以 name 前缀描述）或者功能集（一组特定的 API，以 actionName 前缀描述）。该元素是必填项。您可以查看 [TCM 接入 CAM 的 API](#camApi)。

### 2. 资源（resource）

描述授权的具体数据。资源是用六段式描述。您可以查看 [TCM 资源描述](#camResource)。

### 3. 生效条件（condition）

描述策略生效的约束条件。条件包括操作符、操作键和操作值组成。条件值可包括时间、IP 地址等信息。

### 4. 效力（effect）

描述声明产生的结果是“允许”还是“显式拒绝”。包括 allow（允许）和 deny （显式拒绝）两种情况。该元素是必填项。

### 5. 自定义策略样例

该策略为：允许对广州的两个mesh实例：mesh-abcd1234 和 mesh-1234abcd 做获取详情操作。

```
{
    "version": "2.0",
    "statement": [
        {
            "effect": "allow",
            "resource": [
                "qcs::tcm:gz:uin/1234567:mesh/mesh-abcd1234",
                "qcs::tcm:gz:uin/1234567:mesh/mesh-1234abcd"
            ],
            "action": [
                "name/tcm:DescribeMesh"
            ]
        }
    ]
}
```

更多关于 CAM 自定义策略语法逻辑，请参见 [CAM 语法逻辑](https://cloud.tencent.com/document/product/598/10596)。

## CAM 中可授权的 TCM 资源 [](id:camResource)

| 资源 | 授权策略中的资源描述方法 |
| :-------- | -------------- |
| 服务网格 |  ` qcs::tcm:$region:$account:mesh/$meshid `  |

其中：

- `$region`：描述地域信息，应为某个 region 的 ID，例如 `gz` 为广州。
- `$account`：描述资源拥有者的主账号信息，表示为 `uin/${uin}`，例如 `uin/12345678`，若值为空则表示创建策略的 CAM 用户所属的主账号。
- `$meshid`：描述mesh实例信息，应为某个网格的 ID，或者 `*`。

关于授权策略中的资源描述方式，请参见 [资源描述方式](https://cloud.tencent.com/document/product/598/10606)。

## CAM 中可对 TCM 进行授权的接口 [](id:camApi)

在 CAM 中，可以对 TCM mesh 资源进行以下操作（action）的授权。

### Mesh 实例相关

| API 操作 | API 描述 | 资源 |
| :-------- | :--------| :------ |
| CreateMesh	|  创建服务网格 | mesh 资源 ` qcs::tcm:$region:$account:mesh/* ` |
| DeleteMesh	|  删除服务网格 | mesh 资源 ` qcs::tcm:$region:$account:mesh/$meshid ` |
| DescribeMesh |  获取指定服务网格 | mesh 资源 ` qcs::tcm:$region:$account:mesh/$meshid ` |
| ListMeshes	|  获取服务网格列表 | mesh 资源 ` qcs::tcm:$region:$account:mesh/$meshid ` |
| ModifyMesh	|  修改服务网格配置 | mesh 资源 ` qcs::tcm:$region:$account:mesh/$meshid ` |
| UpgradeMesh	|  升级服务网格 | mesh 资源 ` qcs::tcm:$region:$account:mesh/$meshid ` |

### Istio 资源相关

| API 操作 | API 描述 | 资源 |
| :-------- | :--------| :------ |
|  ForwardRequestRead |  读 Istio 的 CRD 资源 | mesh 资源 ` qcs::tcm:$region:$account:mesh/$meshid ` |
| ForwardRequestWrite |  写 Istio 的 CRD 资源 | mesh 资源 ` qcs::tcm:$region:$account:mesh/$meshid ` |

### 服务发现相关

| API 操作 | API 描述 | 资源 |
| :-------- | :--------| :------ |
|  LinkClusterList |  关联集群到服务网格实例 | mesh 资源 ` qcs::tcm:$region:$account:mesh/$meshid ` |
| UnlinkCluster |  解除关联集群 | mesh 资源 ` qcs::tcm:$region:$account:mesh/$meshid ` |

### 边缘代理网关相关

| API 操作 | API 描述 | 资源 |
| :-------- | :--------| :------ |
| CreateIngressGateway |  创建 IngressGateway | mesh 资源 ` qcs::tcm:$region:$account:mesh/$meshid ` |
| DeleteGatewayInstance |  删除 IngressGateway | mesh 资源 ` qcs::tcm:$region:$account:mesh/$meshid ` |
| DescribeIngressGatewayList |  查询 IngressGateway 列表 | mesh 资源 ` qcs::tcm:$region:$account:mesh/$meshid ` |
| ModifyIngressGateway | 修改 IngressGateway | mesh 资源 ` qcs::tcm:$region:$account:mesh/$meshid ` |

### 体验环境相关

| API 操作 | API 描述 | 资源 |
| :-------- | :--------| :------ |
| CreateTrial |  创建服务网格一键体验环境 | 只对接口进行鉴权 `*` |
| DeleteTrial |  删除服务网格一键体验环境 | 只对接口进行鉴权 `*` |
| RetryTrialTask |  重试创建服务网格一键体验环境 | 只对接口进行鉴权 `*` |
