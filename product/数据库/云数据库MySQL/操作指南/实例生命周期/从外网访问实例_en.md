If your CVM and cloud database are deployed in the same region, you do not need to apply for public IP. If they are deployed in different regions or in a system other than Tencent Cloud, it is necessary to enable public IP to connect CDB MySQL database. This document describes how to enable public network access address and provides a login example.

## Enabling Public Network Access Address

1. Log in to the [Cloud Database Console](https://console.cloud.tencent.com/cdb/), find the instance to be modified in the instance list, and click "Management" in the Operation column.
![](https://mc.qcloudimg.com/static/img/067a823712584842fc983ab34fa79b55/step1.png)
2. Find the "Public IP" in the instance information and click "Enable".
![](https://mc.qcloudimg.com/static/img/320b345a398b918c1d3a103c3accdef7/step2.png)
3. After you click "OK", the process of enabling public network starts.
![](https://mc.qcloudimg.com/static/img/676fad059f9dc83ac7faac68ae5531cc/step3.png)
![](https://mc.qcloudimg.com/static/img/d5511d9493fa18ccd52e8f41934f513e/step4.png)
4. When the public network is enabled successfully, it can be found in the basic information.
![](https://mc.qcloudimg.com/static/img/bb8a03a752acf0e3ca59f3009d911eb0/step5.png)
5. Public network access permission can be disabled with the switch. The access address is reclaimed and allocated again when enabled next time.
![](https://mc.qcloudimg.com/static/img/5dbd6ccaac4f2a893fbbbac871072eea/step6.png)

## Login Example

1.  Use the following standard MySQL statement to log in to the cloud database on a server that is connected to the network and installed with MySQL client. The cloud database account can be any one of those in the "Account Management".
```
mysql -h [Public IP of Cloud Database] -P [Port Number of Cloud Database] -u [Cloud Database Account] -p [Cloud Database Password]
```
>**Note:**
Note: The first "-P" in the command line is uppercase and the second "-p" is lowercase.</blockquote>
Example:
![](https://mc.qcloudimg.com/static/img/59c193b46229a88338bcd51cadad9aaf/step7.png)
2.  After logging in to the cloud database, you can execute the MySQL statement to manage the cloud database. For more information about MySQL statement, please see [MySQL Documentation](http://dev.mysql.com/doc/).
Example:
![](https://mc.qcloudimg.com/static/img/ab2e159d88201f6bf29cee91611a9864/step8.png)

