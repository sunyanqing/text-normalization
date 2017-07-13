# coding: utf-8
__author__ = 'soshial'

import num_base,re

class NumZh(num_base.NumBase):
    def __init__(self,language,logger):
        super(NumZh,self).__init__(language,logger)
        self.decades = {"'20s":u"20年代","1920s":u"20年代","'30s":"thirties","1930s":"thirties","'40s":"fourties","1940s":"fourties",
                     "'50s":"fifties","1950s":"fifties","'60s":u"六十年代","1960s":"sixties","'70s":"seventies","1970s":"seventies",
                     "'80s":"eighties","1980s":"eighties","'90s":"nineties","1990s":"nineties"}
        self.from_to = u"from/to"
        self.endings = [u"-year-old",u"-pound",u"-foot",u"-acre",u"-year",u"-liter",u"-litre",u"-step",u"-yard",
                               u"-day",u"-hour",u"-month-old",u"-month",u"-million",u"-week",u"-mile",u"-plus",u"-point",
                               u"-minute",u"-inch",u"-degrees",u"-second"]
        self.months = ['January','February','March','April','June','July','August','September','October','November','December']
        self.plus = u" 加 "
        self.degree = u"度"
        self.number = u"第"

    def ordinals(self,str):
        #if re.search("^\d*(1st|2nd|3rd|[4567890]th|11th|12th|13th)$",str):
        return self.num2words.to_ordinal(self.get_canonical_number_from_string(re.sub('\D','',str)))
        #else: return False

    def percentage(self,number,power=0):
        percent = [u"百分之", u"千分之", u"万分之"]
        return percent[power] + u" " + self.num2words.to_cardinal(number)

    def other(self,str):
        if str == "24/7": return u"七天、二十四小时"
        elif str == "9/11": return u"九幺幺"
        elif str == "3D": return u"三D"
        else:
            print u"OTHER!!!_with", str
            self.logger.info("OTHER!!!_with", str)

    def short_endings(self,str):
        return str

    def complex_endings(self,str,number):
        return unicode(self.num2words.to_cardinal(number))+re.sub("\d","",str)

    def temperature(self,number):
        #print "@2"
        return self.num2words.to_splitnum(number,self.degree,divisor=1)

    def is_date_near(self,details):
        if set(self.months) & (set(details['left']) | set(details['right'])): return True

if __name__ == "__main__":
    nw = NumZh('zh', None)
    print nw.temperature(-10)
    print nw.temperature(-21)
