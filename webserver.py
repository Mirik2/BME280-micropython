import usocket as socket
from machine import Pin, I2C
import BME280
import html

i2c = I2C(scl=Pin(22),sda=Pin(21), freq=10000)
bme = BME280.BME280(i2c=i2c)

def read_sensor():
  t = bme.temperature
  #p = bme.presure
  h = bme.humidity

  temp = t[0:-1]
  oof = h[0:-1]
  temp_percentage = (float(temp)+6/(40+6)*(100))
  return temp, oof, temp_percentage

# Denne funksjonen returnerer html koden 
def index(sensor, humidity):
  header = 'HTTP/1.0 200 OK\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'
  html = '''

<html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body>
        <h1>{} | {}</h1>
    </body>
</html>
'''.format(sensor, humidity)
  return header + html

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

  

while True:
  conn, addr = s.accept()
  print('Got a connection from %s' % str(addr))
  request = conn.recv(1024)
  print('Content = %s' % str(request))
  temp, oof, temp_percentage = read_sensor()
  print(temp, oof, temp_percentage)
  response = html.web_page(temp, oof, temp_percentage)

  conn.send('HTTP/1.1 200 OK\n')
  conn.send('Content-Type: text/html\n')
  conn.send('Connection: close\n\n')
  conn.sendall(response)
  conn.close()