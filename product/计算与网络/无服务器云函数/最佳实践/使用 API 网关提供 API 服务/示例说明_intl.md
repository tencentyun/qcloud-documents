In this tutorial, assuming that:
- You want to use SCFs to implement Web backend services, such as listing the articles in a blog and providing article contents.
- You want to use APIs to provide services for webpages and Apps.

## Implementation Overview

The implementation process of the service is as follows:

- Create a function, configure API rules in the API gateway and direct the backend service to the function.
- A user sends a request that contains the article ID to the API.
- SCF queries the content corresponding to the ID according to the request parameters, and responds to the request in JSON format.
- The user performs subsequent processing after receiving the response in JSON format.


Note: By the time you finish this tutorial, your account will contain the following resources:

- A SCF triggered by the API gateway.
- An API service in the API gateway and related API rules.

This tutorial is divided into three parts:

- Complete the coding, creation, and testing of a function.
- Complete the design, creation and configuration of an API service and API rules.
- Test and verify the correctness and operation of the APIs through a browser or http request tool.

## API Design

The design of APIs for current applications usually follows the Restful specification. Therefore in this example, we design the APIs for obtaining blog articles as follows:

* /article GET
Return the article list

* /article/{articleId} GET
Return the content of the article with the specified ID


