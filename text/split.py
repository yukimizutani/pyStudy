# input = 'infotest_20180420-20180420-181123-admin.txt'
# out = 'threats.csv'
# values = []
# count = 0
# cols = []
#
# output = open(out, 'w')
# with open(input) as f:
#     for k, l in enumerate(f):
#         # if k == 255 or k == 256 or k == 254 or k == 253:
#         #     print(l.rstrip())
#         #     for (i, elem) in enumerate(l.rstrip().split(',')):
#         #         print(i, elem)
#         line = l.rstrip()
#         if 'THREAT' in line and len(line.split(',')) < 80:
#             # count += 1
#             # print(count, len(line.split(',')))
#             for i, elm in enumerate(line.split(',')):
#                 cols.append(elm)
#             output.write(','.join(cols) + '\n')
#             # if lis[22] == '' or lis[22] == 0:
#             #     if not lis[15][:20] in values:
#             #         values.append(lis[15][:20])
#             #         print(lis[15])
#             # for (i, elem) in enumerate(lis):
#             #     print(i, elem)
#             # if i == 22:
#             #     output.write(elem + '\n')
# print(len(values))
# output.close()

inp = 'FUTURE_USE, Receive Time, Serial Number, Type, Threat/Content Type, FUTURE_USE, Generated Time, Source IP, Destination IP, NAT Source IP, NAT Destination IP, Rule Name, Source User, Destination User, Application, Virtual System, Source Zone, Destination Zone, Inbound Interface, Outbound Interface, Log Action, FUTURE_USE, Session ID, Repeat Count, Source Port, Destination Port, NAT Source Port, NAT Destination Port, Flags, Protocol, Action, URL/Filename, Threat ID, Category, Severity, Direction, Sequence Number, Action Flags, Source Location, Destination Location, FUTURE_USE, Content Type, PCAP_ID, File Digest, Cloud, URL Index, User Agent, File Type, X-Forwarded-For, Referer, Sender, Subject, Recipient, Report ID, Device Group Hierarchy Level 1, Device Group Hierarchy Level 2, Device Group Hierarchy Level 3, Device Group Hierarchy Level 4, Virtual System Name, Device Name, FUTURE_USE, Source VM UUID, Destination VM UUID, HTTP Method, Tunnel ID/IMSI, Monitor Tag/IMEI, Parent Session ID, Parent Start Time, Tunnel Type, Threat Category, Content Version, FUTURE_USE'
print(len(inp.split(',')))