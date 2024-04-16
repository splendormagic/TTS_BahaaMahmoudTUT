from gtts import gTTS
from pydub import AudioSegment
from IPython.display import Audio
import requests



def download_image(url, save_path):
    response = requests.get(url)
    with open(save_path, 'wb') as f:
        f.write(response.content)
    print("هذا الكود بواسطة Bahaa Mahmoud TUT")

# Example usage:
url = "https://bahaamahmoud.com/wp-content/uploads/2024/04/thumbnail-2.jpg"
save_path = "/content/TTS_BahaaMahmoudTUT/BahaaMahmoud.jpg"
download_image(url, save_path)


from IPython.display import Image, display, HTML
display(Image("BahaaMahmoud.jpg", width=320))


link = '<div style="direction: rtl; text-align: left;">✅&nbsp;<a href="https://www.youtube.com/channel/UCTQMuaUubjb4j0QKlg9NomQ" target="_blank">إضغط هنا</a>&nbsp;للمزيد من الشروحات علي قناتي. ✅</div>'
display(HTML(link))