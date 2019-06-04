Support multi-languages access
To access HBase through multiple languages, you need to activate the shtrift service. Enter the directory HBase in the following way (the download address can be found in "Connection and Access", and you need to configure the cloud parameters), and then start as follows
```
bin/hbase-daemon.sh start thrift -p <port> --infoport <infoport>
```

