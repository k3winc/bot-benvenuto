from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, MessageHandler, filters

TOKEN = 'INSERISCI_IL_TUO_TOKEN_QUI'

WELCOME_MESSAGE = """
👋 Benvenutə nel gruppo!

Hai appena messo piede in uno spazio libero, sicuro e dedicato solo ai minorenni 🎉  
Qui puoi:
💬 Socializzare, sfogarti, ridere
🎮 Parlare dei tuoi interessi  
😄 Conoscere nuove persone come te!
📚 Chiedere un aiuto compiti.

📌 Regole base:
1. Rispetta tuttə  
2. Vietato spam o contenuti inappropriati
3. Qui si sta bene se ci si aiuta 🫶

Sentiti liberə di presentarti o buttarti subito in chat!
Hai bisogno di qualcosa? Tagga pure un admin 😉
"""

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    for new_user in update.message.new_chat_members:
        await update.message.reply_text(WELCOME_MESSAGE)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    handler = MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome)
    app.add_handler(handler)

    print("🤖 Bot attivo!")
    app.run_polling()
