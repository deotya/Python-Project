import telebot
import openai
import creds
openai.api_key = (creds.api_key)

# Initialize the Telegram bot
bot = telebot.TeleBot(creds.TOKEN)

# Define a function to generate response using ChatGPT API
def generate_response(text):
    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=(f"User: {text}\nAI: "),
      temperature=0.7,
      max_tokens=1000,
      n=1,
      stop=None,
      frequency_penalty=0,
      presence_penalty=0
    )
    return response.choices[0].text.strip()

# Define a function to handle the /start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Hi {message.from_user.first_name}, I'm your friendly ChatGPT bot. How can I help you today?")

# Define a function to handle user messages
@bot.message_handler(func=lambda message: True)
def echo(message):
    response = generate_response(message.text)
    bot.send_message(message.chat.id, response)

# Start the bot
bot.infinity_polling()
