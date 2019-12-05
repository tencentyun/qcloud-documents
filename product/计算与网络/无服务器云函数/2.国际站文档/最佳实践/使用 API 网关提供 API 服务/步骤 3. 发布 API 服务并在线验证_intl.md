If you complete Step 2: Create and Test the API Service, and the test results meet the expectation, you can publish this service and initiate requests from a browser to verify whether the APIs run normally.

## API Service Publishing

1. In the list in the **Services** page in the API Gateway console, find the blogAPI service created in Step 2, and click **Publish** in **Operation**.

2. In the pop-up window for service publishing, select `Publish` for the publishing environment and enter `Publish API` in the comments, and click **Submit**.

## API Online Verification

After published, the APIs can be accessed externally. Next, you can initiate requests from a browser to verify whether the APIs can respond correctly.

1. In the blogAPI service, click the **Environment Management** tab, and copy the access path of the `Publish` environment, such as, `service-kzeed206-1251762227.ap-guangzhou.apigateway.myqcloud.com/release`.
 **Note**: Since the domain names of services are not the same, the domain name assigned to your service will be different from that in this document. Therefore, do not copy the address directly in this document.

2. Add the path of the created API rules after this path as follows:
```
service-kzeed206-1251762227.ap-guangzhou.apigateway.myqcloud.com/release/article
service-kzeed206-1251762227.ap-guangzhou.apigateway.myqcloud.com/release/article/1
service-kzeed206-1251762227.ap-guangzhou.apigateway.myqcloud.com/release/article/2
```

3. Copy the new path in step 2, paste it to the browser and access it, and check whether the output is the same with that when the API is tested.

4. You can modify the article ID in the request and check the output to see whether the code can handle the wrong article ID correctly.


Now, you have learned how to implement services using SCF and provide services using APIs. You can add new features and API rules subsequently by modifying the code to enrich the application module.

