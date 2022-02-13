# Section02-1 
#파이썬 크롤링 기초
#urllib 사용법 및 기본 스크랩핑

import urllib.request as req 
#파일 URL

img_url ='https://postfiles.pstatic.net/MjAyMDEyMTVfMTg1/MDAxNjA4MDQyMzY0ODAz.VUGUtxbS1hF1ftRzL7mIcRYQQHO6mHBv9MOPa0xNrLwg.9qpCypOByFFr0hwkVKVzyOh4EWDx2N6PiHzFBCJa_ZIg.JPEG.0hoyaho0/IMG_3406.jpg?type=w966'

html_url ='http://google.com'

#다운받을 경로

save_path1 = 'C:/test1.jpg'
save_path2 = 'C:/html_download_test.html'

#예외처리

try:
    file1, header1 = req.urlretrieve(img_url , save_path1)
    file2, header2 = req.urlretrieve(html_url , save_path2)

except Exception as e:
    print('download failed')
    print(e)

else:
    #헤더 정보 출력
    print(header1)
    print(header2)

    #다운로드 파일 정보
    print('filename1 {}'.format(file1))
    print('filename2 {}'.format(file2))
    print()

    print("download is 100 percent clear")
