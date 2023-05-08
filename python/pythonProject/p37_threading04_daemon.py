import threading, requests, time

"""
Thread class 속성 중 daemon 속성은 sub thread가 daemon thread인지 여부를 지정.
daemon thread는 Background thread로 Main thread가 종료되면 즉시 종료됨.
반면 daemon thread가 아닌 thread는 Main thread와 관계없이 자신의 작업이 끝날때까지 계속 실행되는 특징이 있음.
"""
def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), ' chars')
t = threading.Thread(target=getHtml, args=('http://google.com',))
t.daemon = True
t.start()

while True:
    for _ in range(5):
        time.sleep(1)
    print('### End ###')
    break