# coding: utf-8
__author__ = 'soshial'

import num_base,re

class NumEn(num_base.NumBase):
    def __init__(self,language,logger):
        super(NumEn,self).__init__(language,logger)
        self.decades = {"'20s":"twenties","1920s":"twenties","'30s":"thirties","1930s":"thirties","'40s":"fourties","1940s":"fourties",
                     "'50s":"fifties","1950s":"fifties","'60s":"sixties","1960s":"sixties","'70s":"seventies","1970s":"seventies",
                     "'80s":"eighties","1980s":"eighties","'90s":"nineties","1990s":"nineties"}
        self.from_to = u"from/to"
        self.endings = [u"-year-old",u"-pound",u"-foot",u"-acre",u"-year",u"-liter",u"-litre",u"-step",u"-yard",
                               u"-day",u"-hour",u"-month-old",u"-month",u"-million",u"-week",u"-mile",u"-plus",u"-point",
                               u"-minute",u"-inch",u"-degrees",u"-second"]
        self.months = ['January','February','March','April','June','July','August','September','October','November','December']
        self.plus = u"/plus"
        self.degree = u"degree/s"
        self.number = u"number"

    def ordinals(self,str):
        if re.search("^\d*(1st|2nd|3rd|[4567890]th|11th|12th|13th)$",str):
            return self.num2words.to_ordinal(self.get_canonical_number_from_string(re.sub('\D','',str)))
        else: return False

    def percentage(self,number,power=0):
        percent = ["percent","per mille","basis point"]
        return self.num2words.to_cardinal(number) + " " + percent[power]

    def other(self,str):
        if str == "24/7": return "twenty-four seven"
        elif str == "9/11": return "nine-eleven"
        elif str == "3D": return "three-d"
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