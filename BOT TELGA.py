import telebot
import requests
import datetime

TOKEN = '6478731412:AAH-sG3FiS0eoHeKzEc0lgBFOIEOuAgFqoA'

# List of cemetery IDs
admins = ['5238334757', '2015673019', 'ADMIN_ID_3']

active_users = []

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! If you want to get player information, send the IDs in the format --Cemetery ID++Player ID. To add a user to the bot, send @@ID. To remove a user from the bot, send #ID.")
    activate_user(message)

def activate_user(message):
    user_id = str(message.from_user.id)
    if user_id not in active_users:
        active_users.append(user_id)

@bot.message_handler(func=lambda message: True)
def handle_id_commands(message):
    if str(message.from_user.id) in active_users:
        if str(message.from_user.id) in admins:
            if message.text.startswith('@@'):
                id_to_add = message.text.strip('@@')
                if id_to_add not in active_users:
                    active_users.append(id_to_add)
                    bot.reply_to(message, f"ID {id_to_add} successfully added.")
                else:
                    bot.reply_to(message, f"ID {id_to_add} is already in the active users list.")
            elif message.text.startswith('#'):
                id_to_remove = message.text.strip('#')
                if id_to_remove in active_users:
                    active_users.remove(id_to_remove)
                    bot.reply_to(message, f"ID {id_to_remove} successfully removed.")
                else:
                    bot.reply_to(message, f"ID {id_to_remove} is not in the active users list.")
            elif 'list' in message.text:
                active_user_list = "\n".join(active_users)
                bot.reply_to(message, f"Active users list:\n{active_user_list}")
            else:
                get_player_info(message)
        else:
            bot.reply_to(message, "You Need To Buy Autorisation To Activate Bot Contact @Vx_Vortex.")
    else:
        bot.reply_to(message, "Bot Developer: VorTex, send '/start' quickly, I'm running out of time.")

def get_player_info(message):
    if str(message.from_user.id) in active_users:
        if str(message.from_user.id) in admins:
            if '--' in message.text:
                player_id = message.text.split('--')[1]
                id = player_id
                regtion = "me"

                url = 'https://freefireapi.com.br/api/search_id?id={}&region={}'.format(player_id, regtion)
                response = requests.get(url)
                if response.status_code == 200:
                    long_text = response.text
                else:
                    pass

                # Parsing the response data to extract player information
                ap = '"nickname":'
                dp = '","'
                start_link2 = long_text.find(ap) + len(ap) + 1
                end_link2 = long_text.find(dp, start_link2)
                name = long_text[start_link2:end_link2]

                ap1 = 'level"'
                dp1 = ',"exp'
                start_link3 = long_text.find(ap1) + len(ap1) + 1
                end_link3 = long_text.find(dp1, start_link3)
                level = long_text[start_link3:end_link3]
                #print(level)
                # exp
                ap4 = ',"exp"'
                dp4 = ',"'
                start_link42 = long_text.find(ap4) + len(ap4) + 1
                end_link4 = long_text.find(dp4, start_link42)
                exp = long_text[start_link42:end_link4]
                #print(exp)
                # liked
                ap5 = ',"liked"'
                dp4 = ',"showRank'
                start_link5 = long_text.find(ap5) + len(ap5) + 1
                end_link5 = long_text.find(dp4, start_link5)
                liked = long_text[start_link5:end_link5]
                #print(liked)
                # last login
                ap6 = 'lastLoginAt":'
                dp6 = '","csRa'
                start_link6 = long_text.find(ap6) + len(ap6) + 1
                end_link6 = long_text.find(dp6, start_link6)
                lastlogin_beta = long_text[start_link6:end_link6]
                timestamp = int(lastlogin_beta)
                date_time = datetime.datetime.utcfromtimestamp(timestamp)
                lastlogin = date_time
                #print(lastlogin)
                # create accunt
                ap7 = 'createAt":'
                dp7 = '"},"'
                start_link7 = long_text.find(ap7) + len(ap7) + 1
                end_link7 = long_text.find(dp7, start_link7)
                creatlogi_beta = long_text[start_link7:end_link7]
                timestamp = int(creatlogi_beta)
                date_time2 = datetime.datetime.utcfromtimestamp(timestamp)
                creatlogin = date_time2
                #print(creatlogin)
                # rank token
                ap14 = 'rankingPoints"'
                dp14 = ',"badgeCnt'
                start_link14 = long_text.find(ap14) + len(ap14) + 1
                end_link14 = long_text.find(dp14, start_link14)
                rank_token = long_text[start_link14:end_link14]
                #print(rank_token)
                # rank number
                ap15 = '"rank"'
                dp15 = ',"rankingPoints'
                start_link15 = long_text.find(ap15) + len(ap15) + 1
                end_link15 = long_text.find(dp15, start_link15)
                rank_number = long_text[start_link15:end_link15]
                #print(rank_number)
                # langue
                ap8 = '"language":'
                dp8 = '"'
                start_link8 = long_text.find(ap8) + len(ap8) + 1
                end_link8 = long_text.find(dp8, start_link8)
                langue = long_text[start_link8:end_link8]
                #print(langue)
                # bio
                ap9 = '"signature":'
                dp9 = '","rankShow'
                if "signature" in long_text:
                    
                    start_link9 = long_text.find(ap9) + len(ap9) + 1
                    end_link9 = long_text.find(dp9, start_link9)
                    bio = long_text[start_link9:end_link9]
                else:
                    bio = "No bio"
                #print(bio)
                # clan id
                ap10 = '"clanId":'
                dp10 = '","capt'
                start_link10 = long_text.find(ap10) + len(ap10) + 1
                end_link10 = long_text.find(dp10, start_link10)
                guild_id = long_text[start_link10:end_link10]
                #print(guild_id)
                # admin clan id
                ap11 = '"captainBasicInfo":{"accountId":'
                dp11 = '","nickname":'
                start_link12 = long_text.find(ap11) + len(ap11) + 1
                end_link12 = long_text.find(dp11, start_link12)
                admin_id = long_text[start_link12:end_link12]
                #print(admin_id)
                # admin clan name
                ap12 = '{}","nickname":'.format(admin_id)
                dp12 = '","leve'
                start_link11 = long_text.find(ap12) + len(ap12) + 1
                end_link11 = long_text.find(dp12, start_link11)
                admin_name = long_text[start_link11:end_link11]
                #print(admin_name)
                # clan level
                ap13 = 'clanLevel"'
                dp13 = ',"capacity'
                start_link13 = long_text.find(ap13) + len(ap13) + 1
                end_link13 = long_text.find(dp13, start_link13)
                clan_level = long_text[start_link13:end_link13]
                #print(clan_level)
                # clan cpacty
                ap17 = 'capacity"'
                dp17 = ',"member'
                start_link17 = long_text.find(ap17) + len(ap17) + 1
                end_link17 = long_text.find(dp17, start_link17)
                clan_capacity = long_text[start_link17:end_link17]
                #print(clan_capacity)
                # clan maxcapacity
                ap16 = 'memberNum"'
                dp16 = '},"cap'
                start_link16 = long_text.find(ap16) + len(ap16) + 1
                end_link16 = long_text.find(dp16, start_link16)
                clan_maxcapacity = long_text[start_link16:end_link16]
                

                bot.reply_to(message, f" Player Name : {name} \nLevel : {level}\n Uid : {id}\n Exp : {exp}\n Likes : {liked}\n Last Time Logged : {lastlogin}\n Created Account In : {creatlogin}\n Rank : {rank_token}\n Rank Number : {rank_number}\n Langue : {langue}\n Bio : {bio}\n Guild Id : error  \n Guild Leader Name : \n Guild Level : {clan_level}\n Guild Members: {clan_capacity}\n  Guild Join Max Number : {clan_maxcapacity}  ")
            else:
                bot.reply_to(message, "Invalid command format. Please Py --Id To Search Info")
        else:
            bot.reply_to(message, "You Need To Buy Autorisation Bot Contact @Vx_Vortex.")
    else:
        bot.reply_to(message, "Bot Developer: VorTex send '/start' quickly, I'm running out of time.")

bot.polling()