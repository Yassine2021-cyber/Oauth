## authentication flow

from __future__ import absolute_import
import google_auth_oauthlib.flow
from requests_oauthlib import OAuth2Session

client_id= "cloud-cli"
redirect_uri= "urn:ietf:wg:oauth:2.0:oob"
authorization_base_url= "https://auth.cern.ch/auth/realms/cern/protocol/openid-connect/auth"
scope= ['profile', 'email']

keycloack= OAuth2Session(client_id, redirect_uri=redirect_uri,scope=scope)
authorization_url, state =keycloack.authorization_url(authorization_base_url,access_type="offline", prompt="select_account")
print ('Please go here and authorize,'), authorization_url
authorization_response = input('Enter the full callback URL:')

token =keycloack.fetch_token(
   'https://auth.cern.ch/auth/realms/cern/protocol/openid-connect/token',
     authorization_response=authorization_response,
)
