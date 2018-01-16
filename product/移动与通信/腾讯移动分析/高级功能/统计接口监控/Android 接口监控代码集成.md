#### 代码说明
ctx：页面的设备上下文；
monitor 监控对象：需要根据接口情况设置接口名称、耗时、返回值类型、返回码、请求包大小、响应包大小和采样率等信息，详见 doc/api 目录下的文档。
```java
void StatService.reportAppMonitorStat (
Context ctx, StatAppMonitor monitor)
<span style="font-family:'sans serif', tahoma, verdana, helvetica;font-size:14px;line-height:1.5;"><strong>参数：</strong></span><span style="font-family:'sans serif', tahoma, verdana, helvetica;font-size:14px;line-height:1.5;">  </span>
```
#### 调用位置
被监控的接口：StatAppMonitor 方法名列表
<table style="width:740px;" cellpadding="2" cellspacing="0" border="1" bordercolor="#000000">
		<tbody>
			<tr>
				<td>
					<span style="font-size:14px;">接口名</span><br>
				</td>
				<td>
					<span style="font-size:14px;">说明</span><br>
				</td>
			</tr>
			<tr>
				<td>
					<span style="font-size:14px;">setInterfaceName(String interfaceName)</span><br>
				</td>
				<td>
					<span style="font-size:14px;">设置监控的接口名称</span><br>
				</td>
			</tr>
			<tr>
				<td>
					<span style="font-size:14px;">setReqSize(long reqSize)</span><br>
				</td>
				<td>
					<span style="font-size:14px;">请求包大小，单位：byte</span><br>
				</td>
			</tr>
			<tr>
				<td>
					<span style="font-size:14px;">setRespSize(long respSize)</span><br>
				</td>
				<td>
					<span style="font-size:14px;">响应包大小，单位：byte</span><br>
				</td>
			</tr>
			<tr>
				<td>
					<span style="font-size:14px;">setResultType(int resultType)</span><br>
				</td>
				<td>
					<p>
						<span style="font-size:14px;">SUCCESS_RESULT_TYPE；</span> 
					</p>
					<p>
						<span style="font-size:14px;">FAILURE_RESULT_TYPE；</span> 
					</p>
					<p>
						<span style="font-size:14px;">LOGIC_FAILURE_RESULT_TYPE</span> 
					</p>

				</td>
			</tr>
			<tr>
				<td>
					<span style="font-size:14px;">setMillisecondsConsume(long millisecondsConsume)</span><br>
				</td>
				<td>
					<span style="font-size:14px;">调用耗时，单位：毫秒（ms）</span><br>
				</td>
			</tr>
			<tr>
				<td>
					<span style="font-size:14px;">setReturnCode(int returnCode)</span><br>
				</td>
				<td>
					<span style="font-size:14px;">监控接口业务返回码</span><br>
				</td>
			</tr>
			<tr>
				<td>
					<span style="font-size:14px;">setSampling(int sampling)</span><br>
				</td>
				<td>
					<span style="font-size:14px;">采样率： 默认为 1，表示 100%，如果是 1/2，则填 2，如果是 1/4，则填 4，若是 1/n，则填 n</span><br>
				</td>
			</tr>
		</tbody>
</table>	

```java
// 新建监控接口对象
StatAppMonitor monitor = new StatAppMonitor("ping:www.qq.com");
String ip = "www.qq.com";
Runtime run = Runtime.getRuntime();
java.lang.Process proc = null;
try {
    String str = "ping -c 3 -i 0.2 -W 1 " + ip;
    long starttime = System.currentTimeMillis();
    // 被监控的接口
    proc = run.exec(str);
    proc.waitFor();
    long difftime = System.currentTimeMillis() - starttime;
    // 设置接口耗时
    monitor.setMillisecondsConsume(difftime);
    int retCode = proc.waitFor();
    // 设置接口返回码
    monitor.setReturnCode(retCode);
    // 设置请求包大小，若有的话
    monitor.setReqSize(1000);
    // 设置响应包大小，若有的话
    monitor.setRespSize(2000);
    // 设置抽样率
// 默认为1，表示100%。
// 如果是50%，则填2(100/50)，如果是25%，则填4(100/25)，以此类推。
monitor.setSampling(2);
    if (retCode == 0) {
        logger.debug("ping连接成功");
        // 标记为成功
        monitor.setResultType(StatAppMonitor.SUCCESS_RESULT_TYPE);
    } else {
        logger.debug("ping测试失败");
    // 标记为逻辑失败，可能由网络未连接等原因引起的
// 但对于业务来说不是致命的，是可容忍的
        monitor.setResultType(StatAppMonitor.LOGIC_FAILURE_RESULT_TYPE);
    }
} catch (Exception e) {
    logger.e(e);
    // 接口调用出现异常，致命的，标识为失败
    monitor.setResultType(StatAppMonitor.FAILURE_RESULT_TYPE);
} finally {
    proc.destroy();
}
// 上报接口监控
StatService.reportAppMonitorStat(ctx, monitor);
```