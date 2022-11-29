class FooBase(object):
    def foo(self): pass

class A(FooBase):
    def foo(self):
        super(A, self).foo()
        print 'A.foo()'

class B(FooBase):
    def foo(self):
        super(B, self).foo()
        print 'B.foo()'

class C(A, B):
    def foo(self):
        super(C, self).foo()
        print 'C.foo()'
