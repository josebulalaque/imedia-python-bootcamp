class ImageFileValidator:
    def __init__(self, path):
        self.path = path

    def valid(self):
        if self.path.endswith(".jpg") or self.path.endswith(".png") or self.path.endswith(".jpeg"):
            return True
        else:
            return False

class DocumentValidator:
    def __init__(self, path, pages):
        self.path = path
        self.pages = pages

    def valid(self):
        if self.path.endswith(".pdf") and self.pages > 0:
            return True
        else:
            return False


class AudioFileValidator:
    def __init__(self, path, length):
        self.path = path
        self.length = length

    def valid(self):
        if (self.path.endswith(".mp3") or self.path.endswith(".wav")) and self.length > 0:
            return True
        else:
            return False


class VideoFileValidator:
    def __init__(self, path, length, res):
        self.path = path
        self.length = length
        self.res = res

    def valid(self):
        if (self.path.endswith(".mp4")
                and (self.res == "720" or self.res == "1080")
                and self.length > 0):
            return True
        else:
            return False


# image1=ImageFileValidator("image.jpg")
# print(image1.valid())
#
# document1=DocumentValidator("document.pdf", 9000)
#
# audio1=AudioFileValidator("audio.mp3",5000)
#
# video1=VideoFileValidator("video.mp4", 7000, "720/1080")

validators = [
    ImageFileValidator("image.jpg"),
    DocumentValidator("document.pdf", 5),
    AudioFileValidator("audio.mp3",5000),
    VideoFileValidator("video.mp4", 7000, "1080")
]

for validator in validators:
    print(validator.valid())