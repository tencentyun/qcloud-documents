## Feature Description
With COSCMD tool, users can perform operations such as batch upload/download/deletion of Objects by using simple command line instructions.

## Operating Environment
### System environment
Windows or Linux system
(Local characters should be in utf-8 format, otherwise exceptions will occur when operating on Chinese files.)
### Software dependencies
- Python 2.6/2.7/3.5/3.6 
- Latest version of pip

### Installation and configuration
For more information on the installation and configuration of environment, please see [Install and Configure Python](/document/product/436/10866).
## Download and Installation
1. Check whether it is Windows or Linux system.

2. Check whether Python is installed. For more information on how to install Python, please see [Install and Configure Python](/document/product/436/10866)

3. Check whether the latest version of pip is installed. For more information on how to install pip, please see [PyPA pip Document](https://pip.pypa.io/en/stable/installing/).

4. Download [COSCMD installer package](https://github.com/tencentyun/coscmd).

5. Open the Terminal and install pip by executing the following command:

   ```
   pip install coscmd
   ```

   After installation is completed, you can view the current version information using `pip -v` or `pip --version` command.

6. Update COSCMD by executing the following command:

   ```
   pip install coscmd -U
   ```

>Note: pip can be installed or updated by using the above methods in either Linux or Windows environment.

## How to Use
### View help
Users can view the tool's help information with `-h` or `--help` command.
```
coscmd -h  //View current version information
```
The help information is shown as follows:
```
usage: cos_cmd.py [-h] [-d] [-b BUCKET] [-r REGION] [-c CONFIG_PATH]
                  [-l LOG_PATH] [-v]
                  {config,upload,download,delete,copy,list,info,mget,restore,signurl,createbucket,deletebucket,putobjectacl,getobjectacl,putbucketacl,getbucketacl}
                  ...

an easy-to-use but powerful command-line tool. try 'coscmd -h' to get more
informations. try 'coscmd sub-command -h' to learn all command usage, likes
'coscmd upload -h'

positional arguments:
  {config,upload,download,delete,copy,list,info,mget,restore,signurl,createbucket,deletebucket,putobjectacl,getobjectacl,putbucketacl,getbucketacl}
    config              config your information at first.
    upload              upload file or directory to COS.
    download            download file from COS to local.
    delete              delete file or files on COS
    copy                copy file from COS to COS.
    list                list files on COS
    info                get the information of file on COS
    mget                download file from COS to local.
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
  -r REGION, --region REGION
                        set region
  -c CONFIG_PATH, --config_path CONFIG_PATH
                        set config_path
  -l LOG_PATH, --log_path LOG_PATH
                        set log_path
  -v, --version         show program's version number and exit
```
In addition, you can also enter `-h` after each command (with no parameter appended) to see how to use the command. For example:
```
coscmd upload -h  //View the usage of upload command
```
### Configure parameters
You need to configure parameters before using the COSCMD tool. Run the following command for configuration:
```
coscmd config -a  -s  -b  -r  [-m ] [-p ]      
```
In the above example, fields in "<>" are required, and those in "[]" are optional. Parameters are described below:

| Name | Description | Valid Value |
| :---------| :---------------------------------------- | :---- |
| secret_id | ID of the key corresponding to the APPID (required). It can be obtained on the **Key Management** in the left navigation pane of the COS console, or on the [Cloud API Key Console](https://console.cloud.tencent.com/cam/capi). | String |
| secret_key | The Key corresponding to the APPID (required). It can be obtained on the **Key Management** in the left navigation pane of the COS console, or on the [Cloud API Key Console](https://console.cloud.tencent.com/cam/capi). | String |
| bucket | The specified bucket name (required), which is in a format of {name}-{appid}. For more information, please see [Create Bucket](/doc/product/436/6232). | String |
| region | The region where the bucket resides (required). For more information, please see [Available Regions](/doc/product/436/6224) | String |
| max_thread | The maximum number of threads for multi-threaded upload (optional). Default is 5. Valid value: 1-10. | Numeral |
| parts_size | Part size in multipart upload (in MB) (optional). Default is 1 MB. Valid value: 1-10. | Numeral |

> **Note:** 
1. You can directly edit `~/.cos.conf` file (a hidden file located under `My Documents` in Windows environment).
The following shows an example of the content of the configured `.cos.conf` file:
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
2. Add `schema` in the configuration file to select `http/https`. Default is `https`.
3. Bucket must be in a format of `{name}-{appid}`.


### Command for specifying a bucket
-  You can specify a bucket with `-b ` command and upload files to it using relevant commands, such as the command for uploading files.
- The bucket entered must be in a format of `{name}-{appid}`.
```
coscmd -b  method ...  //Command format
coscmd -b AAA-12345567 upload a.txt b.txt  //Example - Upload files
coscmd -b AAA-12344567 createbucket  //Example - Create a bucket
```

### Create a bucket
-  It should be used together with `-b ` command.
```
coscmd -b  createbucket //Command format
coscmd -b AAA-12344567 createbucket  //Example
```

### Delete a bucket
-  It should be used together with `-b ` command.
```
coscmd -b  deletebucket //Command format
coscmd -b AAA-12344567 deletebucket  //Example
```

### Upload files or folder

- Command for file upload is as follows:
```
coscmd upload    //Command format
coscmd upload /home/aaa/123.txt bbb/123.txt  //Example
coscmd upload /home/aaa/123.txt bbb/  //Example
```
- Command for folder upload is as follows:
```
coscmd upload -r    //Command format
coscmd upload -r /home/aaa/ bbb/aaa  //Example
coscmd upload -r /home/aaa/ bbb/  //Example
coscmd upload -r /home/aaa/ /  //Upload to the bucket root directory
coscmd upload -rs /home/aaa/ /home/aaa  //Upload files synchronously and skip those with the same md5
coscmd upload -rs /home/aaa/ /home/aaa --ignore *.txt,*.doc //Ignore .txt and .doc files
```

Replace the parameters in "<>" with the path of the local file to be uploaded (localpath) and the storage path on COS (cospath).
> **Note:** 
* When uploading a file, you need to provide a complete path including the file (folder) name on COS (refer to the example).
* COSCMD supports resuming upload from breakpoint for large files. When multipart upload of large files failed, only the part that fails to be uploaded is uploaded again, instead of starting over from scratch (please ensure that the directory and content of the re-uploaded file are consistent with the uploaded directory).
* COSCMD performs MD5 verification on each part in multipart upload.
* `x-cos-meta-md5` header is carried by default when COSCMD uploads a file, and its value is the `md5` of the file.
* Use -s parameter to upload files synchronously and skip those with the same md5 (only if the source files on COS are uploaded using COSCMD 1.8.3.2 or above, and x-cos-meta-md5 header is carried by default).
* HTTP header that is set with -H parameter must be in json format. For example: `coscmd upload -H '{"Cache-Control":"max-age=31536000","Content-Language":"zh-CN"}'  `.
* You can ignore a certain type of files using ` --ignore` parameter when uploading files. Multiple Shell wildcard rules (separated by commas) are supported.
* File size is limited to 40 TB for a single file upload.

### Download files or folder
- Command for file download is as follows:
```
coscmd download    //Command format
coscmd download bbb/123.txt /home/aaa/111.txt  //Example
coscmd download bbb/123.txt /home/aaa/  //Example
```
- Command for folder download is as follows:
```
coscmd download -r   //Command format
coscmd download -r /home/aaa/ bbb/aaa  //Example
coscmd download -r /home/aaa/ bbb/  //Example
coscmd download -rf / bbb/aaa  //Download all the files under the current bucket root directory and overwrite local files
coscmd download -rs / bbb/aaa  //Download all the files under the current bucket root directory synchronously and skip those with the same md5
coscmd download -rs / bbb/aaa --ignore *.txt,*.doc //Ignore .txt and .doc files
```
Replace the parameters in "<>" with the path of the file to be downloaded on COS (cospath) and the local storage path (localpath).

> **Note:** 
- If a file with the same name exists locally, the download will fail. Use the `-f` parameter to overwrite the local file.
- The API `download` employs multipart download, which should be used since the old version API `mget` has been deprecated.
- Use the parameter `-s` or `--sync` to skip the files that already exist locally when downloading a folder
(only if the folder to be downloaded is uploaded using the API `upload` of `COSCMD`, and `x-cos-meta-md5` header is carried in the files).
- You can ignore a certain type of files using --ignore parameter when downloading files. Multiple Shell wildcard rules (separated by commas) are supported.

### Delete files or folder
- Command for file deletion is as follows:
```
coscmd delete   //Command format
coscmd delete bbb/123.txt  //Example
```
- Command for folder deletion is as follows:
```
coscmd delete -r   //Command format
coscmd delete -r bbb/  //Example
coscmd delete -r /  //Example
```

Replace the parameter in "<>" with the path of the file to be deleted on COS (cospath). You will be prompted to confirm this operation.
> **Note:** 
* You can use `-f` parameter to skip the confirmation that is required for batch deletion.

### Copy files or folder
- Command for file copying is as follows:
```
coscmd copy    //Command format
coscmd copy bucket-appid.cos.ap-guangzhou.myqcloud.com/a.txt aaa/123.txt  //Example
```
- Command for folder copying is as follows:
```
coscmd copy -r    //Command format
coscmd copy -r bucket-appid.cos.ap-guangzhou.myqcloud.com/coscmd/ aaa //Example
coscmd copy -r bucket-appid.cos.ap-guangzhou.myqcloud.com/coscmd/ aaa/ //Example
```

Replace the parameters in "<>" with the path of the file to be copied on COS (sourcepath) and the path to which the file is copied on COS (cospath).

> **Note:** 
The format of sourcepath:```-.cos..myqcloud.com/```

### Print file list
- Print command is as follows:
```
coscmd list   //Command format
coscmd list -a //Example
coscmd list bbb/123.txt  -r -n 10 //Example
```
Replace the parameter in "<>" with the path of the file list to be printed on COS (cospath).
* Use `-a` to print all files.
* Use `-r` to print files recursively. The number and total size of files are listed at the end of the returned result.
* Use `-n num` to set the maximum number of files to be printed.

> **Note:** 
If `` is left empty, the files under the current Bucket root directory are printed by default.

### Display file information
- Command is as follows:
```
coscmd info   //Command format
coscmd info bbb/123.txt //Example
```
Replace the parameter in "<>" with the path of the file to be displayed on COS (cospath).

### Get signed download URL
- Command is as follows:
```
coscmd signurl   //Command format
coscmd signurl bbb/123.txt //Example
coscmd signurl bbb/123.txt -t 100//Example
```
Replace the parameter in "<>" with the path of the file on COS for which you need to get the download URL (cospath).
Use `-t time` to set the validity period of the signature to be printed (in sec).

### Set Access Control List (ACL)
- Command is as follows:
Set Bucket ACL using the following command:
```
coscmd putbucketacl [--grant-read GRANT_READ]  [--grant-write GRANT_WRITE] [--grant-full-control GRANT_FULL_CONTROL] //Command format
coscmd putbucketacl --grant-read 12345678,12345678/11111 --grant-write anyone --grant-full-control 12345678/22222 //Example
```
Set Object ACL using the following command:
```
coscmd putobjectacl [--grant-read GRANT_READ] [--grant-write GRANT_WRITE] [--grant-full-control GRANT_FULL_CONTROL]  //Command format
coscmd putobjectacl --grant-read 12345678,12345678/11111 --grant-write anyone --grant-full-control 12345678/22222 aaa/aaa.txt //Example
```

### How to set ACL
* --grant-read represents read permission.
* --grant-write represents write permission.
* --grant-full-control represents read-write permission.
* GRANT_READ / GRANT_WRITE / GRANT_FILL_CONTORL represents the account granted with permission.
* For authorization to a root account, the format of rootid is used.
* For authorization to a sub-account, the format of rootid/subid is used.
* For authorization to any account, the format of anyone is used.
* Accounts that are granted with permissions at the same time are separated with `,`.
* Replace the parameter with the path of the file to be deleted on COS (cospath).
* In case of Object ACL setting, if you want to set an ACL for all files under a folder, add `/` to the end of the folder name.

### Get Access Control List (ACL)
- Get the Bucket ACL using the following command:
```
coscmd getbucketacl //Command format
coscmd getbucketacl //Example
```
- Get the Object ACL using the following command:
```
coscmd getobjectacl  //Command format
coscmd getobjectacl aaa/aaa.txt //Example
```

### Restore archived files
- Command is as follows:
```
coscmd restore   //Command format
coscmd restore a.txt -d 3 -t  Expedited//Example
coscmd restore a.txt -d 3 -t  Bulk///Example
```
Replace the parameter in "<>" with the path of the file list to be printed on COS (cospath).
* Use `-d day` to set the validity period of the temporary replica. Default value: 7.
* Use `-t tier` to specify restoring mode. Enumerated values: Expedited, Standard, and Bulk. Default value: Standard.

### Command for Debug mode
If `-d` or `-debug` is added before each command, the details of operation during command execution are displayed. Here's an example:
```
//Display details of upload operation
coscmd -d upload    //Command format
coscmd -d upload /home/aaa/123.txt bbb/123.txt  //Example
```
