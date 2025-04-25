import json

from nova_client import NovaClient
from neutron_client import NeutronClient
from swift_client import SwiftClient
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("OpenStack Mcp Server")

nova = NovaClient()
neutron = NeutronClient()
swift = SwiftClient()


@mcp.tool("list-instances")
def list_instances():
    servers = nova.list_servers()
    return ",".join([server["id"] for server in servers])


@mcp.tool("get-instances")
def get_instance(instance_id: str):
    server = nova.get_server_details(instance_id)
    if server:
        return json.dumps(server)
    return "not found"


# @app.route('/containers', methods=['GET'])
# def list_containers():
#     containers = swift.list_containers()
#     return jsonify(containers), 200

# @app.route('/container/<string:container_name>/objects', methods=['GET'])
# def get_container_objects(container_name):
#     objects = swift.get_container_objects(container_name)
#     if not objects:
#         return jsonify({"error": "Container not found"}), 404
#     return jsonify(objects), 200

# @app.route('/networks', methods=['GET'])
# def list_networks():
#     networks = neutron.list_networks()
#     return jsonify(networks), 200

# @app.route('/network/<string:network_id>', methods=['GET'])
# def get_network(network_id):
#     network = neutron.get_network_details(network_id)
#     if not network:
#         return jsonify({"error": "Network not found"}), 404
#     return jsonify(network), 200

if __name__ == "__main__":
    mcp.run()
