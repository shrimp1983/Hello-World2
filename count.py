#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os


def count_num(file_path, suffix):
    '''
    :param file_path: the target folder
    :param suffix: such as .jpg | .txt
    :return: The count of specified files with suffix
    '''
    result = os.walk(file_path)
    count = 0
    for root, dirs, files in result:
        for item in files:
            path = os.path.join(root, item)
            if path.endswith(suffix):
                count += 1
    return count
