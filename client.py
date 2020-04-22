import discord
import re
import dice
import aikatsu

DICE_PATTERN = r'^(?P<value>\d+)d(?P<side>\d+)'
IMAGE_PATH = "./img/"

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
            if m.group('side') != '0':
                # 0面ダイスじゃなかったら処理する
                diceroll_sum = dice.diceRoll(int(m.group('value')),int(m.group('side')))
                await message.channel.send(str(diceroll_sum))

        if message.content.startswith('!aikatsu'):
            diceroll_sum = dice.diceRoll(1, 354)
            display_dic = aikatsu.display_aikatsu(diceroll_sum)
            img = "aikatsu_" + str(format(diceroll_sum, '03d')) + ".jpg"
            
            # 表示
            await message.channel.send(display_dic["title"] + " 【" + display_dic["series"] + "】")
            with open( IMAGE_PATH + img, 'rb') as fp:
                    await message.channel.send(file=discord.File(fp,img))
            await message.channel.send("あらすじ : " + display_dic["story"])

            
