import redis

# 使用hash存放
client = redis.Redis(host='192.168.3.155', password='admin')
# 测试数据
client.hset('video_count', 1001, 1)
client.hset('video_count', 1002, 1)

def counter(video_id: int):   
    cc = redis.Redis(host='192.168.3.155', password='admin')
    count_number = cc.hget('video_count', video_id)
    cc.hset('video_count',video_id,int(count_number.decode())+1)
    return count_number

if __name__ == '__main__':

    print(counter(1001).decode())
    print(counter(1001).decode())
    print(counter(1002).decode())
    print(counter(1001).decode())
    print(counter(1002).decode())