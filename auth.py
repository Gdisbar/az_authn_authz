from fastapi_azure_auth import SingleTenantAzureAuthorizationCodeBearer
import os
from dotenv import load_dotenv
load_dotenv()


AZURE_BACKEND_APP_CLIENT_ID = os.getenv("SERVER_CLIENT_ID")
AZURE_TENANT_ID = os.getenv("TENANT_ID")
AZURE_FRONTEND_APP_CLIENT_ID = os.getenv("CLIENT_OPENAPI_CLIENT_ID")
SCOPE_NAME = os.getenv("SCOPE_NAME")


azure_scheme = SingleTenantAzureAuthorizationCodeBearer(
    app_client_id=AZURE_BACKEND_APP_CLIENT_ID,
    tenant_id=AZURE_TENANT_ID,
    scopes={
        f"api://{AZURE_BACKEND_APP_CLIENT_ID}/{SCOPE_NAME}": 'API is used as user endpoints',
    },
    allow_guest_users=True,  # only if you want outside org to use the API
    
)
