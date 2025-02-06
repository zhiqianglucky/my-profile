"""An example of constructing a profile with two ARM64 nodes connected by a LAN.

Instructions:
Wait for the profile instance to start, and then log in to either host via the
ssh ports specified below.
"""

import geni.portal as portal
import geni.rspec.pg as rspec

request = portal.context.makeRequestRSpec()

# Create two raw "PC" nodes
node1 = request.RawPC("node1")
node2 = request.RawPC("node2")

# Set each of the two to specifically request "m400" nodes, which in CloudLab, are ARM
node1.hardware_type = "m400"
node2.hardware_type = "m400"

# Create a link between them
link1 = request.Link(members = [node1, node2])

portal.context.printRequestRSpec()
