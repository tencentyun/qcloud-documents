Active users = Devices on which App was kept open or was opened at frontend in the statistical period.
For plug-ins, H5 Apps and Mini Programs, only if a page within App was opened in the statistical period can the device is counted as active.
For security, music, FM or tool Apps (such as IME), devices on which the App was kept running at backend are also counted as active users.

### Basic Apps
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
					<span style="font-size:14px;">Scenario Description</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Typical Cases</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Active</span><br>
				</td>
			</tr>
			<tr>
				<td rowspan="8">
					<span style="font-size:14px;">Connected to a network <br>(such as 2G, 3G, 4G, WiFi)</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Auto-start at backend</span><br>
				</td>
				<td>
					<span style="font-size:14px;">This is common on Android phones. The App keeps running at backend after the phone is powered on.</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Many Android Apps are started automatically upon the power-on of phone, unless auto-start is disabled by user.</span><br>
				</td>
				<td>
					<span style="font-size:14px;">×</span><br>
				</td>
			</tr>
			<tr>
			
				<td>
					<span style="font-size:14px;">Cold start</span><br>
				</td>
				<td>
					<span style="font-size:14px;">No process for the App exists at backend. The system creates a new process to allocate to the App.</span><br>
				</td>
				<td>
					<span style="font-size:14px;">The App process does not exist at backend because it has just been installed, or has been killed by the system or manually. <br>===Later===><br>The App is reopened from the phone's desktop, or after user receives a notification, or via voice assistant or control center.</span><br>
				</td>
				<td>
					<span style="font-size:14px;">√</span><br>
				</td>
			</tr>
			<tr>
			
				<td>
					<span style="font-size:14px;">Warm start</span><br>
				</td>
				<td>
					<span style="font-size:14px;">An opened App is interrupted by an operation and then is reopened (via assivetouch or the Back key).</span><br>
				</td>
				<td>
					<span style="font-size:14px;">App1 is running on the device.<br>===Later==><br>User is redirected to App2 via Home key, assitivetouch, **Back**/**Forward**, push message or **Share** (For example, a user who is watching Tencent Video wants to share a video to WeChat's "Moments").</span><br>
				</td>
				<td>
					<span style="font-size:14px;">√</span><br>
				</td>
			</tr>
			<tr>
				
				<td>
					<span style="font-size:14px;">Visible at frontend</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Regardless whether or not an operation has been performed on the App</span><br>
				</td>
				<td>
					<span style="font-size:14px;">App is opened, and there is no screen lock, page switch or switch to backend.</span><br>
				</td>
				<td>
					<span style="font-size:14px;">√</span><br>
				</td>
			</tr>
			<tr>
				
				<td>
					<span style="font-size:14px;">Resident in backend</span><br>
				</td>
				<td>
					<span style="font-size:14px;">App is invisible at frontend but keeps running at backend. When receiving a notification, user didn't take any action.</span><br>
				</td>
				<td>
					<span style="font-size:14px;">User stays on the phone's desktop or is using App1, with App2 running at backend<br>===Later==><br>When receiving a notification from App2, (for example, receiving a campaign notification from Tmall when browsing WeChat pages), the user didn't open App2.</span><br>
				</td>
				<td>
					<span style="font-size:14px;">×</span><br>
				</td>
			</tr>
			<tr>
				
				<td>
					<span style="font-size:14px;">Resident in backend</span><br>
				</td>
				<td>
					<span style="font-size:14px;">App is invisible at frontend but keeps running at backend. When receiving a notification, the user clicked the notification to open the App.</span><br>
				</td>
				<td>
					<span style="font-size:14px;">User stays on the phone's desktop or is using App1, with App2 running at backend<br>===Later==><br>When receiving a notification from App2, (for example, receiving a campaign notification from Tmall when browsing WeChat pages), the user opened App2.</span><br>
				</td>
				<td>
					<span style="font-size:14px;">√</span><br>
				</td>
			</tr>
			<tr>
				
				<td>
					<span style="font-size:14px;">Redirect from the original App to another App (plug-in/H5 App/Mini Program)</span><br>
				</td>
				<td>
					<span style="font-size:14px;">For any redirect to a plug-in/H5 App/Mini Program, only if the user opened the App page can it be counted as active user. </span><br>
				</td>
				<td>
					<span style="font-size:14px;">This can be considered as clicks or exposures. Some business operators that only count clicks as active users (such as Tencent News) keep track of exposures as well.</span><br>
				</td>
				<td>
					<span style="font-size:14px;">√</span><br>
				</td>
			</tr>
			<tr>
			   <td>
					<span style="font-size:14px;">Crash</span><br>
				</td>
				<td>
					<span style="font-size:14px;">App crashed when running at frontend</span><br>
				</td>
				<td>
					<span style="font-size:14px;"><br></span><br>
				</td>
				<td>
					<span style="font-size:14px;">√</span><br>
				</td>
			</tr>
			<tr>
			   <td rowspan="2">
					<span style="font-size:14px;">Network is down</span><br>
				</td>
				<td>
					<span style="font-size:14px;">Visible at frontend</span><br>
				</td>
				<td>
					<span style="font-size:14px;">If the network was down and was not restored until the next day, the user is counted as active for the day when the network failure occurred.</span><br>
				</td>
				<td>
					<span style="font-size:14px;">For example, if the network was down at 11:55 and was restored at 0:15 the next day, the user is counted as active for the previous day.</span><br>
				</td>
				<td>
					<span style="font-size:14px;">√</span><br>
				</td>
			</tr>
			<tr>
			   <td>
					<span style="font-size:14px;">Resident in the backend and invisible at frontend</span><br>
				</td>
				<td>
					<span style="font-size:14px;"><br></span><br>
				</td>
				<td>
					<span style="font-size:14px;"><br></span><br>
				</td>
				<td>
					<span style="font-size:14px;">×</span><br>
				</td>
			</tr>
		</tbody>
</table>	

### Special Apps

Special Apps, such as security/music/FM/tool (IME or weather forecast) Apps are resident in the backend because of their business characteristics Users of such Apps are counted as active whether the Apps run at frontend or backend. Users of map Apps are counted as active only for the statistical period.  

| Network Status | App Type | Scenario | Typical Cases | Active |
|---------|---------|---------|---------|---------|
| Connected to a network or network is down | Security/music/FM Apps, and some tool Apps (IME, file backup) | Running at either frontend or backend | Amap was used in the afternoon on May 16 and kept running at backend and never switched to frontend on May 17. | The user is counted as daily active user for both May 16 and May 17. <br> |
| Connected to a network or network is down | Subway navigation | The App was kept open or was opened at frontend in the statistical period | Amap was used in the afternoon on May 16 and kept running at backend and never switched to frontend on May 17. | The user is counted as daily active user for May 16 only. <br> |






