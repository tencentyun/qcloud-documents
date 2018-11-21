CAM 用户为您在腾讯云中创建的一个实体，每一个 CAM 用户仅同一个腾讯云账户关联。您注册的腾讯云账号身份为**主账号**，您可以通过 [用户管理](https://console.cloud.tencent.com/cam) 来创建拥有不同权限的**子账号**协作您。子账号的类型分为 [子用户](https://cloud.tencent.com/document/product/598/13674)、[协作者](https://cloud.tencent.com/document/product/598/13666) 以及 [消息接收人](https://cloud.tencent.com/document/product/598/13667)。

<table>
	<tr>
		<th rowspan="2">账号类型</th>
		<th rowspan="2">主账号</th>
		<th colspan="3">子账号</th>
	</tr>
	<tr>
		<th>子用户</th>
		<th>协作者</th>
		<th>消息接收人</th>
	</tr>
	<tr>
		<td>定义</td>
		<td>
					<ul>
						<li>拥有腾讯云所有资源，可以任意访问其任何资源。</li>
						<li>不建议使用主账号对资源进行操作，应创建子账号并按照最小权重原则赋予策略，使用权限范围有限的子账号操作您的云资源。</li>
					</ul>
		</td>
		<td>由主账号创建，完全归属于创建该子用户的主账号。</td>
		<td>本身拥有主账号身份，被添加作为当前主账号的协作者，则为当前主账号的子账号之一，可切换回主账号身份。</td>
		<td>仅拥有消息接收功能。</td>
	</tr>
	<tr>
		<td>控制台访问</td>
		<td>✔</td>
		<td>✔</td>
		<td>✔</td>
		<td>	- </td>
	</tr>
	<tr>
		<td>编程访问</td>
		<td>✔</td>
		<td>✔</td>
		<td>✔</td>
		<td>	- </td>
	</tr>
	<tr>
		<td>策略授权</td>
		<td>默认已拥有全部策略</td>
		<td>✔</td>
		<td>✔</td>
		<td>	- </td>
	</tr>
	<tr>
		<td>消息通知</td>
		<td>✔</td>
		<td>✔</td>
		<td>✔</td>
		<td>✔</td>
	</tr>
</table>

