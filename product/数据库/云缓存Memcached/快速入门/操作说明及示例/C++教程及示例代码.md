## 环境及依赖
[下载 libmemcached](https://launchpad.net/libmemcached/1.0/1.0.18/+download/libmemcached-1.0.18.tar.gz)。

安装 libmemcached 客户端。

将 libmemcached.so 文件所在目录加入到变量 LD_LIBRARY_PATH 中，不同系统路径可能不一样，请查看自己的安装目录并替换。

```
tar -xvf libmemcached-1.0.18.tar.gz 
cd libmemcached-1.0.18 
./configure 
sudo make 
sudo make install
#配置path
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
```

## 使用步骤
编写测试代码 memcachedDemo.cpp。
```
编写测试代码 memcachedDemo.cpp
#include<iostream>
#include <string.h>
#include <libmemcached/memcached.h>

using namespace std;

int main(int argc, char *argv[])
{
memcached_st *client = NULL;
memcached_return cache_return;
memcached_server_st *server = NULL;

client = memcached_create(NULL);
server = memcached_server_list_append(server, "***.***.***.***", ****, &cache_return);//管理中心，单击“NoSQL高速存储”，在NoSQL高速存储“管理视图”，可以看到系统分配的IP:Port
cache_return = memcached_server_push(client, server);

if(MEMCACHED_SUCCESS != cache_return){
cout<<"memcached server push failed! cache return:"<<cache_return<<endl;
return -1;
}

string key = "cpp_key";
string val = "cpp_value";
size_t key_len = key.length();
size_t val_len = val.length();
int expiration = 0;
uint32_t flags = 0;
cache_return = memcached_set(client, key.c_str(), key_len, val.c_str(), val_len, expiration, flags);
if(MEMCACHED_SUCCESS === cache_return){
cout<<"set success"<<endl;
}else{
cout<<"set failed! cache return:"<<cache_return<<endl;
}

size_t value_length;
char* getVal = memcached_get(client, key.c_str(), key_len, &value_length, &flags, &cache_return);
if(MEMCACHED_SUCCESS === cache_return){
cout<<"get success, value = "<<getVal<<endl;
}else{
cout<<"get failed, cache return:"<<cache_return<<endl;
}
return 0;
}
编译
g++ -g -Wall -std=c++0x memcachedDemo.cpp -lmemcached -lpthread -o memcached
运行
./memcached
set success
get success, value = cpp_value
```
