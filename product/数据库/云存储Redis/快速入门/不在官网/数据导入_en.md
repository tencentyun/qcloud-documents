## CRS Import Tool crs-port
### 1.	About crs-port
"crs-port" is a tool provided by Tencent Cloud Redis Store (CRS) for importing and exporting CRS instance data through command lines and offers the following features:
• Import RDB files into CRS instances
• Import self-build Redis on CVM to CRS through live migration
•Export RDB files from CRS instances (only master-slave CRS instances are supported)

### 2.	Downloading "crs-port" Tool
You can download "crs-port" tool (support 32-bit and 64-bit) by [clicking here](https://mc.qcloudimg.com/static/archive/e26011d06802eb8b968df8782b14e4f1/crs-port.tar.gz).
Updated On: March, 16, 2017

### 3.	Importing RDB files
Command:
``` crs-port restore -n 16 -i /data/dump.rdb -t 192.168.0.1:6379 -A pwd```
> Parameter Description
• -n [concurrent level] A value equaling 2 times to 4 times the total core count of CPU of the source Redis service is recommended.
• -i Specify the path where the file to be imported is located
• -t IP and port of the destination CRS instance to which the file will be imported
• -A URL password of the destination CRS instance

#### 3.1 Notes
• You need to clear the destination CRS instance before using the tool, otherwise an error will occur.
• You need to ensure that the machine time when the script is executed is correct, otherwise data inconsistencies may occur.



### 4.	dump RDB files
Command:
``` crs-port dump -n 16 -f 192.168.0.1:6379 -P pwd -o /data/dump.rdb```
> Parameter Description
• -n [concurrent level] A value equaling 2 times to 4 times the total core count of CPU is recommended.
• -f IP and port of source Redis service
• -P Password of source Redis service. If no password exists, this parameter can be left empty.
• -o Specify the output path of file.
(Only support master/slave CRS instances. Cluster instances are not supported.)

