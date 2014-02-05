# -*- coding: utf-8 -*-

import sys

import pytest

from copypaste import copy, paste

__all__ = (
    'test_copy_paste',
    'test_copy_paste_with_unknow_copy_command',
    'test_copy_paste_with_unknow_paste_command',
)


PY2 = sys.version_info[0] == 2
PY3 = sys.version_info[0] == 3


if PY2:
    NoSuchFileOrDirectoryException = OSError
elif PY3:
    NoSuchFileOrDirectoryException = FileNotFoundError
else:
    raise NotImplementedError


unix_required = pytest.mark.skipif(
    sys.platform in ('win32', 'cli',),
    reason='requires UNIX like platform'
)


TEST_STRING = 'I\'m here to make web a better place!!'


def test_copy_paste():
    copy(TEST_STRING)
    result = paste()

    assert TEST_STRING == result


@unix_required
def test_copy_paste_with_unknow_copy_command():
    with pytest.raises(NoSuchFileOrDirectoryException):
        copy(TEST_STRING, cmd=['fake_cmd'])


@unix_required
def test_copy_paste_with_unknow_paste_command():
    copy(TEST_STRING)
    with pytest.raises(NoSuchFileOrDirectoryException):
        paste(cmd=['fake_cmd'])
