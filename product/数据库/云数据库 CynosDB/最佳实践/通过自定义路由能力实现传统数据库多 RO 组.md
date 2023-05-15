## 背景
RO 组是只读实例的集合，可以设置其中只读实例的权重进行流量负载均衡，为数据库创建1个或多个只读实例 RO 组。根据需要部署 RO 组，将相应的读请求按一定规则发送到只读实例，可显著提高数据库的读负载能力。TDSQL-C MySQL 版数据库代理支持自定义路由能力，即支持创建多个数据库代理连接地址。不同的数据库代理连接地址，能够分别挂载不同的只读实例。在应用端根据业务需要，对同一数据库关联多个数据库代理地址，即可实现传统数据库的多 RO 组场景。
![](https://qcloudimg.tencent-cloud.cn/raw/2afea7588986fdfaa6bd4bbc04ecb760.png)

## 通过自定义路由能力实现传统数据库多 RO 组
### 前提条件
- 已 [创建集群](https://cloud.tencent.com/document/product/1003/63010)
- 已 [创建只读实例](https://cloud.tencent.com/document/product/1003/45915)

### 步骤1：开通数据库代理
>?开通的数据库代理具备多少节点就可以创建多少个连接地址，为实现多 RO 组场景，开通数据库代理时至少配置2个节点。
>
1. 登录 [TDSQL-C MySQL 版控制台](https://console.cloud.tencent.com/cynosdb/mysql)，在**集群列表**，选择需要开启代理的集群，单击**集群 ID** 或**操作**列的**管理**，进入集群管理页面。
2. 在集群管理页面，选择**数据库代理**页，单击**立即开启**。
![](https://qcloudimg.tencent-cloud.cn/raw/7c9d7fa45963aaf3b28b942d6d785514.png)
3. 在弹出的对话框，完成如下配置，单击**确定**。
<img src="https://qcloudimg.tencent-cloud.cn/raw/567edf553a5ce529f1c0741bd86bab48.png"  style="zoom:90%;"> 
<table>
<thead><tr><th>参数</th><th>说明</th></tr></thead>
<tbody><tr>
<td>网络类型</td>
<td>选择数据库代理的网络，仅支持私有网络 VPC。</td></tr>
<tr>
<td>代理规格</td>
<td>支持选择规格为2核4000MB内存、4核8000MB内存、8核16000MB内存。</td></tr>
<tr>
<td>可用区及节点个数</td>
<td>1. 选择数据库代理可用区，支持单击<strong>新增可用区</strong>来多选，可选择的可用区数量与当前地域可选可用区数量相关。<br>2. 选择节点个数，推荐的代理节点个数为主实例和只读实例 CPU 核数的之和的1/8（向上取整），例如主实例为4核 CPU，只读实例为8核 CPU，则推荐代理数量 = (4 + 8) / 8 ≈ 2，当前版本最多支持选择4个数据库代理节点，建议选择至少2个节点，保证数据库代理具有高可用能力。<br>3. 若您的集群为多可用区部署，为保证数据库代理高可用性，推荐您在主备可用区均配置数据库代理节点，且节点数量为一致。<blockquote class="rno-document-tips rno-document-tips-notice">    <div class="rno-document-tips-body">        <i class="rno-document-tip-icon"></i>        <div class="rno-document-tip-title">注意</div>        <div class="rno-document-tip-desc"><ol><li>如果所选数据库代理与主实例不在同一可用区，通过数据库代理连接时，写入性能可能会下降。</li><li>若计算推荐节点个数后所需代理节点数量超过购买限制，建议选择更高规格代理。</li></ol></div>    </div></blockquote></td></tr>
<tr>
<td>安全组</td>
<td>可根据需要选择已有安全组或新建安全组。<blockquote class="rno-document-tips rno-document-tips-notice">    <div class="rno-document-tips-body">        <i class="rno-document-tip-icon"></i>        <div class="rno-document-tip-title">注意</div>        <div class="rno-document-tip-desc"><p>访问数据库代理需要开通配置安全策略，放通内网访问端口（当前内网端口为：3306），具体详见 <a href="https://cloud.tencent.com/document/product/1003/62745">创建和管理云数据库安全组</a>。</p></div>    </div></blockquote></td></tr>
<tr>
<td>备注</td>
<td>非必填项，可为要开通的数据库代理服务进行备注。</td></tr>
</tbody></table>

### 步骤2：配置默认数据库代理地址（代理地址1）
开通数据库代理后，系统会默认分配一个数据库代理地址，用户需对其进行配置调整，根据需要，重新为实例分配权重。
1. 在**数据库代理** > **概览** > **连接地址**下找到目标访问地址，单击其**操作**列的**调整配置**。
2. 在跳转的窗口下，完成具体策略的配置，单击**下一步**。
 **配置调整**
![](https://qcloudimg.tencent-cloud.cn/raw/644bf89a8561a15b315e05441dbafd06.png)
<table>
<thead><tr><th>参数</th><th>说明</th></tr></thead>
<tbody><tr>
<td>读写属性</td>
<td>选择此代理访问地址的读写属性，支持选择读写分离或只读，若选择读写分离，则自动开启读写分离功能。</td></tr>
<tr>
<td>接入模式</td>
<td>支持<b>均衡分配</b>和<b>就近访问</b>两种接入模式来设置客户端到数据库代理的连接链路，详情请参考 <a href="https://cloud.tencent.com/document/product/1003/90124" target="_blank">接入模式</a>。</td></tr>
<tr>
<td>一致性设置</td>
<td>在读写分离属性下提供了最终一致性、会话一致性和全局一致性三种一致性级别，满足您在不同场景下对一致性的要求，详情请参考 <a href="https://cloud.tencent.com/document/product/1003/76792" target="_blank">一致性级别</a>。</td></tr>
<tr>
<td>连接池状态</td>
<td>连接池功能主要用于减少短连接业务频繁建立新连接带来的实例负载。此项开启，可选择支持的连接池类型，目前默认仅支持会话级连接池。</td></tr>
<tr>
<td>连接池阈值</td>
<td>设置连接池阈值，可选范围：0-300秒。</td></tr>
<tr>
<td>事务拆分</td>
<td>设置是否开启，开启后，在一个事务中拆分读和写到不同的实例上去执行，读请求转发到只读实例，降低主实例负载。</td></tr>
<tr>
<td>故障转移（读写属性为读写分离）</td>
<td>设置是否开启，开启后，数据库代理出现故障时，连接地址将会路由到主实例。</td></tr>
<tr>
<td>自动添加只读实例</td>
<td>设置是否开启，开启后，若您购买新的只读实例，会自动添加到数据库代理中。<ul><li>当读权重为系统自动分配时，新购只读实例按照规格大小默认权重分配。</li><li>当读权重为自定义时，新购只读实例默认加入时权重为0，可通过数据库代理页，连接地址下的调整配置来修改。</li></ul></td></tr>
</tbody></table>

 **配置权重**
 ![](https://qcloudimg.tencent-cloud.cn/raw/812e9fe42a3513f899b25c69d1034662.png)
 >?本文旨在阐述如何利用不同的数据库代理地址分别挂载只读实例实现不同场景的读写分离，以下假设集群下已有的只读实例为：R1、R2、R3、R4。
 >
 在配置权重界面，根据需要选择系统自动分配或自定义，然后启用 R1、R2，并设置权重，单击**确定**。
 
###  步骤3：新建数据库代理连接地址（代理地址2）
1. 在数据库代理管理页面，在**连接地址**后单击**新增访问地址**。
![](https://qcloudimg.tencent-cloud.cn/raw/fd11c8b13b474cd6e2cd30c40f83b6e8.png)
2. 在新建连接窗口，完成如下配置，单击**确定**。
**网络配置**
![](https://qcloudimg.tencent-cloud.cn/raw/486588831c4e587c285fe9c532fe47cb.png)
<table>
<thead><tr><th>参数</th><th>说明</th></tr></thead>
<tbody><tr>
<td>网络类型</td>
<td>选择数据库代理的网络，仅支持私有网络 VPC，支持选择自动分配 IP 或指定 IP。</td></tr>
<tr>
<td>安全组</td>
<td>默认选择的安全组与主实例保持一致，也可根据需要选择已有安全组或新建安全组，支持多选安全组。<blockquote class="rno-document-tips rno-document-tips-notice">    <div class="rno-document-tips-body">        <i class="rno-document-tip-icon"></i>        <div class="rno-document-tip-title">注意</div>        <div class="rno-document-tip-desc"><p>访问数据库代理需要开通配置安全策略，放通内网访问端口（当前内网端口为：3306），具体详见 <a href="https://cloud.tencent.com/document/product/1003/62745">创建和管理云数据库安全组</a>。</p></div>    </div></blockquote></td></tr>
<tr>
<td>备注</td>
<td>非必填项，可为新增数据库代理连接地址进行备注。</td></tr>
</tbody></table>

 **配置策略**
![](https://qcloudimg.tencent-cloud.cn/raw/5fcba4dce76f7d65c3aef31bf78f1664.png)
<table>
<thead><tr><th>参数</th><th>说明</th></tr></thead>
<tbody><tr>
<td>读写属性</td>
<td>选择此代理访问地址的读写属性，支持选择读写分离或只读，若选择读写分离，则自动开启读写分离功能。</td></tr>
<tr>
<td>接入模式</td>
<td>支持<b>均衡分配</b>和<b>就近访问</b>两种接入模式，来设置客户端到数据库代理的连接链路，详情请参考 <a href="https://cloud.tencent.com/document/product/1003/90124" target="_blank">接入模式</a>。</td></tr>
<tr>
<td>一致性设置</td>
<td>在读写分离属性下提供了最终一致性、会话一致性和全局一致性三种一致性级别，满足您在不同场景下对一致性的要求，详情请参考 <a href="https://cloud.tencent.com/document/product/1003/76792" target="_blank">一致性级别</a>。</td></tr>
<tr>
<td>连接池状态</td>
<td>连接池功能主要用于减少短连接业务频繁建立新连接带来的实例负载。此项开启，可选择支持的连接池类型，目前默认仅支持会话级连接池。</td></tr>
<tr>
<td>连接池阈值</td>
<td>设置连接池阈值，可选范围：0 - 300秒。</td></tr>
<tr>
<td>事务拆分</td>
<td>设置是否开启，开启后，在一个事务中拆分读和写到不同的实例上去执行，读请求转发到只读实例，降低主实例负载。</td></tr>
<tr>
<td>故障转移（读写属性为读写分离）</td>
<td>设置是否开启，开启后，数据库代理出现故障时，连接地址将会路由到主实例。</td></tr>
<tr>
<td>自动添加只读实例</td>
<td>设置是否开启，开启后，若您购买新的只读实例，会自动添加到数据库代理中。<ul><li>当读权重为系统自动分配时，新购只读实例按照规格大小默认权重分配。</li><li>当读权重为自定义时，新购只读实例默认加入时权重为0，可通过数据库代理页，连接地址下的调整配置来修改。</li></ul></td></tr>
</tbody></table>

 **配置权重**
>?本文旨在阐述如何利用不同的数据库代理地址分别挂载只读实例实现不同场景的读写分离，以下假设集群下已有的只读实例为：R1、R2、R3、R4。
 >
 在配置权重界面，根据需要选择系统自动分配或自定义，然后启用 R3、R4，并设置权重，单击**确定**。
 
###  步骤4：应用服务关联数据库代理地址
 在应用服务侧，为不同的业务分别关联代理地址1和代理地址2，通过数据库代理地址的请求，全部经过代理集群中转访问数据库不同 RO 组内的主从节点，进行读写分离，即实现多 RO 组场景。
 


