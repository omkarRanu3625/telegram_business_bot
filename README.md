# Business Insights Telegram Bot

A Telegram bot designed to help businesses analyze their data, predict future trends, and get answers to common digital marketing questions. The bot provides three core functionalities:

1. **Analyzing Business Data to Generate Relevant Keywords**
2. **Prediction of Future Trends Based on Industry Analysis**
3. **Advanced AI FAQ for Digital Marketers**

## Features

### 1. Analyzing Business Data to Generate Relevant Keywords
- Collect user inputs such as industry, business objectives, website URLs, social media platforms, and target audience.
- Based on the input, generate relevant and trending keywords for the user's business.

### 2. Prediction of Future Trends Based on Industry Analysis
- Fetch industry benchmark data (e.g., CPC, CTC) from trusted sources like the [PPC Industry Benchmarks](https://databox.com/ppc-industry-benchmarks).
- Display relevant trends and insights to help the user adjust their marketing strategies.

### 3. Advanced AI FAQ for Digital Marketers
- Provide an intelligent FAQ system that answers common questions related to digital marketing using AI-driven insights.

## Requirements

- Python 3.8+
- `virtualenv` (for creating a virtual environment)
- Telegram Bot API token
- Dependencies listed in `requirements.txt`

## Project Structure

telegram_business_bot/ 
├── main.py                  # Main bot logic 
├── requirements.txt         # Python dependencies 
├── industry_analysis.py     # Business Data Analysis logic 
├── ppc_trends_fetcher.py    # PPC trends data scraper and analyzer 
├── ai_faq_system.py         # AI-based FAQ system for digital marketers 
├── envBot/                  # Virtual environment folder 
└── data/                    # Pre-defined keyword dataset, benchmark data


## Installation

### Step 1: Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/omkarRanu3625/telegram_business_bot.git
cd telegram-business-bot

```

Create and activate a virtual environment:

```bash

python -m virtualvenv envBot
source envBot/bin/activate  # On Windows use 'envBot\Scripts\activate'

```


### Step 3: Install Dependencies
Install the required dependencies from requirements.txt:

```bash

pip install -r requirements.txt

```


### Step 4: Set Up Telegram Bot

-Go to BotFather on Telegram and create a new bot.
-Copy the bot token provided by BotFather.
-Replace YOUR_TELEGRAM_BOT_TOKEN in main.py with your bot's token.


### Step 5: Run the Bot
Once the environment is set up, you can run the bot:

```bash
  python main.py  

```  
---
 
## How the Bot Works

|- **1. Start the Conversation:** When a user starts the conversation with the bot, they will be prompted to provide details about their business, such as industry, business objectives, website, social media, etc.
- **2. Keyword Generation:** Based on the provided inputs, the bot will generate industry-specific keywords relevant to the user's business.

- **3. PPC Trends:** The user can request information about the latest industry trends, including cost-per-click (CPC) benchmarks, by typing /ppc_trends.

- **4. AI FAQ:** The bot also has an AI-powered FAQ system where users can ask digital marketing-related questions, and the bot will provide answers based on best practices and AI insights.

---

## Example Usage
 1. Start the Bot: /start
 2. Answer Questions: The bot will ask questions related to the user's business (e.g., industry, business objective, etc.).

 3. Get Keywords: After providing all the necessary inputs, the bot will generate relevant keywords.
 4. Request Trends: Type /ppc_trends to get the latest industry trends.
 5. Ask Questions: Ask any digital marketing-related questions, and the bot will provide answers.
Contributing
 6. Feel free to fork this repository, submit pull requests, or report issues. Contributions are welcome!

---
