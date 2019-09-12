Tencent Cloud VOD product is billed based on the following three parts:

- **Video storage:** The storage space taken up by the source video files and transcoded video files uploaded to Tencent Cloud VOD is charged on the basis of the storage capacity.
- **Video transcoding:** The source video files stored in Tencent Cloud VOD are charged by the specification and length of target files during transcoding.
- **Video acceleration:** Fees generated when CDN is used for acceleration during video playback are charged based on the downstream traffic.

You can view the actual usage of Tencent Cloud VOD via the [console](https://console.cloud.tencent.com/vod).

### Video Storage
#### Billing Item

- VOD storage fee.
- Fee for public network downstream traffic (the downstream traffic generated when videos are pulled directly from the origin server of VOD storage). Videos can be downloaded and played either from the VOD origin server or through the VOD acceleration CDN. If you use the URL (accelerated by VOD CDN) provided in the VOD service for video download and playback, this fee is not incurred. Only users pulling video directly from the origin server need to pay for the public network downstream traffic. Choose our services according to your actual needs.

#### Billing Price

- Original price for storage space: 0.008 CNY/GB/day.
- Discounted price for storage space: 0.0048 CNY/GB/day (at which the Tencent Cloud VOD storage service is billed by default).
- Public network downstream traffic of VOD origin server: 0.5 CNY/GB

#### Billing Description

- Method: Postpaid.
- Rule: Charged by actual usage. The billing value of the day is the peak of daily storage capacity.
- Cycle: Charged on a daily basis. Fees generated in current day are billed and deducted between 12:00 and 18:00 on next day, during which bills are also generated.
- Formula:
<pre><code>Daily storage fee=Peak storage capacity (GB)*0.008 CNY/GB/day
Daily public network downstream traffic fee=Public network traffic (GB)*0.5 CNY/GB</code></pre>

#### Billing Example
For example, if you use VOD storage service on January 1 with a peak storage capacity of 100 GB and pull 10 GB traffic directly from the origin server, the VOD storage fee you need to pay on January 2 is calculated as follows:
> VOD storage fee on January 1=Storage fee on January 1+Public network downstream traffic fee on January 1 =100 (GB)*0.008 CNY/GB+10 (GB)*0.5 CNY/GB=5.8 CNY

### Video Transcoding
#### Billing Item
Duration of VOD transcoding.

#### Billing Price

| Encoding Method | Resolution | Unit Price (CNY/min) |
| ---------  |:--------------------------------:|:---------------:|
| H.264 | 4K (3840*2160) or below | 0.28 |
| H.264 | 2K (2560*1440) or below | 0.14 |
| H.264 | FHD (1920 x 1080) or below | 0.065 |
| H.264 | HD (1280*720) or below | 0.033 |
| H.264 | SD (640*480) or below | 0.022 |
| H.265 | 4K (3840*2160) or below | 1.4 |
| H.265 | 2K (2560*1440) or below | 0.7 |
| H.265 | FHD (1920 x 1080) or below | 0.326 |
| H.265 | HD (1280*720) or below | 0.163 |
| H.265 | SD (640*480) or below | 0.109 |

> Note: H.265 transcoding is unavailable by default. Consult with us by submitting a ticket if needed.
> Video stitching and clipping are charged according to video processing duration, and the unit price is the same as that of transcoding.

#### Billing Description

- Method: Postpaid
- Rule: Charged on a daily basis according to the method for encoding transcoding request, resolution and the length of transcoded output file.
- Cycle: Charged on a daily basis. Fees generated in current day are billed and deducted between 12:00 and 18:00 on next day, during which bills are also generated.
- Formula:
<pre><code>Daily video transcoding fee=Length of transcoded output file (in min)*Transcoding unit price for videos with different encoding methods and resolutions (CNY/min)</code></pre>

#### Billing Example
For example, if you use VOD transcoding service on January 1, and transcode a video with a resolution of 2560*1440 and a length of 1 hour to a video with a resolution of 1280*960 and a length of 100 minutes by using H.264 encoding method, the VOD storage fee you need to pay on January 2 is calculated as follows:
> VOD transcoding fee on January 1=0.14 (CNY/min)*60 (minutes)+0.065 (CNY/min)*100 (minutes)=14.9 CNY

### Video Acceleration
#### Billing Item
Downstream traffic of VOD acceleration.

#### Billing Price
Tencent VOD traffic is billed on a daily basis using tiered prices. The more traffic you use on each day, the lower the billing tier you will get. Detailed tiered unit price is as follows:

| Traffic Tier | Unit Price (CNY/GB/day) |
| ----------      |:----------------:|
| 0 GB-50 GB (inclusive) | 0.24 |
| 50 GB-500 GB (inclusive) | 0.23 |
| 500 GB-1 TB (inclusive) | 0.22 |
| 1 TB-5 TB (inclusive) | 0.20 |
| Above 5 TB | 0.15 |

#### Billing Description
- Method: Postpaid
- Rule: Charged on a daily basis based on the downstream traffic generated when CDN is used for acceleration during video playback.
- Cycle: Charged on a daily basis. Fees generated in current day are billed and deducted between 12:00 and 18:00 on next day, during which bills are also generated.
- Formula:
<pre><code>Daily video traffic fee=Video playback downstream traffic (GB)*Daily traffic tiered unit price (CNY/GB)</code></pre>

#### Billing Example
- For example, if you use VOD acceleration service on January 1 with 55 GB downstream traffic generated, the VOD storage fee you need to pay on January 2 is calculated as follows:
> VOD traffic fee on January 1=0.23 (CNY/GB) * 55 (GB)=12.65 CNY

### Additional Note
For large business volume (storage space usage is greater than 1PB, or daily traffic consumption exceeds 10 TB), daily settlement may not meet your needs. You can contact our service personnel and determine the billing method and price through negotiation.

## Notes on Replacement of VOD Package with Daily Settlement
Tencent Cloud VOD has been well received by customers since its release. We have been committed to improving service quality and optimizing service cost with a view to providing services with high quality and low price for our customers. To make it easy for customers to access our services and help them cut cost, we have optimized the cost of services and adjusted the billing method and price of VOD service.
Additional notes on replacing VOD package with daily settlement:

1. The original VOD package is no longer available. After the package has expired, the service is settled on a daily basis, and the storage and traffic exceeding the package limit is billed at the daily settlement price. That is, the price for storage beyond the package is adjusted from 0.03 CNY/GB/day to 0.0048 CNY/GB/day, and the price for traffic beyond the package is changed from 0.59 CNY/GB to 0.24 CNY/GB.
2. For customers who register the VOD service for the first time, we provide a 30 CNY voucher for trial use. The voucher is limited to VOD service and is valid for one month.
3. In the VOD daily settlement mode, the transcoding service is billed independently. Customers can still use the free transcoding service in the VOD package before its expiration. After the package expires, the VOD service is settled on a daily basis, and the transcoding service is billed independently.
4. In VOD package mode, since only the storage space of source files instead of transcoded files is billed, the storage unit price is relatively high. This is unfair to customers who do not use the transcoding service. In the daily settlement mode, based on the principle of pay-as-you-go, the sum of the storage volume of source files and that of transcoded files is taken as the basis for storage billing. Transcoding fee is not required for customers who do not use the transcoding service. Therefore, if customers of the original package use the transcoding service, the storage may increase significantly after they switch to the daily settlement mode. This is because the storage space of transcoded files is also calculated as billing storage. However, we have optimized the cost by reducing the storage unit price greatly, so you can save cost at the new price.

