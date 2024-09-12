import uvicorn
from fastapi import FastAPI
from mod import Age
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods = ["*"],
    allow_headers = ["*"]

)

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/hello")
def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.post("/fetch")
def predict(data: Age ):
    data = data.dict()
    if int(data["age"]) >= 15 and int(data["age"]) <= 25:
     return {"data": ["https://firebasestorage.googleapis.com/v0/b/hacksphere-7fc8c.appspot.com/o/15-25%2FChrisCrossPlainNavyBlueT-Shirt_600x.png?alt=media&token=919023d0-7aa6-4e5d-a164-0a6238d1c074","https://firebasestorage.googleapis.com/v0/b/hacksphere-7fc8c.appspot.com/o/15-25%2Fpng-clipart-printed-t-shirt-polo-shirt-clothing-t-shirt-tshirt-fashion-thumbnail.png?alt=media&token=b23959d7-8236-4fc8-893f-e3bfbcb8348f","https://firebasestorage.googleapis.com/v0/b/hacksphere-7fc8c.appspot.com/o/15-25%2Fpngtree-strong-boy-t-shirt-design-free-vector-png-image_4442436.png?alt=media&token=b8818f41-149b-4d73-92b9-dc68ab16d541","https://firebasestorage.googleapis.com/v0/b/hacksphere-7fc8c.appspot.com/o/15-25%2Ftshirt-example.png?alt=media&token=bb988511-401c-40c3-a91e-ba79ec764266","https://firebasestorage.googleapis.com/v0/b/hacksphere-7fc8c.appspot.com/o/15-25%2Ftshirt1.png?alt=media&token=a497c914-74ed-4ce4-8d0d-28da0a3b8e7d"]}
    if  int(data["age"]) >= 25 and  int(data["age"]) <= 46:
     return {"data": ["https://firebasestorage.googleapis.com/v0/b/hacksphere-7fc8c.appspot.com/o/25-45%2F61ZtOKCs%2BTL._AC_AC_SY350_QL65_.jpg?alt=media&token=37d660db-3f98-46af-af2d-92bc73d65997","https://firebasestorage.googleapis.com/v0/b/hacksphere-7fc8c.appspot.com/o/25-45%2FT-Shirt-2-1.png?alt=media&token=b20d8cb1-2513-429c-9c6e-30e4212062f9","https://firebasestorage.googleapis.com/v0/b/hacksphere-7fc8c.appspot.com/o/25-45%2Fd0192db9-5d30-4646-a98c-aec58414ce74.a42802ae299c9200149511d1923bc094.webp?alt=media&token=e70d2e86-0eb0-4153-bb2a-3280f3c5dff0","https://firebasestorage.googleapis.com/v0/b/hacksphere-7fc8c.appspot.com/o/25-45%2Fimages%20(1).jpeg?alt=media&token=391e1cc6-ca01-46ad-9014-d7ce7305ebab","https://firebasestorage.googleapis.com/v0/b/hacksphere-7fc8c.appspot.com/o/25-45%2Fimages.jpeg?alt=media&token=c2c5f783-3d9e-46d5-a338-d0d0bd0f520d","https://firebasestorage.googleapis.com/v0/b/hacksphere-7fc8c.appspot.com/o/25-45%2Ft-shirt-png-favpng-HiahwLDMBcCVi1gHZEXjxT06q_t.jpg?alt=media&token=2a684a02-ca4f-4369-9e4c-692d7e9d974c","https://firebasestorage.googleapis.com/v0/b/hacksphere-7fc8c.appspot.com/o/25-45%2Fwhite.jpeg?alt=media&token=9a0624e3-3e64-4164-976d-8a59600921fc"]}
    if int(data["age"]) >= 46 and data["age"] <= 60:
     return {"data": ["https://firebasestorage.googleapis.com/v0/b/hacksphere-7fc8c.appspot.com/o/45-60%2Fimages%20(1).jpeg?alt=media&token=cc26afdd-9d4b-4aa7-a716-f7d788e72311","https://firebasestorage.googleapis.com/v0/b/hacksphere-7fc8c.appspot.com/o/45-60%2Fimages%20(2).jpeg?alt=media&token=f481f9c6-6587-4717-8366-92b336ae15ce","https://firebasestorage.googleapis.com/v0/b/hacksphere-7fc8c.appspot.com/o/45-60%2Fimages%20(3).jpeg?alt=media&token=3c6136f2-8c21-4faf-86f7-e03defbdfb70","https://firebasestorage.googleapis.com/v0/b/hacksphere-7fc8c.appspot.com/o/45-60%2Fmens-round-neck-t-shirt.jpg?alt=media&token=4c8e62e9-55f0-4c26-b6b7-4bdaad0fd4bc"]}
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
