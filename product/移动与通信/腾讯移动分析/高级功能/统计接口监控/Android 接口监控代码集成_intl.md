#### Code Description
ctx: Device context of the page;
Objects monitored by monitor: API name, time taken for calling API, returned value type, error code, request packet size, response packet size, sampling rate and other information need to be set depending on the API to be monitored. For more information, please see the document under directory doc/api.
```java
void StatService.reportAppMonitorStat (
Context ctx, StatAppMonitor monitor)
<span style="font-family:'sans serif', tahoma, verdana, helvetica;font-size:14px;line-height:1.5;"><strong>Parameters:</strong></span><span style="font-family:'sans serif', tahoma, verdana, helvetica;font-size:14px;line-height:1.5;">  </span>
```
#### Where to call the method
Monitored API: StatAppMonitor method name list
<table style="width:740px;" cellpadding="2" cellspacing="0" border="1" bordercolor="#000000">
		<tbody>
			<tr>
				<td>
					<span style="font-size:14px;">API Name</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Description</span><br>
				</td>
			</tr>
			<tr>
				<td>
					<span style="font-size:14px;">setInterfaceName(String interfaceName)</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Set the API name to be monitored</span><br>
				</td>
			</tr>
			<tr>
				<td>
					<span style="font-size:14px;">setReqSize(long reqSize)</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Request packet size (in bytes)</span><br>
				</td>
			</tr>
			<tr>
				<td>
					<span style="font-size:14px;">setRespSize(long respSize)</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Response packet size (in bytes)</span><br>
				</td>
			</tr>
			<tr>
				<td>
					<span style="font-size:14px;">setResultType(int resultType)</span><br>
				</td>
				<td>
					<p>
						<span style="font-size:14px;">SUCCESS_RESULT_TYPE;</span> 
					</p>
					<p>
						<span style="font-size:14px;">FAILURE_RESULT_TYPE;</span> 
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
					<span style="font-size:14px;">Time taken for calling the API (in ms)</span><br>
				</td>
			</tr>
			<tr>
				<td>
					<span style="font-size:14px;">setReturnCode(int returnCode)</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Error code returned for the monitored API</span><br>
				</td>
			</tr>
			<tr>
				<td>
					<span style="font-size:14px;">setSampling(int sampling)</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Sampling rate: Default is 1, which means a sampling rate of 100%. Enter 2 for a sampling rate of 1/2, 4 for 1/4... and n for 1/n.</span><br>
				</td>
			</tr>
		</tbody>
</table>	

```java
// Create a monitoring API object
StatAppMonitor monitor = new StatAppMonitor("ping:www.qq.com");
String ip = "www.qq.com";
Runtime run = Runtime.getRuntime();
java.lang.Process proc = null;
try {
    String str = "ping -c 3 -i 0.2 -W 1 " + ip;
    long starttime = System.currentTimeMillis();
    // The API to be monitored
    proc = run.exec(str);
    proc.waitFor();
    long difftime = System.currentTimeMillis() - starttime;
    // Set the time taken for calling API
    monitor.setMillisecondsConsume(difftime);
    int retCode = proc.waitFor();
    // Set API's error code
    monitor.setReturnCode(retCode);
    // Set request packet size (if any)
    monitor.setReqSize(1000);
    // Set response packet size (if any)
    monitor.setRespSize(2000);
    // Set sampling rate
// Default is 1, which means 100%.
// Enter 2 (100/50) for 50%, 4 (100/25) for 25%, and so on.
monitor.setSampling(2);
    if (retCode == 0) {
        logger.debug("ping connection test is successful");
        // Flagged as successful
        monitor.setResultType(StatAppMonitor.SUCCESS_RESULT_TYPE);
    } else {
        logger.debug("ping connection test failed");
    // Flagged as logical failure, which may be caused by the reason such as unavailability of network.
// But it is not fatal to business and is tolerable
        monitor.setResultType(StatAppMonitor.LOGIC_FAILURE_RESULT_TYPE);
    }
} catch (Exception e) {
    logger.e(e);
    // An exception occurs while calling the API. It is fatal and is identified as a failure.
    monitor.setResultType(StatAppMonitor.FAILURE_RESULT_TYPE);
} finally {
    proc.destroy();
}
// Report the API monitoring data
StatService.reportAppMonitorStat(ctx, monitor);
```
