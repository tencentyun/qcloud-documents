Session statistics is used to count the number of times an App is launched, which is maintained by SDK. Usually, developers are not required to additionally set or call APIs. In the following three cases, the user is considered to open a new session:
1. The App is launched for the first time, or after the Apn process is terminated at the backend;
2. The App is switched to the backend or switched back to the frontend after the time of screen locking exceeds X seconds. X is set by StatConfig.setSessionTimoutMillis(int) function. It is 30,000 ms (30 seconds) by default.
**Example:** If a user presses the home button (or locks screen) to switch to the backend after opening QQ on mobile and operating for 10 minutes, and then switch back to QQ again after 30 seconds, SDK will report a session.
>**Note:**
>Determine whether to adjust the timeout time according to your App service.

3. Call the startNewSession() function provided by SDK

```
void StatService.startNewSession(Context ctx)
```
### Parameters
| Parameter Name | Description |
|------|---------|
| Ctx | device context of the page |

>Note:
><br>If you want to collect the data in h5 page in the App, integrate according to [hybird app android Instructions](https://cloud.tencent.com/document/product/549/12899).

