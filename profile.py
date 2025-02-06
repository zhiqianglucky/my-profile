"""An example of constructing a profile with a single Xen VM.

Instructions:
Wait for the profile instance to start, and then log in to the VM via the
ssh port specified below.  (Note that in this case, you will need to access
the VM through a high port on the physical host, since we have not requested
a public IP address for the VM itself.)
"""

import geni.portal as portal
import geni.rspec.pg as rspec

# Create a Request object to start building the RSpec.
request = portal.context.makeRequestRSpec()
 
# Create a XenVM
node = request.XenVM("node")

# Ask for two cores
node.cores = 2
# Ask for 2GB of ram
node.ram   = 2048
# Add an extra 8GB of space on the primary disk.
# NOTE: Use fdisk, the extra space is in the 4th DOS partition,
#       you will need to create a filesystem and mount it. 
node.disk  = 8

# Alternate method; request an ephemeral blockstore mounted at /mydata. 
# NOTE: Comment out the above line (node.disk) if you do it this way. 
#bs = node.Blockstore("bs", "/mydata")
#bs.size = "8GB"
#bs.placement = "nonsysvol"

# Print the RSpec to the enclosing page.
portal.context.printRequestRSpec()
