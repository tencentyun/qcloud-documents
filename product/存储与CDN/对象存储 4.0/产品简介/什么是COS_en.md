## Introduction to COS

Tencent Cloud COS (Cloud Object Storage) is a distributed storage service that can be used to store and retrieve any amount of data, at any time, from anywhere on the Web. It allows all developers to access a scalable, reliable and secure data storage at low cost.

The COS solves the resource overconsumption problem of traditional file system in accessing directories, and supports mass data storage as well as simple and rapid access to such data via API, SDK or other methods. You can use it to upload, download and manage any type of files. In addition, Tencent Cloud provides an intuitive Web management interface. You can speed up downloads through the nationwide CDN nodes.

This product documentation describes some core concepts of Tencent Cloud COS (such as bucket, object) and how to use such resources. You can learn how to create buckets, store and retrieve objects, and manage resource access permissions from this document.

## COS Vs. Traditional File System

COS is a distributed cloud object storage service, while file system is a typical tree index structure.

File system supports all operations on the directory file. However, as such operations are performed on tree index, the file system consumes larger resources when accessing deeper directories. Due to limitation on the performance of a single device, file system is only available for performing a small amount of data operations. On the contrary, as COS stores both file data and metadata, and is not built as a tree index like file system, it is capable of performing massive user concurrent access and mass data storage.


The following figure illustrates the service architecture of COS:

![](https://mccdn.qcloud.com/static/img/054a0694e4d52fb1a470debcf57452eb/image.png)

For more information on Tencent Cloud COS, refer to:
[Terms and Concepts of COS](https://cloud.tencent.com/document/product/436/6225)
[How to Use Buckets](https://cloud.tencent.com/document/product/436/6232)
[How to Use Objects](https://cloud.tencent.com/document/product/436/6233)

## Standard Storage

High-frequency Storage provides users with Cloud Object Storage with high reliability, high availability and high performance. High-frequency Storage has low access latency and high throughput, which means it is suitable for business scenarios with large amount of hot files and data that is accessed frequently, for example, hot videos, mobile applications, game programs and dynamic websites.

## Low-frequency Storage

Low-frequency Storage provides users with Cloud Object Storage with high reliability, relatively low storage cost and access latency. Low-frequency Storage is suitable for business scenarios with low access frequency, for example, online disks and low-frequency files. Low-frequency Storage has lower storage cost, while maintaining a Time to First Byte within milliseconds. Users can read data with fast speed when retrieving data, without the need to wait.

## Nearline Storage

Nearline Storage provides users with online storage with high reliability and low cost. Nearline Storage is positioned between online storage and offline storage. Nearline Storage is suitable for business scenarios where the data is not accessed frequently, but is still required to be read online when necessary, for example, infrequently used media materials and disaster recovery backup. The most obvious feature of Nearline Storage is that its price is similar with that of offline storage, while Nearline Storage is still able to respond within seconds.
