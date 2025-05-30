from openai import OpenAI
from utils.logger import logger


class LLMClient:
    def __init__(self, llm):
        self.base_url = llm.get("base_url")
        self.api_key = llm.get("api_key")
        self.model = llm.get("model")
        self.max_tokens = llm.get("max_tokens")
        self.system_prompt = llm.get("system_prompt")
        self.client = self._initialize_client()

    def _initialize_client(self):
        try:
            client = OpenAI(
                base_url=self.base_url,
                api_key=self.api_key,
            )
            logger.info("OpenAI client initialized successfully.")
            return client
        except Exception as e:
            logger.error(f"Failed to initialize OpenAI client: {e}")
            raise

    def chat_completion(self, content):
        try:
            messages = [
                {"role": "system", "content": self.system_prompt},
                {"role": "user", "content": content}
            ]
            logger.info(f"Sending chat completion request to model {self.model}...")
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                max_tokens=self.max_tokens,
                # enable_thinking=False,
                extra_body={"enable_thinking": False}
            )
            logger.info("Chat completion request successful.")
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Error during chat completion: {e}")
            raise
