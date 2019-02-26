### App&H5 Linkage Analysis Connection
When you need to track the basic access and click events of App webview, add the following js code in webview:
```html
<script src="//pingjs.qq.com/mta/app_link_h5_stats.js" name="MtaLinkH5"></script>
```
>**Note:**
>Make sure that js sdk has been loaded for the follow-up method reporting.

### Manually Reporting Page Visits

When a page is visited, report the page visits:

```js
MtaLinkH5.pageBasicStats({
  'title': 'Required - The title of each page must be unique'
});
```
>**Note:**
>Make sure that the linkage analysis js sdk has been loaded and the title name has been set.
>title is required, and the title of each page must be unique, otherwise the tracking result will be affected.

### Setting Login Account
Set the information of user's login account:

```js
MtaLinkH5.setLoginUin(uin);
```
>**Note:**
>Make sure that the linkage analysis js sdk has been loaded.
>uin (string) is the user account.

### Custom Event
Track and report custom events on the page:

```js
MtaLinkH5.eventStats(event_id, param_json);
```

>**Note:**
>Make sure that the linkage analysis js sdk has been loaded.
>event_id is the event ID. Copy this ID after it is added to the event.
>param_json (in json format) is event parameter or event parameter value. Each parameter corresponds to a parameter value.

#### Example:
```html
<button onclick="MtaLinkH5.eventStats('test_event')">Event-without parameter</button>
<button onclick="MtaLinkH5.eventStats('test_event', {'param1':'value1'})">Event-single parameter</button>
<button onclick="MtaLinkH5.eventStats('test_event', {'param1':'value1','param2':'value2'})">Event-multiple parameters-the number of parameters should not exceed 5</button>
```

