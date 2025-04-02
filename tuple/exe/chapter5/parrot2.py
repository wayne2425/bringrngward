prompt = "\n Tell me something, and I will repeat it back to you. "
prompt += "\n enter 'quit' to end the prgram. : "

active = True
while active:
    message = input(prompt)

if message == 'quit':
    active = False
else: 
    print(message)
