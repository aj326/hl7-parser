from hl7apy.parser import parse_message
from hl7 import parse
msg=''
with open('sample_01.txt','r') as file:
    msg=file.read()
print(msg)
msg=msg.replace("\n","\r")
message = parse_message(msg)
print(len(parse(msg)))
print(message.children)
for m in message.children:
    print(m.children)

