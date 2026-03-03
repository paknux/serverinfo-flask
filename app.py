from flask import Flask, render_template
import socket
import psutil
import platform

app = Flask(__name__)

@app.route('/')
def index():
    # Mengambil informasi server
    hostname = socket.gethostname()
    try:
        ip_address = socket.gethostbyname(hostname)
    except:
        ip_address = "127.0.0.1"
        
    os_info = f"{platform.system()} {platform.release()}"
    
    # interval=None agar loading instan
    cpu_usage = psutil.cpu_percent(interval=None)
    ram_info = psutil.virtual_memory()
    
    return render_template(
        'index.html', 
        hostname=hostname, 
        ip_address=ip_address, 
        os_info=os_info,
        cpu_usage=cpu_usage,
        ram_percent=ram_info.percent,
        ram_used=round(ram_info.used / (1024**3), 2),
        ram_total=round(ram_info.total / (1024**3), 2)
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)