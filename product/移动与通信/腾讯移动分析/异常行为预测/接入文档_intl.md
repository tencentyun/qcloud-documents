First, customers need to register on the [Mobile Tencent Analytics official website](http://mta.qq.com/), fill in the form and submit application. The system will then automatically send an email to customer service for approval.
>Note:
To complete qualification verification of exceptional behavior prediction service, you need to fill in the following information: company name, company address, application category, application name, applicant's name, applicant's role, applicant's phone number, and applicant's email address, etc.
![](https://main.qcloudimg.com/raw/2229141163aec24a9f8242213494954f.png)
Approval results:

```
1. If the application is rejected, when this service becomes fully available, you will be notified via email.
2. If the application is approved, the process of tracking, self-test and launching of SDK and the process of integration and launching of query API will be enabled concurrently.
```

**Customers who have passed the qualification verification need to start the following two processes concurrently:**
1. Process of tracking, self-test and launching of SDK
i. Download the SDK with test plug-in (see the approval email for download link). Then, integrate SDK by referring to SDK connection document, and track events in the [Industrial Tracking Standards]().
ii. Obtain the URL of self-test tool (see the approval email for URL), and perform self-test as instructed.
iii. After the self-test is passed, package the App for release in the market. After release, perform self-test again (you cannot query the exception score if the test is not passed).

2. Process of integration and launching of query API
i. Obtain the independent access key of the query API (see the approval email).
ii. Refer to the API technical document for the development and integration, and complete the signature verification and API integration.
iii. With SDK event tracking, users can launch the API after normally obtaining the predicted exception score.
iiii. According to different industries, customers need to provide different types of data feedback, and assist with the integration.
