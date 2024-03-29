from mcpi.minecraft import Minecraft
import time
import messageHandler

mc = Minecraft.create("51.83.46.159", 4711)
print("Connection success")

messageHandler = messageHandler.MessageHandler()


class Connection:
    def edited_on_message(self, message):
        player_ID = message.entityId
        message = message.message
        if message.lower() == "sven stop":
            mc.setBlock(-1, -68, 0, 30)  # off
            mc.setBlock(-1, -68, 0, 0)
            connection.start()
            return

        if 'Sven' in message:
            response = "SVEN: " + messageHandler.generate_response(message, player_ID)
            mc.postToChat(response)

    def start(self):
        '''function to control on/off of chatbot (controlls hotbar ingame)'''
        start_up = False
        while start_up == False:
            for posts in mc.events.pollChatPosts():
                if posts.message.lower() == "sven start":
                    start_up = True
                    mc.setBlock(-3, -68, 0, 30)  # on
                    mc.setBlock(-3, -68, 0, 0)

connection = Connection()
connection.start()
while True:
    for posts in mc.events.pollChatPosts():
        connection.edited_on_message(posts)
    time.sleep(1)
