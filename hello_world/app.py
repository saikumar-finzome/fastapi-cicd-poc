from fastapi import FastAPI
from mangum import Mangum



app = FastAPI(title='Serverless Lambda FastAPI')




@app.get("/version",  tags=["Endpoint Test"])
def main_endpoint_test():
    return {"message": "Welcome CI/CD Pipeline with GitHub Actions!"}


# to make it work with Amazon Lambda, we create a handler object
lambda_handler = Mangum(app=app)