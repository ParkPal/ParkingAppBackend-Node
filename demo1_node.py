"""
This is the code that will simulate the host for our first demo.
It will wait for a message from the node then broadcast it to
the server.
"""

from networking import WebConnection
from node import Node

def main():
    """ Create an object to represent this parking spot """
    this_spot = Node(1, "192.168.2.2")

    """ Create an object to broadcoast updates to host """
    mesh_connection = WebConnection("192.168.2.1", 12345)
    mesh_connection.init_conn()

    """ Create an object to recieve data from sensor """
    # gpio_connection = 

#   while True:
    """ Wait for updates from sensor """

    """ Broadcast to Host """
    mesh_connection.transmit_object(this_spot)

main()
