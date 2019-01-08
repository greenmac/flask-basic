class Test(object):
    def __init__(self, value='hello, world!'):
        self.data = value

# 重构__repr__
class TestRepr(Test):
    def __repr__(self):
        return 'TestRepr(%s)' % self.data

tr = TestRepr()
print(tr)

# 重构__str__
class TestStr(Test):
    def __str__(self):
        return '[Value: %s]' % self.data

ts = TestStr()
print(ts)