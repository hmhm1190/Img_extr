# streamlit_app.py
import streamlit as st
from decoder import load_bart_model, load_bart_tokenizer, get_bart_response
from image_processor import read_image, process_donut_image

# Initialize our Streamlit app
st.set_page_config(page_title="Open-source Image Demo")

st.header("Open-source Image Application")
input_prompt = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose a donut image...", type=["jpg", "jpeg", "png"])
image = ""

# Load BART model and tokenizer
bart_model = load_bart_model()
bart_tokenizer = load_bart_tokenizer()

if uploaded_file is not None:
    image = read_image(uploaded_file)
    st.image(image, caption="Uploaded Donut Image.", use_column_width=True)

submit = st.button("Tell me about the donut")

# Store previous questions and answers
previous_responses = []

# If ask button is clicked
if submit:
    donut_image = process_donut_image(image)
    response = get_bart_response(bart_model, bart_tokenizer, input_prompt, input_prompt)
    st.subheader("The Response is")
    st.write(response)
    
    # Store the question and response
    previous_responses.append({"question": input_prompt, "answer": response})

# Display previous questions and answers
st.subheader("Previous Questions and Answers:")
for i, entry in enumerate(previous_responses, start=1):
    st.markdown(f"**Q{i}:** {entry['question']}")
    st.markdown(f"**A{i}:** {entry['answer']}")
    st.markdown("---")
