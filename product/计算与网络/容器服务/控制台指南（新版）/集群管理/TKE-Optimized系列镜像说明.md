## 简介
TKE-Optimized 系列镜像是容器服务（TKE）基于 [TencentOS-kernel](https://github.com/Tencent/TencentOS-kernel) 制作的 Kubernetes 集群节点镜像。针对容器场景全面优化，提供了更高的安全性、稳定性。由腾讯云团队维护定制内核，支持热补丁升级，建议作为您 TKE 集群节点的首选镜像。


## TKE-Optimized 系列镜像的优势

<table>
	<tr><th> 优势 </th><th> 内容 </th></tr>
	<tr><td><b> 内核定制 </b></td><td><ul style="margin: 0;"><li>基于内核社区长期支持的4.14.105版本定制。</li><li>增加适用于云场景的新特性、改进内核性能并修复重大缺陷。</li></ul></td></tr>
	<tr><td><b> 容器支持 </b></td><td><ul style="margin: 0;"><li>针对容器场景进行优化，提供了隔离增强和性能优化特性。</li><li>支持 meminfo、vmstat、cpuinfo、stat、loadavg 等隔离。</li><li>支持 sysctl 隔离，例如 tcp_no_delay_ack 和 tcp_max_orphans。</li><li>修复了大量文件系统和网络的 bug。</li></ul></td></tr>
	<tr><td><b> 性能优化 </b></td><td><ul style="margin: 0;"><li>优化 xfs 内存分配，解决 xfs kmem_alloc 分配失败告警问题。</li><li>优化网络收包大内存分配场景，解决了当 UDP 包量大时，占据过多内存问题。</li><li>限制系统 page cache 占用内存比例，从而避免内存不足影响业务的性能或者 OOM。</li></ul></td></tr>
	<tr><td><b> 支持与更新 </b></td><td><ul style="margin: 0;"><li>内核定期进行更新，增强安全性及功能。</li><li>提供内核的热补丁升级能力。</li></td></tr>
</table>

