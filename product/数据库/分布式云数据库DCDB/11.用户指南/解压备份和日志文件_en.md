For the sake of compression performance and compression ratio, TDSQL's backup files and log files (binlogs) are compressed using [LZ4 (Extremely Fast Compression algorithm)](http://cyan4973.github.io/lz4/). You can use LZ4 tool to decompress these files. Since common decompression tools are not supported for the above file formats, the decompression tool and the operation guide are provided here for your reference.

## Windows
### Downloading Tool
Click [here](https://mccdn.qcloud.com/static/archive/b20514551ff6887a136c63b4808f9f22/LZ4_install_v1.4.zip) to download decompression tool.
### Installing Tool
Double click and decompress the zip file to acquire *LZ4installv1.4.exe*. Double click the exe file and complete the installation as instructed.
The check box in the last step can be ignored if the tool is only used to decompress files 
### Decompressing File
Right click the LZ4 file to be decompressed and select **Decode with LZ4** to complete the process.
![](https://mccdn.qcloud.com/static/img/add13eb42359b33e5695c3da42bbce97/add13eb42359.png)

## Linux
### Installing Tool
Since the yum library of Tencent Cloud CVM contains the LZ4 component, you can simply execute the following command to install this component:
`$ yum install lz4`
The installation is successful if the result is returned as shown below after you execute **LZ4**:
![](https://mccdn.qcloud.com/static/img/c3850df767705f8a454299c00cdc937d/c3850df76770.png)

### Decompressing File
Execute the following command to decompress the file:
`$ lz4 -d xxx.lz4`
