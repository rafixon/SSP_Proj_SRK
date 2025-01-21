from mininet.topo import Topo

class SingleSwitchTopo(Topo):
    "Simple topology with one switch and four hosts."
    def __init__(self):
        Topo.__init__(self)

	# Add switch
        switch = self.addSwitch( 's1' ) 
	
        # Add hosts
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        h4 = self.addHost('h4')

        # Add links
        self.addLink(h1, switch)
        self.addLink(h2, switch)
        self.addLink(h3, switch)
        self.addLink(h4, switch)

# Dictionary to add the topology under a specific key
topos = { 'singleswitch': SingleSwitchTopo }
