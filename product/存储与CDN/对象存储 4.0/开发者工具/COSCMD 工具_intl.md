## Feature Description
With COSCMD tool, users can perform operations such as batch upload/download/deletion of Objects by using simple command line instructions.

## Operating Environment
### System Environment
Windows or Linux system
### Software Dependencies
- Python 2.7 
- The latest version of pip is installed
#### Installation and Configuration
For more information on the installation and configuration of environment, please see [Install and Configure Python](https://cloud.tencent.com/document/product/436/10866).
## Download and Installation
- **Manual installation**
Download link to [GitHub](https://github.com/tencentyun/coscmd.git)
Run the following command under the root directory of the project for installation:
```
python setup.py install
```
- **Install pip**
Execute `pip` command to install:
```
pip install coscmd
```
After installation, you can view the current version information using `-v` or `--version` command.
- **Update pip**
Execute `pip` command to update:
```
pip install coscmd -U
```

> **Note:** 
pip can be installed or updated by using the above methods in either Linux or Windows environment.

## How to Use
### Viewing help
You can view the tool's help information with `-h` or `--help` command.
```
coscmd -h  //View current version information
```
The help information is shown as follows:
```
usage: coscmd [-h] [-d] [-b BUCKET] [-v]
              {config,upload,download,delete,list,info,mget,restore,signurl,createbucket,deletebucket,putobjectacl,getobjectacl,putbucketacl,getbucketacl}
              ...

an easy-to-use but powerful command-line tool. try 'coscmd -h' to get more
informations. try 'coscmd sub-command -h' to learn all command usage, likes
'coscmd upload -h'

positional arguments:
  {config,upload,download,delete,list,info,mget,restore,signurl,createbucket,deletebucket,putobjectacl,getobjectacl,putbucketacl,getbucketacl}
    config              config your information at first.
    upload              upload file or directory to COS.
    download            download file from COS to local.
    delete              delete file or files on COS
    list                list files on COS
    info                get the information of file on COS
    mget                download big file from COS to local(Recommand)
    restore             restore
    signurl             get download url
    createbucket        create bucket
    deletebucket        delete bucket
    putobjectacl        set object acl
    getobjectacl        get object acl
    putbucketacl        set bucket acl
    getbucketacl        get bucket acl

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           debug mode
  -b BUCKET, --bucket BUCKET
                        set bucket
  -v, --version         show program's version number and exit
```
In addition, users can also enter `-h` after each command (do not add parameter) to view the usage of the command. For example:
```
coscmd upload -h  //View the usage of upload command
```
### Configuring Parameters
You need to configure parameters before using the COSCMD tool. Run the following command for configuration:
```
coscmd config -a <secret_id> -s <secret_key> -b <bucket> -r <region> [-m <max_thread>] [-p <parts_size>]      
```
In the above example, fields in "<>" are required, and those in "[]" are optional. Parameters are described below:

| Name | Description | Valid Value |
| :---------| :---------------------------------------- | :---- |
| secret_id | The key ID corresponding to the APPID (required). It can be obtained on the console. For more information, please see [Basic Concepts](https://cloud.tencent.com/doc/product/436/6225). | String |
| secret_key | The Key corresponding to the APPID (required). It can be obtained on the console. For more information, please see [Basic Concepts](https://cloud.tencent.com/doc/product/436/6225). | String |
| bucket | The specified bucket name (required). The naming rule for bucket is {name}-{appid}. For more information, please see [Create Bucket](https://cloud.tencent.com/doc/product/436/6232). | String |
| region | The region of the bucket (required). For more information, please see [Available Regions](https://cloud.tencent.com/doc/product/436/6224). | String |
| max_thread |（Optional）The upper limit of threads for multi-threaded upload. Default is 5. Valid value: 1-10. | Numeral |
| parts_size |(Optional) Part size in multipart upload (in MB) . Default is 1 MB. Valid value: 1-10. | Numeral |

> **Note:** 
1. You can directly edit `~/.cos.conf` file (a hidden file located under `My Documents` in Windows environment).
The following is an example of the contents of configured `.cos.conf` file:
2. Add `schema` in the configuration file to select `http/https`
```
 [common]
secret_id = AChT4ThiXAbpBDEFGhT4ThiXAbpHIJK
secret_key = WE54wreefvds3462refgwewerewr
bucket = ABC-1234567890
region = ap-guangzhou
max_thread = 5
part_size = 1
schema = https
```

### Command for Specifying Bucket
-  Specify a Bucket using `-b <bucket> specify bucket`.
- The bucket entered must be in a format of `{name}-{appid}`.
```
coscmd -b <bucket> method ...  //Command format
coscmd -b AAA-12345567 upload a.txt b.txt  //Example - Upload a file
coscmd -b AAA-12344567 createbucket  //Example - Create a bucket
```

### Creating Bucket
-  It should be used together with `-b <bucket> specify bucket`.
```
coscmd -b <bucket> createbucket //Command format
coscmd createbucket  //Example
coscmd -b AAA-12344567 createbucket  //Example
```

### Deleting Bucket
-  It should be used together with `-b <bucket> specify bucket`.
```
coscmd -b <bucket> deletebucket //Command format
coscmd createbucket  //Example
coscmd -b AAA-12344567 deletebucket  //Example
```
### Uploading File or Folder
- Command for file upload is as follows:
```
coscmd upload <localpath> <cospath>  //Command format
coscmd upload /home/aaa/123.txt bbb/123.txt  //Example
coscmd upload /home/aaa/123.txt bbb/  //Example
```
- Command for folder upload is as follows:
```
coscmd upload -r <localpath> <cospath>  //Command format
coscmd upload -r /home/aaa/ bbb/aaa  //Example
coscmd upload -r /home/aaa/ bbb/  //Example
coscmd upload -r /home/aaa/ /  //Upload to the bucket root directory
```

Replace the parameters in "<>" with the path of the local file to be uploaded (localpath) and the storage path on COS (cospath).
> **Note:** 
* When uploading a file, you need to provide a complete path including the file (folder) name on COS (refer to the example).
* COSCMD supports resuming from break point for large files. When multipart upload of large files failed, only the part that fails to be uploaded is uploaded again, instead of starting over from scratch (please ensure that the directory and content of the re-uploaded file are consistent with the uploaded directory).
* COSCMD performs MD5 verification on each part in multipart upload.

### Downloading File or Folder
- Command for file download is as follows:
```
coscmd download <cospath> <localpath>  //Command format
coscmd download bbb/123.txt /home/aaa/111.txt  //Example
coscmd download bbb/123.txt /home/aaa/  //Example
```
- Command for folder download is as follows:
```
coscmd download-r <cospath> <localpath> //Command format
coscmd download -r /home/aaa/ bbb/aaa  //Example
coscmd download -r /home/aaa/ bbb/  //Example
coscmd download -r / bbb/aaa  //Download all the files under the current bucket root directory
```
Replace the parameters in "<>" with the path of the file to be downloaded on COS (cospath) and the local storage path (localpath).
> **Note:** 
* If a file with the same name exists locally, the download will fail. Use the `-f` parameter to overwrite the local file.
* Replace `download` in the above command with `mget` to perform multipart download. The download speed increases by 2 to 3 times in case of high bandwidth.

### Deleting File or Folder
- Command for file deletion is as follows:
```
coscmd delete <cospath>  //Command format
coscmd delete bbb/123.txt  //Example
```
- Command for folder deletion is as follows:
```
coscmd delete -r <cospath>  //Command format
coscmd delete -r bbb/  //Example
coscmd delete -r /  //Example
```

Replace the parameter in "<>" with the path of the file to be deleted on COS (cospath). You will be prompted to confirm this operation.
> **Note:** 
* You can use `-f` parameter to skip the confirmation that is required for batch deletion.

### Copying File
- Command for file copying is as follows:
```
coscmd copy <sourcepath> <cospath>  //Command format
coscmd copy bucket-appid.cos.ap-guangzhou.myqcloud.com/a.txt aaa/123.txt  //Example
```

Replace the parameters in "<>" with the path of the file to be copied on COS (sourcepath) and the path of the copied file on COS (cospath).

> **Note:** 
The format of sourcepath:```<bucketname>-<appid>.cos.<region>.myqcloud.com/<cospath>```

### List of Files to be Printed
- Print command is as follows:
```
coscmd list <cospath>  //Command format
coscmd list -a //Example
coscmd list bbb/123.txt  -r -n 10 //Example
```
Replace the parameter in "<>" with the path of the file in the list of files to be printed on COS (cospath).
* Use `-a` to print all files.
* Use `-r` to print files recursively. The number and total size of files are listed at the end of returned message.
* Use `-n num` to set the maximum number of files to be printed

> **Note:** 
If `<cospath>` is left empty, the files under the current Bucket root directory are printed by default.

### Displaying File Information
- Command is as follows:
```
coscmd info <cospath>  //Command format
coscmd info bbb/123.txt //Example
```
Replace the parameter in "<>" with the path of the file to be displayed on COS (cospath).

### Obtaining Signed Download URL
- Command is as follows:
```
coscmd signurl<cospath>  //Command format
coscmd signurl bbb/123.txt //Example
coscmd signurl bbb/123.txt -t 100//Example
```
Replace the parameter in "<>" with the path of the file on COS for which you need to obtain download URL (cospath).
Use `-t time` to set the validity period of the signature (in sec).

### Setting Access Control List (ACL)
- Command is as follows:
Set Bucket ACL using the following command:
```
coscmd putbucketacl [--grant-read GRANT_READ]  [--grant-write GRANT_WRITE] [--grant-full-control GRANT_FULL_CONTROL] //Command format
coscmd putbucketacl --grant-read 12345678,12345678/11111 --grant-write anyone --grant-full-control 12345678/22222 //Example
```
Set Object ACL using the following command:
```
coscmd putbucketacl [--grant-read GRANT_READ] [--grant-write GRANT_WRITE] [--grant-full-control GRANT_FULL_CONTROL] <cospath> //Command format
coscmd putbucketacl --grant-read 12345678,12345678/11111 --grant-write anyone --grant-full-control 12345678/22222 aaa/aaa.txt //Example
```

#### Instructions on ACL Settings
> *  --grant-read represents read permission.
* --grant-write represents write permission.
* --grant-full-control represents read/write permission.
* GRANT_READ / GRANT_WRITE / GRANT_FILL_CONTORL represents the account granted with permission.
* To grant permission to a root account, the format of rootid is used.
* To grant permission to a sub-account, the format of rootid/subid is used.
* To grant permission to any account, the format of anyone is used.
* Accounts that are granted with permission at the same time are separated with `,`.
* Replace the parameter with the path of the file to be deleted on COS (cospath).

### Obtaining Access Control List (ACL)
- Set Bucket ACL using the following command:
```
coscmd getbucketacl //Command format
coscmd getbucketacl //Example
```
- Set Object ACL using the following command:
```
coscmd putbucketacl <cospath> //Command format
coscmd getobjectacl aaa/aaa.txt //Example
```

### Restoring Archived File
- Command is as follows:
```
coscmd restore <cospath>  //Command format
coscmd restore a.txt -d 3 -t  Expedited//Example
coscmd restore a.txt -d 3 -t  Bulk///Example
```
Replace the parameter in "<>" with the path of the file in the list of files to be printed on COS (cospath).
* Use `-d day` to set the expiration time of temporary copy. Default value: 7.
* Use `-t tier` to specify restoring mode. Enumerated value: Expedited, Standard, Bulk. Default value: Standard.

### Command for Debug Mode
If `-d` or `-debug` is added before each command, details of operation during command execution is displayed. See the example below:
```
//Display details of upload operation
coscmd -d upload <localpath> <cospath>  //Command format
coscmd -d upload /home/aaa/123.txt bbb/123.txt  //Example
```

