## Preparations for Development
### Obtaining SDK
Download XML C++ SDK resources of COS service from: [XML C++ SDK Download](https://github.com/tencentyun/cos-cpp-sdk-v5 "cos-cpp-sdk-v5 download address").
Download Demo from: [XML C++ SDK Demo](https://github.com/tencentyun/cos-cpp-sdk-v5/blob/master/demo/cos_demo.cpp "Cpp SDK reference").

### Environment
**Dependent static library:** jsoncpp boost_system boost_thread Poco (in lib folder);
**Dependent dynamic library:** ssl crypto rt z (installation is required).
JsonCpp libraries and header files are available in the SDK. If you want to install it yourself, compile the libraries installed in the following steps and replace the relevant library and header files in the SDK. If the above libraries are already installed on the system, you can also delete the relevant libraries and header files in the SDK. The installation steps are as follows:

#### 1. Install the CMake tool.
```
yum install -y gcc gcc-c++ make automake
//Install the required packages such as GCC (skip this step if they have been installed)
yum install -y wget

// The cmake version should be greater than 3.5
wget https://cmake.org/files/v3.5/cmake-3.5.2.tar.gz
tar -zxvf cmake-3.5.2.tar.gz
cd cmake-3.5.2.tar.gz
./bootstrap --prefix=/usr
gmake
gmake install
```

#### 2. Install Boost libraries and header files.
```
wget http://sourceforge.net/projects/boost/files/boost/1.54.0/boost_1_54_0.tar.gz
tar -xzvf boost_1_54_0.tar.gz
cd boost_1_54_0
./bootstrap.sh --prefix=/usr/local
./b2 install --with=all
# Boost libraries are installed in the directory /usr/local/lib
```

#### 3. Install OpenSSL.

```
yum install openssl openssl-devel
```

Or

```
wget https://www.openssl.org/source/openssl-1.0.1t.tar.gz  
tar -xzvf ./openssl-1.0.1t.tar.gz
cd openssl-1.0.1t/
./config --prefix=/usr/local/ssl --openssldir=/usr/local/ssl

cd /usr/local/
ln -s ssl openssl
echo "/usr/local/openssl/lib" >> /etc/ld.so.conf
ldconfig

# Add header/lib file search path (can be written to ~/.bashrc)
LIBRARY_PATH=/usr/local/ssl/lib/:$LIBRARY_PATH
CPLUS_INCLUDE_PATH=/usr/local/ssl/include/:$CPLUS_INCLUDE_PATH
```

#### 4. Obtain Poco libraries and header files from [Poco official website](https://pocoproject.org/download/index.html) and install them (download the complete version).
```
./configure --omit=Data/ODBC,Data/MySQL
make
make install
```

#### 5. Obtain APP ID, SecretID, and SecretKey from the console.
> For more information on definitions of SecretId, SecretKey, Bucket and other terms and how to obtain them, please see [COS Glossary](/document/product/436/7751).

> You can specify the path to the local Boost header files by modifying the following statement in `CMakeList.txt` file: 
```
SET(BOOST_HEADER_DIR "/root/boost_1_61_0")
```

### Configuring SDK
Directly download the source code provided on GitHub in the step [Obtaining SDK](#sdk-.E8.8E.B7.E5.8F.96) to integrate it into your development environment. Execute the following command:
``` bash
cd ${cos-cpp-sdk} 
mkdir -p build 
cd build 
cmake .. 
make
```

There are examples of common APIs in cos_demo.cpp. The generated cos_demo can be run directly, and the name of the generated static library is libcossdk.a. The generated libcossdk.a is placed in the lib path of your own project, and the include directory is copied to the include path of your project.

## Getting Started
### Initialization
```
"SecretId":"*********************************", // Use "AccessKey" for the SDK configuration file earlier than V5.4.3.
"SecretKey":"********************************",
"Region":"cn-north",                
// COS region (ensure it is correct)
"SignExpiredTime":360,              
// Signature timeout (in sec)
"ConnectTimeoutInms":6000,          
// connect timeout (in ms)
"HttpTimeoutInms":60000,            
// http timeout (in ms)
"UploadPartSize":1048576,           
// Size of each part of file in multipart upload; it ranges from 1 MB to 5 GB. Default is 1 MB.
"UploadThreadPoolSize":5,           
// Thread pool size for uploading a single file in multiple parts
"DownloadSliceSize":4194304,        
// Size of each part of file in multipart download
"DownloadThreadPoolSize":5,         
// Thread pool size for downloading a single file
"AsynThreadPoolSize":2,             
// Thread pool size for asynchronous upload and download
"LogoutType":1,                     
// Log output type. 0: Do not output; 1: Output to screen; 2: Output to syslog
"LogLevel":3                     
// Log level. 1: ERR; 2: WARN; 3: INFO; 4: DBG
```
### Creating Bucket
```
#include "cos_api.h"
#include "cos_sys_config.h"
#include "cos_defines.h"

int main(int argc, char *argv[]) {
    // 1. Specify the path to configuration file and initialize CosConfig
    qcloud_cos::CosConfig config("./config.json");
    qcloud_cos::CosAPI cos(config);
    
    // 2. Construct a request to create a Bucket
    std::string bucket_name = "cpp_sdk_v5-123456789"; // Bucket Name
    qcloud_cos::PutBucketReq req(bucket_name);
    qcloud_cos::PutBucketResp resp;
    
    // 3. Call the API for creating Bucket
    qcloud_cos::CosResult result = cos.PutBucket(req, &resp);
    
    // 4. Process the result of the call
    if (result.IsSucc()) {
        // Created successfully
    } else {
        // Failed to create the Bucket. You can call the CosResult's member function to output error information, such as requestID, etc.
        std::cout << "ErrorInfo=" << result.GetErrorInfo() << std::endl;
        std::cout << "HttpStatus=" << result.GetHttpStatus() << std::endl;
        std::cout << "ErrorCode=" << result.GetErrorCode() << std::endl;
        std::cout << "ErrorMsg=" << result.GetErrorMsg() << std::endl;
        std::cout << "ResourceAddr=" << result.GetResourceAddr() << std::endl;
        std::cout << "XCosRequestId=" << result.GetXCosRequestId() << std::endl;
        std::cout << "XCosTraceId=" << result.GetXCosTraceId() << std::endl;
    }
}
```

### Uploading files
```
#include "cos_api.h"
#include "cos_sys_config.h"
#include "cos_defines.h"

int main(int argc, char *argv[]) {
    // 1. Specify the path to configuration file and initialize CosConfig
    qcloud_cos::CosConfig config("./config.json");
    qcloud_cos::CosAPI cos(config);
    
    // 2. Construct a request to upload a file
    std::string bucket_name = "cpp_sdk_v5-123456789"; // Name of destination Bucket for upload
    std::string object_name = "object_name"; // object_name is the object key, which is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg.
    // The local file path is required in the constructor of the request
    qcloud_cos::PutObjectByFileReq req(bucket_name, object_name, "/path/to/local/file");
    req.SetXCosStorageClass("STANDARD_IA"); // Call Set method to set metadata or ACL
    qcloud_cos::PutObjectByFileResp resp;
    
    // 3. Call the API for uploading file
    qcloud_cos::CosResult result = cos.PutObject(req, &resp);
    
    // 4. Process the result of the call
    if (result.IsSucc()) {
        // File is uploaded successfully
    } else {
        // Failed to upload the file. You can call the CosResult's member function to output error information, such as requestID, etc.
        std::cout << "ErrorInfo=" << result.GetErrorInfo() << std::endl;
        std::cout << "HttpStatus=" << result.GetHttpStatus() << std::endl;
        std::cout << "ErrorCode=" << result.GetErrorCode() << std::endl;
        std::cout << "ErrorMsg=" << result.GetErrorMsg() << std::endl;
        std::cout << "ResourceAddr=" << result.GetResourceAddr() << std::endl;
        std::cout << "XCosRequestId=" << result.GetXCosRequestId() << std::endl;
        std::cout << "XCosTraceId=" << result.GetXCosTraceId() << std::endl;
    }
}
```

### Downloading files
```
#include "cos_api.h"
#include "cos_sys_config.h"
#include "cos_defines.h"

int main(int argc, char *argv[]) {
    // 1. Specify the path to configuration file and initialize CosConfig
    qcloud_cos::CosConfig config("./config.json");
    qcloud_cos::CosAPI cos(config);
    
    // 2. Construct a request to create a Bucket
    std::string bucket_name = "cpp_sdk_v5-123456789"; // Name of destination Bucket for upload
    std::string object_name = "object_name"; // object_name is the object key, which is the unique identifier of the object in the bucket. For example, in the object's access domain name bucket1-1250000000.cos.ap-guangzhou.myqcloud.com/doc1/pic1.jpg, the object key is doc1/pic1.jpg.
    std::string local_path = "/tmp/object_name";
    // Parameters appid, bucketname and object, as well as the local path (including file name) are required for the request
    qcloud_cos::GetObjectByFileReq req(bucket_name, object_name, local_path);
    qcloud_cos::GetObjectByFileResp resp;
    
    // 3. Call the API for creating Bucket
    qcloud_cos::CosResult result = cos.GetObject(req, &resp);
    
    // 4. Process the result of the call
    if (result.IsSucc()) {
        // File is downloaded successfully
    } else {
        // Failed to download the file. You can call the CosResult's member function to output error information, such as requestID, etc.
        std::cout << "ErrorInfo=" << result.GetErrorInfo() << std::endl;
        std::cout << "HttpStatus=" << result.GetHttpStatus() << std::endl;
        std::cout << "ErrorCode=" << result.GetErrorCode() << std::endl;
        std::cout << "ErrorMsg=" << result.GetErrorMsg() << std::endl;
        std::cout << "ResourceAddr=" << result.GetResourceAddr() << std::endl;
        std::cout << "XCosRequestId=" << result.GetXCosRequestId() << std::endl;
        std::cout << "XCosTraceId=" << result.GetXCosTraceId() << std::endl;
    }
}
```

