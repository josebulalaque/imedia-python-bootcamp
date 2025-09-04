class ImageFileValidator:
    def __init__(self, path):
        self.path = path

    def valid(self):
        return (
                self.path.endswith('.jpg')
                or self.path.endswith('.jpeg')
                or self.path.endswith('.png')
        )


class DocumentValidator:
    def __init__(self, path, pages):
        self.path = path
        self.pages = pages

    def valid(self):
        return self.path.endswith('.docx') and self.pages > 0


class AudioFileValidator:
    def __init__(self, path, length):
        self.path = path
        self.length = length

    def valid(self):
        return self.length > 0 and (
                self.path.endswith('.mp3')
                or self.path.endswith('.wav')
        )


class VideoFileValidator:
    def __init__(self, path, length, resolution):
        self.path = path
        self.length = length
        self.resolution = resolution

    def valid(self):
        return (
                self.path.endswith('.mp4')
                and (self.resolution == "720" or self.resolution == "1080")
                and self.length > 0
        )
