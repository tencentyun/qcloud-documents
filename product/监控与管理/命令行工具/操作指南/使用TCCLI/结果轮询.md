在使用产品的过程中，有些操作并不能即时完成，您可以使用结果轮询功能来不断查询操作是否完成。例如，在开启一台实例后，实例并不能立即进入 `RUNNING` 状态，则可使用结果轮询功能对实例状态轮询，直到出现 `RUNNING` 状态为止。

## 操作步骤
- 执行以下命令，程序将按照一定时间间隔对实例的状态进行轮询，直到实例的状态为 `RUNNING` 或者超时为止。
```bash
tccli cvm DescribeInstancesStatus --region ap-hongkong --waiter "{'expr':'InstanceStatusSet[0].InstanceState','to':'RUNNING'}"
```
- 您可自定义超时时间和睡眠时间，执行以下命令，设定超时时间为180秒，睡眠时间为5秒。
```bash
tccli cvm DescribeInstancesStatus --region ap-hongkong --waiter "{'expr':'InstanceStatusSet[0].InstanceState','to':'RUNNING','timeout':180,'interval':5}"
```
- 您可在配置文件中设置可选子参数的值。在 `default.configure` 文件中添加如下参数，设置系统超时时间为180s，睡眠时间为5s。
```
"waiter": {
		"interval": 5,
		"timeout": 180
	},
```

## 参数说明
 - **--region**：需替换为您实例所在的地域。
 - **--waiter**：后的参数需使用双引号包裹，且参数需为 JSON 格式。其中必选及可选参数如下表：
 <table>
 <tr>
 <th>参数</th> <th>是否必选</th> <th>说明</th>
 </tr>
 <tr>
	<td>expr</td>
	<td>是</td>
	<td>指定被查询的字段，请使用 <a href="http://jmespath.org/">jmespath</a> 查找被指定的字段的值。</td>
 </tr>
 <tr>
	<td>to</td>
	<td>是</td>
	<td>被轮询的字段的目标值。</td>
 </tr>
 <tr>
	<td>timeout</td>
	<td>否</td>
	<td>轮询的超时时间，单位：秒。</td>
 </tr>
 <tr>
	<td>interval</td>
	<td>否</td>
	<td>进程睡眠的时间，单位：秒。</td>
 </tr>
 </table>
