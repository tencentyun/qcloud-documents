## WeChat and Mobile Terminal APPs

Tom developed a car service APP, and users can book car service via WeChat and the mobile APP. Tom needs a storage space to store the driving licenses information uploaded by users for approval, photos of local car service providers' stores and photos uploaded for user evaluation. These pictures are about 100 GB in size, and the traffic for browsing them is 100 GB per month. Therefore, Tom hosts the application on CVM, stores files in COS-Standard Storage, and uses CDN acceleration service at the same time.

Storage fee = (100 GB - 50 GB) × 0.13 = 6.5 CNY

Traffic fee = (100 GB -10 GB) × (0.15 × (1-60%) + 0.34) = 36 CNY

Here, the price of CDN back-to-origin traffic is 0.15 CNY/GB, the price of CDN accelerated traffic is 0.34 CNY/GB, and the reuse rate of CDN cache is 60%. In fact, the cost of back-to-origin traffic can be reduced through reasonable CDN configuration.

Request fee = 0 CNY

Tencent Cloud will provide you with 1,000,000 fee-free read requests and 100,000 fee-free write requests.

In this case, Tom's monthly cost: standard storage fee 6.5 CNY + traffic fee 36 CNY + request fee 0 CNY = 42.5 CNY

## Websites and Forums

Tom operates a website, on which articles containing pictures, audios and videos are published and software can be downloaded. These files are 1.5 TB in size, the traffic for them is 500 GB per month, and the monthly PV is about 2 million. Therefore, Tom hosts the website on CVM, stores files in COS-Standard Storage, and uses CDN acceleration service at the same time.

Storage fee = (1,500 GB - 50 GB) × 0.13 = 188.5 CNY

Traffic fee = (500 GB -10 GB) × (0.15 × (1-80%) + 0.34) = 181.3 CNY

Here, the price of CDN back-to-origin traffic is 0.15 CNY/GB, the price of CDN accelerated traffic is 0.34 CNY/GB, and the reuse rate of CDN cache is 80%. In fact, the cost of back-to-origin traffic can be reduced through reasonable CDN configuration.

Request fee= (5,000,000 - 1,000,000) × 0.01 + (200,000 - 100,000) × 0.1 = 5 CNY

It is estimated that there are 5,000,000 read requests and 200,000 write requests, among which 1,000,000 read requests and 100,000 write requests are free.

In this case, Tom's monthly fee: standard storage fee 188.5 CNY + traffic fee 181.3 CNY + request fee 5 CNY = 374.8 CNY

## Massive Data Backup

Tom manages a hospital, of which substantial medical records and image materials need storage and backup. These files are 20 TB in size and are growing continuously. The traffic for extracting data from information system of the hospital is about 1 TB per month, and the daily received patients are 10,000. Therefore, Tom stores the files in COS-Infrequent Access Storage, and uses CDN acceleration service at the same time.

Storage fee = 20,000 GB  × 0.1 = 2,000 CNY

Traffic fee = 1,000 GB  × (0.15 × (1-20%) + 0.34) = 460 CNY

Data read fee = 1,000 GB × (1-20%) × 0.02 = 16 CNY

Here, the price of CDN back-to-origin traffic is 0.15 CNY/GB, the price of CDN accelerated traffic is 0.34 CNY/GB, and the reuse rate of CDN cache is 20%. In fact, the cost of back-to-origin traffic can be reduced through reasonable CDN configuration.

Request fee= 1,000,000 × 0.05 + 500,000 × 0.5 = 30 CNY

It is estimated that there are 1,000,000 read requests and 500,000 write requests.

In this case, Tom's monthly cost: storage fee 2,000 CNY + traffic fee 460 CNY + data read fee 16 CNY + request fee 30 CNY = 2,506 CNY


## Video Data Archiving

Tom operates a film and television company with substantial video and audio files to be archived. These files are 1 PB in size, and the monthly extracted video files are about 1 GB in size. Therefore, Tom stores the files in COD-Nearline Storage.

Storage fee = 1,000,000 GB × 0.06 = 60,000 CNY

Traffic fee = 1 GB × 0.64 = 0.64 CNY

Data read fee= 1 GB × 0.06 = 0.06 CNY

Request fee= 1/10,000 × 0.06 + 100,000 × 0.6 = 6 CNY

It is estimated that there is a read request and 1,000,000 write requests.

In this case, Tom's monthly cost: storage fee 60,000 CNY + traffic fee 0.64 CNY + data read fee 0.06 CNY + request fee 6 CNY = about 60,000 CNY


## Price Calculator

You can use [Price Calculator](https://buy.cloud.tencent.com/calculator/cdn) for a rapid price estimation.

![](https://mc.qcloudimg.com/static/img/3e0c746f012f8ab31ee4ef8e9b854206/Free-Converter.com-qq20161104-1-8511018.jpg)

If this document still can not help you, welcome to consult customized schemes and get more technical support by submitting a ticket, seek help from the key customer manager and negotiate price.




