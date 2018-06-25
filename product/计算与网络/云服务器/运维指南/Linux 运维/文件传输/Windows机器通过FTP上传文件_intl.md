You can use FTP channel to upload application from your own server to CVM.

## 1. Configure FTP service on CVM

1) Run the following commands as root to install Vsftp (take CentOS system as an example):

```
yum install vsftpd
```


2) Before starting the vsftpd service, you need to log into the CVM to modify configuration files to disable anonymous login.

Open the configuration file with the following command:

```
vim /etc/vsftpd/vsftpd.conf
```

Change  
```
anonymous_enable=YES (on the 11th line in the configuration file)
```
to

```
anonymous_enable=NO
```
to disable anonymous login.

3) Read the effective configuration.

```
cat /etc/vsftpd/vsftpd.conf |grep ^[^#] 
```
The following results will be returned:

```
local_enable=YES
write_enable=YES
local_umask=022
anon_upload_enable=YES
anon_mkdir_write_enable=YES
anon_umask=022
dirmessage_enable=YES
xferlog_enable=YES
connect_from_port_20=YES
xferlog_std_format=YES
listen=YES
pam_service_name=vsftpd
userlist_enable=YES
tcp_wrappers=YES
```

4) Start vsftpd service.

```
service vsftpd start
```

5) Set up an FTP user account.
Set up an FTP user account by running the following command:

```
useradd
```
For example, if the account is "ftpuser1", the directory is /home/ftpuser1, and login via ssh is not allowed:

```
useradd -m -d /home/ftpuser1 -s /sbin/nologin ftpuser1
```

And set a password for the account using the following command:

```
passwd
```
For example, setting the password for the above account as "ftpuser1":

```
passwd ftpuser1
```

After setting these up, you can log on to the FTP server using the account. 

6) Modify the pam configuration of vsftpd, so that users can connect to the CVM via the account and password they set by themselves.

Use the following command to modify the pam:

```
 vim /etc/pam.d/vsftpd
```

Modify to:

```
#%PAM-1.0 
auth required /lib64/security/pam_listfile.so item=user sense=deny file=/etc/ftpusers onerr=succeed 
auth required /lib64/security/pam_unix.so shadow nullok 
auth required /lib64/security/pam_shells.so 
account required /lib64/security/pam_unix.so 
session required /lib64/security/pam_unix.so 
```

Confirm whether the modified file is correct using the following command:

```
cat /etc/pam.d/vsftpd
```

Returned results are:

```
auth required /lib64/security/pam_listfile.so item=user sense=deny file=/etc/ftpusers onerr=succeed 
auth required /lib64/security/pam_unix.so shadow nullok 
auth required /lib64/security/pam_shells.so 
account required /lib64/security/pam_unix.so 
session required /lib64/security/pam_unix.so 
```

Restart the vsftpd service using the following command to make the modification effective:

```
service vsftpd restart
```

The results are:

```
Shutting down vsftpd:  [ OK ]
Starting vsftpd for vsftpd:  [ OK ]
```

## 2. Upload files to Linux CVM
1) Download and install open source software FileZilla
Please use FileZilla Ver. 3.5.1 or 3.5.2 (Using FileZilla Ver. 3.5.3 for FTP uploading will lead to problems).
Since FileZilla official site only provides the latest Ver.3.5.3 for download, you are recommended to search for download links for Ver.3.5.1 or 3.5.2 on your own. Recommended download link for Ver. 3.5.1: http://www.oldapps.com/filezilla.php?old_filezilla=6350

2) Connect to FTP
Run FileZilla, fill in setting form, and then click "Quick Links".


>Description of the settings:
- Host: Public network IP of CVM (Log in to [CVM Console](https://console.cloud.tencent.com/cvm) page to view the public network IP of CVM).
- User Name: ID of the FTP user account set in the previous step (here “ftpuser1” is used as example).
- Password: Password of the FTP user account set in the previous step (here “ftpuser1” is used as example).
- Port: FTP listener port, default is "21".

3) Upload files to Linux CCVM

When uploading a file, select the local file with the mouse and drag it to the remote site to upload it to Linux CVM.

>Note: CVM FTP path does not support automatic unzipping or deletion of uploaded tar zip files.

