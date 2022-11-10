from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *



updater = Updater('5612294742:AAGJqESZ2PLT-4_AWA_hyDzUhZas8wCwFvU')

updater.dispatcher.add_handler(CommandHandler('hi', hi_command))
updater.dispatcher.add_handler(CommandHandler('time', time_command))
updater.dispatcher.add_handler(CommandHandler('help', help_command))
updater.dispatcher.add_handler(CommandHandler('sum', sum_command))



print('server start')
updater.start_polling()
updater.idle()



'''
# app = ApplicationBuilder().token("YOUR TOKEN HERE").build()

# app.add_handler(CommandHandler("hello", hello))

# app.run_polling()
'''
















# import matplotlib.pyplot as plt
# import numpy as np

# # Fixing random state for reproducibility
# np.random.seed(19680801)


# plt.rcdefaults()
# fig, ax = plt.subplots()

# # Example data
# people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
# y_pos = np.arange(len(people))
# performance = 3 + 10 * np.random.rand(len(people))
# error = np.random.rand(len(people))

# ax.barh(y_pos, performance, xerr=error, align='center')
# ax.set_yticks(y_pos, labels=people)
# ax.invert_yaxis()  # labels read top-to-bottom
# ax.set_xlabel('Performance')
# ax.set_title('How fast do you want to go today?')

# plt.show()



# list = [1,2,3,2,7]
# plt.plot(list)

# plt.show()










# import emoji

# print(emoji.emojize('Python is :thumbs_up:'))










# from progress.bar import Bar, ChargingBar, FillingSquaresBar, FillingCirclesBar, IncrementalBar, PixelBar
# import time

# bar = PixelBar('Processing', max=20)
# for i in range(20):
#     time.sleep(0.1)
#     bar.next()
# bar.finish()











# from isOdd import isOdd

# print(isOdd(1))
# print(isOdd(4))