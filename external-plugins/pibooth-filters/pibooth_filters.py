import os.path as osp

import pibooth
from pibooth.filters import filter_controller
from pibooth.utils import timeit

__version__ = "0.0.1"


@pibooth.hookimpl
def pibooth_configure(cfg):
    """Declare the new configuration options"""
    cfg.add_option('FILTERS', 'filters_list', "('GrayScale')", "Filters enabled")


@pibooth.hookimpl
def state_processing_do(self, cfg, app):
    with timeit("Saving filtered raw captures"):
        captures = app.camera.get_captures()

        for savedir in cfg.gettuple('GENERAL', 'directory', 'path'):
            rawdir = osp.join(savedir, "raw", app.capture_date)

            for capture in captures:
                count = captures.index(capture)
                # img_path = osp.join(rawdir, "pibooth{:03}.jpg".format(count))
                filter_controller.pilgram_aden(capture, osp.join(rawdir, "pibooth{:03}-aden.jpg".format(count)))
                # filter_controller.im_color_temp(4000, img_path, osp.join(rawdir, "pibooth{:03}-filter.jpg".format(count)))
