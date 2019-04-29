This document uses Python 2.7 as an example to describe how to install and configure Python under Windows and Linux systems.

## Windows
### 1. Download
Go to the [Python official website](https://www.python.org/downloads/) and download an appropriate version. In this example, we download [Python 2.7.13](https://www.python.org/ftp/python/2.7.13/python-2.7.13.amd64.msi).
### 2. Install
Double click the Python installation package, and install Python as instructed.
### 3. Configure Environment Variable
After the installation is completed, right click **Computer**, and then click **Properties** -> **Advanced System Settings** -> **Environment Variables** -> **System Variables (S)** to find "Path" (if it does not exist, create one). Append the Python installation path `;C:\Python27` (replace it with yours) to the end of "variable value", and click **OK** to save it.
![161709](//mc.qcloudimg.com/static/img/b5784ed03d0f2fd07195c9c3ae1e5075/image.png)
### 4. Test whether the configuration is successful
Click **Start** (or shortcut: Win+R) -> **Run** (enter `cmd`) -> **OK** (or press Enter), enter the Python command in the popup window, and press Enter. If the following message appears, it indicates that Python 2.7 is installed and configured successfully:
![152355](//mc.qcloudimg.com/static/img/026d7738b234171b285a98f0e751038a/image.png)
## Linux
### 1. Check the Python version 
Check the default version of Python built in Linux yum.
```
python -V
``` 
If it is Python 2.7 or above, ignore the following steps. Otherwise (in case of Python 2.6.6), enter the following command:
```
yum groupinstall "Development tools"
```
### 2. Install the component used to compile Python
```
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel
```
### 3. Download and decompress Python 2.7 
```
wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tar.xz
tar xf Python-2.7.12.tar.xz
```
### 4. Compile and install Python
```
cd Python-2.7.12 //Enter the directory
./configure -prefix=/usr/local
make && make install //Install
make clean 
make distclean
```
### 5. Direct the system Python command to Python 2.7
```
mv /usr/bin/python /usr/bin/python2.6.6
ln -s /usr/local/bin/python2.7 /usr/bin/python
```
### 6. Test whether the configuration is successful
```
python
```
If the following message appears, it indicates that Python 2.7 is installed and configured successfully:
![112046](//mc.qcloudimg.com/static/img/0eb560566c1f67e302e75b1dcb515d98/image.png)

> <font color="#0000cc">**Note:**</font>
If a permission-related error occurs, it is recommended to solve it by adding sudo before the command.

