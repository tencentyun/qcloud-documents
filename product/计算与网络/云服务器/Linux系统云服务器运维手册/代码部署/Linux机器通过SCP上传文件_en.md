Linux machine can upload files to Linux CVM with the following commands:

```
scp local file address  CVM login name@CVM public network IP/domain name  CVM file location
```

For example, upload local file "/home/lnmp0.4.tar.gz" to the directory for the CentOS CVM with IP of 129.20.0.2:

```
scp /home/Inmp0.4.tar.gz root@129.20.0.2 /home/Inmp0.4.tar.gz
```

Press "Enter" and type in login password to complete the upload.