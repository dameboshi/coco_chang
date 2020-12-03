import discord
import re
import dice
import aikatsu

DICE_PATTERN = r'^(?P<value>\d+)d(?P<side>\d+)'
AIKATSU_CMD_PATTERN = r'^!aikatsu *(?P<series>\w*)'
IMAGE_PATH = "./img/"
AIKATSU_FIRST = 178
AIKATSU_STARS = 100
AIKATSU_FRIENDS = 76
AIKATSU_ONPARADE = 28

class MyClient(discord.Client):
    """
    ココちゃんbot(discord用)のcliantクラス
    """
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('!hello'):
            await message.channel.send('COCO dayo')

        if re.search(DICE_PATTERN,message.content) != None:
            # dice_list = message.content.split('d')
            m = re.search(DICE_PATTERN,message.content)
            try:
                diceroll_sum = dice.diceRoll(int(m.group('value')),int(m.group('side')))
                await message.channel.send(str(diceroll_sum))
            except Exception as e:
                print('error:',e)

        if message.content.startswith('!aikatsu'):
            m = re.search(AIKATSU_CMD_PATTERN, message.content)
            if m.group('series') == 'first':
                # 1~178
                diceroll_sum = dice.diceRoll(1, AIKATSU_FIRST)
            elif m.group('series') == 'stars':
                # 179~279
                diceroll_sum = dice.diceRoll(1, AIKATSU_STARS) + AIKATSU_FIRST
            elif m.group('series') == 'friends':
                # 280~354
                diceroll_sum = dice.diceRoll(1, AIKATSU_FRIENDS) + AIKATSU_FIRST + AIKATSU_STARS
            elif m.group('series') == 'onparade':
                # 355~382
                diceroll_sum = dice.diceRoll(1, AIKATSU_ONPARADE) + AIKATSU_FIRST + AIKATSU_STARS + AIKATSU_FRIENDS
            else:
                # その他扱いで全話シャッフル
                diceroll_sum = dice.diceRoll(1, 382)

            display_dic = aikatsu.display_aikatsu(diceroll_sum)
            img = "aikatsu_" + str(format(diceroll_sum, '03d')) + ".jpg"
            # 表示
            await message.channel.send(display_dic["title"] + " 【" + display_dic["series"] + "】")
            with open( IMAGE_PATH + img, 'rb') as fp:
                    await message.channel.send(file=discord.File(fp,img))
            await message.channel.send("あらすじ : " + display_dic["story"])

            
