from base import TestRequest

n = TestRequest()

if __name__ == '__main__':
    post_data = {
        "messages": [
            {
                "type": "text",
                "text": "Hello world"
            }
        ]
    }
    print(n.post('/v2/bot/message/broadcast', post_data).json())
