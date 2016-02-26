# author: camabeh


class Screenshoter:
    """
    Usage:
    box = (100, 100, 400, 400)
    screenshoter = Screenshoter()
    a = screenshoter.grab((0, 0, 1920, 1080))
    a = a.crop(box)
    a.save('screenshot2.png')
    b = screenshoter.grab()
    b = b.crop(box)
    b.save('screenshot3.png')
    """

    def __init__(self):
        # Windows and OS X
        try:
            from PIL import ImageGrab
        except ImportError:
            pass
        else:
            self.grab = Screenshoter.__grabByPIL

        # Linux
        try:
            from Xlib import display, X
        except ImportError:
            pass
        else:
            self.grab = Screenshoter.__grabByX

    @staticmethod
    def __grabByX(bbox=None):
        from PIL import Image
        from Xlib import display, X

        dsp = display.Display()
        root = dsp.screen().root
        geometry = root.get_geometry()

        if bbox:
            # User supplied region [x1, y1] to [x2, y2]
            x1, y1, x2, y2 = bbox
            x2 -= x1
            y2 -= y1
        else:
            # Full Screen
            x1, y1, x2, y2 = 0, 0, geometry.width, geometry.height

        raw = root.get_image(x1, y1, x2, y2, X.ZPixmap, 0xffffffff)
        img = Image.frombytes("RGB", (x2, y2), raw.data, "raw", "BGRX")
        return img

    @staticmethod
    def __grabByPIL(bbox=None):
        from PIL import ImageGrab

        img = ImageGrab.grab(bbox)
        return img
