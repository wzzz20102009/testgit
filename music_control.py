from random import random

import uiautomator2 as u2

#ADD NOTES
def start_douyin():
    d.app_start('com.ss.android.ugc.aweme', stop=False)
    d.swipe(400, 900, 400, 600, 0.05)
    # d.swipe_ext('up')
    d.sleep(3)


def start_cloudmusic():
    d.app_start('com.netease.cloudmusic', stop=False)
    d.sleep(2)
    # if d(resourceId='com.netease.cloudmusic:id/nextBtn').exists:
    #     d(resourceId='com.netease.cloudmusic:id/nextBtn').click()
    # 防容错
    if d(resourceId='com.netease.cloudmusic:id/iv_smallAlbumCover').exists:
        d(resourceId='com.netease.cloudmusic:id/iv_smallAlbumCover').click()
        d(resourceId='com.netease.cloudmusic:id/nextBtn').click()

    d.sleep(5)


def start_bili():
    d.app_start('tv.danmaku.bili', stop=False)
    if d(className='android.widget.FrameLayout', description='首页,5之1,标签').exists:
        print('已定位到首页')
        d(resourceId='tv.danmaku.bili:id/quality_root')[0].click()
    if d(resourceId='tv.danmaku.bili:id/comment_icon').exists:
        d.swipe(400, 900, 400, 600, 0.05)
    d.sleep(5)


d = u2.connect('10.0.53.22:5556')
# 查看当前运行app
print(d.info)
d.app_start('com.netease.cloudmusic', stop=True)
d.sleep(3)
d.app_start('com.ss.android.ugc.aweme', stop=True)
d.sleep(3)
d.app_start('tv.danmaku.bili', stop=True)
d.sleep(3)
while True:
    start_cloudmusic()
    start_douyin()
    start_bili()
