# IPinfo
>Small Python GUI build with Customtkinter, that reveals your current IPv4 Adresse, Geolocation (Country Code) and Country Flag.


# How it Works
When you start IPinfo you are greeted with a modern looking GUI that displays your IPv4, Geolocation and Country Flag. If you press the button it will change to a progressbar and the data from browserleaks and flagsapi will appear one for another. When the process is finished all your data is displayed and the progressbar is now again a button, which can initiate the next refresh if pressed.


# How it looks
![grafik](https://github.com/NiiV3AU/IPinfo/assets/86131759/271e5dd9-1751-486a-aae8-71d6413419f0)
### What you can't see here are the nice animations of the button and the credits.
> Also fyi if youre wondering why IPinfo shows N/A aka Not Available rather then the actual data, its because you need to click the refresh button at the bottom to start the data collection. If the GUI started with the data already scraped, then the GUI would not feel as responsive as it currently is.


# How to Use
### Install the newest release here: 
| [Download IPinfo.exe](https://github.com/NiiV3AU/IPinfo/releases/latest/download/IPinfo.exe) |
| ------------- |

### Or simply run the Python File if you have all Requirements and Dependecies installed:
| [Download Source Code](https://github.com/NiiV3AU/IPinfo/archive/refs/heads/main.zip) | [Check Requirements and Dependencies](https://github.com/NiiV3AU/IPinfo?tab=readme-ov-file#requirements-and-dependencies) |
| ------------- | ------------- |


# Use Cases
Very limited, gets the info as fast as simply visiting [BrowserLeaks](https://browserleaks.com) by itself.
> *'psst*~ it looks cooler :)


# Why then, you ask?
The Project teached me new things as using threading for a more responsive gui, scraping the web with bs4 (BeautifulSoup) and improved my overall python skills. I also uploaded the project on GitHub to get some feedback on my code, so I would appreciate it if you would take your time reviewing my code on flaws etc.


# Requirements and Dependencies
## Programming Language
| [Python](https://python.org) |
| ------------- |
>I used Version 3.12.2 while coding IPinfo

## Libraries
| __Library__ | __pip command__ |                                                          
| ------------- | ------------- |                                                          
| [requests](https://pypi.org/project/requests/) | `pip install requests` |               
| [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) | `pip install bs4` |          
| [customtkinter](https://pypi.org/project/customtkinter/) | `pip install customtkinter` |  
| [pillow](https://pypi.org/project/pillow/) | `pip install Pillow` |                      

## Fonts
| __Fonts__ |
| ------------- |
| [Manrope](https://fonts.google.com/specimen/Manrope) |
| [JetBrains Mono](https://www.jetbrains.com/lp/mono/) |


# Credits
| Data Type | Source |
| ------------- | ------------- |
| IP & Geo Data | [BrowserLeaks](https://browserleaks.com) |
| Flag PNGs | [FlagsAPI](https://flagsapi.com/) |
| Fonts | __Look north__ |
