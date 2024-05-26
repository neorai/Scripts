import time
import psutil
import socket
import getpass
import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class USBEventHandler(FileSystemEventHandler):
    def __init__(self, usb_drive_letter):
        super().__init__()
        self.usb_drive_letter = usb_drive_letter
        self.printed_info = False  # Variable para controlar si la información ya se ha impreso

    def on_created(self, event):
        if event.is_directory:
            return

        filename = event.src_path

        if not self.printed_info:
            current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ip_address = socket.gethostbyname(socket.gethostname())
            computer_name = socket.gethostname()
            mac_address = ":".join(["%02x" % int(part, 16) for part in psutil.net_if_addrs()['Ethernet'][0].address.replace('-', ':').split(':')])[0:17]
            username = getpass.getuser()

            print("Información del sistema:")
            print(f"   - Fecha: {current_time}")
            print(f"   - IP: {ip_address}")
            print(f"   - Nombre del equipo: {computer_name}")
            print(f"   - Nombre de usuario: {username}")
            print(f"   - MAC Address: {mac_address}")
            self.printed_info = True

        print(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Archivo creado en {self.usb_drive_letter}: {filename}")

def get_usb_drives():
    partitions = psutil.disk_partitions()
    usb_drives = [partition.device for partition in partitions if 'removable' in partition.opts.lower()]
    return usb_drives

def monitor_usb_activity():
    previous_drives = set()
    while True:
        current_drives = set(get_usb_drives())
        new_drives = current_drives - previous_drives

        for new_drive in new_drives:
            print(f"Unidad USB detectada: {new_drive}")
            event_handler = USBEventHandler(new_drive)
            observer = Observer()
            observer.schedule(event_handler, path=new_drive + "\\", recursive=True)
            observer.start()

        removed_drives = previous_drives - current_drives
        for removed_drive in removed_drives:
            print(f"Unidad USB retirada: {removed_drive}")
            # Restablecer la variable cuando se retira la unidad USB
            if removed_drive in [handler.usb_drive_letter for handler in observer.event_handlers]:
                for handler in observer.event_handlers[:]:
                    if isinstance(handler, USBEventHandler) and handler.usb_drive_letter == removed_drive:
                        handler.printed_info = False
                        observer.event_handlers.remove(handler)

        previous_drives = current_drives
        time.sleep(2)

if __name__ == "__main__":
    monitor_usb_activity()
