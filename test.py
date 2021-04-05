#!/usr/bin/python
# -*- coding:utf-8 -*-


class B64:
    @staticmethod
    def encoding():
        import base64
        with open('deer.jpg', 'rb') as image:
            image_read = image.read()
            image_64_encode = base64.b64encode(image_read)
        return image_64_encode

    @staticmethod
    def decoding(image_64_encode):
        import base64
        with open('deer_decode.jpg', 'wb') as image_result:
            image_64_decode = base64.b64decode(image_64_encode)
            image_result.write(image_64_decode)


class MD5:
    @staticmethod
    def encoding(data):
        import hashlib
        return hashlib.md5(data.encode(encoding='UTF-8')).hexdigest()


if __name__ == '__main__':
    # e = B64.encoding()
    # B64.decoding(e)

    r = MD5.encoding("你好,世界!")  # 05b5ed5730cdd55cf4b0b4863305dbea
    print(r)
