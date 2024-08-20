
import sys

def main():

    left_stack = list(input())  # 초기 문자열은 커서 왼쪽에 위치
    right_stack = []  # 커서 오른쪽은 빈 리스트로 시작

    for _ in range(int(input())):
        command = sys.stdin.readline().split()
        if command[0] == "L"and left_stack:
            right_stack.append(left_stack.pop())
        elif command[0] == "D"and right_stack:
            left_stack.append(right_stack.pop())
        elif command[0] == "B"and left_stack:
            left_stack.pop()
        elif command[0] == "P":
            left_stack.append(command[1])

    # 두 스택을 합쳐서 최종 문자열을 생성
    left_stack.extend(reversed(right_stack))
    print("".join(left_stack))

main()

