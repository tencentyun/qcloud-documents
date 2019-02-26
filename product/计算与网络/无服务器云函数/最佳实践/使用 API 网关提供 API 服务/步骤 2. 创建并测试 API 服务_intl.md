In this section, you will create a service in the API gateway and related API rules, connect the SCF created in Step 1, and test the correctness of the APIs through the console.

> Note:
> The API service and the function must be in the same region. In this tutorial, the API service is created in the region Guangzhou.


## Creating an API Service and API Rules

1. Log in to the [Tencent Cloud Console](https://console.cloud.tencent.com/apigateway), and select **Internet Middleware** -> **API Gateway** from **Cloud Products**.

2. Click the **Services** tab and change the region to **Guangzhou**.

3. Click **New** to create an API service. Enter the service name `blogAPI` in the pop-up window and click **Submit** to complete the creation.

4. Enter the created service `blogAPI`, and select the **API Management** tab.

5. Click **New** to create an API with the path of `/article` and the request method of GET. To facilitate the test later, select **No Authentication** here. No parameter configuration needs to be made. Click **Next**.

6. Select **Cloud Function** for the backend type, and select `blogArticle` created in Step 1 as the function, and click **Complete**.

7. Click **New** in the **API Management** tab to create another API with the path of `/article/{articleId}` and the request method of GET. Select **No Authentication**, and enter the parameter `articleId` in the parameter configuration with Path as the parameter location, int as the parameter type, and 1 as the default value, and then click **Next**.

8. Select **Cloud Function** for the backend type, and select `blogArticle` created in Step 1 as the function, and click **Complete**.

## Debugging API Rules

1. To debug the API `/article` created in the step 5 above, click **API Debugging**, send a request in the debugging page, and check whether the response body in the returned result is shown as follows:
```
[{"category": "blog", "time": "2017-12-05 13:45", "id": 1, "title": "hello world"}, {"category": "blog", "time": "2017-12-06 08:22", "id": 2, "title": "record info"}, {"category": "python", "time": "2017-12-06 18:32", "id": 3, "title": "python study"}]
```

2. To debug the API `/article/{articleId}` created in the step 7 above, click **API Debugging**, modify the request parameter value to 1 and send a request in the debugging page, and check whether the response body in the returned result is shown as follows:
```
{"category": "blog", "content": "first blog! hello world!", "time": "2017-12-05 13:45", "id": 1, "title": "hello world"}
```

3. You can also modify the value of the request parameter articleId in step 2 to other number and check the response content.

