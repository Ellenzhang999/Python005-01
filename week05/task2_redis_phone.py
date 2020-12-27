import redis
import time

client = redis.Redis(host='192.168.3.155', password='admin')
SUCC = '发送成功'
FAIL = '1 分钟内发送次数超过 5 次, 请等待 1 分钟'

def sendsms(telephone_number: int, content: str, key=None):
    # 短信发送逻辑, 作业中可以使用 print 来代替
    # 请实现每分钟相同手机号最多发送五次功能, 超过 5 次提示调用方,1 分钟后重试稍后    
    # print(f'client.exist:{client.exists(telephone_number)}')

    if client.exists(telephone_number):

        num = int(client.get(telephone_number).decode())

        if num < 4 :
            # 发送消息
            num += 1
            print (f'phone number：{telephone_number} send no.{num} message in 1 minute:{content}')

            # 添加并设置过期时间 （若不显示设置过期时间，原过期时间不再生效）
            client.set(telephone_number, num)
            client.expire(telephone_number, 5)

            return SUCC

        # 若超过5次，停止发送
        return FAIL

    # 在Expire集合里不存在
    else:
        # 添加并设置过期时间
        client.set(telephone_number, 0)
        client.expire(telephone_number, 5)

        # 发送消息
        print (f'phone number：{telephone_number} send no.0 message in 1 minute:{content}')

        return SUCC

if __name__ == '__main__':
    # print(client.exists(12345654321))
    # client.expire(12345654321, 5)
    # print(client.ttl(12345654321))
    # time.sleep(6)
    # print(client.ttl(12345654321))
    # print(client.exists(12345654321))
    # time.sleep(6)
    # print(client.ttl(12345654321))
    print(sendsms(12345654321, content="hello1"))
    print(sendsms(12345654321, content="hello2") )   
    print(sendsms(12345654321, content="hello3") ) 
    print(sendsms(12345654321, content="hello4"))
    # time.sleep(1)     
    # print(client.ttl(12345654321)) 
    print(sendsms(12345654321, content="hello5"))
    # print(client.ttl(12345654321))
    print(sendsms(12345654321, content="hello6")) 
    print(sendsms(88887777666, content="hello1"))
    print(sendsms(88887777666, content="hello2"))
    # print(client.ttl(12345654321))



    # print(sendsms(12345654321, content="hello1"))
    # print(sendsms(12345654321, content="hello2"))
    # time.sleep(2)
    # # print(f'sleep 2 seconds：{client.exists(12345654321)}')
    # print(sendsms(12345654321, content="hello3"))
    # print(sendsms(12345654321, content="hello4"))
    # time.sleep(6)
    # print(client.ttl(12345654321))
    # # print(f'sleep 5 seconds：{client.exists(12345654321)}')
    # print(sendsms(12345654321, content="hello5"))
    # print(sendsms(12345654321, content="hello6"))

