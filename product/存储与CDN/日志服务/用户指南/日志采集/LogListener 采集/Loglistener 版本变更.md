本文档为您介绍日志服务 Loglistener 的版本更新记录。

>?
- 多行-完全正则采集模式，在Loglistener2.4.5版本中开始支持。
- loglistener自动升级功能，在loglistener 2.5.0 版本中开始支持。
- 解析失败日志上传功能，在loglistener2.5.2版本中开始支持。
- 为了更好的使用体验，建议 [前往安装/升级至最新版本](https://cloud.tencent.com/document/product/614/17414)。

<table>
	<tr><th style="width: 10%;">版本号</th><th style="width: 11%;">变更类型</th><th>描述</th></tr>
	<tr><td><b>v2.5.3</b></td><td>Bug 修复</td><td>修复内存问题引发 loglistener 工作异常。</td></tr>
	<tr><td rowspan=2><b>v2.5.2</b></td><td>新功能</td><td>支持解析失败日志上传需求。</td></tr>
	<tr><td>Bug 修复</td><td>修复黑名单 bug，黑名单 FILE 模式支持通配符过滤。</td></tr>
	<tr><td><b>v2.5.1</b></td><td>体验优化</td><td>优化当采集文件找不到断点元数据时的处理。</td></tr>
	<tr><td><b>v2.5.0</b></td><td>新功能</td><td><ul  style="margin: 0;"><li>支持 Loglistener 自动升级。</li><li>支持在 Ubuntu 系统下，Loglistener 自启动。</li></ul></td></tr>
	<tr><td><b>v2.4.6</b></td><td>Bug 修复</td><td><ul  style="margin: 0;"><li>修复变更采集配置时，相关配置cache的数据残留问题。</li><li>修复处理软链接的IN_DELETE事件时，影响其他指向此realpath文件的软链接文件采集的问题。</li><li>修复对于同一源文件同时使用文件软链接和目录软连接进行采集时，loglistener会退出的问题。</li></ul></td></tr>
	<tr><td><b>v2.4.5</b></td><td>新功能</td><td>新增 multiline_fullregex_log 日志采集类型支持。</td></tr>
	<tr><td><b>v2.4.4</b></td><td>Bug 修复</td><td>修复 msec 功能导致的日志采集使用日志时间不准确的问题。</td></tr>
	<tr><td><b>v2.4.3</b></td><td>新功能</td><td>支持自动检测日志格式（logFormat）。</td></tr>
	<tr><td><b>v2.4.2</b></td><td>Bug 修复</td><td>修复拉取配置时，腾讯云容器场景下相关配置的缓存淘汰问题。</td></tr>
	<tr><td rowspan=2><b>v2.4.1</b></td><td>新功能</td><td>支持毫秒采集日志数据。</td></tr>
	<tr><td>Bug 修复</td><td>修复用户日志中无换行符数据引发的工作异常。</td></tr>
	<tr><td><b>v2.4.0</td><td>新功能</td><td>loglistener 支持进程实例级别监控。</td></tr>
	<tr><td rowspan=2><b>v2.3.9</b></td><td>新功能</td><td>支持采集路径配置黑名单。</td></tr>
	<tr><td>Bug 修复x</td><td>修复 boost 版本库过低导致的内存泄漏。</td></tr>
	<tr><td><b>v2.3.8</b></td><td>新功能</td><td>采集配置支持多路径。</td></tr>
	<tr><td><b>v2.3.6</b></td><td>Bug 修复</td><td><ul  style="margin: 0;"><li>修复无效键值key invalid导致的停止采集问题。</li><li>修复请求失败返回502导致的内存泄漏问题。</li></ul></td></tr>
	<tr><td rowspan=2><b>v2.3.5</b></td><td>新功能</td><td>支持日志上下文检索功能。</td></tr>
	<tr><td>Bug 修复</td><td><ul  style="margin: 0;"><li>修复在静态配置模式下，在上传日志时返回鉴权失败时后续不再采集的问题。</li><li>修复在动态配置模式下，内存超过阈值后，不再读取动态配置的问题。</li><li>修复在日志滚动时，如果生产日志速度过大，偶现重复采集的问题。</li><li>修复在日志上传重试多次失败时，导致的内存泄漏的问题。</li></ul></td></tr>
	<tr><td><b>v2.3.1</b></td><td>Bug 修复</td><td><ul  style="margin: 0;"><li>内存限制优化。</li><li>达到内存限制时，超过3s的请求判定为超时。</li></ul></td></tr>
	<tr><td rowspan=2><b>v2.2.6</b></td><td>新功能</td><td>支持分离配置内外网域名。</td></tr>
	<tr><td>Bug 修复</td><td>修复 getip 引发的 loglistener 工作异常。</td></tr>
	<tr><td rowspan=2><b>v2.2.5</b></td><td>新功能</td><td>支持腾讯云织云环境部署。</td></tr>
	<tr><td>Bug 修复</td><td>修复 getip 的 bug: 导致 core。</td></tr>
	<tr><td><b>v2.2.4</b></td><td>体验优化</td><td><ul  style="margin: 0;"><li>安装和初始化改为：tools/loglistener.sh 的子命令 install 和 init。</li><li>启动改成: /etc/init.d/loglistenerd start|stop|restart。</li></ul></td></tr>
	<tr><td><b>v2.2.3</b></td><td>体验优化</td><td>日志轮转 rename+create 不丢日志。</td></tr>
	<tr><td><b>v2.2.2</b></td><td>体验优化</td><td>日志大小超过512KB自动截断。</td></tr>
	<tr><td><b>更早版本</b></td><td>-</td><td><ul  style="margin: 0;"><li>2.2.2版本的 LogListener 支持完全正则采集。</li><li>2.1.4版本的 LogListener 支持多行全文格式。</li><li>2.1.1版本的 LogListener 支持日志结构化。</li></ul></td></tr>
</table>


