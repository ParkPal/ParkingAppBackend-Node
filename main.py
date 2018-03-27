from networking import WebConnection
from node import Node
from car_sensor import CarSensor
import socket

def main():
	print("Node Starting")
	host_conn = WebConnection("192.168.2.1", 12345)
	host_conn.init_conn()

	this_node = Node(1, "192.168.2.2")
	node_sensor = CarSensor()

	if node_sensor.is_occupied():
		this_node.set_inUse(True)
		print("Start: Car Present")
	else:
		this_node.set_inUse(False)
		print("Start: No Car")

	host_conn.transmit_object(this_node)
	host_conn.s.shutdown(socket.SHUT_RDWR)
	host_conn.s.close()

	while(True):
		tmp = node_sensor.is_occupied()
		if tmp != this_node.get_inUse():
			host_conn = WebConnection("192.168.2.1", 12345)
			host_conn.init_conn()
			this_node.set_inUse(tmp)
			host_conn.transmit_object(this_node)
			print("CHANGED")

main()
