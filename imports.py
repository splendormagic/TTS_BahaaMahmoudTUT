from gtts import gTTS
from pydub import AudioSegment
from IPython.display import Audio, clear_output, display, HTML
import requests

# Clear the current cell's output
#clear_output(wait=True)

copyright = '<div style="background-color: #dff2bf; border: 1px solid rgb(79, 138, 16); color: #4f8a10; padding: 10px;"><div class="separator" style="clear: both; direction: rtl; text-align: left;"><span style="font-family: arial; font-size: medium;">هذا الكود بواسطة Bahaa Mahmoud TUT</span></div><div class="separator" style="clear: both; direction: rtl; text-align: left;"><span style="font-family: arial; font-size: medium;"><br /></span></div><div class="separator" style="clear: both; direction: rtl; text-align: left;"><div class="separator" style="clear: both; text-align: center;"><a href="https://www.youtube.com/channel/UCTQMuaUubjb4j0QKlg9NomQ" style="clear: left; float: left; margin-bottom: 1em; margin-right: 1em;"><img border="0" data-original-height="170" data-original-width="600" height="170" src="https://bahaamahmoud.com/wp-content/uploads/2024/04/copyright.jpg" width="600" /></a></div></div><div class="separator" style="clear: both; direction: rtl; text-align: left;"><span style="font-family: arial; font-size: medium;"><br /></span></div><div style="direction: rtl; text-align: left;"><span style="font-family: arial; font-size: medium;">✅&nbsp;<a href="https://www.youtube.com/channel/UCTQMuaUubjb4j0QKlg9NomQ" target="_blank">إضغط هنا</a>&nbsp;للمزيد من الشروحات علي قناتي. ✅</span></div></div>'
display(HTML(copyright))