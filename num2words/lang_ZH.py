# -*- coding: utf-8 -*-
# Copyright (c) 2003, Taro Ogawa.  All Rights Reserved.
# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.
# Copyright (c) 2017, Yanqing Sun.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from __future__ import division, unicode_literals, print_function
from .base import Num2Word_Base

class Num2Word_ZH(Num2Word_Base):
    def set_high_numwords(self, high):
        max = 4 * len(high)
        for word, n in zip(high, range(max, 0, -4)):
            self.cards[10**n] = word

    def setup(self):
        self.negword = u"负 "
        self.pointword = u"点"
        self.errmsg_nornum = "Only numbers may be converted to words."
        self.exclude_title = [u"正", u"点", u"负"]

        self.high_numwords = [u"万", u"亿", u"兆", u"京", u"垓", u"秭", u"穰", u"沟", u"涧", u"正", u"载"]
        self.high_numwords.reverse()
        self.mid_numwords = [(1000, u"千"), (100, u"百"),
                             (90, u"九十"), (80, u"八十"), (70, u"七十"),
                             (60, u"六十"), (50, u"五十"), (40, u"四十"),
                             (30, u"三十")]
        self.low_numwords = [u"二十", u"十九", u"十八", u"十七",
                             u"十六", u"十五", u"十四", u"十三",
                             u"十二", u"十一", u"十", u"九", u"八",
                             u"七", u"六", u"五", u"四", u"三", u"二",
                             u"一", u"零"]
        self.ords = {  }


    def merge(self, lpair, rpair):
        ltext, lnum = lpair
        rtext, rnum = rpair
        if lnum == 1 and rnum < 100:
            return (rtext, rnum)
        elif 100 > lnum > rnum :
            return (u"%s%s"%(ltext, rtext), lnum + rnum)
        elif lnum >= 1000 > 100 > rnum:
            if 10 < rnum < 20: rtext = u"一" + rtext
            return (u"%s 零 %s"%(ltext, rtext), lnum + rnum)
        elif lnum >= 100 > rnum:
            if rnum < 10: return (u"%s 零 %s"%(ltext, rtext), lnum + rnum)
            elif rnum < 20: return (u"%s 一%s"%(ltext, rtext), lnum + rnum)
            else: return (u"%s %s"%(ltext, rtext), lnum + rnum)
        elif rnum > lnum:
            return (u"%s%s"%(ltext, rtext), lnum * rnum)
        return ("%s %s"%(ltext, rtext), lnum + rnum)


    def to_ordinal(self, value):
        self.verify_ordinal(value)
        outwords = self.to_cardinal(value)
        return u"第" + outwords


    def to_ordinal_num(self, value):
        self.verify_ordinal(value)
        return u"第%s"%(value)


    def to_year(self, val, longval=True):
        if not (val//100)%10:
            return self.to_cardinal(val)
        return self.to_splitnum(val, hightxt=u"", jointxt="",
                                longval=longval)

    def to_currency(self, val, longval=True):
        return self.to_splitnum(val, hightxt=u"元", lowtxt=u"分",
                                divisor=1, jointxt="and", longval=longval, cents = True)


n2w = Num2Word_ZH()
to_card = n2w.to_cardinal
to_ord = n2w.to_ordinal
to_ordnum = n2w.to_ordinal_num
to_year = n2w.to_year

def main():
    for val in [ 1, 11, 12, 21, 31, 33, 71, 80, 81, 91, 99, 100, 101, 102, 155,
             180, 300, 308, 832, 1000, 1001, 1061, 1100, 1500, 1701, 3000,
             8280, 8291, 150000, 500000, 1000000, 2000000, 2000001,
             -21212121211221211111, -2.121212, -1.0000100]:
        n2w.test(val)
    n2w.test(1325325436067876801768700107601001012212132143210473207540327057320957032975032975093275093275093270957329057320975093272950730)
    for val in [1,120,1000,1120,1800, 1976,2000,2010,2099,2171]:
        print(val, "is", n2w.to_currency(val))
        print(val, "is", n2w.to_year(val))


if __name__ == "__main__":
    main()
