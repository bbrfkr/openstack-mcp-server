from openstack import connection
from config import get_keystone_session

class NeutronClient:
    def __init__(self):
        self.session = get_keystone_session()
        self.conn = connection.Connection(session=self.session)

    def list_networks(self):
        return [network.to_dict() for network in self.conn.network.networks()]

    def get_network_details(self, network_id):
        network = self.conn.network.get_network(network_id)
        return network.to_dict() if network else None