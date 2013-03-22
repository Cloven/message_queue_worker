import redis
import urbanairship
import re

r = redis.Redis()

ps = r.pubsub()
ps.subscribe(['clan_chat_outgoing'])

for item in ps.listen():
  packet = str(item['data'])
  match = re.match(r'(.*?)\|(.*?)\|(.*)',packet)
  if match:
#    gamertag = match.group(1)
#    clan = match.group(2)
#    chatmessage = match.group(3)
    print packet
  else:
    print "no match"
