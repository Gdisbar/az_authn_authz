

```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```
**fastapi_test-server | Expose an API**

 - Application ID URI  
 
 ```bash  
   api://<SERVER_CLIENT_ID>
 ```

 - Scopes defined by this API : Add a scope

 ```bash
    scope : api://<SERVER_CLIENT_ID>/<SCOPE_NAME>
 ```
 - Authorized client applications : Add a client application
 ```bash
      search by <CLIENT_OPENAPI_CLIENT_ID> & add the scope
 ```

**fastapi_test-server | Manifest**

Set the token version to 2:
```bash
"requestedAccessTokenVersion": 2 (Microsoft Graph app manifest), or
"accessTokenAcceptedVersion": 2 (AAD Graph manifest)
```

**fastapi_test-server | API permissions**

  go to API my organization uses -> search the server 

# Expose an API

Application ID URI
Scopes defined by this API (add a scope)
Authorized client applications (add a client application)

# API Permission

Configured permissions