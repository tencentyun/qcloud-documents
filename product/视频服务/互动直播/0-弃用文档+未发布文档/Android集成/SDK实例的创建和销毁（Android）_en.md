## AVContext Introduction
Before launching AVSDK, you need to create an AVContext (SDK Context) object. AVContext is used to manage SDK internal threads and running contexts. An AVContext object can be considered as an SDK operation instance. In most cases, an application only needs to create one unique AVContext object to use all SDK features.
Note: Ensure that the created AVContext instance is unique. Creating multiple AVContext instances may lead to unexpected consequences due to reasons such as device occupation.
## Creating/Terminating AVContext
### 1. Create AVContext
Creating context requires two steps:
(1) Configure the parameters of AVContext by using Config.
(2) Create AVContext based on the parameters.

**API Description:**
![API Description](//mccdn.qcloud.com/static/img/fbd0e60943c197de706da2c622008df9/image.png)

**Sample Code** (The parameters are for simulation only. You need to acquire the actual parameters from the Server end):
![Sample Code](//mccdn.qcloud.com/static/img/bf6b0411b3cccc11cb73e58604ac4237/image.png)
### 2. Terminate AVContext
(1) Terminating the current AVContext is only available after createContext is called. It is recommended to call this API after asynchronous callback of stop() is performed.
(2) The AVContext object should be set as null after termination.

**API Description:**
![API Description](//mccdn.qcloud.com/static/img/010cdc1f978fd55e19eb5e881fc4f1b5/image.png)

**Sample Code:**
![](//mccdn.qcloud.com/static/img/f2a022be50f705449f8901ed19611ec6/image.png)
## Launching/Stopping AVContext
### 1. Launch AVContext
Launching context requires two steps:
#### (1) Log in to IMSDK
Configuration parameters needed for login are the same as those used to create AVContext.
 ![Log in to IMSDK](//mccdn.qcloud.com/static/img/eed1f82d0d94a751859b7ffed64577b7/image.png)
 
#### (2) Launch AVContext

**API Description:**
 ![API Description](//mccdn.qcloud.com/static/img/bcdb258a321f0a3cc76fda78f3c82660/image.png)
 
**Sample Code:**
 ![Sample Code](//mccdn.qcloud.com/static/img/6ae61b457e50813914adac4435190aab/image.png)
### 2. Stop AVContext
When the current AVContext object is stopped, you must call "destroy" to terminate the AVContext object manually and set it to "null".

**API Description:**
 ![API Description](//mccdn.qcloud.com/static/img/3fd19b52486e51581b2bf29152ae99b6/image.png) 

**Sample Code:**
 ![Sample Code](//mccdn.qcloud.com/static/img/19fdda74630245a84fbee33bc484fb42/image.png)

