from transformers import GPT2Tokenizer

# Initialize the tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")

text = "This is a string!"

# Tokenize the text
token_ids = tokenizer.encode(text, add_special_tokens=True)

# Output the token IDs
print("Token IDs:", token_ids)

# Convert token IDs back to raw tokens and output them
raw_tokens = [tokenizer.decode([token_id]) for token_id in token_ids]
print("Raw tokens:", raw_tokens)