from mininet.topo import Topo
from mininet.link import OVSLink, TCLink

class MyTopology(Topo):  
    "Example topology for DAT300-H24 Assignment 7."
    def __init__(self):

        # Initialize topology
        Topo.__init__(self)

        # Add hosts and switches
        PC1 = self.addHost('PC1')
        PC2 = self.addHost('PC2')
        PC3 = self.addHost('PC3')

        S1 = self.addSwitch('S1')
        S2 = self.addSwitch('S2')

        # Add links
        self.addLink(PC1, S1)
        self.addLink(PC2, S1)
        self.addLink(S1, S2, cls=TCLink, bw=20, delay="5ms")
        self.addLink(S2, PC3)

topos = { 'mytopo': ( lambda: MyTopology() ) } 