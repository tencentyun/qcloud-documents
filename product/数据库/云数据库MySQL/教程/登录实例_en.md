## 1 Log in with the Command Line

1. Log in to [www.qcloud.com][1], go to the "Console", and click "Cloud Database" in "Cloud Services" module to enter the cloud database's "Management View" page.

![][image-1]

2. Obtain the "IP" and "Port Number" of the cloud database which you want to log in.

![][image-2]

3. Set the password for the cloud database. Click the "Initialize" button of the cloud database instance to initialize the settings.

![][image-3]

If you forget the cloud database password, you can reset it. For details, see [Reset Password][2].

4. Log in to the CVM, and use the following standard MySQL statement to log in to cloud database (the default account for the cloud database is "root").


```
mysql -h [Cloud Database IP] -P [Cloud Database Port Number] -uroot -p[Cloud Database Password]
```

> Note:
> You need to install MySQL client first. You can go to [\[MySQL official website to download and install]][3]
> Note: The first "-P" in the command line is uppercase and the second "-p" is lowercase.

Example:

![][image-4]

5. After logging in to the cloud database, you can execute the MySQL statement to manage the cloud database. For detailed MySQL statements, refer to [MySQL Manual][4].

Example:

![][image-5]

## 2 Log in with the Cloud Database Management Interface

1. Log in to [www.qcloud.com][5], go to the "Console", and click "Cloud Database" in "Cloud Services" module to enter the cloud database's "Management View" page.

![][image-6]

2. Set the password for the cloud database. Click the "Initialize" button of the cloud database instance to initialize the settings.

![][image-7]

If you forget the cloud database password, you can reset it. For details, see [Reset Password][6].

3. In the "List of Instances" page of the cloud database, find the cloud database instance which you want to log in, and click the "Login" button on the right.

![][image-8]

4. In the phpMyAdmin login interface, enter the correct cloud database password, and click "Execute" to enter the phpMyAdmin management interface.

![][image-9]

5. In the phpMyAdmin management interface, you can perform relevant operations to the database.

![][image-10]

[1]:	http://www.qcloud.com
[2]:	/doc/product/236/%E5%AF%86%E7%A0%81%E9%87%8D%E7%BD%AE
[3]:	https://dev.mysql.com/downloads/installer/
[4]:	http://dev.mysql.com/doc/
[5]:	http://www.qcloud.com
[6]:	/doc/product/236/%E5%AF%86%E7%A0%81%E9%87%8D%E7%BD%AE

[image-1]:	//mc.qcloudimg.com/static/img/313d5fd529bfe4898651efa2b3b08dc6/1.png
[image-2]:	//mc.qcloudimg.com/static/img/31d1ad4d65d8ada9ebcdc795fcc0ae22/2.png
[image-3]:	//mc.qcloudimg.com/static/img/7c1fe616342da0045d55abbd869e215b/3.png
[image-4]:	//mccdn.qcloud.com/img568127c27a3a6.png
[image-5]:	//mccdn.qcloud.com/img568127e32312e.png
[image-6]:	//mc.qcloudimg.com/static/img/313d5fd529bfe4898651efa2b3b08dc6/1.png
[image-7]:	//mc.qcloudimg.com/static/img/7c1fe616342da0045d55abbd869e215b/3.png%0A
[image-8]:	//mc.qcloudimg.com/static/img/3945a72eb332d620658e95f16da5fc91/6.png
[image-9]:	//mccdn.qcloud.com/img568128dbefa9b.png
[image-10]:	//mccdn.qcloud.com/img568128e2b6f6a.png

