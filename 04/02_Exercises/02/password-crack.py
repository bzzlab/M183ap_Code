import requests

def Brute_force(sessionID:str, passwordLength:int) -> None:

    url:str = "http://webgoat.test:8080/WebGoat/SqlInjectionAdvanced/register"
    password:str = ""
    headers:dict = {
                    "Host": "webgoat.test:8080",
                    "Content-Length": "123",
                    "Accept": "*/*",
                    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
                    "X-Requested-With": "XMLHttpRequest",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
                    "Origin": "http://webgoat.test:8080",
                    "Referer": "http://127.0.0.1:8080/WebGoat/start.mvc",
                    "Accept-Encoding": "gzip, deflate",
                    "Accept-Language": "en-US,en;q=0.9",
                    "Cookie": f"JSESSIONID={sessionID}",
                    "Connection": "close"
                    }

#??
#??
#??
#??
#??
#??
#??
#??

    print("                 ")
    print("Tom's password is")
    print(password)

if __name__ == "__main__":
    sessionID:str = input("Input your session id:")
    passwordLength:int = int(input("Input Tom's password length:"))
    Brute_force(sessionID, passwordLength)