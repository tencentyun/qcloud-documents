## CRS Import Tool crs-port
### About crs-port
"crs-port" is a tool provided by Tencent Cloud Redis Storage (CRS) for importing and exporting CRS instance data through command lines and offers the following features:
• You can only import/export RDB files from instances of Tencent CRS master/slave edition.
• You cannot import/export RDB files from cluster or new-generation CRS instances.

### Download "crs-port" tool
You can download "crs-port" tool (support 32-bit and 64-bit) by [clicking here](https://mc.qcloudimg.com/static/archive/e26011d06802eb8b968df8782b14e4f1/crs-port.tar.gz).
Updated On: March, 16, 2017

### Import RDB files
Command:
``` crs-port restore -n 16 -i /data/dump.rdb -t 192.168.0.1:6379 -A pwd```
Parameter description<br>
n [concurrent level]: A value equaling 2 times to 4 times the total core count of CPU is recommended. <br>
i: Specify the path where the file to be imported is located.<br>
t: IP and port of the destination CRS instance to which the file will be imported.<br>
A: URL password of the destination CRS instance.<br>
setdb=N: Specify a database to be imported to in the destination instance. The value range for N is [0,15]<br>
filterdb=N: Specify a database of which the data is to be imported to the destination instance. The value range for N is [0, 15]

#### Notes
The message " [ERROR] restore error: ERR Target key name is busy. for key: xxx" indicates that the key already exists in the database. This error can be solved as follows:
A. You need to clear the destination CRS instance before using the tool, otherwise an error will occur. You can clear the instance via the console.
B. Check if there is any other writing to the destination instance by checking the QPS after clearing the instance. Stop the writing.
It is necessary to ensure that the machine time when the script is executed is correct, otherwise data inconsistencies may occur.



### Dump RDB files
Command:
``` crs-port dump -n 16 -f 192.168.0.1:6379 -P pwd -o /data/dump.rdb```

Parameter description
n [concurrent level]: A value equaling 2 times to 4 times the total core count of CPU is recommended.
f: IP and port of source Redis service.
P: Password of source Redis service. If no password exists, this parameter can be left empty.
o: Specify the output path of file.
(Only support master/slave CRS instances. Cluster instances are not supported.)

