def validate_pin(pin):
    if len(pin) == 4 and any(i.isalpha() for i in pin) == False:
        return True
    elif len(pin) == 6 and any(i.isalpha() for i in pin) == False:
        return True

    else:
        return False