""" Example node sending data """

from networking import *
from host import *
from node import *
import pickle

def main():
    print("Running...")
    conn = WebConnection("127.0.0.1", 12345)
    conn.init_conn()
    
    host_obj = Host("newhost")
    node_obj = Node(1, "192.168.1.1")
    host_obj.add_node(node_obj)

    conn.transmit_object(host_obj)

#    pick = pickle.dumps(node_obj)
#    conn.transmit_bytes(pick)

    
main()