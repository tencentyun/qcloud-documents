## 通用接口
<table>
<thead>
<tr>
<th width="30%">接口名</th>
<th width="40%">Action</th>
<th width="30%">功能描述</th>
</tr>
</thead>
<tbody><tr>
<td><a href="https://cloud.tencent.com/document/product/214/4007" target="_blank">查询负载均衡异步接口的执行结果</a></td>
<td >DescribeLoadBalancersTaskResult</td>
<td >查询负载均衡异步操作接口的执行结果。</td>
</tr>
<tr>
<td ><a href="https://cloud.tencent.com/document/product/214/1254" target="_blank">购买负载均衡</a></td>
<td>CreateLoadBalancer</td>
<td>通过该接口来购买负载均衡。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/1328" target="_blank">查询负载均衡实例价格</a></td>
<td>InquiryLBPriceAll</td>
<td>查询负载均衡实例的价格。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/1261" target="_blank">查询负载均衡实例列表</a></td>
<td>DescribeLoadBalancers</td>
<td>查询负载均衡实例的列表。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/214/1257" target="_blank">删除负载均衡实例</a></td>
<td>DeleteLoadBalancers</td>
<td>删除负载均衡实例。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8801" target="_blank">负载均衡监控接口</a></td>
<td>GetMonitorData</td>
<td>查询负载均衡的监控数据。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/6045" target="_blank">更换 HTTPS 类型负载均衡证书</a></td>
<td>ReplaceCert</td>
<td>更换负载均衡使用的证书。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/6046" target="_blank">查询证书关联的负载均衡监听器</a></td>
<td>GetCertListWithLoadBalancer</td>
<td>查询证书关联的负载均衡信息。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/37704" target="_blank">克隆负载均衡</a></td>
<td>CloneLB</td>
<td>克隆负载均衡。</td>
</tr>
</tbody></table>

## 传统型负载均衡相关接口
### 实例相关接口

<table>
<thead>
<tr>
<th width="30%">接口名</th>
<th width="40%">Action</th>
<th width="30%">功能描述</th>
</tr>
</thead>
<tbody><tr>
<td><a href="https://cloud.tencent.com/document/product/214/1263" target="_blank">修改负载均衡属性信息</a></td>
<td>ModifyLoadBalancerAttributes</td>
<td>修改用户指定的负载均衡实例的属性信息，包括负载均衡实例的名字等。</td>
</tr>
</tbody></table>

### 监听器相关接口

<table>
<thead>
<tr>
<th width="30%">接口名</th>
<th width="40%">Action</th>
<th width="30%">功能描述</th>
</tr>
</thead>
<tbody><tr>
<td><a href="https://cloud.tencent.com/document/api/214/1255" target="_blank">创建负载均衡监听器</a></td>
<td>CreateLoadBalancerListeners</td>
<td>为用户指定的负载均衡实例创建负载均衡监听器。负载均衡监听器包含了客户要转发请求的协议，端口以及健康检查的策略。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/214/1260" target="_blank">获取负载均衡监听器列表</a></td>
<td>DescribeLoadBalancerListeners</td>
<td>返回用户指定的负载均衡实例的监听器列表。包含监听器的唯一 ID，名字，端口健康检查策略等信息。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/214/1256" target="_blank">删除负载均衡监听器</a></td>
<td>DeleteLoadBalancerListeners</td>
<td>删除用户指定的负载均衡实例的一组监听器。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/214/3601" target="_blank">修改负载均衡监听器属性</a></td>
<td>ModifyLoadBalancerListener</td>
<td>修改负载均衡实例的监听器的属性信息，包括监听器的名字，健康检查策略等信息。</td>
</tr>
</tbody></table>

### 后端服务器相关接口
<table>
<thead>
<tr>
<th width="30%">接口名</th>
<th width="40%">Action</th>
<th width="30%">功能描述</th>
</tr>
</thead>
<tbody><tr>
<td><a href="https://cloud.tencent.com/document/api/214/1265" target="_blank">绑定后端服务器到负载均衡</a></td>
<td>RegisterInstancesWithLoadBalancer</td>
<td>将用户指定的一组云服务器关联到用户指定的负载均衡实例上。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/214/1259" target="_blank">获取负载均衡绑定的后端服务器列表</a></td>
<td>DescribeLoadBalancerBackends</td>
<td>获取用户输入的 <em>LoadBalanceId</em> 这个负载均衡实例上关联的云服务器列表。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/214/1264" target="_blank">修改负载均衡后端服务器权重</a></td>
<td>ModifyLoadBalancerBackends</td>
<td>修改关联到负载均衡实例的一组云服务器的权重。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/214/1258" target="_blank">解绑后端服务器</a></td>
<td>DeregisterInstancesFromLoadBalancer</td>
<td>将关联到负载均衡实例的云服务器进行解绑操作。</td>
</tr>
</tbody></table>

### 健康检查相关接口
<table>
<thead>
<tr>
<th width="30%">接口名</th>
<th width="40%">Action</th>
<th width="30%">功能描述</th>
</tr>
</thead>
<tbody><tr>
<td><a href="https://cloud.tencent.com/document/product/214/1326" target="_blank">查询负载均衡健康检查状态</a></td>
<td>DescribeLBHealthStatus</td>
<td>查询负载均衡实例健康状态。</td>
</tr>
</tbody></table>

## 负载均衡相关接口
>?如下负载均衡相关接口已升级到 3.0 版本，旧版 API 接口未来可能停止维护，目前不展示在左侧导航。负载均衡 API 3.0 版本接口定义更加规范，访问时延下降显著，建议使用 [负载均衡 API 3.0](https://cloud.tencent.com/document/product/214/30667)。

### 负载均衡实例相关接口
<table>
<thead>
<tr>
<th width="30%">接口名</th>
<th width="40%">Action</th>
<th width="30%">功能描述</th>
</tr>
</thead>
<tbody><tr>
<td><a href="https://cloud.tencent.com/document/product/214/13295" target="_blank">修改负载均衡名字</a></td>
<td>ModifyForwardLBName</td>
<td>修改负载均衡的名称。</td>
</tr>
</tbody></table>

### 监听器相关接口
<table>
<thead>
<tr>
<th width="30%">接口名</th>
<th width="40%">Action ID</th>
<th width="30%">功能描述</th>
</tr>
</thead>
<tbody><tr>
<td><a href="https://cloud.tencent.com/document/product/214/9005" target="_blank">查询负载均衡监听器列表</a></td>
<td>DescribeForwardLBListeners</td>
<td>查询负载均衡监听器。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/9000" target="_blank">创建七层负载均衡监听器</a></td>
<td>CreateForwardLBSeventhLayerListeners</td>
<td>创建七层监听器。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/9001" target="_blank">创建四层负载均衡监听器</a></td>
<td>CreateForwardLBFourthLayerListeners</td>
<td>创建四层监听器。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8998" target="_blank">修改负载均衡四层监听器属性</a></td>
<td>ModifyForwardLBFourthListener</td>
<td>修改负载均衡四层监听器属性。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8997" target="_blank">修改负载均衡七层监听器属性</a></td>
<td>ModifyForwardLBSeventhListener</td>
<td>修改负载均衡七层监听器属性。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/9004" target="_blank">删除负载均衡监听器</a></td>
<td>DeleteForwardLBListener</td>
<td>删除负载均衡监听器。</td>
</tr>
</tbody></table>


### 转发规则相关接口
<table>
<thead>
<tr>
<th width="30%">接口名</th>
<th width="40%">Action ID</th>
<th width="30%">功能描述</th>
</tr>
</thead>
<tbody><tr>
<td><a href="https://cloud.tencent.com/document/product/214/9011" target="_blank">创建负载均衡监听器转发规则</a></td>
<td>CreateForwardLBListenerRules</td>
<td>创建负载均衡七层监听器转发规则的能力。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/9007" target="_blank">修改负载均衡监听器转发规则的域名</a></td>
<td>ModifyForwardLBRulesDomain</td>
<td>修改负载均衡七层监听器下的域名。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/9008" target="_blank">修改负载均衡监听器转发规则的健康检查及转发路径</a></td>
<td>ModifyLoadBalancerRulesProbe</td>
<td>修改负载均衡七层监听器转发规则的健康检查及转发路径。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/9012" target="_blank">删除七层负载均衡监听器规则</a></td>
<td>DeleteForwardLBListenerRules</td>
<td>删除负载均衡实例七层监听器的转发规则。</td>
</tr>
</tbody></table>

### 云服务器相关接口

<table>
<thead>
<tr>
<th width="30%">接口名</th>
<th width="40%">Action ID</th>
<th width="30%">功能描述</th>
</tr>
</thead>
<tbody><tr>
<td><a href="https://cloud.tencent.com/document/product/214/8987" target="_blank">查询负载均衡云服务器列表</a></td>
<td>DescribeForwardLBBackends</td>
<td>查询负载均后端绑定的云服务器列表。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8989" target="_blank">绑定云服务器到负载均衡四层监听器的转发规则上</a></td>
<td>RegisterInstancesWithForwardLBFourthListener</td>
<td>绑定云服务器到负载均衡四层监听器的转发规则上。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8988" target="_blank">绑定云服务器到负载均衡七层监听器的转发规则上</a></td>
<td>RegisterInstancesWithForwardLBSeventhListener</td>
<td>绑定云服务器到负载均衡七层监听器的转发规则上。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8981" target="_blank"> 修改四层监听器转发规则上云服务器的权重</a></td>
<td>ModifyForwardFourthBackendsWeight</td>
<td>修改绑定到四层监听器的云服务器的权重。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8978" target="_blank">修改七层监听器转发规则上云服务器的权重</a></td>
<td>ModifyForwardSeventhBackends</td>
<td>修改绑定到七层监听器的云服务器的权重。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8984" target="_blank">修改四层监听器转发规则上云服务器的端口</a></td>
<td>ModifyForwardFourthBackendsPort</td>
<td>修改绑定到四层监听器的云服务器的端口。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8979" target="_blank">修改七层监听器转发规则上云服务器的端口</a></td>
<td>ModifyForwardSeventhBackendsPort</td>
<td>修改绑定到七层监听器的云服务器的端口。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8992" target="_blank">解绑负载均衡四层监听器转发规则上的云服务器</a></td>
<td>DeregisterInstancesFromForwardLBFourthListener</td>
<td>解绑负载均衡四层监听器转发规则上的云服务器。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8991" target="_blank">解绑负载均衡七层监听器转发规则上的云服务器</a></td>
<td>DeregisterInstancesFromForwardLB</td>
<td>解绑负载均衡七层监听器转发规则上的云服务器。</td>
</tr>
</tbody></table>

### 健康检查相关接口

<table>
<thead>
<tr>
<th width="30%">接口名</th>
<th width="40%">Action ID</th>
<th width="30%">功能描述</th>
</tr>
</thead>
<tbody><tr>
<td><a href="https://cloud.tencent.com/document/product/214/8995" target="_blank">查询负载均衡健康检查状态</a></td>
<td>DescribeForwardLBHealthStatus</td>
<td>查询负载均衡实例的健康检查。</td>
</tr>
</tbody></table>

### 重定向相关接口
<table>
<thead>
<tr>
<th width="30%">接口名</th>
<th width="40%">Action ID</th>
<th width="30%">功能描述</th>
</tr>
</thead>
<tbody><tr>
<td><a href="https://cloud.tencent.com/document/product/214/9016" target="_blank">查询监听器规则的重定向关系</a></td>
<td>DescribeRewrite</td>
<td>查询负载均衡的重定向关系。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/9014" target="_blank"> 删除重定向配置 </a></td>
<td>DeleteRewrite</td>
<td>删除负载均衡的重定向关系。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/9015" target="_blank">手动重定向配置</a></td>
<td>ManualRewrite</td>
<td>手动添加负载均衡的重定向关系。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/9017" target="_blank">自动重定向配置</a></td>
<td>AutoRewrite</td>
<td>自动生成负载均衡的重定向关系。</td>
</tr>
</tbody></table>
