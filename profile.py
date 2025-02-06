#!/usr/bin/python

"""
An example of a profile including RF links.

Instructions:
This is an example profile to demonstrate the description of RF links.
It is not particularly useful to instantiate directly.
"""

import geni.portal as portal
import geni.rspec.pg as rspec
import geni.rspec.emulab.pnext as pn

request = portal.context.makeRequestRSpec()

node0 = request.RawPC( "node0" )
iface0 = node0.addInterface( "rf0" )

node1 = request.RawPC( "node1" )
iface1 = node1.addInterface( "rf1" )

rflink = request.RFLink( "rflink" )
rflink.addInterface( iface0 )
rflink.addInterface( iface1 )

portal.context.printRequestRSpec()
