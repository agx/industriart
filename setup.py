#!/usr/bin/python
# vim: set fileencoding=utf-8 :
#
# Copyright (C) 2014 Guido Günther <agx@sigxcpu.org>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
# END OF COPYRIGHT #

from setuptools import setup

setup(name = "industriart",
      version = '0.0.1',
      author = u'Guido Günther',
      author_email = 'agx@sigxcpu.org',
      packages = ['industriart'],
      install_requires=['requests>=1'],
      setup_requires=['nose>=0.11.1','mock>=1.0.1'],
)
