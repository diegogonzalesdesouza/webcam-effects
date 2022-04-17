from yacs.config import CfgNode as CN

_C = CN()

# Image height value in pixels
_C.IMAGE_HEIGHT = 480

# Image WIDTH value in pixels
_C.IMAGE_WIDTH = 640

_C.VIDEO_DEVICE = CN()

# Real video device path
_C.VIDEO_DEVICE.REAL = ""

# Virtual video device path
_C.VIDEO_DEVICE.VIRTUAL = ""

# Inference Device (CPU, GPU)
_C.DEVICE = "CPU"

# Effects list
_C.EFFECTS = []