from base import TestRequest

n = TestRequest()

if __name__ == '__main__':
    print(n.get('/v2/bot/message/quota').json())
