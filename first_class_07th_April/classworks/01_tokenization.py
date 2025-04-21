import tiktoken

encoder = tiktoken.encoding_for_model('gpt-4o')

print('Vocab size  ', encoder.n_vocab)

text = 'Priyansu does not eat nonveg.'
tokens = encoder.encode(text)
print(f"tokens - {tokens}")

my_data = encoder.decode(tokens)
print(f"my original text is {my_data}")