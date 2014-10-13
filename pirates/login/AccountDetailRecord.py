from pirates.piratesbase import PiratesGlobals


class SubDetails:
    def __init__(self):
        self.subAccess = PiratesGlobals.AccessFull
        self.subName = 'developer'


class AccountDetailRecord:
    def __init__(self):
        self.playerAccountId = PiratesGlobals.PiratesSubId
        self.subDetails = {self.playerAccountId: SubDetails()}