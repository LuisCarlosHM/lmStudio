import lmstudio as lms

def read_context(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        file_content = f.read()
    return file_content

    return file_content
# Import the lmstudio library and alias it as lms
# Enable asynchronous LLM for better performance
# Model 1 - Chat completion

# Initialize the model with the "llama-3.2-1b-instruct" configuration
# Optimized for multilingual dialogue use cases, including agentic retrieval and summarization tasks.

# Basic chat completion

def basic_chat_response(input_text):
    model = lms.llm("llama-3.2-1b-instruct")
    return model.respond(input_text)


# Chat completion with context
def chat_with_context(input_text, context):
    # Chat completion with context
    model = lms.llm("llama-3.2-1b-instruct")
    chat = lms.Chat(context)
    print(input_text)
    # Add context to the chat
    chat.add_user_message(input_text)
    result = model.respond(chat)
    return result


# Model 2 - LLM

# Initialize the model with the "qwen2-vl-2b-instruct" configuration
# Vision model capable of understanding images of various resolutions and ratios.


# Describe image 

def describe_image(image_path):
    model = lms.llm("qwen2-vl-2b-instruct")
    image_handle = lms.prepare_image(image_path)
    chat = lms.Chat()
    chat.add_user_message("Describe esta imagen por favor", images=[image_handle])
    prediction = model.respond(chat)
    return prediction


# Model 3 - Text Completion

#  Initialize the model with the "qwen2.5-7b-instruct" configuration
#  Significantly improved performance in handling long-context tasks 
#  while maintaining its capability in short tasks.

# Complete text 
def complete_text(input_text): 
    model = lms.llm("qwen2.5-7b-instruct-1m")
    return model.complete(input_text, config={"maxTokens": 300})

def main():
    # Model 1
    # Basic chat completion
    # print(basic_chat_response("Cuál es el propósito de la vida?"))

    # Chat completion with context
    context = read_context("context.txt")
    # print(chat_with_context("¿De qué trata el laboratorio de inventores?", context))
    print()
    print(chat_with_context("¿Qué se hace en el laboratorio?\n", context))
    print('-' * 50)
    print(chat_with_context("¿Qué es el laboratorio de inventores?\n", context))
    print('-' * 50)
    print(chat_with_context("¿Cuál es el horario de atención?\n", context))
    print('-' * 50)
    print(chat_with_context("¿Puedo hacer mi servicio social en el laboratorio?\n", context))
    print('-' * 50)
    print(chat_with_context("Cómo imprimo algo?\n", context))
    print('-' * 50)
    print(chat_with_context("Dónde está el lab?\n", context))
    print('-' * 50)
    print(chat_with_context("Servicios que ofrece el laboratorio\n", context))
    print()
    # Model 2
    # Describe image
    # print(describe_image("./lizard.jpg"))

    # Model 3
    # Complete text
    # print(complete_text("Mi nombre es"))




if __name__ == "__main__":
    main()