# IPinfo
>Small Python GUI build with Customtkinter, that reveals your current IPv4 Adresse, Geolocation (Country Code) and Country Flag.


# How it Works
When you start IPinfo you are greeted with a modern looking GUI that displays your IPv4, Geolocation and Country Flag. First you can choose between different APIs. If you press the button it will change to a progressbar and the data from your chosen api and the flag from flagsapi will appear one for another in the GUI. When the process is finished all your data is displayed and the progressbar is now again a button, which can initiate the next refresh if pressed.


# How it looks

![grafik](https://github.com/NiiV3AU/IPinfo/assets/86131759/e300cf46-0bfd-480f-b4b9-80e63ca21b41)
![grafik](https://github.com/NiiV3AU/IPinfo/assets/86131759/271e5dd9-1751-486a-aae8-71d6413419f0)
> v1.0.1 vs v1.0.0

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
Very limited, gets the info as fast as simply visiting [BrowserLeaks](https://browserleaks.com), [IP2Location](https://ip2location.com) or [ipify](https://ipify.org) in your Browser.
> *'psst*~ it looks cooler :)


# Why then, you ask?
The Project teached me new things as using threading for a more responsive gui, scraping the web with bs4 (BeautifulSoup) and improved my overall python skills. I also uploaded the project on GitHub to get some feedback on my code, so I would appreciate it if you would take your time reviewing my code on flaws etc.


# Requirements and Dependencies
| __Programming Language:__ | [Python](https://python.org) |
| ------------- | ------------- |
>I used Version 3.12.2 while coding IPinfo

## Libraries
| __Library__ | __pip command__ |                                                          
| ------------- | ------------- |                                                          
| [requests](https://pypi.org/project/requests/) | `pip install requests` |               
| [beautifulsoup4](https://pypi.org/project/beautifulsoup4/) | `pip install bs4` |          
| [customtkinter](https://pypi.org/project/customtkinter/) | `pip install customtkinter` |  
| [pillow](https://pypi.org/project/pillow/) | `pip install Pillow` |                      


# Credits
| __IP & Geo Data:__ | [BrowserLeaks](https://browserleaks.com) | [IP2Location](https://ip2location.com) | [ipify](https://ipify.org) |
| ------------- | ------------- | ------------- | ------------- |

| __Flag PNGs:__ | [FlagsAPI](https://flagsapi.com/) |
| ------------- | ------------- |

| __Fonts:__ | [Manrope](https://fonts.google.com/specimen/Manrope) | [JetBrains Mono](https://www.jetbrains.com/lp/mono/) |
| ------------- | ------------- | ------------- |
