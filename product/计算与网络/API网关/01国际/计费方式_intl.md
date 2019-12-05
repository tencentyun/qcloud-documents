The API gateway charges by recorded number of API calls and outbound traffic. A requesting, calling and returning from the client to the API is recorded as a call.
> Note: API gateway is not charged during internal trial and public trial.

The outbound traffic of API gateway refers to the outgoing traffic relative to API gateway. For example, if the backend service is HTTP call, the traffic from API gateway to HTTP service and the traffic of API gateway responding to front-end client are called outbound traffic. The outbound relationship of traffic is shown in the following table:

| HTTP Type | Source | Target | Traffic Type |
| --- | --- | --- | --- |
| HTTP request | Client, browser, sdk | API gateway | Inbound traffic | 
| HTTP request | API gateway | Backend service | Outbound traffic | 
| HTTP response | Backend service | API gateway | Inbound traffic | 
| HTTP response | API gateway | Client, browser, sdk | Outbound traffic | 


## Billing of Backend HTTP Call

The traffic type and billing type of HTTP service are as follows according to its region.

| HTTP Service Region | HTTP Address | Traffic Type | Billed or not |
| ---          |   ---     | ---   | ---   |
| In the region of the API service within Tencent Cloud | Private network address | Private network traffic | Free | 
| In the region of the API service within Tencent Cloud | Public network address | Public network traffic | Billed | 
| Not in the region of the API service within Tencent Cloud | Public network address | Public network traffic | Billed | 
| Non-Tencent Cloud Internet address | Public network address | Public network traffic | Billed | 

## Billing of Backend Serverless Cloud Function Call

The traffic type and billing type of Serverless Cloud Function (SCF) are shown in the following table according to SCF region.

| SCF Region | Traffic Type | Billed or not |
| ---          |   ---     | ---      |
| In the region of the API service | Private network traffic | Free | 
| Not in the region of the API service | Public network traffic | Billed | 

