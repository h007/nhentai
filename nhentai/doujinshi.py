# coding: utf-8
from __future__ import print_function
from tabulate import tabulate
from constant import DETAIL_URL, IMAGE_URL
from logger import logger


class Doujinshi(object):
    def __init__(self, name=None, subtitle=None, id=None, img_id=None, ext='jpg', pages=0):
        self.name = name
        self.subtitle = subtitle
        self.id = id
        self.img_id = img_id
        self.ext = ext
        self.pages = pages
        self.downloader = None
        self.url = '%s/%d' % (DETAIL_URL, self.id)

    def __repr__(self):
        return '<Doujinshi: {}>'.format(self.name)

    def show(self):
        table = [
            ["Doujinshi", self.name],
            ["Subtitle", self.subtitle],
            ["URL", self.url],
            ["Pages", self.pages],
        ]
        logger.info(u'Print doujinshi information\n{}'.format(tabulate(table)))

    def download(self):
        logger.info('Start download doujinshi: %s' % self.name)
        if self.downloader:
            download_queue = []
            for i in xrange(1, self.pages + 1):
                download_queue.append('%s/%d/%d.%s' % (IMAGE_URL, int(self.img_id), i, self.ext))
            self.downloader.download(download_queue, self.id)
        else:
            logger.critical('Downloader has not be loaded')


if __name__ == '__main__':
    test = Doujinshi(name='test nhentai doujinshi', id=1)
    print(test)
    test.show()
    try:
        test.download()
    except Exception as e:
        print('Exception: %s' % str(e))