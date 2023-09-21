import torch
from transformers import BertTokenizer, BertForQuestionAnswering
import docx
from transformers_paraphrase import Paraphraser

# Load the BERT model and tokenizer
model_name = "bert-base-uncased"
model = BertForQuestionAnswering.from_pretrained(model_name)
tokenizer = BertTokenizer.from_pretrained(model_name)

# Load the paraphraser model
paraphraser = Paraphraser.from_pretrained("bert-base-uncased")

# Load the Word document
document_path = "your_document.docx"
doc = docx.Document(document_path)

# Extract text from the Word document
custom_text = ""
for paragraph in doc.paragraphs:
    custom_text += paragraph.text + "\n"

# Define a question to ask
question = "What is the main topic of this document?"

# Tokenize the input
inputs = tokenizer(question, custom_text, return_tensors="pt")

# Get the answer start and end positions
start_positions, end_positions = model(**inputs)

# Convert the token IDs to tokens
answer_tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0][start_positions:end_positions + 1])
answer = tokenizer.decode(answer_tokens)

print(f"Question: {question}")
print(f"Original Answer: {answer}")

# Paraphrase the answer to make it sound more natural
paraphrased_answer = paraphraser.paraphrase(answer)

print(f"Paraphrased Answer: {paraphrased_answer}")
