## YAML 格式导入 API 示例
```yaml
openapi: 3.0.0
info:
  description: importMockAPI
  version: "1.0.0"
  title: Mock API
paths:
  /mock:
    get:
      description: Import Mock API Test
      operationId: importMockAPI
      responses:
        '200':
          description: Import Mock API Test
```

## JSON 格式导入 API 示例
```json
{
  "openapi": "3.0.0",
  "info": {
    "description": "importMockAPI",
    "version": "1.0.0",
    "title": "Mock API"
  },
  "paths": {
    "/mock": {
      "get": {
        "description": "Import Mock API Test",
        "operationId": "importMockAPI",
        "responses": {
          "200": {
            "description": "Import Mock API Test"
          }
        }
      }
    }
  }
}
```

