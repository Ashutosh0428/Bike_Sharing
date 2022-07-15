from flask import Flask
import sys
from bike.logger import logging
from bike.exception import bikeException
app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        housing = bikeException(e,sys)
        logging.info(housing.error_message)
        logging.info("We are testing logging module")
    return "CI CD pipeline has been established."


if __name__=="__main__":
    app.run(debug=True)