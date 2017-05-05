## CRS Import Tool: crs-port
### 1.	About crs-port
"crs-port" is a tool provided by Tencent Cloud Redis Storage (CRS) for importing and exporting CRS instance data through command lines and offers the following features:
• Import RDB files into CRS instances
• Import self-build Redis on CVM to CRS through live migration
•Export RDB files from CRS instances (only standalone CRS instances are supported)

### 2.	Downloading "crs-port" Tool
To download crs-port-32 tool (32 bit), [click here](https://mccdn.qcloud.com/static/archive/c01d0ebc17d6e379368978c3ad4d9bb3/crs-port-32.tar.gz) 
To download crs-port-64 tool (64 bit), [click here](https://mccdn.qcloud.com/static/archive/38e0786878ca1d1917e4e67a1855bed6/crs-port-64.tar.gz) 
Released on: May 30, 2016

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

### 4.	Hot Migration
Command:
```crs-port sync -n 16 -f 127.0.0.1:6379 -P pwd -t 192.168.0.1:6379 -A pwd```
> Parameter Description
• -n [concurrent level] A value equaling 2 times to 4 times the total core count of CPU of the source Redis service is recommended.
• -f IP and port of source Redis service
• -P Password of source Redis service. If no password exists, this parameter can be left empty.
• -t IP and port of the destination CRS instance to which the file will be imported
• -A URL password of the destination CRS instance

#### 4.1 Important Considerations
• The tool will synchronize RDB files first, then perform incremental synchronization
• You need to clear the destination CRS instance before using the tool, otherwise an error will occur
• Set the slave outbuffer parameter for the source Redis service:
config set client-output-buffer-limit "slave 4295000768 4295000768 0"
You may configure this parameter based on actual conditions to prevent disconnection between master and slave
• The synchronization progress in the command line output log refers to the synchronization progress of RDB files
• Any inconsistency of number of keys between source/destination after synchronization is caused by expiration time. Expired keys will not be synchronized

### 5.	dump RDB files
Command:
``` crs-port dump -n 16 -f 192.168.0.1:6379 -P pwd -o /data/dump.rdb```
> Parameter Description
• -n [concurrent level] A value equaling 2 times to 4 times the total core count of CPU is recommended.
• -f IP and port of source Redis service
• -P Password of source Redis service. If no password exists, this parameter can be left empty.
• -o Specify the output path of file.

