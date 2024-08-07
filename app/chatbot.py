from flask import Blueprint, request, jsonify
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot_bp = Blueprint('chatbot', __name__)

bot = ChatBot('DriverSchoolBot')
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")

@chatbot_bp.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data['message']
    bot_response = bot.get_response(user_message)
    return jsonify(response=str(bot_response))
