"""
Constants.py file to declare constants.
"""

from django.utils.translation import ugettext as _


DISC_TYPES = [('distance', _('Distance Driver')),
              ('fairway', _('Fairway Driver')),
              ('midrange', _('Midrange')),
              ('putter', _('Putter')),
             ]

Extras = [('Glow in the Dark', _('Glow in the Dark')),
          ('Float in Water', _('Float in Water')),
          ('beaded', _('Beaded')),
          ('beadless', _('Beadless')),
          ('pre-order', _('Pre-Order')),
          ('New Items', _('New Items'))
         ]

STABILITY = [('very overstable', _('Very Overstable')),
             ('overstable', _('Overstable')),
             ('stable', _('Stable')),
             ('understable', _('Understable')),
            ]

SKILL_LEVEL = [('beginner', _('Beginner')),
               ('intermediate', _('Intermediate')),
               ('advanced', _('Advanced')),
               ('everyone', _('Everyone')),
              ]
