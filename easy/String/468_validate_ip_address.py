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

