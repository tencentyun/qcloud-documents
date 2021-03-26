## Loglistener版本变更

本文档为您介绍日志服务 Loglistener 的版本更新记录。

>? 多行-完全正则模式采集需升级至 Loglistener 2.4.5版本，建议您前往安装 [最新版本](https://cloud.tencent.com/document/product/614/17414)。
>

<table>
	<tr><th>版本号</th><th>变更类型</th><th>描述</th></tr>
	<tr><td><b>v2.5.3</b></td><td>Bugfix</td><td>修复线程不安全的 mempool 引发的 double free，segment fault 问题。</td></tr>
	<tr><td rowspan=2><b>v2.5.2</b></td><td>新功能</td><td>支持解析失败日志上传需求。</td></tr>
	<tr><td>Bugfix</td><td>修复黑名单 bug，当黑名单配置为 FILE 模式，且指定文件名中带通配字符时，无法有效过滤掉对应文件。</td></tr>
	<tr><td><b>v2.5.1</b></td><td>体验优化</td><td>去掉找不到 pos 文件时的初始化 offset 为当前文件大小的逻辑。</td></tr>
	<tr><td><b>v2.5.0</b></td><td>新功能</td><td><ul  style="margin: 0;"><li>支持 Loglistener 自动升级。</li><li>支持在 Ubuntu 系统下，Loglistener 自启动。</li></ul></td></tr>
	<tr><td><b>v2.4.6</b></td><td>Bugfix</td><td><ul  style="margin: 0;"><li>修复变更采集配置时，_metadata_cache 数据残留问题。</li><li>修复变更采集配置时，_indexReaderMap、_indexReaderQueueMap、_symlinkMap、_needWatchRealPath 等内存配置容器中的数据残留问题。</li><li>修复处理软链接的 IN_DELETE 事件时，直接将 realpath 从 _needWatchRealPath 中移除，可能导致的其它指向此 realpath 的软链接无法采集的问题。</li><li>修复文件软连接和目录软连接同时配置，Loglistener 会 core 的问题。</li></ul></td></tr>
	<tr><td><b>v2.4.5</b></td><td>新功能</td><td>新增 multiline_fullregex_log 日志采集类型支持。</td></tr>
	<tr><td><b>v2.4.4</b></td><td>Bugfix</td><td>修复没有初始化 msec 导致的日志采集使用日志时间不准的问题。</td></tr>
	<tr><td><b>v2.4.3</b></td><td>新功能</td><td>自动检测日志格式（logFormat）。</td></tr>
	<tr><td><b>v2.4.2</b></td><td>Bugfix</td><td>修复拉取配置时，不过滤 metadata 导致内存占用过大的问题。</td></tr>
	<tr><td rowspan=2><b>v2.4.1</b></td><td>新功能</td><td>支持毫秒采集</td></tr>
	<tr><td>Bugfix</td><td>修复用户日志没有 \n 会卡住的问题。</td></tr>
	<tr><td><b>v2.4.0</td><td>新功能</td><td>Loglistener 进程级别监控。</td></tr>
	<tr><td rowspan=2><b>v2.3.9</b></td><td>新功能</td><td>支持采集路径配置黑名单。</td></tr>
	<tr><td>Bugfix</td><td>修复 boost 版本库过低导致的内存泄漏。</td></tr>
	<tr><td><b>v2.3.8</b></td><td>新功能</td><td>支持多路径采集。</td></tr>
	<tr><td><b>v2.3.6</b></td><td>Bugfix</td><td><ul  style="margin: 0;"><li>修复 key invalid 导致进不去资源回收分支导致不采集。</li><li>修复 server 请求失败返回502导致内存泄漏。</li></ul></td></tr>
	<tr><td rowspan=2><b>v2.3.5</b></td><td>新功能</td><td>支持日志上下文检索功能。</td></tr>
	<tr><td>Bugfix</td><td><ul  style="margin: 0;"><li>修复静态配置文件，在上传日志时返回鉴权失败时后续不再采集的问题。</li><li>修复在动态配置文件情况下，内存超限，不再读取动态配置的问题。</li><li>修复在日志滚动时，如果生产日志速度过大，偶现重复采集的问题。</li><li>修复在日志上传多次重试失败时导致的内存泄漏的问题。</li></ul></td></tr>
	<tr><td><b>v2.3.1</b></td><td>Bugfix</td><td><ul  style="margin: 0;"><li>内存限制修改（原先的限制为只限制一个具体值，当内存超过该具体值时，会出现无限增长的情况）。</li><li>添加到内存限制时，进行快速GC的逻辑（到达内存限制时，超过3s的请求判定为超时，正常为120s）</li></ul></td></tr>
	<tr><td rowspan=2><b>v2.2.6</b></td><td>新功能</td><td>支持内外网分离。</td></tr>
	<tr><td>Bugfix</td><td>修复 getip 的 bug:ip 重复。</td></tr>
	<tr><td rowspan=2><b>v2.2.5</b></td><td>新功能</td><td>支持织云部署。</td></tr>
	<tr><td>Bugfix</td><td>修复 getip 的 bug: 导致 core。</td></tr>
	<tr><td><b>v2.2.4</b></td><td>体验优化</td><td><ul  style="margin: 0;"><li>安装和初始化改为：tools/loglistener.sh 的子命令 install 和 init。</li><li>启动改成：/etc/init.d/loglistenerd start|stop|restart。</li><li>编译方式改为：CMakeLists.txt。</li></ul></td></tr>
	<tr><td><b>v2.2.3</b></td><td>体验优化</td><td>日志轮转 rename+create 不丢日志。</td></tr>
	<tr><td><b>v2.2.2</b></td><td>体验优化</td><td>日志超过512K自动截断。</td></tr>
	<tr><td><b>Earlier versions</b></td><td>-</td><td><ul  style="margin: 0;"><li>2.2.2版本的 LogListener 支持完全正则采集。</li><li>2.1.4版本的 LogListener 支持多行全文格式。</li><li>2.1.1版本的 LogListener 支持日志结构化。</li><li>2.0.0版本的 LogListener 更新时需要停止较低版本的 LogListener，然后重新下载安装最新版本。</li></ul></td></tr>
</table>


