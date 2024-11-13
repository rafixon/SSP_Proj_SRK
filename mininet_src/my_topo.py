"""
Topology for project : Implementacja Mechanizmu Równoważenia Obciążenia w Sieciach SDN z Wykorzystaniem Kontrolera POX i Algorytmu Least Weighted Connections
One switch connected to four hosts:

          / --- h2
         |
 h1 --- s1  --- h3
         |
          \ --- h4

Adding the 'topos' dict with a key/value pair to generate our newly defined
topology enables one to pass in '--topo=mytopo' from the command line.
"""
from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology with one switch and four hosts."

    def __init__( self ):
        "Create custom topo."

        # Initialize topology
        Topo.__init__( self )

        # Add hosts
        host1 = self.addHost( 'h1' )
        host2 = self.addHost( 'h2' )
        host3 = self.addHost( 'h3' )
        host4 = self.addHost( 'h4' )

        # Add switch
        switch1 = self.addSwitch( 's1' )

        # Add links
        self.addLink( host1, switch1 )
        self.addLink( host2, switch1 )
        self.addLink( host3, switch1 )
        self.addLink( host4, switch1 )
		
		
        # Initialize topology
        Topo.__init__( self )

# Dictionary to add the topology under a specific key
topos = { 'mytopo': ( lambda: MyTopo() ) }


