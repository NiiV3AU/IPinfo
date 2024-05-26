import requests
from bs4 import BeautifulSoup
import customtkinter as ctk
from customtkinter import CTkFont, CTkImage
from PIL import Image
import os
from threading import Thread
from time import sleep as sleep


BG_COLOR = "#333333"
DBG_COLOR = "#2b2b2b"
FG_COLOR = "#45e876"
BHVR_COLOR = "#36543F"

ctk.set_appearance_mode("dark")

root = ctk.CTk()
root.title("IPinfo")
root.minsize(300, 380)
root.configure(fg_color=DBG_COLOR)
width_of_window = 300
height_of_window = 380
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width / 2) - (width_of_window / 2)
y_coordinate = (screen_height / 2) - (height_of_window / 2)
root.geometry(
    "%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate)
)

# Fonts
BIG_FONT = CTkFont(family="Manrope", size=16, weight="bold")
SMALL_FONT = CTkFont(family="Manrope", size=12)
SMALL_BOLD_FONT = CTkFont(family="Manrope", size=13, weight="bold")
BOLD_FONT = CTkFont(family="Manrope", size=14, weight="bold")
TOOLTIP_FONT = CTkFont(family="Manrope", size=12, slant="italic")
CODE_FONT = CTkFont(family="JetBrains Mono", size=12)
CODE_FONT_BIG = CTkFont(family="JetBrains Mono", size=16)
CREDITS_FONT = CTkFont(family="JetBrains Mono", size=10)

# Credits
copyright_label = ctk.CTkLabel(
    master=root,
    font=CREDITS_FONT,
    text_color=BG_COLOR,
    text="↣ Click Here for Credits ↢\n⋉ © NV3 ⋊\n{ v1.0.1 }",
    bg_color="transparent",
    fg_color=DBG_COLOR,
    justify="center",
)
copyright_label.pack(pady=10, fill="both", expand=False, anchor="n", side="top")

api_label = ctk.CTkLabel(
    master=root,
    font=SMALL_BOLD_FONT,
    text_color="#DCE4EE",
    text="Choose API:",
    bg_color="transparent",
    fg_color=DBG_COLOR,
    height=10,
    justify="center",
)
api_label.pack(pady=5, fill="x", expand=False, anchor="n", side="top")


api_option_menu = ctk.CTkSegmentedButton(
    master=root,
    text_color=DBG_COLOR,
    values=["BrowserLeaks", "IP2Location", "ipify"],
    fg_color=BG_COLOR,
    selected_color=FG_COLOR,
    selected_hover_color=BHVR_COLOR,
    unselected_hover_color=BHVR_COLOR,
    unselected_color=BG_COLOR,
    font=SMALL_BOLD_FONT,
    corner_radius=10,
)
api_option_menu.pack(pady=5, padx=30, fill=None, expand=False, anchor="n", side="top")
api_option_menu.set("BrowserLeaks")
api_var = api_option_menu.get()


# open the project repo on github in a new tab in your default browser
def open_github(e):
    import webbrowser

    webbrowser.open_new_tab("https://github.com/NiiV3AU/IPinfo")


def get_ip(progress_callback):
    # scrape ip address (only IPv4 for the time being) from browserleaks.com
    if api_var == "BrowserLeaks":
        url = "https://browserleaks.com/ip"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        ip_address = soup.find("span", {"id": "client-ipv4"})["data-ip"]
        progress_callback(0.33)
        return ip_address

    # call IP2Location's api for IPv4
    elif api_var == "IP2Location":
        url = "https://api.ip2location.io/"
        response = requests.get(url)
        global data
        data = response.json()
        ip_address = data.get("ip")
        progress_callback(0.33)
        return ip_address

    # call ipify's api for IPv4
    elif api_var == "ipify":
        url = "https://api.ipify.org"
        response = requests.get(url).text
        ip_address = str(response)
        progress_callback(0.33)
        return ip_address
    else:
        progress_callback(0.33)
        return "Unexpected Error"


def get_geo(progress_callback):
    # scrape geolocation aka Country Code from browserleaks.com
    if api_var == "BrowserLeaks":
        url = "https://browserleaks.com/ip"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        geolocation = soup.find("span", {"id": "client-ipv4"})["data-iso_code"]
        progress_callback(0.66)
        return geolocation

    # call IP2Location's api for geolocation aka Country Code (also if ipify is selected because ipify has only ip api support without registration)
    elif api_var == "IP2Location" or "ipify":
        geolocation = data.get("country_code")
        progress_callback(0.66)
        return geolocation

    else:
        progress_callback(0.66)
        return "Unexpected Error"


# checks if flag_cache (folder for flags) exists
# if not then its automatically creates one
FLAG_CACHE_DIR = "flag_cache"
if not os.path.exists(FLAG_CACHE_DIR):
    os.makedirs(FLAG_CACHE_DIR)


flag_image = None


# get the flag.png with the help of the geolocation
def get_flag(country_code, progress_callback):
    filename = os.path.join(FLAG_CACHE_DIR, f"{country_code}_flag.png")
    if os.path.exists(filename):
        # If flag is already in cache (downloaded) then return the cached file rather download a copy
        progress_callback(1.0)
        return filename
    else:
        # Downloading flag.png to cache
        url = f"https://flagsapi.com/{country_code}/flat/64.png"
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            progress_callback(1.0)
            return filename
        else:
            return None


# Textanimation of the copyright_label
def copyright_label_ani_master():

    while True:
        copyright_label.configure(text_color="#4D4D4D")
        sleep(0.1)
        copyright_label.configure(text_color="#666666")
        sleep(0.1)
        copyright_label.configure(text_color="#808080")
        sleep(0.1)
        copyright_label.configure(text_color="#999999")
        sleep(0.1)
        copyright_label.configure(text_color="#B3B3B3")
        sleep(0.1)
        copyright_label.configure(text_color="#CCCCCC")
        sleep(0.2)
        copyright_label.configure(text_color="#E6E6E6")
        sleep(0.3)
        copyright_label.configure(text_color="#FFFFFF")
        sleep(0.4)
        copyright_label.configure(text_color="#E6E6E6")
        sleep(0.3)
        copyright_label.configure(text_color="#CCCCCC")
        sleep(0.2)
        copyright_label.configure(text_color="#B3B3B3")
        sleep(0.1)
        copyright_label.configure(text_color="#999999")
        sleep(0.1)
        copyright_label.configure(text_color="#808080")
        sleep(0.1)
        copyright_label.configure(text_color="#666666")
        sleep(0.1)


# Update labels
def update_gui():
    global flag_label

    def progress_callback(progress):
        progress_bar.set(progress)

    ip_address = get_ip(progress_callback)

    ip_label.configure(text="IP Address: " + ip_address)

    geolocation = get_geo(progress_callback)
    geo_label.configure(text="Geolocation: " + geolocation)

    flag_filename = get_flag(geolocation, progress_callback)
    if flag_filename:
        # destroy old flag_label
        flag_label.destroy()

        # create new flag_label with refreshed flag
        flag_image = ctk.CTkImage(
            dark_image=Image.open(flag_filename),
            light_image=Image.open(flag_filename),
            size=(32, 32),
        )
        flag_label = ctk.CTkLabel(
            master=data_frame,
            text="",
            image=flag_image,
            bg_color="transparent",
            fg_color="transparent",
            corner_radius=24,
            font=CODE_FONT,
        )
        flag_label.pack(expand=True)
    else:
        #
        flag_label.configure(text="Flag not found")
    bar_to_btn(progress_callback)


# replaces update_button with the progressbar
def btn_to_bar():
    ip_label.configure(text="IP Address: loading...")
    geo_label.configure(text="Geolocation: loading...")
    flag_label.configure(text="Country Flag: loading...", image=None)
    update_button.pack_forget()
    progress_bar.pack(expand=True, side="bottom", fill="x", anchor="s")
    start_update = Thread(target=update_gui)
    start_update.start()


# above step in reverse
def bar_to_btn(progress_callback):
    progress_bar.pack_forget()
    progress_callback(0)
    update_button.pack(expand=True, side="bottom", fill="x", anchor="s")


# GUI setup
master_frame = ctk.CTkFrame(master=root, fg_color=DBG_COLOR, corner_radius=0)
master_frame.pack(expand=True, fill="both")

data_frame = ctk.CTkFrame(
    master=master_frame, fg_color=BG_COLOR, corner_radius=24, bg_color="transparent"
)
data_frame.pack(expand=True, fill="both", pady=10, padx=10)

ip_label = ctk.CTkLabel(master=data_frame, text="IP Adress: N/A", font=CODE_FONT)
ip_label.pack(expand=True, pady=20, fill="x")

geo_label = ctk.CTkLabel(master=data_frame, text="Geolocation: N/A", font=CODE_FONT)
geo_label.pack(expand=True, fill="x", pady=10)

flag_label = ctk.CTkLabel(
    master=data_frame,
    text="Country Flag: N/A",
    image=None,
    bg_color="transparent",
    fg_color="transparent",
    corner_radius=24,
    font=CODE_FONT,
)
flag_label.pack(expand=True, fill="x", pady=20)


def hover_update_button(e):
    update_button.configure(text_color=FG_COLOR)
    update_button.configure(fg_color="#36543F")


def nohover_update_button(e):
    update_button.configure(text_color=BG_COLOR)
    update_button.configure(fg_color=FG_COLOR)


update_button = ctk.CTkButton(
    master=data_frame,
    text="Click to refresh     ⁕ * ⁕ ",
    font=SMALL_BOLD_FONT,
    command=btn_to_bar,
    fg_color=FG_COLOR,
    bg_color="transparent",
    hover_color=FG_COLOR,
    corner_radius=0,
    text_color=BG_COLOR,
    height=40,
)

update_button.pack(expand=True, side="bottom", fill="x", anchor="s")


# update_button animation
def update_button_ani():
    while True:
        update_button.configure(text="⁕ ⁕ ⁕     Click to refresh     ⁕ ⁕ ⁕")
        sleep(0.3)
        update_button.configure(text="⁕ ⁕ *     Click to refresh     * ⁕ ⁕")
        sleep(0.2)
        update_button.configure(text="⁕ * ⁕     Click to refresh     ⁕ * ⁕")
        sleep(0.3)
        update_button.configure(text="* ⁕ ⁕     Click to refresh     ⁕ ⁕ *")
        sleep(0.2)


# function to start all animations in two threads
def master_ani_start():
    Thread(target=update_button_ani).start()
    Thread(target=copyright_label_ani_master).start()


# starts the above function after 0.25 sec
root.after(250, master_ani_start)


progress_bar = ctk.CTkProgressBar(
    master=data_frame,
    corner_radius=0,
    bg_color=BG_COLOR,
    fg_color="#36543F",
    progress_color=FG_COLOR,
    height=40,
    border_color=DBG_COLOR,
)

update_button.bind("<Enter>", hover_update_button)
update_button.bind("<Leave>", nohover_update_button)
copyright_label.bind("<ButtonRelease>", open_github)


if __name__ == "__main__":
    root.mainloop()
