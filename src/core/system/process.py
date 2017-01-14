# -*- coding: utf-8 -*-

"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Development Team: Stanislav Menshov
"""

import subprocess
import os

from .exceptions import SystemError


class Process:
    """Process class"""

    @staticmethod
    def system(command):

        """
        Call OS command

        :param str command: os command
        :raise SystemError
        :return: dic
        """

        try:
            os.system(command)
        except OSError as e:
            raise SystemError(e)

    @staticmethod
    def execute(command):
        """
        Excecute OS command

        :param str command: os command
        :raise SystemError
        :return: dic
        """
        try:
            pr = subprocess.Popen(command, cwd=os.getcwd(),
                                  shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            (out, error) = pr.communicate()
            if pr.returncode != 0:
                raise OSError(error.strip())

            return out
        except (subprocess.CalledProcessError, OSError) as e:
            raise SystemError(e)
