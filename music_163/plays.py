import requests
import json


url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_29567189?csrf_token=84b3c0e5c0ae760409e2bd9aa846e00b'
from_data = {
    'params': 'MLzWz05DD2z4tU0RqEmrmZc2L5wKmUHcuJuoLvf0jyNa97rwNiKBnnoDm6mMx5Z0cneP2zHQmwKGhhPdxidEl+cF2XrrNEZ0A4+34uyXUVssG0C9i8Iht4BZprg8VGv/Pl9TZEIncfXp3hJLxDPB9e3ct9aE6iPDFlwu53dMAV70zYkQfg24tYZ4njXjqXeszQoAK7tALhtRwUDJ8+caAf7KdDbq5i2KvambO8rI5/Q=',
    'encSecKey': '93460e090c79df6e133a1f957a9b2f7e7797f7f13560e2b331f667ac9d4929a7facbab4144181c8f82f7558edf015c13a2f8f7726a1336e1692f4f85f40453658f4342ddd80a5fd22cacac5693bb3f622621195c2053af01f172f86ffea5a2d7566a243504c1f6d1c12d5d8f57350eb13270ab201cc5c4c6dffa57be4a59ac4e'
}
from_data = {
    'params': 'MLzWz05DD2z4tU0RqEmrmZc2L5wKmUHcuJuoLvf0jyNa97rwNiKBnnoDm6mMx5Z0cneP2zHQmwKGhhPdxidEl+cF2XrrNEZ0A4+34uyXUVssG0C9i8Iht4BZprg8VGv/Pl9TZEIncfXp3hJLxDPB9e3ct9aE6iPDFlwu53dMAV70zYkQfg24tYZ4njXjqXeszQoAK7tALhtRwUDJ8+caAf7KdDbq5i2KvambO8rI5/Q=',
    'encSecKey': '93460e090c79df6e133a1f957a9b2f7e7797f7f13560e2b331f667ac9d4929a7facbab4144181c8f82f7558edf015c13a2f8f7726a1336e1692f4f85f40453658f4342ddd80a5fd22cacac5693bb3f622621195c2053af01f172f86ffea5a2d7566a243504c1f6d1c12d5d8f57350eb13270ab201cc5c4c6dffa57be4a59ac4e'}
req = requests.post(url, data=from_data)

comment = json.loads(req.text)

# pprint.pprint(comment)
# print(len(comment))
#
# print('hotComments', len(comment['hotComments']), comment['hotComments'])
# print('isMusican', comment['isMusician'])
# print('comments', len(comment['comments']), comment['comments'])
# print('total', comment['total'])
# print('userId', comment['userId'])
# print('topComments', len(comment['topComments']), comment['topComments'])
# print('moreHot', comment['moreHot'])
# print('code', comment['code'])
# print('more', comment['more'])

print('*' * 70, '精彩评论', '*' * 70)
for i in range(0, 15):
    # print(comment['hotComments'][i]['content'])
    if len(comment['hotComments'][i]['beReplied']) > 0:
        print('点赞数：',
              comment['hotComments'][i]['likedCount'],
              comment['hotComments'][i]['content'], '------------>',
              comment['hotComments'][i]['beReplied'][0]['content'])
    else:
        print('点赞数：',
              comment['hotComments'][i]['likedCount'],
              comment['hotComments'][i]['content'].replace('\r', ' '))
print('*' * 70, '最新评论', '*' * 70)
for i in range(20):
    if len(comment['comments'][i]['beReplied']) > 0:
        print('点赞数：',
              comment['comments'][i]['likedCount'],
              comment['comments'][i]['content'], '------------>',
              comment['comments'][i]['beReplied'][0]['content'])
    else:
        print('点赞数：',
              comment['comments'][i]['likedCount'],
              comment['comments'][i]['content'].replace('\r', ' '))
