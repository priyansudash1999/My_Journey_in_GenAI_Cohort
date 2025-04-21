import tiktoken

encoder = tiktoken.encoding_for_model('gpt-4')

print('vocab size ', encoder.n_vocab)

text = 'I am Priyansu'
tokens = encoder.encode(text)

print('tokens', tokens)

decoded = encoder.decode(tokens)
print(f"decoded:-  {decoded}")