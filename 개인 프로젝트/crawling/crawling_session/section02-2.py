#urlopen 함수 기초 사용법


import urllib.request as req
from urllib.error import URLError , HTTPError #예외 처리



#다운로드 경로 및 파일명

path_list = ["C:/test1.jpg" , "C:/index.html"]
#다운로드 리소스

target_url=["http://image.dongascience.com/Photo/2017/03/14900752352661.jpg" , "http://google.com"]

#반복문 사용 시 몇 번째 반복문인지 확인이 필요할 수 있습니다. 이때 사용함
for i,url in enumerate(target_url):
    #예외 처리
    try:
        #실행
        #웹 수신 내용 읽기
        response = req.urlopen(url)

        #수신 내용 읽기
        contents = response.read()

        print("--------------------")

        #상태 정보
        print("header info-{} : {}".format(i , response.info()))
        print("http status code : {}".format(response.getcode()))
        print()
        print("--------------------")
        
        #여기에 담아서 쓰기!
        with open(path_list[i] , 'wb') as c:
            c.write(contents)

    except HTTPError as e:
        print("download failed.")
        print("HTTPError Code : " , e.code)

    except URLError as e:
        print("download failed.")
        print("url error reason: ", e.reason)
#성공
    else:
        print()
        print("Download succeed.")