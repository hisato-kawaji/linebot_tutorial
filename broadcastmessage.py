from base import TestRequest

n = TestRequest()

if __name__ == '__main__':
    post_data = {
        'messages': [
            {
                'type': 'text',
                'text': 'もふもふ'
            },
            {
                'type': 'sticker',
                'packageId': '11537',
                'stickerId': '52002735'
            },
            {
                'type': 'image',
                'originalContentUrl': 'https://images.wallpaperscraft.com/image/nike_logo_sports_lettering_minimalism_42689_1024x1024.jpg',
                'previewImageUrl': 'https://images.wallpaperscraft.com/image/nike_logo_sports_lettering_minimalism_42689_1024x1024.jpg',
                "quickReply": {
                    "items": [
                        {
                            "type": "action",
                            "action": {
                                "type": "cameraRoll",
                                "label": "Send photo"
                            }
                        },
                        {
                            "type": "action",
                            "action": {
                                "type": "camera",
                                "label": "Open camera"
                            }
                        }
                    ]
                }
            }
        ]
    }
    print(n.post('/v2/bot/message/broadcast', post_data).json())
