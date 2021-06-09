本文档为您介绍日志服务 LogListener 的版本更新记录。

>?
> - 多行-完全正则采集模式，在 LogListener 2.4.5版本中开始支持。
> - LogListener 自动升级功能，在 LogListener 2.5.0 版本中开始支持。
> - 解析失败日志上传功能，在 LogListener 2.5.2版本中开始支持。
> - 为了更好的使用体验，建议 [前往安装/升级至最新版本](https://cloud.tencent.com/document/product/614/17414)。
> 

<table>
	<tr><th style="width: 10%;">版本号</th><th style="width: 11%;">变更类型</th><th>描述</th></tr>
	<tr><td><b>v2.5.9</b></td><td>Bug 修复</td><td>修复资源限制策略。</td></tr>
	<tr><td><b>v2.5.8</b></td><td>Bug 修复</td><td><ul  style="margin: 0;"><li>当移除一个目录软链接时，影响到其它指向相同目标的目录软链接的采集的问题。</li><li>当移除一个目录软链接并再次创建相同软链接后，目录下文件无法采集的问题。</li></ul></td></tr>
	<tr><td><b>v2.5.7</b></td><td>Bug 修复</td><td><ul  style="margin: 0;"><li>当 filesize 大于2G时，会存在重复采集的问题（新引入）。</li><li>当文件数量特别多的时候，文件发生 rename 有可能会导致程序卡住。</li><li>文件采集监控中，某字段无法更新。</li></ul></td></tr>
	<tr><td><b>v2.5.6</b></td><td>Bug 修复</td><td>修复特殊使用场景下，触发采集程序异常，停止工作的问题。</td></tr>
	<tr><td><b>v2.5.5</b></td><td>体验优化</td><td><ul  style="margin: 0;"><li>文件采集元数据 checkpoint 优化，保证重启不丢数据。</li><li>支持资源限制可配置及超限处理，内存、CPU、带宽。</li></ul></td></tr>
	<tr><td rowspan=3><b>v2.5.4</b></td><td>新功能</td><td>支持文件采集监控功能。</td></tr>
	<tr><td>体验优化</td><td>增强内存资源限制处理，当内存超限持续一段时间后，LogListener 自动加载。</td></tr>
	<tr><td>Bug 修复</td><td><ul  style="margin: 0;"><li>修复正则处理异常时，无法拉取采集配置和采集业务阻塞的问题。</li><li>修复 inotify 事件队列溢出时，导致的漏采问题。</li><li>修复多文件同时进行 rename 操作时，可能导致部分文件重新采集的问题。</li><li>修复日志文件轮转时，可能导致的日志投递到非对应日志主题的问题。</li></ul></td></tr>
	<tr><td><b>v2.5.3</b></td><td>Bug 修复</td><td>修复内存问题引发 LogListener 工作异常。</td></tr>
	<tr><td rowspan=2><b>v2.5.2</b></td><td>新功能</td><td>支持解析失败日志上传需求。</td></tr>
	<tr><td>Bug 修复</td><td>修复黑名单 bug，黑名单 FILE 模式支持通配符过滤。</td></tr>
	<tr><td><b>v2.5.1</b></td><td>体验优化</td><td>优化当采集文件找不到断点元数据时的处理。</td></tr>
	<tr><td><b>v2.5.0</b></td><td>新功能</td><td><ul  style="margin: 0;"><li>支持 LogListener 自动升级。</li><li>支持在 Ubuntu 系统下，LogListener 自启动。</li></ul></td></tr>
	<tr><td><b>v2.4.6</b></td><td>Bug 修复</td><td><ul  style="margin: 0;"><li>修复变更采集配置时，相关配置 cache 的数据残留问题。</li><li>修复处理软链接的 IN_DELETE 事件时，影响其他指向此 realpath 文件的软链接文件采集的问题。</li><li>修复对于同一源文件同时使用文件软链接和目录软连接进行采集时，LogListener 会退出的问题。</li></ul></td></tr>
	<tr><td><b>v2.4.5</b></td><td>新功能</td><td>新增 multiline_fullregex_log 日志采集类型支持。</td></tr>
	<tr><td><b>v2.4.4</b></td><td>Bug 修复</td><td>修复 msec 功能导致的日志采集使用日志时间不准确的问题。</td></tr>
	<tr><td><b>v2.4.3</b></td><td>新功能</td><td>支持自动检测日志格式（logFormat）。</td></tr>
	<tr><td><b>v2.4.2</b></td><td>Bug 修复</td><td>修复拉取配置时，腾讯云容器场景下相关配置的缓存淘汰问题。</td></tr>
	<tr><td rowspan=2><b>v2.4.1</b></td><td>新功能</td><td>支持毫秒采集日志数据。</td></tr>
	<tr><td>Bug 修复</td><td>修复用户日志中无换行符数据引发的工作异常。</td></tr>
	<tr><td><b>v2.4.0</td><td>新功能</td><td>LogListener 支持进程实例级别监控。</td></tr>
	<tr><td rowspan=2><b>v2.3.9</b></td><td>新功能</td><td>支持采集路径配置黑名单。</td></tr>
	<tr><td>Bug 修复</td><td>修复 boost 版本库过低导致的内存泄漏。</td></tr>
	<tr><td><b>v2.3.8</b></td><td>新功能</td><td>采集配置支持多路径。</td></tr>
	<tr><td><b>v2.3.6</b></td><td>Bug 修复</td><td><ul  style="margin: 0;"><li>修复无效键值 key invalid 导致的停止采集问题。</li><li>修复请求失败返回502导致的内存泄漏问题。</li></ul></td></tr>
	<tr><td rowspan=2><b>v2.3.5</b></td><td>新功能</td><td>支持日志上下文检索功能。</td></tr>
	<tr><td>Bug 修复</td><td><ul  style="margin: 0;"><li>修复在静态配置模式下，在上传日志时返回鉴权失败时后续不再采集的问题。</li><li>修复在动态配置模式下，内存超过阈值后，不再读取动态配置的问题。</li><li>修复在日志滚动时，如果生产日志速度过大，偶现重复采集的问题。</li><li>修复在日志上传重试多次失败时，导致的内存泄漏的问题。</li></ul></td></tr>
	<tr><td><b>v2.3.1</b></td><td>Bug 修复</td><td><ul  style="margin: 0;"><li>内存限制优化。</li><li>达到内存限制时，超过3s的请求判定为超时。</li></ul></td></tr>
	<tr><td rowspan=2><b>v2.2.6</b></td><td>新功能</td><td>支持分离配置内外网域名。</td></tr>
	<tr><td>Bug 修复</td><td>修复 getip 引发的 LogListener 工作异常。</td></tr>
	<tr><td rowspan=2><b>v2.2.5</b></td><td>新功能</td><td>支持腾讯云织云环境部署。</td></tr>
	<tr><td>Bug 修复</td><td>修复 getip 的 bug: 导致 core。</td></tr>
	<tr><td><b>v2.2.4</b></td><td>体验优化</td><td><ul  style="margin: 0;"><li>安装和初始化改为：tools/loglistener.sh 的子命令 install 和 init。</li><li>启动改成: /etc/init.d/loglistenerd start|stop|restart。</li></ul></td></tr>
	<tr><td><b>v2.2.3</b></td><td>体验优化</td><td>日志轮转 rename+create 不丢日志。</td></tr>
	<tr><td><b>v2.2.2</b></td><td>体验优化</td><td>日志大小超过512KB自动截断。</td></tr>
	<tr><td><b>更早版本</b></td><td>-</td><td><ul  style="margin: 0;"><li>2.2.2版本的 LogListener 支持完全正则采集。</li><li>2.1.4版本的 LogListener 支持多行全文格式。</li><li>2.1.1版本的 LogListener 支持日志结构化。</li></ul></td></tr>
</table>


