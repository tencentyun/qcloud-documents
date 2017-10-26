用户可以使用云数据库多线程导入导出工具(cdb_mydumper)，完成和mysqldump类似的功能，用来快速备份和恢复实例数据。

## 1. 使用限制

- 为了保证实例数据的安全性，只能在有权限访问该实例的虚拟机上使用本工具。

- 本工具需要在Linux云服务器上运行，并使用正确的用户名和密码访问实例。

- 在执行数据导出导入时，需要按工具的使用说明设置好相关的参数，默认会在本地按时间生成目录，如export-20130926-185241 。

## 2. 注意事项
- 由于cdb_mydumper采用多线程导出，所以无法保证导出顺序和使用mysqldump一致，可能会给某些依赖时间的特性（routine，event等）带来数据不一致，建议用户把mysql库和其他数据库分开导出导入。

-  由于cdb_mydumper提供的库提取和库合并功能依赖于分割符，所以要求用户数据库名不包含点号（.） ,表名不包含减号（-）。

## 3. 导出数据格式说明
导出的数据格式默认是binary格式的sql文件。

## 2 安装部署

### 2.1 下载工具

1.下载云数据库数据导入导出工具：

<table  style="width:650px">
	<thead>
		<tr>
			<th scope="col"><strong>版本</strong></th>
			<th scope="col" style="width: 100px;"><strong>发布日期</strong></th>
			<th scope="col" style="width: 300px;"><strong>说明</strong></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="text-align: center;"><a href="http://qzonestyle.gtimg.cn/qzone/vas/opensns/res/doc/cdb_mydumper_v1.0.0.tar.gz" target="_blank">cdb_mydumper_v1.0.0.tar.gz</a></td>
			<td style="text-align: center; width: 77px;">2013-10-01</td>
			<td style="text-align: center; width: 236px;">云数据库数据多线程导入导出工具1.0.0版本下载链接。</td>
		</tr>
	</tbody>
</table>

2.将该工具保存到本地后，上传到云服务器，然后登录云服务器（仅限Linux服务器）对工具包进行解压。

解压过程如下：

```
tar xzvf cdb_mydumper_v1.0.0.tar.gz
```

3.解压后，会出现mydumper文件夹，里面有2个二进制执行文件。文件说明如下：

mydumper：云数据库数据多线程导出工具。
myloader：云数据库数据多线程导入工具。

4.此工具无需安装，直接在云服务器（仅限Linux服务器）上运行即可。

### 2.2 命令说明

在使用工具导出数据之前，先赋予文件执行权限，命令如下：

```
$ chmod +x mydumper myloader
```

执行如下命令：
```
$ ./mydumper –V
```

运行以上命令后，屏幕上打印出如下文字：

注意将下面打印出的工具版本号与2.1节中给出的工具最新版本做对比，如果不一致，则请下载最新的工具。


```
mydumper 0.2.3-cdb-1.0.0, built against MySQL 5.1.54 
Compile Time: 01:55:13 Sep 19 2013
```

## 3. 使用说明

### 3.1 命令示例
1. 导出整个库 
$./mydumper -h 127.0.0.1 –P 20120 –u root -p 123 -G -R -E -l -A -o alldb 
2. 导入整个库
$./myloader -h 127.0.0.1 –P 20120 –u root -p 123 -d alldb 
3. 导出多个库
$./mydumper -h 127.0.0.1 –P 20120 –u root -p 123 -G -R -E -l -B alarmDB,db_cms_logging,test -o dbs 
4. 导入多个库
$./myloader -h 127.0.0.1 –P 20120 –u root -p 123 -d dbs 
5. 导出单库多表
$./mydumper -h 127.0.0.1 –P 20120 –u root -p 123 -G -R -E -l -B alarmDB -T alarm_history,alarm_strategy -o tbs 
6. 导入单库多表
$./myloader -h 127.0.0.1 –P 20120 –u root -p 123 –t 2 -d tbs 
7. 提取库导入
$./myloader -h 127.0.0.1 –P 20120 –u root -p 123 -B alarmDB, db_cms_logging -d alldb 
8. 提取表导入
$./myloader -h 127.0.0.1 –P 20120 –u root -p 123 -B alarmDB -T alarm_history,alarm_strategy -d dbs 
9. 多库导入单库（合服）
$./myloader -h 127.0.0.1 –P 20120 –u root -p 123 -A newdir -B alarmDB -T alarm_history,alarm_strategy -d dbs 

### 3.2 命令输入参数说明

**mydumper**

<table style="width:800px">
	<thead>
		<tr>
			<th scope="col" style="width:160px"><strong>名称</strong></th>
			<th scope="col" style="width:33px"><strong>可选</strong></th>
			<th scope="col" style="width:60px"><strong>类型</strong></th>
			<th scope="col" style="width:300px"><strong>说明</strong></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="text-align:left; width:142px"><strong>-h,--host</strong></td>
			<td style="text-align:left; width:35px">必选</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">dump的实例ip。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-p,--password</strong></td>
			<td style="text-align:left; width:35px">必选</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">dump的实例密码。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-P,--port</strong></td>
			<td style="text-align:left; width:35px">必选</td>
			<td style="text-align:left; width:60px">int</td>
			<td style="text-align:left; width:242px">dump的实例端口。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-S,--socket</strong></td>
			<td style="text-align:left; width:35px">必选</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">本地dump的实例套接字信息，和-h -p -P二者选一。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-A,--all-databases</strong></td>
			<td style="text-align:left; width:35px">可选</td>
			<td style="text-align:left; width:60px">int</td>
			<td style="text-align:left; width:242px">dump所有的数据库。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-B,--databases</strong></td>
			<td style="text-align:left; width:35px">可选</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">dump数据库列表，用逗号隔开。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-T,--tables-list</strong></td>
			<td style="text-align:left; width:35px">可选</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">dump数据表列表，用逗号隔开。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-o,--outputdir</strong></td>
			<td style="text-align:left; width:35px">可选</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">输出目录，缺省值是./export-&lt;datatime&gt;/。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-s,--statement-size</strong></td>
			<td style="text-align:left; width:35px">可选</td>
			<td style="text-align:left; width:60px">int</td>
			<td style="text-align:left; width:242px">生成的insert语句的字节数，缺省是64K。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-i,--ignore-engines</strong></td>
			<td style="text-align:left; width:35px">可选</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">忽略的存储引擎类型，用逗号隔开。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-m,--no-schemas</strong></td>
			<td style="text-align:left; width:35px">可选</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">不dump表的schema信息。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-G,--opt-triggers</strong></td>
			<td style="text-align:left; width:35px">可选</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">需要dump表的trigger信息。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-R,--opt-routines</strong></td>
			<td style="text-align:left; width:35px">可选</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">需要dump数据库的routine信息。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-E,--opt-events</strong></td>
			<td style="text-align:left; width:35px">可选</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">需要dump数据库的event信息。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-n,--charset-name</strong></td>
			<td style="text-align:left; width:35px">可选</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">设置导出的字符集，缺省是binary。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-l,--add-locks</strong></td>
			<td style="text-align:left; width:35px">可选</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">设置是否在生成的sql数据文件前面加上lock table。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-t,--threads</strong></td>
			<td style="text-align:left; width:35px">可选</td>
			<td style="text-align:left; width:60px">int</td>
			<td style="text-align:left; width:242px">并发导出线程的数目。<span style="color:#FF0000">默认6线程导出，用户可以调整该值来提高导出速度，最多可设置为128线程导出。</span></td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-V,--version</strong></td>
			<td style="text-align:left; width:35px">可选</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">查看版本信息。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-v,--verbose</strong></td>
			<td style="text-align:left; width:35px">可选</td>
			<td style="text-align:left; width:60px">int</td>
			<td style="text-align:left; width:242px">设置日志级别0=silent,1=errors,2=warnings,3=info,缺省是2。</td>
		</tr>
	</tbody>
</table>


**myloader**

<table  style="width:800px">
	<thead>
		<tr>
			<th scope="col" style="width:160px"><strong>名称</strong></th>
			<th scope="col" style="width: 33px;"><strong>可选</strong></th>
			<th scope="col" style="width:60px"><strong>类型</strong></th>
			<th scope="col" style="width:242px"><strong>说明</strong></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="text-align:left; width:142px"><strong>-d, --directory</strong></td>
			<td style="text-align: left; width: 33px;">必选</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">导入的文件目录。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-h,--host</strong></td>
			<td style="text-align: left; width: 33px;">必选</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">导入的实例ip。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-p,--password</strong></td>
			<td style="text-align: left; width: 33px;">必选</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">导入的文件目录。。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-P,--port</strong></td>
			<td style="text-align: left; width: 33px;">必选</td>
			<td style="text-align:left; width:60px">int</td>
			<td style="text-align:left; width:242px">导入的实例端口。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-S,--socket</strong></td>
			<td style="text-align: left; width: 33px;">必选</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">本地导入的实例套接字信息，和-h -p -P二者选一。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-e,--enable-binlog</strong></td>
			<td style="text-align: left; width: 33px;">必选</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">导入数据的时候记录binlog，<span style="color:#FF0000">如未指定此参数，会造成主从数据不一致。</span></td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-A,--all-databases</strong></td>
			<td style="text-align: left; width: 33px;">可选</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">导入到同一个新的数据库。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-B,--databases</strong></td>
			<td style="text-align: left; width: 33px;">可选</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">选择导入的数据库列表，用逗号隔开。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-T,--tables-list</strong></td>
			<td style="text-align: left; width: 33px;">可选</td>
			<td style="text-align:left; width:60px">string</td>
			<td style="text-align:left; width:242px">选择导入数据表列表，用逗号隔开。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-W, --skip-views</strong></td>
			<td style="text-align: left; width: 33px;">可选</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">设置不需要导入view。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-R, --skip-routines</strong></td>
			<td style="text-align: left; width: 33px;">可选</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">设置不需要导入routine。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-E, --skip-events</strong></td>
			<td style="text-align: left; width: 33px;">可选</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">设置不需要导入event。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-t,--threads</strong></td>
			<td style="text-align: left; width: 33px;">可选</td>
			<td style="text-align:left; width:60px">int</td>
			<td style="text-align:left; width:242px">并发导入线程的数目。<span style="color:#FF0000">用户可通过调整该值来调整导入速度，建议设置为4线程以内导入，最好设置为2线程导入。</span></td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-V,--version</strong></td>
			<td style="text-align: left; width: 33px;">可选</td>
			<td style="text-align:left; width:60px">none</td>
			<td style="text-align:left; width:242px">查看版本信息。</td>
		</tr>
		<tr>
			<td style="text-align:left; width:142px"><strong>-v,--verbose</strong></td>
			<td style="text-align: left; width: 33px;">可选</td>
			<td style="text-align:left; width:60px">int</td>
			<td style="text-align:left; width:242px">设置日志级别0=silent,1=errors,2=warnings,3=info,缺省是2。</td>
		</tr>
	</tbody>
</table>

### 3.4 导出数据说明

- 导出数据中

默认条件下，导出过程不输出任何信息，可以使用-v <num> 来设置日志级别，看到进度信息

- 导出数据完成

默认条件下，导出过程不输出任何信息，完成后进程退出 

-  导出数据出错

若导入导出过程中出错，此工具会打印出和MySQL错误输出一致的错误信息和错误码，具体可以查看MySQL的错误码

-  导出数据的输出文件目录结构

输出文件说明：

<table>
	<thead>
		<tr>
			<th scope="col" style="width: 92px;"><strong>文件类型</strong></th>
			<th scope="col" style="width: 145px;"><strong>命名规则</strong></th>
			<th scope="col" style="width: 131px;"><strong>示例</strong></th>
			<th scope="col" style="width: 104px;"><strong>说明</strong></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td style="width: 92px;">导出的头信息文件</td>
			<td style="width: 145px;">SaveDir/.metedata_begin</td>
			<td style="width: 131px;">alldb/.metadata_begin</td>
			<td style="width: 104px;">文本格式，保持和mysqldump的输出首部相同。</td>
		</tr>
		<tr>
			<td style="width: 92px;">导出的库schema信息文件</td>
			<td style="width: 145px;">SaveDir/dbname-dbmyschema.sql</td>
			<td style="width: 131px;">alldb/mysql-dbmyschema.sql</td>
			<td style="width: 104px;">导出的库schema信息。</td>
		</tr>
		<tr>
			<td style="width: 92px;">导入的库routine信息文件</td>
			<td style="width: 145px;">SaveDir/dbname-dbmyroutine.sql</td>
			<td style="width: 131px;">alldb/mysql-dbmyroutine.sql</td>
			<td style="width: 104px;">导入的库routine信息。</td>
		</tr>
		<tr>
			<td style="width: 92px;">导出的库event信息文件</td>
			<td style="width: 145px;">SaveDir/dbname-dbmyevent.sql</td>
			<td style="width: 131px;">alldb/mysql-dbmyevent.sql</td>
			<td style="width: 104px;">导出的库event信息。</td>
		</tr>
		<tr>
			<td style="width: 92px;">导出的库对应的view信息文件</td>
			<td style="width: 145px;">SaveDir/dbname-dbmyview.sql</td>
			<td style="width: 131px;">alldb/d_ip_lib.v_detail-dbmyview.sql</td>
			<td style="width: 104px;">导出的库对应的view的schema信息。</td>
		</tr>
		<tr>
			<td style="width: 92px;">导出的view的schema信息文件</td>
			<td style="width: 145px;">SaveDir/dbname.tbname-myview.sql</td>
			<td style="width: 131px;">alldb/d_ip_lib.v _detail-myview.sql</td>
			<td style="width: 104px;">导出的view的schema信息。</td>
		</tr>
		<tr>
			<td style="width: 92px;">导出的表的schema信息文件</td>
			<td style="width: 145px;">SaveDir/dbname.tbname-myschema.sql</td>
			<td style="width: 131px;">alldb/d_ip_lib.t_svr-myschema.sql</td>
			<td style="width: 104px;">导出的表的schema信息。</td>
		</tr>
		<tr>
			<td style="width: 92px;">导出的表的数据文件</td>
			<td style="width: 145px;">SaveDir/dbname.tbname-mytable.sql</td>
			<td style="width: 131px;">alldb/d_ip_lib.t_svr-mytable.sql</td>
			<td style="width: 104px;">导出的表的数据信息。</td>
		</tr>
		<tr>
			<td style="width: 92px;">导出的尾信息文件</td>
			<td style="width: 145px;">SaveDir/.metedata_end</td>
			<td style="width: 131px;">alldb/.metadata_end</td>
			<td style="width: 104px;">文本格式，保持和mysqldump的输出尾部相同。</td>
		</tr>
	</tbody>
</table>










