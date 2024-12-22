 # Main bot logic

import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ConversationHandler
from industry_analysis import analyze_business_data
#from ppc_trends_fetcher import fetch_trends
from ai_faq_system import get_faq_response

logging.basicConfig(level=logging.INFO)

# States for the conversation
INDUSTRY, OBJECTIVE, WEBSITE, SOCIAL_MEDIA, PPC, TARGET_AUDIENCE, LOCATION = range(7)

async def start(update: Update, context):
    await update.message.reply_text(
        "Welcome to the Business Insights Bot! Let's start by analyzing your business data.\n"
        "What industry is your business in?"
    )
    return INDUSTRY

async def industry_input(update: Update, context):
    context.user_data['industry'] = update.message.text
    await update.message.reply_text("What is your business objective?")
    return OBJECTIVE

async def objective_input(update: Update, context):
    context.user_data['objective'] = update.message.text
    await update.message.reply_text("Do you have a website? (yes/no)")
    return WEBSITE

async def website_input(update: Update, context):
    if update.message.text.lower() == 'yes':
        await update.message.reply_text("Please provide the URL:")
        return WEBSITE
    else:
        context.user_data['website'] = None
        await update.message.reply_text("Do you have any social media platforms? (yes/no)")
        return SOCIAL_MEDIA

async def social_media_input(update: Update, context):
    context.user_data['social_media'] = update.message.text
    await update.message.reply_text("Do you use PPC campaigns? (yes/no)")
    return PPC

async def ppc_input(update: Update, context):
    context.user_data['ppc'] = update.message.text.lower() == 'yes'
    await update.message.reply_text("Who are you trying to reach?")
    return TARGET_AUDIENCE

async def target_audience_input(update: Update, context):
    context.user_data['target_audience'] = update.message.text
    await update.message.reply_text("What location would you like to target?")
    return LOCATION

async def location_input(update: Update, context):
    context.user_data['location'] = update.message.text
    await update.message.reply_text("Analyzing your data, please wait...")

    # Call the business analysis function
    keywords = analyze_business_data(context.user_data)

    await update.message.reply_text(f"Here are the trending keywords for your business:\n{keywords}")
    return ConversationHandler.END

#async def ppc_trends(update: Update, context):
 #   trends = fetch_trends(context.user_data.get('industry'))
  #  await update.message.reply_text(f"Here are the PPC trends for your industry:\n{trends}")

async def faq(update: Update, context):
    question = update.message.text
    answer = get_faq_response(question)
    await update.message.reply_text(f"Answer: {answer}")

async def cancel(update: Update, context):
    await update.message.reply_text("Goodbye!")
    return ConversationHandler.END

if __name__ == '__main__':
    application = ApplicationBuilder().token("Your_BOT_Token").build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            INDUSTRY: [MessageHandler(filters.TEXT & ~filters.COMMAND, industry_input)],
            OBJECTIVE: [MessageHandler(filters.TEXT & ~filters.COMMAND, objective_input)],
            WEBSITE: [MessageHandler(filters.TEXT & ~filters.COMMAND, website_input)],
            SOCIAL_MEDIA: [MessageHandler(filters.TEXT & ~filters.COMMAND, social_media_input)],
            PPC: [MessageHandler(filters.TEXT & ~filters.COMMAND, ppc_input)],
            TARGET_AUDIENCE: [MessageHandler(filters.TEXT & ~filters.COMMAND, target_audience_input)],
            LOCATION: [MessageHandler(filters.TEXT & ~filters.COMMAND, location_input)]
        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )

    application.add_handler(conv_handler)
    # application.add_handler(CommandHandler('ppc_trends', ppc_trends))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, faq))

    application.run_polling()
