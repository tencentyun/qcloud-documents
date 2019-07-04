## Microservice Development

If you are developing a microservice architecture, you may face the following facts:
* There are a large number of microservice modules.
* Each module provides its own API services.
* Each module provides its own service address or LB.
* Some API calls are associated with each other.
* In some cases, multiple APIs need to be called to obtain the final data.
* The calling specifications, naming conventions and parameter calling methods may vary with different APIs.
* API verification and authentication are required for each module.
* API calls of some modules may increase abruptly due to business changes.

In this case, the management and use of APIs will become more and more complicated with the growing number of micro-service modules. API Gateway can help you solve these problems easily:
* It allows centralized management of APIs. The API users can query the API usage in a single place.
* It generates documents and SDKs and tests and calls APIs automatically, allowing users or developers to get started with APIs more quickly.
* It helps you manage request traffic through throttling, so that back-end modules can withstand traffic spikes.
* It unifies the specifications, naming conventions and parameter calling methods of different APIs.
* It helps you centrally perform the API verification and authentication.



## Serverless Development

In case of the development using Serverless Cloud Function (SCF), if you want to make API services available to Apps, Web applications or Clients after you write the functions, an access mechanism must be put in place.

You can use API Gateway to configure an API to be linked with the backend Cloud Function. Then each call to the API triggers the execution of the Cloud Function to implement the business functions. For Serverless development, you only pay for the API calls and the execution of SCF.


## Prevent Opening APIs of Traditional Applications

With API Gateway, you do not need to directly open the old APIs of traditional applications to the Internet, thus avoiding server vulnerabilities and security problems. Meanwhile, you can manage traffic through throttling in API Gateway to avoid application or service failures caused by traffic spikes. By leveraging Tencent Cloud's CAM, API Gateway will provide access control based on different permissions to cater for the needs of a diversity of users or clients.

