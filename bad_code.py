# ✅ 방법 1: 테스트 누락된 새 코드 (테스트 없음)
def calculate_area(width, height):
    return width * height

def unused_feature():
    a = 1
    b = 2
    c = a + b
    d = c + 3
    e = d * 2
    f = e - 1
    g = f / 2
    h = g + 5
    i = h * 3
    j = i - 7
    k = j + 10
    l = k / 2
    print("Final:", l)

# ✅ 방법 2: 중복 코드 유도 (복붙)
def duplicate_block():
    print("block A")
    print("block B")
    print("block C")
    print("block D")

def duplicate_block_2():
    print("block E")
    print("block F")
    print("block G")
    print("block H")

# ✅ 방법 3: 보안 Hotspot 유발
import os

def delete_files():
    os.system("rm -rf /")  # 위험 명령어
