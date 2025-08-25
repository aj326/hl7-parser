from hl7apy.parser import parse_message
from hl7 import parse,Component
msg=''
with open('sample_01.txt','r') as file:
    msg=file.read()
# print(msg)
msg=msg.replace("\n","\r")
message = parse_message(msg)
h = parse(msg)
# print(message.children)
# for m in message.children:
#     print(m.children)

# print(message.MSH.MSH_3[0])
print(h['MSH.F3.R1'])
print(h['MSH.F4.R1.C2'])
# print(h.segment('MSH')(4)(1))
# extract_field(segment, segment_num=1, field_num=1, repeat_num=1, component_num=1, subcomponent_num=1)
print(len(h['PID'][0][5][0]))
for n in h['PID'][0][5][0]:
    if n[0] !="": print(n,type(n))
print(h['ORC'])
print(h['OBX'])