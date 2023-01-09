## 操作场景

TSE 北极星网格用于解决分布式或者微服务架构中的服务注册与发现、故障容错、流量控制和安全问题，支持多语言客户端、集成多种主流服务框架，帮助用户实现高效、稳定、高可用、免运维的服务治理能力。

本文介绍在 TSE 控制台创建一个PolarisMesh 治理中心实例的操作步骤和应用接入的流程，帮助您快速了解如何使用北极星网格。



## 前提条件

[已获取访问授权](https://cloud.tencent.com/document/product/1364/56268)



## 创建引擎实例

1. 登录 [TSE 控制台](https://console.cloud.tencent.com/tse)。
2. 在**北极星网格**下的 **polarismesh** 页面，单击**新建**。
3. 在购买页根据自身业务需求选择相关配置。
   <dx-alert infotype="explain" title="">
     TSE 北极星网格默认支持同城多活高可用架构。
     </dx-alert>  
   <table>
   <thead>
   <tr>
   <th>参数</th>
   <th>说明</th>
   </tr>
   </thead>
   <tbody><tr>
   <td>计费模式</td>
     <td>支持<b>包年包月</b>和<b>按量付费</b>两种计费方式，如果您的北极星网格使用时间在一个月以上，建议采用预付费（包年包月）模式，具体价格请参见 <a href="https://cloud.tencent.com/document/product/1364/75671">Polarismesh 价格说明</a></td>
   </tr>
   <tr>
   <td>地域</td>
   <td>选择与您部署业务最靠近的地域。</td>
   </tr>
   <tr>
   <td>开源版本</td>
   <td>支持 1.9.0.1。</td>
   </tr>
   <tr>
   <td>产品版本</td>
   <td><ul><li>标准版：可用于测试、生成环境。支持多节点部署。</li>
   <li>开发版：仅支持单节点，1核1G的规格，建议仅用于体验。开发版没有容灾能力。为了保证您业务的稳定性，正式环境强烈建议标准版。</li></ul></td>
   </tr>
   <tr>
   <td>规格</td>
   <td>根据业务需求选择服务实例配额数量。</td>
   </tr>
   <tr>
   <td>集群网络</td>
   <td>所选择的私有网络必须和业务所在的私有网络一致。所选择的子网不用和业务所在的私有网络一致。</td>
   </tr>
   <tr>
   <td>名称</td>
   <td>最长60个字符，支持中英文大小写、-、_，名称一旦创建后不支持修改。</td>
   </tr>
   <tr>
   <td>资源标签</td>
   <td>用于分类管理资源，选填，具体使用方法可参见 <a href="https://cloud.tencent.com/document/product/1364/74387">标签管理</a>。</td>
   </tr>
   </tbody></table>
4. 单击**立即购买**，在 **polarismesh** 列表页面的状态栏，您可以查看到引擎创建的进度。



## 后续步骤

引擎实例创建完成后，您可以根据您的业务场景选择对应的参考文档体验应用接入的操作流程。

<table>
<tr>
<th>应用场景</th>
<th>参考文档</th>
</tr>
<tr>
<td rowspan="3">Java 应用开发</td>
<td><a href="https://cloud.tencent.com/document/product/1364/66652">polaris-Java 接入 </a></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/1364/66658">gRPC-Java 接入 </a></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/1364/66655"> Spring Cloud 接入 </a></td>
</tr>
<tr>
<td rowspan="4">Go 应用开发</td>
<td><a href="https://cloud.tencent.com/document/product/1364/66653">polaris-Go 接入 </a></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/1364/66656">gRPC-Go 接入 </a></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/1364/66655"> Dubbo-Go 接入 </a></td>
</tr>
<tr>
<td><a href="https://cloud.tencent.com/document/product/1364/72008"> Kitex-Go 接入 </a></td>
</tr>
<tr>
<td>PHP 应用接入</td>
<td><a href="https://cloud.tencent.com/document/product/1364/66654"> polaris-PHP 接入 </a></td>
</tr>
<tr>
<td>网关接入</td>
<td><a href="https://cloud.tencent.com/document/product/1364/68143"> Nginx 接入 </a></td>
</tr>
<tr>
<td>迁移指南</td>
<td><a href="https://cloud.tencent.com/document/product/1364/70567"> Eureka 迁移指南</a></td>
</tr>
</table>
