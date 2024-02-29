import json
from datetime import datetime, timedelta
import oci
import json
import pytz


def create_auth_token_for_user(user_id, description):
    # Initialize the IdentityClient using instance principal
    identity_client = oci.identity.IdentityClient({}, signer=oci.auth.signers.InstancePrincipalsSecurityTokenSigner())
    # Create a new auth token for the specified user
    create_auth_token_details = oci.identity.models.CreateAuthTokenDetails(
        description=description
    )
    auth_token_response = identity_client.create_auth_token(user_id=user_id,
                                                            create_auth_token_details=create_auth_token_details)
    return auth_token_response.data


def delete_old_api_keys(user_ocid):
    # Get the instance principal
    provider = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
    # Initialize the IdentityClient
    identity_client = oci.identity.IdentityClient(config={}, signer=provider)
    # List the user's API keys
    api_keys = identity_client.list_api_keys(user_id=user_ocid).data
    # Get the current time
    current_time = datetime.utcnow()
    # Delete API keys created more than 12 hours ago
    for api_key in api_keys:
        creation_time = api_key.time_created
        if (current_time - creation_time).total_seconds() > 12 * 3600:
            identity_client.delete_api_key(api_key_id=api_key.id, user_id=user_ocid)

    print("API keys created more than 12 hours ago have been deleted.")


def delete_auth_tokens_for_user(user_id):
    # Initialize the IdentityClient using instance principal
    identity_client = oci.identity.IdentityClient({}, signer=oci.auth.signers.InstancePrincipalsSecurityTokenSigner())
    # Fetch all auth tokens for the specified user
    list_auth_tokens_response = identity_client.list_auth_tokens(user_id=user_id)
    auth_tokens = list_auth_tokens_response.data
    # Sort auth tokens by creation time
    sorted_tokens = sorted(auth_tokens, key=lambda x: x.time_created)
    # Get current time
    current_time = datetime.utcnow().replace(tzinfo=pytz.UTC)
    # Check if any auth token is older than 12 hours
    for auth_token in auth_tokens:
        time_difference = current_time - auth_token.time_created
        if time_difference > timedelta(hours=12):
            identity_client.delete_auth_token(auth_token.id)
            print(f"Deleted auth token {auth_token.id} because it's older than 12 hours.")
    # If there are 2 or more tokens, delete the oldest one
    if len(auth_tokens) >= 2:
        oldest_token = sorted_tokens[0]
        identity_client.delete_auth_token(auth_token_id=oldest_token.id, user_id=user_id)
        print(f"Deleted oldest auth token {oldest_token.id}.")


def get_auth_tokens_for_user(user_id):
    # Initialize the IdentityClient using instance principal
    identity_client = oci.identity.IdentityClient({}, signer=oci.auth.signers.InstancePrincipalsSecurityTokenSigner())
    # Fetch all auth tokens for the specified user
    list_auth_tokens_response = identity_client.list_auth_tokens(user_id=user_id)
    # Extract and format auth token details
    auth_tokens = []
    for auth_token in list_auth_tokens_response.data:
        auth_token_info = {
            "id": auth_token.id,
            "description": auth_token.description,
            "inactive_status": auth_token.inactive_status,
            "time_created": auth_token.time_created.isoformat(),
            "lifecycle_state": auth_token.lifecycle_state,
            "user_id": auth_token.user_id,
            # "compartment_id": auth_token.compartment_id   <-- Remove this line
        }
        auth_tokens.append(auth_token_info)

    # Return the auth tokens in JSON format
    return json.dumps(auth_tokens, indent=4)


user_id = "user ocid"

# Delete Old API Keys
delete_auth_tokens_for_user(user_id)

# Create a new auth token
description = "Test Auth Token - " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
new_auth_token = create_auth_token_for_user(user_id, description)

# Delete Old API Keys
delete_old_api_keys(user_id)
