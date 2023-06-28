from fastapi import FastAPI #fastapi 모듈
app = FastAPI()

from fastapi.responses import FileResponse #return값에 파일을 넣을 수 있음
@app.get("/") #주소 접속 시
def file():
    return FileResponse('index.html') #파일 내보내

@app.get("/data") #/docs 하면 내가 뭐 만들었는지 예쁘게 보여줌
def sendData():
    return {'hello' : 1234}


#유저한테 데이터를 받고 싶으면 모델부터 만들어야함
from pydantic import BaseModel
class userModel(BaseModel):
    name : str
    phone : int
'''
@app.post("/send/{model_name:model_phone}")
def UserData(data : userModel): 
    print(data)
    return "전송완료"
'''

@app.get("/send/{usermodel}")
async def UserInput(data:userModel):
    print(data)
    return "전송완?"