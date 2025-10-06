import ollama

class ChattyBot:
    def __init__(self):
        self.messages = []
        system_prompt = "You are a user friendly assistant and friend chatbot to the user . Be polite and give answers to users of whatever they ask. You can use emojis , be decent and friendly , also try to adapt to the talking style of the user."
        self.messages.append({'role': 'system', 'content': system_prompt})

    def get_response(self, user_input: str) -> str:
        # exit phrases handled outside
        self.messages.append({'role': 'user', 'content': user_input})

        # send conversation history to Ollama
        response = ollama.chat(model='gemma:2b', messages=self.messages)
        assistant_response = response['message']['content']

        # add assistant reply to history
        self.messages.append({'role': 'assistant', 'content': assistant_response})
        return assistant_response
