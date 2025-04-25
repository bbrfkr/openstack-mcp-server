from openstack import connection
from config import get_keystone_session

class NovaClient:
    def __init__(self):
        self.session = get_keystone_session()
        self.conn = connection.Connection(session=self.session)

    def list_servers(self):
        return [server.to_dict() for server in self.conn.compute.servers()]

    def get_server_details(self, server_id):
        server = self.conn.compute.get_server(server_id)
        return server.to_dict() if server else None