import chainlit as cl
import openai
from dotenv import load_dotenv

load_dotenv()


@cl.on_message
async def main(message: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5",
        message=[
            {"role": "assistant", "content": "you are a helpful assistant"},
            {"role": "user", "content": message},
        ],
        temperature=1,
    )

    # Custom serialization function for cl.Message
    def message_serializer(obj):
        if isinstance(obj, cl.Message):
            return {"content": obj.content}
        raise TypeError(
            f"Object of type {obj.__class__.__name__} is not JSON serializable"
        )

    # Serialize using the custom function
    response_content = response["choices"][0]["message"]["content"]
    serialized_message = json.dumps(
        cl.Message(content=response_content), default=message_serializer
    )

    await cl.Message(content=serialized_message).send()
