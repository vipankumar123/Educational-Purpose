import streamlit as st
from googletrans import LANGUAGES, Translator


def main():
    st.title("Language Translator")
    st.write("tranlate text from one language to another")

    text_input = st.text_area("Enter text to translate:", "")

    languages = get_languages()

    target_lang = st.selectbox("select target language:", languages)

    if st.button("Tranlate"):
        if text_input:
            translate = tranlste_text(text_input, target_lang)
            st.subheader("Translation result: ")
            st.write(translate)
    else:
        st.warning("Please enter text to tranlste?")



def get_languages():
    language = [LANGUAGES[lang] for lang in LANGUAGES]
    return language

def tranlste_text(text, target_lang):
    translator = Translator()
    translation = translator.translate(text, dest=target_lang)
    return translation.text


if __name__ == "__main__":
    main()