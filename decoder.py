# bart_model.py
from transformers import BartForConditionalGeneration, BartTokenizer

def load_bart_model():
    return BartForConditionalGeneration.from_pretrained("facebook/bart-large-cnn")

def load_bart_tokenizer():
    return BartTokenizer.from_pretrained("facebook/bart-large-cnn")

def get_bart_response(model, tokenizer, input_text, prompt):
    input_ids = tokenizer.encode(input_text + prompt, return_tensors="pt", max_length=1024, truncation=True)
    attention_mask = input_ids != tokenizer.pad_token_id
    output = model.generate(input_ids, attention_mask=attention_mask, max_length=200, num_beams=4, length_penalty=2.0)
    response = tokenizer.decode(output[0], skip_special_tokens=True)
    return response
