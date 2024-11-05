def saisir_ip():
    ip = input("Veuiller saisir une addres IP: ")

#saisir_ip()


def est_ip_valide(ip):
    est_ip_valide=("192.168.1.1")
    print(f"verifiaction de l'addrese ip{ip} ")
    
    #est_ip_valide()


def est_segment_valide(segment):
    
    saisir_ip()
    if  ip.count('.') != 3:
        print("Adresse IP invalide : le format doit contenir 4 octets séparés par des points.")
    else:
        valide = True
    octets = ip.split('.')
    
    for octet in octets:
        if not octet.isdigit() or not (0 <= int(octet) <= 255):
            print(f"Octet non valide trouvé : {octet}")
            valide = False
            break
    
    if valide:
        print("Adresse IP valide.")




est_segment_valide()