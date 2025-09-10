import base64


class Decoding_words:
    def __init__(self):
        self.dangerous_words = 'R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT'
        self.less_dangerous_words = 'RnJlZWRvbSBGbG90aWxsYSxSZXNpc3RhbmNlLExpYmVyYXRpb24sRnJlZSBQYWxlc3RpbmUsR2F6YSxDZWFzZWZpcmUsUHJvdGVzdCxVTlJXQQ=='

    def get_less_dangerous_words(self):
        return self.decoding_less_dangerous_words()

    def get_dangerous_words(self):
        return self.decoding_dangerous_words()


    def decoding_dangerous_words(self):
        encoded_bytes = self.dangerous_words.encode('utf-8')
        decoded_bytes = base64.b64decode(encoded_bytes)
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string

    def decoding_less_dangerous_words(self):
        encoded_bytes = self.less_dangerous_words.encode('utf-8')
        decoded_bytes = base64.b64decode(encoded_bytes)
        decoded_string = decoded_bytes.decode('utf-8')
        return decoded_string

