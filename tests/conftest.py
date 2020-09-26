# -*- coding: utf-8 -*-

import os
import pygame
import pytest

from pibooth.config.parser import PiConfigParser
from pibooth.counters import Counters
from pibooth.pictures import sizing
from PIL import Image


MOCKS_DIR = os.path.join(os.path.dirname(__file__), 'mocks')
CAPTURES_DIR = os.path.join(os.path.dirname(__file__), 'captures')


@pytest.fixture(scope='session')
def captures_portrait():
    return [Image.open(os.path.join(CAPTURES_DIR, 'portrait', img))
            for img in os.listdir(os.path.join(CAPTURES_DIR, 'portrait'))]


@pytest.fixture(scope='session')
def captures_landscape():
    return [Image.open(os.path.join(CAPTURES_DIR, 'landscape', img))
            for img in os.listdir(os.path.join(CAPTURES_DIR, 'landscape'))]


@pytest.fixture(scope='session')
def fond_path():
    return os.path.join(CAPTURES_DIR, 'fond.jpg')


@pytest.fixture(scope='session')
def overlay_path():
    return os.path.join(CAPTURES_DIR, 'overlay.png')


@pytest.fixture(scope='session')
def preview_path():
    return os.path.join(CAPTURES_DIR, 'preview.jpg')


@pytest.fixture(scope='session')
def cfg_path():
    return os.path.join(MOCKS_DIR, 'pibooth.cfg')


@pytest.fixture(scope='session')
def cfg(cfg_path):
    return PiConfigParser(cfg_path, None)


@pytest.fixture
def counters(tmpdir):
    return Counters(str(tmpdir.join('data.pickle')), nbr_printed=0)


@pytest.fixture
def resolution():
    return (1934, 2464)  # Final capture resolution


@pytest.fixture
def window_rect():
    """Return a Rect object for the window (can be totally
    different from the resolution).
    """
    # return pygame.Rect(0, 0, 800, 480)  # Screen Offical 7"
    return pygame.Rect(0, 0, 1920, 1080)  # Screen 1080p Full HD


@pytest.fixture
def preview_rect(window_rect, resolution):
    """Return a Rect object for resizing preview and images
    in order to fit to the defined window.

    (from :py:class:`BaseCamera`)
    """
    border = 50
    res = sizing.new_size_keep_aspect_ratio(resolution,
                                            (window_rect.width - 2 * border,
                                             window_rect.height - 2 * border))
    return pygame.Rect(window_rect.centerx - res[0] // 2,
                       window_rect.centery - res[1] // 2,
                       res[0], res[1])
