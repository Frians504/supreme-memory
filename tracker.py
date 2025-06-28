import requests, os
from time import sleep

def banner():
    os.system('clear')
    print("\033[1;32m")
    with open("assets/mr-frians-banner.txt") as b:
        print(b.read())
    print("\033[0m")

def get_location(phone_number):
    print(f"[+] Mencari lokasi untuk: {phone_number}")
    try:
        response = requests.get(f"http://ip-api.com/json/{phone_number}")
        data = response.json()
        if data['status'] == 'success':
            print(f"Negara     : {data['country']}")
            print(f"Kota       : {data['city']}")
            print(f"ISP        : {data['isp']}")
            print(f"Latitude   : {data['lat']}")
            print(f"Longitude  : {data['lon']}")
            map_link = f"https://www.google.com/maps?q={data['lat']},{data['lon']}"
            print(f"\n[+] Link Google Maps: {map_link}")
        else:
            print("Nomor tidak ditemukan atau tidak valid.")
    except:
        print("Gagal mengambil data!")

if __name__ == "__main__":
    banner()
    no = input("Masukkan nomor/ IP target: ")
    get_location(no)
