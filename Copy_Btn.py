import clipboard
def COPY(content):
    try:
        str(content)
        clipboard.copy(content)
    except:
        pass   