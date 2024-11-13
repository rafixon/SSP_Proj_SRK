# SSP_Proj_SRK

Projekt: Implementacja Mechanizmu Równoważenia Obciążenia w Sieciach SDN z Wykorzystaniem Kontrolera POX i Algorytmu Least Weighted Connections

Autorzy:
Rafał Mycek
Jakub Kostecki
Szymon Krzyworzeka

1.Topologia:


                   / --- h2
                  |
          h1 --- s1  --- h3
                  |
                   \ --- h4

Połączenia w topologii:
- h1 h1-eth0:s1-eth1
- h2 h2-eth0:s1-eth2
- h3 h3-eth0:s1-eth3
- h4 h4-eth0:s1-eth4
- s1 lo:  s1-eth1:h1-eth0 s1-eth2:h2-eth0 s1-eth3:h3-eth0 s1-eth4:h4-eth0
- c0

Plik w którym znajduje się topologia ma nazwę my_topo.py
aby otworzyć topologie proszę użyć: sudo mn --custom my_topo.py --topo mytopo
