from cog import BasePredictor, Input

class Predictor(BasePredictor):

    def predict(
        self,
        prompt: str = Input(description="Message to the chatbot")
    ) -> str:

        return f"You said: {prompt}"
