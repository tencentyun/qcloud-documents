## 数据库实例复制方式
CDB for MySQL数据库实例有如下三种数据复制方式：

* 异步复制

> 应用发起数据更新(含insert、update、delete操作)请求，Master在执行完更新操作后立即向应用程序返回响应，然后Master再向Slave复制数据。

> 数据更新过程中Master不需要等待Slave的响应，因此异步复制的数据库实例通常具有较高的性能，且Slave不可用并不影响Master对外提供服务。但因数据并非实时同步到Slave，而Master在Slave有延迟的情况下发生故障则有较小概率会引起数据不一致。

> CDB for MySQL异步复制采用一主一备的架构。
 
 
* 强同步复制

> 应用发起数据更新(含insert、update、delete操作)请求，Master在执行完更新操作后立即向Slave复制数据，Slave**接收到数据并执行完**后才向Master返回成功信息，Master必须在接受到Slave的成功信息后再向应用程序返回响应。

> 因Master向Slave复制数据是同步进行的，Master每次更新操作都需要同时保证Slave也成功执行，因此强同步复制能最大限度的保障主从数据的一致性。但因每次Master更新请求都强依赖于Slave的返回，因此Slave如果仅有单台，它不可用将会极大影响Master上的操作。

> CDB for MySQL强同步复制采用一主两备的架构，仅需其中一台Slave成功执行即可返回，避免了单台Slave不可用影响Master上操作的问题，提高了强同步复制集群的可用性。

* 半同步复制

> 应用发起数据更新(含insert、update、delete操作)请求，Master在执行完更新操作后立即向Slave复制数据，Slave**接收到数据并写到relay log中（无需执行）**后才向Master返回成功信息，Master必须在接受到Slave的成功信息后再向应用程序返回响应。

> 仅在数据复制发生异常(Slave节点不可用或者数据复制所用网络发生异常)的情况下，Master会暂停（MySQL默认约10秒左右）对应用的响应，将复制方式降级为异步复制。当数据复制恢复正常，将恢复为强同步复制。

> CDB for MySQL半同步复制采用一主一备的架构。
