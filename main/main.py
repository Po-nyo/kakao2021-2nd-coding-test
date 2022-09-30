from solution import *
from api.kakao_api import KakaoApiRequester

if __name__ == '__main__':
    kakao = KakaoApiRequester()
    # do_nothing(kakao)
    solution(kakao)
    print(kakao.score())

# 시나리오 1번 레코드 (solution)
# {'status': 'finished', 'time': 720, 'failed_requests_count': '88.0', 'distance': '586.3'}
# {'score': 279.9940581232493}

# 시나리오 2번 레코드 (do_nothing)
# {'status': 'finished', 'time': 720, 'failed_requests_count': '1687.0', 'distance': '0.0'}
# {'score': 596.4027149321267}
