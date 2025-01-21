# SSP_Proj_SRK

## Projekt: Implementacja Mechanizmu Równoważenia Obciążenia w Sieciach SDN z Wykorzystaniem Kontrolera POX i Algorytmu Least Weighted Connections

Autorzy:
Rafał Mycek
Jakub Kostecki
Szymon Krzyworzeka

### 1. Uruchomienie środowiska:
*https://www.youtube.com/watch?v=c7l6TR1Ptic*
  * Wymagania sprzętowe
    1. OS; Ubuntu 24.04
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
Klient generujacy zapytania na porcie http 80 do serwera pod virtuanym adresem 10.0.1.1

aby włączyć serwer proszę użyć: sudo python3 generator_server.py <nazwa_serwera> <port_nasluchujacy>
aby włączyć klineta proszę użyć: sudo python3 generator_client.py

### 4. Loadbalancer:
Plik wlc_lb.py
Implementacja Load Balancera wykorzystujacego algorytm Least Weighted Connections.

Dodano nowe słowniki:
self.server_connections - licznik aktywnych połączeń do serwerów.
self.server_weights - wagi przypisane do serwerów

Zmieniono sposób wyboru serwera w _pick_server(), zamiast losowego wyboru, teraz serwer wybierany jest na podstawie ilorazu liczby aktywnych połączeń do wagi serwera:
return min(self.server_connections, key=lambda s: self.server_connections[s] / self.server_weights[s])

Po wybraniu serwera w _handle_PacketIn(), zwiększana jest liczba jego aktywnych połączeń:
self.server_connections[server] += 1

Ponadto program obsługuje mechanizm ARP, dodawanie wpisów do tablicy przepływów FlowMod, oraz wysyłanie pakietów ze sterownika PacketOut

### 5. Uruchomienie projektu:

1. Po zainstalowaniu środowiska z punktu 1 proszę pobrać poniższe pliki oraz zamieścić je w odpowiednich miejscach:
 * wlc_lb.py - /pox/pox/misc
 * single_switch_topo.py - folder /mininet
 * generator_server.py - dowolnie
 * generator_client.py - dowolnie

2. Proszę przejść do katalogu /pox i otworzyć sterownik kontrolera pox za pomocą:
   root@ubuntu:~/pox$ python3 pox.py wlc_lb --ip=10.0.1.1 --servers=10.0.0.2,10.0.0.3,10.0.0.4
   
4. Proszę przejść do katalogu /mininet i otworzyć topologie w mininecie za pomocą:;
   root@ubuntu:~/mininet$ sudo mn --custom single_switch_topo.py --topo singleswitch --controller=remote,ip=127.0.0.1:6633
   
5. Proszę otworzyć terminale urządzeń za pomocą xterm w konsoli mininet:

   mininet > xterm h1
   mininet > xterm h2
   mininet > xterm h3
   mininet > xterm h4
   
6. Na klientach od 2 do 4 proszę włączyć nasłuchujące serwery:
   h2: sudo python3 generator_server.py h2 80
   h3: sudo python3 generator_server.py h3 80
   h4: sudo python3 generator_server.py h4 80

7. Na kliencie 1 proszę włączyć generator ruchu:
   h1: sudo python3 generator_client.py

8. Prosze obserwować dystrybucję pakietów
   stosunek między serwerami wynosi 1:2:4
