import socket
import re
from urllib import parse, request
from dotenv import load_dotenv
#from googleapiclient.discovery import build
#try
load_dotenv()

def genPrefix(largo):
    num=str(largo+5)
    while(len(num)<5):
        num= "0"+num
    return num+"ytser"

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 5000        # Port to listen on (non-privileged ports are > 1023)
"""KEY_YT = os.getenv('KEY_YT')    #Youtube api key
tag = "" 

youtube = build('youtube', 'v3', developerKey = KEY_YT)"""

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.send(b'00010sinitytser')
    s.recv(4096)
    print('Servicio youtube iniciado')
    while True:
        data = s.recv(4096)
        tag = data[10:].decode()
        print(tag+" este es este")

        query_string = parse.urlencode ({'search_query': tag})
        html_content = request.urlopen ('http://www.youtube.com/results?'+query_string)
        search_results = re.findall( r"watch\?v=(\S{11})", html_content.read().decode())


        """request = youtube.search().list(
            part='snippet',
            maxResults= 1,
            order = 'relevance',
            q = tag,
            type = 'video'
            )
            
        response = request.execute    """

        print(query_string)
        print("------------------------")
        print(search_results)
        videoid = search_results[0]
        prefix=genPrefix(len(videoid))
        print(prefix+videoid)
        s.send((prefix+videoid).encode("utf-8"))