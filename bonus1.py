from bs4 import BeautifulSoup
import requests
# N1
class Disease:
    def __init__(self, name, ID=None):
        self.ID = ID
        self.name = name

    def __repr__(self):
        return f"{self.name},(id={self.ID})"


class Doctor:
    def __init__(self, Full_name, department=None, patients_list=None):
        if patients_list is None:
            patients_list = []
        self.Full_name = Full_name
        self.department = department
        self.patients_list = list(patients_list)

    def __repr__(self):
        return f"{self.Full_name}, department: {self.department}, patients list:{self.patients_list}"


class Patient:
    def __init__(self, private_number, name, doctor, disease_name: list):
        if disease_name is None:
            disease_name = []
        self.private_number = private_number
        self.name = name
        self.doctor = Doctor(doctor)
        self.disease_name = disease_name

    def __str__(self):
        return f"Hello {self.name}, private number:{self.private_number}, doctor: {self.doctor.Full_name}," \
               f" diseases: {self.disease_name}"

    def diagnose(self, sickness: Disease, doctor: Doctor = None):
        self.disease_name.append(sickness)
        if doctor is not None:
            if len(doctor.patients_list) < 20:
                self.doctor = doctor
                doctor.patients_list.append(self.name)
                return "doctor attached"
            else:
                return "The doctor cannot be attached."
        else:
            return "The sickness has been added to the list"




d1 = Disease("covid", 12)
d2 = Disease("cold", 11)
d3 = Disease("diabetes", 14)
doc1 = Doctor("john stockton", "dentist", ["ani", "giorgi", "taso"])
p1 = Patient(123321, "ani", doc1, [d1, d2])
doc2 = Doctor("laura james", "neurologist", ["nika", "luka"])
print(p1.diagnose(d3, doc2))
print(p1.diagnose(d3))
print(p1)
#N3
response = requests.get("https://finance.yahoo.com/crypto/")
print(response.status_code)
content = response.text
soup = BeautifulSoup(content, "html.parser")
body = soup.find("body")
app = body.find("div",id="app")
reactroot = app.find("div")
cont = reactroot.find("div")
render = cont.find("div",{"class":"render-target-active render-target-default Pos(a) W(100%)"})
bgc = render.find("div",{"class":"Bgc($bg-body) Mih(100%) W(100%) Bgc($layoutBgColor)! finance US"})
ydc = bgc.find("div",{"class":"YDC-Lead"})
ydc_lead = ydc.find("div",{"class":"YDC-Lead-Stack"})
ydc_complete = ydc_lead.find("div",id="YDC-Lead-Stack-Composite")
lead = ydc_complete.find("div",id="Lead-5-ScreenerResults-Proxy")
lead5 = lead.find("section",{"class":"Ta(start) Bxz(bb) Px(20px) Pt(20px) Maw($newGridWidth) Bgc($lv2BgColor) Mx(a)"})
fin = lead5.find("div",{"class":"Pos(r) Pos(r) Mih(265px)"})
scr = fin.find("div",id='scr-res-table')
ovx = scr.find("div",{"class":"Ovx(a) Ovx(h)--print Ovy(h) W(100%)"})
table = ovx.find("table",{"class":"W(100%)"})
tbody = table.find("tbody")
# anu im problemas ki davaxwie tavi mara mere gamichirda da ver gavige