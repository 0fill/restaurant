
class Test():
    def method(self):
        print("Test")

    def est(self):
        Test.method(self)

t = Test()
t.est()