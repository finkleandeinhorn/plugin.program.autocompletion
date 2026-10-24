# -*- coding: utf8 -*-

# Copyright (C) 2015 - Philipp Temminghoff <phil65@kodi.tv>
# This program is Free Software see LICENSE file for details

import json
import sys

import xbmc
import xbmcaddon
import xbmcgui

ADDON = xbmcaddon.Addon()
ADDON_VERSION = ADDON.getAddonInfo('version')


def select_suggestion():
    """Put the chosen suggestion into the open virtual keyboard and focus Done."""
    home = xbmcgui.Window(10000)
    text = home.getProperty('AutoCompletion.Selection')
    home.clearProperty('AutoCompletion.Selection')
    if not text:
        return
    xbmc.executeJSONRPC(json.dumps({
        "jsonrpc": "2.0", "id": 1, "method": "Input.SendText",
        "params": {"text": text, "done": False},
    }))
    xbmc.executebuiltin('SetFocus(300)')


xbmc.log("version %s started" % ADDON_VERSION)
if len(sys.argv) > 1 and sys.argv[1] == 'select':
    select_suggestion()
else:
    ADDON.openSettings()
xbmc.log('finished')
