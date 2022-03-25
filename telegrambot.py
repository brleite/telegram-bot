import requests

def send_message(chat_id, token, message, parse_mode='html'):
    """Send message to Telegram BOT
    Args:
        chat_id (int): chat_id number: -111111
        token [str]: Token to HTTP API: 11111111:AAAAAAAAA
        message (str): Message 
        parse_mode (str, optional): [Message format 'html' or 'markdown']. Defaults to 'html'.
    Returns:
        str : Response Status Code
    """
    data = {'chat_id':chat_id, 'text':message, 'parse_mode':parse_mode}

    response = requests.post('https://api.telegram.org/bot' + token + '/sendMessage', data, verify=False)

    return response.status_code