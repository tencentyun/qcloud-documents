Users can use the rollback tool to roll back a database or table on Tencent Cloud platform. Based on cold backup and binlog, the tool can be used to roll back data in real time.

The CDB rollback tool can roll back the cloud database or table to the specified time with regular images and real-time flow reconstruction, and ensure that all data have the same time slice. During the rollback, the access to the original database or table is not affected,and a new database or table will be generated. After the rollback is finished, the user can see the original database or table, as well as the new database or table.

> Note: Cloud database will not change any user data. The data damage due to personal cause can be repaired through rollback.

## 1. Permission Control

In order to ensure the security of data in the database or table, the tool will authenticate a request.

### 1.1 Service Limits

**Environment limit**  

This tool can only run on a CVM.

**Data limit**

Only data within 3 days can be rolled back.

**Requests limit**

As data rollback is a resource-consuming service, the number of requests that can be made by an application is limited. After a rollback command is initiated, the system will verify the maximum number of requests of the application. If the rollback is not allowed, please contact us and submit a ticket.

## 2. Tool Instructions

### 2.1 Installation Instructions

1.Download the CDB rollback tool:
<table  style="width:600px">
	<thead>
		<tr>
			<th scope="col"><strong>Version</strong></th>
			<th scope="col" style="width: 100px;"><strong>Release Date</strong></th>
			<th scope="col" style="width:300px;"><strong>Description</strong></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td><a href="http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/CdbRollbackTools_x64_v1.1.0.zip" target="_blank">CdbRollbackTools_x64_v1.1.0.zip</a></td>
			<td style="width: 65px;">April 18, 2013</td>
			<td style="width: 216px;">Rollback of a single database and a single table is supported. (For Guangzhou)</td>
		</tr>
		<tr>
			<td><a href="http://share.weiyun.com/64bd19fd2182ccbead0facc47383b998" target="_blank">CdbRollbackTools.zip</a></td>
			<td style="width: 65px;">Jan 20, 2015</td>
			<td style="width: 216px;">Rollback of a single database and a single table is supported. (For Shanghai)</td>
		</tr>
	</tbody>
</table>

2.Save the tool to the local, then upload it to the CVM, and decompress the toolkit.
The decompression process is as follows:
```
unzip CdbRollbackTools_x64_v1.1.0.zip
```
3.After the decompression, there will be a binary executable file. The file is described as follows:
CdbRollbackTools: Cloud Database rollback tool.
4.Run the tool directly on the CVM (Linux CVM only) without installation. 

### 2.2 Command Description

**1. View the tool helper to get tool command description**

```
$ ./CdbRollbackTools -h
```

**2. View tool version**

```
$ ./CdbRollbackTools -v
```

**3. Execute database rollback**

```
$ ./CdbRollbackTools start appid instanceName dbName destdbName rollbackPoint user passwd strategy token
```

**4. Execute table rollback**

```
$ ./CdbRollbackTools start appid instanceName dbName tableName destTableName rollbackPoint user passwd strategy token
```

### 2.3 Executing Rollback Task

**1. Command Example**
```
$ ./CdbRollbackTools start 125000000 16_test_2011_10_31 rb_database rb_table rb_dest_table_1 201209251650 user passwd full e827a9de-06f0-11e2-81d1-781dbace8354
```
**2. Input Parameter Description**
<table style="width:700px">
	<thead>
		<tr>
			<th scope="col" style="width: 130px;"><strong>Name</strong></th>
			<th scope="col" style="width:450px;"><strong>Description</strong></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="width: 92px;">start</td>
			<td style="width: 395px;">Command type. It means initiating a rollback task.</td>
		</tr>
		<tr>
			<td style="width: 92px;">appid</td>
			<td style="width: 395px;">Cloud service account of the application for rollback, beginning with 125 (it can be queried on the overview page). The machine using the rollback tool must be under this account.</td>
		</tr>
		<tr>
			<td style="width: 92px;">instanceName</td>
			<td style="width: 395px;">Name of instance to be rolled back. It must be under the appid.</td>
		</tr>
		<tr>
			<td style="width: 92px;">dbName</td>
			<td style="width: 395px;">Name of database to be rolled back. It must be under the instanceName.</td>
		</tr>
		<tr>
			<td style="width: 92px;">tableName</td>
			<td style="width: 395px;">Name of table to be rolled back. It must be under the dbName.</td>
		</tr>
		<tr>
			<td style="width: 92px;">destdbName</td>
			<td style="width: 395px;"><span style="color:#FF0000">Name of the destination database, which cannot exist. </span>A new database with this name will be created under the instanceName. The rolled back data will be in this database.</td>
		</tr>
		<tr>
			<td style="width: 92px;">destTableName</td>
			<td style="width: 395px;"><span style="color:#FF0000">Name of the destination table, which cannot exist. </span>A new table with this name will be created under the dbName. The rolled back data will be in this table.</td>
		</tr>
		<tr>
			<td style="width: 92px;">rollbackPoint</td>
			<td style="width: 395px;">Time to which the data need to be rolled back. It must be in such a format as 201209251650, meaning September 25, 2012, 16:50.</td>
		</tr>
		<tr>
			<td style="width: 92px;">user</td>
			<td style="width: 395px;">Username of dbName.</td>
		</tr>
		<tr>
			<td style="width: 92px;">passwd</td>
			<td style="width: 395px;">Password of dbName. <span style="color:#FF0000">If the password contains special symbols such as $ and *, you need to include the password in single quotation marks, for example &#39;cdb$123*CDB&#39;.</span></td>
		</tr>
		<tr>
			<td style="width: 92px;">strategy</td>
			<td style="width: 395px;">Rollback types:
			<p><span style="color:#FF0000">db: Roll back images and flows of dbName database. It is suitable for sql operations within the same database.</span><br />
			full: Roll back all images and flows. It is suitable for all types of sql operations, but is less efficient.</p>
			</td>
		</tr>
		<tr>
			<td style="width: 92px;">token</td>
			<td style="width: 395px;">Key for rollback. Please enter: <span style="color:#FF0000">rollback-tencent-cloud-token</span>.
			<p>If the rollback is not allowed, please contact us and <a href="https://console.cloud.tencent.com/workorder/category" target="_blank">submit a ticket</a>.</p>
			</td>
		</tr>
	</tbody>
</table>


**3.Execution Results**  

If the command execution succeeds, the tool will output the following results:

```
start ok, appId:125000000 instName:16_test_2011_10_31 dbName:rb_database tableName:rb_table timePoint:201209251650 destTableName:rb_dest_table_1
```

If the command execution fails, the tool will output the following results:

```
execute failed:cdb rollback internal error
```

**4.Error Code Description**

<table style="width:500px">
	<thead>
		<tr>
			<th scope="col" style="width: 95px;"><strong>Error Code</strong></th>
			<th scope="col" style="width: 400px;"><strong>Description</strong></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="text-align: center; width: 87px;">0</td>
			<td style="text-align: center; width: 400px;">Task is initiated successfully</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 87px;">-1</td>
			<td style="text-align: center; width: 400px;">Task is received and is in queue</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 87px;">-50</td>
			<td style="text-align: center; width: 400px;">Cloud database internal error</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 87px;">-51</td>
			<td style="text-align: center; width: 400px;">Cloud database is under maintenance</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 87px;">-100</td>
			<td style="text-align: center; width: 400px;">Permission error. Please check whether the downloaded tool has execution permission</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 87px;">-110</td>
			<td style="text-align: center; width: 400px;">token does not exist</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 87px;">-111</td>
			<td style="text-align: center; width: 400px;">token has been used</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 87px;">-120</td>
			<td style="text-align: center; width: 400px;">Incorrect timepoint format</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 87px;">-121</td>
			<td style="text-align: center; width: 400px;">timepoint is too early</td>
		</tr>
		<tr>
			<td style="text-align: center; width: 87px;">-122</td>
			<td style="text-align: center; width: 400px;">timepoint is too late</td>
		</tr>
	</tbody>
</table>


### 2.4 Querying Rollback Progress

**1. Command Example**

```
$ ./CdbRollbackTools query 125000000
```

**2. Input Parameter Description**

<table  style="width:800px">
	<thead>
		<tr>
			<th scope="col" style="width: 69px;"><strong>Name</strong></th>
			<th scope="col" style="width:500px;">Description</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="width: 69px; text-align: center;">query</td>
			<td style="width: 417px; text-align: center;">Command type. It means querying a rollback task.</td>
		</tr>
		<tr>
			<td style="width: 69px; text-align: center;">app_id</td>
			<td style="width: 417px; text-align: center;">Cloud service account of the application for query, beginning with 125 (it can be queried on the overview page). The query command will make all the rollback tasks under the app_id listed.</td>
		</tr>
	</tbody>
</table>

**3. Execution Results** 

If the command execution succeeds, the tool will output the following results:

```
appId:125000000 instName:16_test_2011_10_31 dbName:rb_database tableName:rb_table rollbackPoint:201209251650 NewTableName:rb_dest_table_1 strategy:full stat:100% createTime:2012-9-25 17:11:5
```

If the command execution fails, the tool will output the following results:

```
execute failed:cdb rollback internal error
```

**4. Output Parameter Description**

<table  style="width:500px">
	<thead>
		<tr>
			<th scope="col" style="width: 167px;"><strong>Name</strong></th>
			<th scope="col" style="width: 320px;"><strong>Description</strong></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="width: 167px; text-align: center;">appId</td>
			<td style="width: 320px; text-align: center;">Cloud service account for rollback</td>
		</tr>
		<tr>
			<td style="width: 167px; text-align: center;">instName</td>
			<td style="width: 320px; text-align: center;">Name of instance to be rolled back</td>
		</tr>
		<tr>
			<td style="width: 167px; text-align: center;">dbName</td>
			<td style="width: 320px; text-align: center;">Name of database to be rolled back</td>
		</tr>
		<tr>
			<td style="width: 167px; text-align: center;">tableName</td>
			<td style="width: 320px; text-align: center;">Name of table to be rolled back</td>
		</tr>
		<tr>
			<td style="width: 167px; text-align: center;">newdbName</td>
			<td style="width: 320px; text-align: center;">Destination database name for rollback</td>
		</tr>
		<tr>
			<td style="width: 167px; text-align: center;">newTableName</td>
			<td style="width: 320px; text-align: center;">Destination table name for rollback</td>
		</tr>
		<tr>
			<td style="width: 167px; text-align: center;">rollbackPoint</td>
			<td style="width: 320px; text-align: center;">Rollback timepoint</td>
		</tr>
		<tr>
			<td style="width: 167px; text-align: center;">strategy</td>
			<td style="width: 320px; text-align: center;">Strategy selected for rollback</td>
		</tr>
		<tr>
			<td style="width: 167px; text-align: center;">stat</td>
			<td style="width: 320px; text-align: center;">Status of rollback task:
			<p>100%: Task completed<br />
			0% - 99%: Task in progress<br />
			Failed: Task failed</p>
			</td>
		</tr>
		<tr>
			<td style="width: 167px; text-align: center;">createTime</td>
			<td style="width: 320px; text-align: center;">Task initiation time</td>
		</tr>
	</tbody>
</table>

