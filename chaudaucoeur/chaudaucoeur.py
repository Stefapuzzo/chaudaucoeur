def chaud_au_coeur(day,month):

    binary_message = "01010110 01101111 01110101 01110011 00100000 01101101 01100101 00100000 01101101 01100001 01101110 01110001 01110101 01100101 01111010 00101100 00100000 01100010 01100001 01110100 01100011 01101000 00100000 00100011 00110100 00110101 00110000 00100000 00100001"
    binary_values = binary_message.split()
    message = ""
    for binary_value in binary_values:
        an_integer = int(binary_value, 2)
        ascii_character = chr(an_integer)
        message += ascii_character

    import datetime
    today = datetime.datetime.now()
    if today.day == 31 and today.month == 8:
        return message

if __name__ == "__main__":
    day, month = 31, 8
    message = chaud_au_coeur(day,month)
    print(message)
