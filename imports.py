from gtts import gTTS
from pydub import AudioSegment
from IPython.display import Audio, clear_output, display, HTML
import requests

# Clear the current cell's output
#clear_output(wait=True)

copyright = '<div style="background-color: #dff2bf; border: 1px solid rgb(79, 138, 16); color: #4f8a10; padding: 10px;"><div class="separator" style="clear: both; direction: rtl; text-align: left;"><span style="font-family: arial; font-size: medium;">هذا الكود بواسطة Bahaa Mahmoud TUT</span></div><div class="separator" style="clear: both; direction: rtl; text-align: left;"><br /></div><div class="separator" style="clear: both; direction: rtl; text-align: left;"><a href="https://www.youtube.com/channel/UCTQMuaUubjb4j0QKlg9NomQ" style="margin-left: 1em; margin-right: 1em;" target="_blank"><img border="0" data-original-height="170" data-original-width="600" height="114" src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjPtDh1Q5HSkuMzb0tFLJ1_EArRMWY4qyfUmhGNo3rSwhtlEgDulg0hz3RbRvDtElzFVnyBlC49Vi1zOzuWrjIAYqKX1nNVyp1in3nCgLJS04QOsb6mzDPP9HHuG_kbpNILJc619RQ4meIeYtkPWwIS0WN_NMnMzHKTYi04WdeBH5RfvQHN9meXMVbX_yM/w400-h114/copyright.jpg" width="400" /></a></div><div style="direction: rtl; text-align: left;"><br /></div><div style="direction: rtl; text-align: left;"><span style="font-family: arial; font-size: medium;">✅&nbsp;<a href="https://www.youtube.com/channel/UCTQMuaUubjb4j0QKlg9NomQ" target="_blank">إضغط هنا</a>&nbsp;للمزيد من الشروحات علي قناتي. ✅</span></div></div>'
display(HTML(copyright))