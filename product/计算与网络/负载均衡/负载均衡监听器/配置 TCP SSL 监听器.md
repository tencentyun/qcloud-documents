## TCP SSL 监听器简介
您可以在负载均衡实例上添加一个 TCP SSL 监听器转发来自客户端加密的 TCP 协议请求。TCP SSL 协议适用于需要超高性能、大规模 TLS 卸载的场景。TCP SSL 协议的监听器，后端服务器可直接获取客户端的真实 IP。
>?
>- TCP SSL 监听器正在内测中，如需使用，请提交  [工单申请](https://console.cloud.tencent.com/workorder/category/create?level1_id=6&level2_id=163&level1_name=%E8%AE%A1%E7%AE%97%E4%B8%8E%E7%BD%91%E7%BB%9C&level2_name=%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1%20LB)。
>- TCP SSL 监听器目前仅支持公网负载均衡（不支持内网），不支持传统型负载均衡。

## 前提条件
您需要 [创建负载均衡实例](https://cloud.tencent.com/document/product/214/6149)。

## 配置 TCP SSL 监听器
### 步骤1：打开监听器管理页面
1. 登录 [负载均衡控制台](https://console.cloud.tencent.com/clb)。
2. 在左侧导航栏，选择【实例管理】。
3. 在 CLB 实例列表页单击需配置的实例 ID，进入实例详情页。
4. 单击【监听器管理】标签页，您也可以在列表页的操作栏中单击【配置监听器】。
![](https://main.qcloudimg.com/raw/376f020caf12788e492e7f7300465ea8.png)
5. “监听器管理”页面如下图所示。
![](https://main.qcloudimg.com/raw/8b20cb5510626c49860d5e67c1f2c736.png)

### 步骤2：配置监听器
在 TCP/UDP/TCP SSL 监听器下，单击【新建】，在弹出框中配置 TCP SSL 监听器。
#### 1. 基本配置
<table>
<thead>
<tr>
<th width="15%">监听器基本配置</th>
<th width="70%">说明</th>
<th width="15%">示例</th>
</tr>
</thead>
<tbody><tr>
<td>名称</td>
<td>监听器的名称</td>
<td><span>test-tcpssl-9000&nbsp;&nbsp;&nbsp;&nbsp;</span></td>
</tr>
<tr>
<td>监听协议端口</td>
<td>监听器的协议和监听端口<br><li>监听协议：CLB 支持的协议包括 TCP、UDP、TCP SSL、HTTP、HTTPS，本例选择 TCP SSL。</li><li>监听端口：用来接收请求并向后端服务器转发请求的端口，端口范围为1 - 65535。</li><li>同一个负载均衡实例内，监听端口不可重复。</li></td>
<td>TCP SSL:9000</td>
</tr>
<tr>
<td>SSL 解析方式</td>
<td>支持单向认证和双向认证</td>
<td>单向认证</td>
</tr>
<tr>
<td>服务器证书</td>
<td>可以选择 <a href="https://console.cloud.tencent.com/ssl">SSL 证书平台</a> 中已有的证书，或上传证书</td>
<td>选择已有的证书 cc/UzxFoXsE</td>
</tr>
<tr>
<td>均衡方式</td>
<td>TCP SSL 监听器中，负载均衡支持加权轮询（WRR）和加权最小连接数（WLC）两种调度算法 <br><li>加权轮询算法：根据后端服务器的权重，按依次将请求分发给不同的服务器。加权轮询算法根据<strong>新建连接数</strong>来调度，权值高的服务器被轮询到的次数（概率）越高，相同权值的服务器处理相同数目的连接数。</li><li>加权最少连接数：根据服务器当前活跃的连接数来估计服务器的负载情况，加权最小连接数根据服务器负载和权重来综合调度，当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。</li></td>
<td>加权轮询</td>
</tr>
</tbody></table>

创建 TCP SSL 监听器具体基本配置如下图所示：
![](https://main.qcloudimg.com/raw/292b6d97cc864b901fe24c33f8cb1249.png)

#### 2. 健康检查
| 健康检查配置    | 说明                    | 示例                                |
| ------- | ------------------------ | ---------------------------------------- |
| 健康检查状态 | 开启或关闭健康检查。TCP SSL 监听器中，负载均衡实例向指定的服务器端口发 SYN 包进行健康检查。 | 开启 |
| 响应超时 | <li> 健康检查响应的最大超时时间。</li><li>如果后端云服务器在超时时间内没有正确响应，则判定为健康检查异常。</li><li>可配置范围：2 - 60秒，默认值2秒。</li> | 2s |
| 检测间隔 | <li>负载均衡进行健康检查的时间间隔。</li><li>可配置范围：5 - 300秒，默认值5秒。</li> | 5s |
| 不健康阈值 | <li>如果连续 n 次（n 为填写的数值）收到的健康检查结果失败，则识别为不健康，控制台显示为**异常**。</li><li>可配置范围：2 - 10次，默认值3次。</li> | 3次 |
| 健康阈值 |<li>如果连续 n 次（n 为填写的数值）收到的健康检查结果为成功，则识别为健康，控制台显示为**健康**。</li><li>可配置范围：2 - 10次，默认值3次。 </li> | 3次 |

健康检查具体配置如下图所示：
![](https://main.qcloudimg.com/raw/373dba1c1f3564c708d87c1444184b70.png)

#### 3. 会话保持（暂不支持）
![](https://main.qcloudimg.com/raw/ae0886790d14e2fe8487dd309b31d9a2.png)

### 步骤3：绑定后端云服务器
1. 在“监听器管理”页面，单击已创建完毕的监听器，如上述 `TCP SSL:9000` 监听器，即可在监听器右侧查看已绑定的后端服务。
![](https://main.qcloudimg.com/raw/c22b487fabac14489a521e5573b444b0.png)
2. 单击【绑定】，在弹出框中选择需绑定的后端服务器，并配置服务端口和权重。
 1. 添加端口功能：在右侧“已选择”云服务器框内，单击【添加端口】，即可添加同一个云服务器的多个端口，如同时添加 CVM 的 80、81、82 三个端口。
 2. 默认端口功能：先填写“默认端口”，再选择云服务器，每台云服务器的端口均为默认端口。
![](https://main.qcloudimg.com/raw/e0ef33bc1e3de8bd048f22b046dd2d50.png)

完成步骤1到步骤3之后，TCP SSL 监听器规则已配置完毕，配置详情如下：
![](https://main.qcloudimg.com/raw/a217130cfbaf64d92c9e42d1a07eaccc.png)

### 步骤4：安全组（可选）
您可以配置负载均衡的安全组来进行公网流量的隔离，详情请参见 [配置负载均衡安全组](https://cloud.tencent.com/document/product/214/14733)。

### 步骤5：修改/删除监听器（可选）
如果您需要修改或删除已创建的监听器，请在“监听器管理”页面，单击已创建完毕的监听器，选择【修改】或【删除】来完成操作。
![](https://main.qcloudimg.com/raw/13cde6cfce64bff29f81ecdeaa43545a.png)
