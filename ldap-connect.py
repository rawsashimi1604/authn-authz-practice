from ldap3 import Server, Connection, ALL, SUBTREE

# LDAP server configuration
ldap_server = 'ldap://your-ldap-server.com'
ldap_user = 'cn=admin,dc=example,dc=com'
ldap_password = 'your_password'
base_dn = 'dc=example,dc=com'

# Connect to the LDAP server
server = Server(ldap_server, get_info=ALL)
conn = Connection(server, user=ldap_user, password=ldap_password, auto_bind=True)

# Check if the connection is bound
if conn.bound:
    print("Successfully connected and authenticated to the LDAP server.")

    # Perform a search
    search_filter = '(objectClass=person)'
    conn.search(search_base=base_dn, search_filter=search_filter, search_scope=SUBTREE, attributes=['cn', 'mail'])

    # Process the search results
    for entry in conn.entries:
        print(entry)

    # Unbind the connection
    conn.unbind()
else:
    print("Failed to connect or authenticate to the LDAP server.")
