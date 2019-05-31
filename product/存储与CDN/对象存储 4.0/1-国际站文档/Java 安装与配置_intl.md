JDK is the SDK for Java. This document takes JDK 1.7 and 1.8 as examples to describe how to install and configure JDK under Windows and Linux systems.

## Windows
### 1. Download JDK
Go to the [Oracle official website](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) to download an appropriate JDK version for installation.
### 2. Install
Install JDK as instructed in the default directory (C drive) or a custom installation directory. In this example, we use the following directories:
`D:\Program Files\Java\jdk1.8.0_31`
`D:\Program Files\Java\jre1.8.0_31`
![Local synchronization tool 1](//mc.qcloudimg.com/static/img/0652f9759c4f7fa7e61aa406ca1ad822/image.png)
### 3. Configure
After the installation is completed, right click **Computer**, and then click **Properties** -> **Advanced System Settings** -> **Environment Variables** -> **System Variables** -> **New** to configure the software.
Variable name (N): **JAVA_HOME**   
Variable value (V): D:\Program Files\Java\jdk1.8.0_31    *// Configure according to your actual installation path*
![Local synchronization tool 2](//mc.qcloudimg.com/static/img/f02f0ec6b87576f32fbade9cd8d55c1e/image.png)
Variable name (N): **CLASSPATH**   
Variable value (V): .;%JAVA_HOME%\lib\dt.jar;%JAVA_HOME%\lib\tools.jar;        *// Note: Variable value begins with "."*
![Local synchronization tool 3](//mc.qcloudimg.com/static/img/d2c87f5ce4c2927f5e9ca9d20e4478d6/image.png)
Variable name (N): **Path**
Variable value (V): %JAVA_HOME%\bin;%JAVA_HOME%\jre\bin;
![Local synchronization tool 4](//mc.qcloudimg.com/static/img/5ee8cc105d52f9052cc49251ce88ed9a/image.png)
### 4. Test
Test whether the configuration is successful: **Start** (or shortcut: Win+R) -> **Run** (enter `cmd`) -> **OK** (or press Enter), then enter the command `javac` and press Enter. The following message indicates that the environment variable is configured successfully.
![Local synchronization tool 5](//mc.qcloudimg.com/static/img/83f8417d6f540c20182267acba29f2ad/image.png)
## Linux
If openjdk is installed by using yum or apt-get command, the class library may be incomplete, thus leading to errors when you run relevant tools after the installation. Therefore, we recommend that you install the JDK by means of manual decompression and installation. Specific steps are as follows:
### 1. Download JDK
Go to the [Oracle official website](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html) to download an appropriate JDK version for installation.
Note: You need to download a version for Linux. Take jdk-8u151-linux-x64.tar.gz as an example. The file you downloaded may be another version, but the suffix of your file must be .tar.gz.
### 2. Create a directory 
Create a `java` directory in the `/usr/` directory.
```
mkdir /usr/java
cd /usr/java 
```
Place the downloaded file jdk-8u151-linux-x64.tar.gz in the /usr/java/ directory. 

### 3. Decompress JDK
```
tar -zxvf jdk-8u151-linux-x64.tar.gz 
```
### 4. Set Environment Variables
```
Modify /etc/profile 
```
Add the following content to the profile file and save it:
```
set java environment
JAVA_HOME=/usr/java/jdk1.8.0_151        
JRE_HOME=/usr/java/jdk1.8.0_151/jre     
CLASS_PATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar:$JRE_HOME/lib
PATH=$PATH:$JAVA_HOME/bin:$JRE_HOME/bin
export JAVA_HOME JRE_HOME CLASS_PATH PATH 
```
Note: JAVA_HOME and JRE_HOME should be configured according to your actual installation path and JDK version.

Make the change take effect:
```
source /etc/profile 
```

### 5. Test
```
java -version
```
If the java version information appears, it indicates that JDK is installed successfully.
```
java version "1.8.0_151"
Java(TM) SE Runtime Environment (build 1.8.0_151-b12)
Java HotSpot(TM) 64-Bit Server VM (build 25.151-b12, mixed mode)
```

