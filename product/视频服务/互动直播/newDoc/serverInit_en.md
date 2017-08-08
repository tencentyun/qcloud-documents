# FreeShow Server QuickStart

## 1. Code Deployment

### 1.1 Establish PHP and Database Environment

#### Server Environment Requirement 

* Linux OS
* PHP >= 5.4
* MySQL >= 5.5.3

### 1.2 Modify Configuration

* [Code Download](https://github.com/zhaoyang21cn/SuiXinBoPHPServer/tree/StandaloneAuth). Deploy code into php directory.
* Enter the database URL, username and password of MySQL in lib/db/DBConfig.php.
* Change server/account/AccountLoginCmd.php into your ILVB SDKAPPPID.

```php
	const SDKAPPID = '1400019352';
```

* Modify the following code in service/service/Server.php into your log path.

```php
	$handler = new FileLogHandler('/data/log/sxb/sxb_' . date('Y-m-d') . '.log');
```

* Modify deps/bin/tls_licence_tools to have execution permission in order to generate userSig.
* Modify permission for deps/sig directory to allow other users to read from and write to this directory (chmod 757 deps/sig). This is used to generate temporary sig files, public and private keys used to generate and verify sig are placed in this directory.<br/>
If a user chooses to place the files to another customized directory, please modify server/account/AccountLoginCmd.php into customized directory to ensure that these files are readable.

```php
	$private_key = DEPS_PATH . '/sig/private_key';
	$public_key = DEPS_PATH . '/sig/public_key';
```

* If you use LVB code to perform non-interactive stream push, you need to modify the BIZID of the codes in server/live/ReportLiveRoomInfoCmd.php.

```php
	const BIZID = '123456';
```

* If you want to upload images, you need to activate Tencent Cloud COS service and enter the corresponding APPID, SecretKey and SecretID in deps/cos-php-sdk/Conf.php.

### 1.3 Create Table and Database

Execute sql in the sxb_db.sql file.

## 2. Code Directory Structure

![](https://mc.qcloudimg.com/static/img/0413205b36b65645ef4a5ddd8135198c/2.png)

### 2.1 service 

The service layer (a.k.a the interface layer) mainly includes account management, LVB service, AV room service and COS service. Each service (module) contains subinterfaces. For more information, please see the protocol document.

#### (1) LVB Service

- Start LVB: The database Replaces a record. Note that one user can only have one ongoing LVB at a time;
- End LVB: The record is deleted from the database;
- LVB List: Acquire LVB list from database pages;
- LVB Heartbeat Packet: The client sent heartbeat packet to update data every 10 seconds.

#### (2) COS Service

Acquire COS signature.

#### (3) AvRoom Service

Acquire AV room number.


### 2.2 model 

Data layer.

### 2.3 client-data 

Client data object layer which is mainly used to receive and return data objects to the client.

### 2.4 lib 

Contains libraries such as databases and logs.

### 2.5 deps 

Dependent libraries, programs and files. These mainly include other projects or SDKs, such as Tencent Cloud COS SDK.

### 2.6 cron 
Scheduled background task. Clears any LVB records that do not send heartbeat packet in 90 seconds. Scheduled execution is available through the use of crontab.

## 3. Important Note
 
 * The other users must have read/write permissions for the sig directory.
 * The deps/bin/tls_licence_tools signature program must have execution permission.
 * Change to your own SDKAPPID and private/public key path.

## 4. Interaction Diagram
![Tencent ILVB Data Interaction](https://mc.qcloudimg.com/static/img/4094feaf383cf1e3c5714bd3f9dbfc8e/hudongzhibo.png)

## 5. Realized Features

* Register
* Login
* Create rooms
* Report room creation result
* Pull live room list
* Report room entrance information
* Pull room member list
* Heartbeat report
* Apply to join broadcasting
* Report joint broadcasting application result
* Report completion of recorded video
* Exit room
* Pull VOD list
* Pull non-interactive broadcasting address list
* Pull the non-interactive broadcasting address of specified room
* Log out

