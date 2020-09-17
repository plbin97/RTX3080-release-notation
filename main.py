from subprocess import call
import time
import requests
from datetime import datetime


isReleased = False

while True:

    searchString = """<a href='#' data-width='1024' data-height='579' data-analytics="btn-manual:3080-staticprice" data-title="Notify me" data-href='https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/notify-me-form/' target="overlay" id='3080-staticprice' class='  link-btn btn-manual lb_iframe brand-green regular-btn ' onclick='NVIDIAGDC.button.click(this, $(this).data(&quot;href&quot;),true, function() { ;return NVIDIAGDC.button.callbacks(this); }); return false;'><div class='btn'><span class="far fa fa-envelope fa-fw"></span> NOTIFY ME</div></a>"""

    requestResult = requests.get("https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3080/").text

    searchResult = requestResult.find(searchString)
    if searchString == -1 :
        isReleased = True
        break

    now = datetime.now()
    currentTime = now.strftime("%H:%M:%S")
    print(currentTime + " not release yet")
    time.sleep(5)

if isReleased:
    displayCommend = 'display notification \"' + \
                     "RTX 3080 released" + '\" with title \"Important!!!\"'
    voiceCommend = 'say "3080 has been released"'
    call(["osascript", "-e", displayCommend])
    print("RTX 3080 has been released")
    while True:
        call(["osascript", "-e", voiceCommend])
        time.sleep(1)
