负载均衡 API 已全面升级至3.0版本，基于2.0版本接口访问时延较高和使用复杂的考虑，原负载均衡 API2.0 接口服务将不再提供技术支持，并于北京时间2022年11月30日起下线。如果您的业务还在使用负载均衡 API2.0 相关接口，建议尽快将服务升级至 API3.0 接口，以免对您的业务造成影响。

- 【推荐】当前负载均衡 API2.0 的接口大多为传统型负载均衡使用的接口，您可选择将“传统型负载均衡”升级为“负载均衡”类型，升级后资费不变，VIP 不变，可覆盖传统型负载均衡的所有功能，且能提供更多功能和更好的用户体验。升级后支持直接调用 API3.0 接口。传统型负载均衡升级详情请参见 [传统型负载均衡升级公告](https://cloud.tencent.com/document/product/214/75481)。
- 若您暂未从“传统型负载均衡”升级为“负载均衡”类型，则可选择将 API2.0 接口切换为 API3.0。您可参照下方的 [API2.0 切换3.0接口列表](#APIlist) 找到需切换的新接口，完成升级。


## [API2.0 切换3.0接口列表](id:APIlist)

### 通用接口
<table>
<thead>
<tr>
<th width="35%">API2.0 接口</th>
<th width="35%">API3.0 接口</th>
<th>备注</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/4007" target="_blank">DescribeLoadBalancersTaskResult</a></br>（查询负载均衡异步接口的执行结果）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30683" target="_blank">DescribeTaskStatus</a></br>（查询异步任务状态）</td>
<td rowspan="2">支持切换，切换后该接口可按 API3.0 的调用方式进行调用，不存在鉴权问题。</td>
</tr>
<tr>
<td ><a href="https://cloud.tencent.com/document/product/214/1254" target="_blank">CreateLoadBalancer</a></br>（购买负载均衡实例）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30692" target="_blank">CreateLoadBalancer</a></br>（购买负载均衡实例）</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/1328" target="_blank">InquiryLBPriceAll</a></br>（查询负载均衡实例价格）</td>
<td>/</td>
<td>原有 API 对应的价格查询功能已不再推荐使用。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/1261" target="_blank">DescribeLoadBalancers</a></br>（查询负载均衡实例列表）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30685" target="_blank">DescribeLoadBalancers</a></br>（查询负载均衡实例列表）</td>
<td rowspan="2">支持切换，切换后该接口可按 API3.0 的调用方式进行调用，不存在鉴权问题。</td>
<tr>
<td><a href="https://cloud.tencent.com/document/api/214/1257" target="_blank">DeleteLoadBalancers</a></br>（删除负载均衡实例）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30689" target="_blank">DeleteLoadBalancer</a></br>（删除负载均衡实例）</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8801" target="_blank">GetMonitorData</a></br>（负载均衡监控接口）</td>
<td><a href="https://cloud.tencent.com/document/product/214/8801" target="_blank">GetMonitorData</a></br>（拉取指标监控数据）</td>
<td>此接口为腾讯云可观测平台 API 接口，切换至 API3.0 接口的方式请参见 <a href="https://cloud.tencent.com/document/product/248/81039#getmonitordata">接口迁移说明</a>。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/6045" target="_blank">ReplaceCert</a></br>（更换 HTTPS 类型负载均衡证书）</td>
<td><a href="https://cloud.tencent.com/document/product/214/36907" target="_blank">ReplaceCertForLoadBalancers</a></br>（替换负载均衡实例所关联的证书）</td>
<td rowspan="2">支持切换，切换后该接口可按 API3.0 的调用方式进行调用，不存在鉴权问题。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/6046" target="_blank">GetCertListWithLoadBalancer</a></br>（查询证书关联的负载均衡监听器）</td>
<td><a href="https://cloud.tencent.com/document/product/214/40953" target="_blank">DescribeLoadBalancerListByCertId</a></br>（根据证书ID查询负载均衡）</td>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/37704" target="_blank">CloneLB</a></br>（克隆负载均衡）</td>
<td><a href="https://cloud.tencent.com/document/product/214/64874" target="_blank">CloneLoadBalancer</a></br>（克隆负载均衡实例）</td>
<td>该接口 API3.0 无法沿用 API2.0 的 CAM 权限，调用时可能会出现鉴权失败问题。建议您将“传统型负载均衡”升级为“负载均衡”类型，升级后支持直接调用 API3.0 接口，升级详情请参见 <a href="https://cloud.tencent.com/document/product/214/75481">传统型负载均衡升级公告</a>。</td></tr>
</tr>
</tbody></table>

### 传统型负载均衡接口
#### 实例相关接口
<table>
<thead>
<tr>
<th width="35%">API2.0 接口</th>
<th width="35%">API3.0 接口</th>
<th>备注</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/1263" target="_blank">ModifyLoadBalancerAttributes</a></br>（修改负载均衡属性信息）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30680" target="_blank">ModifyLoadBalancerAttributes</a></br>（修改负载均衡实例的属性）</td>
<td>支持切换，切换后该接口可按 API3.0 的调用方式进行调用。
<dx-alert infotype="notice" title="">
该接口 API2.0 仅支持修改实例名称，对应仅修改实例名称的 CAM 权限。该接口 API3.0 支持修改实例名称、调整网络计费模式、修改绑定的后端服务的地域信息等，对应这些功能的 CAM 权限。切换后，会存在 CAM 权限策略比切换前多的情况。
</dx-alert>

</td></tr>
</tbody></table>

#### 监听器相关接口

<table>
<thead>
<tr>
<th width="35%">API2.0 接口</th>
<th width="35%">API3.0 接口</th>
<th>备注</th>
</tr>
</thead>
<tbody><tr>
<td><a href="https://cloud.tencent.com/document/product/214/1260" target="_blank">DescribeLoadBalancerListeners</a></br>（获取负载均衡监听器列表）</td>
<td><a href="https://cloud.tencent.com/document/product/214/31791" target="_blank">DescribeClassicalLBListeners</a></br>（获取传统型负载均衡监听器列表）</td>
<td>支持切换，切换后该接口可按 API3.0 的调用方式进行调用，不存在鉴权问题。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/1255" target="_blank">CreateLoadBalancerListeners</a></br>（创建负载均衡监听器）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30693" target="_blank">CreateListener</a></br>（创建负载均衡监听器）</td>
<td rowspan="3">该接口 API3.0 无法沿用 API2.0 的 CAM 权限，调用时可能会出现鉴权失败问题。建议您将“传统型负载均衡”升级为“负载均衡”类型，升级后支持直接调用 API3.0 接口，升级详情请参见 <a href="https://cloud.tencent.com/document/product/214/75481">传统型负载均衡升级公告</a>。</td></tr>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/1256" target="_blank">DeleteLoadBalancerListeners</a></br>（删除负载均衡监听器）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30690" target="_blank">DeleteListener</a></br>（删除负载均衡监听器）</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/3601" target="_blank">ModifyLoadBalancerListener</a></br>（修改负载均衡监听器属性）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30681" target="_blank">ModifyListener</a></br>（修改负载均衡监听器属性）</td>
</tr>
</tbody></table>

#### 后端服务器相关接口
<table>
<thead>
<tr>
<th width="35%">API2.0 接口</th>
<th width="35%">API3.0 接口</th>
<th>备注</th>
</tr>
</thead>
<tbody><tr>
<td><a href="https://cloud.tencent.com/document/api/214/1265" target="_blank">RegisterInstancesWithLoadBalancer</a></br>（绑定后端服务器到负载均衡）</td>
<td><a href="https://cloud.tencent.com/document/product/214/31789" target="_blank">RegisterTargetsWithClassicalLB</a></br>（绑定后端服务到传统型负载均衡）</td>
<td  rowspan="3">支持切换，切换后该接口可按 API3.0 的调用方式进行调用，不存在鉴权问题。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/214/1259" target="_blank">DescribeLoadBalancerBackends</a></br>（获取负载均衡绑定的后端服务器列表）</td>
<td><a href="https://cloud.tencent.com/document/product/214/31790" target="_blank">DescribeClassicalLBTargets</a></br>（获取传统型负载均衡绑定的后端服务器列表）</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/214/1258" target="_blank">DeregisterInstancesFromLoadBalancer</a></br>（解绑后端服务器）</td>
<td><a href="https://cloud.tencent.com/document/product/214/31794" target="_blank">DeregisterTargetsFromClassicalLB</a></br>（解绑传统型负载均衡的后端服务器）</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/api/214/1264" target="_blank">ModifyLoadBalancerBackends</a></br>（修改负载均衡后端服务器权重）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30677" target="_blank">ModifyTargetWeight</a></br>（修改监听器绑定的后端机器的转发权重）</td>
<td>该接口 API3.0 无法沿用 API2.0 的 CAM 权限，调用时可能会出现鉴权失败问题。建议您将“传统型负载均衡”升级为“负载均衡”类型，升级后支持直接调用 API3.0 接口，升级详情请参见 <a href="https://cloud.tencent.com/document/product/214/75481">传统型负载均衡升级公告</a>。</td></tr>
</tr>
</tbody></table>

#### 其他相关接口
<table>
<thead>
<tr>
<th width="35%">API2.0 接口</th>
<th width="35%">API3.0 接口</th>
<th>备注</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/1326" target="_blank">DescribeLBHealthStatus</a></br>（查询负载均衡健康检查状态）</td>
<td><a href="https://cloud.tencent.com/document/product/214/31792" target="_blank">DescribeClassicalLBHealthStatus</a></br>（获取传统型负载均衡后端的健康状态）</td>
<td>支持切换，切换后该接口可按 API3.0 的调用方式进行调用，不存在鉴权问题。</td>
</tr>
</tbody></table>


### 负载均衡接口
#### 负载均衡实例相关接口
<table>
<thead>
<tr>
<th width="35%">API2.0 接口</th>
<th width="35%">API3.0 接口</th>
<th>备注</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/13295" target="_blank">ModifyForwardLBName</a></br>（修改负载均衡名字）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30680" target="_blank">ModifyLoadBalancerAttributes</a></br>（修改负载均衡实例的属性）</td>
<td>支持切换，切换后该接口可按 API3.0 的调用方式进行调用，不存在鉴权问题。</td>
</tr>
</tbody></table>

#### 监听器相关接口
<table>
<thead>
<tr>
<th width="35%">API2.0 接口</th>
<th width="35%">API3.0 接口</th>
<th>备注</th>
</tr>
</thead>
<tbody><tr>
<td><a href="https://cloud.tencent.com/document/product/214/9001" target="_blank">CreateForwardLBFourthLayerListeners</a></br>（创建四层负载均衡监听器）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30693" target="_blank">CreateListener</a></br>（创建负载均衡监听器）</td>
<td rowspan="10">支持切换，切换后该接口可按 API3.0 的调用方式进行调用，不存在鉴权问题。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/9000" target="_blank">CreateForwardLBSeventhLayerListeners</a></br>（创建七层负载均衡监听器）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30693" target="_blank">CreateListener</a></br>（创建负载均衡监听器）</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/9011" target="_blank">CreateForwardLBListenerRules</a></br>（创建负载均衡监听器转发规则）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30691" target="_blank">CreateRule</a></br>（创建负载均衡七层监听器转发规则
）</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/9004" target="_blank">DeleteForwardLBListener</a></br>（删除负载均衡监听器）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30690" target="_blank">DeleteListener</a></br>（删除负载均衡监听器）</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/9012" target="_blank">DeleteForwardLBListenerRules</a></br>（删除七层负载均衡监听器规则）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30688" target="_blank">DeleteRule</a></br>（删除负载均衡七层监听器的转发规则）</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/9005" target="_blank">DescribeForwardLBListeners</a></br>（查询负载均衡监听器列表）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30686" target="_blank">DescribeListeners</a></br>（查询负载均衡的监听器列表）</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8998" target="_blank">ModifyForwardLBFourthListener</a></br>（修改负载均衡四层监听器属性）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30681" target="_blank">ModifyLoadBalancerListener</a></br>（修改负载均衡监听器属性）</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8997" target="_blank">ModifyForwardLBSeventhListener</a></br>（修改负载均衡七层监听器属性）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30681" target="_blank">ModifyLoadBalancerListener</a></br>（修改负载均衡监听器属性）</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/9007" target="_blank">ModifyForwardLBRulesDomain</a></br>（修改负载均衡监听器转发规则的域名）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30682" target="_blank">ModifyDomain</a></br>（修改七层转发规则的域名）</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/9008" target="_blank">ModifyLoadBalancerRulesProbe</a></br>（修改负载均衡监听器转发规则的健康检查及转发路径）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30679" target="_blank">ModifyRule</a></br>（修改负载均衡七层监听器的转发规则）</td>
</tr>
</tbody></table>

#### 后端服务相关接口
<table>
<thead>
<tr>
<th width="35%">API2.0 接口</th>
<th width="35%">API3.0 接口</th>
<th>备注</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8992" target="_blank">DeregisterInstancesFromForwardLBFourthListener</a></br>（解绑负载均衡四层监听器转发规则上的云服务器）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30687" target="_blank">DeregisterTargets</a></br>（从负载均衡监听器上解绑后端服务）</td>
<td rowspan="9">支持切换，切换后该接口可按 API3.0 的调用方式进行调用，不存在鉴权问题。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8991" target="_blank">DeregisterInstancesFromForwardLB</a></br>（解绑负载均衡七层监听器转发规则上的云服务器）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30687" target="_blank">DeregisterTargets</a></br>（从负载均衡监听器上解绑后端服务）</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8987" target="_blank">DescribeForwardLBBackends</a></br>（查询负载均衡云服务器列表）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30684" target="_blank">DescribeTargets</a></br>（查询负载均衡绑定的后端服务列表）</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8989" target="_blank">RegisterInstancesWithForwardLBFourthListener</a></br>（绑定云服务器到负载均衡四层监听器的转发规则上）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30676" target="_blank">RegisterTargets</a></br>（绑定后端机器到监听器上）</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8988" target="_blank">RegisterInstancesWithForwardLBSeventhListener</a></br>（绑定云服务器到负载均衡七层监听器的转发规则上）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30676" target="_blank">RegisterTargets</a></br>（绑定后端机器到监听器上）</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8984" target="_blank">ModifyForwardFourthBackendsPort</a></br>（修改四层监听器转发规则上云服务器的端口）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30678" target="_blank">ModifyTargetPort</a></br>（修改监听器绑定的后端机器的端口）</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8981" target="_blank"> ModifyForwardFourthBackendsWeight</a></br>（修改四层监听器转发规则上云服务器的权重）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30677" target="_blank">ModifyTargetWeight</a></br>（修改监听器绑定的后端机器的转发权重）</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8978" target="_blank">ModifyForwardSeventhBackends</a></br>（修改七层监听器转发规则上云服务器的权重）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30677" target="_blank">ModifyTargetWeight</a></br>（修改监听器绑定的后端机器的转发权重）</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8979" target="_blank">ModifyForwardSeventhBackendsPort</a></br>（修改七层监听器转发规则上云服务器的端口）</td>
<td><a href="https://cloud.tencent.com/document/product/214/30678" target="_blank">ModifyTargetPort</a></br>（修改监听器绑定的后端机器的端口）</td>
</tr>
</tbody></table>


#### 健康检查相关接口

<table>
<thead>
<tr>
<th width="35%">API2.0 接口</th>
<th width="35%">API3.0 接口</th>
<th>备注</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/8995" target="_blank">DescribeForwardLBHealthStatus</a></br>（查询负载均衡健康检查状态）</td>
<td><a href="https://cloud.tencent.com/document/product/214/34898" target="_blank">DescribeTargetHealth</a></br>（获取负载均衡后端服务的健康检查状态）</td>
<td>支持切换，切换后该接口可按 API3.0 的调用方式进行调用，不存在鉴权问题。</td>
</tr>
</tbody></table>


#### 重定向相关接口

<table>
<thead>
<tr>
<th width="35%">API2.0 接口</th>
<th width="35%">API3.0 接口</th>
<th>备注</th>
</tr>
</thead>
<tbody>
</tr>
</thead>
<tbody><tr>
<td><a href="https://cloud.tencent.com/document/product/214/9017" target="_blank">AutoRewrite</a></br>（自动重定向配置）</td>
<td><a href="https://cloud.tencent.com/document/product/214/34901" target="_blank">AutoRewrite</a></br>（自动生成负载均衡转发规则的重定向关系）</td>
<td rowspan="4">支持切换，切换后该接口可按 API3.0 的调用方式进行调用，不存在鉴权问题。</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/9016" target="_blank">DescribeRewrite</a></br>（查询监听器规则的重定向关系）</td>
<td><a href="https://cloud.tencent.com/document/product/214/34899" target="_blank">DescribeRewrite</a></br>（查询负载均衡转发规则的重定向关系）</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/9014" target="_blank"> DeleteRewrite </a></br>（删除重定向配置）</td>
<td><a href="https://cloud.tencent.com/document/product/214/34900" target="_blank"> DeleteRewrite </a></br>（删除负载均衡转发规则之间的重定向关系）</td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/214/9015" target="_blank">ManualRewrite</a></br>（手动重定向配置）</td>
<td><a href="https://cloud.tencent.com/document/product/214/34897" target="_blank">ManualRewrite</a></br>（手动添加负载均衡转发规则的重定向关系）</td>
</tr>
</tbody></table>


