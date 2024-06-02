# authn-authz-practice

## Ldap practice

script is `ldap-connect.py`

### Creating a ldap server locally

- Step 1: Pull the OpenLDAP docker image
  - `docker pull osixia/openldap`
- Step 2: Run the container
  - `docker run --name my-openldap-container -p 389:389 -p 636:636 -e LDAP_ORGANISATION="Example Org" -e LDAP_DOMAIN="example.org" -e LDAP_ADMIN_PASSWORD="adminpassword" -d osixia/openldap`
- Step 3: Verify the container is running
  - `docker ps -a`
- Step 4: Interact with server using `openldap`
  - Install openldap (brew): `brew install openldap`
