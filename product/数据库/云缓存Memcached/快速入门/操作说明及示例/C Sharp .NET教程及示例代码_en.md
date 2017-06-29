This document describes two methods for using C# client: [[.NET memcached client library](http://sourceforge.net/projects/memcacheddotnet/)] and [[EnyimMemcached](https://github.com/enyim/EnyimMemcached)].

## 1. Use .NET memcached client library

**Environment and dependency**

Download and decompress memcacheddotnet_clientlib-1.1.5.zip;

Copy four dll files under the directory memcached\trunk\clientlib\src\clientlib\bin\2.0\Release to .NET project under the same directory;

Reference Memcached.ClientLibrary.dll in .Net project.

**Sample code: .NET memcached client library**


```
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

using Memcached.ClientLibrary;

namespace TestMemcachedApp
{
    class Program
    {
        [STAThread]
        public static void Main(String[] args)
        {
            string[] serverlist = { "***.***.***.***:****" };//Multiple servers can be used. The format of server is IP:PORT (e.g.: 127.0.0.1:11211)  

            //Initialize the pool  
            SockIOPool pool = SockIOPool.GetInstance();
            pool.SetServers(serverlist);//Set the list of cache servers available for the connection pool
            pool.InitConnections = 3;//Initial number of connections  
            pool.MinConnections = 3;//Minimum number of connections  
            pool.MaxConnections = 5;//Maximum number of connections  
            pool.SocketConnectTimeout = 1000;//Set the socket connection timeout  
            pool.SocketTimeout = 3000;//Set the socket read timeout  
            pool.MaintenanceSleep = 30;//Set the sleep time of maintenance thread. If it is 0, the maintenance thread will not launch. 30 means the maintenance thread wakes up every 30 seconds.

            //Obtain or set the fault flag of the pool.
            //If this flag is set to true, the socket connection is failed, and a socket (if available) will be returned from another server.
            //If it is set to false, you will obtain a socket (if available). If the socket cannot be connected to the requested server, NULL is returned.
            pool.Failover = true;

            pool.Nagle = false;//If it is set to false, disable Nagle algorithm for all the created sockets  
            pool.Initialize();

            // Obtain client instance  
            MemcachedClient mc = new MemcachedClient();
            mc.EnableCompression = false;

            mc.Set("cSharp_key", "cSharp_value");  //Store data onto the cache server. The string "cSharp_value" is cached here, and key is "cSharp_key"  

            if (mc.KeyExists("cSharp_key"))   //The test cache has a project with key being test  
            {
                Console.WriteLine("cSharp_key is Exists");
                Console.WriteLine(mc.Get("test").ToString());  //Obtain the project with key being cSharp_key from the cache  
            }
            else
            {
                Console.WriteLine("cSharp_key not Exists");
            }


            mc.Delete("cSharp_key");  //Remove the project with key being test from the cache  

            if (mc.KeyExists("cSharp_key"))
            {
                Console.WriteLine("cSharp_key is Exists");
                Console.WriteLine(mc.Get("cSharp_key").ToString());
            }
            else
            {
                Console.WriteLine("cSharp_key not Exists");
            }
            Console.ReadLine();

            SockIOPool.GetInstance().Shutdown();  //Shutdown the pool and sockets  
        }
    }
}
```

## 2. Use EnyimMemcached

**Environment and dependency**

Download and modify the file build\CommonProperties.targets. Comment out the program set signature option, to avoid the problem where compile would fail when dll is called.

Directly open the solution by using Visual Studio. There are 6 projects in total, and you just need to right-click Enyim.Caching to generate a dll file (the name of the generated dll file is Enyim.Caching.dll, and it is recommended to use Release version);

Create a .Net client project, and reference the dll file generated above in the project.

Write the test code and run.

**Sample code: EnyimMemcached**

```
using System;
using System.Net;
using Enyim.Caching;
using Enyim.Caching.Configuration;
using Enyim.Caching.Memcached;

namespace DemoApp
{
    class Program
    {
        static void Main(string[] args)
        {
            MemcachedClientConfiguration config = new MemcachedClientConfiguration();
            IPAddress ip = IPAddress.Parse(Dns.GetHostEntry("***.***.***.***").AddressList[0].ToString());//***.***.***.*** is the IP in the cmem console list
            config.Servers.Add(new IPEndPoint(ip, ****));//**** is the port in the cmem console list
            config.Protocol = MemcachedProtocol.Binary;//Binary protocol is used
            memConfig.SocketPool.MinPoolSize = 5;//Minimum number of connections of the connection pool
            memConfig.SocketPool.MaxPoolSize = 200;//Maximum number of connections of the connection pool

            var mc = new MemcachedClient(config);

            //Write data into cmem
            mc.Store(StoreMode.Set, "csharp_key", "csharp_value");

            //Read an data entry from cmem
            Console.WriteLine(mc.Get("csharp_key"));

            //Read multiple data entries from cmem; only 1.2.4 supports it (windows version is at 1.2.1)
            List<string> keys = new List<string>();

            for (int i = 1; i < 100; i++)
            {
               string k = "aaaa" + i + "--" + (i * 2);
               keys.Add(k);

                mc.Store(StoreMode.Set, k, i);
            }

            IDictionary<string, ulong> cas;
            IDictionary<string, object> retvals = mc.Get(keys, out cas);
        }
    }
}
```
