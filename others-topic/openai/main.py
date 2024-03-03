import openai
import streamlit as st

openai.api_key = "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"

def generate_ai_response(user_input):
    messages = [
        {"role": "system", "content": "you are a kind helpful assistant."}
    ]
    message = f"{user_input}"

    if message:
        messages.append(
            {"role": "user", "content": message},
        )

        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        return reply

#streamlit app
def main():
    st.title("AI Assistant")
    user_input = st.text_input("Ask a Question: ")
    if st.button("Genrate Response"):
        if user_input:
            result = generate_ai_response(user_input)
            st.write(result)

if __name__ == "__main__":
    main()