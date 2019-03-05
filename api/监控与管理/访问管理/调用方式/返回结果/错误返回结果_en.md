If an API call fails, the "code" field in the returned result is not 0 but a code description, and the "message" field shows the detailed error information. You can query detailed error message on error code page based on code and message.
Example of returned error:
```
{
    "code": 4000,
    "message": "(100004) incorrect projectId",
}
```

