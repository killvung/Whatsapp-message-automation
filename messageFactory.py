'''
Factory to produce messages
'''
def get_send_header():
    '''
    ==============
    獲鴨自動腥野系統
    ==============
    '''
    return "================\r\n\u7372\u9D28\u81EA\u52D5\u8165\u91CE\u7CFB\u7D71\r\n================\n"

def get_body(*messages):
    result = "\u8FC5\u8272\u8010\u6D74:\r\n----------------\n" #迅色耐浴\n----------------
    if len(messages) == 0:
        return result + "    \u7121\u54A9\u7279\u5225\u5206\u4EAB\n" # 無咩特別分享

    body_part = ""
    for position, message in enumerate(messages):
        body_part += str(position) + ".) "
        body_part += (message + "\n")
    return result + body_part

def get_footer():
    return "================\n\u8DCC\u5C4E\u92EA\u9B3C\u672A\u6557\u8F4E\u6953\n================"

def construct_default_message():
    return get_send_header() + get_body() + get_footer()

def construct_message(*messages):
    return construct_default_message() if len(messages) == 0 else get_send_header() + get_body(*messages) + get_footer()
