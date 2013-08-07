#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from ZeroconfService import ZeroconfService

service = ZeroconfService(name="Shumen's avahi web server",
                          port=80,  stype="_http._tcp")
service.publish()

#most of the time you don't have to run avahi-browse, because your browser can probably find these things for itself. Safari can on the Mac, for example - look for the "Bonjour" menu.
#ssh mymachine.local
