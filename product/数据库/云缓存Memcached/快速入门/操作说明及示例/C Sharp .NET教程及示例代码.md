本文介绍两种 C# 客户端的使用方法 [.NET memcached client library](http://sourceforge.net/projects/memcacheddotnet/) 和 [EnyimMemcached](https://github.com/enyim/EnyimMemcached)。

## 使用 .NET memcached client library
**环境和依赖**
下载并解压 memcacheddotnet_clientlib-1.1.5.zip。

拷贝 memcached\trunk\clientlib\src\clientlib\bin\2.0\Release 目录下的四个 dll 文件到 .NET 工程，并保持其在同一目录下。

在 .NET 工程中引用 Memcached.ClientLibrary.dll。

**代码示例 .NET memcached client library**
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
            string[] serverlist = { "***.***.***.***:****" };//服务器可以是多个, server的构成形式是IP:PORT（如：127.0.0.1:11211）  

            //初始化池  
            SockIOPool pool = SockIOPool.GetInstance();
            pool.SetServers(serverlist);//设置连接池可用的cache服务器列表
            pool.InitConnections = 3;//初始连接数  
            pool.MinConnections = 3;//最小连接数  
            pool.MaxConnections = 5;//最大连接数  
            pool.SocketConnectTimeout = 1000;//设置连接的套接字超时  
            pool.SocketTimeout = 3000;//设置套接字超时读取  
            pool.MaintenanceSleep = 30;//设置维护线程运行的睡眠时间。如果设置为0，那么维护线程将不会启动,30就是每隔30秒醒来一次  

            //获取或设置池的故障标志。  
            //如果这个标志被设置为true则socket连接失败，将试图从另一台服务器返回一个套接字如果存在的话  
            //如果设置为false，则得到一个套接字如果存在的话。否则返回NULL，如果它无法连接到请求的服务器  
            pool.Failover = true;

            pool.Nagle = false;//如果为false，对所有创建的套接字关闭Nagle的算法  
            pool.Initialize();

            // 获得客户端实例  
            MemcachedClient mc = new MemcachedClient();
            mc.EnableCompression = false;

            mc.Set("cSharp_key", "cSharp_value");  //存储数据到缓存服务器，这里将字符串"cSharp_value"缓存，key 是"cSharp_key"  

            if (mc.KeyExists("cSharp_key"))   //测试缓存存在key为test的项目  
            {
                Console.WriteLine("cSharp_key is Exists");
                Console.WriteLine(mc.Get("test").ToString());  //在缓存中获取key为cSharp_key的项目  
            }
            else
            {
                Console.WriteLine("cSharp_key not Exists");
            }


            mc.Delete("cSharp_key");  //移除缓存中key为test的项目  

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

            SockIOPool.GetInstance().Shutdown();  //关闭池， 关闭sockets  
        }
    }
}
```

## 使用 EnyimMemcached
**环境和依赖**

下载后先修改 build\CommonProperties.targets 文件，注释掉其中的程序集签名选项，避免调用 dll 时编译不通过的问题。

使用 Visual Studio 直接打开解决方案，总共六个项目，只需右键选中 Enyim.Caching 项目单独生成 dll 即可（生成的 dll 文件名为 Enyim.Caching.dll，最好为 Release 版）。

新建 .Net 客户端项目，并在项目中引用之前生成的dll文件。

编写测试代码并运行。

**代码示例 EnyimMemcached**

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
            IPAddress ip = IPAddress.Parse(Dns.GetHostEntry("***.***.***.***").AddressList[0].ToString());//***.***.***.***为cmem控制台列表中的ip地址
            config.Servers.Add(new IPEndPoint(ip, ****));//****为cmem控制台列表中的端口
            config.Protocol = MemcachedProtocol.Binary;//使用二进制协议
            memConfig.SocketPool.MinPoolSize = 5;//连接池最小连接数
            memConfig.SocketPool.MaxPoolSize = 200;//连接池最大连接数

            var mc = new MemcachedClient(config);

            //向cmem写入数据
            mc.Store(StoreMode.Set, "csharp_key", "csharp_value");

            //从cmem读取一条数据
            Console.WriteLine(mc.Get("csharp_key"));

            //从cmem读取多条数据 only 1.2.4 supports it (Windows version is at 1.2.1)
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

