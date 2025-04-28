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
    return json.dumps(servers)


@mcp.tool("get-instances")
def get_instance(instance_id: str):
    server = nova.get_server_details(instance_id)
    if server:
        return json.dumps(server)
    return "not found"


@mcp.tool("list-containers")
def list_containers():
    containers = swift.list_containers()
    return json.dumps(containers)


@mcp.tool("get-container-objects")
def get_container_objects(container_name: str):
    objects = swift.get_container_objects(container_name)
    if not objects:
        return json.dumps({"error": "Container not found"}), 404
    return json.dumps(objects)


@mcp.tool("list-networks")
def list_networks():
    networks = neutron.list_networks()
    return json.dumps(networks)


@mcp.tool("get-network")
def get_network(network_id: str):
    network = neutron.get_network_details(network_id)
    if network:
        return json.dumps(network)
    return "not found"


if __name__ == "__main__":
    mcp.run()
