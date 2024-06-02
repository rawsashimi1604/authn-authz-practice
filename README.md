# authn-authz-practice

## Creating a python virutal environmnet

Create a python virtual environment to prevent clashing of dependencies and for
best practice. command is either `python` or `python3`

```bash
python -m venv authpractice
source authpractice/bin/activate
```

To deactivate the virtual environment

```
cd authpractice/bin
deactivate
```

## Ldap practice

script is `ldap.py`

### Creating a ldap server locally

- Step 1: Pull the OpenLDAP docker image
  - `docker pull osixia/openldap`
- Step 2: Run the container
  - `docker run --name my-openldap-container -p 389:389 -p 636:636 -e LDAP_ORGANISATION="Example Org" -e LDAP_DOMAIN="example.org" -e LDAP_ADMIN_PASSWORD="adminpassword" -d osixia/openldap`
- Step 3: Verify the container is running
  - `docker ps -a`
- Step 4: Interact with server using `openldap` or use docker container
  - Install openldap (brew): `brew install openldap`

### Querying ldap server

Try this command to query the ldap server

```bash
ldapsearch -x -H ldap://localhost -D "cn=admin,dc=example,dc=org" -w
adminpassword -b "dc=example,dc=org"
```

## Kerboros pracgtice

## Oauth 2 practice

## Open id connect practice
