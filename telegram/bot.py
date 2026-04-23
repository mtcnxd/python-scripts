from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from configs import TOKEN
import requests
import json

def get_data():
    response = requests.get("https://mecanicarubio.com/api/investments/total")
    return response.json()

# /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    json_data = get_data()
    
    total = 0
    if json_data is not None:            
        message = "Hola Marcos, tus saldos son los siguientes 😀:\n\n"

        for item in json_data['items']:
            message += f"✅ En {item['name']} tienes {item['current_amount']}\n"

        message += f"\nEn total tienes {json_data['total']} 🫰😅"

        await update.message.reply_text(text=message)

# /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text()

# /status
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Todo funcionando correctamente ✅")

async def domain_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Por favor, proporciona un dominio")
        return

    domain = " ".join(context.args)
    
    url = f"http://epp-us-va2.catched.com:4125/infoDomain/{domain}"
    response = requests.get(url)
    formated = json.dumps(response.json(), indent=4)
    print(formated)
    
    await update.message.reply_text(f"<pre>{formated}</pre>", parse_mode="HTML")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("saludar", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("status", status))
    app.add_handler(CommandHandler("info", domain_info))

    print("Bot corriendo...")
    app.run_polling()

if __name__ == "__main__":
    main()