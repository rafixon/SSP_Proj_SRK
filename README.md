# SSP_Proj_SRK

## Projekt: Implementacja Mechanizmu Równoważenia Obciążenia w Sieciach SDN z Wykorzystaniem Kontrolera POX i Algorytmu Least Weighted Connections

Autorzy:
Rafał Mycek
Jakub Kostecki
Szymon Krzyworzeka

### 1. Uruchomienie środowiska:
*https://www.youtube.com/watch?v=c7l6TR1Ptic*
  * Wymagania sprzętowe
    1. OS; Ubuntu 24.04 lub nowszy
    2. Python 3.12
    3. Mininet 2.3

  * Pobrać repozytorium Mininet:`git clone https://github.com/mininet/mininet.git`
  * Po Mininet pobraniu: `sudo apt-get install mininet`
  * Pobrać repozytorium Pox: `git clone http://github.com/noxrepo/pox`
  * Pobrać aplikacje XTerm: `sudo apt-get xterm`

### 2. Topologia:
Plik single_switch_topo.py

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

aby otworzyć topologie proszę użyć: sudo mn --custom single_switch_topo.py --topo mytopo

### 3. Generator Ruchu:
Pliki generator_server.py oraz generator_client.py

Dwie aplikacje klienta oraz serwera
Serwer nasłuchujacy na podanym przez użytkownika porcie
Klient generujacy zapytania na porcie http 80 do wirtualnego serwera 10.0.1.1

aby włączyć serwer proszę użyć: sudo python3 generator_server.py <nazwa_serwera> <port_nasluchujacy>
aby włączyć klineta proszę użyć: sudo python3 generator_client.py

### 4. Loadbalancer:
Plik wlc_lb.py
Implementacja Load Balancera wykorzystujacego algorytm Least Weighted Connections.
Aplikacja oparta na programie James`a McCauley

Implementacja algorytmu:
XXXXX

Ponadto program obsługuje mechanizm ARP, dodawanie wpisów do tablicy przepływów FlowMod, oraz wysyłanie pakietów ze sterownika PacketOut

### 5. Uruchomienie projektu:

 1. Po zainstalowaniu środowiska z punktu 1 proszę pobrać poniższe pliki oraz zamieścić je w odpowiednich miejscach:
  * wlc_lb.py - /pox
  * single_switch_topo.py - folder /mininet
  * generator_server.py - dowolnie
  * generator_client.py - dowolnie
   
 2. Proszę przejść do katalogu /mininet i otworzyć topologie w mininecie za pomocą:
    sudo mn --custom single_switch_topo.py --topo singleswitch --controllers=remote, ip=127.0.0.1:6633

 3. Proszę przejść do katalogu /pox i otworzyć sterownik kontrolera pox za pomocą:
    python3 pox.py wlc_lb.py --ip=10.0.1.1 --servers=10.0.0.2,10.0.0.3,10.0.0.4
   
 4. Proszę otworzyć terminale urządzeń za pomocą xterm w konsoli mininet:
    xterm h1, xterm h2,...
   
 5. Na klientach od 2 do 4 proszę włączyć nasłuchujące serwery:
    h2: sudo python3 generator_server.py h2 80
    h3: sudo python3 generator_server.py h3 80
    h4: sudo python3 generator_server.py h4 80

 6. Na kliencie 1 proszę włączyć generator ruchu:
    h1: sudo python3 generator_client.py

 7. Prosze obserwować dystrybucję pakietów
    stosunek między serwerami wynosi 1:2:4
