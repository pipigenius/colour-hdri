#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, unicode_literals

import numpy as np
import os
import re
from collections import defaultdict

from colour_hdri.constants import DEFAULT_SOURCE_RAW_IMAGE_FORMATS

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2015 - Colour Developers'
__license__ = 'New BSD License - http://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-science@googlegroups.com'
__status__ = 'Production'

__all__ = ['linear_conversion',
           'vivication',
           'path_exists',
           'filter_files']


def linear_conversion(a, in_range, out_range):
    a = np.asarray(a)

    in_min, in_max = in_range
    out_min, out_max = out_range

    return (((a - in_min) / (in_max - in_min)) *
            (out_max - out_min) + out_min)


def vivication():
    return defaultdict(vivication)


def path_exists(path):
    """
    Returns if given path exists.
    :param path: Path.
    :type path: unicode
    :return: Path existence.
    :rtype: bool
    """

    if not path:
        return False
    else:
        return os.path.exists(path)


def filter_files(directory, extensions=DEFAULT_SOURCE_RAW_IMAGE_FORMATS):
    """
    Filters given directory for raw files matching given extensions.
    :param directory: Directory to filter.
    :type directory: unicode
    :param extensions: Extensions to filter.
    :type extensions: tuple or list
    :return: Raw files.
    :rtype: list
    """

    return map(lambda x: os.path.join(directory, x),
               filter(lambda x: re.search('\.({0})$'.format(
                   '|'.join(extensions)), x), sorted(os.listdir(directory))))
