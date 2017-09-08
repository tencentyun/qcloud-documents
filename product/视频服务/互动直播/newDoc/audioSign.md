
## 音视频密钥使用说明
### 一、密钥及加密算法
#### 1、密钥： appId对应音视频密钥，长度16字节；官网上可查,如下:
![](https://zhaoyang21cn.github.io/iLiveSDK_Help/readme_img/audiosig_0.png)
#### 2、加密算法：Tea加密；
#### 3、加密库及例子：附件《tea.zip》；

### 二、使用场景一：开房间权限加密串

#### 1、密文内容

字段描述|类型/长度|值定义/备注
:--:|:--:|:--
cVer|unsigned char/1|版本号，填0
wAccountLen|unsigned short /2|第三方自己的帐号长度
buffAccount|wAccountLen|第三方自己的帐号字符
dwSdkAppid|unsigned int/4|sdkappid
dwAuthId|unsigned int/4|群组号码
dwExpTime|unsigned int/4|过期时间 （当前时间 + 有效期（单位：秒，建议300秒））
dwPrivilegeMap|unsigned int/4|权限位
dwAccountType|unsigned int/4|第三方帐号类型

#### 2、加密方式
##### a）、密文中的数字转换成网络字节序（大端字节序）；
##### b）、把密文拼接成一段字符串；
##### c）、用tea加密对字符串加密，symmetry_encrypt函数输出的字符串即为权限加密串(注意:不用要把二进制串转成16进制)；
#### 3、密文验证
用工具test_tea_decode(和lib一起打包提供)可以初步验证密文是否可以解密.
##### a)将密文转成16进制的可读字符串.
##### b)工具校验:
能正确解密的场景:
![](https://zhaoyang21cn.github.io/iLiveSDK_Help/readme_img/audiosig_1.png)
不能正确解密的场景:
![](https://zhaoyang21cn.github.io/iLiveSDK_Help/readme_img/audiosig_2.png)
### 二、使用场景二：跨房间连麦加密串
#### 1、密文内容
附件：《conn_room_sig.proto》
```
package tencent.im.groupvideo.conn_room;

message ConnRoomSig
{
    optional uint32         uint32_groupcode            = 1; //发起方群号
    optional string         str_third_account           = 2; //发起方第三方帐号

    optional uint32         uint32_conned_groupcode     = 3; //被连方群号
    optional string         str_conned_third_account    = 4; //被连方第三方帐号

    optional uint32         uint32_create_time          = 5; //签名创建时间
    optional uint32         uint32_expire_time          = 6; //签名过期时间
}
```
字段描述|是否必须|值定义/备注
:--:|:--:|:--:
uint32_groupcode|是|发起方群号/群组Id
str_third_account|是|发起方帐号
uint32_conned_groupcode|是|被连麦群号/群组Id
str_conned_third_account|是|被连方帐号
uint32_create_time|是|签名创建时间
uint32_expire_time|是|签名过期时间，建议设置为创建时间+300秒
#### 2、加密方式
##### a）、使用google protobuf序列化ConnRoomSig对象，输出二进制字符串；
##### b）、用tea加密对二进制字符串加密，symmetry_encrypt函数输出的字符串即为加密串；
##### c）、把加密串转换成16进制字符串，大小写均可，如：
```
bytes_conn_room_sig: 
"00A47C7E5FD0471A6D90CBE6FAAC2D862A114EFC6337D8F0BD1161BB53250F4EE46DB0244E8515D58BA7DAED23190484"
```
google protobuf官网：[https://github.com/google/protobuf](https://github.com/google/protobuf)


[加密代码下载](http://dldir1.qq.com/hudongzhibo/ILiveSDK/tea_3.zip)
