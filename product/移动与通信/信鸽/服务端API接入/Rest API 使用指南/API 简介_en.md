The request URL is:` http://domain name for API/v2/class/method?params`

| Field Name | Description | Note |
|-|-|-|
| Domain name for API | Domain name for API | openapi.xg.qq.com is always used |
| v2 | Version number of the current API | None |
| Class | API class provided | None |
| method | APIs provided by each API class | Such as query, setting, deletion, etc.|
| params | Parameters passed when an API is called in GET mode | Include common parameters and API-specific parameters. All parameters must be UTF-8 encoded and params strings must be URL encoded |

>**Note:**
>When an API is called in POST mode, the parameters need to be passed as POST parameters, and the content is the same as the params field. The "Content-type" field in HTTP HEADER should be set to "application/x-www-form-urlencoded".

