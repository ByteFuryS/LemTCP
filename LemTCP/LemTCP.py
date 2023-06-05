import socket
import argparse
import concurrent.futures
from termcolor import colored
import os
#This project is licensed under the terms of the GNU General Public License v3.0. For more details, see the LICENSE file.
# Argümanları almak ve analiz etmek için bir ArgumentParser oluşturuyoruz
parser = argparse.ArgumentParser(description='Port tarama aracı.')
parser.add_argument('--ip', help='Taranacak IP adresi')  # Tarama yapılacak IP adresini belirtiriz
parser.add_argument('--port1', type=int, help='Taranacak port aralığının ilk portu')  # Port aralığının başlangıç noktası
parser.add_argument('--port2', type=int, help='Taranacak port aralığının ikinci portu')  # Port aralığının bitiş noktası
parser.add_argument('--output', help='Sonuçları yazdıracağınız dosya yolu')  # Sonuçları yazdırmak için dosya yolu
parser.add_argument('--only-open', action='store_true', help='Sadece açık portları göster')  # Sadece açık portları gösterme opsiyonu
args = parser.parse_args()  # Argümanları analiz eder

# Argümanlardan alınan değerleri belirleyici değişkenlere aktarırız
ip = args.ip
port1 = args.port1
port2 = args.port2
output_file = args.output
only_open = args.only_open

# Port tarama ve servis tespiti için fonksiyon
def port_tara(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Yeni bir TCP/IP soketi oluşturuyoruz
    sock.settimeout(4)  # Soketin zaman aşımı süresini belirliyoruz
    result = sock.connect_ex((ip, port))  # IP ve port için bağlantı oluşturma denemesi
    service_name = "Bilinmiyor"  # Varsayılan olarak servis ismi bilinmiyor
    if result == 0:  # Eğer bağlantı başarılıysa (port açıksa)
        try:
            service_name = socket.getservbyport(port)  # Servis ismini almayı deneyin
        except Exception as e:  # Hata durumunda servis ismi bilinmiyor olacak
            service_name = "Bilinmiyor"
    sock.close()  # Soketi kapatıyoruz
    return (port, result, service_name)  # Port numarası, bağlantı sonucu ve servis ismini döndürürüz

# Ekrana LemXat yazdırma
os.system("figlet -f Epic LemTCP | lolcat -a -d 3")

# Belirtilen port aralığındaki tüm portları tarıyoruz
with concurrent.futures.ThreadPoolExecutor(max_workers=300) as executor:
    portlar = range(port1, port2+1)  # Tarama yapılacak port aralığını belirliyoruz
    sonuclar = list(executor.map(port_tara, portlar))  # Her port için port_tara fonksiyonunu paralel olarak çalıştırıp sonuçları alıyoruz

# Sonuçları ekrana ve dosyaya yazdırıyoruz
if output_file:  # Eğer bir çıktı dosyası belirtildiyse
    with open(output_file, 'w') as f:  # Bu dosyayı yazma modunda açıyoruz
        for port, result, service_name in sonuclar:  # Tüm sonuçları tek tek işliyoruz
            if result == 0:  # Eğer port açıksa
                print(colored("Port {}: Açık, Servis: {}".format(port, service_name), "green"))  # Ekrana açık port bilgisini yazdırıyoruz
                f.write("Port {}: Açık, Servis: {}\n".format(port, service_name))  # Açık port bilgisini dosyaya yazdırıyoruz
            elif not only_open:  # Eğer "sadece açık portları göster" opsiyonu aktif değilse
                print(colored("Port {}: Kapalı".format(port), "red"))  # Kapalı port bilgisini ekrana yazdırıyoruz
                f.write("Port {}: Kapalı\n".format(port))  # Kapalı port bilgisini dosyaya yazdırıyoruz
    print("Sonuçlar {} dosyasına yazıldı.".format(output_file))  # Sonuçların dosyaya yazıldığı bilgisini ekrana yazdırıyoruz
else:  # Eğer çıktı dosyası belirtilmemişse
    for port, result, service_name in sonuclar:  # Tüm sonuçları tek tek işliyoruz
        if result == 0:  # Eğer port açıksa
            print(colored("Port {}: Açık, Servis: {}".format(port, service_name), "green"))  # Ekrana açık port bilgisini yazdırıyoruz
        elif not only_open:  # Eğer "sadece açık portları göster" opsiyonu aktif değilse
            print(colored("Port {}: Kapalı".format(port), "red"))  # Kapalı port bilgisini ekrana yazdırıyoruz


#This project is licensed under the terms of the GNU General Public License v3.0. For more details, see the LICENSE file.
