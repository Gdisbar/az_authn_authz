

```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

## FastAPI Test Server

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
"requestedAccessTokenVersion": 2 # (Microsoft Graph app manifest), or
"accessTokenAcceptedVersion": 2 # (AAD Graph manifest)
```

**fastapi_test-server | API permissions**

  go to API my organization uses -> search the test-server -> add the permissons 


**fastapi_test-server - Overview | Add redirection**

```bash
    # Remember to use localhost not 127.0.0.1 in browser 
    # while doing local testing
    http://localhost:8000/docs
```

## FastAPI Test Client

at the time of creation of client put the redirection url
as 

```bash
http://localhost:8000/oauth2-redirect
```