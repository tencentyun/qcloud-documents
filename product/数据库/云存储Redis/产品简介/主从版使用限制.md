
### 1. 主从版暂不支持命令
script 组命令存在安全风险，不予开放
<table>
	<tbody>
			<tr>
			<th><strong>Server（服务器）</strong></th>
			<th><strong>Script（脚本）</strong></th>
		</tr>
		<tr>
			<td>FLUSHALL</td>
			<td>EVAL</td>
		</tr>	
		<tr>
			<td>FLUSHDB</td>
			<td>EVALSHA</td>
		</tr>	
		<tr>
			<td>BGREWRITEAOF</td>
			<td>SCRIPT EXISTS</td>
		</tr>	
		<tr>
			<td>BGSAVE</td>
			<td>SCRIPT FLUSH</td>
		</tr>	
		<tr>
			<td>CLIENT KILL</td>
			<td>SCRIPT KILL</td>
		</tr>	
		<tr>
			<td>CLIENT LIST</td>
			<td>SCRIPT LOAD</td>
		</tr>	
		<tr>
			<td>CLIENT GETNAME</td>
						<td>&nbsp;</td>
		</tr>	
		<tr>
			<td>CLIENT SETNAME</td>
						<td>&nbsp;</td>
		</tr>	
		<tr>
			<td>CONFIG GET</td>
						<td>&nbsp;</td>
		</tr>			
		<tr>
			<td>CONFIG SET</td>
						<td>&nbsp;</td>
		</tr>		
		<tr>
			<td>CONFIG RESETSTAT</td>
						<td>&nbsp;</td>
		</tr>
		<tr>
			<td>COMMAND</td>
						<td>&nbsp;</td>
		</tr>
		<tr>
			<td>COMMAND COUNT</td>
						<td>&nbsp;</td>
		</tr>
		<tr>
			<td>COMMAND GETKEYS</td>
						<td>&nbsp;</td>
		</tr>
		<tr>
			<td>COMMAND INFO</td>
						<td>&nbsp;</td>
		</tr>
		<tr>
			<td>DEBUG OBJECT</td>
						<td>&nbsp;</td>
		</tr>
		<tr>
			<td>DEBUG SEGFAULT</td>
						<td>&nbsp;</td>
		</tr>
		<tr>
			<td>LASTSAVE</td>
						<td>&nbsp;</td>
		</tr>
		<tr>
			<td>MONITOR</td>
						<td>&nbsp;</td>
		</tr>
		<tr>
			<td>ROLE</td>
						<td>&nbsp;</td>
		</tr>
		<tr>
			<td>SAVE</td>
						<td>&nbsp;</td>
		</tr>
		<tr>
			<td>SHUTDOWN</td>
						<td>&nbsp;</td>
		</tr>
		<tr>
			<td>SLAVEOF</td>
						<td>&nbsp;</td>
		</tr>
		<tr>
			<td>MIGRATE</td>
						<td>&nbsp;</td>
		</tr>
		<tr>
			<td>SYNC</td>
						<td>&nbsp;</td>
		</tr>
		<tr>
			<td>PSYNC</td>
						<td>&nbsp;</td>
		</tr>
	</tbody>
</table>

### 2. 容量型主从版使用限制

容量型主从版暂不支持命令

|server 族|scripting 族|keys 族|lists 族|connection 族|
|---|---|---|-----|----|
|bgrewriteaof	|eval	|touch|	blpop|	swapdb|
|bgsave	|evalsha|	restore|	brpop	|　
|client kill|	script debug|	object|	brpoplpush|	　
|client list|	script exists|	unlink	|　	|　
|client getname	|script flush	|wait	||　	　
|client pause|	script kill|	migrate	　|  |   |
|client reply|	script load|	dump	|  |　
|client setname	|　|  | 	　	　	|  |
|command count	|　|	| |　	　	　
|command getkeys| |	　|  |	　	　	　
|command info	|　	|    |  |　	　	　
|config get	|　	  |   |    |   |
|config rewrite	|　	|   |    |　	　	　
|config set	|　	|    |    |　	　	　
|config resetstat|	　|    |    |	　	　	　
|debug object	|　	|   |    |　	　	　
|debug segfault	|　|   |   |	　	　	　
|flushall|	　	|    |    |　	　	　
|flushdb|	　	 |     |       |　	　	　
|lastsave|	　	|       |        |　	　	　
|monitor|	　	   |        |          |　	　	　
|role	|　	|     |       |         	　	　
|save|	　	|      |        |        　	　	　
|shutdown|	　	|        |       |　	　	　
|slaveof|	　	　	|         |        |　	　
|slowlog|	　	　	|        |      |　	　
|sync	|        |       |       |      |    |

