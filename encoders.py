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
        "cmd":{
            "command":"cmd_command",
            "powershell":"cmd_powershell",
            "powershellhidden":"cmd_powershellhidden",
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





def cmd_command(string):
    pbase = 'python3 -c "PLACEHOLDER"'
    return pbase.replace('PLACEHOLDER', string)
def cmd_powershell(string):
    pbase = 'powershell.exe python3 -c "PLACEHOLDER"'
    return pbase.replace('PLACEHOLDER', string)
def cmd_powershellhidden(string):
    pbase = 'powershell.exe -windowstyle hidden python3 -c "PLACEHOLDER"'
    return pbase.replace('PLACEHOLDER', string)

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
