In consideration of compression performance and compression ratio, the backup files and BINLOG files are compressed using LZ4 (Extremely Fast Compression algorithm) tool. You can also use LZ4 tool for decompression. Since common decompression tools are not supported for the above files, this document provides a decompression tool and instructions.

## Windows
### Downloading Tool
Click [here](https://mccdn.qcloud.com/static/archive/b20514551ff6887a136c63b4808f9f22/LZ4_install_v1.4.zip) to download the decompression tool.
### Installing Tool
Double-click the zip file. After the file has been decompressed, you can get *LZ4installv1.4.exe*. Double-click the exe file, and then complete the installation as instructed.
If it is only used to decompress the file, the check box in the last step can be ignored.
### Decompressing File
As shown in the figure below, right-click the LZ4 file to be decompressed, and select **Decode with LZ4** to complete the decompression process
![](https://mccdn.qcloud.com/static/img/add13eb42359b33e5695c3da42bbce97/add13eb42359.png)

## Linux
### Installing Tool
YUM database of Tencent Cloud's CVM has an LZ4 component, so you can directly run the following command for installation:
`$ yum install lz4`
A message indicating a successful installation is returned if you run **LZ4**, as shown below:
![](https://mccdn.qcloud.com/static/img/c3850df767705f8a454299c00cdc937d/c3850df76770.png)

### Decompressing File
Run the following command for decompression:
`$ lz4 -d xxx.lz4`
