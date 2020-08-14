## 操作场景

该任务指导您使用 C++ 语言，通过密钥对鉴权来对您的 API 进行认证管理。

## 操作步骤

1. 在 [API 网关控制台](https://console.cloud.tencent.com/apigateway/index?rid=1)，创建一个 API，选择鉴权类型为“密钥对”（参考 [创建 API 概述](https://cloud.tencent.com/document/product/628/11795)）。
2. 将 API 所在服务发布至发布环境（参考 [服务发布与下线](https://cloud.tencent.com/document/product/628/11809)）。
3. 在控制台密钥管理界面创建密钥对。
4. 在控制台使用计划界面创建使用计划，并将使用计划与已创建的密钥对绑定（参考 [使用计划示例](https://cloud.tencent.com/document/product/628/11816)）。
5. 将使用计划与 API 或 API 所在服务进行绑定。
6. 参考 [示例代码](#example)，使用 C++ 语言生成签名内容。

## 环境依赖

本 Demo 中使用 libcurl 发起 HTTP 请求,故编译机器需要安装 libcurl 库。

## 注意事项

- 最终发送的 HTTP 请求内至少包含两个 Header：Date 和 X-Date 二选一以及 Authorization，可以包含更多 Header。如果使用 Date Header，服务端将不会校验时间；如果使用 X-Date Header，服务端将校验时间。
- Date Header 的值为格林威治时间（GMT）格式的 HTTP 请求构造时间，例如 Fri, 09 Oct 2015 00:00:00 GMT。
- X-Date Header 的值为格林威治时间（GMT）格式的 HTTP 请求构造时间，例如 Mon, 19 Mar 2018 12:08:40 GMT。X-Date Header 里的时间和当前时间的差值不能超过15分钟。
- 如果是微服务 API，Header 中需要添加 “X-NameSpace-Code” 和 “X-MicroService-Name” 两个字段，通用 API 不需要添加，Demo 中默认添加了这两个字段。

## 目录结构

本 Demo 中共包含 7 个文件，目录结构如下：

```plaintext
├─AuthenticationDemo.cpp
├─request.cpp
├─base64.h
├─base64.cpp
├─hmac.h
├─sha1.h
└─sha1.cpp
```

## 编译命令
```plaintext
g++ -o AuthenticationDemo AuthenticationDemo.cpp request.cpp base64.cpp sha1.cpp -lcurl
```
<span id="example"></span>

## 示例代码

#### AuthenticationDemo.cpp

```cpp
/*本Demo中使用libcurl发起http请求,故编译机器需要安装libcurl库*/
/*编译命令 g++ -o AuthenticationDemo AuthenticationDemo.cpp request.cpp base64.cpp sha1.cpp -lcurl*/

#include <iostream>
#include <stdio.h>
#include"hmac.h"
#include"sha1.h"
#include"base64.h"

extern void get_request(const string &defaultDomain, const string &source, const string &dateTime, const string &sign, const string &reqUrl);//具体实现在request.cpp中
extern void post_request(const string &defaultDomain, const string &source, const string &dateTime, const string &sign, const string &reqUrl);//具体实现在request.cpp中

using namespace std;

void GetGmtTime(string &szGmtTime)
{   
    time_t rawTime;    
    struct tm* timeInfo;   
    char szTemp[30]={0};    
    time(&rawTime);   
    timeInfo = gmtime(&rawTime);   
    strftime(szTemp,sizeof(szTemp),"%a, %d %b %Y %H:%M:%S GMT",timeInfo); 
	szGmtTime = szTemp;
}

int calcAuthorization(const string &source, const string &secretId, const string &secretKey,string &sign, string &dateTime)
{
	GetGmtTime(dateTime);
	sign = "x-date: " + dateTime + "\nsource: " + source;
	sign = hmac<SHA1>(sign, secretKey);
	string binDight;
	HexToBin(sign , binDight);
	BinToBase64(binDight , sign);
    char tempauth[1024] = {0};
    snprintf(tempauth,sizeof(tempauth)-1,"hmac id=\"%s\", algorithm=\"hmac-sha1\", headers=\"x-date source\", signature=\"%s\"", secretId.c_str(), sign.c_str());
	sign = tempauth;

    return 0;
}


/*下面代码中secretId,secretKey,defaultDomain,reqUrl根据业务实际情况填写即可*/

int main()
{
    const string secretId = "your secretId";// 密钥对的 SecretId
    const string secretKey = "your secretKey";// 密钥对的 SecretKey
    const string source = "xxxxxx"; // 签名水印值，可填写任意值
    string sign, dateTime;
    calcAuthorization(source, secretId, secretKey, sign, dateTime);
    const string defaultDomain = "service-xxxxxxxx-1234567890.ap-guangzhou.apigateway.myqcloud.com"; // 用户 API 所在服务的域名
    const string reqUrl = "https://service-xxxxxxxx-1234567890.ap-guangzhou.apigateway.myqcloud.com/release/xxapi"; // 用户 API 的访问路径

    get_request(defaultDomain, source, dateTime, sign, reqUrl);
	//post_request(defaultDomain, source, dateTime, sign, reqUrl);

    return 0;
}
```

#### request.cpp

```cpp
#include <iostream>
#include <cstring>
#include "curl/curl.h" 

using namespace std;

size_t req_reply(void *ptr, size_t size, size_t nmemb, void *stream)  
{   
	((std::string*)stream)->append((char*)ptr, size*nmemb);
    return size * nmemb; 
}  

void get_request(const string &defaultDomain, const string &source, const string &dateTime, const string &sign, const string &reqUrl)
{
    CURL* curl = curl_easy_init();
    if (curl)
    {
        curl_easy_setopt(curl, CURLOPT_URL, reqUrl.c_str());
		curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 0L);
        struct curl_slist * slist = NULL;
        slist = curl_slist_append(slist, "Accept:*/*");
        slist = curl_slist_append(slist, "Accept-Charset:utf-8;");
        string headDomain = "Host:" + defaultDomain;
        slist = curl_slist_append(slist, headDomain.c_str());
        string headSource = "Source:" + source;
        slist = curl_slist_append(slist, headSource.c_str());
        string headDatetime = "X-Date:" + dateTime;
        slist = curl_slist_append(slist, headDatetime.c_str());	
        string headAuthorization = "Authorization:" + sign;
        slist = curl_slist_append(slist, headAuthorization.c_str());
        // 如果是微服务 API，Header 中需要添加'X-NameSpace-Code'、'X-MicroService-Name'两个字段，通用 API 不需要添加。
        slist = curl_slist_append(slist, "x-NameSpace-Code:testmic");
        slist = curl_slist_append(slist, "x-MicroService-Name:provider-demo");
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, slist);
        curl_easy_setopt(curl, CURLOPT_CONNECTTIMEOUT, 5); 
        curl_easy_setopt(curl, CURLOPT_TIMEOUT, 5);
        curl_easy_setopt(curl, CURLOPT_READFUNCTION, NULL);
		std::string response_data;        
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response_data);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, req_reply);		   

        CURLcode res = curl_easy_perform(curl);
        if (res != CURLE_OK)
        {
            fprintf(stderr, "curl_easy_perform() failed: %s\n",
            curl_easy_strerror(res));
        }
        else
        {
            // get response code
            long response_code;
            curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &response_code);
            printf("response code %d \n", response_code);
            printf("response data : %s\n ",response_data.c_str());
        }
        curl_slist_free_all(slist);
        curl_easy_cleanup(curl);
    }
    curl_global_cleanup();
}

void post_request(const string &defaultDomain, const string &source, const string &dateTime, const string &sign, const string &reqUrl)
{
	CURL* curl = curl_easy_init();
    if (curl)
    {
        curl_easy_setopt(curl, CURLOPT_URL, reqUrl.c_str());
		curl_easy_setopt(curl, CURLOPT_SSL_VERIFYPEER, 0L);
        curl_easy_setopt(curl, CURLOPT_POST, 1);
        struct curl_slist * slist = NULL;
        slist = curl_slist_append(slist, "Accept:*/*");
        slist = curl_slist_append(slist, "Accept-Charset:utf-8;");
        string headDomain = "Host:" + defaultDomain;
        slist = curl_slist_append(slist, headDomain.c_str());
        string headSource = "Source:" + source;
        slist = curl_slist_append(slist, headSource.c_str());
        string headDatetime = "X-Date:" + dateTime;
        slist = curl_slist_append(slist, headDatetime.c_str());	
        string headAuthorization = "Authorization:" + sign;
        slist = curl_slist_append(slist, headAuthorization.c_str());
        // 如果是微服务 API，Header 中需要添加'X-NameSpace-Code'、'X-MicroService-Name'两个字段，通用 API 不需要添加。
        slist = curl_slist_append(slist, "x-NameSpace-Code:testmic");
        slist = curl_slist_append(slist, "x-MicroService-Name:provider-demo");
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, slist);
		
		 // set body
        std::string body = "{\
            \"title\":\"post title\",\
            \"body\" : \"post body\",\
            \"userId\" : 1}";
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, body.c_str());
		
        curl_easy_setopt(curl, CURLOPT_CONNECTTIMEOUT, 5); 
        curl_easy_setopt(curl, CURLOPT_TIMEOUT, 5);
        curl_easy_setopt(curl, CURLOPT_READFUNCTION, NULL);
		std::string response_data;        
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &response_data);
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, req_reply);		   

        CURLcode res = curl_easy_perform(curl);
        if (res != CURLE_OK)
        {
            fprintf(stderr, "curl_easy_perform() failed: %s\n",
            curl_easy_strerror(res));
        }
        else
        {
            // get response code
            long response_code;
            curl_easy_getinfo(curl, CURLINFO_RESPONSE_CODE, &response_code);
            printf("response code %d \n", response_code);
            printf("response data : %s\n ",response_data.c_str());
        }
        curl_slist_free_all(slist);
        curl_easy_cleanup(curl);
    }
    curl_global_cleanup();
}
```

#### base64.h

```cpp
//Base64编码表
#include<string>
using namespace std;
const  char Base64EncodeMap[64] =
{
	'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
	'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
	'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
	'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
	'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
	'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
	'w', 'x', 'y', 'z', '0', '1', '2', '3',
	'4', '5', '6', '7', '8', '9', '+', '/'
};

int BinToDecInt(string strBin);
void BinToBase64(string binStr , string &base64Str);
void HexToBin(string hexDight , string& binDight);
```

#### base64.cpp

```cpp
#include"base64.h"

int BinToDecInt(string strBin){
              int num = 0;
			  int b = 0;
			  for(int i = 0; i < strBin.length() ;i++){
				  num = num * 2;
				  b = static_cast<int>(strBin[i]-'0');
				  num = num + b;
			  }
			  return num;
		}

void BinToBase64(string binStr , string &base64Str)
{
	while(binStr.length() % 6 != 0){
		binStr = binStr + "0";
	}
	base64Str = "";
	string tmp = "";
	int index = 0;
	int num = 0;
	while(index < binStr.length()){
		tmp = binStr.substr(index , 6);
		index = index + 6;
		num = BinToDecInt(tmp);
		base64Str = base64Str + Base64EncodeMap[num];
	}
	base64Str = base64Str + "=";
}



void HexToBin(string hexDight , string& binDight){
	binDight = "";
	int f = 0,c = 0;
	char e;
	for(int f = 0; f < hexDight.length() ; f++){
		e = hexDight[f];
		if(e >= 'a' && e <= 'f'){
			int a = static_cast<int>(e-'a'+10);
			switch(a){
				case 10 : binDight = binDight + "1010";
					break;
				case 11 : binDight = binDight + "1011";
					break;
				case 12 : binDight = binDight + "1100";
					break;
				case 13 : binDight = binDight + "1101";
					break;
				case 14 : binDight = binDight + "1110";
					break;
				case 15 : binDight = binDight + "1111";
					break;
			}
		}
		else if( e >= '0' && e <= '9'){
			int b = static_cast<int>(e-'0');
			if(f == 0){
			switch(b){
				case 0: binDight = binDight + "0000";
					break;
				case 1: binDight = binDight + "0001";
					break;
				case 2: binDight = binDight + "0010";
					break;
				case 3: binDight = binDight + "0011";
					break;
				case 4: binDight = binDight + "0100";
					break;
				case 5: binDight = binDight + "0101";
					break;
				case 6: binDight = binDight + "0110";
					break;
				case 7: binDight = binDight + "0111";
					break;
				case 8: binDight = binDight + "1000";
					break;
				case 9: binDight = binDight + "1001";
					break;		
			}
			}
			else{
				switch(b){
				case 0 : binDight = binDight + "0000";
						 break;
				case 1: binDight = binDight + "0001";
					break;
				case 2: binDight = binDight + "0010";
					break;
				case 3: binDight = binDight + "0011";
					break;
				case 4: binDight = binDight + "0100";
					break;
				case 5: binDight = binDight + "0101";
					break;
				case 6: binDight = binDight + "0110";
					break;
				case 7: binDight = binDight + "0111";
					break;
				case 8: binDight = binDight + "1000";
					break;
				case 9: binDight = binDight + "1001";
					break;		
				}
			}
		}
	}
}
```

#### hmac.h

```cpp
#pragma once


#include <string>
#include <cstring>

/// compute HMAC hash of data and key using MD5, SHA1 or SHA256
template <typename HashMethod>
std::string hmac(const void* data, size_t numDataBytes, const void* key, size_t numKeyBytes)
{
  unsigned char usedKey[HashMethod::BlockSize] = {0};

  if (numKeyBytes <= HashMethod::BlockSize)
  {
    memcpy(usedKey, key, numKeyBytes);
  }
  else
  {
    HashMethod keyHasher;
    keyHasher.add(key, numKeyBytes);
    keyHasher.getHash(usedKey);
  }

  for (size_t i = 0; i < HashMethod::BlockSize; i++)
    usedKey[i] ^= 0x36;

  unsigned char inside[HashMethod::HashBytes];
  HashMethod insideHasher;
  insideHasher.add(usedKey, HashMethod::BlockSize);
  insideHasher.add(data,    numDataBytes);
  insideHasher.getHash(inside);

  for (size_t i = 0; i < HashMethod::BlockSize; i++)
    usedKey[i] ^= 0x5C ^ 0x36;

  HashMethod finalHasher;
  finalHasher.add(usedKey, HashMethod::BlockSize);
  finalHasher.add(inside,  HashMethod::HashBytes);

  return finalHasher.getHash();
}

template <typename HashMethod>
std::string hmac(const std::string& data, const std::string& key)
{
  return hmac<HashMethod>(data.c_str(), data.size(), key.c_str(), key.size());
}
```

#### sha1.h

```cpp
#pragma once

#include <string>

#ifdef _MSC_VER
// Windows
typedef unsigned __int8  uint8_t;
typedef unsigned __int32 uint32_t;
typedef unsigned __int64 uint64_t;
#else
// GCC
#include <stdint.h>
#endif


class SHA1 //: public Hash
{
public:
  enum { BlockSize = 512 / 8, HashBytes = 20 };

  SHA1();

  std::string operator()(const void* data, size_t numBytes);

  std::string operator()(const std::string& text);

  void add(const void* data, size_t numBytes);

  std::string getHash();

  void getHash(unsigned char buffer[HashBytes]);

  void reset();

private:
  void processBlock(const void* data);

  void processBuffer();

  uint64_t m_numBytes;

  size_t   m_bufferSize;

  uint8_t  m_buffer[BlockSize];

  enum { HashValues = HashBytes / 4 };

  uint32_t m_hash[HashValues];
};
```

#### sha1.cpp

```cpp
#include "sha1.h"

#ifndef _MSC_VER
#include <endian.h>
#endif


SHA1::SHA1()
{
  reset();
}


void SHA1::reset()
{
  m_numBytes   = 0;
  m_bufferSize = 0;

  m_hash[0] = 0x67452301;
  m_hash[1] = 0xefcdab89;
  m_hash[2] = 0x98badcfe;
  m_hash[3] = 0x10325476;
  m_hash[4] = 0xc3d2e1f0;
}


namespace
{
  inline uint32_t f1(uint32_t b, uint32_t c, uint32_t d)
  {
    return d ^ (b & (c ^ d)); 
  }

  inline uint32_t f2(uint32_t b, uint32_t c, uint32_t d)
  {
    return b ^ c ^ d;
  }

  inline uint32_t f3(uint32_t b, uint32_t c, uint32_t d)
  {
    return (b & c) | (b & d) | (c & d);
  }

  inline uint32_t rotate(uint32_t a, uint32_t c)
  {
    return (a << c) | (a >> (32 - c));
  }

  inline uint32_t swap(uint32_t x)
  {
#if defined(__GNUC__) || defined(__clang__)
    return __builtin_bswap32(x);
#endif
#ifdef MSC_VER
    return _byteswap_ulong(x);
#endif

    return (x >> 24) |
          ((x >>  8) & 0x0000FF00) |
          ((x <<  8) & 0x00FF0000) |
           (x << 24);
  }
}

void SHA1::processBlock(const void* data)
{
  uint32_t a = m_hash[0];
  uint32_t b = m_hash[1];
  uint32_t c = m_hash[2];
  uint32_t d = m_hash[3];
  uint32_t e = m_hash[4];

  const uint32_t* input = (uint32_t*) data;

  uint32_t words[80];
  for (int i = 0; i < 16; i++)
#if defined(__BYTE_ORDER) && (__BYTE_ORDER != 0) && (__BYTE_ORDER == __BIG_ENDIAN)
    words[i] = input[i];
#else
    words[i] = swap(input[i]);
#endif

  for (int i = 16; i < 80; i++)
    words[i] = rotate(words[i-3] ^ words[i-8] ^ words[i-14] ^ words[i-16], 1);

  for (int i = 0; i < 4; i++)
  {
    int offset = 5*i;
    e += rotate(a,5) + f1(b,c,d) + words[offset  ] + 0x5a827999; b = rotate(b,30);
    d += rotate(e,5) + f1(a,b,c) + words[offset+1] + 0x5a827999; a = rotate(a,30);
    c += rotate(d,5) + f1(e,a,b) + words[offset+2] + 0x5a827999; e = rotate(e,30);
    b += rotate(c,5) + f1(d,e,a) + words[offset+3] + 0x5a827999; d = rotate(d,30);
    a += rotate(b,5) + f1(c,d,e) + words[offset+4] + 0x5a827999; c = rotate(c,30);
  }

  for (int i = 4; i < 8; i++)
  {
    int offset = 5*i;
    e += rotate(a,5) + f2(b,c,d) + words[offset  ] + 0x6ed9eba1; b = rotate(b,30);
    d += rotate(e,5) + f2(a,b,c) + words[offset+1] + 0x6ed9eba1; a = rotate(a,30);
    c += rotate(d,5) + f2(e,a,b) + words[offset+2] + 0x6ed9eba1; e = rotate(e,30);
    b += rotate(c,5) + f2(d,e,a) + words[offset+3] + 0x6ed9eba1; d = rotate(d,30);
    a += rotate(b,5) + f2(c,d,e) + words[offset+4] + 0x6ed9eba1; c = rotate(c,30);
  }

  for (int i = 8; i < 12; i++)
  {
    int offset = 5*i;
    e += rotate(a,5) + f3(b,c,d) + words[offset  ] + 0x8f1bbcdc; b = rotate(b,30);
    d += rotate(e,5) + f3(a,b,c) + words[offset+1] + 0x8f1bbcdc; a = rotate(a,30);
    c += rotate(d,5) + f3(e,a,b) + words[offset+2] + 0x8f1bbcdc; e = rotate(e,30);
    b += rotate(c,5) + f3(d,e,a) + words[offset+3] + 0x8f1bbcdc; d = rotate(d,30);
    a += rotate(b,5) + f3(c,d,e) + words[offset+4] + 0x8f1bbcdc; c = rotate(c,30);
  }

  for (int i = 12; i < 16; i++)
  {
    int offset = 5*i;
    e += rotate(a,5) + f2(b,c,d) + words[offset  ] + 0xca62c1d6; b = rotate(b,30);
    d += rotate(e,5) + f2(a,b,c) + words[offset+1] + 0xca62c1d6; a = rotate(a,30);
    c += rotate(d,5) + f2(e,a,b) + words[offset+2] + 0xca62c1d6; e = rotate(e,30);
    b += rotate(c,5) + f2(d,e,a) + words[offset+3] + 0xca62c1d6; d = rotate(d,30);
    a += rotate(b,5) + f2(c,d,e) + words[offset+4] + 0xca62c1d6; c = rotate(c,30);
  }

  m_hash[0] += a;
  m_hash[1] += b;
  m_hash[2] += c;
  m_hash[3] += d;
  m_hash[4] += e;
}

void SHA1::add(const void* data, size_t numBytes)
{
  const uint8_t* current = (const uint8_t*) data;

  if (m_bufferSize > 0)
  {
    while (numBytes > 0 && m_bufferSize < BlockSize)
    {
      m_buffer[m_bufferSize++] = *current++;
      numBytes--;
    }
  }

  if (m_bufferSize == BlockSize)
  {
    processBlock((void*)m_buffer);
    m_numBytes  += BlockSize;
    m_bufferSize = 0;
  }

  if (numBytes == 0)
    return;

  while (numBytes >= BlockSize)
  {
    processBlock(current);
    current    += BlockSize;
    m_numBytes += BlockSize;
    numBytes   -= BlockSize;
  }

  while (numBytes > 0)
  {
    m_buffer[m_bufferSize++] = *current++;
    numBytes--;
  }
}


void SHA1::processBuffer()
{
  size_t paddedLength = m_bufferSize * 8;

  paddedLength++;

  size_t lower11Bits = paddedLength & 511;
  if (lower11Bits <= 448)
    paddedLength +=       448 - lower11Bits;
  else
    paddedLength += 512 + 448 - lower11Bits;

  paddedLength /= 8;

  unsigned char extra[BlockSize];

  if (m_bufferSize < BlockSize)
    m_buffer[m_bufferSize] = 128;
  else
    extra[0] = 128;

  size_t i;
  for (i = m_bufferSize + 1; i < BlockSize; i++)
    m_buffer[i] = 0;
  for (; i < paddedLength; i++)
    extra[i - BlockSize] = 0;

  uint64_t msgBits = 8 * (m_numBytes + m_bufferSize);

  unsigned char* addLength;
  if (paddedLength < BlockSize)
    addLength = m_buffer + paddedLength;
  else
    addLength = extra + paddedLength - BlockSize;

  *addLength++ = (unsigned char)((msgBits >> 56) & 0xFF);
  *addLength++ = (unsigned char)((msgBits >> 48) & 0xFF);
  *addLength++ = (unsigned char)((msgBits >> 40) & 0xFF);
  *addLength++ = (unsigned char)((msgBits >> 32) & 0xFF);
  *addLength++ = (unsigned char)((msgBits >> 24) & 0xFF);
  *addLength++ = (unsigned char)((msgBits >> 16) & 0xFF);
  *addLength++ = (unsigned char)((msgBits >>  8) & 0xFF);
  *addLength   = (unsigned char)( msgBits        & 0xFF);

  processBlock(m_buffer);
  
  if (paddedLength > BlockSize)
    processBlock(extra);
}

std::string SHA1::getHash()
{
  unsigned char rawHash[HashBytes];
  getHash(rawHash);

  std::string result;
  result.reserve(2 * HashBytes);
  for (int i = 0; i < HashBytes; i++)
  {
    static const char dec2hex[16+1] = "0123456789abcdef";
    result += dec2hex[(rawHash[i] >> 4) & 15];
    result += dec2hex[ rawHash[i]       & 15];
  }

  return result;
}


void SHA1::getHash(unsigned char buffer[SHA1::HashBytes])
{
  uint32_t oldHash[HashValues];
  for (int i = 0; i < HashValues; i++)
    oldHash[i] = m_hash[i];

  processBuffer();

  unsigned char* current = buffer;
  for (int i = 0; i < HashValues; i++)
  {
    *current++ = (m_hash[i] >> 24) & 0xFF;
    *current++ = (m_hash[i] >> 16) & 0xFF;
    *current++ = (m_hash[i] >>  8) & 0xFF;
    *current++ =  m_hash[i]        & 0xFF;

    m_hash[i] = oldHash[i];
  }
}

std::string SHA1::operator()(const void* data, size_t numBytes)
{
  reset();
  add(data, numBytes);
  return getHash();
}

std::string SHA1::operator()(const std::string& text)
{
  reset();
  add(text.c_str(), text.size());
  return getHash();
}
```
