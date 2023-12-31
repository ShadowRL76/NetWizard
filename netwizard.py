import socket
from scapy.all import *
import pyfiglet 
import termcolor
import argparse
import netifaces
from getmac import *
import time
import os
import requests 
import random
import subprocess
import importlib

class NetWizard():
    def __init__(self):
        self.print_banner()
        self.eth_mac = get_mac_address(interface="en0")
        self.wlan0_mac = get_mac_address(interface="wlan0")
        self.wlan0mon_mac = get_mac_address(interface="wlan0mon")
        self.clear_and_print()



    def Mac_Address_Interface_Menu(self):
        while True:
            print("1) wlan0")
            print("2) wlan0mon")
            print("3) eth0")
            print("b) Main menu")
            print("0) EXIT")
            user_input = input("Choose: ")
    

            if user_input == '1':
                self.clear_screen()
                try:
                    if self.wlan0_mac:
                        print(f"Your MAC address is: {self.wlan0_mac}")
                    else:
                        raise Exception("Network interface 'wlan0' not found or MAC address is unavailable.")
        
                    input("Press Enter to continue...")
                    self.clear_screen()
                    self.MacAddressInterfaceMenu()
                except Exception as e:
                    self.clear_and_print()
                    print()
                    print(f"An error occurred: {e}")
                    print()
                    input("Press Enter to continue...")
                    self.clear_and_print()
            
            elif user_input == '2':
                self.clear_screen()
                try:
                    if self.wlan0mon_mac:
                        print(f"Your MAC address is: {self.wlan0mon_mac}")
                    else:
                        raise Exception("Network interface 'wlan0' not found or MAC address is unavailable.")
                    self.clear_and_print()
                    input("Press Enter to continue...")
                    self.clear_screen()
                    self.MacAddressInterfaceMenu()
                except Exception as e:
                    self.clear_and_print()
                    print()
                    print(f"An error occurred: {e}")
                    print()
                    input("Press Enter to continue...")
                    self.clear_and_print()
            
            
            elif user_input == '3':
                self.clear_screen()
                try:
                    if self.eth_mac:
                        print(f"Your MAC address is: {self.eth_mac}")
                    else:
                        raise Exception("Network interface 'wlan0' not found or MAC address is unavailable.")
        
                    input("Press Enter to continue...")
                    self.clear_screen()
                    self.MacAddressInterfaceMenu()
                except Exception as e:
                    self.clear_and_print()
                    print()
                    print(f"An error occurred: {e}")
                    print()
                    input("Press Enter to continue...")
                    self.clear_and_print()

            
            elif user_input == 'b':
                self.clear_and_print()
                self.menuOptions()
            
            elif user_input == '0':
                        self.quit()
            

    
    def menuOptions(self):
        while True:
            print("ifc) ifconfig\t          l) local IPs & gateways | scan) Arp-scan network")
            print("1) Enable wlan0\t         d1) Disable wlan0        | start) Start monitor mode")
            print("2) Enable wlan0mon\t d2) Disable wlan0mon     | stop) Stop monitor mode")
            print("3) Change Mac\t         d3) Restore original MAC | update) Check for updates")
            print("4) Enable anonym8\t d4) Disable anonym8      | errors) Fix some errors")
            print("5) Enable anonsurf\t d5) Disable anonssurf    | ks) keyboard shortcuts")
            print("6) Anonssurf's status\t d6) Restart anonssurf    | d) Buy me a coffee")
            print("7) View public IP\t d7) anonym8 menu         | s) Go to settings menu")
            print("8) View MAC")
            print("9) TOOLS \t         15) Spoof EMAIL")
            print("10) Handshake \t         16) Ngrok port forward")
            print("11) Find WPS pin\t 17) Ask (Howdoi tool)")
            print("12) WEP hacking \t 18) Auto-exploit browser")
            print("13) MITM \t         19) Geolocate an IP") 
            print("14) Metasploit           20) PortScanner")    
            print("0) EXIT")
            print()
            user_input = input("Enter an option: ")

            
            if user_input.lower() == 'ifc':
                self.clear_and_print()
                print(f"Your network interfaces are {conf.ifaces}")
                print()
                print()
                print("Click enter to return")
                if input() == '\n':
                    self.menuOptions()
                self.clear_and_print()
            

            elif user_input == '1':
                pass


            elif user_input == '2':
                pass


            elif user_input == '3':
                pass


            elif user_input == '4':
                self.anonym8_install_menu()


            elif user_input == '5':
                self.anonsurf_install_menu()


            elif user_input == '6':
                pass


            elif user_input == '7':
                self.clear_screen()
                try:
                    self.print_banner()
                    print(f"Your public IP is: {requests.get('http://ip.42.pl/raw').text}")
                    print()
                    print()
                    print("Click enter to return")
                    if input() == '\n':
                        self.menuOptions()
                    self.clear_and_print()
                except Exception as e:
                    print("Error: No public IP address found")

            elif user_input == '8':
                self.clear_and_print()
                self.Mac_Address_Interface_Menu()

            elif user_input == '9':
                pass


            elif user_input == '10':
                pass


            elif user_input == '11':
                pass


            elif user_input == '12':
                pass


            elif user_input == '13':
                pass


            elif user_input == '14':
               pass


            elif user_input == '15':
                pass


            elif user_input == '16':
                pass


            elif user_input == '17':
                pass


            elif user_input == '18':
               pass


            elif user_input == '19':
                pass


            elif user_input == '20':
                self.clear_and_print()
                PortScanner()
                print()
                input('Press enter to continue...')
                self.clear_and_print()


            elif user_input == '0':
                self.quit()


            elif user_input == 'd1':
                pass


            elif user_input == 'd2':
                pass


            elif user_input == 'd3':
                pass


            elif user_input == 'd4':
                self.anonym8_stop_command()


            elif user_input == 'd5':
                self.anonsurf_stop_menu()


            elif user_input == 'd6':
                self.anonsurf_restart_menu()

            elif user_input == 'd7':
                self.anonym8_menu()

            elif user_input == 'l':
                pass


            elif user_input == 'scan':
                pass


            elif user_input == 'start':
                pass


            elif user_input == 'stop':
                pass


            elif user_input == 'update':
                pass


            elif user_input == 'errors':
                pass


            elif user_input == 'ks':
                pass


            elif user_input == 'ds':
                pass


            elif user_input == 's':
               pass

            
            elif user_input == 'r':
                subprocess.run(['reboot'])

            else:
                print("Thats not an option!")
                time.sleep(0.5)
                self.clear_and_print()
                self.menuOptions()

    
    def anonym8_menu(self):
        self.clear_and_print()
        while True:
            print("1) ---[ Tor tunneling features ]---")
            print("2) ---[ IP related features ]---")
            print("3) ---[ I2P related features ]---")
            print("4) ---[ privoxy related features ]---")
            print("5) ---[ macchanger related features ]---")
            print("6) ---[ arm related features ]---")
            print("7) ---[ wipe related features ]---")
            print("8) ---[ hostname related features ]---")
            print("b  ---[ back to main menu ]---")
            print("0  ---[ exits the program ]")
            user_input = input("Choose: ")

            while True:
                if user_input == '1':
                    self.clear_and_print()
                    print("1) anonym8 start                 => Start Tor Tunneling")
                    print("2) anonym8 stop                  => Stop Tor Tunneling")
                    print("3) anonym8 change                => Changes identity restarting TOR")
                    print("4) anonym8 status                => Tor Tunneling Status")
                    print("b) Main menu                     => Returns to Main Menu")
                    print("0) EXIT                          => Exit's the program")
                    
                    sub_tunneling_input = input("Choose: ")
                    
                    if sub_tunneling_input == '1':
                        self.anonym8_install_menu()
                    
                    elif sub_tunneling_input == '2':
                        self.anonym8_stop_command()

                    elif sub_tunneling_input == '3':
                        self.anonym8_change_command()

                    elif sub_tunneling_input == '4':
                        self.anonym8_status_command()

                    elif sub_tunneling_input == 'b':
                        self.clear_and_print()
                        self.menuOptions()
                    
                    elif sub_tunneling_input == '0':
                        self.quit()


                elif user_input == '2':
                    self.clear_and_print()
                    print("1) anonym8 status_ip             => IP status")
                    print("b) Main menu                     => Returns to Main Menu")
                    print("0) EXIT                          => Exit's the program")
                    
                    sub_status_ip = input("Choose: ")

                    if sub_status_ip == '1':
                        self.anonym8_ip_status()

                    elif sub_status_ip == 'b':
                        self.clear_and_print()
                        self.menuOptions()
                    
                    elif sub_status_ip == '0':
                        self.quit()

                elif user_input == '3':
                    self.clear_and_print()
                    print("1) anonym8 start_i2p             => Start i2p services")
                    print("3) anonym8 stop_i2p              => Stop i2p services")
                    print("3) anonym8 status_i2p            => i2P status")
                    print("b) Main menu                     => Returns to Main Menu")
                    print("0) EXIT                          => Exit's the program")

                    i2p_input = input("Choose: ")

                    if i2p_input == '1':
                        self.anonym8_start_i2p()
                    
                    elif i2p_input == '2':
                        self.anonym8_stop_i2p()
                    
                    elif i2p_input == '3':
                        self.anonym8_status_command()
                    
                    elif i2p_input == 'b':
                        self.clear_and_print()
                        self.menuOptions()
                    
                    elif i2p_input == '0':
                        self.quit()
                    
                        


                elif user_input == '4':
                    self.clear_and_print()
                    print("1) anonym8 start_privoxy         => Start privoxy services")
                    print("2) anonym8 stop_privoxy          => Stop privoxy services")
                    print("3) anonym8 status_privoxy        => Privoxy status")
                    print("b) Main menu                     => Returns to Main Menu")
                    print("0) EXIT                          => Exit's the program")
                    
                    privoxy_input = input("Choose: ")

                    if privoxy_input == '1':
                        self.anonym8_privoxy_start()
                    
                    elif privoxy_input == '2':
                        self.anonym8_privoxy_stop()
                    
                    elif privoxy_input== '3':
                        self.anonym8_privoxy_status()
                    
                    elif privoxy_input == 'b':
                        self.clear_and_print()
                        self.menuOptions()
                    
                    elif privoxy_input == '0':
                        self.quit()



                
                elif user_input == '5':
                    self.clear_and_print()
                    print("1) anonym8 start_mac             => Start macchanger services")
                    print("2) anonym8 stop_mac              => Stop macchanger services")
                    print("3) anonym8 status_mac            => macchanger status")
                    print("b) Main menu                     => Returns to Main Menu")
                    print("0) EXIT                          => Exit's the program")
                    
                    mac_input = input("Choose: ")

                    if mac_input == '1':
                        self.anonym8_mac_start()
                    
                    elif mac_input == '2':
                        self.anonym8_mac_stop()
                    
                    elif mac_input== '3':
                        self.anonym8_mac_status()
                    
                    elif mac_input == 'b':
                        self.clear_and_print()
                        self.menuOptions()
                    
                    elif mac_input == '0':
                        self.quit()



                elif user_input == '6':
                    self.clear_and_print()
                    print("1) anonym8 start_arm             => Start Monitoring Anonymizing Relay  (arm)")
                    print("b) Main menu                     => Returns to Main Menu")
                    print("0) EXIT                          => Exit's the program")
                    
                    arm_input = input("Choose: ")

                    if arm_input == '1':
                        self.anonym8_start_arm()

                    elif arm_input == 'b':
                        self.clear_and_print()
                        self.menuOptions()
                    
                    elif arm_input == '0':
                        self.quit()


                elif user_input == '7':
                    self.clear_and_print()
                    print("1) anonym8 wipe                  => cache, RAM & swap-space cleaner")
                    print("b) Main menu                     => Returns to Main Menu")
                    print("0) EXIT                          => Exit's the program")
                    
                    wipe_input = input("Choose: ")

                    if wipe_input == '1':
                        self.anonym8_wipe()

                    elif wipe_input == 'b':
                        self.clear_and_print()
                        self.menuOptions()
                    
                    elif wipe_input == '0':
                        self.quit()



                elif user_input == '8':
                    self.clear_and_print()
                    print("1) anonym8 change_hostname       => Randomly Spoofing hostname")
                    print("2) anonym8 restore_hostname      => Restore Default hostname")
                    print("3) anonym8 status_hostname       => Show Current Hostname")
                    print("b) Main menu                     => Returns to Main Menu")
                    print("0) EXIT                          => Exit's the program")

                    hostname = input("Choose: ")

                    if hostname == '1':
                        self.anonym8_change_hostname()
                    
                    elif hostname == '2':
                        self.anonym8_restore_hostname()
                    
                    elif hostname == '3':
                        self.anonym8_status_hostname()
                    
                    elif hostname == 'b':
                        self.clear_and_print()
                        self.menuOptions()
                    
                    elif hostname == '0':
                        self.quit()





    def anonym8_stop_command(self):
        self.clear_and_print()
        package_dir = 'anonym8'
        home_dir = os.path.expanduser("~")
        stop_command = 'anonym8 stop'
        try:
            os.chdir(os.path.join(home_dir, package_dir))
            subprocess.run(stop_command, shell=True)
            self.returnInput()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.returnInput()


    def anonym8_change_command(self):
        self.clear_and_print()
        package_dir = 'anonym8'
        home_dir = os.path.expanduser("~")
        change_command = 'anonym8 change'
        try:
            os.chdir(os.path.join(home_dir, package_dir))
            subprocess.run(change_command, shell=True)
            self.returnInput()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.returnInput()


    def anonym8_status_command(self):
        self.clear_and_print()
        package_dir = 'anonym8'
        home_dir = os.path.expanduser("~")
        status_command = 'anonym8 status'
        try:
            os.chdir(os.path.join(home_dir, package_dir))
            subprocess.run(status_command, shell=True)
            self.returnInput()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.returnInput()


    def anonym8_ip_status(self):
        self.clear_and_print()
        package_dir = 'anonym8'
        home_dir = os.path.expanduser("~")
        ip_status_command = 'anonym8 status_ip'
        try:
            os.chdir(os.path.join(home_dir, package_dir))
            subprocess.run(ip_status_command, shell=True)
            self.returnInput()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.returnInput()


    def anonym8_start_i2p(self):
        self.clear_and_print()
        package_dir = 'anonym8'
        home_dir = os.path.expanduser("~")
        start_ip2_command = 'anonym8 start_i2p'
        try:
            os.chdir(os.path.join(home_dir, package_dir))
            subprocess.run(start_ip2_command, shell=True)
            self.returnInput()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.returnInput()

    def anonym8_stop_i2p(self):
        self.clear_and_print()
        package_dir = 'anonym8'
        home_dir = os.path.expanduser("~")
        stop_ip2_command = 'anonym8 stop_i2p'
        try:
            os.chdir(os.path.join(home_dir, package_dir))
            subprocess.run(stop_ip2_command, shell=True)
            self.returnInput()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.returnInput()

    def anonym8_i2p_status(self):
        self.clear_and_print()
        package_dir = 'anonym8'
        home_dir = os.path.expanduser("~")
        status_ip2_command = 'anonym8 status_i2p'
        try:
            os.chdir(os.path.join(home_dir, package_dir))
            subprocess.run(status_ip2_command, shell=True)
            self.returnInput()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.returnInput()


    def anonym8_privoxy_start(self):
        self.clear_and_print()
        package_dir = 'anonym8'
        home_dir = os.path.expanduser("~")
        start_privoxy_command = 'anonym8 start_privoxy'
        try:
            os.chdir(os.path.join(home_dir, package_dir))
            subprocess.run(start_privoxy_command, shell=True)
            self.returnInput()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.returnInput()

    
    def anonym8_privoxy_stop(self):
        self.clear_and_print()
        package_dir = 'anonym8'
        home_dir = os.path.expanduser("~")
        stop_privoxy_command = 'anonym8 stop_privoxy'
        try:
            os.chdir(os.path.join(home_dir, package_dir))
            subprocess.run(stop_privoxy_command, shell=True)
            self.returnInput()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.returnInput()


    def anonym8_privoxy_status(self):
        self.clear_and_print()
        package_dir = 'anonym8'
        home_dir = os.path.expanduser("~")
        privoxy_status_command = 'anonym8 status_privoxy'
        try:
            os.chdir(os.path.join(home_dir, package_dir))
            subprocess.run(privoxy_status_command, shell=True)
            self.returnInput()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.returnInput()

    
    def anonym8_mac_start(self):
        self.clear_and_print()
        package_dir = 'anonym8'
        home_dir = os.path.expanduser("~")
        privoxy_status_command = 'anonym8 start_mac'
        try:
            os.chdir(os.path.join(home_dir, package_dir))
            subprocess.run(privoxy_status_command, shell=True)
            self.returnInput()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.returnInput()
        
    def anonym8_mac_stop(self):
        self.clear_and_print()
        package_dir = 'anonym8'
        home_dir = os.path.expanduser("~")
        privoxy_status_command = 'anonym8 stop_mac'
        try:
            os.chdir(os.path.join(home_dir, package_dir))
            subprocess.run(privoxy_status_command, shell=True)
            self.returnInput()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.returnInput()
        
    def anonym8_mac_status(self):
        self.clear_and_print()
        package_dir = 'anonym8'
        home_dir = os.path.expanduser("~")
        privoxy_status_command = 'anonym8 status_mac'
        try:
            os.chdir(os.path.join(home_dir, package_dir))
            subprocess.run(privoxy_status_command, shell=True)
            self.returnInput()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.returnInput()
        
    def anonym8_start_arm(self):
        self.clear_and_print()
        package_dir = 'anonym8'
        home_dir = os.path.expanduser("~")
        arm_start_command = 'anonym8 start_arm'
        try:
            os.chdir(os.path.join(home_dir, package_dir))
            subprocess.run(arm_start_command, shell=True)
            self.returnInput()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.returnInput()

    def anonym8_wipe(self):
        self.clear_and_print()
        package_dir = 'anonym8'
        home_dir = os.path.expanduser("~")
        wipe_command = 'anonym8 wipe'
        try:
            os.chdir(os.path.join(home_dir, package_dir))
            subprocess.run(wipe_command, shell=True)
            self.returnInput()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.returnInput()


    def anonym8_change_hostname(self):
        self.clear_and_print()
        package_dir = 'anonym8'
        home_dir = os.path.expanduser("~")
        change_hostname_command = 'anonym8 change_hostname'
        try:
            os.chdir(os.path.join(home_dir, package_dir))
            subprocess.run(change_hostname_command, shell=True)
            self.returnInput()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.returnInput()


    def anonym8_restore_hostname(self):
        self.clear_and_print()
        package_dir = 'anonym8'
        home_dir = os.path.expanduser("~")
        hostname_restore_command = 'anonym8 restore_hostname'
        try:
            os.chdir(os.path.join(home_dir, package_dir))
            subprocess.run(hostname_restore_command, shell=True)
            self.returnInput()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.returnInput()


    def anonym8_status_hostname(self):
        self.clear_and_print()
        package_dir = 'anonym8'
        home_dir = os.path.expanduser("~")
        hostname_status_command = 'anonym8 status_hostname'
        try:
            os.chdir(os.path.join(home_dir, package_dir))
            subprocess.run(hostname_status_command, shell=True)
            self.returnInput()
        except Exception as e:
            print(f"An error occurred: {e}")
            self.returnInput()





    def anonym8_install_menu(self):
        self.clear_and_print()
        try:
            package_name = 'anonym8'
            package = "git clone https://github.com/HiroshiManRise/anonym8.git"
            package_dir = 'anonym8'
            home_dir = os.path.expanduser("~")
            start_command = 'anonym8 start'
            print("User's home directory:", home_dir)

            print("Current working directory:", os.getcwd())
            print("Trying to change to directory:", home_dir)

            if not os.path.exists(os.path.join(home_dir, package_dir)):
                user_install = input(f"The package {package_name} is not installed. Would you like to install it? (Y, N)")
                if user_install == 'Y':
                    self.clear_and_print()
                    os.chdir(home_dir)
                    subprocess.run(package, shell=True, check=True)
                    os.chdir(package_dir)
                    subprocess.run(["chmod", "+x", "INSTALL.sh"])
                    subprocess.run(['./INSTALL.sh'], check=True)
            else:
                try:
                    os.chdir(os.path.join(home_dir, package_dir))
                    subprocess.run(start_command, shell=True)
                    print("anonym8 started")
                except Exception as e:
                    print(f"An error occurred: {e}")

        except Exception as e:
            print(f"An error occurred: {e}")
        print()
        self.returnInput()


    def anonsurf_install_menu(self):
        self.clear_and_print()
        try:
            package_name = 'kali-anonsurf'
            package = "git clone https://github.com/Und3rf10w/kali-anonsurf.git"
            package_dir = 'kali-anonsurf'
            home_dir = os.path.expanduser("~")
            print("User's home directory:", home_dir)

            print("Current working directory:", os.getcwd())
            print("Trying to change to directory:", home_dir)

            if not os.path.exists(os.path.join(home_dir, package_dir)):
                user_install = input(f"The package {package_name} is not installed. Would you like to install it? (Y, N)")
                if user_install == 'Y':
                    self.clear_and_print()
                    os.chdir(home_dir)
                    subprocess.run(package, shell=True, check=True)
                    os.chdir(package_dir)
                    subprocess.run(['./installer.sh'], check=True)
            else:
                try:
                    os.chdir(os.path.join(home_dir, package_dir))
                    start_command = 'anonsurf start'
                    subprocess.run(start_command, shell=True)
                    print("Anonsurf started")
                except Exception as e:
                    print(f"An error occurred: {e}")

        except Exception as e:
            print(f"An error occurred: {e}")
        print()
        self.returnInput()


    def anonsurf_stop_menu(self):
        self.clear_and_print()
        home_dir = os.path.expanduser("~")
        package_dir = 'kali-anonsurf'
        stop_command = 'anonsurf stop'
        try:
            os.chdir(os.path.join(home_dir, package_dir))
            subprocess.run(stop_command, shell=True)
            print("Anonsurf stopped successfully")
        except Exception as e:
            print(f"An error occurred: {e}")


    def anonsurf_restart_menu(self):
        self.clear_and_print()
        home_dir = os.path.expanduser("~")
        package_dir = 'kali-anonsurf'
        restart_command = 'anonsurf restart'
        try:
            os.chdir(os.path.join(home_dir, package_dir))
            subprocess.run(restart_command, shell=True)
            print("Anonsurf restart successfully")
        except Exception as e:
            print(f"An error occurred: {e}")
        self.returnInput()







    def returnInput(self):
            print("Click enter to return...")
            input() == '\n'
            self.clear_screen()
            self.print_banner()
            self.menuOptions()

        

    def option_not_found(self):
        print("Option not found")
        time.sleep(1)
        self.clear_screen()
        self.print_banner()


    def clear_screen(self):
        os.system('clear')

    def clear_and_print(self):
        self.clear_screen()
        self.print_banner()

    def print_banner(self):
        banner = pyfiglet.Figlet(font='doom')
        banner_text = banner.renderText('NetWizard')
        colored_banner = termcolor.colored(banner_text, 'red', 'on_black')
        print(colored_banner)


    def quit(self):
        banner = pyfiglet.Figlet(font='doom')
        banner_text = banner.renderText('Goodbye')
        colored_banner = termcolor.colored(banner_text, 'red', 'on_black')
        print(colored_banner)
        quit()


        
class PortScanner:
    def __init__(self):
        self.open_ports = []
        #Sock stream is TCP 
        self.IP_ADDRESS = input("Type in an IP address: ")
        self.PORT_NUMBER = input("Type in a Port number: ")
        if self.PORT_NUMBER.lower() == "all":
            for port in range(0,65536):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    try:
                        s.settimeout(5)
                        s.connect((self.IP_ADDRESS, port))
                        self.open_ports.append(port)  # Store open port in the list
                        print(f"Connection Successfully established")
                    except Exception as e:
                        print(f"Failed to connect to {port}: {e}")
                        pass
        else:
            try:
                self.PORT_NUMBER = int(self.PORT_NUMBER)
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    try:
                        s.settimeout(5)
                        s.connect((self.IP_ADDRESS, self.PORT_NUMBER))
                        self.open_ports.append(self.PORT_NUMBER)  
                        print(f"Connection successfully established on port {self.PORT_NUMBER}")
                    except Exception as e:
                        print(f"Failed to connect to port {self.PORT_NUMBER}: {e}")
            except ValueError:
                print("Invalid input. Please enter a valid port number or 'all' for all ports.")


            print(f"Open ports on {self.IP_ADDRESS}: {self.open_ports}")
       
       

      
if __name__ == '__main__':
    net_wizard = NetWizard()
    net_wizard.menuOptions()
    
