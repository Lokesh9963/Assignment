#Program to open your favourite tv show or movie in ur system using python


class Video(object):
    def __init__(self, path):
        self.path = path

    def play(self):
        from os import startfile
        startfile(self.path)


class Movie_MP4(Video):
    type = 'MP4'


movie = Movie_MP4(r'D:\nirmala convent.mp4')
movie.play()