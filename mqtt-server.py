import paho.mqtt.client as mqtt
import paho.mqtt.publish as publish
import json
from myutil import d2s

map1={"2024010":"Aeternum",
"2076086":"Virtus",
"2076169":"Sapientia",
"2071070":"Veritas",
"2171007":"Libertas",
"2171060":"Pax",
"2170016":"Fortuna",
"2230006":"Gloria",
"2271001":"Animus",
"2371104":"Tempus",
"2372125":"Caritas",
"2372155":"Corpus",
"2403074":"Lumen",
"2495025":"Domus",
"2433001":"Scientia",
"2431047":"Nox",
"2466005":"Amor",
"2466018":"Fatum",
"2476044":"Bellum",
"2476341":"Silva",
"2492023":"Mare",
"2492039":"Terra",
"2549091":"Caelum",
"2570002":"Ignis",
"2512053":"Aqua",
"2548044":"Vita",
"2544021":"Mors",
"2564060":"Homo",
"2564096":"Deus",
"2564120":"Fides",
"2568019":"Spes",
"2566019":"Malum",
"2593089":"Bonum",
"2593299":"Lex",
"2599140":"Rex"}

# MQTT 브로커 설정
broker_address = "damoa.io"  # MQTT 브로커 주소 (필요시 변경)
port = 1883                   # 기본 MQTT 포트
topic = "ewha/iot/ask"        # 구독할 토픽

# 연결 성공 시 호출되는 콜백 함수
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # 연결 성공 후 토픽 구독
    client.subscribe(topic)
    print(f"Subscribed to topic: {topic}")

# 메시지 수신 시 호출되는 콜백 함수
def on_message(client, userdata, msg):
    # 수신된 메시지 출력
    payload = msg.payload.decode("utf-8")
    print(f"Received message on topic '{msg.topic}': {payload}")
    try:
        j=json.loads(payload)
    except:
        j={}
        print("json error", payload)
        
    with open("log.txt","a") as f:
        h=j.get('hakbun','XX')
        if h not in map1:
            print(d2s(), msg.topic, payload, "incorrect hakbun", file=f)
        else:
            print(d2s(), msg.topic, payload, file=f)
            publish.single(f'ewha/iot/{h}', f'제출할 값은 {map1[h]}  입니다.')

# MQTT 클라이언트 생성
client = mqtt.Client()

# 콜백 함수 설정
client.on_connect = on_connect
client.on_message = on_message

# MQTT 브로커에 연결
client.connect(broker_address, port, 60)

# 메시지 루프 시작 (네트워크 트래픽을 처리하고 콜백 함수 호출)
try:
    print(f"Connecting to MQTT broker at {broker_address}:{port}...")
    client.loop_forever()
except KeyboardInterrupt:
    print("Disconnecting from broker")
    client.disconnect()
