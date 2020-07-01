腾讯云云监控为负载均衡（CLB）提供以下监控指标：

## 负载均衡器实例监控指标

<table class="t"><tbody><tr>
<th><b>指标中文名</b></th>
<th><b>指标英文名</b></th>
<th><b>单位</b></th>
<th><b>维度</b></th>
<tr>
<td> 活跃连接数
<td> rrv_connum
<td> 个
<td> 后端服务器IP、后端服务器端口和VPC ID
<tr>
<td> 非活跃连接数
<td> rrv_inactive_conn
<td> 个
<td> 后端服务器IP、后端服务器端口和VPC ID
<tr>
<td> 入包量
<td> rrv_inpkg
<td> 个/s
<td> 后端服务器IP、后端服务器端口和VPC ID
<tr>
<td> 入流量
<td> rrv_intraffic
<td> bps
<td> 后端服务器IP、后端服务器端口和VPC ID
<tr>
<td> 新建连接数
<td> rrv_new_conn
<td> 个
<td> 后端服务器IP、后端服务器端口和VPC ID
<tr>
<td> 出包量
<td> rrv_outpkg
<td> 个/s
<td> 后端服务器IP、后端服务器端口和VPC ID
<tr>
<td> 出流量
<td> rrv_outtraffic
<td> bps
<td> 后端服务器IP、后端服务器端口和VPC ID
</tbody></table>

## 后端服务器监控指标

<table><tbody><tr>
<th><b>指标中文名</b></th>
<th><b>指标英文名</b></th>
<th><b>单位</b></th>
<th><b>维度</b></th>
<tr>
<td> 活跃连接数
<td> rv_connum
<td> 个
<td> 后端服务器IP和VPC ID
<tr>
<td> 非活跃连接数
<td> rv_inactive_conn
<td> 个
<td> 后端服务器IP和VPC ID
<tr>
<td> 入包量
<td> rv_inpkg
<td> 个/s
<td> 后端服务器IP和VPC ID
<tr>
<td> 入流量
<td> rv_intraffic
<td> bps
<td> 后端服务器IP和VPC ID
<tr>
<td> 新建连接数
<td> rv_new_conn
<td> 个
<td> 后端服务器IP和VPC ID
<tr>
<td> 出包量
<td> rv_outpkg
<td> 个/s
<td> 后端服务器IP和VPC ID
<tr>
<td> 出流量
<td> rv_outtraffic
<td> bps
<td> 后端服务器IP和VPC ID
</tbody></table>

## 后端服务器端口级别监控指标

<table class="t"><tbody><tr>
<th><b>指标名称</b></th>
<th><b>含义</b></th>
<th><b>单位</b></th>
<th><b>维度</b></th>
<tr>
<td> 活跃连接数（端口级别）
<td> rrv_connum
<td> 个
<td> 后端服务器IP、后端服务器端口和VPC ID
<tr>
<td> 非活跃连接数（端口级别）
<td> rrv_inactive_conn
<td> 个
<td> 后端服务器IP、后端服务器端口和VPC ID
<tr>
<td> 入包量（端口级别）
<td> rrv_inpkg
<td> 个/s
<td> 后端服务器IP、后端服务器端口和VPC ID
<tr>
<td> 入流量（端口级别）
<td> rrv_intraffic
<td> bps
<td> 后端服务器IP、后端服务器端口和VPC ID
<tr>
<td> 新建连接数（端口级别）
<td> rrv_new_conn
<td> 个
<td> 后端服务器IP、后端服务器端口和VPC ID
<tr>
<td> 出包量（端口级别）
<td> rrv_outpkg
<td> 个/s
<td> 后端服务器IP、后端服务器端口和VPC ID
<tr>
<td> 出流量（端口级别）
<td> rrv_outtraffic
<td> bps
<td> 后端服务器IP、后端服务器端口和VPC ID
</tbody></table>


有关更多负载均衡的监控指标，可以查看云监控 API 中的[读取监控数据接口](https://cloud.tencent.com/doc/api/405/4667)。

