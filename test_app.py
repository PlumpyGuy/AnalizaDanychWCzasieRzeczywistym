import subprocess, requests, time
p = subprocess.Popen(["python", "app.py"])
time.sleep(2)

res1 = requests.get("http://127.0.0.1:8000/")
res2 = requests.get("http://127.0.0.1:8000/mojastrona")
res3 = requests.get("http://127.0.0.1:8000/hello")
res4 = requests.get("http://127.0.0.1:8000/hello?name=Sebastian")
responses = [res1, res2, res3, res4]
for i in responses:
    if i.status_code == 200:
        print(i.content.decode())
    else:
        print(f"Błąd: {i.status_code}")
res5 = requests.get("http://127.0.0.1:8000/api/v1.0/predict?num1=3&num2=4")
print(res5.json())

p.kill()
