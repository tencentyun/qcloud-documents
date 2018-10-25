### Basic Descriptions
**Metric Definition**
Duration per use refers to the time period from entering the App frontend to leaving the frontend (one page is opened in one screen by default).
**Update cycle**
The usage duration data are updated the next day, namely, the data generated in the previous day are updated on a daily basis.

### Detailed Rules
**Usage duration**
The usage duration starts to be calculated after the App is opened and the usage duration is greater than 0 second. If the App is closed by users or runs in the backend for over 30 seconds, the App can be regarded as terminated.

**Average duration per use**
Average duration per use = Usage duration/Launch count

**Per capita usage duration**
Per capita usage duration = Visit duration/active users

### Analysis Scenarios
**Basic Apps**
<table>
		<tbody>
			<tr>
				<td>
					<span style="font-size:14px;">Network Status</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Scenario</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Scenario Segmentation and Description</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Typical Cases</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Usage Duration</span><br>
				</td>
			</tr>
			<tr>
				<td rowspan="6">
					<span style="font-size:14px;">No matter whether Internet is available</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Visible at frontend</span><br>
				</td>
				<td>
					<span style="font-size:14px;">App is opened (even if there is no subsequent operation) and is not interrupted (the screen is not locked and it is not redirected to other App pages).</span><br>
				</td>
				<td>
					<span style="font-size:14px;">The App is in use from 14:05 to 14:38.</span><br>
				</td>
				<td>
					<span style="font-size:14px;">33 minutes</span><br>
				</td>
			</tr>
			<tr>
			
				<td>
					<span style="font-size:14px;">Redirect from the original App to another App (plugins/H5/Mini Programs) and keep using the new App.</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Redirect to plugins/H5/Mini Programs. If only the entry is opened, it will not be regarded as a redirection; only if the page level is reached, it can be regarded as a redirection.</span><br>
				</td>
				<td>
					<span style="font-size:14px;">14:05: Use +D19:D25 WeChat.<br>14:06: Enter into Tencent News Plugin.<br>14:08: View some news till 14:15, and the WeChat frontend exits.</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Tencent News Plugin: 14:08-14:15 7 minutes;<br>WeChat: 14:05-14:15 10 minutes.</span><br>
				</td>
			</tr>
			<tr>
			
				<td>
					<span style="font-size:14px;">Redirect from the original App to another App (plugins/H5/Mini Programs), and then return to the original App.</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Redirect to plugins/H5/Mini Programs. If only the entry is opened, it will not be regarded as a redirection; only if the page level is reached, it can be regarded as a redirection.</span><br>
				</td>
				<td>
					<span style="font-size:14px;">14:05: Watching Tencent videos.<br>14:06: Edit messages of WeChat's "Moments".<br>14:08: Complete editing and sharing. <br>14:08 Go back to view Tencent videos. 15:30:</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Tencent Video: 14:05-14:06 1 minute<br>14:08-15:30 82 minutes 83 minutes in total<br>WeChat: 14:06-14:08 2 minutes</span><br>
				</td>
			</tr>
			<tr>
				
				<td>
					<span style="font-size:14px;">The screen is locked during usage</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Manually or automatically</span><br>
				</td>
				<td>
					<span style="font-size:14px;">14:05: Wait for WeChat messages but get no reply.<br>14:06: Automatically lock the screen.<br>14:11: Unlock the screen.</span><br>
				</td>
				<td>
					<span style="font-size:14px;">WeChat: 14:05-14:06 1 minute</span><br>
				</td>
			</tr>
			<tr>
				
				<td>
					<span style="font-size:14px;">Get interrupted</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Answer calls, send and receive text messages and view notifications<br> (viewing notifications cannot be monitored by MTA).</span><br>
				</td>
				<td>
					<span style="font-size:14px;">14:05: Using WeChat.<br>14:06: Answer a call.<br>14:20: End the call and return to WeChat to continue chatting.<br>14:30: Enter Tmall via a friend's message.</span><br>
				</td>
				<td>
					<span style="font-size:14px;">WeChat: 14:05-14:06 1 minute<br>14:20-14:30 10 minutes<br>11 minutes in total</span><br>
				</td>
			</tr>
			<tr>
				
				<td>
					<span style="font-size:14px;">Crash</span><br>
				</td>
				<td>
					<span style="font-size:14px;"><br></span><br>
				</td>
				<td>
					<span style="font-size:14px;">14:05: Play Arena of Valor.<br>14:15: Flashback occurs due to too many processes in the backend and too frequent operations.<br>14:15: Terminate some processes running in the backend.<br>14:17: Open and play Arena of Valor till 14:30.</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Arena of Valor: 14:05-14:15 10 minutes<br>14:17-14:30 13 minutes<br>23 minutes in total</span><br>
				</td>
			</tr>
			<tr>
				<td rowspan="3">
					<span style="font-size:14px;">Network is down</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Network is down</span><br>
				</td>
				<td>
					<span style="font-size:14px;"><br></span><br>
				</td>
				<td>
					<span style="font-size:14px;">14:05: Browsing Taobao.<br>14:15: The network is down due to weak signals.<br>14:16: Internet is available and browse Taobao for shopping till 14:30, then play WeChat.</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Taobao: 14:05-14:15 10 minutes<br>14:16-14:30 14 minutes<br>24 minutes in total</span><br>
				</td>
			</tr>
			<tr>
			   <td>
					<span style="font-size:14px;">No matter whether Internet is available</span><br>
				</td>
				<td>
					<span style="font-size:14px;">After the network is down, the App keeps running at the frontend and does not exit, and the screen is not locked.</span><br>
				</td>
				<td>
					<span style="font-size:14px;">14:05: Watching Tencent videos.<br>14:06: Get informed that the mobile traffic is used, then break the network.<br>14:38: Find and watch a locally cached video till the App exited the frontend or 14:05: Playing Craz3 Match. <br>14:06: Suddenly the Power is off and the Internet is unavailable, and the game goes into the offline mode.<br>14:38: Stop playing and have a call.</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Tencent Video: 14:05-14:38 33 minutes<br>Craz3 Match: 14:05-14:38 33 minutes</span><br>
				</td>
			</tr>
			<tr>		
				<td>
					<span style="font-size:14px;">No matter whether Internet is available</span><br>
				</td>
				<td>
					<span style="font-size:14px;">App exits the frontend after the network is down.</span><br>
				</td>
				<td>
					<span style="font-size:14px;"><br></span><br>
				</td>
				<td>
					<span style="font-size:14px;">Do not calculate time.</span><br>
				</td>
			</tr>
		</tbody>
</table>

**Special Apps**
The business characteristics of special Apps determine that some types of Apps have to reside in the backend all the time, such as map, security, music, FM and tool Apps (IME or weather forecast), and the time spent both in frontend and backend will be counted into the usage duration.

| Network Status | Scenario | Scenario Segmentation and Description | Typical Cases | Usage Duration |
|---------|---------|---------|---------|---------|
| Connected to network or network is down | Keep running at the frontend or backend | Map, security, music, FM and tool Apps (IME or weather forecast) | 14:05: Open Amap and navigate home.<br>14:06: Exit the frontend of Amap and open WeChat for chatting.<br>14:08 Lock the screen manually.<br>14:38 Terminate the map process running at backend. | Amap: 33 minutes (Unless terminated, processes running at backend are counted)<br>WeChat: 14:00-14:08 2 minutes |
| Connected to network or network is down | The App had been running at frontend. | Metro navigation Apps | 14:05: Open Amap and navigate home.<br>14:06: Exit the frontend of Amap and open WeChat for chatting.<br>14:08: Lock the screen manually.<br>14:38 Terminate the map process running at backend. | √ |
