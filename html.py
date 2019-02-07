def web_page(temp, oof, temp_percentage):
  html = """<html><head><meta http-equiv="refresh" content="3;<meta name="viewport" content="width=device-width, initial-scale=1">
  <style>body{padding: 20px; margin: auto; width: 50%; text-align: center;}
  .progress{background-color: #F5F5F5;} .progress.vertical{position: relative;
  width: 25%; height: 60%; display: inline-block; margin: 20px;}
  .progress.vertical > .progress-bar{width: 100% !important;position: absolute;bottom: 0;}
  .progress-bar{background: linear-gradient(to top, #f5af19 0%, #f12711 100%);}
  .progress-bar-hum{background: linear-gradient(to top, #9CECFB 0%, #65C7F7 50%, #0052D4 100%);}
  p{position: absolute; font-size: 1.5rem; top: 50%; left: 50%; transform: translate(-50%, -50%); z-index: 5;}</style></head>
  <body><h1>BME280 Sensor</h1><div class="progress vertical">
  <p>"""+str(temp)+""" C<p>
  <div role="progressbar" style="height: """+str(temp_percentage)+"""%;" class="progress-bar"></div></div><div class="progress vertical">
  <p>"""+str(oof)+""" %</p>
  <div role="progressbar" style="height: """+str(oof)+"""%;" class="progress-bar progress-bar-hum"></div></div></body></html>"""
  return html