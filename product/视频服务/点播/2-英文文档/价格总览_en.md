## Billing Type

Tencent Cloud VOD now supports Pay-by-Usage (Postpaid) billing method.

Pay-by-Usage means you can pay for the service after use. You need to top up your Tencent Cloud account in advance. Every day, the system calculates the actual usage of the previous day, sends bill, settles account, and deducts fees from your account balance based on actual usage.

Now, the billing type described below is only effective in Mainland China. Consult our customer service for overseas businesses.

## Billing Method

Tencent Cloud VOD product is billed based on the following three parts:

- Video storage: Source video files uploaded to Tencent Cloud VOD service and transcoded video files take up storage space, which are charged based on the storage capacity.

- Video transcoding: Transcoding of source video files stored in Tencent Cloud VOD service is charged based on the specification and duration of target files.

- Video acceleration: Fees generated when CDN is used for acceleration during video playback are charged based on the downstream traffic.

You can check the actual usage of Tencent Cloud VOD on the console.

### Video Storage

1、 Billing item: Fees for VOD storage and public network downstream traffic (that is, the downstream traffic directly generated when videos are pulled from the origin server of VOD storage)

2、 Price:

- Storage space: 0.008 CNY/GB/day

- Public network downstream traffic: 0.5 CNY/GB

3、 Billing description:

- Billing method: Postpaid

- Billing rule: Charged based on the actual usage. The fees for a day are charged based on the day's peak storage capacity.

- Billing cycle: Charged on a daily basis. Fees generated in the previous day are billed and deducted between 12:00 and 18:00 of the next day, during which bills are also generated.

- Billing formula:

<pre><code>Daily storage fee = Peak storage capacity (GB) x 0.008 CNY/GB/day

Daily public network downstream traffic fee = Public network traffic (GB) x 0.5 CNY/GB</code></pre>



4、 Billing examples:

- For example, if you use VOD storage service on January 1 with a peak storage capacity of 100 GB and pull 10 GB traffic directly from the origin server, the VOD storage fee you need to pay on January 2 is calculated as follows:

<pre><code>VOD storage fee for January 1 = Storage fee for January 1 + Public network downstream traffic fee for January 1 = 100 (GB) x 0.008 CNY/GB + 10 (GB) x 0.5 CNY/GB=5.8 CNY</code></pre>

### Video Transcoding

1、 Billing item: VOD transcoding processing time

2、 Price:

| Encoding Method    | Resolution                            |  Unit Price (CNY/minute) |
| ---------  |:--------------------------------:| ---------------:|
| H.264      | 4K (3840 x 2160) and below           | 0.28           |
| H.264      | 2K (2560 x 1440) and below           | 0.14           |
| H.264      | FHD (1920 x 1080) and below     | 0.065          |
| H.264      | HD (1280 x 720) and below        | 0.033          |
| H.264      | SD (640 x 480) and below         | 0.022          |
| H.265      | 4K (3840 x 2160) and below            | 1.4            |
| H.265      | 2K (2560 x 1440) and below            | 0.7            |
| H.265      | FHD (1920 x 1080) and below      | 0.326          |
| H.265      | HD (1280 x 720) and below         | 0.163          |
| H.265      | SD (640 x 480) and below          | 0.109          |

> Note: H.265 transcoding is unavailable by default. Contact us by submitting a ticket if needed.

3、 Billing description:

- Billing method: Postpaid

- Billing rule: Charged on a daily basis according to the requested encoding mode, resolution and the length of the transcoded output file.

- Billing cycle: Charged on a daily basis. Fees generated in the previous day are billed and deducted between 12:00 and 18:00 of the next day, during which bills are also generated.

- Billing formula:

<pre><code>Daily video transcoding fee = Length of transcoded output file (in min) x Transcoding unit price for videos with different encoding methods and resolutions (CNY/min)</code></pre>

4、 Billing examples:

- For example, if you use VOD transcoding service on January 1 and transcode a video with resolution of 2560 x 1440 and a length of 1 hour as well as a video with resolution of 1280 x 960 and a length of 100 minutes using H.264 encoding method, the VOD storage fee you need to pay on January 2 is calculated as follows:

<pre><code>VOD transcoding fee for January 1 = 0.14 (CNY/min) x 60 (minutes) + 0.065 (CNY/min) x 100 (minutes) = 14.9 CNY</code></pre>


### Video Acceleration

1、 Billing item: Downstream traffic of VOD acceleration

2、 Price:

Tencent VOD traffic is billed based on a daily tiered pricing model. The more traffic you use in each day, the lower the billing tier you will get. Detailed tiered unit price is as follows:

| Traffic Tier         | Unit Price (CNY/GB/day)  |
| ----------      |:----------------:|
| 0 GB-50 GB (inclusive)   | 0.29             |
| 50 GB-500 GB (inclusive)   | 0.27             |
| 500 GB-1 TB (inclusive)   | 0.26             |
| 1 TB-5 TB (inclusive)     | 0.24             |
| Above 5 TB          | 0.23             |

3、 Billing description:

- Billing method: Postpaid

- Billing rule: Charged on a daily basis based on the downstream traffic generated when CDN is used for acceleration during video playback.

- Billing cycle: Charged on a daily basis. Fees generated in the previous day are billed and deducted between 12:00 and 18:00 pm of the next day, during which bills are also generated.

- Billing formula:

<pre><code>Daily video traffic fee = Video playback downstream traffic (GB) x Daily traffic tiered unit price (CNY/GB)</code></pre>

4、 Billing examples:

- For example, if you use VOD acceleration service on January 1 with 55 GB downstream traffic generated, the VOD storage fee you need to pay on January 2 is calculated as follows:

<pre><code>VOD traffic fee for January 1 = 0.27 (CNY/GB) x 55 (GB)=14.85 CNY</code></pre>

## Reclamation of Resources upon Suspense of VOD Service

To ensure that you can use our service normally, we will suspend the service of customers whose accounts are in arrears, and reclaim the resources allocated to the customers with long-standing arrears.

#### Rules for Suspense of Service

1. Policy of service suspension: Fees generated in the previous day are billed and deducted between 12:00 and 18:00 of the next day, during which bills are also generated. If deduction failed due to insufficient balance, the overdraft notice is sent on the same day. If the account has not been topped up from 8:00 to 12:00 on the next day, the service is officially suspended, otherwise it is not suspended.

2. Suspended service: You are not allowed to use all the services provided by VOD or the console upon the suspension of service. However, VOD files and configuration information are not deleted or modified.

3. Policy of service activation: The service is automatically activated after the account is topped up to an amount greater than 0.

4. Reclamation policy: After the service is suspended, if the account is not topped up to an amount greater than 0 within 30 days, the reclamation policy is enabled. We then delete the source files and transcoded files stored on the Tencent Cloud VOD service to release resources. This operation cannot be undone. To protect your files from accidental deletion, pay attention to the account's arrearage information and make payments in time.


