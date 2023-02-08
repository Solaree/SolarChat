import string, base64, random

def token_api():
    tokens = []
    base64_string = '=='
    sample_string = str(random.randint(000000000000000000, 999999999999999999))

    while base64_string.find('==') != -1:
        sample_string_bytes = sample_string.encode('ascii')
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode('ascii')
    else:
        token = base64_string + '.' + random.choice(string.ascii_letters).upper() + ''.join(
            random.choice(string.ascii_letters + string.digits) for _ in range(5)) + '.' + ''.join(
            random.choice(string.ascii_letters + string.digits) for _ in range(27))
        tokens.append(token)
    return token