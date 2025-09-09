import base64

encoded_string  = 'R2Vub2NpZGUsV2FyIENyaW1lcyxBcGFydGhlaWQsTWFzc2FjcmUsTmFrYmEsRGlzcGxhY2VtZW50LEh1bWFuaXRhcmlhbiBDcmlzaXMsQmxvY2thZGUsT2NjdXBhdGlvbixSZWZ1Z2VlcyxJQ0MsQkRT'

encoded_bytes = encoded_string.encode('utf-8')

decoded_bytes = base64.b64decode(encoded_bytes)

decoded_string = decoded_bytes.decode('utf-8')

for i in decoded_string.split(","):
    print(i)