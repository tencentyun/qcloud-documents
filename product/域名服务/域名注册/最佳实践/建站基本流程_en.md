For a new developer, you can follow the 5 steps listed below to build a simple website (all steps are required without a certain sequence):
![](//mc.qcloudimg.com/static/img/56e6e903622c3aaa851f1072d629c2d1/image.png)
### Register/Transfer Domain Name
Domain name registration is basic for establishing any service on the Internet. A domain name is required before you build a website.
 - If you have owned a domain name at another registrar, you can [Transfer Domain Name to Tencent Cloud](https://console.cloud.tencent.com/domain/trans-in?from=qcloudHpHeaderDnspod);
 - If you don't have a domain name, you need to [Register Domain Name](https://buy.cloud.tencent.com/domain).

It's suggested to use simple English letters you like which are also related to the nature of your website and easy to be memorized. If you're planning for a Chinese website, you can use Chinese pinyin as domain name (such as `baidu.com`) so it's easier to promote the website and leave an impression on visitors.
Open [Tencent Cloud Official Website](https://cloud.tencent.com/), from the top navigation bar, click "Cloud Product" -> "Domain Name Service" -> "Domain Name Registration". Then query the domain name you want to purchase, select the usage period and complete the payment to acquire your domain name.
>Note: According to regulations of the registry, for domain names with the suffixes ".com/.cn/.net/.xyz/.club/.info/.mobi/.中国", identity verification must be completed in 5 work days after registration, or they will be put into "Serverhold" status and cannot be used.

### Domain Name ICP Licensing
According to regulations of MIIT, websites that haven't acquired permission or haven't completed ICP licensing procedures cannot engage in any Internet information services (or it is considered as illegal act). To not affect the running of your website, it is suggested to complete website ICP licensing first. After the communication administration distributes the ICP license number to you, your website will be activated for visit. If your domain name is not licensed by ICP, complete [Domain Name ICP Licensing](https://console.cloud.tencent.com/beian).
Log in to [Tencent Cloud Official Website](https://cloud.tencent.com/). From the upper-right corner, click "Console" to enter the console, then click "ICP License" on the upper-right corner to go to the "Domain Name ICP Licensing" page and apply for ICP license for your purchased domain name. For information on the steps of this operation, please see [Illustration on Domain Name ICP Licensing](https://cloud.tencent.com/document/product/243/655).

### Purchase Cloud Virtual Machine
You need a place on the Internet where you can store the information of your website. Thus, you should [Purchase CVM](https://cloud.tencent.com/product/cvm).
Tencent Cloud Virtual Machines (CVM) are safe and can be flexibly configured, which are more than enough for you to build a personal blog or small website. If you have efficient budget, it is recommended to prioritize CVM performance according to your actual demand. For example, select CVM with good memory and CPU if you need high computing capacity, or select those with good bandwidth and memory if you need high access capacity.
Open [Tencent Cloud Official Website](https://cloud.tencent.com/). From the top navigation bar, open "Cloud Product" -> "Basic Products" -> "Computing" -> "Cloud Virtual Machine". Click "Buy Now" to open the CVM purchase page and select the CVM model which suits your website best.
**1. Select region and model:** Select the region which is the nearest to your customers so they can access your website quickly.
 - CPU -- This represents the computing capacity of the CVM. It is recommended to select a CPU with 2 cores or more if your website expects a lot of traffic and contains many dynamic pages.
 - Memory -- Select this according to the size of your website. You can use smaller memory for common personal blog or enterprise presentation website. You can also use larger memory for websites such as online stores or news websites.
 
**2. Select image:** The basic environment provided by Tencent Cloud contains necessary operating system and initialized components. You can configure application environment and relevant softwares on your own.
**3. Select storage and network:** Select a suitable disk size and network bandwidth for your CVM.
 - Disk: This depends on the data amount of your website. You should consider the space to be remained when selecting this. In addition, the I/O speed of a disk determines the speed for reading files.
 - Bandwidth: Select a suitable bandwidth according to the nature of your website. Common textual websites, image websites or forums require very little bandwidth, in which case 2 MB is enough basically. While websites that are mainly used for video watching or download may require a bandwidth of 10 MB or more.
 
**4. Configure information:** Configure the CVM name, user name and password for your CVM.
Finally, submit the order to complete the purchase process.

### Build a Website
Since the preparation work is done, you only need to build a simple website on your purchased CVM to get your very own website on the Internet.
If you want to build a WordPress blog platform, please see [Building a WordPress Site](https://cloud.tencent.com/document/product/213/8044);
If you want to build a Discuz forum platform, please see [Building a Discuz Forum](https://cloud.tencent.com/document/product/213/8043);
If you want to build a website for mobile devices, please see [Sohu Fast Website](https://www.kuaizhan.com/?utm_source=qcloud&utm_term=A).

### Domain Name Resolution
Domain name resolution is a necessary step to allow your website to be accessed by its domain name. You can select Tencent Cloud DNSPod resolution to ensure that your website enjoys a stable, fast and secure resolution service. To access your website using the purchased domain name, you need to configure [Domain Name Resolution](https://console.cloud.tencent.com/cns/domains).
Open [Tencent Cloud Official Website](https://cloud.tencent.com/). From the top navigation bar, click "Console" to enter the cloud product console. Here, click "Domain Name Management" to go to the domain name list. Click "Resolution" in the **Action** bar of the corresponding domain name and add resolution record to finish domain name resolution configuration. For more information on the steps of this operation, please see [Quickly Add Domain Name Resolution](https://cloud.tencent.com/document/product/302/3446).
After completing the steps above, open your browser and access your domain name to browse your website.

