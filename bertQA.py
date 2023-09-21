import torch
from transformers import BertTokenizer, BertForQuestionAnswering


model_name = "bert-base-uncased"
model = BertForQuestionAnswering.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(model_name)
#iss dataset ko aur badha sakta hai tu chahe to par phir tokenizer ko modify karna padega aur model ko bhi.
custom_text = """
Hi I'm abhishek mehtaari ka I can do anything you want me to do for you.
"""

# Define a question to ask
question = "What abhishek can do?"

inputs = tokenizer(question, custom_text, return_tensors="pt")

# Get the answer start and end positions
start_positions, end_positions = model(**inputs)
start_positions = torch.argmax(start_positions)

answer_tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][start_positions:end_positions + 1])
answer = tokenizer.decode(answer_tokens)

print(f"Question: {question}")
print(f"Answer: {answer}")
