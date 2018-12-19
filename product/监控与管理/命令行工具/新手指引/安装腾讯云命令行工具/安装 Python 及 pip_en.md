Python environment is required to run Tencent Cloud CLI. You need to check whether your computer has installed Python environment and Pip tools before using CLI.

## Installing Python and Pip on Windows
Log in to [Python Official Website](https://www.python.org/downloads/) to download Python 2.7.x and install it according to the installation guide.

Note: Enable Pip before installing Python. Otherwise, Tencent Cloud CLI cannot be installed.

## Installing Python and Pip on Linux/Unix/MacOS
### Method 1: Installation by OS
(1) To install Python and Pip on Ubuntu, use the following command:

```
$ sudo apt-get install python python-pip
```

(2) To install Python and Pip on CentOS and Redhat, use the following command:

```
$ sudo yum install python python-pip
```
### Method 2: Installation by Source Code
(1) Install Python

```
$ wget https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz
$ tar -zxvf Python-2.7.12.tgz
$ cd Python-2.7.12
$ ./configure
$ make
$ sudo make install
```

(2) Install Pip tools

```
$ curl "https://bootstrap.pypa.io/get-pip.py" -o "pip-install.py"
$ sudo python pip-install.py
```
