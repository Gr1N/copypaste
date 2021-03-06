copypaste
=========

Platform independent copy + paste library for Python
This library is easier and more powerful than [xerox](https://github.com/kennethreitz/xerox), I think :).

Supported:

* OS X (pbcopy + pbpaste)
* Linux (required [xclip](http://sourceforge.net/projects/xclip/))
* Windows (required [pywin32](http://sourceforge.net/projects/pywin32/) or [IronPython](http://ironpython.codeplex.com))

Install
-------

```shell
pip install copypaste
```

Usage
-----

```python
>>> from copypaste import copy, paste
>>>
>>> copy('I\'m here to make web a better place!!')
>>> paste()
"I'm here to make web a better place!!"
>>>
>>> # Only for UNIX like systems you can specify your own command for copy and paste
>>> copy('I\'m here to make web a better place!!', cmd=['xsel', '-pi'])
>>> paste(cmd=['xsel', '-o'])
"I'm here to make web a better place!!"
>>>
```

Command line usage
------------------

```shell
% copy "I'm here to make web a better place!!"
% paste
I'm here to make web a better place!!
%
% echo I\'m here to make web a better place!! | copy
% paste
I'm here to make web a better place!!
%
```

License
-------

*copypaste* is licensed under the MIT license. See the license file for details.
