## Feature Description

This tool is used to batch delete all files and directories under the specified COS path. **Only applicable to COS 4.0**

## Operating Environment

### System Environment

Linux, OS X or Windows system

### Required Software

Python 2.7.x

## How to Use

### Acquire the Tool Package

Github project: https://github.com/tencentyun/cos4_rm_recursive

Execute the following command from the download path to decompress:

```
sudo tar -xzvf cos_rm_recursive.tar.gz
```

### Configuration Instructions

#### Modify Configuration File conf/config.json

```json
{
  "appid":10000202,
  "secret_id":"*******",
  "secret_key":"******",
  "region":"guangzhou",
  "log_level":4,
  "log_file_name":"del_file.log",
  "dir_thread_num":2,
  "file_thread_num":5, 
  "log_out_to_screen":1,
}
```

Note:
- **appid, secret_id, secret_key**: Modify these items according to the corresponding information of your project. You can acquire them from the console
- **region**: Region: shanghai, guangzhou, tianjin, guangzhoup
- **log_level** : Log level. 0: debug. 1: info. 2: warning. 3: error
- **log_file_name**: File name of the log
- **dir_thread_num**: Number of threads when searching folders recursively
- **file_thread_num**: Number of threads when deleting files
- **log_out_to_screen**: Whether to print log onto the screen. 0: Do not print. 1: Print


#### Modify Configuration File conf/bucketlist.txt

This configuration file identifies the names of buckets and folders to be deleted. Folders need to end with "/". Structure is similar to the following:

```
testbucket, /folder1/
testbucket, /folder2/
```

Description

1. You can simply enter "<root folder> /" (bucketName, /), which means deleting all files and folders under this bucket
2. When you delete a specified directory, the directory itself will also be deleted
3. Note that folders cannot be nested with each other. For example, folder1, folder2 and folder3 must be independent

### Use the Software

Execute delete command:

``` 
python rm_recursive.py
```

### Returned Result

When execution is completed, the following critical information will be displayed on the screen and recorded in the log:

``` 
$./rm_recursive.py   
delete task started  ...........
delete task ended

rm task finished
timecost:5.16713190079 (s)
delfilenum=0,deldirnum=0,delfilefailnum=0,deldirfailnum=0
```

## FAQs

- In COS system, the operation for deleting a folder will fail if there are still files under the folder. Therefore, if a certain file fails to be deleted, all parent folders of this file will not be deleted.


- Operation frequency is restricted in COS system. Frequency control is likely to be triggered if the number of threads is configured too high, when the deletion tool will print `ERROR_PROXY_FREQ_CONTROL` on the screen. In this case, you will need to decrease the number of thread for deleting files accordingly.

