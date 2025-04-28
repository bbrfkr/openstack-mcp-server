from openstack import connection
from config import get_keystone_session


class SwiftClient:
    def __init__(self):
        self.session = get_keystone_session()
        self.conn = connection.Connection(session=self.session)

    def list_containers(self):
        return [
            container.to_dict() for container in self.conn.object_store.containers()
        ]

    def get_container_objects(self, container_name):
        objects = self.conn.object_store.objects(container_name)
        if objects:
            return [obj.to_dict() for obj in objects]
        return None
