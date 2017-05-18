As the e-commerce system architecture develops, problems may emerge as a result of differences. For example, if the order system (order_module) is built from Java, the inventory system (inventory_module) is built from Erlang, and the shipping system employs the Python architecture, the traditional solutions need developers to always maintain some redundant codes to convert the incoming HTTP requests from modules into function calls in the application. When the Tencent Cloud CMQ service is employed:

- The differences between platforms and between programming languages can be masked. CMQ provides standard Restful API access, which makes it extremely simple to exchange data between systems
- SDKs of C++, C#, PHP, Golang, Python and other mainstream languages are provided. You can easily use Tencent Cloud CMQ by installing an SDK

![](//mccdn.qcloud.com/static/img/e9e128dbd0b7e6fe297b1d32e7b72960/image.png)
