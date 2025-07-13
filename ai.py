import g4f


# Используем доступные модели
class AI:

    def __init__(self, prompt):
        self.available_models = [
            "gpt-4",
            "gpt-3.5-turbo-16k",
            "llama2-70b",
            "claude-2"
        ]
        self.prompt = prompt
    def get_prompt(self, prompt):
        self.prompt = prompt
    def give_answer(self):
        try:

            response = g4f.ChatCompletion.create(
                model="gpt-4",  # Используем доступную модель
                messages=[{"role": "user", "content": self.prompt}],
                stream=False,
                )


            for message in response:
                print(message, flush=True, end='')
            if isinstance(response, str):
                return response
            elif hasattr(response, '__iter__'):
                return " ".join(str(item) for item in response)
            else:
                return str(response["content"])
        except Exception as e:
            return f"Ошибка: {str(e)}"








