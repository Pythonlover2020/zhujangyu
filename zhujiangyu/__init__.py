code = ['utf-8','gbk','cp936','gb2312']
def decode(text):
    '''
    该函数用于解码
    :param text: 要解码的文本
    :return: 解码后的文本
    '''
    for each in code:
        try:
            new_text = text.decode(each)
        except UnicodeDecodeError:
            continue
        else:
            return new_text