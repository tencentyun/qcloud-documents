## 1. Environment and dependency

Download libmemcached. [[libmemcached-1.0.18.tar.gz](https://launchpad.net/libmemcached/1.0/1.0.18/+download/libmemcached-1.0.18.tar.gz)].

Install libmemcached client.

Add the directory of the file libmemcached.so into the variable LD_LIBRARY_PATH. Path may vary in different systems, please check your installation directory and replace.

# Install

```
tar -xvf libmemcached-1.0.18.tar.gz 
cd libmemcached-1.0.18 
./configure 
sudo make 
sudo make install
# Configure path
export LD_LIBRARY_PATH=/usr/local/lib:$LD_LIBRARY_PATH
```
## 2. Steps

Write the test code memcachedDemo.cpp.

```
Write the test code memcachedDemo.cpp.
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
server = memcached_server_list_append(server, "***.***.***.***", ****, &cache_return);//In the console, click "NoSQL Fast Storage", and you can see IP:Port assigned by the system in "Management View".
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
Compile
g++ -g -Wall -std=c++0x memcachedDemo.cpp -lmemcached -lpthread -o memcached
Run
./memcached
set success
get success, value = cpp_value
```
