If your CVM and cloud database are deployed in the same region, there is no need to apply for public network address. If you want to connect to the CDB MySQL database on a system in different region or on a system other than Tencent Cloud, this document describes how to enable the public network access address and offers login example.

## Enabling Public Network Access Address

1. Go to the management console, find the instance to be modified in the instance list. Click "Management" in the Operation column:

![](//mccdn.qcloud.com/img56825925da077.png)

2. In the "Public Network Address" in the instance information and click "Enable":

![](//mccdn.qcloud.com/img5682595c5d4e7.png)

3. Set the password for the public network access account, which should be a combination of 8-16 characters comprised of at least two of the following types: letters, numbers, special characters (!, @, #, $, %, ^, *, ()). The public network access account is assigned by the system by default, so it cannot be modified currently:

![](//mccdn.qcloud.com/img56825964bf4e6.png)

4. After the password is entered, the enabling process of public network starts:

![](//mccdn.qcloud.com/img5682596b1222d.png)

5. When the public network is enabled successfully, its access address as well as access account ID and password will be displayed, and the relevant information will be sent via internal message:

![](//mccdn.qcloud.com/img568259720d52d.png)

![](//mccdn.qcloud.com/img5682597c603ca.png)


6. Public network access permission can be disabled with the switch. The access address will be reclaimed and allocated again when enabled next time.

![](//mccdn.qcloud.com/img5682598beba65.png)

## Login Example

1. Log in to the CVM, and use the following standard MySQL statement to log in to cloud database (the default account for the cloud database is "root").


```
mysql -h [Public Network Address of Cloud Database] -P [Port Number of Cloud Database] -uroot -p[Cloud Database Password]
```

> Note: The first "-P" in the command line is uppercase and the second "-p" is lowercase.

Example:

![](//mccdn.qcloud.com/static/img/1ad43e0d40701c303fc00b8853cb4d3e/image.png)

5. After logging in to the cloud database, you can execute the MySQL statement to manage the cloud database. For more information about MySQL statement, refer to [MySQL Documentation](http://dev.mysql.com/doc/).

Example:

![](//mccdn.qcloud.com/static/img/751ff4b57b51b21bf687bff6487a69a4/image.png)
