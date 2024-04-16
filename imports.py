from gtts import gTTS
from pydub import AudioSegment
from IPython.display import Audio, clear_output
import requests


#Copyright

def download_image(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)
    

# Example usage:
url = "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgVfrydE3PZ-mi0eBJv0IuGp8A-B-a_3Ol-0ZSE0Fd-6uAK-bnCG0l2qT304X1-OwB2SHSmjPeapELNMmRraAOhMwb9maPd-q2aP41iMKXF35Ro-uGbsRpt9jtbyI05CqCwUGCR1KgtLpfSDGSkKouaT2ftQakF2ieonnIg0_sA_ZzyD2eqOwcdr64TUU4/s16000/copyright.jpg"
save_path = "/content/TTS_BahaaMahmoudTUT/BahaaMahmoud.jpg"
download_image(url, save_path)

# Clear the current cell's output
clear_output(wait=True)

print("هذا الكود بواسطة Bahaa Mahmoud TUT")

from IPython.display import Image, display, HTML
display(Image("BahaaMahmoud.jpg", width=520))


link = '<div style="direction: rtl; text-align: left;">✅&nbsp;<a href="https://www.youtube.com/channel/UCTQMuaUubjb4j0QKlg9NomQ" target="_blank">إضغط هنا</a>&nbsp;للمزيد من الشروحات علي قناتي. ✅</div>'
display(HTML(link))