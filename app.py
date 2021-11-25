
from flask import Flask, request, render_template
import json
import requests
app = Flask(__name__)
dictionary={
  "long": 0,
  "lat": 0,
  "nf": 0,
  "prx": 0,
  "gt": 0,
  "gr": 0,
  "channel": 0,
  "aclr1": 0,
  "aclr2": 0,
  "carrier": 0,
  "bandwidth": 0
}
headers={'accept': 'application/json', 'Content-Type': 'application/json'}
@app.route('/', methods =["GET", "POST"])

def gfg():
	if request.method == "POST":
		req_channel = request.form.get("chn")
		dictionary["channel"]=req_channel
		req_longitude = request.form.get("lgtd")
		dictionary["long"]=req_longitude
		req_latitude = request.form.get("lat")
		dictionary["lat"]=req_latitude
		req_nf = request.form.get("nf")
		dictionary["nf"]=req_nf
		req_ptx = request.form.get("ptx")
		dictionary["prx"]=req_ptx
		req_gtx = request.form.get("gtx")
		dictionary["gt"]=req_gtx
		req_grx = request.form.get("grx")
		dictionary["gr"]=req_grx
		req_aclr1 = request.form.get("aclr1")
		dictionary["aclr1"]=req_aclr1
		req_aclr2 = request.form.get("aclr2")
		dictionary["aclr2"]=req_aclr2
		jsons=json.dumps(dictionary)
		#return jsons
		r=requests.post('http://maluch.mikr.us:20232/api/v0.1/dsa/register', data=json.dumps(dictionary), headers=headers)
		print(r)
	return render_template("form.html")



if __name__=='__main__':
	app.run()

