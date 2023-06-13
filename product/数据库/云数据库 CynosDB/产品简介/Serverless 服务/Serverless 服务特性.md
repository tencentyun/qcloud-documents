TDSQL-C MySQL 版提供 Serverless 服务以满足企业对特定业务场景的数据库服务要求，助力企业降本增效。本文介绍 Serverless 服务的几大特性。

| 特性项 | 说明 | 
|---------|---------|
|资源扩缩范围（CCU）| 可调整 CCU 弹性扩缩容的范围。Serverless 集群会在该范围内根据实际业务压力自动增加或减少 CCU。|
| 弹性策略 | Serverless 集群会持续监控用户的 CPU、内存等 workload 负载情况，根据一定的规则触发自动扩缩容策略。|
| 自动启停 | Serverless 服务支持自定义实例自动暂停时间，无连接时实例会自动暂停。当有任务连接接入时，实例会秒级无间断自动唤醒。|


## 资源扩缩范围（CCU）
CCU（TDSQL-C Compute Unit）为 Serverless 的计算计费单位，一个 CCU 近似等于1个 CPU 和 2GB 内存的计算资源，每个计费周期的 CCU 使用数量为：`数据库所使用的 CPU 核数` 与 `内存大小的1/2` 二者中取最大值。

Serverless 服务需要设定弹性范围，详细弹性范围区间可参考 [算力配置](https://cloud.tencent.com/document/product/1003/81821)。

建议在第一次设置弹性范围时，最小容量配置为0.25 CCU，最大容量选择较高的值。较小的容量设置可以让您的集群在完全空闲时最大限度地进行缩减，避免产生额外的费用，较大的容量可以在您的集群负载过大时最大限度地进行扩展，稳定度过业务峰值。
>?
>- 如果您的业务场景需要快速扩展到非常高的容量，请考虑将最小容量设置为稍大一些的值。
>- 如果您需要更改资源扩缩范围，可以登录控制台，根据实际的视图模式相应更改。
><dx-tabs>
::: 页签视图
在目标**集群管理页 > 集群详情**下方，单击读写实例右上方的调整配置，在跳转页面进行算力配置更改。调整完成后会立即生效，对业务无感。
![](https://qcloudimg.tencent-cloud.cn/raw/0c6a24c4e1bdb2ed37865b3d4c077ca4.png)
![](https://qcloudimg.tencent-cloud.cn/raw/8c188bcdc6752a228da3775819ab5daf.png)
:::
::: 列表视图
在目标**集群管理页 > 实例列表**对读写实例进行配置调整。调整完成后会立即生效，对业务无感。
![](https://qcloudimg.tencent-cloud.cn/raw/8c188bcdc6752a228da3775819ab5daf.png)
:::
</dx-tabs>
>

## 弹性策略
Serverless 服务的弹性策略是利用监控计算层实现的。通过监控业务负载情况，系统对计算资源进行自动扩缩容，并对该时刻所消耗的资源进行计费。当没有数据库请求时，监控服务会触发计算资源的回收，并通知接入层。当用户再次访问时，接入层则会唤醒集群，再次提供访问。

Serverless 服务的弹性策略一开始会根据用户购买时选择的容量范围，将 CPU、内存资源限制到最大规格，极大程度降低因 CPU 和内存扩容带来的时间影响和使用限制。当集群触发到自动弹性的负载阈值后，Buffer pool 会根据监控提前进行分钟级调整。在这个方案下用户使用数据库可以无感知进行 CPU 扩容，并且不会因为连接突增导致实例 OOM。

## 自动启停
#### 暂停服务
- 您可根据业务需要，自助开启或关闭自动暂停设置，该设置可在 [控制台](https://console.cloud.tencent.com/cynosdb) 进行修改。
>?如需开启或关闭自动暂停设置，您可根据实际视图模式进行相应操作。
><dx-tabs>
::: 页签视图
在目标**集群管理页 > 集群详情**下方，单击读写实例右上方的调整配置，在跳转页面进行自动暂停设置更改。
![](https://qcloudimg.tencent-cloud.cn/raw/72fe9842d7d56a7b30a73f312b6bbc22.png)
:::
::: 列表视图
在目标集群管理页的**实例列表 > 读写实例**的**操作**列单击 **更多 > 调整配置**。
![](https://qcloudimg.tencent-cloud.cn/raw/72fe9842d7d56a7b30a73f312b6bbc22.png)
:::
</dx-tabs>
>

 - 开启状态下，需要设定自动暂停时间，默认为1小时。数据库在该时间内没有连接和 CPU 使用时，将自动暂停，暂停后计算不计费，存储仍然按实际使用量计费。
 - 关闭状态下，数据库会保持持续运行，在没有连接和 CPU 使用时，按用户配置的最小 CCU 算力进行计费，适用于业务有心跳连接的应用场景。

- 您也可以在控制台根据实际视图模式对指定数据库进行手动暂停操作。
<dx-tabs>
::: 页签视图
![](https://qcloudimg.tencent-cloud.cn/raw/b0ecd89a2d609546b69cf763ac41b301.png)
:::
::: 列表视图
![](https://main.qcloudimg.com/raw/fa880723650d7cc8f86f888eb62e5521.png)
:::
</dx-tabs>

>!Serverless 服务的自动暂停的判断条件为是否存在用户连接，如果业务场景需要使用 event_scheduler 来实现定时触发 SQL 的操作，则不建议开启自动暂停。
>

#### 启动服务
处于暂停状态的数据库无法使用控制台功能，如需操作可在数据库自动启动后操作，或根据实际视图模式手动在 [控制台](https://console.cloud.tencent.com/cynosdb) 启动 Serverless 数据库。
<dx-tabs>
::: 页签视图
![](https://qcloudimg.tencent-cloud.cn/raw/641cf3ee2737ed6f5f55e2cb3ac4fb18.png)
:::
::: 列表视图
![](https://main.qcloudimg.com/raw/a1068366aa2b08d3043d9852b7e73663.png)
:::
</dx-tabs>


#### 连接不断转发请求能力
当有连接访问时，系统会秒级自动启动处于暂停状态的数据库，用户不需设置重连机制。

TDSQL-C MySQL 版的接入层增加了一个恢复感知器（简称 perceptron）的模块来实现请求转发，perceptron 在和客户端握手之后，不断用户连接，恢复集群后，与 TDSQL-C MySQL 版握手，后续转发四层报文。
整体流程设计采用了两个挑战随机数进行鉴权，以实现中继模块 perceptron 不存储用户名密码的情况下也可以完成用户名密码验证，保证了用户密码的安全性，也不会引入存储密码不一致的问题。
![](https://qcloudimg.tencent-cloud.cn/raw/2fa0215f51fe80c40964c4ba48bdc7d5.png)

在实例暂停的状态下，如果有连接发起，MySQL 客户端首先会同 perceptron 进行 TCP 握手（P0），完成 TCP 握手后，perceptron 会向客户端发送 “随机数 A” 进行挑战（P1），MySQL 客户端用自己的账号密码和 “随机数 A” 来计算并回复自己的 “登录解答 A”（P2）。由于 perceptron 并没有存储用户的账号密码，所以无法校验 “登录解答 A” 是否正确，但 perceptron 能区分客户端是 MySQL 客户端，还是其他类型的客户端（perceptron 在机器学习界是分类器，区分不同类型的客户端也是用他命名的原因之一）。校验 “登录解答 A” 将由 TDSQL-C MySQL 版计算层（下文简称 TDSQL-C）来完成，perceptron 通过管控唤醒 TDSQL-C 后（P3），开始下一步的登录校验流程。

在和 perceptron TCP 握手之后（P4），对于 TDSQL-C 来说，perceptron 也是一个普通的 MySQL 客户端，所以也发送一个 “随机数 B” 挑战（P5）给 perceptron。Perceptron 的回复是一个特殊的 MySQL 报文（P6），首先它用 “随机数 B” 和 perceptron 自身的鉴权机制计算得到 “登录解答 B” 并放入报文中，其次它也将 “随机数 A” 和 “登录解答 A” 捎带在此报文中。 TDSQL-C 收到特殊的解答报文后会做两次校验，第一次是 “随机数 B” 和 “登录解答 B” 的正确性以及 perceptron 的身份，通过后再进行第二次的 “随机数 A” 和 “登录解答 A” 的正确性，通过即以用户身份进行登录，并回复 perceptron 登录成功（P7）。Perceptron 进而回复用户登录成功（P8）。

当集群处于暂停状态时，仅保留 perceptron 的路由，当集群恢复后时，系统同时保留 perceptron 的路由和 TDSQL-C 的路由，并设置 perceptron 的路由权重为 0，以实现新增连接直连到 TDSQL-C，同时存量与perceptron 已经建连的连接依然能够通讯。
