from icrawler.builtin import BingImageCrawler, GoogleImageCrawler #google didn't work and I had to use selenium


# we are building cats image detection that's why we put cat here
# if you want some other images then put that name in classes list
classes = ['green apple']
number = 100
# here root directory is find your root directory there u will find
# new file name data in which all images are saved.
for c in classes:
    BingImageCrawler = BingImageCrawler(storage={'root_dir': f'p/{c.replace(" ", ".")}'})
    BingImageCrawler.crawl(keyword=c, filters=None, max_num=100, offset=0)
