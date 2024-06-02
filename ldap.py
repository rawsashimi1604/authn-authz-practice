from ldap3 import Server, Connection, ALL, SUBTREE

class LdapManager:
    ldap_server = 'ldap://localhost'
    ldap_user = 'cn=admin,dc=example,dc=org'
    ldap_password = 'adminpassword'
    base_dn = 'dc=example,dc=org'

    def __init__(self):
        self.init_ldap_conn()

    def init_ldap_conn(self):
        server = Server(self.ldap_server, get_info=ALL)
        self.conn = Connection(server, user=self.ldap_user, password=self.ldap_password, auto_bind=True)
        if self.conn.bound:
            print("Successfully connected and authenticated to the LDAP server.")
        else:
            print("Failed to connect or authenticate to the LDAP server.")
            exit()
    
    def search(self, search_filter, attributes, search_scope=SUBTREE):
        # search_filter = '(objectClass=person)'

        self.conn.search(search_base=self.base_dn, search_filter=search_filter, search_scope=search_scope, attributes=attributes)
        if len(self.conn.entries) == 0:
            print("No entries found.")
            
        else:
            for entry in self.conn.entries:
                print(entry)

    def quit(self):
        self.conn.unbind()
        print("Quit the connection.")

    def add(self, dn, attributes):
        self.conn.add(dn, attributes)
        result_description = self.conn.result["description"]
        if result_description == "success":
            print(f"Successfully added the entry. {dn}")
        else:
            print(f"Failed to add the entry. {result_description}")

if __name__=="__main__":
    ldap_manager = LdapManager()
    ldap_manager.search('(objectClass=person)', ['cn', 'sn', 'mail'])
    ldap_manager.quit()