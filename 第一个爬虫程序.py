url = ("https://v3-web.douyinvod.com/95d4832be59fcca4d7c90e711c673378/6550f026/video/tos/cn/tos-cn-ve-15c001-alinc2/0bbf9a0c58b54bc38ef2acbbf5bb4a5f/?a=6383&ch=4&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=1450&bt=1450&cs=0&ds=3&ft=GN7rKGVVyw3nRKo80mo~xj7ScoApuzGSEvrKK5VzD2o0g3&mime_type=video_mp4&qs=0&rc=NTxnOGk4PGc4NTM7N2kzOkBpM3g3c2k6ZjRsPDMzNGkzM0A1XmAyYzUzXjIxLzE0Y2JgYSMya2RrcjRvb3JgLS1kLTBzcw%3D%3D&btag=e00028000&dy_q=1699799395&l=2023111222295508A24E9694BF9213E6AF")

import requests
res = requests.get(url)
open("五号视频.mp4","wb").write(res.content)


