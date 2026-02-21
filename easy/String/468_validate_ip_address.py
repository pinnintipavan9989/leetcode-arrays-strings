def validIPAddress(queryIP):
    
    if queryIP.count('.') == 3:
        parts = queryIP.split('.')
        for part in parts:
            if not part.isdigit():
                return "Neither"
            if (part[0] == '0' and len(part) > 1) or int(part) > 255:
                return "Neither"
        return "IPv4"
    
    if queryIP.count(':') == 7:
        hex_digits = "0123456789abcdefABCDEF"
        parts = queryIP.split(':')
        for part in parts:
            if len(part) == 0 or len(part) > 4:
                return "Neither"
            for ch in part:
                if ch not in hex_digits:
                    return "Neither"
        return "IPv6"
    
    return "Neither"

examples = [
    "172.16.254.1",                       # IPv4
    "256.256.256.256",                    # Neither ( >255 )
    "192.168.01.1",                       # Neither (leading zero)
    "2001:0db8:85a3:0000:0000:8a2e:0370:7334",  # IPv6
    "2001:db8:85a3::8A2E:037j:7334",       # Neither (invalid char j)
    "1e1.4.5.6"                           # Neither
]

for ip in examples:
    print(ip, "->", validIPAddress(ip))