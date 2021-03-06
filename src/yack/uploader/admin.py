# -*- coding: utf-8 -*-
"""
 Copyright (c) 2011 Frédéric Bertolus.

 This file is part of Yack.
 Yack is free software: you can redistribute it and/or modify it
 under the terms of the GNU Affero General Public License as published by the
 Free Software Foundation, either version 3 of the License, or (at your
 option) any later version.

 Yack is distributed in the hope that it will be useful, but WITHOUT
 ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for
 more details.
 You should have received a copy of the GNU Affero General Public License along
 with Yack. If not, see http://www.gnu.org/licenses/.
"""

from yack.uploader.models import YackPack
from yack.uploader.models import YackFile
from yack.uploader.models import YackFilePart
from yack.uploader.models import YackFileSubPart
from django.contrib import admin

admin.site.register(YackPack)
admin.site.register(YackFile)
admin.site.register(YackFilePart)
admin.site.register(YackFileSubPart)
