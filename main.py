import telebot
import utils

TOKEN = "7505424553:AAH-gnl9ZaxiISnOE2OukqAKePcWWy4GZL8"
bot = telebot.TeleBot(TOKEN)

point = 0 
spisoc = []
@bot.message_handler(commands=['start'])
def handle_start(message):
    kb = telebot.types.InlineKeyboardMarkup()
    utils.vkt_start(kb)
    bot.send_message(message.chat.id, 'викторина нажимне начать викторину', reply_markup=kb)
    

    

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    global point
    kb = telebot.types.InlineKeyboardMarkup()
    if call.data == 'vk':
        utils.vkt_start1(kb)
        bot.edit_message_text('1. Какой элемент является основным компонентом воды?', call.message.chat.id,
                        call.message.id, reply_markup=kb)
        
    if call.data == '1.1':
        point -=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start2(kb)
        bot.edit_message_text('2. Какой планетой является третьей от Солнца в нашей солнечной системе?', call.message.chat.id,
                        call.message.id, reply_markup=kb)
    if call.data == '1.2':
        point +=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start2(kb)
        bot.edit_message_text('2. Какой планетой является третьей от Солнца в нашей солнечной системе?', call.message.chat.id,
                        call.message.id, reply_markup=kb)

    if call.data == '1.3':
        point -=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start2(kb)
        bot.edit_message_text('2. Какой планетой является третьей от Солнца в нашей солнечной системе?', call.message.chat.id,
                        call.message.id, reply_markup=kb)   
        
    if call.data == '2.1':
        point -=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start3(kb)
        bot.edit_message_text('3. Кто написал "Гарри Поттера"', call.message.chat.id,
                        call.message.id, reply_markup=kb)
    if call.data == '2.2':
        point -=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start3(kb)
        bot.edit_message_text('3. Кто написал "Гарри Поттера"?', call.message.chat.id,
                        call.message.id, reply_markup=kb)

    if call.data == '2.3':
        point +=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start3(kb)
        bot.edit_message_text('3. Кто написал "Гарри Поттера"', call.message.chat.id,
                        call.message.id, reply_markup=kb)  
    
    if call.data == '3.1':
        point +=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start4(kb)
        bot.edit_message_text('4. Какой язык является официальным в Бразилии?', call.message.chat.id,
                        call.message.id, reply_markup=kb)
    if call.data == '3.2':
        point -=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start4(kb)
        bot.edit_message_text('4. Какой язык является официальным в Бразилии?', call.message.chat.id,
                        call.message.id, reply_markup=kb)

    if call.data == '3.3':
        point -=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start4(kb)
        bot.edit_message_text('4. Какой язык является официальным в Бразилии?', call.message.chat.id,
                        call.message.id, reply_markup=kb)  

    if call.data == '4.1':
        point -=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start5(kb)
        bot.edit_message_text('5. Какой континент является самым большим по площади?', call.message.chat.id,
                        call.message.id, reply_markup=kb)
    if call.data == '4.2':
        point -=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start5(kb)
        bot.edit_message_text('5. Какой континент является самым большим по площади?', call.message.chat.id,
                        call.message.id, reply_markup=kb)

    if call.data == '4.3':

        point +=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start5(kb)
        bot.edit_message_text('5. Какой континент является самым большим по площади?', call.message.chat.id,
                        call.message.id, reply_markup=kb) 
        
    if call.data == '5.1':

        point -=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start6(kb)
        bot.edit_message_text('6. Какой газ составляет большую часть атмосферы Земли?', call.message.chat.id,
                        call.message.id, reply_markup=kb) 
    if call.data == '5.2':

        point +=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start6(kb)
        bot.edit_message_text('6. Какой газ составляет большую часть атмосферы Земли?', call.message.chat.id,
                        call.message.id, reply_markup=kb) 
    if call.data == '5.3':

        point -=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start6(kb)
        bot.edit_message_text('6. Какой газ составляет большую часть атмосферы Земли?', call.message.chat.id,
                        call.message.id, reply_markup=kb) 

    if call.data == '6.1':

        point -=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start7(kb)
        bot.edit_message_text('7. Кто был первым человеком на Луне?', call.message.chat.id,
                        call.message.id, reply_markup=kb) 


    if call.data == '6.2':

        point +=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start7(kb)
        bot.edit_message_text('7. Кто был первым человеком на Луне?', call.message.chat.id,
                        call.message.id, reply_markup=kb) 

    if call.data == '6.3':

        point -=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start7(kb)
        bot.edit_message_text('7. Кто был первым человеком на Луне?', call.message.chat.id,
                        call.message.id, reply_markup=kb) 

    if call.data == '7.1':

        point -=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start8(kb)
        bot.edit_message_text('8. Какой фильм получил Оскар за лучший фильм в 1994 году?', call.message.chat.id,
                        call.message.id, reply_markup=kb) 
        
    if call.data == '7.2':

        point +=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start8(kb)
        bot.edit_message_text('8. Какой фильм получил Оскар за лучший фильм в 1994 году?', call.message.chat.id,
                        call.message.id, reply_markup=kb) 
        
    if call.data == '7.3':

        point -=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start8(kb)
        bot.edit_message_text('8. Какой фильм получил Оскар за лучший фильм в 1994 году?', call.message.chat.id,
                        call.message.id, reply_markup=kb) 

    if call.data == '8.1':

        point -=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start9(kb)
        bot.edit_message_text('9. Какой элемент имеет химический символ "Fe"?', call.message.chat.id,
                        call.message.id, reply_markup=kb)
        
    if call.data == '8.2':

        point +=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start9(kb)
        bot.edit_message_text('9. Какой элемент имеет химический символ "Fe"?', call.message.chat.id,
                        call.message.id, reply_markup=kb)
    
    if call.data == '8.3':

        point -=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start9(kb)
        bot.edit_message_text('9. Какой элемент имеет химический символ "Fe"?', call.message.chat.id,
                        call.message.id, reply_markup=kb)
        
    if call.data == '9.1':

        point +=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start10(kb)
        bot.edit_message_text('10. Какой океан является самым большим на планете?', call.message.chat.id,
                        call.message.id, reply_markup=kb)
        
    if call.data == '9.2':

        point -=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start10(kb)
        bot.edit_message_text('10. Какой океан является самым большим на планете?', call.message.chat.id,
                        call.message.id, reply_markup=kb)
        
    if call.data == '9.3':

        point -=1
        kb = telebot.types.InlineKeyboardMarkup()
        utils.vkt_start10(kb)
        bot.edit_message_text('10. Какой океан является самым большим на планете?', call.message.chat.id,
                        call.message.id, reply_markup=kb)
        
    if call.data == '10.1':
        point -=1
        utils.vkt_start11(kb)
        bot.edit_message_text(f'Ваши балы {point}/10', call.message.chat.id,
                        call.message.id, reply_markup=kb)
    
    if call.data == '10.2':
        point -=1
        utils.vkt_start11(kb)
        bot.edit_message_text(f'Ваши балы {point}/10', call.message.chat.id,
                        call.message.id, reply_markup=kb)
        
    if call.data == '10.3':
        point +=1
        utils.vkt_start11(kb)
        bot.edit_message_text(f'Ваши балы {point}/10', call.message.chat.id,
                        call.message.id, reply_markup=kb)

    
    



        

bot.polling(non_stop=True, interval=1)