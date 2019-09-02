You can use CDB multi-thread import/export tool (cdb_mydumper) to quickly backup and recover instance data, owing to its functions similar to mysqldump.

## 1. Service Limits

- To ensure the security of instance data, you can only use this tool on a virtual machine that has permission to access the instance.

- You need to run this tool on a Linux CVM, and access the instance with correct username and password.

- During data export and import, you need to set relevant parameters according to tool instructions. A directory will be generated locally based on the export or import time by default, for example, export-20130926-185241.

## 2. Note
- Since cdb_mydumper exports data in a multi-thread way, the exported data may not be in the same order as those exported using mysqldump, and data inconsistencies may occur to some time-dependent characteristics (routine, event, etc.). Therefore, you are advised to export and import mysql database and other databases separately.

-  Since functions of database extraction and database merging provided by cdb_mydumper depend on delimiters, it is required that your database name exclude dots (.), and that the table name exclude minus signs (-).

## 3. Format of Exported Data
The exported data are in the format of binary sql files by default.

## 2. Installation and Deployment

### 2.1 Downloading the Tool
1. Download the CDB data import/export tool:
<table  style="width:650px">
	<thead>
		<tr>
			<th scope="col"><strong>Version</strong></th>
			<th scope="col" style="width: 100px;"><strong>Release Date</strong></th>
			<th scope="col" style="width: 300px;"><strong>Description</strong></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="text-align: center;"><a href="http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/cdb_mydumper_v1.0.0.tar.gz" target="_blank">cdb_mydumper_v1.0.0.tar.gz</a></td>
			<td style="text-align: center; width: 77px;">Oct 1, 2013</td>
			<td style="text-align: center; width: 236px;">Download link for CDB multi-thread data import/export tool 1.0.0</td>
		</tr>
	</tbody>
</table>
2. Save the tool to the local, then upload it to the CVM, and log in to the CVM (Linux CVM only) to decompress the toolkit.
The decompression process is as follows:
```
tar xzvf cdb_mydumper_v1.0.0.tar.gz
```

3. After the decompression, there will be a mydumper folder with two binary executable files. The files are described as follows:
mydumper: CDB multi-thread data export tool.
myloader: CDB multi-thread data import tool.
4. Run the tool directly on the CVM (Linux CVM only) without installation.

### 2.2 Command Description

Before using the tool to export data, you need to give the tool permission to execute files. The command is as follows:

```
$ chmod +x mydumper myloader
```

Run the following command:
```
$ ./mydumper -V
```

After that, the following text will appear on the screen:

Please check whether the tool version number printed below is the latest version number as provided in Section 2.1. If not, download the latest version.


```
mydumper 0.2.3-cdb-1.0.0, built against MySQL 5.1.54 
Compile Time: 01:55:13 Sep 19 2013
```

## 3. Instructions

### 3.1 Command Examples
1. Export the entire database 
$./mydumper -h 127.0.0.1 -P 20120 -u root -p 123 -G -R -E -l -A -o alldb 
2. Import the entire database
$./myloader -h 127.0.0.1 -P 20120 -u root -p 123 -d alldb 
3. Export multiple databases
$./mydumper -h 127.0.0.1 -P 20120 -u root -p 123 -G -R -E -l -B alarmDB,db_cms_logging,test -o dbs 
4. Import multiple databases
$./myloader -h 127.0.0.1 -P 20120 -u root -p 123 -d dbs 
5. Export a single database and multiple tables
$./mydumper -h 127.0.0.1 -P 20120 -u root -p 123 -G -R -E -l -B alarmDB -T alarm_history,alarm_strategy -o tbs 
6. Import a single database and multiple tables
$./myloader -h 127.0.0.1 -P 20120 -u root -p 123 -t 2 -d tbs 
7. Import an extracted database
$./myloader -h 127.0.0.1 -P 20120 -u root -p 123 -B alarmDB, db_cms_logging -d alldb 
8. Import an extracted table
$./myloader -h 127.0.0.1 -P 20120 -u root -p 123 -B alarmDB -T alarm_history,alarm_strategy -d dbs 
9. Import multiple databases to a single database (combining CVMs)
$./myloader -h 127.0.0.1 -P 20120 -u root -p 123 -A newdir -B alarmDB -T alarm_history,alarm_strategy -d dbs 

### 3.2 Description of Command Input Parameters

**mydumper**

<table style="width:800px">
	<thead>
		<tr>
			<th scope="col" style="width:160px"><strong>Name</strong></th>
			<th scope="col" style="width:33px"><strong>Required/Optional</strong></th>
			<th scope="col" style="width:60px"><strong>Type</strong></th>
			<th scope="col" style="width:300px"><strong>Description</strong></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="text-align:left; width:142px"><strong>-h,--host</strong></td>
			<td style="text-align:left; width:35px">Required</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">IP of instance to be dumped.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-p,--password</strong></td>
			<td style="text-align:left; width:35px">Required</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">Password of instance to be dumped.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-P,--port</strong></td>
			<td style="text-align:left; width:35px">Required</td>
			<td style="text-align:left; width:60px">int</td>
			<td style="text-align:left; width:242px">Port of instance to be dumped.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-S,--socket</strong></td>
			<td style="text-align:left; width:35px">Required</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">Socket information of local instance to be dumped. Choose one between it and -h -p -P.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-A,--all-databases</strong></td>
			<td style="text-align:left; width:35px">Optional</td>
			<td style="text-align:left; width:60px">int</td>
			<td style="text-align:left; width:242px">Dump all the databases.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-B,--databases</strong></td>
			<td style="text-align:left; width:35px">Optional</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">List of databases to be dumped. Databases should be separated by commas.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-T,--tables-list</strong></td>
			<td style="text-align:left; width:35px">Optional</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">List of data tables to be dumped. Data tables should be separated by commas.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-o,--outputdir</strong></td>
			<td style="text-align:left; width:35px">Optional</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">Output directory. Default value is ./export-&lt;datatime&gt;/.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-s,--statement-size</strong></td>
			<td style="text-align:left; width:35px">Optional</td>
			<td style="text-align:left; width:60px">int</td>
			<td style="text-align:left; width:242px">Bytes of generated insert statement. Default is 64K.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-i,--ignore-engines</strong></td>
			<td style="text-align:left; width:35px">Optional</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">Type of ignored storage engines. The engines should be separated by commas.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-m,--no-schemas</strong></td>
			<td style="text-align:left; width:35px">Optional</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">schema information of tables that are not dumped.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-G,--opt-triggers</strong></td>
			<td style="text-align:left; width:35px">Optional</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">trigger information of tables that need to be dumped.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-R,--opt-routines</strong></td>
			<td style="text-align:left; width:35px">Optional</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">routine information of databases that need to be dumped.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-E,--opt-events</strong></td>
			<td style="text-align:left; width:35px">Optional</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">Event information of databases that need to be dumped.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-n,--charset-name</strong></td>
			<td style="text-align:left; width:35px">Optional</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">Set the character set to be exported. Default is binary.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-l,--add-locks</strong></td>
			<td style="text-align:left; width:35px">Optional</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">Set whether to add "lock table" in front of the generated sql data file.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-t,--threads</strong></td>
			<td style="text-align:left; width:35px">Optional</td>
			<td style="text-align:left; width:60px">int</td>
			<td style="text-align:left; width:242px">Number of threads for concurrent export. <span style="color:#FF0000">The default is 6-thread export. You can adjust the value to increase export speed. The maximum value is 128.</span></td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-V,--version</strong></td>
			<td style="text-align:left; width:35px">Optional</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">Check version information.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-v,--verbose</strong></td>
			<td style="text-align:left; width:35px">Optional</td>
			<td style="text-align:left; width:60px">int</td>
			<td style="text-align:left; width:242px">Set log level, 0 = silent, 1 = errors, 2 = warnings, 3 = info. Default is 2.</td>
		</tr>
	</tbody>
</table>


**myloader**

<table  style="width:800px">
	<thead>
		<tr>
			<th scope="col" style="width:160px"><strong>Name</strong></th>
			<th scope="col" style="width: 33px;"><strong>Required/Optional</strong></th>
			<th scope="col" style="width:60px"><strong>Type</strong></th>
			<th scope="col" style="width:242px"><strong>Description</strong></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="text-align:left; width:142px"><strong>-d, --directory</strong></td>
			<td style="text-align: left; width: 33px;">Required</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">Directory of file to be imported.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-h,--host</strong></td>
			<td style="text-align: left; width: 33px;">Required</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">IP of instance to be imported.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-p,--password</strong></td>
			<td style="text-align: left; width: 33px;">Required</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">Directory of file to be imported.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-P,--port</strong></td>
			<td style="text-align: left; width: 33px;">Required</td>
			<td style="text-align:left; width:60px">int</td>
			<td style="text-align:left; width:242px">Port of instance to be imported.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-S,--socket</strong></td>
			<td style="text-align: left; width: 33px;">Required</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">Socket information of local instance to be imported. Choose one between it and -h -p -P.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-e,--enable-binlog</strong></td>
			<td style="text-align: left; width: 33px;">Required</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">binlog is recorded during data import. <span style="color:#FF0000">If this parameter is not specified, master and slave data will be inconsistent.</span></td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-A,--all-databases</strong></td>
			<td style="text-align: left; width: 33px;">Optional</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">Import to the same new database.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-B,--databases</strong></td>
			<td style="text-align: left; width: 33px;">Optional</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">Select the list of databases to be imported. Databases should be separated by commas.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-T,--tables-list</strong></td>
			<td style="text-align: left; width: 33px;">Optional</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">Select the list of data tables to be imported. Data tables should be separated by commas.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-W, --skip-views</strong></td>
			<td style="text-align: left; width: 33px;">Optional</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">Set not to import view.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-R, --skip-routines</strong></td>
			<td style="text-align: left; width: 33px;">Optional</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">Set not to import routine.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-E, --skip-events</strong></td>
			<td style="text-align: left; width: 33px;">Optional</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">Set not to import event.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-t,--threads</strong></td>
			<td style="text-align: left; width: 33px;">Optional</td>
			<td style="text-align:left; width:60px">int</td>
			<td style="text-align:left; width:242px">Number of threads for concurrent import. <span style="color:#FF0000">You can adjust the value to change the import speed. It is recommended to set the value within 4, with 2 as the best choice.</span></td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-V,--version</strong></td>
			<td style="text-align: left; width: 33px;">Optional</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">Check version information.</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-v,--verbose</strong></td>
			<td style="text-align: left; width: 33px;">Optional</td>
			<td style="text-align:left; width:60px">int</td>
			<td style="text-align:left; width:242px">Set log level, 0 = silent, 1 = errors, 2 = warnings, 3 = info. Default is 2.</td>
		</tr>
	</tbody>
</table>

### 3.4 Data Export Description

- Data export in progress

By default, no information is output during export. You can use -v <num> to set the log level to view the progress information

- Data export finished

By default, no information is output during export. When data export is finished, the process exits 

-  Data export error

If an error occurs during import or export, this tool will print out error message and error code consistent with those output by MySQL. You can view MySQL error codes for details.

-  Output file directory structure of exported data

Output file description:

<table>
	<thead>
		<tr>
			<th scope="col" style="width: 92px;"><strong>File Type</strong></th>
			<th scope="col" style="width: 145px;"><strong>Naming Rule</strong></th>
			<th scope="col" style="width: 131px;"><strong>Example</strong></th>
			<th scope="col" style="width: 104px;"><strong>Description</strong></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="width: 92px;">Exported header information file</td>
			<td style="width: 145px;">SaveDir/.metedata_begin</td>
			<td style="width: 131px;">alldb/.metadata_begin</td>
			<td style="width: 104px;">Text format, the same as output header of mysqldump.</td>
		</tr>
		<tr>
			<td style="width: 92px;">schema information file of exported database</td>
			<td style="width: 145px;">SaveDir/dbname-dbmyschema.sql</td>
			<td style="width: 131px;">alldb/mysql-dbmyschema.sql</td>
			<td style="width: 104px;">schema information of exported database</td>
		</tr>
		<tr>
			<td style="width: 92px;">routine information file of imported database</td>
			<td style="width: 145px;">SaveDir/dbname-dbmyroutine.sql</td>
			<td style="width: 131px;">alldb/mysql-dbmyroutine.sql</td>
			<td style="width: 104px;">routine information of imported database</td>
		</tr>
		<tr>
			<td style="width: 92px;">event information file of exported database</td>
			<td style="width: 145px;">SaveDir/dbname-dbmyevent.sql</td>
			<td style="width: 131px;">alldb/mysql-dbmyevent.sql</td>
			<td style="width: 104px;">event information of exported database</td>
		</tr>
		<tr>
			<td style="width: 92px;">view information file corresponding to exported database</td>
			<td style="width: 145px;">SaveDir/dbname-dbmyview.sql</td>
			<td style="width: 131px;">alldb/d_ip_lib.v_detail-dbmyview.sql</td>
			<td style="width: 104px;">schema information of the view corresponding to exported database</td>
		</tr>
		<tr>
			<td style="width: 92px;">schema information file of exported view</td>
			<td style="width: 145px;">SaveDir/dbname.tbname-myview.sql</td>
			<td style="width: 131px;">alldb/d_ip_lib.v _detail-myview.sql</td>
			<td style="width: 104px;">schema information of exported view</td>
		</tr>
		<tr>
			<td style="width: 92px;">schema information file of exported table</td>
			<td style="width: 145px;">SaveDir/dbname.tbname-myschema.sql</td>
			<td style="width: 131px;">alldb/d_ip_lib.t_svr-myschema.sql</td>
			<td style="width: 104px;">schema information of exported table</td>
		</tr>
		<tr>
			<td style="width: 92px;">Data file of exported table</td>
			<td style="width: 145px;">SaveDir/dbname.tbname-mytable.sql</td>
			<td style="width: 131px;">alldb/d_ip_lib.t_svr-mytable.sql</td>
			<td style="width: 104px;">Data information of exported table</td>
		</tr>
		<tr>
			<td style="width: 92px;">Exported tail information file</td>
			<td style="width: 145px;">SaveDir/.metedata_end</td>
			<td style="width: 131px;">alldb/.metadata_end</td>
			<td style="width: 104px;">Text format, the same as output tail of mysqldump.</td>
		</tr>
	</tbody>
</table>











