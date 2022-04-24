from flask import Flask, request, jsonify
from classifier import get_prediction
app=Flask(__name__)
@app.route("/predict-digit", methods=["POST"])
def predictdata():
    image=request.files.get("digit")
    prediction= get_prediction(image)
if __name__=="__main__":
    app.run(debug=True)
    