#!/usr/bin/python3
#!/usr/bin/env python
# -*- coding: iso-8859-1 -*-


"""
/******************************************************************************\
| PROGRAM : qt-sshh         VERSION : @version 0.1    AUTHOR: @author tuanhace |
| LANGUAGE: Python 3.9      COMPILER: GCC 4.8.5       IDE   : PyCharm CE       |
| FILE    : @file docopt_test.py                                               |
| DATE    : @date 2023-12-20 15:00                                             |
| NOTE    :                                                                    |
|                                                                              |
|------------------------------------------------------------------------------|
| AUTHORISATION AND DISCLAIMER:                                                |
| * @copyright 2023 - 2023 by The Authors. All rights reserved.                |
|                                                                              |
|   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS        |
|   "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT          |
|   LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR      |
|   A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT       |
|   OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,      |
|   SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT           |
|   LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,      |
|   DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY      |
|   THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT        |
|   (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE      |
|   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.       |
|                                                                              |
|------------------------------------------------------------------------------|
| DESIGN REFERENCE:                                                            |
|                                                                              |
|------------------------------------------------------------------------------|
| DESCRIPTION:                                                                 |
| * @brief                                                                     |
|   Qt SSH Helper                                                              |
|                                                                              |
| * @details                                                                   |
|                                                                              |
|------------------------------------------------------------------------------|
| REVISION HISTORY:                                                            |
|   Ver     Date        Author      Reason                                     |
| * 0.1     2023-12-20  tuanhace    Init                                       |
|                                                                              |
\******************************************************************************/
"""


#==============================[ IMPORT ]==============================#

import unittest

from docopt import *


#==============================[ CONST ]==============================#



#==============================[ SETTINGS ]==============================#



#==============================[ DEFINE ]==============================#



#==============================[ VAR ]==============================#



#==============================[ CLASS ]==============================#

class TestDocopt(unittest.TestCase):
    def test_docopt(self):
        usage_docstr = """SSH Helper

Usage:
    sshh <destination> [-p <port>] [-l <login_name>] [-C] [-X]

Options:
    -h --help           Show this help message and exit
    -V --version        Show the version number and exit
    -p <port>           Port to connect to on the remote host [default: 22]
    -l <login_name>     Specify the user to log in as on the remote machine
    -C                  Request compression of all data
    -X                  Enable X11 forwarding
    -v                  Multiple -v options increase the verbosity. The maximum is 3
    -o <option>         SSH option
"""
        cmdline = 'myserver -CXp22 -l myuser -vvv -a 01 -z26 --yes --aa "ei ei" --zzz="zed zed zed" -oStrictHostKeyChecking=no -o "LogLevel = error" -vvvv'
        _parsed_args, remain_str = docopt(usage_docstr, cmdline.split())
        self.assertEqual(remain_str, '-v -v -v -a 01 -z -2 -6 --yes --aa "ei ei" --zzz="zed zed zed" -oStrictHostKeyChecking=no -o"LogLevel = error" -v -v -v -v')


#==============================[ INTERNAL FUNCTION ]==============================#



#==============================[ API FUNCTION ]==============================#



#==============================[ MAIN ]==============================#

if __name__ == '__main__':
    unittest.main()
